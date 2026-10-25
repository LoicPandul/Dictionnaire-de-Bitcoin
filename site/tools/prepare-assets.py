#!/usr/bin/env python3
"""Prépare les images du site à partir des sources du dépôt. À relancer seulement si les sources changent.

Toutes les images viennent du livre lui-même :
- l'arbre gravé de la couverture (assets/cover-hardcover.pdf), titre imprimé effacé, en traits transparents ;
- la feuille du dos de la couverture, vectorisée (emblème et favicon) ;
- les 19 pictogrammes de catégorie (assets/pictograms), retracés en SVG d'un seul tracé ;
- le livre en volume (bannière assets/images/cover.png), fond ramené au bleu nuit de la couverture ;
- la couverture à plat et six pages intérieures (dictionnaire-de-bitcoin.pdf).

Dépendances : poppler (pdfimages, pdftoppm), Python 3 avec opencv-python-headless, numpy, pillow, potracer.
    uv venv /tmp/venv && uv pip install --python /tmp/venv/bin/python opencv-python-headless numpy pillow potracer
    /tmp/venv/bin/python site/tools/prepare-assets.py
Les pictogrammes passent d'abord par un navigateur sans écran (Playwright) pour lire les SVG d'origine :
    node site/tools/raster-pictos.mjs <dossier de sortie>   (voir l'étape 3)
"""
import os
import subprocess
import sys
import tempfile

import cv2
import numpy as np
import potrace
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, '..', 'static', 'img')
TMP = tempfile.mkdtemp(prefix='dico-assets-')

NAVY = (25, 48, 66)        # #193042, le fond de la couverture
GRAVURE = (169, 186, 200)  # #A9BAC8, les traits de l'arbre sur bleu nuit
OS_ = (238, 234, 224)      # #EEEAE0, le titre de la couverture


def run(*cmd):
    subprocess.run(cmd, check=True)


def smoothstep(x, e0, e1):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def trace(mask, scale, turdsize=20, alphamax=1.0, tolerance=0.4):
    """Bitmap booléen (True = encre) vers un attribut d de chemin SVG."""
    path = potrace.Bitmap(~mask).trace(turdsize=turdsize, alphamax=alphamax, opticurve=True, opttolerance=tolerance)
    f = lambda v: f'{v * scale:.2f}'.rstrip('0').rstrip('.')
    parts = []
    for curve in path:
        s = curve.start_point
        d = [f'M{f(s.x)} {f(s.y)}']
        for seg in curve.segments:
            if seg.is_corner:
                d.append(f'L{f(seg.c.x)} {f(seg.c.y)}L{f(seg.end_point.x)} {f(seg.end_point.y)}')
            else:
                d.append(f'C{f(seg.c1.x)} {f(seg.c1.y)} {f(seg.c2.x)} {f(seg.c2.y)} {f(seg.end_point.x)} {f(seg.end_point.y)}')
        parts.append(''.join(d) + 'Z')
    return ''.join(parts)


def cover_image():
    run('pdfimages', '-png', os.path.join(ROOT, 'assets', 'cover-hardcover.pdf'), os.path.join(TMP, 'hc'))
    return cv2.imread(os.path.join(TMP, 'hc-000.png'))  # 5041 × 3425, BGR


