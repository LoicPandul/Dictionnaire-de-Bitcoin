#!/usr/bin/env python3
"""
Migration vers le rangement bilingue du dépôt (docs/structure.md).

    python3 scripts/migrations/structure_bilingue.py            # simulation : affiche ce qui changerait
    python3 scripts/migrations/structure_bilingue.py --apply    # applique (git mv + mise à jour des chemins)

Le script :
  1. déplace les fichiers avec `git mv` (l'historique suit) ;
  2. réécrit les chemins cités dans les fichiers texte suivis (README, docs, scripts, YAML) ;
  3. remplace l'arbre du README par l'arbre cible de docs/structure.md ;
  4. lance `python3 scripts/main.py check`.

Les fichiers markdown déplacés (charte, docs/edition-2027/) n'ont que des liens vers des
fichiers voisins, qui suivent le déplacement : seuls les chemins cités depuis l'extérieur
sont réécrits. Il ne touche ni au contenu des définitions ni à leurs dossiers : definitions/fr et
chronologie/fr sont déjà à leur place. Il est idempotent : un déplacement déjà fait est
ignoré, et une seconde exécution ne change rien. Il refuse de tourner si l'arbre de travail
contient des modifications non commitées (sauf --allow-dirty), pour que la migration tienne
dans un commit à part, facile à relire.
"""

import argparse
import functools
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
print = functools.partial(print, flush=True)  # garder l'ordre avec la sortie de check

# (ancien chemin, nouveau chemin), relatifs à la racine du dépôt.
MOVES = [
    ("specifications/bip.yaml", "specifications/fr/bip.yaml"),
    ("specifications/bolt.yaml", "specifications/fr/bolt.yaml"),
    ("specifications/blip.yaml", "specifications/fr/blip.yaml"),
    ("specifications/nip.yaml", "specifications/fr/nip.yaml"),
    ("templates/introduction.md", "templates/fr/introduction.md"),
    ("templates/contributors.md", "templates/fr/contributors.md"),
    ("templates/legal.yaml", "templates/fr/legal.yaml"),
    ("templates/excluded_words.yaml", "templates/fr/excluded_words.yaml"),
    ("templates/pending_terms.yaml", "templates/fr/pending_terms.yaml"),
    ("STYLE_GUIDE.md", "docs/charte-editoriale.md"),
    ("edition-2027", "docs/edition-2027"),
    ("fonts", "assets/fonts"),
]

# Réécriture des chemins cités dans le texte. Les regex excluent ce qui est déjà migré et
# les faux amis (« feat/edition-2027 », « /fonts/ » d'une URL, « specifications/fr/ »).
REWRITES = [
    (re.compile(r"(?<![\w/.-])specifications/(?!fr/|en/)(bip|bolt|blip|nip|\*|<[^>/]+>)\.yaml"),
     r"specifications/fr/\1.yaml"),
    (re.compile(r"(?<![\w/.-])templates/(introduction\.md|contributors\.md|legal\.yaml|excluded_words\.yaml|pending_terms\.yaml)"),
     r"templates/fr/\1"),
    (re.compile(r"(?<![\w/.-])(\./)?STYLE_GUIDE\.md"), r"\1docs/charte-editoriale.md"),
    (re.compile(r"(?<![\w/.-])(\./)?edition-2027/"), r"\1docs/edition-2027/"),
    (re.compile(r"(?<![\w/.-])(\./)?fonts/(?=static|Archivo|Atkinson|\)|`|\s|$)"), r"\1assets/fonts/"),
]

# Fichiers dont on réécrit les chemins : texte suivi par git, hors contenu du dictionnaire.
TEXT_SUFFIXES = {".md", ".py", ".yaml", ".yml", ".mjs", ".js", ".json", ".tsv", ".txt", ".toml"}
SKIP_PREFIXES = ("definitions/", "chronologie/", "scripts/migrations/", "site/node_modules/",
                 "docs/structure.md")  # structure.md cite les anciens chemins à dessein

TREE_BEGIN, TREE_END = "<!-- arbre:debut -->", "<!-- arbre:fin -->"


def git(*args, check=True) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=check).stdout


