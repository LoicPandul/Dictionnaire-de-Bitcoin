#!/usr/bin/env python3
"""
Génération du PDF d'une édition via XeLaTeX (ou Tectonic, son équivalent autonome).

Mise en page de la charte graphique 2027 (design/charte-2027.md, sections 3 et 4, branche
feat/couverture-2027) : Archivo en instances statiques (fonts/static/), Atkinson Hyperlegible
Mono pour le code, Fira Math pour les formules. Deux formats Amazon KDP :
  - broché 5,5 × 8,5 po (13,97 × 21,59 cm) ;
  - relié 7 × 10 po (17,78 × 25,4 cm).
"""

import re
import shutil
import subprocess
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import yaml

from ..config import BASE_DIR, BUILD_DIR, FONTS_DIR, PICTOGRAMS_DIR, TEMPLATES_DIR, find_tex_engine
from ..core.book import Book, Section
from ..core.chronology import MOIS_FR
from .latex import clean_content, escape, inline, markdown_to_latex

# Au-delà de 700 pages, KDP exige 22,3 mm de marge intérieure pour le broché (charte, section 4).
KDP_THICK_BOOK_PAGES = 700


@dataclass(frozen=True)
class PdfFormat:
    id: str
    suffix: str
    isbn_key: str
    paper: str               # paperwidth, paperheight
    inner: str               # marge intérieure
    margins: str             # autres marges et en-têtes
    code_max_chars: int      # caractères par ligne d'un bloc de code
    body: tuple              # corps et interlignage du texte courant (pt)
    code_inline: float
    code_block: tuple
    vedette: float
    categorie: float
    renvois: float
    note: tuple
    table: tuple
    folio: float
    toc: tuple
    letter: float            # lettre de section, pleine page
    part: float              # ouverture de partie
    entry_gap: str           # blanc entre deux entrées
    image_gap: str
    image_height: str        # hauteur maximale d'une image
    picto: str               # hauteur du pictogramme de catégorie

    def geometry(self) -> str:
        return f"{self.paper}, inner={self.inner}, {self.margins}"


FORMATS = {
    "broche": PdfFormat(
        id="broche", suffix="", isbn_key="isbn_paperback",
        paper="paperwidth=13.97cm, paperheight=21.59cm", inner="20mm",
        margins="top=8mm, bottom=8mm, outer=10.5mm, headheight=12pt, headsep=5mm, footskip=8mm",
        code_max_chars=64, body=(9, 11.5), code_inline=8.5, code_block=(7.4, 10), vedette=10.5,
        categorie=8, renvois=7.5, note=(8, 10.5), table=(7.5, 9.5), folio=7.5, toc=(7, 8.5),
        letter=120, part=48, entry_gap="9pt", image_gap="6pt", image_height="85mm", picto="3mm",
    ),
    "relie": PdfFormat(
        id="relie", suffix="-relie", isbn_key="isbn_hardcover",
        paper="paperwidth=17.78cm, paperheight=25.4cm", inner="25.5mm",
        margins="top=9.5mm, bottom=9.5mm, outer=13.5mm, headheight=14pt, headsep=6mm, footskip=9.5mm",
        code_max_chars=81, body=(9.5, 12), code_inline=9, code_block=(7.4, 10), vedette=11,
        categorie=8.5, renvois=8, note=(8.5, 11), table=(8, 10), folio=8, toc=(7.5, 9),
        letter=150, part=60, entry_gap="10pt", image_gap="7pt", image_height="110mm", picto="3mm",
    ),
}

STATUS_FR = {
    # BIP (BIP-0003 et anciens statuts de BIP-0002)
    "draft": "Brouillon", "complete": "Complet", "deployed": "Déployé", "closed": "Clos",
    "final": "Final", "active": "Actif", "proposed": "Proposé", "withdrawn": "Retiré",
    "replaced": "Remplacé", "rejected": "Rejeté", "obsolete": "Obsolète", "deferred": "Reporté",
}


