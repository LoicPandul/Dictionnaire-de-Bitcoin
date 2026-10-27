#!/usr/bin/env python3
"""
Modèle du livre : ce qu'une édition imprime, dans quel ordre, avec quels renvois.

Une édition (templates/editions.yaml) est une suite de sections :
  - `dictionary` : une partie de definitions/fr (technique, ecosysteme, personnes), en
    version développée (definition.md) ou courte (courte.md) ;
  - `chronology` : chronologie/fr ;
  - `specs` : une ou plusieurs séries de specifications/ (BIP, BOLT et bLIP, NIP), avec ou
    sans le texte développé des entrées du dictionnaire qui leur sont consacrées.

Les générateurs (PDF, EPUB) ne lisent que ce modèle. Un renvoi n'est imprimé que si sa
cible est présente dans l'édition : chaque cible a une ancre, le slug de son dossier.
"""

from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from ..config import TEMPLATES_DIR
from . import chronology as chronology_mod
from . import specs as specs_mod
from .dictionary import Dictionary, group_by_letter
from .definition import Definition

VERSIONS = ("developpee", "courte")


@dataclass
class Section:
    kind: str                     # dictionary | chronology | specs
    id: str
    title: str
    intro: str = ""
    version: str = "developpee"   # sections dictionary
    letter_pages: bool = False
    letters: "OrderedDict[str, List[Definition]]" = field(default_factory=OrderedDict)
    events: list = field(default_factory=list)
    series: list = field(default_factory=list)     # List[SpecSeries]
    detail: bool = False          # sections specs : imprimer la définition développée liée


@dataclass
class Edition:
    id: str
    title: str
    subtitle: str
    file: str
    sections: list


def load_editions(templates_dir: Optional[Path] = None) -> Dict[str, dict]:
    path = (templates_dir or TEMPLATES_DIR) / "editions.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f).get("editions", {})


def _fallback_series(series: str, dictionary: Dictionary) -> Optional[specs_mod.SpecSeries]:
    """Série construite depuis les définitions quand specifications/<série>.yaml manque."""
    label = specs_mod.SERIES[series]
    prefix = {"bip": "bip-", "bolt": "bolt-", "blip": "blip-"}.get(series)
    if not prefix:
        return None
    docs = []
    for d in dictionary.by_part("specifications"):
        if not d.slug.startswith(prefix):
            continue
        number = d.slug[len(prefix):]
        if not number.isdigit():
            continue
        docs.append(specs_mod.SpecDoc(
            series=series, id=d.title, sort_key=int(number), title="",
            status=[], summary=(d.short or "").strip(), definition=d.slug,
        ))
    if not docs:
        return None
    docs.sort(key=lambda e: e.sort_key)
    return specs_mod.SpecSeries(series=series, label=label, source="", source_commit="", entries=docs)


class Book:
    """Une édition résolue : sections remplies, ancres et renvois calculés."""

    def __init__(self, edition_id: str, dictionary: Dictionary, editions: Optional[Dict[str, dict]] = None):
        editions = editions if editions is not None else load_editions()
        if edition_id not in editions:
            raise ValueError(f"Édition inconnue : {edition_id} (disponibles : {', '.join(editions)})")
        cfg = editions[edition_id]
        self.dictionary = dictionary
        self.taxonomy = dictionary.taxonomy
        self.edition = Edition(
            id=edition_id,
            title=cfg.get("title", "Dictionnaire de Bitcoin"),
            subtitle=cfg.get("subtitle", ""),
            file=cfg.get("file", f"dictionnaire-de-bitcoin-{edition_id}"),
            sections=[],
        )
        self.warnings: List[str] = []
        all_series = specs_mod.load_all()
        events = chronology_mod.load()

        for i, raw in enumerate(cfg.get("sections", [])):
            kind = raw["type"]
            if kind == "dictionary":
                part = self.taxonomy.part(raw["part"]) if self.taxonomy else None
                defs = dictionary.by_part(raw["part"])
                version = raw.get("version", "developpee")
                if version not in VERSIONS:
                    raise ValueError(f"editions.yaml : version inconnue « {version} »")
                if not defs:
                    self.warnings.append(f"section {raw['part']} : aucune entrée, ignorée")
                    continue
                self.edition.sections.append(Section(
                    kind="dictionary", id=raw["part"],
                    title=raw.get("title") or (part.title if part else raw["part"]),
                    intro=(raw.get("intro") or (part.intro if part else "")).strip(),
                    version=version,
                    letter_pages=bool(raw.get("letter_pages", part.letter_pages if part else False)),
                    letters=group_by_letter(defs),
                ))
            elif kind == "chronology":
                if not events:
                    self.warnings.append("chronologie : aucun événement, section ignorée")
                    continue
                self.edition.sections.append(Section(
                    kind="chronology", id=raw.get("id", "chronologie"),
                    title=raw.get("title", "Chronologie"), intro=(raw.get("intro") or "").strip(),
                    events=events,
                ))
            elif kind == "specs":
                loaded = []
                for s in raw["series"]:
                    serie = all_series.get(s) or _fallback_series(s, dictionary)
                    if serie:
                        loaded.append(serie)
                    else:
                        self.warnings.append(f"spécifications {s} : aucune donnée, série ignorée")
                if not loaded:
                    continue
                self.edition.sections.append(Section(
                    kind="specs", id=raw.get("id", "-".join(raw["series"])),
                    title=raw.get("title", " et ".join(s.label for s in loaded)),
                    intro=(raw.get("intro") or "").strip(),
                    series=loaded, detail=bool(raw.get("detail", False)),
                ))
            else:
                raise ValueError(f"editions.yaml : type de section inconnu « {kind} »")

        self.anchors = self._compute_anchors()

    # --- ancres et renvois -------------------------------------------------

    def _compute_anchors(self) -> set:
        anchors = set()
        for s in self.edition.sections:
            if s.kind == "dictionary":
                for defs in s.letters.values():
                    anchors.update(d.slug for d in defs)
            elif s.kind == "specs":
                for serie in s.series:
                    for doc in serie.entries:
                        anchors.add(self.spec_anchor(doc))
                        if doc.definition:
                            anchors.add(doc.definition)
        return anchors

    @staticmethod
    def spec_anchor(doc) -> str:
        return f"spec-{doc.series}-{doc.sort_key}"

    def has_anchor(self, slug: str) -> bool:
        return slug in self.anchors

    def body(self, definition: Definition, section: Section) -> str:
        """Texte à imprimer pour une entrée dans une section donnée."""
        if section.version == "courte":
            return definition.short or ""
        return definition.content

    def cross_references(self, definition: Definition) -> List[Definition]:
        """Renvois de l'entrée dont la cible est imprimée dans l'édition, triés par titre."""
        targets = []
        for ref in definition.cross_references:
            target = self.dictionary.get_by_uuid(ref)
            if target and target.slug != definition.slug and self.has_anchor(target.slug):
                targets.append(target)
        return sorted(targets, key=lambda d: d.sort_key)

    def related(self, slugs: List[str]) -> List[Definition]:
        """Entrées du dictionnaire citées par un événement, si elles sont imprimées."""
        out = []
        for slug in slugs:
            d = self.dictionary.get_by_slug(slug)
            if d and self.has_anchor(d.slug):
                out.append(d)
        return out

    def definition_for(self, doc) -> Optional[Definition]:
        return self.dictionary.get_by_slug(doc.definition) if doc.definition else None

    def entry_count(self) -> int:
        n = 0
        for s in self.edition.sections:
            if s.kind == "dictionary":
                n += sum(len(v) for v in s.letters.values())
        return n
