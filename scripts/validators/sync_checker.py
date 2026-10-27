#!/usr/bin/env python3
"""
Synchronisation des deux versions du dictionnaire.

Chaque dossier de definitions/fr doit avoir une version développée (definition.md) et
une version courte (courte.md) : les deux versions ont donc exactement les mêmes termes.
La version courte tient en une ou deux phrases, 45 mots au plus, sans liste, image,
formule, lien, gras ni titre.
"""

import re
from pathlib import Path
from typing import List, Tuple

from ..config import DEFINITIONS_DIR

MAX_WORDS = 45
MAX_SENTENCES = 2
# Fin de phrase : ponctuation forte suivie d'une espace ou de la fin du texte, sauf
# après une abréviation (« Block Inc. », « etc. », « J.-C. »).
SENTENCE_END = re.compile(r"(\S*)[.!?…](?=\s|$)")
ABBREVIATIONS = {"etc", "inc", "ltd", "corp", "co", "cf", "vol", "dr", "st", "mr", "mrs", "jr", "sr", "no",
                 "n°", "av", "apr", "env", "mt"}
INITIALS = re.compile(r"([A-Za-z]\.-?)+[A-Za-z]")  # « J.-C », « U.S »
FORBIDDEN = [
    (re.compile(r"^\s*([*\-]|\d+\.)\s", re.MULTILINE), "liste"),
    (re.compile(r"!\["), "image"),
    (re.compile(r"(?<!\\)\$"), "formule"),
    (re.compile(r"\]\("), "lien"),
    (re.compile(r"\*\*"), "gras"),
    (re.compile(r"^#", re.MULTILINE), "titre"),
    (re.compile(r"[—–]"), "tiret cadratin ou demi-cadratin"),
]


def _sentences(text: str) -> int:
    without_code = re.sub(r"`[^`]*`", "x", text)
    count = 0
    for m in SENTENCE_END.finditer(without_code):
        word = m.group(1).lower().rstrip(".")
        if word in ABBREVIATIONS or INITIALS.fullmatch(m.group(1)):
            continue
        count += 1
    return count


def check_short(text: str) -> List[str]:
    """Problèmes d'une version courte (liste vide si elle est conforme)."""
    problems = []
    text = text.strip()
    if not text:
        return ["vide"]
    if "\n\n" in text:
        problems.append("plusieurs paragraphes")
    words = len(text.split())
    if words > MAX_WORDS:
        problems.append(f"{words} mots (max {MAX_WORDS})")
    n = _sentences(text)
    if n == 0:
        problems.append("aucune phrase terminée")
    elif n > MAX_SENTENCES:
        problems.append(f"{n} phrases (max {MAX_SENTENCES})")
    for pattern, label in FORBIDDEN:
        if pattern.search(text):
            problems.append(label)
    return problems


def check(base: Path = None) -> Tuple[List[str], dict]:
    """Retourne (erreurs, compteurs) pour tous les dossiers de definitions/fr."""
    base = base or DEFINITIONS_DIR
    errors: List[str] = []
    long_terms, short_terms = set(), set()
    for d in sorted(p for p in base.glob("*/*") if p.is_dir()):
        long_md, short_md = d / "definition.md", d / "courte.md"
        if long_md.exists() and long_md.read_text(encoding="utf-8").strip():
            long_terms.add(d.name)
        elif long_md.exists():
            errors.append(f"[{d.name}] definition.md vide")
        if short_md.exists():
            short_terms.add(d.name)
            for problem in check_short(short_md.read_text(encoding="utf-8")):
                errors.append(f"[{d.name}] courte.md : {problem}")
    for slug in sorted(long_terms - short_terms):
        errors.append(f"[{slug}] courte.md manquant")
    for slug in sorted(short_terms - long_terms):
        errors.append(f"[{slug}] courte.md sans definition.md")
    stats = {"developpees": len(long_terms), "courtes": len(short_terms),
             "communs": len(long_terms & short_terms)}
    return errors, stats