def load_legal() -> dict:
    with open(TEMPLATES_DIR / "legal.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _fs(size, leading=None) -> str:
    leading = leading if leading is not None else round(size * 1.2, 1)
    return rf"\fontsize{{{size}}}{{{leading}}}\selectfont"


# --------------------------------------------------------------------------
# Préambule
# --------------------------------------------------------------------------

def _preamble(fmt: PdfFormat, legal: dict, book: Book) -> str:
    static = (FONTS_DIR / "static").as_posix() + "/"
    pictos = PICTOGRAMS_DIR.as_posix() + "/"
    title = book.edition.title
    subtitle = book.edition.subtitle
    isbn = legal.get(fmt.isbn_key, "")
    keywords = f"Bitcoin, {legal.get('license', '')}" + (f", ISBN {isbn}" if isbn else "")
    body, body_lead = fmt.body
    return rf"""% {title} - édition {book.edition.id}, format {fmt.id}
% Mise en page : charte graphique 2027 (design/charte-2027.md)
\documentclass[9pt,twoside,openright]{{extbook}}

\usepackage{{fontspec}}
\usepackage{{polyglossia}}
\setdefaultlanguage{{french}}
\setotherlanguage{{english}}

\usepackage[{fmt.geometry()}, includehead, includefoot]{{geometry}}

% Polices : instances statiques d'Archivo et d'Atkinson Hyperlegible Mono (fonts/static/)
\setmainfont{{ArchivoTexte}}[Path={static}, Extension=.ttf, UprightFont=*-Regular, ItalicFont=*-Italic, BoldFont=*-Bold]
\setsansfont{{ArchivoTexte}}[Path={static}, Extension=.ttf, UprightFont=*-Regular, ItalicFont=*-Italic, BoldFont=*-Bold]
\setmonofont{{AtkinsonHyperlegibleMono}}[Path={static}, Extension=.ttf, UprightFont=*-Regular, ItalicFont=*-Italic, BoldFont=*-Bold]
\newfontfamily\vedettefont{{ArchivoVedette-Regular}}[Path={static}, Extension=.ttf, LetterSpace=1]
\newfontfamily\categoriefont{{ArchivoCategorie-Regular}}[Path={static}, Extension=.ttf, Numbers=Tabular]
\newfontfamily\titrefont{{ArchivoTitre-Regular}}[Path={static}, Extension=.ttf]
\newfontfamily\couverturefont{{ArchivoCouverture-Regular}}[Path={static}, Extension=.ttf]

% Formules : Fira Math, seule exception aux deux familles (charte, section 3)
\usepackage{{amsmath}}
\usepackage{{unicode-math}}
\setmathfont{{FiraMath-Regular.otf}}

\renewcommand{{\normalsize}}{{{_fs(body, body_lead)}}}
\normalsize
\newcommand{{\inlinecodesize}}{{{_fs(fmt.code_inline)}}}
\newcommand{{\codeblocksize}}{{{_fs(*fmt.code_block)}}}
\newcommand{{\notesize}}{{{_fs(*fmt.note)}}}
\newcommand{{\tablesize}}{{{_fs(*fmt.table)}\addfontfeature{{Numbers=Tabular}}}}

\usepackage{{microtype}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.3em}}
\usepackage{{ragged2e}}
\justifying
\tolerance=1000
\emergencystretch=3em
\hyphenpenalty=50
\exhyphenpenalty=50
\widowpenalty=10000
\clubpenalty=10000
\raggedbottom

\usepackage{{xcolor}}
\definecolor{{codebg}}{{HTML}}{{EBEBEB}}
\definecolor{{linkcolor}}{{RGB}}{{0, 0, 0}}

\usepackage[colorlinks=true, linkcolor=linkcolor, urlcolor=linkcolor, pdfborder={{0 0 0}},
  pdftitle={{{title}}}, pdfauthor={{{legal.get('author', '')}}},
  pdfsubject={{{title} : {subtitle}}}, pdfkeywords={{{keywords}}}]{{hyperref}}
\urlstyle{{same}}

\usepackage{{graphicx}}
\graphicspath{{{{{pictos}}}}}
\newcommand{{\imagespace}}{{{fmt.image_gap}}}
\newcommand{{\imagemaxheight}}{{{fmt.image_height}}}

\usepackage{{array}}
\usepackage{{colortbl}}
\usepackage{{xltabular}}
\usepackage{{multicol}}
\setlength{{\multicolsep}}{{0pt}}
\setlength{{\columnsep}}{{1.2em}}

% Listes : puce, retrait de 4 mm, 2 pt entre les éléments
\usepackage{{enumitem}}
\setlist[itemize]{{label=•, topsep=2pt, itemsep=2pt, parsep=0pt, leftmargin=4mm, before=\vspace{{-\parskip}}}}
\setlist[enumerate]{{topsep=2pt, itemsep=2pt, parsep=0pt, leftmargin=5mm, before=\vspace{{-\parskip}}}}

% Citations : italique, retrait de 4 mm
\renewenvironment{{quote}}{{\list{{}}{{\leftmargin=4mm\rightmargin=0pt\topsep=2pt}}\item\relax\itshape}}{{\endlist}}

% Code : fond gris 8 %, sans cadre
\usepackage{{tcolorbox}}
\tcbuselibrary{{breakable,skins}}
\newtcolorbox{{codeblock}}{{colback=codebg, colframe=codebg, boxrule=0pt, arc=0pt, boxsep=0pt,
  left=2mm, right=2mm, top=2mm, bottom=2mm, breakable, fontupper=\ttfamily\codeblocksize\raggedright}}
\usepackage{{soul}}
\DeclareRobustCommand{{\inlinecodelong}}[1]{{\begingroup\sethlcolor{{codebg}}\ttfamily\inlinecodesize\hl{{\,#1\,}}\endgroup}}

\usepackage{{csquotes}}
\usepackage{{needspace}}

% En-têtes : folio et titre courant en Archivo Catégorie, mots vedettes en capitales
\usepackage{{fancyhdr}}
\newcommand{{\currentletter}}{{}}
\newcommand{{\foliofont}}{{\categoriefont{_fs(fmt.folio)}}}
\fancypagestyle{{dictionary}}{{
  \fancyhf{{}}
  \fancyhead[CE,CO]{{\foliofont\currentletter}}
  \fancyhead[LE]{{\foliofont\rightmark}}
  \fancyhead[RO]{{\foliofont\leftmark}}
  \fancyfoot[C]{{\foliofont\thepage}}
  \renewcommand{{\headrulewidth}}{{0pt}}
  \renewcommand{{\footrulewidth}}{{0pt}}
}}
\fancypagestyle{{frontmatter}}{{
  \fancyhf{{}}
  \fancyfoot[C]{{\foliofont\thepage}}
  \renewcommand{{\headrulewidth}}{{0pt}}
  \renewcommand{{\footrulewidth}}{{0pt}}
}}
\fancypagestyle{{letterpage}}{{\fancyhf{{}}\renewcommand{{\headrulewidth}}{{0pt}}\renewcommand{{\footrulewidth}}{{0pt}}}}

% Pages blanches insérées par \cleardoublepage : sans en-tête
\makeatletter
\renewcommand{{\cleardoublepage}}{{\clearpage\if@twoside\ifodd\c@page\else\hbox{{}}\thispagestyle{{empty}}\newpage\fi\fi}}
\makeatother

\newcommand{{\cleanurl}}[1]{{\textenglish{{\url{{#1}}}}}}

% Mot vedette : Archivo Vedette, capitales, interlettrage +1 %, sans cartouche
\newcommand{{\vedette}}[1]{{{{\vedettefont{_fs(fmt.vedette)}#1}}}}
% Catégorie : Archivo Catégorie, casse de phrase
\newcommand{{\categorie}}[1]{{{{\categoriefont{_fs(fmt.categorie)}#1}}}}
% Renvois : « Voir aussi : » puis les titres en Archivo Vedette, séparés de 3 mm
\newcommand{{\renvoisfont}}{{\vedettefont{_fs(fmt.renvois)}}}
\newcommand{{\renvoislabel}}{{{_fs(fmt.renvois)}}}
\newcommand{{\entrygap}}{{\vspace{{{fmt.entry_gap}}}}}
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
\begin{{center}}{{\titrefont\fontsize{{20}}{{24}}\selectfont {escape(book.edition.title)}}}\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _title_page(book: Book, legal: dict) -> str:
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{3cm}}
\begin{{center}}
{{\couverturefont\fontsize{{30}}{{32}}\selectfont {escape(book.edition.title.upper())}}}\\[0.6cm]
{{\categoriefont\fontsize{{11}}{{14}}\selectfont {escape(book.edition.subtitle)}}}
\end{{center}}
\vfill
\begin{{center}}{{\fontsize{{12}}{{16}}\selectfont\itshape {escape(legal.get('author', ''))}}}\end{{center}}
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
{{\small
{body}
\par}}
\clearpage"""


def _final_page(book: Book, legal: dict, fmt: PdfFormat) -> str:
    body = "\\\\[0.4em]\n".join(_legal_lines(book, legal, fmt))
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}\small
{body}
\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _front_title(title: str) -> str:
    return rf"\begin{{center}}{{\titrefont\fontsize{{16}}{{20}}\selectfont {title}}}\end{{center}}\vspace{{0.4em}}"


