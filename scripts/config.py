#!/usr/bin/env python3
"""
Configuration centralisée pour le Dictionnaire de Bitcoin.
"""

from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).parent.parent
DEFINITIONS_DIR = BASE_DIR / "definitions" / "fr"
TEMPLATES_DIR = BASE_DIR / "templates"

# Fichiers de sortie
OUTPUT_PDF = BASE_DIR / "dictionnaire-de-bitcoin.pdf"
OUTPUT_INDEX = BASE_DIR / "index.md"
OUTPUT_STATS = BASE_DIR / "stats.md"
README_FILE = BASE_DIR / "README.md"

# Liens
GITHUB_URL = "https://github.com/LoicPandul/Dictionnaire-de-Bitcoin"
