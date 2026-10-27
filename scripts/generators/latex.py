#!/usr/bin/env python3
"""
Conversion du markdown des définitions en LaTeX (XeLaTeX, polyglossia).

Le markdown du dictionnaire est volontairement restreint (docs/charte-editoriale.md) : paragraphes,
italique, gras dans les textes liminaires seulement, code inline et blocs de code,
formules `$…$` et `$$…$$`, listes, citations, tableaux, images `![alt](./assets/x.png)`
et liens. Chaque construction est protégée par un marqueur avant l'échappement des
caractères spéciaux, puis restaurée.
"""

import re
from pathlib import Path
from typing import Optional

from . import images

URL_TRAILING = ".,;:!?"


def escape(text: str) -> str:
    """Échappe les caractères spéciaux LaTeX d'un texte brut."""
    replacements = [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
    ]
    out = []
    for ch in text:
        for old, new in replacements:
            if ch == old:
                out.append(new)
                break
        else:
            out.append(ch)
    return "".join(out)


def escape_url(url: str) -> str:
    """Prépare une URL pour \\url dans un argument de commande."""
    return url.replace("\\", "/").replace("%", r"\%").replace("#", r"\#").replace("{", "").replace("}", "")


def clean_content(content: str) -> str:
    """Normalise les espaces : polyglossia gère seul les espaces de la ponctuation française."""
    content = content.replace("&nbsp;", " ")
    content = content.replace("\u200b", "")  # espace sans chasse, absente d'Archivo
    content = content.replace("\u00A0", " ").replace("\u202F", " ")
    content = re.sub(r"(https?)[\s]*:[\s]*//", r"\1://", content)
    content = re.sub(r"[ \t]+", " ", content)
    return content


def fix_math(content: str) -> str:
    """Remplace les commandes mathématiques que la police ou les paquets ne gèrent pas."""
    content = re.sub(r"\\text\{([^}]+)\}", r"\\mathrm{\1}", content)
    content = re.sub(r"\\mod\b", r"\\bmod", content)
    return content


def format_code_block(code: str, max_chars: int) -> str:
    """Bloc de code : sauts de ligne d'origine conservés, lignes longues coupées, échappement."""
    def esc(text: str) -> str:
        text = text.replace("\\", r"\textbackslash{}")
        for old, new in [("{", r"\{"), ("}", r"\}"), ("$", r"\$"), ("%", r"\%"), ("#", r"\#"),
                         ("&", r"\&"), ("_", r"\_"), ("^", r"\textasciicircum{}"),
                         ("~", r"\textasciitilde{}")]:
            text = text.replace(old, new)
        # Les espaces multiples comptent dans du code.
        return re.sub(r" {2,}", lambda m: r"\ " * len(m.group(0)), text)

    lines = []
    for line in code.split("\n"):
        while len(line) > max_chars:
            lines.append(esc(line[:max_chars]))
            line = line[max_chars:]
        lines.append(esc(line) if line else r"\mbox{}")
    return r"\noindent " + ("\\\\\n").join(lines)


def _convert_table(table_text: str) -> Optional[str]:
    lines = table_text.strip().split("\n")
    if len(lines) < 3 or not re.match(r"^\|[\s\-:|]+\|$", lines[1].strip()):
        return None
    header = [c.strip() for c in lines[0].strip().strip("|").split("|")]
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines[2:]]
    n = len(header)
    col_spec = "@{}" + " ".join([">{\\raggedright\\arraybackslash}X"] * n) + "@{}"
    out = [
        r"\par\vspace{0.25em}",
        r"{\tablesize\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.3}\setlength{\arrayrulewidth}{0.3pt}",
        r"\noindent\begin{xltabular}{\linewidth}{" + col_spec + "}",
        # Filets de 0,3 pt : ceux de l'en-tête en Figue, ceux des lignes en noir
        r"\arrayrulecolor{figue}\hline",
        " & ".join(rf"\textbf{{{_cell(h)}}}" for h in header) + r" \\ \hline\arrayrulecolor{black}",
    ]
    for row in rows:
        cells = [_cell(c) for c in row[:n]] + [""] * max(0, n - len(row))
        out.append(" & ".join(cells) + r" \\ \hline")
    out += [r"\end{xltabular}", r"}", r"\vspace{0.15em}"]
    return "\n".join(out)


def _emphasis(content: str) -> str:
    content = re.sub(r"\*\*([^*\n]+)\*\*", r"\\textbf{\1}", content)
    # « * » suivi d'une espace est une puce de liste, jamais une ouverture d'italique.
    content = re.sub(r"(?<![\\*\w])\*(?=\S)([^*\n]+?)(?<=\S)\*(?!\w)", r"\\textit{\1}", content)
    content = re.sub(r"(?<![\\\w])\\_([^_\n]+?)\\_(?!\w)", r"\\textit{\1}", content)
    return content


def _cell(text: str) -> str:
    """Cellule de tableau : les marqueurs du texte englobant restent pour la restauration finale."""
    return _emphasis(escape(text))


def inline(text: str) -> str:
    """Convertit un fragment sur une ligne (cellule de tableau, titre court)."""
    return markdown_to_latex(text, inline_only=True)


