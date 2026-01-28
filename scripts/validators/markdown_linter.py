#!/usr/bin/env python3
"""
Normalisation et validation du markdown des définitions.
"""

import re
from pathlib import Path
from ..core.dictionary import Dictionary


def lint(dictionary: Dictionary, fix: bool = False, verbose: bool = True) -> bool:
    """
    Vérifie et normalise le markdown des définitions.

    Args:
        dictionary: Le dictionnaire à vérifier
        fix: Si True, corrige automatiquement les problèmes
        verbose: Si True, affiche les détails

    Returns:
        True si tout est OK (ou corrigé), False sinon.
    """
    print("Vérification du markdown...")

    issues = []
    fixed = 0

    for definition in dictionary:
        definition_issues = _check_definition(definition)

        if definition_issues:
            issues.extend(definition_issues)

            if fix:
                _fix_definition(definition, definition_issues)
                fixed += len(definition_issues)

    if issues and not fix:
        print(f"\n[WARNING] {len(issues)} problème(s) trouvé(s):")
        for issue in issues[:20]:  # Limiter l'affichage
            print(f"  [{issue['slug']}] {issue['message']}")
        if len(issues) > 20:
            print(f"  ... et {len(issues) - 20} autres")
        return False

    if fix and fixed > 0:
        print(f"[OK] {fixed} problème(s) corrigé(s)")

    print(f"[OK] Markdown validé")
    return True


def _check_definition(definition) -> list:
    """Vérifie une définition individuelle."""
    issues = []
    content = definition.content

    # Vérifier les listes avec tirets au lieu d'astérisques
    if re.search(r'^- ', content, re.MULTILINE):
        issues.append({
            'slug': definition.slug,
            'type': 'list_dash',
            'message': "Utilise des tirets '-' au lieu d'astérisques '*' pour les listes"
        })

    # Vérifier les citations sans ligne vide avant
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('>') and i > 0:
            prev_line = lines[i - 1].strip()
            if prev_line and not prev_line.startswith('>'):
                issues.append({
                    'slug': definition.slug,
                    'type': 'quote_spacing',
                    'message': f"Citation sans ligne vide avant (ligne {i + 1})"
                })

    # Vérifier les liens cassés potentiels
    broken_links = re.findall(r'\[([^\]]+)\]\(([^)]*)\)', content)
    for text, url in broken_links:
        if url.startswith('./') and '.md#' in url:
            # Ancien format de lien interne
            issues.append({
                'slug': definition.slug,
                'type': 'old_link_format',
                'message': f"Ancien format de lien: [{text}]({url})"
            })

    return issues


def _fix_definition(definition, issues) -> bool:
    """Corrige les problèmes d'une définition."""
    content_path = definition.path / "definition.md"
    content = content_path.read_text(encoding='utf-8')
    modified = False

    for issue in issues:
        if issue['type'] == 'list_dash':
            # Remplacer les tirets par des astérisques
            content = re.sub(r'^- ', '* ', content, flags=re.MULTILINE)
            modified = True

        elif issue['type'] == 'quote_spacing':
            # Ajouter une ligne vide avant les citations
            lines = content.split('\n')
            new_lines = []
            for i, line in enumerate(lines):
                if line.startswith('>') and i > 0:
                    prev_line = lines[i - 1].strip()
                    if prev_line and not prev_line.startswith('>'):
                        new_lines.append('')
                new_lines.append(line)
            content = '\n'.join(new_lines)
            modified = True

    if modified:
        content_path.write_text(content, encoding='utf-8')

    return modified


def normalize_all(dictionary: Dictionary) -> int:
    """Normalise tout le markdown du dictionnaire."""
    return lint(dictionary, fix=True, verbose=True)
