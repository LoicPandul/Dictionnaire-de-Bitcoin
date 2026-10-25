#!/usr/bin/env python3
"""
Génération de INDEX.md : toutes les entrées, partie par partie puis lettre par lettre.
"""

from pathlib import Path

from ..config import OUTPUT_INDEX
from ..core.dictionary import Dictionary, group_by_letter


def generate(dictionary: Dictionary, output_path: Path = None) -> bool:
    output_path = output_path or OUTPUT_INDEX
    taxonomy = dictionary.taxonomy
    lines = [
        "# Index du Dictionnaire de Bitcoin",
        "",
        f"Ce fichier liste les {dictionary.total_count} entrées du dictionnaire, partie par partie.",
        "Chaque entrée a une version développée (`definition.md`) et une version courte (`courte.md`).",
        "",
    ]
    parts = [p for p in taxonomy.parts if dictionary.by_part(p.id)]
    lines.append(" | ".join(f"[{p.title}](#{_anchor(p.title)})" for p in parts))
    lines += ["", "---", ""]

    for p in parts:
        defs = dictionary.by_part(p.id)
        lines += [f"## {p.title}", "", f"{len(defs)} entrées.", ""]
        for letter, group in group_by_letter(defs).items():
            lines += [f"### {p.title} : {letter}", "", "| Terme | Catégorie | UUID |", "|-------|-----------|------|"]
            for d in group:
                rel = d.path.resolve().relative_to(output_path.resolve().parent).as_posix()
                lines.append(f"| [{d.title}]({rel}/definition.md) | {d.category} | `{d.uuid}` |")
            lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Index : {output_path} ({dictionary.total_count} entrées)")
    return True


def _anchor(title: str) -> str:
    """Ancre GitHub d'un titre markdown."""
    import re
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
