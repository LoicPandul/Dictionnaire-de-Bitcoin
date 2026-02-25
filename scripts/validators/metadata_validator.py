#!/usr/bin/env python3
"""
Validation des métadonnées YAML des définitions.
Vérifie que title, english_term et french_term sont en MAJUSCULES.
Vérifie que toutes les cross-references pointent vers des définitions existantes.
"""

import re
from ..core.dictionary import Dictionary


def validate(dictionary: Dictionary) -> bool:
    """
    Vérifie les métadonnées de toutes les définitions :
    - Casse des champs title, english_term, french_term
    - Validité des cross-references (UUIDs existants)

    Returns:
        True si tout est OK, False si des problèmes ont été trouvés.
    """
    casse_ok = _validate_casse(dictionary)
    crossref_ok = _validate_cross_references(dictionary)
    return casse_ok and crossref_ok


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


def _validate_cross_references(dictionary: Dictionary) -> bool:
    """
    Vérifie que chaque UUID dans cross_references correspond
    à une définition existante dans le dictionnaire.

    Returns:
        True si toutes les cross-references sont valides, False sinon.
    """
    print("Vérification des cross-references...")

    errors = []

    for definition in dictionary:
        for ref_uuid in definition.cross_references:
            target = dictionary.get_by_uuid(ref_uuid)
            if target is None:
                errors.append(
                    f"[{definition.slug}] cross-reference invalide: "
                    f"UUID \"{ref_uuid}\" ne correspond à aucune définition"
                )

    if errors:
        print(f"\n[ERREUR] {len(errors)} cross-reference(s) invalide(s):")
        for e in errors:
            print(f"  ✗ {e}")
        return False

    print("[OK] Cross-references validées")
    return True


def _has_lowercase(text: str) -> bool:
    """Vérifie si un texte contient des lettres minuscules."""
    return any(c.islower() for c in text)
