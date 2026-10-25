#!/usr/bin/env python3
"""Extrait de CMU Serif (fonts/cmunrm.ttf) les contours des lettres du logotype « DICTIONNAIRE DE BITCOIN »,
avec leurs points (sur la courbe et de contrôle), leur chasse et les approches de paire (GPOS),
pour le pied de page. Écrit lib/logotype.json. Dépendance : fontTools.
    python3 site/tools/logotype.py
"""
import json
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.recordingPen import DecomposingRecordingPen

HERE = os.path.dirname(os.path.abspath(__file__))
font = TTFont(os.path.join(HERE, '..', '..', 'fonts', 'cmunrm.ttf'))
gs = font.getGlyphSet()
cmap = font.getBestCmap()
upm = font['head'].unitsPerEm
WORD = 'DICTIONNAIRE DE BITCOIN'

# Approches de paire depuis GPOS (PairPos, formats 1 et 2).
def gpos_pairs():
    pairs = {}
    gpos = font['GPOS'].table
    for lookup in gpos.LookupList.Lookup:
        for st in lookup.SubTable:
            if st.LookupType == 9:
                st = st.ExtSubTable
            if getattr(st, 'LookupType', None) != 2 and type(st).__name__ != 'PairPos':
                continue
            cov = st.Coverage.glyphs
            if st.Format == 1:
                for i, first in enumerate(cov):
                    for pvr in st.PairSet[i].PairValueRecord:
                        v = pvr.Value1.XAdvance if pvr.Value1 and hasattr(pvr.Value1, 'XAdvance') else 0
                        if v:
                            pairs[(first, pvr.SecondGlyph)] = v
            elif st.Format == 2:
                c1 = st.ClassDef1.classDefs
                c2 = st.ClassDef2.classDefs
                for first in cov:
                    k1 = c1.get(first, 0)
                    for second in set(WORD):
                        g2 = cmap.get(ord(second))
                        if not g2:
                            continue
                        rec = st.Class1Record[k1].Class2Record[c2.get(g2, 0)]
                        v = rec.Value1.XAdvance if rec.Value1 and hasattr(rec.Value1, 'XAdvance') else 0
                        if v and (first, g2) not in pairs:
                            pairs[(first, g2)] = v
    return pairs

pairs = gpos_pairs()
glyphs = {}
for ch in sorted(set(WORD) - {' '}):
    name = cmap[ord(ch)]
    pen = SVGPathPen(gs)
    gs[name].draw(pen)
    rec = DecomposingRecordingPen(gs)
    gs[name].draw(rec)
    nodes = []
    for op, pts in rec.value:
        if op in ('moveTo', 'lineTo'):
            nodes.append([round(pts[0][0]), round(pts[0][1]), 1])
        elif op == 'qCurveTo':
            for p in pts[:-1]:
                if p is not None:
                    nodes.append([round(p[0]), round(p[1]), 0])
            nodes.append([round(pts[-1][0]), round(pts[-1][1]), 1])
        elif op == 'curveTo':
            nodes += [[round(pts[0][0]), round(pts[0][1]), 0], [round(pts[1][0]), round(pts[1][1]), 0], [round(pts[2][0]), round(pts[2][1]), 1]]
    glyphs[ch] = {'d': pen.getCommands(), 'adv': font['hmtx'][name][0], 'nodes': nodes}

kern = {}
for a in set(WORD):
    for b in set(WORD):
        if a == ' ' or b == ' ':
            continue
        v = pairs.get((cmap[ord(a)], cmap[ord(b)]))
        if v:
            kern[a + b] = v
space = font['hmtx'][cmap[32]][0]
cap = max(p[1] for g in glyphs.values() for p in g['nodes'] if p[2])
out = {'upm': upm, 'cap': cap, 'space': space, 'glyphs': glyphs, 'kern': kern}
with open(os.path.join(HERE, '..', 'lib', 'logotype.json'), 'w') as fh:
    json.dump(out, fh, separators=(',', ':'))
print('glyphes', len(glyphs), 'paires', kern, 'capitale', cap)

# Chasses (en em) de tous les caractères des titres, pour calculer au build la taille des vedettes.
import glob, re
chars = set()
for meta in glob.glob(os.path.join(HERE, '..', '..', 'definitions', 'fr', '*', '*', 'metadata.yaml')):
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', open(meta, encoding='utf8').read(), re.M)
    if m:
        chars |= set(m.group(1))
adv = {}
for ch in sorted(chars):
    g = cmap.get(ord(ch))
    if g:
        adv[ch] = round(font['hmtx'][g][0] / upm, 4)
with open(os.path.join(HERE, '..', 'lib', 'cmu-advances.json'), 'w') as fh:
    json.dump(adv, fh, ensure_ascii=False, separators=(',', ':'))
print('chasses', len(adv), 'manquants', ''.join(sorted(c for c in chars if c not in adv)))
