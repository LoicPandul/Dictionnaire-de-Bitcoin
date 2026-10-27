#!/usr/bin/env python3
"""
Dictionnaire de Bitcoin : validation et génération.

    python3 scripts/main.py check                      # tout valider, sans rien modifier
    python3 scripts/main.py fix                        # corrections automatiques du markdown et des renvois
    python3 scripts/main.py build                      # toutes les éditions, tous les formats
    python3 scripts/main.py build --edition complete --format pdf,epub
    python3 scripts/main.py index | stats | info

Sans argument, un menu propose les mêmes commandes.
"""

import argparse
import subprocess
from collections import Counter
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import BUILD_DIR, find_epubcheck, find_tex_engine  # noqa: E402
from scripts.core.book import Book, load_editions  # noqa: E402
from scripts.core.dictionary import Dictionary  # noqa: E402
from scripts.generators import index_generator, pdf_generator, stats_generator  # noqa: E402
from scripts.core import translations  # noqa: E402
from scripts.validators import (  # noqa: E402
    content_validator, markdown_linter, metadata_validator, sync_checker, translation_checker)

FORMATS = ("pdf", "epub")


def _report(title: str, errors: list, limit: int = 40) -> bool:
    if not errors:
        print(f"[OK] {title}")
        return True
    print(f"[ERREUR] {title} : {len(errors)} problème(s)")
    for e in errors[:limit]:
        print(f"  ✗ {e}")
    if len(errors) > limit:
        print(f"  … et {len(errors) - limit} autre(s)")
    return False


def cmd_check(dictionary: Dictionary, args=None) -> bool:
    print(f"\n{dictionary.total_count} entrées chargées.")
    ok = _report("Métadonnées", metadata_validator.validate(dictionary))
    sync_errors, stats = sync_checker.check()
    ok &= _report(f"Versions courtes ({stats['courtes']} courtes / {stats['developpees']} développées)", sync_errors)
    ok &= _report("Markdown", markdown_linter.check(dictionary))
    ok &= _report("Spécifications (BIP, BOLT, bLIP)", content_validator.validate_specs(dictionary))
    ok &= _report("Chronologie", content_validator.validate_chronology(dictionary))
    ok &= _report("Traductions (structure)", translation_checker.validate(dictionary))
    for lang, (counts, _) in translation_checker.summary(dictionary).items():
        print(f"[INFO] Synchro {translation_checker.describe(lang, counts)} (détail : main.py sync)")
    print("\nValidation réussie." if ok else "\nValidation en échec.")
    return ok


def cmd_fix(dictionary: Dictionary, args=None) -> bool:
    n = markdown_linter.fix(dictionary)
    print(f"[OK] {n} correction(s) de markdown")
    n = metadata_validator.fix_cross_references(dictionary)
    print(f"[OK] {n} renvoi(s) invalide(s) retiré(s)")
    return True


def _epubcheck(path: Path) -> bool:
    command = find_epubcheck()
    if not command:
        print("[ATTENTION] epubcheck introuvable : EPUB non validé (voir scripts/README.md).")
        return True
    result = subprocess.run(command + [str(path)], capture_output=True, text=True, errors="replace")
    report = path.with_suffix(".epubcheck.txt")
    report.write_text(result.stdout + result.stderr, encoding="utf-8")
    summary = [l for l in (result.stdout + result.stderr).splitlines() if "Messages:" in l or "No errors" in l]
    print(f"  epubcheck : {' / '.join(summary) or 'voir ' + str(report)}")
    if result.returncode != 0:
        print(f"[ERREUR] epubcheck a trouvé des erreurs : {report}")
        return False
    print("[OK] epubcheck : aucune erreur")
    return True


def cmd_build(dictionary: Dictionary, args=None) -> bool:
    editions = load_editions()
    wanted_editions = list(editions) if not args or args.edition == "all" else args.edition.split(",")
    wanted_formats = FORMATS if not args or args.format == "all" else tuple(args.format.split(","))
    for f in wanted_formats:
        if f not in FORMATS:
            print(f"[ERREUR] format inconnu : {f} (formats : {', '.join(FORMATS)})")
            return False
    if not (args and args.force) and not cmd_check(dictionary):
        print("[ERREUR] Build interrompu : corrigez les erreurs ou relancez avec --force.")
        return False

    engine, _ = find_tex_engine()
    print(f"\nMoteur LaTeX : {engine or 'aucun'}")
    ok = True
    produced = []
    for edition_id in wanted_editions:
        book = Book(edition_id, dictionary, editions)
        print(f"\n=== Édition « {edition_id} » : {book.entry_count()} entrées, "
              f"{len(book.edition.sections)} sections ===")
        for w in book.warnings:
            print(f"  [ATTENTION] {w}")
        out_dir = (Path(args.output_dir) if args and args.output_dir else BUILD_DIR) / edition_id
        out_dir.mkdir(parents=True, exist_ok=True)
        if "pdf" in wanted_formats:
            path = pdf_generator.generate(book, out_dir)
            ok &= path is not None
            produced += [path] if path else []
        if "epub" in wanted_formats:
            from scripts.generators import epub_generator
            path = epub_generator.generate(book, out_dir)
            ok &= path is not None
            if path:
                produced.append(path)
                ok &= _epubcheck(path)
    print("\nFichiers produits :")
    for p in produced:
        print(f"  {p}")
    print("\nBuild terminé." if ok else "\nBuild terminé avec des erreurs.")
    return ok


