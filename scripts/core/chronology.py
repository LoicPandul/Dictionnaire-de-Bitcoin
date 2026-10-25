#!/usr/bin/env python3
"""
Chronologie de l'écosystème (chronologie/fr/*.yaml).

Un fichier par année à partir de 2009, plus `avant-2009.yaml`. Chaque événement a une
date ISO (jour, mois ou année seule quand le jour n'est pas connu), un titre, un texte,
des renvois vers le dictionnaire et au moins deux sources indépendantes.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

import yaml

from ..config import CHRONOLOGY_DIR

DATE_RE = re.compile(r"^(-?\d{1,4})(?:-(\d{2}))?(?:-(\d{2}))?$")

MOIS_FR = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril", 5: "mai", 6: "juin",
    7: "juillet", 8: "août", 9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
}


@dataclass
class Event:
    date: str
    title: str
    text: str
    related: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)
    file: str = ""

    @property
    def parts(self):
        m = DATE_RE.match(self.date)
        if not m:
            return None
        year, month, day = m.groups()
        return int(year), int(month) if month else None, int(day) if day else None

    @property
    def year(self) -> Optional[int]:
        p = self.parts
        return p[0] if p else None

    @property
    def sort_key(self):
        p = self.parts or (9999, None, None)
        # Une date sans jour (ou sans mois) passe avant les dates précises de la même période.
        return (p[0], p[1] or 0, p[2] or 0, self.title)

    def date_fr(self) -> str:
        """« 3 janvier 2009 », « janvier 2009 » ou « 2009 »."""
        p = self.parts
        if not p:
            return self.date
        year, month, day = p
        if month and day:
            jour = "1er" if day == 1 else str(day)
            return f"{jour} {MOIS_FR[month]} {year}"
        if month:
            return f"{MOIS_FR[month]} {year}"
        return str(year)


def load(base: Optional[Path] = None) -> List[Event]:
    """Tous les événements, triés par date. Liste vide si le dossier n'existe pas."""
    base = base or CHRONOLOGY_DIR
    events: List[Event] = []
    if not base.exists():
        return events
    for path in sorted(base.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for raw in data.get("events", []):
            events.append(Event(
                date=str(raw.get("date", "")),
                title=str(raw.get("title", "")).strip(),
                text=str(raw.get("text", "")).strip(),
                related=[str(s) for s in (raw.get("related") or [])],
                sources=[str(s) for s in (raw.get("sources") or [])],
                file=path.name,
            ))
    events.sort(key=lambda e: e.sort_key)
    return events
