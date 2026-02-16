#!/usr/bin/env python3
"""
Génération de l'INDEX.md.
"""

from pathlib import Path
from ..core.dictionary import Dictionary
from ..config import OUTPUT_INDEX, GITHUB_URL


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère le fichier INDEX.md."""
    if output_path is None:
        output_path = OUTPUT_INDEX

    print(f"Génération de l'index: {output_path}")

    lines = []

    # En-tête
    lines.append("# Index du Dictionnaire de Bitcoin")
    lines.append("")
    lines.append(f"Ce fichier contient la liste de toutes les {dictionary.total_count} définitions du dictionnaire.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table des matières par lettre
    lines.append("## Navigation rapide")
    lines.append("")

    letter_links = []
    for letter in dictionary.letters():
        letter_links.append(f"[{letter}](#{letter.lower()})")

    lines.append(" | ".join(letter_links))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Définitions par lettre
    for letter in dictionary.letters():
        definitions = dictionary.get_by_letter(letter)

        lines.append(f"## {letter}")
        lines.append("")

        for definition in definitions:
            # Lien vers la définition
            rel_path = f"definitions/fr/{letter.lower()}/{definition.slug}/definition.md"
            lines.append(f"- [{definition.title}]({rel_path})")

        lines.append("")

    # Écrire le fichier
    output_path.write_text("\n".join(lines), encoding='utf-8')

    print(f"[OK] Index généré: {output_path} ({dictionary.total_count} entrées)")
    return True
