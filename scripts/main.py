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
from scripts.generators import pdf_generator, epub_generator, index_generator, stats_generator
from scripts.validators import markdown_linter
from scripts.config import DEFINITIONS_DIR


def cmd_build(dictionary):
    """Génère tous les formats."""
    print("\n" + "=" * 60)
    print("Build complet du Dictionnaire de Bitcoin")
    print("=" * 60)

    # 1. Lint
    print("\n--- Étape 1/4: Validation du markdown ---")
    markdown_linter.lint(dictionary, fix=False)

    # 2. Index
    print("\n--- Étape 2/4: Génération de l'index ---")
    index_generator.generate(dictionary)

    # 3. Stats
    print("\n--- Étape 3/4: Génération des statistiques ---")
    stats_generator.generate(dictionary)

    # 4. PDF
    print("\n--- Étape 4/4: Génération du PDF ---")
    pdf_generator.generate(dictionary)

    # 5. EPUB
    print("\n--- Étape 5/5: Génération de l'EPUB ---")
    epub_generator.generate(dictionary)

    print("\n" + "=" * 60)
    print("Build terminé!")
    print("=" * 60)


def cmd_pdf(dictionary):
    """Génère le PDF."""
    print("\nGénération du PDF...")
    pdf_generator.generate(dictionary)
    print("PDF généré!")


def cmd_epub(dictionary):
    """Génère l'EPUB."""
    print("\nGénération de l'EPUB...")
    epub_generator.generate(dictionary)
    print("EPUB généré!")


def cmd_index(dictionary):
    """Met à jour l'index."""
    print("\nMise à jour de l'index...")
    index_generator.generate(dictionary)
    print("INDEX.md mis à jour!")


def cmd_stats(dictionary):
    """Génère les statistiques."""
    print("\nGénération des statistiques...")
    stats_generator.generate(dictionary)
    print("stats.md généré!")


def cmd_lint(dictionary):
    """Vérifie le markdown."""
    print("\nVérification du markdown...")
    markdown_linter.lint(dictionary, fix=False)


def cmd_lint_fix(dictionary):
    """Corrige automatiquement le markdown."""
    print("\nCorrection automatique du markdown...")
    markdown_linter.lint(dictionary, fix=True)
    print("Corrections appliquées!")


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
    print("  0. Build complet (PDF, EPUB, INDEX, stats)")
    print("  1. Générer le PDF")
    print("  2. Générer l'EPUB")
    print("  3. Mettre à jour INDEX.md")
    print("  4. Générer les statistiques")
    print("  5. Vérifier le markdown")
    print("  6. Corriger le markdown (auto-fix)")
    print("  7. Afficher les informations")
    print("  8. Quitter")
    print()


def main():
    # Charger le dictionnaire
    print("Chargement du dictionnaire...")
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")

    commands = {
        "0": cmd_build,
        "1": cmd_pdf,
        "2": cmd_epub,
        "3": cmd_index,
        "4": cmd_stats,
        "5": cmd_lint,
        "6": cmd_lint_fix,
        "7": cmd_info,
    }

    while True:
        show_menu()

        try:
            choice = input("  Votre choix: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nAu revoir!")
            break

        if choice == "8" or choice.lower() == "q":
            print("\nAu revoir!")
            break

        if choice in commands:
            try:
                commands[choice](dictionary)
            except Exception as e:
                print(f"\n[ERREUR] {e}")
        else:
            print("\n[ERREUR] Choix invalide. Veuillez entrer un chiffre entre 0 et 8.")

        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
