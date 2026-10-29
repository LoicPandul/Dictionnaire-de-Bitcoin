#!/usr/bin/env python3
"""
Classe représentant une définition du dictionnaire.
"""

import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml


@dataclass
class Definition:
    """Une entrée de definitions/<langue>/<lettre>/<slug>/."""

    uuid: str
    title: str
    slug: str
    category: str
    content: str            # definition.md : version développée
    path: Path

    short: Optional[str] = None   # courte.md : version courte (None si absente)
    english_term: Optional[str] = None
    french_term: Optional[str] = None
    cross_references: List[str] = field(default_factory=list)
    assets: List[dict] = field(default_factory=list)
    version: Optional[str] = None
    part: Optional[str] = None    # renseignée par Dictionary à partir de la taxonomie
    assets_dir: Optional[Path] = None  # images de l'entrée (celles de la source pour une traduction)
    source_slug: Optional[str] = None  # traduction : slug de l'entrée d'origine

    @classmethod
    def load(cls, directory: Path) -> "Definition":
        """Charge une définition depuis un dossier."""
        metadata_path = directory / "metadata.yaml"
        content_path = directory / "definition.md"
        short_path = directory / "courte.md"

        if not metadata_path.exists():
            raise FileNotFoundError(f"metadata.yaml manquant : {metadata_path}")
        if not content_path.exists():
            raise FileNotFoundError(f"definition.md manquant : {content_path}")

        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = yaml.safe_load(f) or {}

        content = content_path.read_text(encoding="utf-8")
        short = short_path.read_text(encoding="utf-8").strip() if short_path.exists() else None

        return cls(
            uuid=metadata.get("uuid", ""),
            title=metadata.get("title", ""),
            slug=metadata.get("slug", ""),
            category=metadata.get("category", ""),
            content=content,
            path=directory,
            short=short,
            english_term=metadata.get("english_term"),
            french_term=metadata.get("french_term"),
            cross_references=metadata.get("cross_references") or [],
            assets=metadata.get("assets") or [],
            version=metadata.get("version"),
        )

    @property
    def assets_path(self) -> Path:
        return self.assets_dir or self.path / "assets"

    @property
    def credits(self) -> Dict[str, str]:
        """Crédit de chaque image de tiers (champ `credit` de `assets:`), par nom de fichier."""
        return {a["filename"]: str(a["credit"]).strip() for a in self.assets
                if isinstance(a, dict) and a.get("filename") and str(a.get("credit") or "").strip()}

    @property
    def sort_key(self) -> str:
        """Clé de tri alphabétique (sans accents, insensible à la casse)."""
        normalized = unicodedata.normalize("NFKD", self.title)
        return "".join(c for c in normalized if not unicodedata.combining(c)).upper()

    @property
    def first_letter(self) -> str:
        """Première lettre du titre, sans accent (pour le classement)."""
        return self.sort_key[:1]

    def __repr__(self) -> str:
        return f"Definition(title={self.title!r}, slug={self.slug!r})"
