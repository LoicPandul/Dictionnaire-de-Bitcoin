#!/usr/bin/env python3
"""
Dictionnaire de Bitcoin - Script principal

Exécuter directement : python scripts/main.py
"""

import sys
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.core.dictionary import Dictionary
from scripts.generators import pdf_generator, index_generator, stats_generator
from scripts.validators import markdown_linter, metadata_validator
from scripts.config import DEFINITIONS_DIR


def cmd_build(dictionary):
    """Génère tous les formats."""
    print("\n" + "=" * 60)
    print("Build complet du Dictionnaire de Bitcoin")
    print("=" * 60)

    # 1. Lint + fix automatique
    print("\n--- Étape 1/5: Correction du markdown ---")
    markdown_linter.lint(dictionary, fix=True)

    # 2. Validation des métadonnées
    print("\n--- Étape 2/5: Validation des métadonnées ---")
    if not metadata_validator.validate(dictionary):
        print("\n[ERREUR] La validation des métadonnées a échoué. Build interrompu.")
        return

    # 3. Index
    print("\n--- Étape 3/5: Génération de l'index ---")
    index_generator.generate(dictionary)

    # 4. Stats
    print("\n--- Étape 4/5: Génération des statistiques ---")
    stats_generator.generate(dictionary)

    # 5. PDF
    print("\n--- Étape 5/5: Génération du PDF ---")
    pdf_generator.generate(dictionary)

    print("\n" + "=" * 60)
    print("Build terminé!")
    print("=" * 60)


def cmd_pdf(dictionary):
    """Génère le PDF."""
    print("\nGénération du PDF...")
    pdf_generator.generate(dictionary)


def cmd_index(dictionary):
    """Met à jour l'index."""
    print("\nMise à jour de l'index...")
    index_generator.generate(dictionary)


def cmd_stats(dictionary):
    """Génère les statistiques."""
    print("\nGénération des statistiques...")
    stats_generator.generate(dictionary)


def cmd_lint(dictionary):
    """Vérifie le markdown."""
    print("\nVérification du markdown...")
    markdown_linter.lint(dictionary, fix=False)


def cmd_lint_fix(dictionary):
    """Corrige automatiquement le markdown."""
    print("\nCorrection automatique du markdown...")
    markdown_linter.lint(dictionary, fix=True)


def cmd_info(dictionary):
    """Affiche les informations du dictionnaire."""
    print("\n" + "=" * 60)
    print("Dictionnaire de Bitcoin - Informations")
    print("=" * 60)
    print(f"\nNombre total de définitions: {dictionary.total_count}")
    print(f"Lettres: {', '.join(dictionary.letters())}")
    print(f"Catégories: {len(dictionary.categories())}")
    print(f"\nDéfinitions par lettre:")

    for letter in dictionary.letters():
        count = len(dictionary.get_by_letter(letter))
        print(f"  {letter}: {count}")


def show_menu():
    """Affiche le menu principal."""
    print("\n" + "=" * 60)
    print("  DICTIONNAIRE DE BITCOIN - Menu principal")
    print("=" * 60)
    print()
    print("  0. Build complet (PDF, INDEX, stats)")
    print("  1. Générer le PDF")
    print("  2. Mettre à jour INDEX.md")
    print("  3. Générer les statistiques")
    print("  4. Vérifier le markdown")
    print("  5. Corriger le markdown (auto-fix)")
    print("  6. Afficher les informations")
    print("  7. Quitter")
    print()


def main():
    # Charger le dictionnaire
    print("Chargement du dictionnaire...")
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")

    commands = {
        "0": cmd_build,
        "1": cmd_pdf,
        "2": cmd_index,
        "3": cmd_stats,
        "4": cmd_lint,
        "5": cmd_lint_fix,
        "6": cmd_info,
    }

    show_menu()

    try:
        choice = input("  Votre choix: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAu revoir!")
        return

    if choice == "7" or choice.lower() == "q":
        print("\nAu revoir!")
        return

    if choice in commands:
        try:
            commands[choice](dictionary)
        except Exception as e:
            print(f"\n[ERREUR] {e}")
            import traceback
            traceback.print_exc()
    else:
        print("\n[ERREUR] Choix invalide. Veuillez entrer un chiffre entre 0 et 7.")

    print("\nTerminé.")


if __name__ == "__main__":
    main()
