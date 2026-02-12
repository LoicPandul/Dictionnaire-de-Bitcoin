#!/usr/bin/env python3
"""
Script de migration des cross-references (one-time).

1. Transforme les blockquotes ► en paragraphes italiques dans les definition.md
2. Supprime les phrases "Pour plus d'informations..." et les termes liés
3. Convertit les cross_references de slugs en UUIDs dans les metadata.yaml
"""

import re
import unicodedata
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFINITIONS_DIR = BASE_DIR / "definitions" / "fr"


def _strip_accents(text: str) -> str:
    """Retire les accents d'une chaîne (NFD → ASCII)."""
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


def build_slug_to_uuid_map() -> dict:
    """Construit un mapping slug → uuid depuis tous les metadata.yaml.

    Retourne aussi un mapping secondaire sans accents pour le fallback.
    """
    mapping = {}
    mapping_no_accent = {}
    for letter_dir in sorted(DEFINITIONS_DIR.iterdir()):
        if not letter_dir.is_dir() or len(letter_dir.name) != 1:
            continue
        for def_dir in sorted(letter_dir.iterdir()):
            if not def_dir.is_dir():
                continue
            meta_path = def_dir / "metadata.yaml"
            if not meta_path.exists():
                continue
            with open(meta_path, 'r', encoding='utf-8') as f:
                metadata = yaml.safe_load(f)
            if metadata and 'slug' in metadata and 'uuid' in metadata:
                slug = metadata['slug']
                mapping[slug] = metadata['uuid']
                mapping_no_accent[_strip_accents(slug)] = metadata['uuid']
    return mapping, mapping_no_accent


def process_definition_md(filepath: Path) -> bool:
    """Traite un fichier definition.md pour transformer les blockquotes ►.

    - Retire le préfixe '> ► ' (blockquote + flèche)
    - Supprime les phrases "Pour plus d'informations,..." jusqu'à la fin
    - Conserve le texte restant en italique comme paragraphe normal
    - Supprime la ligne entièrement si elle ne contient plus rien après nettoyage
    - NE TOUCHE PAS aux blockquotes sans ► (vraies citations)

    Returns True if the file was modified.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    modified = False

    for line in lines:
        if line.startswith('> ► '):
            modified = True
            # Retirer le préfixe blockquote + flèche
            inner = line[4:].strip()

            # Retirer les marqueurs italiques extérieurs *...*
            if inner.startswith('*') and inner.endswith('*') and len(inner) > 2:
                inner_text = inner[1:-1]
            else:
                inner_text = inner

            # Supprimer "Pour plus d'informations,..." jusqu'à la fin
            inner_text = re.sub(
                r'\s*Pour plus d\'informations,.*$',
                '',
                inner_text
            )

            # Nettoyer
            inner_text = inner_text.strip()

            # Si le contenu est vide après suppression, ne pas ajouter la ligne
            if not inner_text:
                continue

            # Remettre en italique comme paragraphe normal
            new_lines.append(f'*{inner_text}*')
        else:
            new_lines.append(line)

    if not modified:
        return False

    # Nettoyer les lignes vides multiples consécutives en fin de fichier
    while len(new_lines) > 1 and new_lines[-1] == '' and new_lines[-2] == '':
        new_lines.pop()

    new_content = '\n'.join(new_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True


def update_metadata_cross_refs(filepath: Path, slug_to_uuid: dict, slug_no_accent: dict) -> tuple:
    """Met à jour les cross_references de slugs vers UUIDs dans un metadata.yaml.

    Fait un remplacement textuel pour préserver le formatage du fichier.
    Utilise un fallback sans accents si le slug exact n'est pas trouvé.

    Returns (modified, unresolved_slugs)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = yaml.safe_load(content)
    if not metadata or 'cross_references' not in metadata:
        return False, []

    cross_refs = metadata['cross_references']
    if not cross_refs:
        return False, []

    modified = False
    unresolved = []
    new_content = content

    for ref in cross_refs:
        # Skip si déjà un UUID
        if re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', ref):
            continue

        # Chercher d'abord par slug exact, puis par slug sans accents
        uuid = slug_to_uuid.get(ref)
        if not uuid:
            uuid = slug_no_accent.get(_strip_accents(ref))

        if uuid:
            # Remplacer le slug par l'UUID dans le texte (différents formats de citation)
            for pattern in [f'"{ref}"', f"'{ref}'"]:
                if pattern in new_content:
                    new_content = new_content.replace(pattern, f'"{uuid}"', 1)
                    modified = True
                    break
            else:
                # Sans guillemets : "  - slug\n"
                old = f'  - {ref}\n'
                new = f'  - "{uuid}"\n'
                if old in new_content:
                    new_content = new_content.replace(old, new, 1)
                    modified = True
        else:
            unresolved.append(ref)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return modified, unresolved


def main():
    print("=== Migration des cross-references ===\n")

    # 1. Construire le mapping slug → uuid
    print("1. Construction du mapping slug -> uuid...")
    slug_to_uuid, slug_no_accent = build_slug_to_uuid_map()
    print(f"   {len(slug_to_uuid)} definitions indexees.\n")

    # 2. Traiter les fichiers definition.md
    print("2. Transformation des blockquotes dans les definition.md...")
    md_modified = 0
    md_total = 0

    for letter_dir in sorted(DEFINITIONS_DIR.iterdir()):
        if not letter_dir.is_dir() or len(letter_dir.name) != 1:
            continue
        for def_dir in sorted(letter_dir.iterdir()):
            if not def_dir.is_dir():
                continue
            md_path = def_dir / "definition.md"
            if not md_path.exists():
                continue
            md_total += 1
            if process_definition_md(md_path):
                md_modified += 1

    print(f"   {md_modified}/{md_total} fichiers modifies.\n")

    # 3. Convertir les cross_references en UUIDs
    print("3. Conversion des cross_references (slug -> uuid)...")
    meta_modified = 0
    meta_total = 0
    all_unresolved = []

    for letter_dir in sorted(DEFINITIONS_DIR.iterdir()):
        if not letter_dir.is_dir() or len(letter_dir.name) != 1:
            continue
        for def_dir in sorted(letter_dir.iterdir()):
            if not def_dir.is_dir():
                continue
            meta_path = def_dir / "metadata.yaml"
            if not meta_path.exists():
                continue
            meta_total += 1
            modified, unresolved = update_metadata_cross_refs(meta_path, slug_to_uuid, slug_no_accent)
            if modified:
                meta_modified += 1
            if unresolved:
                all_unresolved.extend([(meta_path, s) for s in unresolved])

    print(f"   {meta_modified}/{meta_total} fichiers modifies.\n")

    if all_unresolved:
        print("ATTENTION - Slugs non resolus:")
        for path, slug in all_unresolved:
            rel = path.relative_to(BASE_DIR)
            print(f"   - {slug} (dans {rel})")

    print("\n=== Migration terminee ===")


if __name__ == "__main__":
    main()