def _front_text(title: str, template: str) -> str:
    path = TEMPLATES_DIR / template
    content = path.read_text(encoding="utf-8") if path.exists() else ""
    latex = markdown_to_latex(clean_content(content))
    # Intertitres des textes liminaires : Archivo Vedette, comme les mots vedettes
    latex = re.sub(r"\\section\*\{(.+?)\}", r"\\par\\vspace{0.6em}\\noindent\\vedette{\1}\\par\\nopagebreak", latex)
    latex = re.sub(r"\\subsection\*\{(.+?)\}", r"\\par\\vspace{0.4em}\\noindent\\vedette{\1}\\par\\nopagebreak", latex)
    return rf"""
\clearpage\thispagestyle{{frontmatter}}
{_front_title(title)}
{latex}
\clearpage"""


# --------------------------------------------------------------------------
# Table des matières
# --------------------------------------------------------------------------

def _toc(book: Book, fmt: PdfFormat) -> str:
    toc_font = _fs(*fmt.toc) + r"\addfontfeature{Numbers=Tabular}"
    out = [rf"""
\clearpage\thispagestyle{{frontmatter}}
{_front_title("Table des matières")}"""]
    out.append(r"{\small")
    for s in book.edition.sections:
        out.append(rf"\noindent\hyperlink{{part-{s.id}}}{{\vedette{{{escape(s.title.upper())}}}}}\dotfill\pageref*{{part:{s.id}}}\par")
    out.append(r"}\vspace{1.2em}")

    for s in book.edition.sections:
        if s.kind != "dictionary":
            continue
        out.append(rf"\needspace{{6\baselineskip}}\noindent\vedette{{{escape(s.title.upper())}}}\par\vspace{{0.4em}}")
        for letter, defs in s.letters.items():
            out.append(rf"\needspace{{5\baselineskip}}\par\vspace{{0.6em}}\noindent\vedette{{{letter}}}\par\nopagebreak\vspace{{0.2em}}")
            out.append(r"\begin{multicols}{2}")
            out.append(rf"{toc_font}\raggedright\setlength{{\parskip}}{{0.12em}}")
            for d in defs:
                out.append(rf"\noindent\hyperlink{{{d.slug}}}{{{escape(d.title)}}}\dotfill\pageref*{{def:{d.slug}}}\par")
            out.append(r"\end{multicols}")
        out.append(r"\vspace{1.5em}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Parties
# --------------------------------------------------------------------------

def _part_opener(section: Section, fmt: PdfFormat) -> str:
    intro = ""
    if section.intro:
        intro = r"\vspace{1cm}" + "\n\n" + markdown_to_latex(clean_content(section.intro), inline_only=True) + "\n"
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{}}
\phantomsection\hypertarget{{part-{section.id}}}{{}}\label{{part:{section.id}}}
\vspace*{{4cm}}
\noindent{{\couverturefont\fontsize{{{fmt.part}}}{{{fmt.part}}}\selectfont\raggedright {escape(section.title.upper())}\par}}
{intro}
\clearpage"""


def _letter_page(letter: str, fmt: PdfFormat) -> str:
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{{letter}}}
\vspace*{{\fill}}
\begin{{center}}{{\couverturefont\fontsize{{{fmt.letter}}}{{{fmt.letter}}}\selectfont {letter}}}\end{{center}}
\vspace*{{\fill}}
\clearpage
\pagestyle{{dictionary}}"""


