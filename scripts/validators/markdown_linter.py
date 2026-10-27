#!/usr/bin/env python3
"""
Normalisation et validation du markdown des définitions.
"""

import re
from pathlib import Path
from ..core.dictionary import Dictionary


def check(dictionary: Dictionary) -> list:
    """Retourne la liste des problèmes de markdown, sans rien modifier."""
    return [f"[{i['slug']}] {i['message']}" for d in dictionary for i in _check_definition(d)]


def fix(dictionary: Dictionary) -> int:
    """Corrige les problèmes que l'on sait corriger. Retourne le nombre de corrections."""
    fixed = 0
    for definition in dictionary:
        issues = _check_definition(definition)
        if issues and _fix_definition(definition, issues, dictionary):
            fixed += len(issues)
    return fixed


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
