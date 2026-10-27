#!/usr/bin/env python3
"""
Classe représentant l'ensemble des définitions de definitions/fr.
"""

from collections import OrderedDict
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional

from .definition import Definition
from .taxonomy import Taxonomy


def group_by_letter(definitions: Iterable[Definition]) -> "OrderedDict[str, List[Definition]]":
    """Regroupe des définitions par première lettre, chaque groupe trié par titre."""
    groups: Dict[str, List[Definition]] = {}
    for d in definitions:
        groups.setdefault(d.first_letter, []).append(d)
    return OrderedDict(
        (letter, sorted(groups[letter], key=lambda d: (d.sort_key, d.slug)))
        for letter in sorted(groups)
    )


class Dictionary:
    """Toutes les entrées, indexées par slug et par UUID."""

    def __init__(self, definitions: List[Definition], taxonomy: Optional[Taxonomy] = None,
                 warnings: Optional[List[str]] = None):
        self.definitions = sorted(definitions, key=lambda d: (d.sort_key, d.slug))
        self.taxonomy = taxonomy
        self.warnings = warnings or []
        self._by_slug = {d.slug: d for d in self.definitions}
        self._by_uuid = {d.uuid: d for d in self.definitions if d.uuid}
        if taxonomy:
            for d in self.definitions:
                d.part = taxonomy.part_of(d.category)

    @classmethod
    def load(cls, base_path: Optional[Path] = None, taxonomy: Optional[Taxonomy] = None) -> "Dictionary":
        """Charge toutes les définitions. Ne modifie jamais le disque."""
        if base_path is None:
            from ..config import DEFINITIONS_DIR
            base_path = DEFINITIONS_DIR
        if taxonomy is None:
            taxonomy = Taxonomy.load()

        definitions, warnings = [], []
        for letter_dir in sorted(base_path.iterdir()):
            if not (letter_dir.is_dir() and len(letter_dir.name) == 1):
                continue
            for def_dir in sorted(letter_dir.iterdir()):
                if not def_dir.is_dir():
                    continue
                if not any(def_dir.iterdir()):
                    warnings.append(f"dossier vide : {def_dir.relative_to(base_path)}")
                    continue
                try:
                    definitions.append(Definition.load(def_dir))
                except Exception as e:  # une entrée cassée ne bloque pas le chargement
                    warnings.append(f"{def_dir.relative_to(base_path)} : {e}")
        return cls(definitions, taxonomy, warnings)

    def get_by_slug(self, slug: str) -> Optional[Definition]:
        return self._by_slug.get(slug)

    def get_by_uuid(self, uuid: str) -> Optional[Definition]:
        return self._by_uuid.get(uuid)

    def by_part(self, part: str) -> List[Definition]:
        return [d for d in self.definitions if d.part == part]

    def letters(self) -> List[str]:
        return list(group_by_letter(self.definitions).keys())

    def get_by_letter(self, letter: str) -> List[Definition]:
        return group_by_letter(self.definitions).get(letter.upper(), [])

    def categories(self) -> List[str]:
        return sorted({d.category for d in self.definitions if d.category})

    def __iter__(self) -> Iterator[Definition]:
        return iter(self.definitions)

    def __len__(self) -> int:
        return len(self.definitions)

    @property
    def total_count(self) -> int:
        return len(self.definitions)
