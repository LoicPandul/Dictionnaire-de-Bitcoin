#!/usr/bin/env python3
"""
Chronologie de l'écosystème (chronologie/<langue>/*.yaml).

Un fichier par année à partir de 2009, plus `avant-2009.yaml`. Chaque événement a une
date ISO (jour, mois ou année seule quand le jour n'est pas connu), un titre, un texte,
des renvois vers le dictionnaire et au moins deux sources indépendantes. Une traduction
(chronologie/en/) ne porte que le titre et le texte de chaque événement (scripts/core/yaml_sync.py).
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

import yaml

from ..config import CHRONOLOGY_DIR, CHRONOLOGY_ROOT
from . import i18n

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
    key: str = ""      # date, puis « date#2 »… pour un deuxième événement du même jour dans le fichier

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

    def date_label(self, lang: str = "fr") -> str:
        """« 3 janvier 2009 », « janvier 2009 » ou « 2009 » (« January 3, 2009 » en anglais)."""
        p = self.parts
        return i18n.date_label(lang, *p) if p else self.date

    def date_fr(self) -> str:
        return self.date_label("fr")


def load(base: Optional[Path] = None, lang: str = "fr") -> List[Event]:
    """Tous les événements, triés par date. Liste vide si le dossier n'existe pas.

    Dans une langue traduite : les événements d'origine, avec le titre et le texte traduits ;
    un événement sans traduction n'est pas retenu.
    """
    if lang != i18n.SOURCE_LANG and base is None:
        from . import yaml_sync
        translated = {(it.file, it.key): it.translation
                      for it in yaml_sync.items(yaml_sync.CHRONOLOGY, i18n.SOURCE_LANG, lang) if it.translation}
        events = []
        for ev in load():
            raw = translated.get((ev.file, ev.key))
            if raw:
                events.append(Event(ev.date, str(raw.get("title", "")).strip(), str(raw.get("text", "")).strip(),
                                    ev.related, ev.sources, ev.file, ev.key))
        events.sort(key=lambda e: e.sort_key)
        return events
    base = base or CHRONOLOGY_DIR
    events: List[Event] = []
    if not base.exists():
        return events
    for path in sorted(base.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        seen = {}
        for raw in data.get("events", []):
            date = str(raw.get("date", ""))
            seen[date] = seen.get(date, 0) + 1
            events.append(Event(
                date=str(raw.get("date", "")),
                title=str(raw.get("title", "")).strip(),
                text=str(raw.get("text", "")).strip(),
                related=[str(s) for s in (raw.get("related") or [])],
                sources=[str(s) for s in (raw.get("sources") or [])],
                file=path.name,
                key=date if seen[date] == 1 else f"{date}#{seen[date]}",
            ))
    events.sort(key=lambda e: e.sort_key)
    return events
