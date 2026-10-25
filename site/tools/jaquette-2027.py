#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["uharfbuzz>=0.40", "pillow>=10"]
# ///
"""Jaquette 2027 du site : le banian de la couverture, sans ses textes, pour le héros de l'accueil.

Réutilise le générateur de la couverture 2027 (`design/couverture/banyan.py` et `typeset.py`,
branche feat/couverture-2027) : même graine (le bloc de genèse), mêmes couleurs, même titre en
Archivo Couverture. Les racines se posent sur le titre du site, composé en HTML exactement à la
place où la couverture l'imprime : ce script écrit ces positions dans lib/jaquette.json.

Format : la jaquette du broché sans fond perdu (dos, tranche de 680 pages, avant), en points.
Sorties dans le dossier donné :
  couronne.svg  feuillage et figues (sur fond Figue) ;
  racines.svg   racines aériennes et piliers (blanc sur transparent) ;
puis tools/raster-jaquette.mjs les rend en images.

    uv run site/tools/jaquette-2027.py --couverture <chemin de design/couverture> --sortie /tmp/jaquette
"""
import argparse
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

IN = 72.0
FIGUE, FIGUE_SOMBRE, CANOPEE, FIGUE_VIVE, BLANC = "#AA226A", "#691E47", "#4B2034", "#E12789", "#FFFFFF"
TITLE = ("DICTIONNAIRE", "DE BITCOIN")


def smoothstep(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--couverture", required=True, help="dossier design/couverture de la branche 2027")
    ap.add_argument("--sortie", required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(Path(args.couverture).resolve()))
    from banyan import Banyan  # noqa: E402
    from typeset import Face, Profile  # noqa: E402

    out = Path(args.sortie)
    out.mkdir(parents=True, exist_ok=True)
    archivo = ROOT / "fonts" / "Archivo-Variable.ttf"

    # Jaquette du broché, sans fond perdu : dos | tranche | avant.
    tw, th, spine = 5.5 * IN, 8.5 * IN, 680 * 0.002252 * IN
    W, H = 2 * tw + spine, th
    back = (0.0, tw)
    sp = (tw, tw + spine)
    front = (tw + spine, W)
    m, mi = 0.42 * IN, 0.375 * IN
    T = (front[0] + mi, m, front[1] - m, H - m)  # zone de texte de l'avant

    # Titre : mêmes règles que la couverture (Archivo largeur 62, graisse 900, approche −0,005 em).
    ft = Face(archivo, wdth=62, wght=900)
    tr = -0.005
    size = (T[2] - T[0]) / ft.width(TITLE[0], 1, tr)
    base_au = T[3]
    base_sub = base_au - size * 0.5
    base2 = base_sub - size * 0.46
    base1 = base2 - size * 0.86
    g1 = ft.glyphs(TITLE[0], size, T[0], base1, tr)
    prof = Profile([p for g in g1 for p in g[4]])
    pillars = []
    for ch, x, adv, _, polys in g1:
        if ch == "I":
            xs = [p[0] for poly in polys for p in poly]
            pillars.append(((min(xs) + max(xs)) / 2, max(xs) - min(xs)))
    gap = max(2.0, size * 0.04)
    pillar_x = {round(x, 2) for x, _ in pillars}

    def ground(x):
        if round(x, 2) in pillar_x:
            return (prof.min, "land")
        if x >= front[0]:
            if prof.x0 <= x <= prof.x1:
                t = prof.at(x)
                if t is not None and t < prof.min + size * 0.05:
                    return (t - gap, "land")
            return (prof.min - gap, "stop")
        if x >= sp[0]:
            return (0.24 * H, "stop")       # tranche : le titre vertical commence dessous
        return (0.31 * H, "stop")           # dos : le mot du jour commence dessous

    def canopy(x):
        f, b = 0.235 * H, 0.165 * H
        return b + (f - b) * smoothstep(back[1] - tw * 0.25, front[0] + tw * 0.15, x)

    def density(x):
        return 0.35 if sp[0] < x < sp[1] else 1.0

    unit = 66.0
    tree = Banyan(W, H, canopy, leaf_r=2.3 * unit / 66.0)
    lay = tree.build(ground, pillars=pillars, density=density)

    def g(name, fill):
        return f'<g fill="{fill}">' + "".join(f'<path d="{d}"/>' for d in lay[name]) + "</g>"

    head = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.2f}" height="{H:.2f}">'
    (out / "couronne.svg").write_text(
        head + f'<rect width="{W:.2f}" height="{H:.2f}" fill="{FIGUE}"/>'
        + g("leaves_a", FIGUE_SOMBRE) + g("leaves_b", CANOPEE) + g("figs", FIGUE_VIVE) + "</svg>")
    (out / "racines.svg").write_text(head + g("roots", BLANC) + g("pillars", BLANC) + "</svg>")

    # Positions des textes, en fractions : x et largeurs rapportés à l'avant, y à la hauteur.
    fw = front[1] - front[0]
    upem = ft.upem
    pos = {
        "jaquette": {"largeur_pt": round(W, 2), "hauteur_pt": round(H, 2), "dos": round(tw / W, 5),
                     "tranche": round(spine / W, 5), "avant": round(tw / W, 5)},
        "titre": {"corps": round(size / fw, 5), "x": round((T[0] - front[0]) / fw, 5),
                  "ligne1": round(base1 / H, 5), "ligne2": round(base2 / H, 5), "approche": tr},
        "sous_titre": {"corps": round(size * 0.232 / fw, 5), "ligne": round(base_sub / H, 5)},
        "auteur": {"corps": round(size * 0.19 / fw, 5), "ligne": round(base_au / H, 5),
                   "droite": round((front[1] - T[2]) / fw, 5)},
        "racines_bas_dos": 0.31, "racines_bas_tranche": 0.24,
        "couronne_avant": 0.235, "upem": upem,
    }
    (ROOT / "site" / "lib" / "jaquette.json").write_text(json.dumps(pos, indent=1))
    print(json.dumps({"racines": len(lay["roots"]), "piliers": len(lay["pillars"]),
                      "feuilles": len(lay["leaves_a"]) + len(lay["leaves_b"]), "titre_pt": round(size, 2)}))


if __name__ == "__main__":
    main()
