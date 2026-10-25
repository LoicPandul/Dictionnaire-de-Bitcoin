#!/usr/bin/env python3
"""
Génération du PDF d'une édition via XeLaTeX (ou Tectonic, son équivalent autonome).

Deux formats Amazon KDP, même mise en page à l'échelle près :
  - broché 5,5 × 8,5 po (13,97 × 21,59 cm) ;
  - relié 7 × 10 po (17,78 × 25,4 cm).
"""

import shutil
import subprocess
import unicodedata
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import yaml

from ..config import BASE_DIR, BUILD_DIR, FONTS_DIR, PICTOGRAMS_DIR, TEMPLATES_DIR, find_tex_engine
from ..core.book import Book, Section
from ..core.chronology import MOIS_FR
from .latex import clean_content, escape, inline, markdown_to_latex


@dataclass(frozen=True)
class PdfFormat:
    id: str
    suffix: str
    geometry: str
    code_max_chars: int
    isbn_key: str
    header_letter: str      # taille de la lettre courante en en-tête
    header_word: str        # taille du mot guide en en-tête
    page_number: str
    toc_text: str
    toc_letterbox: str      # \fontsize de la cartouche de lettre de la TDM
    letter_page: str        # \fontsize de la grande lettre des pages de lettre


FORMATS = {
    "broche": PdfFormat(
        id="broche", suffix="", isbn_key="isbn_paperback", code_max_chars=64,
        geometry="paperwidth=13.97cm, paperheight=21.59cm, top=8mm, bottom=8mm, outer=10.5mm, "
                 "inner=20mm, headheight=12pt, headsep=5mm, footskip=8mm",
        header_letter=r"\small", header_word=r"\scriptsize", page_number=r"\small",
        toc_text=r"\scriptsize", toc_letterbox=r"\fontsize{11}{13}", letter_page=r"\fontsize{120}{144}",
    ),
    "relie": PdfFormat(
        id="relie", suffix="-relie", isbn_key="isbn_hardcover", code_max_chars=81,
        geometry="paperwidth=17.78cm, paperheight=25.4cm, top=9.5mm, bottom=9.5mm, outer=13.5mm, "
                 "inner=25.5mm, headheight=14pt, headsep=6mm, footskip=9.5mm",
        header_letter=r"\fontsize{9}{11}\selectfont", header_word=r"\fontsize{8}{10}\selectfont",
        page_number=r"\fontsize{9}{11}\selectfont", toc_text=r"\fontsize{8}{10}\selectfont",
        toc_letterbox=r"\fontsize{14}{17}", letter_page=r"\fontsize{153}{183}",
    ),
}

STATUS_FR = {
    # BIP (BIP-0003 et anciens statuts de BIP-0002)
    "draft": "Brouillon", "complete": "Complet", "deployed": "Déployé", "closed": "Clos",
    "final": "Final", "active": "Actif", "proposed": "Proposé", "withdrawn": "Retiré",
    "replaced": "Remplacé", "rejected": "Rejeté", "obsolete": "Obsolète", "deferred": "Reporté",
    # NIP
    "optional": "optionnel", "mandatory": "obligatoire", "unrecommended": "déconseillé",
    "deprecated": "déprécié",
}


def _main_font() -> str:
    """Arial si la machine l'a, sinon Liberation Sans (mêmes métriques)."""
    fc = shutil.which("fc-list")
    if fc:
        out = subprocess.run([fc, ":", "family"], capture_output=True, text=True).stdout
        families = {f.strip() for line in out.splitlines() for f in line.split(",")}
        if "Arial" in families:
            return "Arial"
        if "Liberation Sans" in families:
            return "Liberation Sans"
    return "Arial"


