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
    fixed_count = 0

    for definition in dictionary:
        definition_issues = _check_definition(definition)

        if definition_issues:
            issues.extend(definition_issues)

            if fix:
                if _fix_definition(definition, definition_issues, dictionary):
                    fixed_count += len(definition_issues)

    if fix and fixed_count > 0:
        print(f"[OK] {fixed_count} problème(s) corrigé(s)")
        return True

    if issues and not fix:
        print(f"\n[WARNING] {len(issues)} problème(s) trouvé(s):")
        for issue in issues[:20]:  # Limiter l'affichage
            print(f"  [{issue['slug']}] {issue['message']}")
        if len(issues) > 20:
            print(f"  ... et {len(issues) - 20} autres")
        return False

    if not issues:
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

    # Vérifier les liens avec l'ancien format (./X.md#slug)
    old_links = re.findall(r'\[([^\]]+)\]\(\./([A-Za-z])\.md#([a-z0-9\-éèàùâêîôûäëïöü]+)\)', content)
    for text, letter, slug in old_links:
        issues.append({
            'slug': definition.slug,
            'type': 'old_link_format',
            'message': f"Ancien format de lien: [{text}](./{ letter}.md#{slug})",
            'data': {'text': text, 'letter': letter.lower(), 'target_slug': slug}
        })

    return issues


def _fix_definition(definition, issues, dictionary) -> bool:
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

        elif issue['type'] == 'old_link_format':
            # Convertir l'ancien format de lien vers le nouveau format
            data = issue['data']
            text = data['text']
            letter = data['letter']
            target_slug = data['target_slug']

            # Ancien format: [TEXT](./X.md#slug)
            # Nouveau format: [TEXT](../x/slug/definition.md)
            old_pattern = re.escape(f"[{text}](./") + r"[A-Za-z]\.md#" + re.escape(target_slug) + r"\)"
            new_link = f"[{text}](../{letter}/{target_slug}/definition.md)"

            content = re.sub(old_pattern, new_link, content, flags=re.IGNORECASE)
            modified = True

    if modified:
        content_path.write_text(content, encoding='utf-8')

    return modified


def normalize_all(dictionary: Dictionary) -> int:
    """Normalise tout le markdown du dictionnaire."""
    return lint(dictionary, fix=True, verbose=True)
