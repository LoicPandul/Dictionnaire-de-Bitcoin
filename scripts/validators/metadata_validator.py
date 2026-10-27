#!/usr/bin/env python3
"""
Validation des métadonnées des définitions (metadata.yaml).

`validate` ne fait que lire et retourne la liste des erreurs. `fix_cross_references`
retire les renvois vers des UUID inconnus : c'est la seule correction automatique, et
elle ne s'exécute que sur demande (`python3 scripts/main.py fix`).
"""

import re
from collections import Counter
from typing import List

from ..core.dictionary import Dictionary

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(\./assets/([^)\s]+)\)")
# Champs d'une image dans `assets:` : son fichier, et le crédit d'une image de tiers
# (logo, capture…), imprimé en petit sous l'image : « Logo Bitcoin Core, © …, MIT ».
ASSET_FIELDS = {"filename", "credit"}
CREDIT_MAX_CHARS = 200


def validate(dictionary: Dictionary) -> List[str]:
    errors: List[str] = list(dictionary.warnings)
    taxonomy = dictionary.taxonomy
    if taxonomy:
        errors += taxonomy.problems()

    uuids = Counter(d.uuid for d in dictionary)
    slugs = Counter(d.slug for d in dictionary)

    for d in dictionary:
        where = f"[{d.slug or d.path.name}]"
        if not UUID_RE.match(d.uuid or ""):
            errors.append(f"{where} uuid invalide : {d.uuid!r}")
        elif uuids[d.uuid] > 1:
            errors.append(f"{where} uuid en double : {d.uuid}")
        if d.slug != d.path.name:
            errors.append(f"{where} le slug ne correspond pas au dossier « {d.path.name} »")
        if not SLUG_RE.match(d.slug or ""):
            errors.append(f"{where} slug invalide")
        elif slugs[d.slug] > 1:
            errors.append(f"{where} slug en double")
        if d.path.parent.name != (d.slug or "?")[0]:
            errors.append(f"{where} rangé dans « {d.path.parent.name}/ » au lieu de « {d.slug[:1]}/ »")

        for field_name in ("title", "english_term", "french_term"):
            value = getattr(d, field_name)
            if value and any(c.islower() for c in value):
                errors.append(f"{where} {field_name} doit être en MAJUSCULES : « {value} »")
        if not d.title:
            errors.append(f"{where} title manquant")
        if d.english_term and d.french_term:
            errors.append(f"{where} english_term et french_term ne peuvent pas coexister")

        if not d.category:
            errors.append(f"{where} catégorie manquante")
        elif taxonomy and d.category not in taxonomy.listed:
            errors.append(f"{where} catégorie inconnue : « {d.category} »")

        for ref in d.cross_references:
            if dictionary.get_by_uuid(ref) is None:
                errors.append(f"{where} renvoi vers un UUID inconnu : {ref}")
            elif ref == d.uuid:
                errors.append(f"{where} renvoi vers elle-même")

        for asset in d.assets:
            if not isinstance(asset, dict) or not asset.get("filename"):
                errors.append(f"{where} entrée de assets: sans filename : {asset!r}")
                continue
            for key in sorted(set(asset) - ASSET_FIELDS):
                errors.append(f"{where} assets: champ inconnu « {key} » ({asset['filename']})")
            if "credit" in asset:
                credit = asset["credit"]
                if not isinstance(credit, str) or not credit.strip():
                    errors.append(f"{where} assets: credit vide ou non textuel ({asset['filename']})")
                elif "\n" in credit.strip() or len(credit) > CREDIT_MAX_CHARS:
                    errors.append(f"{where} assets: credit sur une ligne, {CREDIT_MAX_CHARS} caractères au plus "
                                  f"({asset['filename']})")
        declared = {a.get("filename") for a in d.assets if isinstance(a, dict)}
        used = set(IMAGE_RE.findall(d.content))
        for name in sorted(used - declared):
            errors.append(f"{where} image utilisée mais absente de assets: dans metadata.yaml : {name}")
        for name in sorted(declared):
            if not (d.path / "assets" / name).exists():
                errors.append(f"{where} image déclarée introuvable : assets/{name}")
    return errors


def fix_cross_references(dictionary: Dictionary) -> int:
    """Retire les renvois vers des UUID inconnus. Retourne le nombre de renvois retirés."""
    removed = 0
    for d in dictionary:
        invalid = [r for r in d.cross_references if dictionary.get_by_uuid(r) is None]
        if not invalid:
            continue
        path = d.path / "metadata.yaml"
        text = path.read_text(encoding="utf-8")
        for ref in invalid:
            text = re.sub(rf'^\s+-\s+"?{re.escape(ref)}"?\s*\n', "", text, flags=re.MULTILINE)
            d.cross_references.remove(ref)
            removed += 1
            print(f"  [{d.slug}] renvoi retiré : {ref}")
        path.write_text(text, encoding="utf-8")
    return removed