def load_legal() -> dict:
    with open(TEMPLATES_DIR / "legal.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# --------------------------------------------------------------------------
# Préambule
# --------------------------------------------------------------------------

def _preamble(fmt: PdfFormat, legal: dict, book: Book) -> str:
    fonts = FONTS_DIR.as_posix() + "/"
    pictos = PICTOGRAMS_DIR.as_posix() + "/"
    main_font = _main_font()
    title = book.edition.title
    subtitle = book.edition.subtitle
    isbn = legal.get(fmt.isbn_key, "")
    keywords = f"Bitcoin, {legal.get('license', '')}" + (f", ISBN {isbn}" if isbn else "")
    return rf"""% {title} - édition {book.edition.id}, format {fmt.id}
\documentclass[9pt,twoside,openright]{{extbook}}

\usepackage{{fontspec}}
\usepackage{{polyglossia}}
\setdefaultlanguage{{french}}
\setotherlanguage{{english}}

\usepackage[{fmt.geometry}, includehead, includefoot]{{geometry}}

\setmainfont{{{main_font}}}
\setsansfont{{{main_font}}}
\setmonofont{{Fira Code}}[Path={fonts}, Extension=.ttf, UprightFont=FiraCode-Regular, BoldFont=FiraCode-Bold, Scale=0.85]
\newfontfamily\cmufont{{cmunrm}}[Path={fonts}, Extension=.ttf, AutoFakeBold=1.5]

\usepackage{{microtype}}
\usepackage{{setspace}}
\setstretch{{1.0}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.35em}}
\usepackage{{ragged2e}}
\justifying
\tolerance=1000
\emergencystretch=3em
\hyphenpenalty=50
\exhyphenpenalty=50
\widowpenalty=150
\clubpenalty=150
\raggedbottom

\usepackage{{xcolor}}
\definecolor{{inlinecodebg}}{{RGB}}{{239, 241, 243}}
\definecolor{{inlinecodeborder}}{{RGB}}{{208, 215, 222}}
\definecolor{{linkcolor}}{{RGB}}{{0, 0, 0}}

\usepackage[colorlinks=true, linkcolor=linkcolor, urlcolor=linkcolor, pdfborder={{0 0 0}},
  pdftitle={{{title}}}, pdfauthor={{{legal.get('author', '')}}},
  pdfsubject={{{title} : {subtitle}}}, pdfkeywords={{{keywords}}}]{{hyperref}}
\urlstyle{{same}}

\usepackage{{graphicx}}
\graphicspath{{{{{pictos}}}}}
\usepackage{{float}}

\usepackage{{array}}
\usepackage{{colortbl}}
\usepackage{{xltabular}}
\usepackage{{multicol}}
\arrayrulecolor{{white}}
\setlength{{\multicolsep}}{{0pt}}
\setlength{{\columnsep}}{{0.5em}}

\usepackage{{enumitem}}
\setlist[itemize]{{topsep=0.2em, itemsep=0.05em, parsep=0pt, leftmargin=1.2em, before=\vspace{{-\parskip}}}}
\setlist[enumerate]{{topsep=0.2em, itemsep=0.05em, parsep=0pt, leftmargin=1.5em, before=\vspace{{-\parskip}}}}

\usepackage{{tcolorbox}}
\tcbuselibrary{{breakable,skins}}
\newtcolorbox{{codeblock}}{{colback=inlinecodebg, colframe=inlinecodeborder, boxrule=0.3pt, arc=0pt,
  boxsep=0pt, left=6pt, right=6pt, top=4pt, bottom=4pt, breakable,
  fontupper=\ttfamily\fontsize{{9}}{{10}}\selectfont\raggedright}}

\usepackage{{soul}}
\DeclareRobustCommand{{\inlinecodelong}}[1]{{\begingroup\sethlcolor{{inlinecodebg}}\ttfamily\fontsize{{9}}{{10}}\selectfont\hl{{\,#1\,}}\endgroup}}

\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{amsfonts}}
\usepackage{{csquotes}}
\usepackage{{needspace}}

\usepackage{{fancyhdr}}
\newcommand{{\currentletter}}{{}}
\fancypagestyle{{dictionary}}{{
  \fancyhf{{}}
  \fancyhead[CE,CO]{{{fmt.header_letter}\textit{{\currentletter}}}}
  \fancyhead[LE]{{{fmt.header_word}\textit{{\rightmark}}}}
  \fancyhead[RO]{{{fmt.header_word}\textit{{\leftmark}}}}
  \fancyfoot[C]{{{fmt.page_number}\thepage}}
  \renewcommand{{\headrulewidth}}{{0pt}}
  \renewcommand{{\footrulewidth}}{{0pt}}
}}
\fancypagestyle{{frontmatter}}{{
  \fancyhf{{}}
  \fancyfoot[C]{{{fmt.page_number}\thepage}}
  \renewcommand{{\headrulewidth}}{{0pt}}
  \renewcommand{{\footrulewidth}}{{0pt}}
}}
\fancypagestyle{{letterpage}}{{\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}\renewcommand{{\footrulewidth}}{{0pt}}}}

% Pages blanches insérées par \cleardoublepage : sans en-tête
\makeatletter
\renewcommand{{\cleardoublepage}}{{\clearpage\if@twoside\ifodd\c@page\else\hbox{{}}\thispagestyle{{empty}}\newpage\fi\fi}}
\makeatother

\newcommand{{\cleanurl}}[1]{{\textenglish{{\url{{#1}}}}}}

% Vedette : cartouche noire ajustée au titre
\newcommand{{\vedettefit}}[1]{{\fcolorbox{{black}}{{black}}{{\hspace{{0.3em}}{{\color{{white}}\fontsize{{8}}{{11}}\selectfont\bfseries\addfontfeature{{LetterSpace=3.0}}#1}}\hspace{{0.3em}}}}}}
% Cartouche de lettre (TDM, intertitres de lettre, années)
\newcommand{{\tocletterbox}}[1]{{\fcolorbox{{black}}{{black}}{{\hspace{{0.2em}}{{\color{{white}}{fmt.toc_letterbox}\selectfont\cmufont\bfseries #1}}\hspace{{0.2em}}}}}}
"""


# --------------------------------------------------------------------------
# Pages liminaires et finales
# --------------------------------------------------------------------------

def _date_fr(now: datetime) -> str:
    return f"{now.day:02d} {MOIS_FR[now.month]} {now.year}"


def _half_title(book: Book) -> str:
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}{{\fontsize{{18}}{{22}}\selectfont\cmufont\bfseries {escape(book.edition.title)}}}\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _title_page(book: Book, legal: dict) -> str:
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{3cm}}
\begin{{center}}
{{\fontsize{{22}}{{26}}\selectfont\cmufont\bfseries {escape(book.edition.title)}}}\\[0.6cm]
{{\fontsize{{11}}{{14}}\selectfont\cmufont {escape(book.edition.subtitle.upper())}}}
\end{{center}}
\vfill
\begin{{center}}{{\fontsize{{12}}{{16}}\selectfont\cmufont\itshape {escape(legal.get('author', ''))}}}\end{{center}}
\vspace*{{2cm}}
\clearpage"""


def _legal_lines(book: Book, legal: dict, fmt: PdfFormat) -> List[str]:
    now = datetime.now()
    isbn = legal.get(fmt.isbn_key, "")
    lines = [
        rf"\textbf{{© {now.year} {escape(legal.get('author', ''))}}}",
        rf"\textbf{{\textit{{{escape(book.edition.title)} : {escape(book.edition.subtitle)}}}}}",
        rf"Version du {_date_fr(now)}",
        rf"\cleanurl{{{legal.get('github_url', '')}}}",
        rf"Cet ouvrage est sous licence {escape(legal.get('license', ''))}",
        rf"\cleanurl{{{legal.get('license_url', '')}}}",
        rf"Lightning : {escape(legal.get('lightning_address', ''))}",
        rf"Email : {escape(legal.get('email', ''))}",
        rf"Site web : \cleanurl{{{legal.get('website', '')}}}",
        rf"GitHub : \cleanurl{{{legal.get('github_profile', '')}}}",
    ]
    if isbn and book.edition.id == "complete":
        lines.append(rf"ISBN : {isbn}")
    return lines


def _copyright_page(book: Book, legal: dict, fmt: PdfFormat) -> str:
    body = "\\\\[0.4em]\n".join(r"\noindent " + l for l in _legal_lines(book, legal, fmt))
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{\fill}}
\small\setstretch{{1.0}}
{body}
\normalsize
\clearpage"""


