#!/usr/bin/env python3
"""
Génération de l'EPUB via Pandoc.
"""

import os
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime

from ..core.dictionary import Dictionary
from ..config import (
    BASE_DIR, TEMPLATES_DIR, OUTPUT_EPUB, DEFINITIONS_DIR,
    AUTHOR, PROJECT_NAME, PROJECT_SUBTITLE, LICENSE, EPUB_LANG
)


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère l'EPUB du dictionnaire."""
    if output_path is None:
        output_path = OUTPUT_EPUB

    print(f"Génération de l'EPUB: {output_path}")

    # 1. Générer le markdown intermédiaire
    md_content = _build_markdown_for_epub(dictionary)

    # 2. Écrire le fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_content)
        temp_md = f.name

    try:
        # 3. Préparer les fichiers de configuration
        metadata_path = TEMPLATES_DIR / "epub" / "metadata.yaml"
        style_path = TEMPLATES_DIR / "epub" / "style.css"
        cover_path = BASE_DIR / "img" / "cover.png"

        # 4. Construire la commande Pandoc
        cmd = [
            "pandoc",
            temp_md,
            "--from=markdown",
            "--to=epub",
            "--toc",
            "-o", str(output_path)
        ]

        # Ajouter les options si les fichiers existent
        if metadata_path.exists():
            cmd.extend(["--metadata-file", str(metadata_path)])
            cmd.extend(["--epub-metadata", str(metadata_path)])

        if style_path.exists():
            cmd.extend(["--css", str(style_path)])

        if cover_path.exists():
            cmd.extend(["--epub-cover-image", str(cover_path)])

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"[ERROR] Pandoc failed: {result.stderr}")
            return False

        print(f"[OK] EPUB généré: {output_path}")
        return True

    finally:
        # Nettoyer le fichier temporaire
        os.unlink(temp_md)


def _build_markdown_for_epub(dictionary: Dictionary) -> str:
    """Construit le markdown formaté pour l'EPUB."""
    sections = []

    # En-tête avec métadonnées
    sections.append(_generate_yaml_header())

    # Licence et informations
    sections.append(_generate_license_section())

    # Contributeurs
    contributors_content = _load_contributors()
    if contributors_content:
        sections.append("# Contributeurs\n")
        sections.append(contributors_content)

    # Contenu par lettre
    for letter in dictionary.letters():
        sections.append(f"\n# {letter}\n")

        for definition in dictionary.get_by_letter(letter):
            md = definition.to_markdown(format_type="full")
            # Convertir les chemins d'images
            md = _adjust_image_paths(md, definition)
            # Convertir les listes en HTML pour meilleure compatibilité
            md = _markdown_lists_to_html(md)
            sections.append(md)
            sections.append("\n")

    return "\n".join(sections)


def _generate_yaml_header() -> str:
    """Génère l'en-tête YAML pour Pandoc."""
    year = datetime.now().year
    return f"""---
title: "{PROJECT_NAME}"
author: "{AUTHOR}"
lang: "{EPUB_LANG}"
rights: "© {year} {AUTHOR}. {LICENSE}"
---
"""


def _generate_license_section() -> str:
    """Génère la section de licence."""
    year = datetime.now().year
    date_str = datetime.now().strftime('%d/%m/%Y')

    return f"""# Informations

**{PROJECT_NAME}**

*{PROJECT_SUBTITLE}*

© {year} {AUTHOR}

Version du {date_str}

Cet ouvrage est sous licence {LICENSE}

[https://creativecommons.org/licenses/by-nc-sa/4.0/](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

"""


def _load_contributors() -> str:
    """Charge le fichier des contributeurs."""
    contributors_path = TEMPLATES_DIR / "contributors.md"
    if contributors_path.exists():
        return contributors_path.read_text(encoding='utf-8')
    return ""


def _adjust_image_paths(content: str, definition) -> str:
    """Ajuste les chemins des images pour l'EPUB."""
    import re
    # Construire le chemin absolu vers les assets (avec forward slashes)
    assets_path = str(definition.path / "assets").replace('\\', '/')

    def replace_image(match):
        filename = match.group(1)
        return f'![]({assets_path}/{filename})'

    # Remplacer les chemins relatifs par des chemins absolus
    content = re.sub(r'!\[\]\(\./assets/([^)]+)\)', replace_image, content)
    return content


def _markdown_lists_to_html(content: str) -> str:
    """Convertit les listes markdown en HTML pour meilleure compatibilité EPUB."""
    lines = content.split('\n')
    new_content = []
    in_list = False

    for line in lines:
        if line.strip().startswith('* '):
            if not in_list:
                new_content.append('<ul>')
                in_list = True
            item_content = line.strip()[2:]  # Enlever "* "
            new_content.append(f'<li>{item_content}</li>')
        else:
            if in_list:
                new_content.append('</ul>')
                in_list = False
            new_content.append(line)

    if in_list:
        new_content.append('</ul>')

    return '\n'.join(new_content)
