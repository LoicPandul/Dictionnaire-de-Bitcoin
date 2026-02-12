#!/usr/bin/env python3
"""
Classe représentant le dictionnaire complet.
"""

from pathlib import Path
from typing import Dict, List, Iterator, Optional
from .definition import Definition


class Dictionary:
    """Représente le dictionnaire complet."""

    def __init__(self, definitions: List[Definition], lang: str = "fr"):
        self.definitions = definitions
        self.lang = lang
        self._by_slug: Dict[str, Definition] = {d.slug: d for d in definitions}
        self._by_uuid: Dict[str, Definition] = {d.uuid: d for d in definitions if d.uuid}
        self._by_letter: Dict[str, List[Definition]] = {}
        self._build_letter_index()

    @classmethod
    def load(cls, base_path: Optional[Path] = None, lang: str = "fr") -> "Dictionary":
        """Charge toutes les définitions depuis le système de fichiers."""
        if base_path is None:
            from ..config import DEFINITIONS_DIR
            base_path = DEFINITIONS_DIR

        definitions = []

        # Parcourir chaque dossier de lettre
        for letter_dir in sorted(base_path.iterdir()):
            if letter_dir.is_dir() and len(letter_dir.name) == 1:
                # Parcourir chaque définition dans cette lettre
                for def_dir in sorted(letter_dir.iterdir()):
                    if def_dir.is_dir():
                        try:
                            definition = Definition.load(def_dir)
                            definitions.append(definition)
                        except Exception as e:
                            print(f"[WARNING] Failed to load definition from {def_dir}: {e}")

        return cls(definitions, lang)

    def _build_letter_index(self):
        """Construit l'index par lettre."""
        for definition in self.definitions:
            letter = definition.first_letter
            if letter not in self._by_letter:
                self._by_letter[letter] = []
            self._by_letter[letter].append(definition)

    def get_by_slug(self, slug: str) -> Optional[Definition]:
        """Retourne une définition par son slug."""
        return self._by_slug.get(slug)

    def get_by_uuid(self, uuid: str) -> Optional[Definition]:
        """Retourne une définition par son UUID."""
        return self._by_uuid.get(uuid)

    def get_by_letter(self, letter: str) -> List[Definition]:
        """Retourne toutes les définitions d'une lettre."""
        return self._by_letter.get(letter.upper(), [])

    def letters(self) -> List[str]:
        """Retourne la liste des lettres triées."""
        return sorted(self._by_letter.keys())

    def categories(self) -> List[str]:
        """Retourne la liste des catégories uniques triées."""
        cats = set()
        for d in self.definitions:
            if d.category:
                cats.add(d.category)
        return sorted(cats)

    def search(self, query: str) -> List[Definition]:
        """Recherche des définitions par titre ou contenu."""
        query_lower = query.lower()
        results = []
        for d in self.definitions:
            if query_lower in d.title.lower() or query_lower in d.content.lower():
                results.append(d)
        return results

    def __iter__(self) -> Iterator[Definition]:
        return iter(self.definitions)

    def __len__(self) -> int:
        return len(self.definitions)

    def __getitem__(self, slug: str) -> Optional[Definition]:
        return self.get_by_slug(slug)

    @property
    def total_count(self) -> int:
        """Nombre total de définitions."""
        return len(self.definitions)

    def stats(self) -> dict:
        """Retourne des statistiques sur le dictionnaire."""
        return {
            "total_definitions": self.total_count,
            "letters": len(self._by_letter),
            "categories": len(self.categories()),
            "definitions_per_letter": {
                letter: len(defs) for letter, defs in self._by_letter.items()
            },
        }
