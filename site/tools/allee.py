"""Allée des baobabs de la couverture 2027, en SVG à calques pour le site.

Reprend design/couverture/baobab.py (branche feat/couverture-2027) avec la même graine :
le dessin est celui de la couverture. Chaque arbre est un groupe à part, pour que le
site les anime séparément (le soleil, les trois baobabs du fond, le grand baobab, le sol).

    python3 site/tools/allee.py <dossier design/couverture> > site/lib/allee.json
"""
import json
import re
import random
import sys

sys.path.insert(0, sys.argv[1])
import baobab  # noqa: E402
from banyan import GENESIS  # noqa: E402

# Proportions de la première du broché, ramenées à une largeur de 1000 : arbre de 1060 (1,06 × la largeur), sol à 1100.
S, H, X0, GY = 1000.0, 1060.0, 0.0, 1100.0
rng = random.Random(int(GENESIS, 16) ^ 0xBA0BAB)
sun_r = min(S * 0.2, H * 0.22)
calques = {"soleil": baobab.ellipse(X0 + S * 0.69, GY - H * 0.4, sun_r, sun_r)}
fond = []
for nom, (u, h) in zip(("gauche", "droite", "petit"), ((0.17, 0.46), (0.82, 0.5), (0.69, 0.3))):
    d = baobab.grandidieri(X0 + u * S, GY, H * h, rng, scale_w=0.75, light=False)
    left, right = baobab.column(X0 + u * S, GY, GY - H * h * 0.7, *(H * h * 0.75 * f for f in (0.17, 0.168, 0.135)), bulge=0.35)
    fond.append({"nom": nom, "arbre": " ".join(d["arbre"]), "clair": baobab.light_band(left, right, 0.24)})
d = baobab.grandidieri(X0 + S * 0.47, GY, H, rng)
grand = {"nom": "grand", "fond": " ".join(d["fond"]), "arbre": " ".join(d["arbre"]), "clair": " ".join(d["clair"])}
sol = (f"M{X0:.2f} {GY + 0.5:.2f} L{X0 + S:.2f} {GY + 0.5:.2f} L{X0 + S:.2f} {GY - H * 0.012:.2f} "
       f"Q{X0 + S * 0.5:.2f} {GY - H * 0.03:.2f} {X0:.2f} {GY - H * 0.012:.2f}Z")
out = {"viewBox": [0, 0, S, GY + 2], "soleil": calques["soleil"], "fond": fond, "grand": grand, "sol": sol,}
# Un dixième d'unité suffit à l'écran (la toile fait 1 000 de large).
court = lambda v: re.sub(r"(\d+\.\d)\d+", r"\1", v) if isinstance(v, str) else v
out = {k: court(v) if not isinstance(v, list) else [{kk: court(vv) for kk, vv in t.items()} if isinstance(t, dict) else t for t in v] for k, v in out.items()}
out["grand"] = {k: court(v) for k, v in out["grand"].items()}
json.dump(out, sys.stdout, ensure_ascii=False)
