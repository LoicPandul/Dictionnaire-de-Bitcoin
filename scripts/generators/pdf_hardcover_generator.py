#!/usr/bin/env python3
"""
Génération du PDF au format relié 7"x10" (17.78cm x 25.4cm).

Réutilise le générateur broché (pdf_generator) et adapte la géométrie
pour le format relié avec des marges proportionnelles.
"""

import os
import subprocess
import tempfile
from pathlib import Path

from ..core.dictionary import Dictionary
from ..config import BASE_DIR, OUTPUT_PDF
from . import pdf_generator


# Fichier de sortie : même nom avec suffixe -relie
OUTPUT_PDF_HARDCOVER = OUTPUT_PDF.with_name(
    OUTPUT_PDF.stem + "-relie" + OUTPUT_PDF.suffix
)

# Géométrie broché (à remplacer)
_BROCHE_GEOMETRY = """    paperwidth=13.97cm,
    paperheight=21.59cm,
    top=8mm,
    bottom=8mm,
    outer=10.5mm,
    inner=20mm,
    headheight=12pt,
    headsep=5mm,
    footskip=8mm,"""

# Géométrie relié 7"x10" (17.78cm x 25.4cm, marges proportionnelles)
_RELIE_GEOMETRY = """    paperwidth=17.78cm,
    paperheight=25.4cm,
    top=9.5mm,
    bottom=9.5mm,
    outer=13.5mm,
    inner=25.5mm,
    headheight=14pt,
    headsep=6mm,
    footskip=9.5mm,"""


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère le PDF du dictionnaire au format relié."""
    if output_path is None:
        output_path = OUTPUT_PDF_HARDCOVER

    print(f"Génération du PDF relié: {output_path}")

    # Adapter la limite de caractères des blocs de code au format plus large
    original_max_chars = pdf_generator.CODE_MAX_CHARS
    pdf_generator.CODE_MAX_CHARS = 81

    # Charger les infos légales et construire le LaTeX via le générateur broché
    legal = pdf_generator._load_legal_info()
    latex_content = pdf_generator._build_latex_content(dictionary, legal)

    # Restaurer la valeur originale
    pdf_generator.CODE_MAX_CHARS = original_max_chars

    # Remplacer la géométrie broché par la géométrie relié
    latex_content = latex_content.replace(_BROCHE_GEOMETRY, _RELIE_GEOMETRY)

    # Compiler avec XeLaTeX (2 passes)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.tex', delete=False, encoding='utf-8') as f:
        f.write(latex_content)
        temp_tex = f.name

    try:
        output_dir = output_path.parent

        for pass_num in range(2):
            print(f"  Passe {pass_num + 1}/2...")
            cmd = [
                "xelatex",
                "-interaction=nonstopmode",
                "-output-directory", str(output_dir),
                "-jobname", "dictionnaire_temp_relie",
                temp_tex
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                encoding='utf-8', errors='replace', cwd=str(output_dir)
            )

        temp_pdf = output_dir / "dictionnaire_temp_relie.pdf"

        if not temp_pdf.exists():
            print(f"[ERROR] XeLaTeX n'a pas généré de PDF")
            if result.stderr:
                print(f"Stderr: {result.stderr[-2000:]}")
            return False

        if output_path.exists():
            output_path.unlink()
        temp_pdf.rename(output_path)

        # Nettoyer les fichiers auxiliaires
        for ext in ['.aux', '.log', '.out', '.toc']:
            aux_file = output_dir / f"dictionnaire_temp_relie{ext}"
            if aux_file.exists():
                aux_file.unlink()

        print(f"[OK] PDF relié généré: {output_path}")
        return True

    finally:
        if os.path.exists(temp_tex):
            os.unlink(temp_tex)