def cmd_index(dictionary: Dictionary, args=None) -> bool:
    return index_generator.generate(dictionary)


def cmd_stats(dictionary: Dictionary, args=None) -> bool:
    return stats_generator.generate(dictionary)


def _find_pair(pairs, ref: str):
    for p in pairs:
        if ref in (p.uuid, getattr(p.source, "slug", None), getattr(p.translation, "slug", None)):
            return p
    return None


def cmd_sync(dictionary: Dictionary, args=None) -> bool:
    """État de la synchro entre la langue d'origine et chaque traduction (docs/traduction.md)."""
    languages = translations.load_languages()
    wanted = [args.lang] if args and args.lang else list(languages["translations"])
    part_of = dictionary.taxonomy.part_of if dictionary.taxonomy else None
    ok = True
    for lang in wanted:
        if lang not in languages["translations"]:
            print(f"[ERREUR] langue inconnue : {lang} (templates/languages.yaml)")
            return False
        scope = set(languages["translations"][lang].get("parts") or [])
        exclude = set(languages["translations"][lang].get("exclude") or [])
        all_pairs = translations.pairs(languages["source"], lang, part_of, exclude=exclude)

        if args and (args.mark or args.mark_unmarked):
            refs = list(args.mark or [])
            if args.mark_unmarked:
                refs += [p.uuid for p in all_pairs if p.status == translations.UNMARKED]
            for ref in refs:
                p = _find_pair(all_pairs, ref)
                if not p or not (p.source and p.translation):
                    print(f"[ERREUR] {ref} : pas de paire source/traduction à marquer")
                    ok = False
                    continue
                values = translations.mark(p.source, p.translation)
                p.status = translations.UP_TO_DATE
                print(f"  [{p.translation.lang}/{p.translation.slug}] synchro enregistrée "
                      f"({p.source.lang} {values['source_hash']} @ {values['source_commit'] or '?'})")
            continue

        if args and args.new:
            p = _find_pair(all_pairs, args.new)
            if not p or not p.source or p.translation:
                print(f"[ERREUR] {args.new} : entrée introuvable, ou déjà traduite")
                return False
            if not args.title:
                print("[ERREUR] --new demande --title « TITRE TRADUIT »")
                return False
            e = translations.create(p.source, lang, args.title, args.slug)
            print(f"[OK] {e.rel}/metadata.yaml créé. Écrivez definition.md et courte.md, "
                  f"puis : python3 scripts/main.py sync --mark {e.slug}")
            continue

        if args and args.diff:
            p = _find_pair(all_pairs, args.diff)
            if not p or not (p.source and p.translation):
                print(f"[ERREUR] {args.diff} : pas de paire source/traduction")
                return False
            commit = p.translation.meta.get("source_commit")
            print(f"Source : {p.source.rel}\nTraduction : {p.translation.rel}\nStatut : {p.status}")
            if not commit:
                print("Aucun source_commit : comparez les deux versions à la main.")
                return True
            print(f"Changements depuis {commit} :\n", flush=True)
            r = subprocess.run(["git", "diff", "--stat", "-p", commit, "--", p.source.rel, p.translation.rel],
                               cwd=Path(__file__).resolve().parent.parent, text=True)
            return r.returncode == 0

        by_part = {}
        for p in all_pairs:
            by_part.setdefault(p.part or "?", Counter())[p.status] += 1
        name = languages["translations"][lang].get("name", lang)
        print(f"\n{languages['source'].upper()} → {lang.upper()} ({name}), périmètre : {', '.join(sorted(scope)) or 'tout'}")
        print(f"  {'partie':<16}{'traduites':>10}{'manquantes':>12}{'à jour':>8}{'en retard':>11}"
              f"{'à reporter':>12}{'conflits':>10}{'à marquer':>11}")
        for part, c in sorted(by_part.items(), key=lambda kv: -sum(kv[1].values())):
            missing = c[translations.MISSING] + c[translations.ORIGIN_MISSING]
            done = sum(c.values()) - missing - c[translations.ORPHAN] - c[translations.EXCLUDED]
            flag = "" if (not scope or part in scope) else "  (hors périmètre)"
            print(f"  {part:<16}{done:>10}{missing:>12}{c[translations.UP_TO_DATE]:>8}"
                  f"{c[translations.TRANSLATION_BEHIND]:>11}{c[translations.SOURCE_BEHIND]:>12}"
                  f"{c[translations.CONFLICT]:>10}{c[translations.UNMARKED]:>11}{flag}")
        counts, _ = translation_checker.summary(dictionary)[lang]
        print(f"  Dans le périmètre : {translation_checker.describe(lang, counts)}")

        listed = [s for s in translations.STATUSES if s not in (translations.UP_TO_DATE, translations.EXCLUDED)]
        if args and args.list:
            # Les entrées manquantes se comptent par centaines : on les liste seulement sur demande.
            listed = [s for s in listed if s == args.list or (args.list == "all" and s != translations.MISSING)]
            for status in listed:
                rows = [p for p in all_pairs if p.status == status
                        and (status != translations.MISSING or not scope or p.part in scope)]
                if not rows:
                    continue
                print(f"\n  {status} ({len(rows)}) :")
                for p in rows:
                    src = p.source.rel if p.source else "—"
                    dst = p.translation.rel if p.translation else "—"
                    print(f"    {src}  →  {dst}")
        pending = sum(counts[s] for s in listed if s not in (translations.MISSING, translations.ORIGIN_MISSING))
        if args and args.strict and (pending or counts[translations.MISSING] or counts[translations.ORIGIN_MISSING]):
            ok = False
    return ok


