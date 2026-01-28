#!/usr/bin/env python3
"""
Génération des statistiques du dictionnaire.
"""

import re
from pathlib import Path
from collections import Counter
from datetime import datetime

from ..core.dictionary import Dictionary
from ..config import OUTPUT_STATS, README_FILE


def generate(dictionary: Dictionary, output_path: Path = None, update_readme: bool = True):
    """Génère le fichier stats.md et met à jour le badge du README."""
    if output_path is None:
        output_path = OUTPUT_STATS

    print(f"Génération des statistiques: {output_path}")

    stats = dictionary.stats()

    lines = []

    # En-tête
    lines.append("# Statistiques du Dictionnaire de Bitcoin")
    lines.append("")
    lines.append(f"*Dernière mise à jour : {datetime.now().strftime('%d/%m/%Y à %H:%M')}*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Statistiques globales
    lines.append("## Statistiques globales")
    lines.append("")
    lines.append(f"- **Nombre total de définitions** : {stats['total_definitions']}")
    lines.append(f"- **Nombre de lettres utilisées** : {stats['letters']}")
    lines.append(f"- **Nombre de catégories** : {stats['categories']}")
    lines.append("")

    # Définitions par lettre
    lines.append("## Définitions par lettre")
    lines.append("")
    lines.append("| Lettre | Nombre |")
    lines.append("|:------:|-------:|")

    for letter in sorted(stats['definitions_per_letter'].keys()):
        count = stats['definitions_per_letter'][letter]
        lines.append(f"| {letter} | {count} |")

    lines.append("")

    # Top lettres
    lines.append("## Top 5 des lettres les plus fournies")
    lines.append("")

    sorted_letters = sorted(
        stats['definitions_per_letter'].items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    for i, (letter, count) in enumerate(sorted_letters, 1):
        lines.append(f"{i}. **{letter}** : {count} définitions")

    lines.append("")

    # Catégories
    lines.append("## Catégories")
    lines.append("")

    category_counts = Counter()
    for definition in dictionary:
        if definition.category:
            category_counts[definition.category] += 1

    for category, count in category_counts.most_common():
        lines.append(f"- **{category}** : {count}")

    lines.append("")

    # Termes les plus fréquents dans le contenu
    lines.append("## Termes les plus fréquents")
    lines.append("")

    word_counts = _count_frequent_words(dictionary)
    for word, count in word_counts.most_common(15):
        lines.append(f"- **{word}** : {count} occurrences")

    # Écrire le fichier
    output_path.write_text("\n".join(lines), encoding='utf-8')
    print(f"[OK] Statistiques générées: {output_path}")

    # Mettre à jour le badge du README
    if update_readme:
        _update_readme_badge(stats['total_definitions'])

    return True


def _count_frequent_words(dictionary: Dictionary) -> Counter:
    """Compte les mots les plus fréquents dans les définitions."""
    # Mots à ignorer (stop words français + termes trop communs)
    stop_words = {
        'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'ou', 'en',
        'est', 'sont', 'pour', 'par', 'sur', 'dans', 'avec', 'qui', 'que',
        'ce', 'cette', 'ces', 'il', 'elle', 'ils', 'elles', 'on', 'nous',
        'vous', 'leur', 'leurs', 'son', 'sa', 'ses', 'au', 'aux', 'se',
        'ne', 'pas', 'plus', 'peut', 'être', 'avoir', 'faire', 'comme',
        'tout', 'tous', 'toute', 'toutes', 'autre', 'autres', 'même',
        'donc', 'ainsi', 'alors', 'si', 'mais', 'car', 'donc', 'ni',
        'à', 'y', 'a', 'été', 'aussi', 'entre', 'sous', 'vers', 'chez',
        'sans', 'depuis', 'lors', 'encore', 'très', 'bien', 'peu', 'où'
    }

    word_counts = Counter()

    for definition in dictionary:
        # Nettoyer le contenu
        content = definition.content.lower()
        # Extraire les mots (lettres et chiffres uniquement)
        words = re.findall(r'\b[a-zàâäéèêëïîôùûüç]{4,}\b', content)

        for word in words:
            if word not in stop_words:
                word_counts[word] += 1

    return word_counts


def _update_readme_badge(total_count: int):
    """Met à jour le badge du nombre de définitions dans le README."""
    if not README_FILE.exists():
        print("[WARNING] README.md not found")
        return

    content = README_FILE.read_text(encoding='utf-8')

    # Chercher et remplacer le badge
    pattern = r'(Nombre%20de%20définitions-)\d+(-black)'
    replacement = f'\\g<1>{total_count}\\g<2>'

    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        README_FILE.write_text(new_content, encoding='utf-8')
        print(f"[OK] Badge README mis à jour: {total_count} définitions")
    else:
        print("[INFO] Badge README déjà à jour")
