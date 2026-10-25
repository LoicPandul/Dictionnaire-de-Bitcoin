#!/usr/bin/env python3
"""Prépare les images du site tirées du livre imprimé et des pictogrammes. À relancer seulement si les sources changent.

- les 19 pictogrammes de catégorie (assets/pictograms), retracés en SVG d'un seul tracé ;
- six pages intérieures et la boucle « feuilletage » (dictionnaire-de-bitcoin.pdf, édition 2026).
La jaquette de l'accueil (banian 2027) est faite par tools/jaquette-2027.py, la carte sociale depuis
tools/carte-sociale.html (capture 1200 × 630).

Dépendances : poppler (pdftoppm), ffmpeg, Python 3 avec opencv-python-headless, numpy, pillow, potracer.
    uv venv /tmp/venv && uv pip install --python /tmp/venv/bin/python opencv-python-headless numpy pillow potracer
    node site/tools/raster-pictos.mjs /tmp/pictos      (lit les SVG d'origine dans un navigateur sans écran)
    /tmp/venv/bin/python site/tools/prepare-assets.py /tmp/pictos
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



def run(*cmd):
    subprocess.run(cmd, check=True)


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


# 1. Pictogrammes : rendus en PNG 1024 px par raster-pictos.mjs, puis retracés.
def pictos(raster_dir):
    os.makedirs(os.path.join(OUT, 'pictos'), exist_ok=True)
    for f in sorted(os.listdir(raster_dir)):
        if not f.endswith('.png'):
            continue
        ink = cv2.imread(os.path.join(raster_dir, f), 0) < 128
        d = trace(ink, 100 / 1024, turdsize=30, tolerance=0.35)
        with open(os.path.join(OUT, 'pictos', f[:-4] + '.svg'), 'w') as fh:
            fh.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="{d}"/></svg>')


# 2. Six pages intérieures du PDF (édition 2026).
def pages():
    pdf = os.path.join(ROOT, 'dictionnaire-de-bitcoin.pdf')
    for n in (3, 31, 36, 212, 467, 516):
        run('pdftoppm', '-r', '150', '-png', '-f', str(n), '-l', str(n), pdf, os.path.join(TMP, 'p'))
        src = [p for p in os.listdir(TMP) if p.startswith('p-') and p.endswith(f'{n:03d}.png')][0]
        page = Image.open(os.path.join(TMP, src)).convert('RGB')
        page.resize((600, round(600 * page.height / page.width)), Image.LANCZOS).save(
            os.path.join(OUT, f'page-{n}.webp'), 'WEBP', quality=82, method=6)


# 3. La boucle « feuilletage » : 41 pages du PDF, une toutes les quatorze, 9 images par seconde,
#    en niveaux de gris, avec son image d'attente.
def riffle():
    pdf = os.path.join(ROOT, 'dictionnaire-de-bitcoin.pdf')
    video = os.path.join(HERE, '..', 'static', 'video')
    os.makedirs(video, exist_ok=True)
    frames = os.path.join(TMP, 'riffle')
    os.makedirs(frames, exist_ok=True)
    for k, n in enumerate(range(14, 581, 14)):
        run('pdftoppm', '-r', '80', '-png', '-f', str(n), '-l', str(n), '-scale-to-x', '440', '-scale-to-y', '-1', pdf, os.path.join(frames, 'r'))
        src = [p for p in os.listdir(frames) if p.startswith('r-')][0]
        os.replace(os.path.join(frames, src), os.path.join(frames, f'f{k:03d}.png'))
    run('ffmpeg', '-loglevel', 'error', '-y', '-framerate', '9', '-i', os.path.join(frames, 'f%03d.png'), '-vf', 'scale=320:-2,format=gray,format=yuv420p',
        '-c:v', 'libx264', '-preset', 'veryslow', '-crf', '31', '-movflags', '+faststart', '-an', os.path.join(video, 'feuilletage.mp4'))
    run('ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(frames, 'f000.png'), '-vf', 'scale=320:-2,format=gray', '-quality', '78', os.path.join(video, 'feuilletage.webp'))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages()
    riffle()
    if len(sys.argv) > 1:
        pictos(sys.argv[1])
    print('images prêtes dans', os.path.relpath(OUT, ROOT))
