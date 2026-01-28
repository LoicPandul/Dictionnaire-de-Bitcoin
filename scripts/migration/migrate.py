#!/usr/bin/env python3
"""
Script de migration de l'ancienne structure vers la nouvelle.
Transforme les fichiers par lettre (A.md, B.md, etc.) en dossiers individuels par définition.
"""

import os
import re
import uuid
import shutil
import unicodedata
from pathlib import Path
from datetime import datetime

# Chemins
BASE_DIR = Path(__file__).parent.parent.parent
OLD_DICT_DIR = BASE_DIR / "dictionnaire"
NEW_DICT_DIR = BASE_DIR / "definitions" / "fr"
OLD_ASSETS_DIR = OLD_DICT_DIR / "assets"


def slugify(title: str) -> str:
    """Convertit un titre en slug (minuscules, tirets, sans accents)."""
    # Normaliser les accents
    title = unicodedata.normalize('NFKD', title)
    title = ''.join(c for c in title if not unicodedata.combining(c))
    # Minuscules
    title = title.lower()
    # Remplacer les espaces et caractères spéciaux par des tirets
    title = re.sub(r'[^a-z0-9]+', '-', title)
    # Nettoyer les tirets multiples
    title = re.sub(r'-+', '-', title)
    # Supprimer tirets début/fin
    return title.strip('-')


def get_first_letter(title: str) -> str:
    """Retourne la première lettre normalisée (sans accent) pour le classement."""
    # Normaliser les accents
    normalized = unicodedata.normalize('NFKD', title)
    first_char = ''.join(c for c in normalized if not unicodedata.combining(c))[0]
    return first_char.lower()


def parse_definition(raw_text: str) -> dict:
    """
    Parse une définition brute et extrait ses composants.

    Format attendu:
    ## TITRE
    ▪ **Catégorie**

    ► ***EN : ENGLISH TERM***  (optionnel)
    ► ***FR : TERME FRANÇAIS*** (optionnel)

    Corps de la définition...

    ![](assets/N.png)  (optionnel)

    > ► *Notes...* (optionnel)
    """
    lines = raw_text.strip().split('\n')

    definition = {
        'uuid': str(uuid.uuid4()),
        'title': '',
        'slug': '',
        'category': None,
        'english_term': None,
        'french_term': None,
        'content': '',
        'assets': [],
        'cross_references': []
    }

    # Première ligne = titre (sans le ##)
    if lines:
        definition['title'] = lines[0].strip()
        definition['slug'] = slugify(definition['title'])

    # Parser le reste
    content_lines = []
    i = 1

    while i < len(lines):
        line = lines[i]

        # Catégorie: ▪ **Catégorie**
        if line.strip().startswith('▪'):
            match = re.search(r'\*\*(.+?)\*\*', line)
            if match:
                definition['category'] = match.group(1)
            i += 1
            continue

        # Terme anglais: ► ***EN : TERM***
        if '► ***EN :' in line or '►***EN :' in line:
            match = re.search(r'\*\*\*EN\s*:\s*(.+?)\*\*\*', line)
            if match:
                definition['english_term'] = match.group(1).strip()
            i += 1
            continue

        # Terme français: ► ***FR : TERME***
        if '► ***FR :' in line or '►***FR :' in line:
            match = re.search(r'\*\*\*FR\s*:\s*(.+?)\*\*\*', line)
            if match:
                definition['french_term'] = match.group(1).strip()
            i += 1
            continue

        # Image: ![](assets/N.png)
        img_match = re.search(r'!\[\]\(assets/(\d+)\.png\)', line)
        if img_match:
            img_id = img_match.group(1)
            asset_index = len(definition['assets']) + 1
            definition['assets'].append({
                'filename': f'image-{asset_index}.png',
                'original_id': int(img_id)
            })
            # Remplacer le chemin dans le contenu
            line = re.sub(
                r'!\[\]\(assets/\d+\.png\)',
                f'![](./assets/image-{asset_index}.png)',
                line
            )

        # Références croisées: [**TERM**](./X.md#slug) ou [TERM](./X.md#slug)
        ref_matches = re.findall(r'\[(?:\*\*)?([^\]]+?)(?:\*\*)?\]\(\./([A-Za-z])\.md#([a-z0-9\-é]+)\)', line)
        for _, letter, ref_slug in ref_matches:
            if ref_slug not in definition['cross_references']:
                definition['cross_references'].append(ref_slug)

        content_lines.append(line)
        i += 1

    # Nettoyer le contenu (enlever les lignes vides au début)
    while content_lines and not content_lines[0].strip():
        content_lines.pop(0)

    definition['content'] = '\n'.join(content_lines)

    return definition


def parse_letter_file(filepath: Path) -> list:
    """Parse un fichier lettre et extrait toutes les définitions."""
    content = filepath.read_text(encoding='utf-8')

    # Split par ## (titre de définition)
    # On garde le délimiteur avec le split
    parts = re.split(r'^## ', content, flags=re.MULTILINE)

    definitions = []
    for part in parts[1:]:  # Skip le premier élément (avant le premier ##)
        if part.strip():
            definition = parse_definition(part)
            if definition['title']:
                definitions.append(definition)

    return definitions