def tracked_text_files():
    for name in git("ls-files").splitlines():
        if name.startswith(SKIP_PREFIXES) or Path(name).suffix not in TEXT_SUFFIXES:
            continue
        path = ROOT / name
        if path.is_file():
            yield name, path


def plan_moves():
    todo = []
    for old, new in MOVES:
        if (ROOT / old).exists() and not (ROOT / new).exists():
            todo.append((old, new))
        elif (ROOT / old).exists() and (ROOT / new).exists():
            print(f"  [ATTENTION] {old} et {new} existent tous les deux : fusion à faire à la main")
    return todo


def plan_rewrites(moved_to: dict):
    """(chemin, ancien texte, nouveau texte) pour chaque fichier dont un chemin cité change."""
    changes = []
    for name, path in tracked_text_files():
        name = moved_to.get(name, name)
        path = ROOT / name if (ROOT / name).exists() else path
        text = path.read_text(encoding="utf-8", errors="strict")
        new = text
        for pattern, repl in REWRITES:
            new = pattern.sub(repl, new)
        if new != text:
            changes.append((name, text, new))
    return changes


def target_tree() -> str:
    doc = (ROOT / "docs" / "structure.md").read_text(encoding="utf-8")
    m = re.search(re.escape(TREE_BEGIN) + r"\n(.*?)\n" + re.escape(TREE_END), doc, re.S)
    if not m:
        sys.exit("docs/structure.md : arbre cible introuvable entre les marqueurs")
    return m.group(1)


def replace_readme_tree(apply: bool) -> bool:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(TREE_BEGIN) + r"\n.*?\n" + re.escape(TREE_END), re.S)
    if not pattern.search(text):
        print("  [ATTENTION] README.md : marqueurs de l'arbre absents, arbre non remplacé")
        return False
    new = pattern.sub(lambda _: f"{TREE_BEGIN}\n{target_tree()}\n{TREE_END}", text)
    if new == text:
        return False
    if apply:
        readme.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="appliquer (sinon simulation)")
    ap.add_argument("--allow-dirty", action="store_true", help="accepter un arbre de travail modifié")
    ap.add_argument("--no-check", action="store_true", help="ne pas lancer main.py check à la fin")
    args = ap.parse_args()

    if args.apply and not args.allow_dirty and git("status", "--porcelain").strip():
        print("[ERREUR] L'arbre de travail contient des modifications : commitez-les d'abord "
              "(ou --allow-dirty).")
        return 1

    mode = "APPLICATION" if args.apply else "SIMULATION (rien n'est modifié ; --apply pour appliquer)"
    print(f"Migration vers le rangement bilingue : {mode}\n")

    moves = plan_moves()
    print(f"Déplacements ({len(moves)}) :")
    for old, new in moves:
        print(f"  git mv {old} {new}")
        if args.apply:
            (ROOT / new).parent.mkdir(parents=True, exist_ok=True)
            git("mv", old, new)
    if not moves:
        print("  aucun (déjà fait)")

    # En simulation, les fichiers n'ont pas bougé : on lit les anciens chemins.
    moved_to = {}
    if args.apply:
        for old, new in moves:
            for name in git("ls-files", new).splitlines():
                moved_to[old + name[len(new):]] = name
    changes = plan_rewrites(moved_to if args.apply else {})
    print(f"\nChemins réécrits dans {len(changes)} fichier(s) :")
    for name, old_text, new_text in changes:
        old_lines, new_lines = old_text.splitlines(), new_text.splitlines()
        n = sum(1 for a, b in zip(old_lines, new_lines) if a != b)
        print(f"  {name} ({n} ligne(s))")
        if args.apply:
            (ROOT / name).write_text(new_text, encoding="utf-8")

    if replace_readme_tree(args.apply):
        print("\nREADME.md : arbre du dépôt remplacé par l'arbre cible de docs/structure.md")

    if args.apply and not args.no_check:
        print("\n$ python3 scripts/main.py check")
        r = subprocess.run([sys.executable, "scripts/main.py", "check"], cwd=ROOT)
        if r.returncode != 0:
            return r.returncode
        print("\nMigration appliquée. Relisez `git status`, puis commitez en un seul commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
