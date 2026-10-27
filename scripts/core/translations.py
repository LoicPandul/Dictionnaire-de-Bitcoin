#!/usr/bin/env python3
"""
Synchronisation des langues du dictionnaire (docs/traduction.md).

Une entrée existe dans une ou plusieurs langues : definitions/<langue>/<lettre>/<slug>/. Les
versions d'une même entrée partagent le même UUID ; le slug, lui, suit la langue.

La version traduite garde la trace de sa source dans son metadata.yaml :

    source_lang: "fr"                   # langue de la version d'origine
    source_slug: "adresse-de-reception" # dossier de la source (aide à la lecture)
    source_hash: "…"                    # empreinte de la source au moment de la synchro
    source_commit: "…"                  # dernier commit de la source à ce moment (indice pour git diff)
    translation_hash: "…"               # empreinte de la traduction au moment de la synchro

L'empreinte couvre ce qui se traduit : le titre, definition.md et courte.md. En la comparant
aux fichiers actuels, on sait dans quel sens la synchro est à refaire :
  - la source a changé, la traduction non : traduction en retard ;
  - la traduction a changé, la source non : modification à reporter dans la source ;
  - les deux ont changé : conflit, à fusionner à la main.
Les métadonnées non traduites (catégorie, renvois, images déclarées) ne sont écrites qu'une fois,
dans la version d'origine, et valent pour toutes les langues.
"""

import hashlib
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from ..config import BASE_DIR, DEFINITIONS_ROOT, LANGUAGES_FILE

HASH_LEN = 16
SOURCE_FIELDS = ("source_lang", "source_slug", "source_hash", "source_commit", "translation_hash")

# Statuts d'une paire (source, traduction), du point de vue d'une langue cible.
UP_TO_DATE = "à jour"
MISSING = "manquante"
UNMARKED = "à marquer"            # traduction présente, synchro jamais enregistrée
TRANSLATION_BEHIND = "en retard"  # la source a changé depuis la traduction
SOURCE_BEHIND = "à reporter"      # la traduction a changé : reporter dans la source
CONFLICT = "conflit"              # les deux ont changé
ORIGIN_MISSING = "absente de la langue d'origine"  # entrée écrite d'abord dans la langue cible
ORPHAN = "orpheline"              # la source a été supprimée : supprimer ou rattacher la traduction
EXCLUDED = "exclue"               # entrée sans objet dans la langue cible (templates/languages.yaml)
STATUSES = (UP_TO_DATE, TRANSLATION_BEHIND, SOURCE_BEHIND, CONFLICT, UNMARKED, MISSING, ORIGIN_MISSING, ORPHAN,
            EXCLUDED)


def load_languages(path: Path = None) -> dict:
    """templates/languages.yaml : langue d'origine et périmètre de chaque traduction."""
    path = path or LANGUAGES_FILE
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("source", "fr")
    data.setdefault("translations", {})
    return data


def _normalize(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    return "\n".join(l.rstrip() for l in lines).strip()


def fingerprint(title: str, definition: str, short: str) -> str:
    """Empreinte du contenu traduisible d'une entrée (titre, développée, courte)."""
    payload = "\x00".join(_normalize(x or "") for x in (title, definition, short))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:HASH_LEN]


@dataclass
class Entry:
    """Une version linguistique d'une entrée : definitions/<lang>/<lettre>/<slug>/."""

    lang: str
    path: Path
    meta: dict
    definition: str = ""
    short: str = ""
    problems: List[str] = field(default_factory=list)

    @classmethod
    def load(cls, lang: str, directory: Path) -> "Entry":
        problems = []
        meta = {}
        meta_path = directory / "metadata.yaml"
        if meta_path.exists():
            try:
                meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError as e:
                problems.append(f"metadata.yaml illisible : {e}")
        else:
            problems.append("metadata.yaml manquant")
        long_md, short_md = directory / "definition.md", directory / "courte.md"
        definition = long_md.read_text(encoding="utf-8") if long_md.exists() else ""
        short = short_md.read_text(encoding="utf-8") if short_md.exists() else ""
        return cls(lang, directory, meta, definition, short, problems)

    @property
    def uuid(self) -> str:
        return str(self.meta.get("uuid") or "")

    @property
    def slug(self) -> str:
        return str(self.meta.get("slug") or self.path.name)

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or "")

    @property
    def rel(self) -> str:
        return self.path.relative_to(BASE_DIR).as_posix()

    @property
    def is_translation(self) -> bool:
        return bool(self.meta.get("source_lang"))

    def current_hash(self) -> str:
        return fingerprint(self.title, self.definition, self.short)


def load_entries(lang: str, root: Path = None) -> Dict[str, Entry]:
    """Toutes les entrées d'une langue, indexées par UUID (les doublons sont signalés à part)."""
    base = (root or DEFINITIONS_ROOT) / lang
    entries: Dict[str, Entry] = {}
    if not base.is_dir():
        return entries
    for d in sorted(p for p in base.glob("*/*") if p.is_dir()):
        e = Entry.load(lang, d)
        entries.setdefault(e.uuid or f"?{e.rel}", e)
    return entries


