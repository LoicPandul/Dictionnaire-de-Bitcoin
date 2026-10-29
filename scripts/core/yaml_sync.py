#!/usr/bin/env python3
"""
Synchronisation des traductions de la chronologie et des résumés de spécifications.

Ces textes vivent dans des fichiers YAML par langue : chronologie/<langue>/<année>.yaml et
specifications/<langue>/<série>.yaml. Le fichier traduit ne garde que ce qui se traduit
(titre et texte d'un événement, résumé d'une spécification) ; dates, statuts, renvois et
sources restent dans le fichier d'origine.

Chaque élément traduit porte `source_hash` et `translation_hash`, comme le metadata.yaml d'une
définition traduite (scripts/core/translations.py) : on en tire les mêmes statuts.
Un résumé se reconnaît à son identifiant (`BIP-0032`), un événement à sa date dans son
fichier (`2009-01-03`, puis `2009-01-03#2` pour le deuxième événement du même jour).
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from ..config import BASE_DIR, CHRONOLOGY_ROOT, SPECIFICATIONS_ROOT
from . import translations as tr

CHRONOLOGY = "chronologie"
SUMMARIES = "resumes-specifications"
KINDS = (SUMMARIES, CHRONOLOGY)

# Par sorte : dossier racine, clé de la liste, champs traduits, champs écrits dans la traduction.
_CONF = {
    SUMMARIES: (SPECIFICATIONS_ROOT, "entries", ("summary",), ("id", "summary")),
    CHRONOLOGY: (CHRONOLOGY_ROOT, "events", ("title", "text"), ("date", "title", "text")),
}


@dataclass
class Item:
    kind: str
    key: str                     # « BIP-0032 », « 2009-01-03 », « 2009-01-03#2 »
    file: str                    # nom du fichier (« bip.yaml », « 2009.yaml »)
    source: Optional[dict]       # élément du fichier d'origine
    translation: Optional[dict]  # élément du fichier traduit
    status: str = tr.MISSING

    @property
    def label(self) -> str:
        return f"{self.kind}/{self.file} {self.key}"


def _text(kind: str, raw: dict) -> str:
    return "\x00".join(str(raw.get(k) or "") for k in _CONF[kind][2])


def item_hash(kind: str, raw: dict) -> str:
    return tr.fingerprint(_text(kind, raw), "", "")


def _keyed(kind: str, raw_items: list) -> Dict[str, dict]:
    out, seen = {}, {}
    for raw in raw_items or []:
        if kind == SUMMARIES:
            key = str(raw.get("id", ""))
        else:
            date = str(raw.get("date", ""))
            seen[date] = seen.get(date, 0) + 1
            key = date if seen[date] == 1 else f"{date}#{seen[date]}"
        out.setdefault(key, raw)
    return out


def load_file(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def items(kind: str, origin: str, target: str) -> List[Item]:
    root, list_key, _, _ = _CONF[kind]
    names = sorted({p.name for lang in (origin, target) for p in (root / lang).glob("*.yaml")})
    result = []
    for name in names:
        src = _keyed(kind, load_file(root / origin / name).get(list_key))
        dst = _keyed(kind, load_file(root / target / name).get(list_key))
        for key in list(src) + [k for k in dst if k not in src]:
            s, t = src.get(key), dst.get(key)
            if s is not None and t is not None:
                status = status_of(kind, s, t)
            elif s is not None:
                status = tr.MISSING
            else:
                status = tr.ORPHAN
            result.append(Item(kind, key, name, s, t, status))
    return result


def status_of(kind: str, source: dict, translation: dict) -> str:
    if not (translation.get("source_hash") and translation.get("translation_hash")):
        return tr.UNMARKED
    source_changed = item_hash(kind, source) != translation.get("source_hash")
    translation_changed = item_hash(kind, translation) != translation.get("translation_hash")
    if source_changed and translation_changed:
        return tr.CONFLICT
    if source_changed:
        return tr.TRANSLATION_BEHIND
    if translation_changed:
        return tr.SOURCE_BEHIND
    return tr.UP_TO_DATE


def all_items(origin: str, target: str) -> List[Item]:
    return [i for kind in KINDS for i in items(kind, origin, target)]


def _quote(value) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def _write(kind: str, path: Path, data: dict) -> None:
    """Réécrit un fichier traduit : commentaires d'en-tête conservés, une valeur par ligne."""
    _, list_key, _, fields = _CONF[kind]
    header = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("#") or not line.strip():
                header.append(line)
            else:
                break
    while header and not header[-1].strip():
        header.pop()
    lines = header + (["", f"{list_key}:"] if header else [f"{list_key}:"])
    for raw in data.get(list_key) or []:
        keys = [k for k in (*fields, "source_hash", "translation_hash") if raw.get(k) not in (None, "")]
        for i, k in enumerate(keys):
            lines.append(f"  {'- ' if i == 0 else '  '}{k}: {_quote(raw[k])}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def mark(selected: List[Item], target: str) -> int:
    """Enregistre que les éléments choisis sont à jour de leur source ; retourne leur nombre."""
    by_file: Dict[Tuple[str, str], List[Item]] = {}
    for it in selected:
        if it.source is not None and it.translation is not None:
            by_file.setdefault((it.kind, it.file), []).append(it)
    for (kind, name), its in by_file.items():
        root, list_key, _, _ = _CONF[kind]
        path = root / target / name
        data = load_file(path)
        keyed = _keyed(kind, data.get(list_key))
        for it in its:
            raw = keyed[it.key]
            raw["source_hash"] = item_hash(kind, it.source)
            raw["translation_hash"] = item_hash(kind, raw)
            it.status = tr.UP_TO_DATE
        _write(kind, path, data)
    return sum(len(v) for v in by_file.values())


def rel(kind: str, lang: str, name: str) -> str:
    return (_CONF[kind][0] / lang / name).relative_to(BASE_DIR).as_posix()
