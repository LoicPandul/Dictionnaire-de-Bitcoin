#!/usr/bin/env python3
"""
Vérification de l'ordre alphabétique des définitions.
"""

import unicodedata
from ..core.dictionary import Dictionary


def validate(dictionary: Dictionary, verbose: bool = True) -> bool:
    """
    Vérifie que les définitions sont dans l'ordre alphabétique.

    Returns:
        True si tout est en ordre, False sinon.
    """
    print("Vérification de l'ordre alphabétique...")

    errors = []

    for letter in dictionary.letters():
        definitions = dictionary.get_by_letter(letter)

        # Vérifier l'ordre dans chaque lettre
        for i in range(1, len(definitions)):
            prev_title = _normalize_for_sort(definitions[i - 1].title)
            curr_title = _normalize_for_sort(definitions[i].title)

            if prev_title > curr_title:
                errors.append({
                    'letter': letter,
                    'prev': definitions[i - 1].title,
                    'curr': definitions[i].title,
                })

    if errors:
        print(f"\n[ERROR] {len(errors)} erreur(s) d'ordre alphabétique trouvée(s):")
        for error in errors:
            print(f"  [{error['letter']}] '{error['prev']}' devrait être après '{error['curr']}'")
        return False

    print(f"[OK] Toutes les définitions sont dans l'ordre alphabétique")
    return True


def _normalize_for_sort(title: str) -> str:
    """Normalise un titre pour le tri alphabétique."""
    # Supprimer les accents
    normalized = unicodedata.normalize('NFKD', title)
    normalized = ''.join(c for c in normalized if not unicodedata.combining(c))
    # Minuscules
    return normalized.lower()
