#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools>=4.50"]
# ///
"""Instances statiques des polices de la charte 2027, pour les outils qui ne lisent
pas les axes variables (XeLaTeX, Pillow, Kindle, navigateurs anciens).

    uv run design/polices/instances.py

Écrit les fichiers dans fonts/static/.  Ajoute l'espace fine insécable U+202F
(absente des fichiers d'origine) en la faisant pointer sur l'espace fine U+2009.
Licence : SIL OFL 1.1, voir fonts/OFL-*.txt (aucun nom réservé, renommage permis).
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "fonts"
OUT = SRC / "static"

# (fichier source, famille, style, axes, italique)
INSTANCES = [
    ("Archivo-Variable.ttf", "Archivo Texte", "Regular", {"wdth": 92, "wght": 400}, False),
    ("Archivo-Italic-Variable.ttf", "Archivo Texte", "Italic", {"wdth": 92, "wght": 400}, True),
    ("Archivo-Variable.ttf", "Archivo Texte", "Bold", {"wdth": 92, "wght": 700}, False),
    ("Archivo-Variable.ttf", "Archivo Vedette", "Regular", {"wdth": 75, "wght": 750}, False),
    ("Archivo-Variable.ttf", "Archivo Categorie", "Regular", {"wdth": 100, "wght": 600}, False),
    ("Archivo-Variable.ttf", "Archivo Titre", "Regular", {"wdth": 75, "wght": 800}, False),
    ("Archivo-Variable.ttf", "Archivo Couverture", "Regular", {"wdth": 62, "wght": 900}, False),
    ("Archivo-Variable.ttf", "Archivo Schema", "Regular", {"wdth": 100, "wght": 400}, False),
    ("Archivo-Variable.ttf", "Archivo Schema", "Bold", {"wdth": 100, "wght": 600}, False),
    ("Archivo-Italic-Variable.ttf", "Archivo Schema", "Italic", {"wdth": 100, "wght": 400}, True),
    ("AtkinsonHyperlegibleMono-Variable.ttf", "Atkinson Hyperlegible Mono", "Regular", {"wght": 400}, False),
    ("AtkinsonHyperlegibleMono-Italic-Variable.ttf", "Atkinson Hyperlegible Mono", "Italic", {"wght": 400}, True),
    ("AtkinsonHyperlegibleMono-Variable.ttf", "Atkinson Hyperlegible Mono", "Bold", {"wght": 700}, False),
]


def set_names(font, family, style):
    name = font["name"]
    ps = (family + "-" + style).replace(" ", "")
    for rec in list(name.names):
        if rec.nameID in (16, 17, 21, 22, 25) or rec.nameID >= 256:
            name.removeNames(nameID=rec.nameID)
    for nid, val in ((1, family), (2, style), (3, f"{ps};2027"), (4, f"{family} {style}"), (6, ps)):
        name.setName(val, nid, 3, 1, 0x409)
        name.setName(val, nid, 1, 0, 0)


def add_narrow_nbsp(font):
    for table in font["cmap"].tables:
        if table.isUnicode() and 0x202F not in table.cmap:
            src = table.cmap.get(0x2009) or table.cmap.get(0x0020)
            if src:
                table.cmap[0x202F] = src


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for src, family, style, axes, italic in INSTANCES:
        font = instantiateVariableFont(TTFont(SRC / src), axes, updateFontNames=False)
        set_names(font, family, style)
        add_narrow_nbsp(font)
        os2 = font["OS/2"]
        os2.usWeightClass = int(axes.get("wght", 400))
        os2.fsSelection = (os2.fsSelection & ~0b1100001) | (1 if italic else 0) | (0b100000 if style == "Bold" else 0) | (0b1000000 if style == "Regular" else 0)
        font["head"].macStyle = (2 if italic else 0) | (1 if style == "Bold" else 0)
        out = OUT / f"{family.replace(' ', '')}-{style}.ttf"
        font.save(out)
        print(out.relative_to(ROOT), axes)


if __name__ == "__main__":
    main()
