#!/usr/bin/env python3
"""
Classe représentant une définition du dictionnaire.
"""

import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Definition:
    """Représente une définition du dictionnaire."""

    uuid: str
    title: str
    slug: str
    category: str
    content: str
    path: Path

    english_term: Optional[str] = None
    french_term: Optional[str] = None
    cross_references: List[str] = field(default_factory=list)
    assets: List[dict] = field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    @classmethod
    def load(cls, directory: Path) -> "Definition":
        """Charge une définition depuis un dossier."""
        metadata_path = directory / "metadata.yaml"
        content_path = directory / "definition.md"

        if not metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
        if not content_path.exists():
            raise FileNotFoundError(f"Definition file not found: {content_path}")

        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = yaml.safe_load(f)

        with open(content_path, "r", encoding="utf-8") as f:
            content = f.read()

        return cls(
            uuid=metadata.get("uuid", ""),
            title=metadata.get("title", ""),
            slug=metadata.get("slug", ""),
            category=metadata.get("category", ""),
            content=content,
            path=directory,
            english_term=metadata.get("english_term"),
            french_term=metadata.get("french_term"),
            cross_references=metadata.get("cross_references", []),
            assets=metadata.get("assets", []),
            created_at=metadata.get("created_at"),
            updated_at=metadata.get("updated_at"),
        )

    def to_markdown(self, format_type: str = "full", base_path: str = "") -> str:
        """
        Convertit la définition en markdown.

        Args:
            format_type: "full" pour le format complet, "body" pour le corps seul
            base_path: Chemin de base pour les liens relatifs
        """
        lines = []

        if format_type == "full":
            # Titre
            lines.append(f"## {self.title}")

            # Catégorie
            if self.category:
                lines.append(f"▪ **{self.category}**")
                lines.append("")

            # Terme anglais/français
            if self.english_term:
                lines.append(f"► ***EN : {self.english_term}***")
                lines.append("")
            elif self.french_term:
                lines.append(f"► ***FR : {self.french_term}***")
                lines.append("")

        # Contenu
        content = self.content

        # Ajuster les chemins des images si nécessaire
        if base_path:
            content = self._adjust_image_paths(content, base_path)

        lines.append(content)

        return "\n".join(lines)

    def _adjust_image_paths(self, content: str, base_path: str) -> str:
        """Ajuste les chemins des images dans le contenu."""
        # Remplacer ./assets/ par le chemin absolu approprié
        pattern = r'!\[\]\(\./assets/([^)]+)\)'
        replacement = f'![]({base_path}/{self.path.name}/assets/\\1)'
        return re.sub(pattern, replacement, content)

    @property
    def first_letter(self) -> str:
        """Retourne la première lettre (pour classement)."""
        import unicodedata
        normalized = unicodedata.normalize('NFKD', self.title)
        first_char = ''.join(c for c in normalized if not unicodedata.combining(c))[0]
        return first_char.upper()

    def has_assets(self) -> bool:
        """Vérifie si la définition a des assets."""
        return len(self.assets) > 0

    def __repr__(self) -> str:
        return f"Definition(title={self.title!r}, slug={self.slug!r})"