def cmd_info(dictionary: Dictionary, args=None) -> bool:
    print(f"\n{dictionary.total_count} entrées")
    for part in dictionary.taxonomy.parts:
        print(f"  {part.title} : {len(dictionary.by_part(part.id))}")
    print(f"Versions courtes : {sum(1 for d in dictionary if d.short)}")
    engine, binary = find_tex_engine()
    print(f"Moteur LaTeX : {engine or 'aucun'} {binary or ''}")
    print(f"epubcheck : {' '.join(find_epubcheck() or ['introuvable'])}")
    return True


COMMANDS = {
    "check": (cmd_check, "Tout valider (métadonnées, versions courtes, markdown, spécifications, chronologie)"),
    "fix": (cmd_fix, "Corriger automatiquement le markdown et les renvois invalides"),
    "build": (cmd_build, "Générer les éditions (PDF à imprimer, EPUB)"),
    "index": (cmd_index, "Mettre à jour INDEX.md"),
    "stats": (cmd_stats, "Mettre à jour stats.md et le badge du README"),
    "sync": (cmd_sync, "État de la synchro entre le français et les traductions"),
    "info": (cmd_info, "Afficher les informations"),
}


def menu() -> None:
    names = list(COMMANDS)
    print("\n" + "=" * 60 + "\n  DICTIONNAIRE DE BITCOIN\n" + "=" * 60)
    for i, name in enumerate(names):
        print(f"  {i}. {COMMANDS[name][1]}")
    print(f"  {len(names)}. Quitter")
    try:
        choice = input("\n  Votre choix : ").strip()
    except (KeyboardInterrupt, EOFError):
        return
    if not choice.isdigit() or int(choice) >= len(names):
        return
    dictionary = Dictionary.load()
    COMMANDS[names[int(choice)]][0](dictionary, None)


def main() -> int:
    if len(sys.argv) == 1:
        menu()
        return 0
    parser = argparse.ArgumentParser(description="Dictionnaire de Bitcoin : validation et génération.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, (_, help_text) in COMMANDS.items():
        p = sub.add_parser(name, help=help_text)
        if name == "build":
            p.add_argument("--edition", default="all", help="éditions de templates/editions.yaml séparées par des virgules (complete, essentiel) ou all (défaut)")
            p.add_argument("--format", default="all", help="pdf, epub (séparés par des virgules) ou all")
            p.add_argument("--output-dir", help="dossier de sortie (défaut : build/)")
            p.add_argument("--force", action="store_true", help="générer même si la validation échoue")
        if name == "sync":
            p.add_argument("--lang", help="langue cible (défaut : toutes celles de templates/languages.yaml)")
            p.add_argument("--list", nargs="?", const="all", metavar="STATUT",
                           help="lister les entrées par statut (tous, ou un seul : « en retard », « à reporter »…)")
            p.add_argument("--mark", nargs="+", metavar="SLUG",
                           help="enregistrer que ces traductions sont à jour (slug FR, slug EN ou UUID)")
            p.add_argument("--mark-unmarked", action="store_true",
                           help="enregistrer toutes les traductions jamais marquées")
            p.add_argument("--new", metavar="SLUG_FR", help="créer le dossier de traduction d'une entrée")
            p.add_argument("--title", help="titre traduit, en MAJUSCULES (avec --new)")
            p.add_argument("--slug", help="slug traduit (avec --new ; défaut : tiré du titre)")
            p.add_argument("--diff", metavar="SLUG", help="changements de la source et de la traduction depuis la synchro")
            p.add_argument("--strict", action="store_true",
                           help="échouer s'il reste une traduction manquante, en retard ou à reporter dans le périmètre")
    args = parser.parse_args()
    dictionary = Dictionary.load()
    return 0 if COMMANDS[args.command][0](dictionary, args) else 1


if __name__ == "__main__":
    sys.exit(main())
