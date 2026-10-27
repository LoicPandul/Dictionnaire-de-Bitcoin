#!/usr/bin/env python3
"""Chasses (en em) de tous les caractères des titres en Archivo Titre (largeur 75, graisse 800),
pour que le build calcule la taille de chaque vedette : deux lignes au plus à toutes les largeurs.
Écrit lib/archivo-advances.json. Dépendance : fontTools.
    python3 site/tools/chasses.py
"""
import glob
import json
import os
import re

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = os.path.dirname(os.path.abspath(__file__))
font = instancer.instantiateVariableFont(TTFont(os.path.join(HERE, '..', '..', 'assets', 'fonts', 'Archivo-Variable.ttf')), {'wdth': 75, 'wght': 800})
cmap, upm = font.getBestCmap(), font['head'].unitsPerEm
chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz–  ')
for meta in glob.glob(os.path.join(HERE, '..', '..', 'definitions', 'fr', '*', '*', 'metadata.yaml')):
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', open(meta, encoding='utf8').read(), re.M)
    if m:
        chars |= set(m.group(1))
adv = {ch: round(font['hmtx'][cmap[ord(ch)]][0] / upm, 4) for ch in sorted(chars) if ord(ch) in cmap}
with open(os.path.join(HERE, '..', 'lib', 'archivo-advances.json'), 'w') as fh:
    json.dump(adv, fh, ensure_ascii=False, separators=(',', ':'))
print('chasses', len(adv), 'manquants', ''.join(sorted(c for c in chars if ord(c) not in cmap)))