def _letter_heading(letter: str) -> str:
    return rf"""
\renewcommand{{\currentletter}}{{{letter}}}
\par\needspace{{6\baselineskip}}\vspace{{1.2em}}
\noindent{{\couverturefont\fontsize{{28}}{{30}}\selectfont {letter}}}\par\nopagebreak
\vspace{{0.3em}}"""


def _meta_line(book: Book, d) -> str:
    """Ligne sous le mot vedette : pictogramme, catégorie en casse de phrase, traduction."""
    bits = []
    if d.category:
        picto = book.taxonomy.pictogram(d.category) if book.taxonomy else None
        label = escape(book.taxonomy.display(d.category) if book.taxonomy else d.category)
        icon = ""
        if picto and (PICTOGRAMS_DIR / f"{picto}.pdf").exists():
            icon = rf"\raisebox{{-0.6mm}}{{\includegraphics[height=3mm]{{{picto}.pdf}}}}\hspace{{1.2mm}}"
        bits.append(icon + label)
    if d.english_term:
        bits.append(rf"EN\,: {escape(d.english_term)}")
    elif d.french_term:
        bits.append(rf"FR\,: {escape(d.french_term)}")
    if not bits:
        return ""
    return r"\noindent\categorie{" + r"\enspace·\enspace ".join(bits) + r"}\par\nopagebreak"


