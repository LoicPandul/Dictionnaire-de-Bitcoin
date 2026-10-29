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
from scripts.core import translations, yaml_sync  # noqa: E402
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

    languages = translations.load_languages()
    lang_arg = args.lang if args and getattr(args, "lang", None) else languages["source"]
    langs = [languages["source"], *languages["translations"]] if lang_arg == "all" else lang_arg.split(",")
    for lang in langs:
        if lang != languages["source"] and lang not in languages["translations"]:
            print(f"[ERREUR] langue inconnue : {lang} (templates/languages.yaml)")
            return False

    engine, _ = find_tex_engine()
    print(f"\nMoteur LaTeX : {engine or 'aucun'}")
    ok = True
    produced = []
    for lang, edition_id in [(l, e) for l in langs for e in wanted_editions]:
        source = lang == languages["source"]
        book_dictionary = dictionary if source else Dictionary.load_translation(lang, dictionary)
        book = Book(edition_id, book_dictionary, editions, lang=lang)
        print(f"\n=== Édition « {edition_id} » ({lang}) : {book.entry_count()} entrées, "
              f"{len(book.edition.sections)} sections ===")
        for w in book_dictionary.warnings[:5] if not source else []:
            print(f"  [ATTENTION] {w}")
        for w in book.warnings:
            print(f"  [ATTENTION] {w}")
        out_root = Path(args.output_dir) if args and args.output_dir else BUILD_DIR
        out_dir = (out_root if source else out_root / lang) / edition_id
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
        conf = languages["translations"][lang]
        scope = set(conf.get("parts") or [])
        all_pairs = translations.pairs(languages["source"], lang, part_of, **translation_checker.filters(conf))
        items = yaml_sync.all_items(languages["source"], lang)

        if args and (args.mark or args.mark_unmarked):
            refs = list(args.mark or [])
            if args.mark_unmarked:
                refs += [p.uuid for p in all_pairs if p.status == translations.UNMARKED]
                refs += [it.label for it in items if it.status == translations.UNMARKED]
            chosen = []
            for ref in refs:
                found = [it for it in items if ref in (it.key, it.label) and it.translation is not None]
                if found:
                    chosen += found
                    continue
                p = _find_pair(all_pairs, ref)
                if not p or not (p.source and p.translation):
                    print(f"[ERREUR] {ref} : pas de paire source/traduction à marquer")
                    ok = False
                    continue
                values = translations.mark(p.source, p.translation)
                p.status = translations.UP_TO_DATE
                print(f"  [{p.translation.lang}/{p.translation.slug}] synchro enregistrée "
                      f"({p.source.lang} {values['source_hash']} @ {values['source_commit'] or '?'})")
            if chosen:
                n = yaml_sync.mark(chosen, lang)
                print(f"  {n} élément(s) de la chronologie ou des résumés marqués à jour")
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
        for part, status in [(p.part or "?", p.status) for p in all_pairs] + [(it.kind, it.status) for it in items]:
            by_part.setdefault(part, Counter())[status] += 1
        name = languages["translations"][lang].get("name", lang)
        print(f"\n{languages['source'].upper()} → {lang.upper()} ({name}), périmètre : {', '.join(sorted(scope)) or 'tout'}")
        print(f"  {'partie':<24}{'traduites':>10}{'manquantes':>12}{'à jour':>8}{'en retard':>11}"
              f"{'à reporter':>12}{'conflits':>10}{'à marquer':>11}")
        for part, c in sorted(by_part.items(), key=lambda kv: -sum(kv[1].values())):
            missing = c[translations.MISSING] + c[translations.ORIGIN_MISSING]
            done = (sum(c.values()) - missing - c[translations.ORPHAN] - c[translations.EXCLUDED]
                    - c[translations.PENDING])
            flag = "" if (not scope or part in scope) else "  (hors périmètre)"
            if c[translations.PENDING]:
                flag += f"  ({c[translations.PENDING]} en attente)"
            if c[translations.ORPHAN]:
                flag += f"  ({c[translations.ORPHAN]} orphelines)"
            print(f"  {part:<24}{done:>10}{missing:>12}{c[translations.UP_TO_DATE]:>8}"
                  f"{c[translations.TRANSLATION_BEHIND]:>11}{c[translations.SOURCE_BEHIND]:>12}"
                  f"{c[translations.CONFLICT]:>10}{c[translations.UNMARKED]:>11}{flag}")
        counts, _ = translation_checker.summary(dictionary)[lang]
        print(f"  Dans le périmètre : {translation_checker.describe(lang, counts)}")

        listed = [s for s in translations.STATUSES if s not in (translations.UP_TO_DATE, translations.EXCLUDED)]
        if args and args.list == translations.PENDING:
            listed = [translations.PENDING]
        if args and args.list:
            # Les entrées manquantes se comptent par centaines : on les liste seulement sur demande.
            listed = [s for s in listed if s == args.list or (args.list == "all" and s != translations.MISSING)]
            for status in listed:
                rows = [p for p in all_pairs if p.status == status
                        and (status != translations.MISSING or not scope or p.part in scope)]
                lines = [f"{p.source.rel if p.source else '—'}  →  {p.translation.rel if p.translation else '—'}"
                         for p in rows]
                lines += [f"{yaml_sync.rel(it.kind, languages['source'], it.file)} {it.key}  →  "
                          f"{yaml_sync.rel(it.kind, lang, it.file)}" for it in items if it.status == status
                          and (status != translations.MISSING or not scope or it.kind in scope)]
                if not lines:
                    continue
                print(f"\n  {status} ({len(lines)}) :")
                for line in lines:
                    print(f"    {line}")
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
            p.add_argument("--lang", default="fr",
                           help="langue du livre : fr (défaut), en, ou all ; une traduction sort dans build/<langue>/")
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
