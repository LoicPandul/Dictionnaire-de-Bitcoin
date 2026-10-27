#!/usr/bin/env python3
"""
Validation des traductions (definitions/<langue>/ autres que la langue d'origine) et état
de leur synchronisation avec la langue d'origine.

`validate` retourne les erreurs de structure, qui font échouer `check` : métadonnées,
fichiers manquants, versions courtes, markdown, images. Une traduction en retard ou
manquante n'est pas une erreur : `summary` la compte, `python3 scripts/main.py sync` la
détaille, et `sync --strict` échoue tant qu'il en reste dans le périmètre.
"""

import re
from collections import Counter
from typing import Dict, List, Tuple

from ..core import translations as tr
from ..core.dictionary import Dictionary
from . import sync_checker

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HASH_RE = re.compile(rf"^[0-9a-f]{{{tr.HASH_LEN}}}$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def _check_entry(e: tr.Entry, dictionary: Dictionary, languages: dict) -> List[str]:
    where = f"[{e.lang}/{e.slug}]"
    errors = [f"{where} {p}" for p in e.problems]
    m = e.meta
    if not UUID_RE.match(e.uuid):
        errors.append(f"{where} uuid invalide : {e.uuid!r}")
    if m.get("slug") != e.path.name:
        errors.append(f"{where} le slug ne correspond pas au dossier « {e.path.name} »")
    if not SLUG_RE.match(e.slug):
        errors.append(f"{where} slug invalide")
    elif e.path.parent.name != e.slug[0]:
        errors.append(f"{where} rangé dans « {e.path.parent.name}/ » au lieu de « {e.slug[0]}/ »")
    if not e.title:
        errors.append(f"{where} title manquant")
    elif any(c.islower() for c in e.title):
        errors.append(f"{where} title doit être en MAJUSCULES : « {e.title} »")

    if e.is_translation:
        if m.get("source_lang") not in [languages["source"], *languages["translations"]]:
            errors.append(f"{where} source_lang inconnue : {m.get('source_lang')!r}")
        for k in ("source_hash", "translation_hash"):
            if m.get(k) and not HASH_RE.match(str(m[k])):
                errors.append(f"{where} {k} invalide : {m[k]!r}")
        if e.lang == languages["source"]:
            pass  # traduction vers la langue d'origine : la source est dans une autre langue
        elif dictionary.get_by_uuid(e.uuid) is None:
            errors.append(f"{where} source introuvable : aucun UUID {e.uuid} dans definitions/{m.get('source_lang')}/")
    elif e.lang != languages["source"]:
        # Entrée écrite d'abord dans cette langue : elle porte ses propres métadonnées.
        taxonomy = dictionary.taxonomy
        if not m.get("category"):
            errors.append(f"{where} ni source_lang (traduction) ni category (entrée d'origine)")
        elif taxonomy and m["category"] not in taxonomy.listed:
            errors.append(f"{where} catégorie inconnue : « {m['category']} »")
        for ref in m.get("cross_references") or []:
            if dictionary.get_by_uuid(ref) is None:
                errors.append(f"{where} renvoi vers un UUID inconnu : {ref}")

    if not e.definition.strip():
        errors.append(f"{where} definition.md manquant ou vide")
    if not e.short.strip():
        errors.append(f"{where} courte.md manquant ou vide")
    else:
        errors += [f"{where} courte.md : {p}" for p in sync_checker.check_short(e.short)]
    if re.search(r"^- ", e.definition, re.MULTILINE):
        errors.append(f"{where} listes avec '-' au lieu de '*'")
    lines = e.definition.split("\n")
    for i, line in enumerate(lines[1:], start=1):
        if line.startswith(">") and lines[i - 1].strip() and not lines[i - 1].startswith(">"):
            errors.append(f"{where} citation sans ligne vide avant (ligne {i + 1})")
    for target in IMAGE_RE.findall(e.definition):
        if "://" not in target and not (e.path / target).resolve().exists():
            errors.append(f"{where} image introuvable : {target}")
    return errors


def validate(dictionary: Dictionary) -> List[str]:
    """Erreurs de structure de toutes les langues traduites."""
    languages = tr.load_languages()
    errors: List[str] = []
    for lang in languages["translations"]:
        dirs = tr.all_entry_dirs(lang)
        entries = [tr.Entry.load(lang, d) for d in dirs]
        for key, label in ((lambda e: e.uuid, "uuid"), (lambda e: e.slug, "slug")):
            counts = Counter(key(e) for e in entries)
            errors += [f"[{lang}/{e.slug}] {label} en double" for e in entries if counts[key(e)] > 1]
        for e in entries:
            errors += _check_entry(e, dictionary, languages)
    # Une entrée d'origine peut être la traduction d'une autre langue (source_lang dans definitions/fr).
    for e in tr.load_entries(languages["source"]).values():
        if e.is_translation:
            errors += _check_entry(e, dictionary, languages)
    return errors


def summary(dictionary: Dictionary) -> Dict[str, Tuple[Counter, Dict[str, Counter]]]:
    """Par langue cible : compteur des statuts dans le périmètre, et par partie."""
    languages = tr.load_languages()
    part_of = dictionary.taxonomy.part_of if dictionary.taxonomy else None
    result = {}
    for lang, conf in languages["translations"].items():
        scope = set(conf.get("parts") or [])
        in_scope, by_part = Counter(), {}
        for p in tr.pairs(languages["source"], lang, part_of, exclude=set(conf.get("exclude") or [])):
            by_part.setdefault(p.part or "?", Counter())[p.status] += 1
            if p.status != tr.EXCLUDED and (not scope or p.part in scope or p.status != tr.MISSING):
                in_scope[p.status] += 1
        result[lang] = (in_scope, by_part)
    return result


def describe(lang: str, counts: Counter) -> str:
    total = sum(counts.values()) - counts[tr.ORPHAN]
    done = total - counts[tr.MISSING] - counts[tr.ORIGIN_MISSING]
    parts = [f"{done}/{total} traduites", f"{counts[tr.UP_TO_DATE]} à jour"]
    for status in tr.STATUSES[1:]:
        if counts[status]:
            parts.append(f"{counts[status]} {status}")
    return f"{lang.upper()} : " + ", ".join(parts)