def _see_also(targets, label: str = "Voir aussi") -> str:
    if not targets:
        return ""
    links = (r"\hspace{3mm}" + "\n").join(
        rf"\mbox{{\hyperlink{{{t.slug}}}{{{escape(t.title)}}}}}" for t in targets)
    return "\n".join([
        r"\par\nopagebreak\vspace{1pt}",
        r"{\raggedright\renvoislabel " + label + r"\,: \renvoisfont " + links + r"\par}",
    ])


def _body(content: str, assets_dir: Optional[Path], fmt: PdfFormat) -> str:
    """Corps d'une entrée ; une note finale tout en italique passe au corps de note."""
    content = clean_content(content).strip()
    paragraphs = re.split(r"\n\s*\n", content)
    note = ""
    if len(paragraphs) > 1 and re.fullmatch(r"\*[^*\n](?:.|\n)*[^*\n]\*", paragraphs[-1].strip()):
        note = markdown_to_latex(paragraphs[-1], assets_dir=assets_dir, code_max_chars=fmt.code_max_chars)
        content = "\n\n".join(paragraphs[:-1])
    body = markdown_to_latex(content, assets_dir=assets_dir, code_max_chars=fmt.code_max_chars)
    if note:
        body += "\n\n{\\notesize " + note + "\\par}"
    return body


