#!/usr/bin/env python3
"""
Validation des métadonnées YAML des définitions.
Vérifie que title, english_term et french_term sont en MAJUSCULES.
"""

import re
from ..core.dictionary import Dictionary


def validate(dictionary: Dictionary) -> bool:
    """
    Vérifie que les champs title, english_term et french_term
    ne contiennent pas de minuscules.

    Affiche un WARNING pour chaque problème trouvé.
    Ne corrige rien automatiquement.

    Returns:
        True si tout est OK, False si des warnings ont été émis.
    """
    print("Vérification des métadonnées (casse)...")

    warnings = []

    for definition in dictionary:
        # Vérifier title
        if definition.title and _has_lowercase(definition.title):
            warnings.append(
                f"[{definition.slug}] title contient des minuscules: \"{definition.title}\""
            )

        # Vérifier english_term
        if definition.english_term and _has_lowercase(definition.english_term):
            warnings.append(
                f"[{definition.slug}] english_term contient des minuscules: \"{definition.english_term}\""
            )

        # Vérifier french_term
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


def _has_lowercase(text: str) -> bool:
    """Vérifie si un texte contient des lettres minuscules."""
    return any(c.islower() for c in text)
