#!/usr/bin/env python3
"""
Classe représentant l'ensemble des définitions d'une langue (definitions/<langue>).
"""

import re
from collections import OrderedDict
from dataclasses import replace
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
        # Une traduction se retrouve aussi par le slug de son entrée d'origine : la chronologie et
        # les spécifications citent les slugs français.
        for d in self.definitions:
            if d.source_slug and d.source_slug not in self._by_slug:
                self._by_slug[d.source_slug] = d
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

    @classmethod
    def load_translation(cls, lang: str, source: "Dictionary", root: Optional[Path] = None) -> "Dictionary":
        """Les entrées traduites dans `lang`, avec les métadonnées de leur version d'origine.

        Titre, slug et textes viennent de definitions/<lang>/ ; catégorie, renvois et images
        de l'entrée d'origine (même UUID). Les liens d'images vers le dossier d'origine
        (`../../../fr/<lettre>/<slug>/assets/x.png`) redeviennent `./assets/x.png`, résolus
        dans ce dossier. Une entrée sans traduction n'est pas dans le livre de cette langue.
        """
        from ..config import DEFINITIONS_ROOT
        from . import i18n, translations as tr
        base = (root or DEFINITIONS_ROOT) / lang
        definitions, warnings = [], []
        for e in tr.load_entries(lang, base.parent).values():
            src = source.get_by_uuid(e.uuid)
            if not (e.is_translation and src and e.definition.strip()):
                warnings.append(f"{e.rel} : traduction sans source ou sans texte, ignorée")
                continue
            content = re.sub(r"\]\((?:\.\./)+[a-z]{2}/[a-z0-9]/[^/)]+/assets/", "](./assets/", e.definition)
            definitions.append(replace(
                src, title=e.title, slug=e.slug, path=e.path, assets_dir=src.assets_path, source_slug=src.slug,
                content=i18n.smart_quotes(content), short=i18n.smart_quotes(e.short.strip()) or None,
                english_term=None, french_term=None,
            ))
        return cls(definitions, source.taxonomy, warnings)

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
