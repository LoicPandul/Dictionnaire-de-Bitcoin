#!/usr/bin/env python3
"""
Parties du livre et catégories (templates/parts.yaml, templates/categories.yaml).

Chaque catégorie appartient à une seule partie : la partie d'une définition se déduit
de sa catégorie. `categories.yaml` reste la liste de référence (le site lit ses
commentaires comme description des catégories) ; `parts.yaml` range ces catégories
dans les parties et leur associe un pictogramme.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from ..config import TEMPLATES_DIR

# Parties construites à partir de definitions/fr (les autres viennent de specifications/
# et de chronologie/).
DICTIONARY_PARTS = ("technique", "ecosysteme", "personnes", "specifications")


@dataclass
class Part:
    id: str
    title: str
    intro: str = ""
    letter_pages: bool = False
    categories: List[str] = field(default_factory=list)


class Taxonomy:
    """Catégories valides, partie et pictogramme de chaque catégorie."""

    def __init__(self, parts: List[Part], pictograms: Dict[str, str], listed: List[str]):
        self.parts = parts
        self.pictograms = pictograms
        self.listed = listed  # ordre de categories.yaml
        self._part_of = {cat: p.id for p in parts for cat in p.categories}

    @classmethod
    def load(cls, templates_dir: Optional[Path] = None) -> "Taxonomy":
        templates_dir = templates_dir or TEMPLATES_DIR
        with open(templates_dir / "categories.yaml", encoding="utf-8") as f:
            listed = yaml.safe_load(f).get("categories", [])
        with open(templates_dir / "parts.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        parts, pictograms = [], {}
        for raw in data.get("parts", []):
            cats = []
            for c in raw.get("categories", []):
                cats.append(c["name"])
                if c.get("pictogram"):
                    pictograms[c["name"]] = c["pictogram"]
            parts.append(Part(
                id=raw["id"],
                title=raw.get("title", raw["id"]),
                intro=(raw.get("intro") or "").strip(),
                letter_pages=bool(raw.get("letter_pages", False)),
                categories=cats,
            ))
        return cls(parts, pictograms, listed)

    def part_of(self, category: str) -> Optional[str]:
        return self._part_of.get(category)

    def part(self, part_id: str) -> Optional[Part]:
        return next((p for p in self.parts if p.id == part_id), None)

    def pictogram(self, category: str) -> Optional[str]:
        return self.pictograms.get(category)

    def problems(self) -> List[str]:
        """Incohérences entre categories.yaml et parts.yaml."""
        errors = []
        seen = {}
        for p in self.parts:
            if p.id not in DICTIONARY_PARTS:
                errors.append(f"parts.yaml : partie inconnue « {p.id} » (attendu : {', '.join(DICTIONARY_PARTS)})")
            for cat in p.categories:
                if cat in seen:
                    errors.append(f"parts.yaml : « {cat} » est rangée dans {seen[cat]} et dans {p.id}")
                seen[cat] = p.id
        for cat in self.listed:
            if cat not in seen:
                errors.append(f"categories.yaml : « {cat} » n'est rangée dans aucune partie de parts.yaml")
        for cat in seen:
            if cat not in self.listed:
                errors.append(f"parts.yaml : « {cat} » absente de categories.yaml")
        return errors