def create_definition_folder(definition: dict, dry_run: bool = False) -> Path:
    """Crée le dossier et les fichiers pour une définition."""
    letter = get_first_letter(definition['title'])
    folder = NEW_DICT_DIR / letter / definition['slug']

    if dry_run:
        print(f"  [DRY RUN] Would create: {folder}")
        return folder

    # Créer le dossier
    folder.mkdir(parents=True, exist_ok=True)

    # Créer metadata.yaml
    metadata_lines = [
        f"uuid: \"{definition['uuid']}\"",
        f"title: \"{definition['title']}\"",
        f"slug: \"{definition['slug']}\"",
    ]

    if definition['category']:
        metadata_lines.append(f"category: \"{definition['category']}\"")

    if definition['english_term']:
        metadata_lines.append(f"english_term: \"{definition['english_term']}\"")

    if definition['french_term']:
        metadata_lines.append(f"french_term: \"{definition['french_term']}\"")

    if definition['cross_references']:
        metadata_lines.append("cross_references:")
        for ref in definition['cross_references']:
            metadata_lines.append(f"  - \"{ref}\"")

    if definition['assets']:
        metadata_lines.append("assets:")
        for asset in definition['assets']:
            metadata_lines.append(f"  - filename: \"{asset['filename']}\"")

    today = datetime.now().strftime('%Y-%m-%d')
    metadata_lines.append(f"created_at: \"{today}\"")
    metadata_lines.append(f"updated_at: \"{today}\"")

    metadata_path = folder / "metadata.yaml"
    metadata_path.write_text('\n'.join(metadata_lines), encoding='utf-8')

    # Créer definition.md
    content_path = folder / "definition.md"
    content_path.write_text(definition['content'], encoding='utf-8')

    # Copier les assets
    if definition['assets']:
        assets_folder = folder / "assets"
        assets_folder.mkdir(exist_ok=True)

        for asset in definition['assets']:
            src = OLD_ASSETS_DIR / f"{asset['original_id']}.png"
            dst = assets_folder / asset['filename']
            if src.exists():
                shutil.copy2(src, dst)
            else:
                print(f"  [WARNING] Image not found: {src}")

    return folder


def migrate(dry_run: bool = False):
    """Exécute la migration complète."""
    print("=" * 60)
    print("Migration du Dictionnaire de Bitcoin")
    print("=" * 60)

    if dry_run:
        print("\n[MODE DRY RUN - Aucune modification ne sera effectuée]\n")

    # Vérifier que le dossier source existe
    if not OLD_DICT_DIR.exists():
        print(f"ERREUR: Le dossier source n'existe pas: {OLD_DICT_DIR}")
        return

    # Créer le dossier de destination
    if not dry_run:
        NEW_DICT_DIR.mkdir(parents=True, exist_ok=True)

    total_definitions = 0
    total_assets = 0

    # Parser chaque fichier lettre
    for letter_file in sorted(OLD_DICT_DIR.glob("*.md")):
        letter = letter_file.stem.upper()
        print(f"\n[{letter}] Parsing {letter_file.name}...")

        definitions = parse_letter_file(letter_file)
        print(f"    Found {len(definitions)} definitions")

        for definition in definitions:
            create_definition_folder(definition, dry_run)
            total_definitions += 1
            total_assets += len(definition['assets'])

    print("\n" + "=" * 60)
    print(f"Migration {'(DRY RUN) ' if dry_run else ''}terminée!")
    print(f"  - Définitions migrées: {total_definitions}")
    print(f"  - Images copiées: {total_assets}")
    print("=" * 60)


def verify_migration():
    """Vérifie que la migration s'est bien passée."""
    print("\nVérification de la migration...")

    # Compter les définitions dans la nouvelle structure
    definition_count = 0
    for letter_dir in NEW_DICT_DIR.iterdir():
        if letter_dir.is_dir() and len(letter_dir.name) == 1:
            for def_dir in letter_dir.iterdir():
                if def_dir.is_dir():
                    metadata_file = def_dir / "metadata.yaml"
                    definition_file = def_dir / "definition.md"
                    if metadata_file.exists() and definition_file.exists():
                        definition_count += 1
                    else:
                        print(f"  [WARNING] Définition incomplète: {def_dir}")

    print(f"\nNombre de définitions dans la nouvelle structure: {definition_count}")

    # Comparer avec l'ancienne structure
    old_count = 0
    for letter_file in OLD_DICT_DIR.glob("*.md"):
        content = letter_file.read_text(encoding='utf-8')
        old_count += len(re.findall(r'^## ', content, flags=re.MULTILINE))

    print(f"Nombre de définitions dans l'ancienne structure: {old_count}")

    if definition_count == old_count:
        print("\n[OK] La migration est complète!")
    else:
        print(f"\n[WARNING] Différence de {abs(definition_count - old_count)} définition(s)")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Migration du Dictionnaire de Bitcoin")
    parser.add_argument('--dry-run', action='store_true', help="Simuler sans modifier les fichiers")
    parser.add_argument('--verify', action='store_true', help="Vérifier la migration")

    args = parser.parse_args()

    if args.verify:
        verify_migration()
    else:
        migrate(dry_run=args.dry_run)
        if not args.dry_run:
            verify_migration()
