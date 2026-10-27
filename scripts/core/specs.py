#!/usr/bin/env python3
"""
Spécifications numérotées : BIP, BOLT, bLIP (specifications/<série>.yaml).

Ce ne sont pas des définitions : chaque document a un numéro, un titre, un statut et un
résumé en français. Quand le dictionnaire a déjà une entrée développée consacrée au
document, le champ `definition` donne son slug.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from ..config import SPECIFICATIONS_DIR

# Ordre des séries dans le livre, et leur nom affiché.
SERIES = {
    "bip": "BIP",
    "bolt": "BOLT",
    "blip": "bLIP",
}


@dataclass
class SpecDoc:
    series: str
    id: str                      # « BIP-0032 », « BOLT-02 », « bLIP-0001 »
    sort_key: int
    title: str
    status: List[str]            # une valeur par document
    summary: str
    url: str = ""
    type: str = ""
    layer: str = ""
    authors: List[str] = field(default_factory=list)
    created: str = ""
    definition: Optional[str] = None   # slug d'une entrée développée
    related: List[str] = field(default_factory=list)  # entrées liées du dictionnaire
    raw: dict = field(default_factory=dict)


@dataclass
class SpecSeries:
    series: str
    label: str
    source: str
    source_commit: str
    entries: List[SpecDoc]


def _status_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def load_series(series: str, base: Optional[Path] = None) -> Optional[SpecSeries]:
    """Charge specifications/<series>.yaml, ou None si le fichier n'existe pas."""
    path = (base or SPECIFICATIONS_DIR) / f"{series}.yaml"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    entries = []
    for raw in data.get("entries", []):
        if "sort_key" in raw:
            key = int(raw["sort_key"])
        else:
            key = int(raw.get("number", 0))
        entries.append(SpecDoc(
            series=series,
            id=str(raw.get("id", "")),
            sort_key=key,
            title=str(raw.get("title", "")),
            status=_status_list(raw.get("status")),
            summary=str(raw.get("summary", "")).strip(),
            url=str(raw.get("url", "")),
            type=str(raw.get("type", "") or ""),
            layer=str(raw.get("layer", "") or ""),
            authors=[str(a) for a in (raw.get("authors") or [])],
            created=str(raw.get("created", "") or ""),
            definition=raw.get("definition") or None,
            related=[str(s) for s in (raw.get("related") or [])],
            raw=raw,
        ))
    entries.sort(key=lambda e: (e.sort_key, e.id))
    return SpecSeries(
        series=series,
        label=SERIES.get(series, series.upper()),
        source=str(data.get("source", "")),
        source_commit=str(data.get("source_commit", "")),
        entries=entries,
    )


def load_all(base: Optional[Path] = None) -> Dict[str, SpecSeries]:
    result = {}
    for series in SERIES:
        loaded = load_series(series, base)
        if loaded:
            result[series] = loaded
    return result