def _entry(book: Book, section: Section, d, fmt: PdfFormat) -> str:
    title = escape(d.title)
    parts = [
        r"\par\needspace{4\baselineskip}\entrygap",
        rf"\label{{def:{d.slug}}}\markboth{{{title}}}{{{title}}}\hypertarget{{{d.slug}}}{{}}",
        rf"\noindent\vedette{{{title}}}\par\nopagebreak\vspace{{1pt}}",
        _meta_line(book, d),
        r"\nopagebreak",
    ]
    text = book.body(d, section)
    body = _body(text, d.path / "assets", fmt) if section.version == "developpee" else \
        markdown_to_latex(clean_content(text), assets_dir=d.path / "assets", code_max_chars=fmt.code_max_chars)
    parts.append(body)
    if section.version == "developpee":
        parts.append(_see_also(book.cross_references(d)))
    return "\n".join(p for p in parts if p)


def _dictionary_section(book: Book, section: Section, fmt: PdfFormat) -> str:
    out = [_part_opener(section, fmt), r"\pagestyle{dictionary}"]
    for letter, defs in section.letters.items():
        out.append(_letter_page(letter, fmt) if section.letter_pages else _letter_heading(letter))
        for d in defs:
            out.append(_entry(book, section, d, fmt))
    return "\n".join(out)


def _chronology_section(book: Book, section: Section, fmt: PdfFormat) -> str:
    out = [_part_opener(section, fmt), r"\pagestyle{dictionary}"]
    year = None
    for ev in section.events:
        if ev.year != year:
            year = ev.year
            out.append(_letter_heading(str(year)))
        date = escape(ev.date_fr())
        out.append(r"\par\needspace{3\baselineskip}\vspace{4pt}")
        out.append(rf"\markboth{{{year}}}{{{year}}}\noindent\vedette{{{date.upper()}}}\enspace{{\itshape {inline(ev.title)}}}\par\nopagebreak")
        out.append(markdown_to_latex(clean_content(ev.text), inline_only=True))
        out.append(_see_also(book.related(ev.related), "Voir"))
    return "\n".join(out)


def _status_label(doc) -> str:
    labels = []
    for s in doc.status:
        fr = STATUS_FR.get(s.lower())
        labels.append(fr if fr and fr.lower() == s.lower() else f"{fr} ({s})" if fr else s)
    return ", ".join(labels)


def _specs_section(book: Book, section: Section, fmt: PdfFormat) -> str:
    out = [_part_opener(section, fmt), r"\pagestyle{dictionary}"]
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
            out.append(r"\par\needspace{4\baselineskip}\entrygap")
            out.append(rf"\markboth{{{ident}}}{{{ident}}}{anchors}")
            out.append(rf"\noindent\vedette{{{ident.upper()}}}\par\nopagebreak\vspace{{1pt}}")
            meta = []
            status = _status_label(doc)
            if status:
                meta.append(rf"Statut\,: {escape(status)}")
            if doc.type:
                meta.append(rf"Type\,: {escape(doc.type)}")
            if doc.created:
                meta.append(rf"Créé le\,: {escape(doc.created)}")
            if meta:
                out.append(r"\noindent\categorie{" + r"\enspace·\enspace ".join(meta) + r"}\par\nopagebreak")
            if doc.title:
                out.append(rf"\noindent\textenglish{{\textit{{{inline(doc.title)}}}}}\par\nopagebreak")
            if doc.summary:
                out.append(markdown_to_latex(clean_content(doc.summary), inline_only=True) + r"\par")
            out.append(_see_also(book.related(doc.related), "Voir"))
            linked = book.definition_for(doc)
            if section.detail and linked:
                out.append(r"\vspace{0.2em}")
                out.append(_body(linked.content, linked.path / "assets", fmt))
    return "\n".join(out)


# --------------------------------------------------------------------------
# Assemblage et compilation
# --------------------------------------------------------------------------