def _final_page(book: Book, legal: dict, fmt: PdfFormat) -> str:
    body = "\\\\[0.4em]\n".join(_legal_lines(book, legal, fmt))
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}\small\setstretch{{1.0}}
{body}
\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _front_text(title: str, template: str, cartouche_h1: bool = False) -> str:
    path = TEMPLATES_DIR / template
    content = path.read_text(encoding="utf-8") if path.exists() else ""
    latex = markdown_to_latex(clean_content(content), use_cartouche_h1=cartouche_h1)
    latex = latex.replace(r"\subsection*{", r"\subsection*{\cmufont ")
    return rf"""
\clearpage\thispagestyle{{frontmatter}}
\begin{{center}}{{\fontsize{{14}}{{18}}\selectfont\cmufont\bfseries {title}}}\end{{center}}
\vspace{{-0.2em}}
\small
{latex}
\normalsize
\clearpage"""


# --------------------------------------------------------------------------
# Table des matières
# --------------------------------------------------------------------------

def _toc(book: Book, fmt: PdfFormat) -> str:
    out = [r"""
\clearpage\thispagestyle{frontmatter}
\begin{center}{\fontsize{14}{18}\selectfont\cmufont\bfseries TABLE DES MATIÈRES}\end{center}
\vspace{0.3cm}"""]
    # Les parties, avec leur page
    out.append(r"{\small")
    for i, s in enumerate(book.edition.sections):
        out.append(rf"\noindent\hyperlink{{part-{s.id}}}{{\textbf{{{escape(s.title)}}}}}\dotfill\pageref*{{part:{s.id}}}\par")
    out.append(r"}\vspace{1.2em}")

    # Le détail des entrées de chaque partie du dictionnaire
    for s in book.edition.sections:
        if s.kind != "dictionary":
            continue
        out.append(rf"\needspace{{6\baselineskip}}\noindent{{\cmufont\bfseries {escape(s.title.upper())}}}\par\vspace{{0.4em}}")
        first = True
        for letter, defs in s.letters.items():
            if not first:
                out.append(r"\vspace{1.6em}")
            first = False
            if len(defs) <= 10:
                out.append(rf"\needspace{{{4 + (len(defs) + 1) // 2}\baselineskip}}\begin{{minipage}}{{\linewidth}}")
            else:
                out.append(r"\needspace{8\baselineskip}")
            out.append(rf"\noindent\tocletterbox{{{letter}}}\vspace{{0.45em}}")
            out.append(r"\begin{multicols}{2}")
            out.append(rf"{fmt.toc_text}\raggedright\setlength{{\parskip}}{{0.18em}}")
            for d in defs:
                out.append(rf"\noindent\hyperlink{{{d.slug}}}{{{escape(d.title)}}}\dotfill\pageref*{{def:{d.slug}}}\par")
            out.append(r"\end{multicols}")
            if len(defs) <= 10:
                out.append(r"\end{minipage}")
        out.append(r"\vspace{2em}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Parties
# --------------------------------------------------------------------------

def _part_opener(section: Section) -> str:
    intro = ""
    if section.intro:
        intro = (r"\vspace{1.5cm}\begin{minipage}{0.8\linewidth}\small\justifying "
                 + markdown_to_latex(clean_content(section.intro), inline_only=True) + r"\end{minipage}")
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{}}
\phantomsection\hypertarget{{part-{section.id}}}{{}}\label{{part:{section.id}}}
\vspace*{{\fill}}
\begin{{center}}
{{\fontsize{{26}}{{32}}\selectfont\cmufont\bfseries {escape(section.title)}}}\\[0.4cm]
{intro}
\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _letter_page(letter: str, fmt: PdfFormat) -> str:
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{{letter}}}
\vspace*{{\fill}}
\begin{{center}}{{{fmt.letter_page}\selectfont\cmufont\bfseries {letter}}}\end{{center}}
\vspace*{{\fill}}
\clearpage
\pagestyle{{dictionary}}"""


def _letter_heading(letter: str) -> str:
    return rf"""
