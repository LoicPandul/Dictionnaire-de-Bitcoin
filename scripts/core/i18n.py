#!/usr/bin/env python3
"""
Langue du livre : textes de l'interface, dates, libellés et guillemets.

Le livre se génère dans la langue d'origine (`fr`) ou dans une langue traduite
(templates/languages.yaml). Les textes propres au livre vivent dans templates/<langue>/ :
note de l'auteur, remerciements, mentions légales et, pour une traduction, `book.yaml`
(titres et introductions des parties, noms affichés des catégories, titres des éditions).
Les quelques mots que les générateurs impriment eux-mêmes (« Voir aussi », « Statut »…)
sont dans STRINGS ci-dessous.
"""

import re
from pathlib import Path
from typing import Optional

import yaml

from ..config import TEMPLATES_DIR

SOURCE_LANG = "fr"

STRINGS = {
    "fr": {
        "see_also": "Voir aussi", "see": "Voir", "related_one": "Terme associé", "related_many": "Termes associés",
        "status": "Statut", "type": "Type", "created": "Créé le", "contents": "Table des matières",
        "contributors": "Contributeurs et remerciements", "author_note": "Note de l'auteur",
        "legal": "Mentions légales", "version_of": "Version du", "licensed": "Cet ouvrage est sous licence",
        "website": "Site web", "email": "Email", "start": "Début", "range": "à", "colon": "\\,: ",
        "isbn": "ISBN", "other_term": "EN",
    },
    "en": {
        "see_also": "See also", "see": "See", "related_one": "Related term", "related_many": "Related terms",
        "status": "Status", "type": "Type", "created": "Created", "contents": "Contents",
        "contributors": "Contributors and acknowledgments", "author_note": "Author's note",
        "legal": "Legal notice", "version_of": "Version of", "licensed": "This work is licensed under",
        "website": "Website", "email": "Email", "start": "Start", "range": "to", "colon": ": ",
        "isbn": "ISBN", "other_term": "FR",
    },
}

MONTHS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
           "octobre", "novembre", "décembre"],
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September",
           "October", "November", "December"],
}

# Statuts des spécifications : libellé imprimé, suivi du statut d'origine quand ils diffèrent.
STATUS = {
    "fr": {"draft": "Brouillon", "complete": "Complet", "deployed": "Déployé", "closed": "Clos",
           "final": "Final", "active": "Actif", "proposed": "Proposé", "withdrawn": "Retiré",
           "replaced": "Remplacé", "rejected": "Rejeté", "obsolete": "Obsolète", "deferred": "Reporté"},
    # Les statuts des BOLT sont écrits en français dans specifications/fr/bolt.yaml.
    "en": {"actif": "Active", "retiré": "Withdrawn"},
}


def t(lang: str, key: str) -> str:
    return STRINGS.get(lang, STRINGS[SOURCE_LANG])[key]


def date_label(lang: str, year: int, month: Optional[int] = None, day: Optional[int] = None) -> str:
    """« 3 janvier 2009 » ou « January 3, 2009 » ; mois ou année seule si le jour manque."""
    if lang == "en":
        if month and day:
            return f"{MONTHS['en'][month - 1]} {day}, {year}"
        return f"{MONTHS['en'][month - 1]} {year}" if month else str(year)
    if month and day:
        return f"{'1er' if day == 1 else day} {MONTHS['fr'][month - 1]} {year}"
    return f"{MONTHS['fr'][month - 1]} {year}" if month else str(year)


def status_label(lang: str, status: str) -> str:
    label = STATUS.get(lang, {}).get(status.lower())
    if not label or label.lower() == status.lower():
        return label or status
    return label if lang != SOURCE_LANG and status.lower() in STATUS.get(lang, {}) else f"{label} ({status})"


def texts_dir(lang: str) -> Path:
    return TEMPLATES_DIR / lang


def book_labels(lang: str) -> dict:
    """templates/<langue>/book.yaml (vide pour la langue d'origine, qui lit parts.yaml et editions.yaml)."""
    path = texts_dir(lang) / "book.yaml"
    if lang == SOURCE_LANG or not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# --- guillemets anglais --------------------------------------------------------

_PROTECT = re.compile(r"```.*?```|`[^`\n]*`|\$\$.*?\$\$|(?<!\\)\$[^$\n]+?\$|\]\([^)]*\)|https?://\S+|<[^>]+>",
                      re.DOTALL)


def smart_quotes(text: str) -> str:
    """Guillemets et apostrophes typographiques ("x" → “x”, it's → it’s), hors code, formules et liens."""
    if not text:
        return text
    store = []

    def keep(m):
        store.append(m.group(0))
        return f"\u0007{len(store) - 1}\u0007"

    text = _PROTECT.sub(keep, text)
    text = re.sub(r'(^|[\s(\[{\u2014/-])"', "\\1\u201c", text, flags=re.MULTILINE)
    text = text.replace('"', "\u201d")
    text = re.sub(r"(\w)'(\w)", "\\1\u2019\\2", text)
    text = re.sub(r"(^|[\s(\[{-])'", "\\1\u2018", text, flags=re.MULTILINE)
    text = text.replace("'", "\u2019")
    return re.sub(r"\u0007(\d+)\u0007", lambda m: store[int(m.group(1))], text)
