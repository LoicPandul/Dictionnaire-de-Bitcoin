#!/usr/bin/env python3
"""Prépare les images du site tirées du livre imprimé. À relancer seulement si le PDF change.

- quatre pages intérieures et la boucle « feuilletage » (dictionnaire-de-bitcoin.pdf, édition 2026).
Les pictogrammes 2027 sont lus tels quels dans assets/pictograms au build ; l'Allée des baobabs de
l'accueil vient de tools/allee.py ; favicon et carte sociale sont ceux du script de couverture.

Dépendances : poppler (pdftoppm), ffmpeg, Python 3 avec pillow.
    python3 site/tools/prepare-assets.py
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, '..', 'static', 'img')
TMP = tempfile.mkdtemp(prefix='dico-assets-')



def run(*cmd):
    subprocess.run(cmd, check=True)


def pages():
    pdf = os.path.join(ROOT, 'dictionnaire-de-bitcoin.pdf')
    for n in (31, 212, 467, 516):
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
        run('pdftoppm', '-r', '200', '-png', '-f', str(n), '-l', str(n), '-scale-to-x', '1280', '-scale-to-y', '-1', pdf, os.path.join(frames, 'r'))
        src = [p for p in os.listdir(frames) if p.startswith('r-')][0]
        os.replace(os.path.join(frames, src), os.path.join(frames, f'f{k:03d}.png'))
    run('ffmpeg', '-loglevel', 'error', '-y', '-framerate', '9', '-i', os.path.join(frames, 'f%03d.png'), '-vf', 'scale=640:-2,format=gray,format=yuv420p',
        '-c:v', 'libx264', '-preset', 'veryslow', '-crf', '30', '-movflags', '+faststart', '-an', os.path.join(video, 'feuilletage.mp4'))
    run('ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(frames, 'f000.png'), '-vf', 'scale=640:-2,format=gray', '-quality', '80', os.path.join(video, 'feuilletage.webp'))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    pages()
    riffle()
    print('images prêtes dans', os.path.relpath(OUT, ROOT))
