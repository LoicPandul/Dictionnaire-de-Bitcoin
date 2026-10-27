#!/usr/bin/env python3
"""
Configuration centralisée pour le Dictionnaire de Bitcoin.
"""

import shutil
from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).parent.parent
DEFINITIONS_DIR = BASE_DIR / "definitions" / "fr"
TEMPLATES_DIR = BASE_DIR / "templates"
SPECIFICATIONS_DIR = BASE_DIR / "specifications"
CHRONOLOGY_DIR = BASE_DIR / "chronologie" / "fr"
FONTS_DIR = BASE_DIR / "fonts"
PICTOGRAMS_DIR = BASE_DIR / "assets" / "pictograms"

# Sorties de build (ignorées par git) et outils locaux (.tools/, ignoré par git)
BUILD_DIR = BASE_DIR / "build"
TOOLS_DIR = BASE_DIR / ".tools"

# Fichiers générés et suivis par git
OUTPUT_INDEX = BASE_DIR / "INDEX.md"
OUTPUT_STATS = BASE_DIR / "stats.md"
README_FILE = BASE_DIR / "README.md"

# Liens
GITHUB_URL = "https://github.com/LoicPandul/Dictionnaire-de-Bitcoin"


def find_tex_engine():
    """Retourne le moteur LaTeX disponible : ("xelatex", chemin) ou ("tectonic", chemin).

    `xelatex` (TeX Live, MiKTeX) a la priorité. À défaut, Tectonic : un moteur XeTeX
    autonome qui s'installe sans droits administrateur (binaire dans .tools/bin/).
    """
    xelatex = shutil.which("xelatex")
    if xelatex:
        return "xelatex", xelatex
    local = TOOLS_DIR / "bin" / "tectonic"
    if local.exists():
        return "tectonic", str(local)
    tectonic = shutil.which("tectonic")
    if tectonic:
        return "tectonic", tectonic
    return None, None


def find_epubcheck():
    """Retourne la commande epubcheck sous forme de liste, ou None."""
    jars = sorted(TOOLS_DIR.glob("epubcheck-*/epubcheck.jar"))
    java = shutil.which("java")
    if jars and java:
        return [java, "-jar", str(jars[-1])]
    epubcheck = shutil.which("epubcheck")
    if epubcheck:
        return [epubcheck]
    return None