def build_latex(book: Book, fmt: PdfFormat, legal: Optional[dict] = None) -> str:
    legal = legal or load_legal()
    s = [_preamble(fmt, legal, book), r"\begin{document}", r"\frontmatter", r"\pagestyle{frontmatter}",
         _half_title(book), r"\cleardoublepage", _title_page(book, legal), _copyright_page(book, legal, fmt),
         r"\clearpage\thispagestyle{empty}\null",
         _front_text("Contributeurs et remerciements", "contributors.md"),
         _front_text("Note de l'auteur", "introduction.md"),
         r"\cleardoublepage", _toc(book, fmt),
         r"\mainmatter", r"\pagestyle{dictionary}", r"\setcounter{page}{1}"]
    for section in book.edition.sections:
        if section.kind == "dictionary":
            s.append(_dictionary_section(book, section, fmt))
        elif section.kind == "chronology":
            s.append(_chronology_section(book, section, fmt))
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
        # Une passe par processus, jusqu'à ce que le .aux ne bouge plus. Les recompilations
        # automatiques de Tectonic dans un même processus gonflent des lignes de plusieurs
        # dizaines de points (constaté avec Tectonic 0.17 : 936 pages au lieu de 744).
        aux = tex_path.with_suffix(".aux")
        if aux.exists():
            aux.unlink()
        result, previous = None, None
        for _ in range(5):
            cmd = [binary, "-X", "compile", "--reruns", "0", "--keep-intermediates", "--keep-logs",
                   "--outdir", str(workdir), str(tex_path)]
            result = subprocess.run(cmd, capture_output=True, text=True, errors="replace", cwd=workdir)
            if result.returncode != 0:
                break
            current = aux.read_text(errors="replace") if aux.exists() else ""
            if current == previous:
                break
            previous = current
        return result
    result = None
    for _ in range(2):  # deux passes : références de pages de la table des matières
        cmd = [binary, "-interaction=nonstopmode", "-halt-on-error", "-output-directory", str(workdir), str(tex_path)]
        result = subprocess.run(cmd, capture_output=True, text=True, errors="replace", cwd=workdir)
        if result.returncode != 0:
            break
    return result


def _page_count(pdf: Path) -> int:
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout if shutil.which("pdfinfo") else ""
    m = re.search(r"^Pages:\s+(\d+)", out, flags=re.MULTILINE)
    return int(m.group(1)) if m else 0


def generate(book: Book, fmt_id: str = "broche", output_dir: Optional[Path] = None) -> Optional[Path]:
    """Génère le PDF d'une édition dans un format. Retourne le chemin, ou None en cas d'échec."""
    fmt = FORMATS[fmt_id]
    output_dir = output_dir or BUILD_DIR / book.edition.id
    workdir = output_dir / f"tex{fmt.suffix or '-broche'}"
    workdir.mkdir(parents=True, exist_ok=True)
    name = f"{book.edition.file}{fmt.suffix}"
    tex_path = workdir / f"{name}.tex"
    pdf = workdir / f"{name}.pdf"

    for attempt in range(2):
        tex_path.write_text(build_latex(book, fmt), encoding="utf-8")
        rel = tex_path.relative_to(BASE_DIR) if tex_path.is_relative_to(BASE_DIR) else tex_path
        print(f"  Compilation de {rel} (marge intérieure {fmt.inner})…")
        result = _compile(tex_path)
        if result.returncode != 0 or not pdf.exists():
            log = workdir / f"{name}.log"
            tail = (result.stdout or "")[-1500:] + (result.stderr or "")[-1500:]
            print(f"[ERREUR] La compilation a échoué ({tex_path}).\n{tail}")
            if log.exists():
                for line in [l for l in log.read_text(errors="replace").splitlines() if l.startswith("!")][:10]:
                    print(f"  {line}")
            return None
        pages = _page_count(pdf)
        # Livre épais : KDP impose une marge intérieure plus large, on recompose une fois.
        if fmt.id == "broche" and pages > KDP_THICK_BOOK_PAGES and fmt.inner == "20mm" and attempt == 0:
            fmt = replace(fmt, inner="22.5mm")
            continue
        break

    final = output_dir / f"{name}.pdf"
    shutil.move(str(pdf), final)
    print(f"[OK] PDF : {final} ({pages} pages)")
    if fmt.id == "relie" and pages > 550:
        print(f"[ATTENTION] {pages} pages : KDP limite le relié à 550 pages (charte, section 4).")
    return final
