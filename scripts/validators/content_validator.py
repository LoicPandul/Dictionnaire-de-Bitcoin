#!/usr/bin/env python3
"""
Validation des parties qui ne sont pas des définitions : spécifications (BIP, BOLT,
bLIP) et chronologie.
"""

import re
from collections import Counter
from typing import List

from ..core import chronology, specs
from ..core.dictionary import Dictionary

URL_RE = re.compile(r"^https?://\S+$")
MAX_SUMMARY_WORDS = 60
MAX_EVENT_WORDS = 50


def validate_specs(dictionary: Dictionary) -> List[str]:
    errors = []
    linked = set()
    for name, serie in specs.load_all().items():
        ids = Counter(e.id for e in serie.entries)
        for e in serie.entries:
            where = f"[specifications/{name}.yaml {e.id or '?'}]"
            if not e.id:
                errors.append(f"{where} id manquant")
            elif ids[e.id] > 1:
                errors.append(f"{where} id en double")
            if not e.title:
                errors.append(f"{where} title manquant")
            if not e.status:
                errors.append(f"{where} status manquant")
            if not e.summary:
                errors.append(f"{where} summary manquant")
            elif len(e.summary.split()) > MAX_SUMMARY_WORDS:
                errors.append(f"{where} summary de {len(e.summary.split())} mots (max {MAX_SUMMARY_WORDS})")
            if e.url and not URL_RE.match(e.url):
                errors.append(f"{where} url invalide")
            for slug in e.related:
                if dictionary.get_by_slug(slug) is None:
                    errors.append(f"{where} related « {slug} » introuvable")
            if e.definition:
                target = dictionary.get_by_slug(e.definition)
                if target is None:
                    errors.append(f"{where} definition « {e.definition} » introuvable")
                else:
                    linked.add(target.slug)
    for d in dictionary.by_part("specifications"):
        if d.slug not in linked and specs.load_all():
            series = d.slug.split("-")[0]
            if series in specs.SERIES and specs.load_series(series):
                errors.append(f"[{d.slug}] entrée de la partie spécifications reliée à aucun document de specifications/{series}.yaml")
    return errors


def validate_chronology(dictionary: Dictionary) -> List[str]:
    errors = []
    events = chronology.load()
    seen = Counter((e.date, e.title) for e in events)
    for e in events:
        where = f"[chronologie/fr/{e.file} {e.date} {e.title[:40]}]"
        if e.parts is None:
            errors.append(f"{where} date invalide (attendu AAAA-MM-JJ, AAAA-MM ou AAAA)")
        if not e.title:
            errors.append(f"{where} title manquant")
        if not e.text:
            errors.append(f"{where} text manquant")
        elif len(e.text.split()) > MAX_EVENT_WORDS:
            errors.append(f"{where} text de {len(e.text.split())} mots (max {MAX_EVENT_WORDS})")
        if len(set(e.sources)) < 2:
            errors.append(f"{where} moins de deux sources")
        for s in e.sources:
            if not URL_RE.match(s):
                errors.append(f"{where} source qui n'est pas une URL : {s[:60]}")
        for slug in e.related:
            if dictionary.get_by_slug(slug) is None:
                errors.append(f"{where} related « {slug} » introuvable")
        if seen[(e.date, e.title)] > 1:
            errors.append(f"{where} événement en double")
        expected = "avant-2009.yaml" if (e.year or 0) < 2009 else f"{e.year}.yaml"
        if e.parts and e.file != expected:
            errors.append(f"{where} rangé dans {e.file} au lieu de {expected}")
    return errors