# 1. L'arbre : on efface le titre imprimé (pixels chauds et clairs) et son halo sombre,
#    puis on garde les traits froids comme couche alpha, reconstruite là où passait le texte.
def tree(cover):
    front = cover[:, 2690:-4].astype(np.float32)  # la dernière colonne de la couverture est un filet clair
    b, g, r = front[..., 0], front[..., 1], front[..., 2]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    text = ((lum > 105) & ((r - b) > -14)).astype(np.uint8)
    hole = cv2.dilate(text, np.ones((5, 5), np.uint8), iterations=2)
    l8 = np.clip(lum, 0, 255).astype(np.uint8)
    l8[hole > 0] = 40
    small = cv2.resize(l8, (l8.shape[1] // 4, l8.shape[0] // 4), interpolation=cv2.INTER_AREA)
    bg = cv2.GaussianBlur(cv2.erode(small, np.ones((9, 9), np.uint8)), (0, 0), 6)
    bg = cv2.resize(bg, (l8.shape[1], l8.shape[0]), interpolation=cv2.INTER_LINEAR).astype(np.float32)
    alpha = np.clip((lum - bg - 5) / 55.0, 0, 1)
    alpha[(r - b) > -6] = 0
    a8 = (alpha * 255).astype(np.uint8)
    a8[hole > 0] = 0
    rec = cv2.inpaint(a8, hole * 255, 4, cv2.INPAINT_TELEA).astype(np.float32) / 255
    a = (smoothstep(rec, 0.08, 0.7) * 255).astype(np.uint8)
    h, w = a.shape
    # Traits Gravure sur le bleu nuit exact de la couverture, en image opaque : l'alpha d'une gravure
    # aussi fine coûte trois fois plus cher que l'image pleine.
    k = (a.astype(np.float32) / 255)[..., None]
    rgb = np.array(NAVY, np.float32) * (1 - k) + np.array(GRAVURE, np.float32) * k
    img = Image.fromarray(rgb.astype(np.uint8), 'RGB')
    for height in (1100, 1600):
        r = img.resize((round(w * height / h), height), Image.LANCZOS)
        r.save(os.path.join(OUT, f'arbre-{height}.avif'), 'AVIF', quality=45)
        r.save(os.path.join(OUT, f'arbre-{height}.webp'), 'WEBP', quality=68, method=6)


# 2. La feuille du dos de la couverture : emblème (détaillé) et favicon.
def leaf(cover):
    crop = cv2.cvtColor(cover[290:520, 2420:2580], cv2.COLOR_BGR2GRAY).astype(np.float32)
    variants = {'feuille': (6, 2.2, 140, 20, 0.4), 'feuille-petite': (4, 3.4, 128, 30, 0.6)}
    for name, (up, blur, thr, turd, tol) in variants.items():
        big = cv2.GaussianBlur(cv2.resize(crop, (crop.shape[1] * up, crop.shape[0] * up), interpolation=cv2.INTER_CUBIC), (0, 0), blur)
        bw = big > thr
        ys, xs = np.where(bw)
        bw = bw[ys.min() - 4:ys.max() + 5, xs.min() - 4:xs.max() + 5]
        h, w = bw.shape
        d = trace(bw, 100 / h, turdsize=turd, tolerance=tol)
        vw = f'{w * 100 / h:.1f}'
        with open(os.path.join(OUT, f'{name}.svg'), 'w') as fh:
            fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} 100"><path d="{d}"/></svg>')
        if name == 'feuille-petite':
            # Favicon : la feuille couleur os sur un carré bleu nuit.
            s = 100 * 1.36
            x0 = (s - float(vw)) / 2
            fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s:.0f} {s:.0f}">'
                   f'<rect width="100%" height="100%" fill="#193042"/>'
                   f'<path transform="translate({x0:.1f} 18)" fill="#EEEAE0" d="{d}"/></svg>')
            with open(os.path.join(HERE, '..', 'static', 'favicon.svg'), 'w') as fh:
                fh.write(fav)


# 3. Pictogrammes : rendus en PNG 1024 px par raster-pictos.mjs, puis retracés.
def pictos(raster_dir):
    os.makedirs(os.path.join(OUT, 'pictos'), exist_ok=True)
    for f in sorted(os.listdir(raster_dir)):
        if not f.endswith('.png'):
            continue
        ink = cv2.imread(os.path.join(raster_dir, f), 0) < 128
        d = trace(ink, 100 / 1024, turdsize=30, tolerance=0.35)
        with open(os.path.join(OUT, 'pictos', f[:-4] + '.svg'), 'w') as fh:
            fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="{d}"/></svg>')


# 4. Le livre en volume : fond de la bannière (#1B3A4B) ramené au bleu nuit de la couverture.
def book3d():
    im = np.asarray(Image.open(os.path.join(ROOT, 'assets', 'images', 'cover.png')).convert('RGB').crop((40, 0, 1160, 1000))).astype(np.float32)
    im *= np.array(NAVY, np.float32) / np.array((27, 58, 75), np.float32)
    Image.fromarray(np.clip(im, 0, 255).astype(np.uint8)).save(os.path.join(OUT, 'livre.webp'), 'WEBP', quality=80, method=6)


# 5. La couverture à plat et six pages intérieures du PDF.
def pages(cover):
    front = cv2.cvtColor(cover[:, 2690:-4], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(front)
    img.resize((900, round(900 * img.height / img.width)), Image.LANCZOS).save(os.path.join(OUT, 'couverture.webp'), 'WEBP', quality=80, method=6)
    pdf = os.path.join(ROOT, 'dictionnaire-de-bitcoin.pdf')
    for n in (3, 31, 36, 212, 467, 516):
        run('pdftoppm', '-r', '150', '-png', '-f', str(n), '-l', str(n), pdf, os.path.join(TMP, 'p'))
        src = [p for p in os.listdir(TMP) if p.startswith('p-') and p.endswith(f'{n:03d}.png')][0]
        page = Image.open(os.path.join(TMP, src)).convert('RGB')
        page.resize((600, round(600 * page.height / page.width)), Image.LANCZOS).save(
            os.path.join(OUT, f'page-{n}.webp'), 'WEBP', quality=82, method=6)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    cov = cover_image()
    tree(cov)
    leaf(cov)
    book3d()
    pages(cov)
    if len(sys.argv) > 1:
        pictos(sys.argv[1])
    print('images prêtes dans', os.path.relpath(OUT, ROOT))
