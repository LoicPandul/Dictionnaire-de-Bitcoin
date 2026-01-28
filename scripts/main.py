#!/usr/bin/env python3
"""
Dictionnaire de Bitcoin - Script principal

Usage:
    python scripts/main.py build      # Génère tout (PDF, EPUB, INDEX, stats)
    python scripts/main.py pdf        # Génère uniquement le PDF
    python scripts/main.py epub       # Génère uniquement l'EPUB
    python scripts/main.py index      # Met à jour INDEX.md
    python scripts/main.py stats      # Génère stats.md
    python scripts/main.py validate   # Valide le dictionnaire
    python scripts/main.py lint       # Normalise le markdown
    python scripts/main.py lint --fix # Corrige automatiquement le markdown
"""

import sys
import argparse
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.core.dictionary import Dictionary
from scripts.generators import pdf_generator, epub_generator, index_generator, stats_generator
from scripts.validators import alphabetical, markdown_linter
from scripts.config import DEFINITIONS_DIR


def cmd_build(args):
    """Génère tous les formats."""
    print("=" * 60)
    print("Build complet du Dictionnaire de Bitcoin")
    print("=" * 60)

    dictionary = Dictionary.load()
    print(f"\nChargé: {dictionary.total_count} définitions\n")

    # 1. Lint
    print("\n--- Étape 1/5: Validation du markdown ---")
    markdown_linter.lint(dictionary, fix=False)

    # 2. Index
    print("\n--- Étape 2/5: Génération de l'index ---")
    index_generator.generate(dictionary)

    # 3. Stats
    print("\n--- Étape 3/5: Génération des statistiques ---")
    stats_generator.generate(dictionary)

    # 4. PDF
    print("\n--- Étape 4/5: Génération du PDF ---")
    pdf_generator.generate(dictionary)

    # 5. EPUB
    print("\n--- Étape 5/5: Génération de l'EPUB ---")
    epub_generator.generate(dictionary)

    print("\n" + "=" * 60)
    print("Build terminé!")
    print("=" * 60)


def cmd_pdf(args):
    """Génère le PDF."""
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")
    pdf_generator.generate(dictionary)


def cmd_epub(args):
    """Génère l'EPUB."""
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")
    epub_generator.generate(dictionary)


def cmd_index(args):
    """Met à jour l'index."""
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")
    index_generator.generate(dictionary)


def cmd_stats(args):
    """Génère les statistiques."""
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")
    stats_generator.generate(dictionary)


def cmd_validate(args):
    """Valide le dictionnaire."""
    print("=" * 60)
    print("Validation du Dictionnaire de Bitcoin")
    print("=" * 60)

    dictionary = Dictionary.load()
    print(f"\nChargé: {dictionary.total_count} définitions\n")

    all_valid = True

    # Vérifier l'ordre alphabétique
    if not alphabetical.validate(dictionary):
        all_valid = False

    # Vérifier le markdown
    if not markdown_linter.lint(dictionary, fix=False):
        all_valid = False

    print("\n" + "=" * 60)
    if all_valid:
        print("Validation réussie!")
    else:
        print("Validation échouée - voir les erreurs ci-dessus")
        sys.exit(1)
    print("=" * 60)


def cmd_lint(args):
    """Normalise le markdown."""
    dictionary = Dictionary.load()
    print(f"Chargé: {dictionary.total_count} définitions")

    if args.fix:
        markdown_linter.lint(dictionary, fix=True)
    else:
        markdown_linter.lint(dictionary, fix=False)


def cmd_info(args):
    """Affiche les informations du dictionnaire."""
    dictionary = Dictionary.load()

    print("=" * 60)
    print("Dictionnaire de Bitcoin - Informations")
    print("=" * 60)
    print(f"\nNombre total de définitions: {dictionary.total_count}")
    print(f"Lettres: {', '.join(dictionary.letters())}")
    print(f"Catégories: {len(dictionary.categories())}")
    print(f"\nDéfinitions par lettre:")

    for letter in dictionary.letters():
        count = len(dictionary.get_by_letter(letter))
        print(f"  {letter}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Dictionnaire de Bitcoin - Outils de gestion",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    subparsers = parser.add_subparsers(dest="command", help="Commandes disponibles")

    # Commande build
    subparsers.add_parser("build", help="Génère tous les formats (PDF, EPUB, INDEX, stats)")

    # Commande pdf
    subparsers.add_parser("pdf", help="Génère uniquement le PDF")

    # Commande epub
    subparsers.add_parser("epub", help="Génère uniquement l'EPUB")

    # Commande index
    subparsers.add_parser("index", help="Met à jour INDEX.md")

    # Commande stats
    subparsers.add_parser("stats", help="Génère stats.md")

    # Commande validate
    subparsers.add_parser("validate", help="Valide le dictionnaire")

    # Commande lint
    lint_parser = subparsers.add_parser("lint", help="Normalise le markdown")
    lint_parser.add_argument("--fix", action="store_true", help="Corrige automatiquement les problèmes")

    # Commande info
    subparsers.add_parser("info", help="Affiche les informations du dictionnaire")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Dispatcher les commandes
    commands = {
        "build": cmd_build,
        "pdf": cmd_pdf,
        "epub": cmd_epub,
        "index": cmd_index,
        "stats": cmd_stats,
        "validate": cmd_validate,
        "lint": cmd_lint,
        "info": cmd_info,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
