#!/usr/bin/env python3
"""
Validation des métadonnées YAML des définitions.
Vérifie que title, english_term et french_term sont en MAJUSCULES.
Vérifie que toutes les cross-references pointent vers des définitions existantes.
"""

import re
import yaml
from ..core.dictionary import Dictionary
from ..config import TEMPLATES_DIR


def validate(dictionary: Dictionary) -> bool:
    """
    Vérifie les métadonnées de toutes les définitions :
    - Casse des champs title, english_term, french_term
    - Validité des catégories (doivent exister dans categories.yaml)
    - Validité des cross-references (UUIDs existants)

    Returns:
        True si tout est OK, False si des problèmes ont été trouvés.
    """
    casse_ok = _validate_casse(dictionary)
    terms_ok = _validate_terms(dictionary)
    categories_ok = _validate_categories(dictionary)
    crossref_ok = _validate_cross_references(dictionary)
    return casse_ok and terms_ok and categories_ok and crossref_ok


def _validate_casse(dictionary: Dictionary) -> bool:
    """Vérifie que title, english_term et french_term sont en MAJUSCULES."""
    print("Vérification des métadonnées (casse)...")

    warnings = []

    for definition in dictionary:
        if definition.title and _has_lowercase(definition.title):
            warnings.append(
                f"[{definition.slug}] title contient des minuscules: \"{definition.title}\""
            )

        if definition.english_term and _has_lowercase(definition.english_term):
            warnings.append(
                f"[{definition.slug}] english_term contient des minuscules: \"{definition.english_term}\""
            )

        if definition.french_term and _has_lowercase(definition.french_term):
            warnings.append(
                f"[{definition.slug}] french_term contient des minuscules: \"{definition.french_term}\""
            )

    if warnings:
        print(f"\n[WARNING] {len(warnings)} problème(s) de casse trouvé(s):")
        for w in warnings:
            print(f"  ⚠ {w}")
        return False

    print("[OK] Métadonnées validées (casse)")
    return True


def _validate_terms(dictionary: Dictionary) -> bool:
    """Vérifie qu'une définition n'a pas à la fois english_term et french_term."""
    print("Vérification des termes (english_term / french_term)...")

    errors = []

    for definition in dictionary:
        if definition.english_term and definition.french_term:
            errors.append(
                f"[{definition.slug}] possède à la fois english_term (\"{definition.english_term}\") "
                f"et french_term (\"{definition.french_term}\")"
            )

    if errors:
        print(f"\n[ERREUR] {len(errors)} définition(s) avec english_term ET french_term:")
        for e in errors:
            print(f"  ✗ {e}")
        return False

    print("[OK] Termes validés (pas de doublon english/french)")
    return True


def _validate_categories(dictionary: Dictionary) -> bool:
    """Vérifie que chaque définition a une catégorie valide définie dans categories.yaml."""
    print("Vérification des catégories...")

    # Charger les catégories autorisées
    categories_path = TEMPLATES_DIR / "categories.yaml"
    with open(categories_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    valid_categories = set(data.get("categories", []))

    errors = []

    for definition in dictionary:
        cat = definition.category
        if not cat:
            errors.append(f"[{definition.slug}] catégorie manquante")
        elif cat not in valid_categories:
            errors.append(
                f"[{definition.slug}] catégorie invalide: \"{cat}\""
            )

    if errors:
        print(f"\n[ERREUR] {len(errors)} problème(s) de catégorie:")
        for e in errors:
            print(f"  ✗ {e}")
        print(f"\nCatégories autorisées: {', '.join(sorted(valid_categories))}")
        return False

    print("[OK] Catégories validées")
    return True


def _validate_cross_references(dictionary: Dictionary) -> bool:
    """
    Vérifie que chaque UUID dans cross_references correspond
    à une définition existante dans le dictionnaire.
    Supprime automatiquement les cross-references invalides des fichiers YAML.

    Returns:
        True (les cross-references invalides sont supprimées automatiquement).
    """
    print("Vérification des cross-references...")

    removed_count = 0

    for definition in dictionary:
        invalid_uuids = [
            ref_uuid for ref_uuid in definition.cross_references
            if dictionary.get_by_uuid(ref_uuid) is None
        ]

        if invalid_uuids:
            for uuid in invalid_uuids:
                print(
                    f"  ⚠ [{definition.slug}] cross-reference supprimée: "
                    f"UUID \"{uuid}\" ne correspond à aucune définition"
                )
                definition.cross_references.remove(uuid)
                removed_count += 1

            _save_metadata(definition)

    if removed_count:
        print(f"\n[AUTO-FIX] {removed_count} cross-reference(s) invalide(s) supprimée(s)")
    else:
        print("[OK] Cross-references validées")

    return True


def _save_metadata(definition) -> None:
    """Sauvegarde uniquement les cross_references dans le fichier metadata.yaml.

    Édite le fichier par manipulation textuelle pour ne pas altérer
    le reste du fichier (guillemets, ordre des clés, formatage).
    """
    metadata_path = definition.path / "metadata.yaml"

    with open(metadata_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Supprimer le bloc cross_references existant (clé + lignes indentées)
    content = re.sub(r'cross_references:\s*\n(?:\s+-\s+.*\n)*', '', content)

    # Reconstruire le bloc si des références restent
    if definition.cross_references:
        lines = "cross_references:\n"
        for ref in definition.cross_references:
            lines += f'  - "{ref}"\n'
        content = content.rstrip('\n') + '\n' + lines

    with open(metadata_path, "w", encoding="utf-8") as f:
        f.write(content)


def _has_lowercase(text: str) -> bool:
    """Vérifie si un texte contient des lettres minuscules."""
    return any(c.islower() for c in text)