def markdown_to_latex(content: str, assets_dir: Optional[Path] = None, code_max_chars: int = 64,
                      use_cartouche_h1: bool = False, inline_only: bool = False,
                      color: bool = True, credits: Optional[dict] = None) -> str:
    """Convertit du markdown du dictionnaire en LaTeX.

    `color` : livre imprimé en couleur (schémas en couleur) ou en noir et blanc (versions « -nb »).
    `credits` : crédit des images de tiers, par nom de fichier, imprimé sous l'image.
    """
    store = []

    def keep(latex: str) -> str:
        store.append(latex)
        return f"\x00{len(store) - 1}\x00"

    # 1. Blocs de code
    if not inline_only:
        def code_block(m):
            code = m.group(2).rstrip("\n")
            return keep("\\begin{codeblock}\n" + format_code_block(code, code_max_chars) + "\n\\end{codeblock}")
        content = re.sub(r"```([\w+-]*)[ \t]*\n(.*?)```", code_block, content, flags=re.DOTALL)

    # 2. Code inline
    def inline_code(m):
        code = m.group(1)
        code = escape(code).replace("‖", r"{\rmfamily ‖}")  # absent d'Atkinson Hyperlegible Mono
        return keep(rf"\inlinecodelong{{{code}}}")
    content = re.sub(r"`([^`\n]+)`", inline_code, content)

    # 3. Formules (bloc puis inline)
    content = re.sub(r"\$\$(.+?)\$\$", lambda m: keep("$$" + fix_math(m.group(1)) + "$$"), content, flags=re.DOTALL)
    content = re.sub(r"(?<!\\)\$([^$\n]+?)\$", lambda m: keep("$" + fix_math(m.group(1)) + "$"), content)

    # 4. Images (avec ou sans texte alternatif)
    def image(m):
        if assets_dir is None:
            return ""
        # Version couleur ou noir et blanc du schéma, vectorielle si possible (images.py).
        path = images.for_print(assets_dir / m.group(2), color).as_posix()
        caption = ""
        credit = (credits or {}).get(m.group(2))
        if credit:
            # Crédit d'une image de tiers : petit, en Écorce, sous l'image et avant la légende
            caption += r"\par\vspace{1pt}{\creditsize\color{ecorce}" + _emphasis(escape(credit)) + r"\par}"
        if m.group(1).strip():
            # Légende : texte secondaire, en Écorce (charte, section 2)
            caption += (r"\par\vspace{2pt}{\footnotesize\itshape\color{ecorce} " + _emphasis(escape(m.group(1).strip()))
                       + r"\par}")
        return keep(rf"{{\centering\includegraphics[width=0.8\linewidth,keepaspectratio,height=\imagemaxheight]{{{path}}}{caption}\par}}")
    content = re.sub(r"!\[([^\]]*)\]\(\./assets/([^)\s]+)\)", image, content)

    # 5. Liens markdown : le texte seul
    content = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r"\1", content)

    # 6. URL brutes
    def url(m):
        raw = m.group(0)
        trail = ""
        while raw and raw[-1] in URL_TRAILING:
            trail = raw[-1] + trail
            raw = raw[:-1]
        return keep(rf"\cleanurl{{{escape_url(raw)}}}") + trail
    content = re.sub(r"https?://[^\s<>()\[\]{}\\\"«»*\x00]+", url, content)

    # 7. Tableaux
    if not inline_only:
        def table(m):
            latex = _convert_table(m.group(0))
            return keep(latex) + "\n" if latex else m.group(0)
        content = re.sub(r"(?:^\|.+\|[ \t]*\n?)+", table, content, flags=re.MULTILINE)

    # 8. Titres de niveau 1 (textes liminaires)
    if not inline_only:
        if use_cartouche_h1:
            content = re.sub(r"^# (.+)$", lambda m: keep(r"\par\vspace{0.4em}\noindent\vedette{" + escape(m.group(1)) + r"}\par\nopagebreak"), content, flags=re.MULTILINE)
        content = re.sub(r"^### (.+)$", lambda m: keep(r"\subsubsection*{" + escape(m.group(1)) + "}"), content, flags=re.MULTILINE)
        content = re.sub(r"^## (.+)$", lambda m: keep(r"\subsection*{" + escape(m.group(1)) + "}"), content, flags=re.MULTILINE)
        content = re.sub(r"^# (.+)$", lambda m: keep(r"\section*{" + escape(m.group(1)) + "}"), content, flags=re.MULTILINE)

    # 9. Échappement du texte restant (marqueurs \x00n\x00 intacts)
    content = escape(content)

    # 10. Emphase
    content = _emphasis(content)

    if not inline_only:
        # 11. Citations
        content = re.sub(r"^> ?(.*)$", lambda m: r"\begin{quote}" + m.group(1) + r"\end{quote}", content, flags=re.MULTILINE)
        # 12. Listes
        content = _lists(content)

    # 13. Restauration (en boucle : un marqueur peut en contenir un autre)
    for _ in range(4):
        content = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], content)
    return content


def _lists(content: str) -> str:
    out, kind = [], None
    for line in content.split("\n"):
        s = line.strip()
        bullet = re.match(r"^[*\-] (.*)$", s)
        number = re.match(r"^\d+[.)] (.*)$", s)
        item_kind = "itemize" if bullet else "enumerate" if number else None
        if item_kind:
            if kind and kind != item_kind:
                out.append(rf"\end{{{kind}}}")
                kind = None
            if not kind:
                if out and out[-1].strip():
                    out.append("")
                out.append(rf"\begin{{{item_kind}}}")
                kind = item_kind
            out.append(r"  \item " + (bullet or number).group(1))
        else:
            if kind and s:
                out.append(rf"\end{{{kind}}}")
                kind = None
            out.append(line)
    if kind:
        out.append(rf"\end{{{kind}}}")
    return "\n".join(out)