\renewcommand{{\currentletter}}{{{letter}}}
\par\needspace{{6\baselineskip}}\vspace{{0.8em}}
\begin{{center}}\tocletterbox{{{letter}}}\end{{center}}
\vspace{{0.2em}}"""


def _meta_table(cells: List[str]) -> str:
    if not cells:
        return ""
    spec = "|" + "|".join(["c"] * len(cells)) + "|"
    return (r"\noindent{\fontsize{6}{7}\selectfont\setlength{\tabcolsep}{4.5pt}\arrayrulecolor{black}"
            r"\setlength{\arrayrulewidth}{0.3pt}"
            rf"\begin{{tabular}}{{{spec}}}\hline\rule[-2.5pt]{{0pt}}{{9pt}}{' & '.join(cells)} \\ \hline\end{{tabular}}}}\nopagebreak")


def _category_cell(book: Book, category: str) -> str:
    picto = book.taxonomy.pictogram(category) if book.taxonomy else None
    if picto and (PICTOGRAMS_DIR / f"{picto}.pdf").exists():
        return rf"\raisebox{{-0.5pt}}{{\includegraphics[height=5.5pt]{{{picto}.pdf}}}}\hspace{{0.3em}}{escape(category)}"
    return escape(category)


def _xref_boxes(targets, label_one: str, label_many: str) -> str:
    if not targets:
        return ""
    boxes = (r"\hspace{2pt}" + "\n").join(
        rf"\fbox{{\rule[-2.5pt]{{0pt}}{{9pt}}\hspace{{4.5pt}}\textbf{{\hyperlink{{{t.slug}}}{{{escape(t.title)}}}}}\hspace{{4.5pt}}}}"
        for t in targets)
    label = label_one if len(targets) == 1 else label_many
    return "\n".join([
        r"\par\nopagebreak",
        r"{\raggedleft\fontsize{6}{7}\selectfont\setlength{\fboxrule}{0.3pt}\setlength{\fboxsep}{0pt}%",
        rf"{label}\,:\hspace{{3pt}}%",
        boxes,
        r"\par}",
    ])


def _entry(book: Book, section: Section, d, fmt: PdfFormat) -> str:
    title = escape(d.title)
    parts = [
        r"\needspace{3\baselineskip}",
        rf"\label{{def:{d.slug}}}\markboth{{{title}}}{{{title}}}\hypertarget{{{d.slug}}}{{}}",
        rf"\noindent\vedettefit{{{title}}}\par\nopagebreak\nointerlineskip\vspace{{-\parskip}}",
    ]
    cells = [_category_cell(book, d.category)] if d.category else []
    if d.english_term:
        cells.append(rf"EN\,: {escape(d.english_term)}")
    elif d.french_term:
        cells.append(rf"FR\,: {escape(d.french_term)}")
    parts += [_meta_table(cells), r"\vspace{0.025em}\nopagebreak", ""]

    body = markdown_to_latex(clean_content(book.body(d, section)), assets_dir=d.path / "assets",
                             code_max_chars=fmt.code_max_chars)
    xrefs = book.cross_references(d) if section.version == "developpee" else []
    if xrefs:
        parts.append(body.rstrip() + "%")
        parts.append(_xref_boxes(xrefs, r"Terme associ\'{e}", r"Termes associ\'{e}s"))
    else:
        parts.append(body)
    parts.append(r"\vspace{0.4em}")
    return "\n".join(parts)


def _dictionary_section(book: Book, section: Section, fmt: PdfFormat) -> str:
    out = [_part_opener(section), r"\pagestyle{dictionary}"]
    for letter, defs in section.letters.items():
        out.append(_letter_page(letter, fmt) if section.letter_pages else _letter_heading(letter))
        for d in defs:
            out.append(_entry(book, section, d, fmt))
    return "\n".join(out)


def _chronology_section(book: Book, section: Section) -> str:
    out = [_part_opener(section), r"\pagestyle{dictionary}"]
    year = None
    for ev in section.events:
        if ev.year != year:
            year = ev.year
            out.append(_letter_heading(str(year)))
        related = book.related(ev.related)
        date = escape(ev.date_fr())
        out.append(r"\needspace{3\baselineskip}")
        out.append(rf"\markboth{{{year}}}{{{year}}}\noindent{{\bfseries {date}}}\enspace·\enspace\textit{{{inline(ev.title)}}}\par\nopagebreak")
        out.append(markdown_to_latex(clean_content(ev.text), inline_only=True) + "%")
        if related:
            out.append(_xref_boxes(related, "Voir", "Voir"))
        out.append(r"\par\vspace{0.5em}")
    return "\n".join(out)


def _status_label(doc) -> str:
    labels = []
    for s in doc.status:
        fr = STATUS_FR.get(s.lower())
        labels.append(fr if fr and fr.lower() == s.lower() else f"{fr} ({s})" if fr else s)
    return ", ".join(labels)


def _specs_section(book: Book, section: Section, fmt: PdfFormat) -> str:
    out = [_part_opener(section), r"\pagestyle{dictionary}"]
    for serie in section.series:
        if len(section.series) > 1:
            out.append(_letter_heading(serie.label))
        else:
            out.append(rf"\renewcommand{{\currentletter}}{{{serie.label}}}")
        for doc in serie.entries:
            ident = escape(doc.id)
            anchors = rf"\hypertarget{{{book.spec_anchor(doc)}}}{{}}"
            if doc.definition:
                anchors += rf"\hypertarget{{{doc.definition}}}{{}}\label{{def:{doc.definition}}}"
            out.append(r"\needspace{4\baselineskip}")
            out.append(rf"\markboth{{{ident}}}{{{ident}}}{anchors}")
            out.append(rf"\noindent\vedettefit{{{ident}}}\par\nopagebreak\nointerlineskip\vspace{{-\parskip}}")
            cells = []
            status = _status_label(doc)
            if status:
                cells.append(rf"Statut\,: {escape(status)}")
            if doc.type:
                cells.append(rf"Type\,: {escape(doc.type)}")
            if doc.created:
                cells.append(rf"Créé le\,: {escape(doc.created)}")
            out.append(_meta_table(cells))
            out.append(r"\vspace{0.025em}\nopagebreak")
            out.append("")
            if doc.title:
                out.append(rf"\noindent\textenglish{{\textit{{{inline(doc.title)}}}}}\par\nopagebreak")
            if doc.summary:
                out.append(markdown_to_latex(clean_content(doc.summary), inline_only=True) + r"\par")
            related = book.related(doc.related)
            if related:
                out.append(_xref_boxes(related, "Voir", "Voir"))
            linked = book.definition_for(doc)
            if section.detail and linked:
                out.append(r"\vspace{0.2em}")
                out.append(markdown_to_latex(clean_content(linked.content), assets_dir=linked.path / "assets",
                                             code_max_chars=fmt.code_max_chars))
            out.append(r"\vspace{0.6em}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Assemblage et compilation
# --------------------------------------------------------------------------

def build_latex(book: Book, fmt: PdfFormat, legal: Optional[dict] = None) -> str:
    legal = legal or load_legal()
    s = [_preamble(fmt, legal, book), r"\begin{document}", r"\frontmatter", r"\pagestyle{frontmatter}",
         _half_title(book), r"\cleardoublepage", _title_page(book, legal), _copyright_page(book, legal, fmt),
         r"\clearpage\thispagestyle{empty}\null",
         _front_text("CONTRIBUTEURS ET REMERCIEMENTS", "contributors.md"),
         _front_text("NOTE DE L'AUTEUR", "introduction.md", cartouche_h1=True),
         r"\cleardoublepage", _toc(book, fmt),
         r"\mainmatter", r"\pagestyle{dictionary}", r"\setcounter{page}{1}"]
    for section in book.edition.sections:
        if section.kind == "dictionary":
            s.append(_dictionary_section(book, section, fmt))
        elif section.kind == "chronology":
            s.append(_chronology_section(book, section))
        elif section.kind == "specs":
            s.append(_specs_section(book, section, fmt))
    s += [r"\backmatter", r"\pagestyle{empty}", r"\cleardoublepage", _final_page(book, legal, fmt),
          r"\clearpage\thispagestyle{empty}\null", r"\end{document}"]
    return "\n\n".join(s)


def _compile(tex_path: Path) -> subprocess.CompletedProcess:
    engine, binary = find_tex_engine()
    if engine is None:
        raise RuntimeError("Aucun moteur LaTeX : installez TeX Live (xelatex) ou Tectonic "
                           "(binaire dans .tools/bin/tectonic, voir scripts/README.md).")
    workdir = tex_path.parent
    if engine == "tectonic":
        cmd = [binary, "-X", "compile", "--keep-logs", "--outdir", str(workdir), str(tex_path)]
        return subprocess.run(cmd, capture_output=True, text=True, errors="replace", cwd=workdir)
    result = None
    for _ in range(2):  # deux passes : références de pages de la table des matières
        cmd = [binary, "-interaction=nonstopmode", "-halt-on-error", "-output-directory", str(workdir), str(tex_path)]
        result = subprocess.run(cmd, capture_output=True, text=True, errors="replace", cwd=workdir)
        if result.returncode != 0:
            break
    return result


def generate(book: Book, fmt_id: str = "broche", output_dir: Optional[Path] = None) -> Optional[Path]:
    """Génère le PDF d'une édition dans un format. Retourne le chemin, ou None en cas d'échec."""
    fmt = FORMATS[fmt_id]
    output_dir = output_dir or BUILD_DIR / book.edition.id
    workdir = output_dir / f"tex{fmt.suffix or '-broche'}"
    workdir.mkdir(parents=True, exist_ok=True)
    name = f"{book.edition.file}{fmt.suffix}"
    tex_path = workdir / f"{name}.tex"
    tex_path.write_text(build_latex(book, fmt), encoding="utf-8")

    print(f"  Compilation de {tex_path.relative_to(BASE_DIR) if tex_path.is_relative_to(BASE_DIR) else tex_path}…")
    result = _compile(tex_path)
    pdf = workdir / f"{name}.pdf"
    if result.returncode != 0 or not pdf.exists():
        log = workdir / f"{name}.log"
        tail = (result.stdout or "")[-1500:] + (result.stderr or "")[-1500:]
        print(f"[ERREUR] La compilation a échoué ({tex_path}).\n{tail}")
        if log.exists():
            errors = [l for l in log.read_text(errors="replace").splitlines() if l.startswith("!")]
            for line in errors[:10]:
                print(f"  {line}")
        return None
    final = output_dir / f"{name}.pdf"
    shutil.move(str(pdf), final)
    print(f"[OK] PDF : {final}")
    return final
