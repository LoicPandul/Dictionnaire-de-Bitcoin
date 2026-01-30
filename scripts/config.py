#!/usr/bin/env python3
"""
Configuration centralisée pour le Dictionnaire de Bitcoin.
"""

from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).parent.parent
DEFINITIONS_DIR = BASE_DIR / "definitions" / "fr"
TEMPLATES_DIR = BASE_DIR / "templates"
SCRIPTS_DIR = BASE_DIR / "scripts"

# Fichiers de sortie
OUTPUT_PDF = BASE_DIR / "Dictionnaire de Bitcoin.pdf"
OUTPUT_EPUB = BASE_DIR / "Dictionnaire_de_Bitcoin.epub"
OUTPUT_INDEX = BASE_DIR / "INDEX.md"
OUTPUT_STATS = BASE_DIR / "stats.md"
README_FILE = BASE_DIR / "README.md"

# Templates
PDF_TEMPLATE = TEMPLATES_DIR / "pdf" / "template.tex"
PDF_METADATA = TEMPLATES_DIR / "pdf" / "metadata.yaml"
EPUB_METADATA = TEMPLATES_DIR / "epub" / "metadata.yaml"
EPUB_STYLE = TEMPLATES_DIR / "epub" / "style.css"
CONTRIBUTORS_FILE = TEMPLATES_DIR / "contributors.md"

# Images
IMG_DIR = BASE_DIR / "img"

# Métadonnées du projet
PROJECT_NAME = "Dictionnaire de Bitcoin"
PROJECT_SUBTITLE = "Tout le vocabulaire technique de Bitcoin"
AUTHOR = "Loïc Morel"
PUBLISHER = "Pandul"
LICENSE = "CC BY-NC-SA 4.0"
GITHUB_URL = "https://github.com/LoicPandul/Dictionnaire-de-Bitcoin"

# Langues supportées
DEFAULT_LANG = "fr"
SUPPORTED_LANGS = ["fr"]

# Configuration PDF
PDF_ENGINE = "xelatex"
PDF_FONT = "Arial"
PDF_MARGIN = "1.2in"

# Configuration EPUB
EPUB_LANG = "fr"