def all_entry_dirs(lang: str, root: Path = None) -> List[Path]:
    base = (root or DEFINITIONS_ROOT) / lang
    return sorted(p for p in base.glob("*/*") if p.is_dir()) if base.is_dir() else []


@dataclass
class Pair:
    uuid: str
    source: Optional[Entry]        # version d'origine (None si seule la traduction existe)
    translation: Optional[Entry]   # version traduite (None si elle manque)
    status: str = MISSING
    part: Optional[str] = None


def status_of(source: Entry, translation: Entry) -> str:
    m = translation.meta
    if not (m.get("source_hash") and m.get("translation_hash")):
        return UNMARKED
    source_changed = source.current_hash() != m.get("source_hash")
    translation_changed = translation.current_hash() != m.get("translation_hash")
    if source_changed and translation_changed:
        return CONFLICT
    if source_changed:
        return TRANSLATION_BEHIND
    if translation_changed:
        return SOURCE_BEHIND
    return UP_TO_DATE


def pairs(origin: str, target: str, part_of=None, root: Path = None, exclude=()) -> List[Pair]:
    """Paires entre la langue d'origine du dépôt et une langue cible, par UUID.

    Le sens de chaque paire se lit dans les métadonnées : la version qui porte `source_lang`
    est la traduction. Une entrée écrite d'abord dans la langue cible (sans `source_lang`) a
    donc pour traduction la version dans la langue d'origine.
    """
    a, b = load_entries(origin, root), load_entries(target, root)
    result = []
    for uuid in sorted(set(a) | set(b)):
        ea, eb = a.get(uuid), b.get(uuid)
        if ea and eb:
            source, translation = (eb, ea) if ea.is_translation and not eb.is_translation else (ea, eb)
            status = status_of(source, translation)
        elif ea:
            source, translation, status = ea, None, EXCLUDED if ea.slug in exclude else MISSING
        elif eb.is_translation:
            source, translation, status = None, eb, ORPHAN
        else:
            source, translation, status = eb, None, ORIGIN_MISSING
        cat = (source or translation).meta.get("category") or (ea.meta.get("category") if ea else None)
        result.append(Pair(uuid, source, translation, status, part_of(cat) if part_of and cat else None))
    return result


def last_commit(path: Path) -> str:
    """Dernier commit qui a touché `path` (vide hors dépôt git)."""
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%h", "--", str(path)], cwd=BASE_DIR,
                             capture_output=True, text=True, check=True).stdout.strip()
        return out
    except (OSError, subprocess.CalledProcessError):
        return ""


def write_source_fields(entry: Entry, values: dict) -> None:
    """Écrit ou met à jour les champs source_* d'un metadata.yaml, sans toucher au reste.

    Le site lit metadata.yaml avec un parseur minimal (une clé par ligne, valeurs entre
    guillemets doubles) : on garde exactement cette forme.
    """
    path = entry.path / "metadata.yaml"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = [l for l in text.splitlines() if not re.match(rf"^({'|'.join(SOURCE_FIELDS)}):", l)]
    # Les champs de synchro se placent juste après slug, avant le reste.
    insert_at = next((i + 1 for i, l in enumerate(lines) if l.startswith("slug:")), len(lines))
    new = [f'{k}: "{values.get(k, "")}"' for k in SOURCE_FIELDS]
    lines[insert_at:insert_at] = new
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for k in SOURCE_FIELDS:
        entry.meta[k] = values.get(k, "")


def mark(source: Entry, translation: Entry) -> dict:
    """Enregistre que `translation` est à jour de `source`."""
    values = {
        "source_lang": source.lang,
        "source_slug": source.slug,
        "source_hash": source.current_hash(),
        "source_commit": last_commit(source.path),
        "translation_hash": translation.current_hash(),
    }
    write_source_fields(translation, values)
    return values


def slugify(title: str) -> str:
    """Slug d'un titre : minuscules sans accents, mots reliés par des tirets."""
    import unicodedata
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def create(source: Entry, lang: str, title: str, slug: str = None, root: Path = None) -> Entry:
    """Crée le dossier d'une traduction : metadata.yaml seul, synchro non encore enregistrée."""
    slug = slug or slugify(title)
    directory = (root or DEFINITIONS_ROOT) / lang / slug[0] / slug
    if directory.exists():
        raise FileExistsError(f"{directory.relative_to(BASE_DIR)} existe déjà")
    directory.mkdir(parents=True)
    (directory / "metadata.yaml").write_text(
        f'uuid: "{source.uuid}"\ntitle: "{title.upper()}"\nslug: "{slug}"\n'
        f'source_lang: "{source.lang}"\nsource_slug: "{source.slug}"\n', encoding="utf-8")
    return Entry.load(lang, directory)
