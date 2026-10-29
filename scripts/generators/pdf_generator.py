#!/usr/bin/env python3
"""
Génération du PDF d'une édition via XeLaTeX (ou Tectonic, son équivalent autonome).

Mise en page de la charte graphique 2027 (design/charte-2027.md, sections 3 et 4, branche
feat/couverture-2027) : Archivo en instances statiques (assets/fonts/static/), Atkinson Hyperlegible
Mono pour le code, Fira Math pour les formules. Deux brochés Amazon KDP, choisis par
l'édition (clé `format` de templates/editions.yaml) :
  - `couleur` : 7 × 10 po (17,78 × 25,4 cm), intérieur couleur premium, papier blanc,
    24 à 828 pages ; l'édition complète ;
  - `poche` : 5 × 8 po (12,7 × 20,32 cm), intérieur noir et blanc ; l'édition « essentiel ».
La couleur suit la charte (section 2) en recettes CMJN ; en noir et blanc, la Figue devient
du noir et les schémas passent en version « -nb ».
"""

import re
import shutil
import subprocess
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import yaml

from ..config import BASE_DIR, BUILD_DIR, DEFINITIONS_DIR, FONTS_DIR, PICTOGRAMS_DIR, TEMPLATES_DIR, TEXTS_DIR, find_tex_engine
from ..core.book import Book, Section
from ..core import i18n
from . import images
from .latex import clean_content, escape, inline, markdown_to_latex

# Marge intérieure minimale d'un broché KDP selon le nombre de pages (sans fond perdu ; marge
# extérieure, haute et basse : 6,4 mm au moins). Source : aide KDP, « Paperback and hardcover
# manuscript formatting », https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6
KDP_GUTTER_MM = ((150, 9.6), (300, 12.7), (500, 15.9), (700, 19.1), (828, 22.3))
KDP_MIN_PAGES, KDP_MAX_PAGES = 24, 828


def kdp_gutter(pages: int) -> float:
    """Marge intérieure minimale (mm) exigée par KDP pour ce nombre de pages."""
    return next((mm for limit, mm in KDP_GUTTER_MM if pages <= limit), KDP_GUTTER_MM[-1][1])


@dataclass(frozen=True)
class PdfFormat:
    id: str
    label: str
    color: bool              # intérieur couleur (sinon noir et blanc)
    isbn_key: str
    paper: str               # paperwidth, paperheight
    inner: float             # marge intérieure (mm), relevée si KDP en exige plus
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
        return f"{self.paper}, inner={self.inner}mm, {self.margins}"


FORMATS = {
    # Livre complet : grand format en couleur, corps du broché de la charte (9 / 11,5 pt,
    # section 3) pour rester sous 750 pages avec les schémas 2027.
    "couleur": PdfFormat(
        id="couleur", label="7 × 10 po, couleur", color=True, isbn_key="isbn_paperback",
        paper="paperwidth=17.78cm, paperheight=25.4cm", inner=25.5,
        margins="top=9.5mm, bottom=9.5mm, outer=13.5mm, headheight=14pt, headsep=6mm, footskip=9.5mm",
        code_max_chars=81, body=(9, 11.5), code_inline=8.5, code_block=(7.4, 10), vedette=11,
        categorie=8.5, renvois=8, note=(8.5, 11), table=(8, 10), folio=8, toc=(7.5, 9),
        letter=150, part=60, entry_gap="9pt", image_gap="6pt", image_height="90mm", picto="3mm",
    ),
    # Essentiel : livre de poche en noir et blanc, réglages du broché de la charte.
    "poche": PdfFormat(
        id="poche", label="5 × 8 po, noir et blanc", color=False, isbn_key="",
        paper="paperwidth=12.7cm, paperheight=20.32cm", inner=16,
        margins="top=8mm, bottom=8mm, outer=10mm, headheight=12pt, headsep=5mm, footskip=8mm",
        code_max_chars=58, body=(9, 11.5), code_inline=8.5, code_block=(7.4, 10), vedette=10.5,
        categorie=8, renvois=7.5, note=(8, 10.5), table=(7.5, 9.5), folio=7.5, toc=(7, 8.5),
        letter=120, part=44, entry_gap="9pt", image_gap="6pt", image_height="85mm", picto="3mm",
    ),
}

def load_legal(lang: str = i18n.SOURCE_LANG) -> dict:
    """Mentions légales : templates/<langue>/legal.yaml, complété par celui de la langue d'origine."""
    data = {}
    for path in (TEXTS_DIR / "legal.yaml", i18n.texts_dir(lang) / "legal.yaml"):
        if path.exists():
            with open(path, encoding="utf-8") as f:
                data.update(yaml.safe_load(f) or {})
    return data


def _colors(fmt: PdfFormat) -> str:
    """Couleurs de la charte (section 2). Couleur : recettes CMJN de la charte, écrites telles
    quelles (convertir l'hexadécimal donnerait une Figue plus terne). Noir et blanc : la Figue
    devient du noir, l'Écorce garde son N70."""
    if fmt.color:
        return "\n".join([
            "% Charte 2027 : Figue (C0 M100 J0 N35), Écorce (N70), gris 8 % du code ; texte en noir pur",
            r"\definecolor{figue}{cmyk}{0,1,0,0.35}",
            r"\definecolor{ecorce}{cmyk}{0,0,0,0.70}",
            r"\definecolor{codebg}{cmyk}{0,0,0,0.08}",
        ])
    return "\n".join([
        "% Charte 2027, intérieur noir et blanc : Figue en noir, Écorce N70, gris 8 % du code",
        r"\definecolor{figue}{gray}{0}",
        r"\definecolor{ecorce}{gray}{0.30}",
        r"\definecolor{codebg}{gray}{0.92}",
    ])


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
\setdefaultlanguage{{{"english" if book.lang == "en" else "french"}}}
\setotherlanguage{{{"french" if book.lang == "en" else "english"}}}

\usepackage[{fmt.geometry()}, includehead, includefoot]{{geometry}}

% Polices : instances statiques d'Archivo et d'Atkinson Hyperlegible Mono (assets/fonts/static/)
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
\newcommand{{\creditsize}}{{{_fs(7, 8.5)}}}
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
{_colors(fmt)}

% Liens sans couleur propre : chaque élément porte la couleur que lui donne la charte.
\usepackage[hidelinks, pdfborder={{0 0 0}},
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

% En-têtes : folio et titre courant en Archivo Catégorie, mots vedettes en capitales ;
% titre courant en Figue, comme les mots vedettes qu'il reprend, folio en noir
\usepackage{{fancyhdr}}
\newcommand{{\currentletter}}{{}}
\newcommand{{\foliofont}}{{\categoriefont{_fs(fmt.folio)}}}
\fancypagestyle{{dictionary}}{{
  \fancyhf{{}}
  \fancyhead[CE,CO]{{\foliofont\color{{figue}}\currentletter}}
  \fancyhead[LE]{{\foliofont\color{{figue}}\rightmark}}
  \fancyhead[RO]{{\foliofont\color{{figue}}\leftmark}}
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

\newcommand{{\cleanurl}}[1]{{{{\color{{figue}}\textenglish{{\url{{#1}}}}}}}}

% Mot vedette : Archivo Vedette, capitales, interlettrage +1 %, sans cartouche, en Figue
\newcommand{{\vedette}}[1]{{{{\vedettefont{_fs(fmt.vedette)}\color{{figue}}#1}}}}
% Catégorie : Archivo Catégorie, casse de phrase
\newcommand{{\categorie}}[1]{{{{\categoriefont{_fs(fmt.categorie)}#1}}}}
% Renvois : « Voir aussi : » puis les titres en Archivo Vedette, séparés de 3 mm, en Figue (liens)
\newcommand{{\renvoisfont}}{{\vedettefont{_fs(fmt.renvois)}\color{{figue}}}}
\newcommand{{\renvoislabel}}{{{_fs(fmt.renvois)}}}
\newcommand{{\entrygap}}{{\vspace{{{fmt.entry_gap}}}}}
"""


# --------------------------------------------------------------------------
# Pages liminaires et finales
# --------------------------------------------------------------------------

def _date(now: datetime, lang: str) -> str:
    if lang == "en":
        return i18n.date_label(lang, now.year, now.month, now.day)
    return f"{now.day:02d} {i18n.MONTHS['fr'][now.month - 1]} {now.year}"


def _half_title(book: Book) -> str:
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{\fill}}
\begin{{center}}{{\titrefont\fontsize{{20}}{{24}}\selectfont\color{{figue}} {escape(book.edition.title)}}}\end{{center}}
\vspace*{{\fill}}
\clearpage"""


def _title_page(book: Book, legal: dict) -> str:
    return rf"""
\clearpage\thispagestyle{{empty}}
\vspace*{{3cm}}
\begin{{center}}
{{\couverturefont\fontsize{{30}}{{32}}\selectfont\color{{figue}} {escape(book.edition.title.upper())}}}\\[0.6cm]
{{\categoriefont\fontsize{{11}}{{14}}\selectfont {escape(book.edition.subtitle)}}}
\end{{center}}
\vfill
\begin{{center}}{{\fontsize{{12}}{{16}}\selectfont\itshape {escape(legal.get('author', ''))}}}\end{{center}}
\vspace*{{2cm}}
\clearpage"""


def _legal_lines(book: Book, legal: dict, fmt: PdfFormat) -> List[str]:
    now = datetime.now()
    isbn = legal.get(fmt.isbn_key, "")
    lang = book.lang
    c = " : " if lang == i18n.SOURCE_LANG else ": "
    lines = [
        rf"\textbf{{© {now.year} {escape(legal.get('author', ''))}}}",
        rf"\textbf{{\textit{{{escape(book.edition.title)}{c}{escape(book.edition.subtitle)}}}}}",
        rf"{i18n.t(lang, 'version_of')} {_date(now, lang)}",
        rf"\cleanurl{{{legal.get('github_url', '')}}}",
        rf"{i18n.t(lang, 'licensed')} {escape(legal.get('license', ''))}",
        rf"\cleanurl{{{legal.get('license_url', '')}}}",
        rf"Lightning{c}{escape(legal.get('lightning_address', ''))}",
        rf"{i18n.t(lang, 'email')}{c}{escape(legal.get('email', ''))}",
        rf"{i18n.t(lang, 'website')}{c}\cleanurl{{{legal.get('website', '')}}}",
        rf"GitHub{c}\cleanurl{{{legal.get('github_profile', '')}}}",
    ]
    if isbn and book.edition.id == "complete":
        lines.append(rf"ISBN{c}{isbn}")
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
    return rf"\begin{{center}}{{\titrefont\fontsize{{16}}{{20}}\selectfont\color{{figue}} {title}}}\end{{center}}\vspace{{0.4em}}"


def _front_text(title: str, template: str, lang: str = i18n.SOURCE_LANG) -> str:
    path = i18n.texts_dir(lang) / template
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
{_front_title(i18n.t(book.lang, "contents"))}"""]
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
\noindent{{\couverturefont\fontsize{{{fmt.part}}}{{{fmt.part}}}\selectfont\raggedright\color{{figue}} {escape(section.title.upper())}\par}}
{intro}
\clearpage"""


def _letter_page(letter: str, fmt: PdfFormat) -> str:
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{{letter}}}
\vspace*{{\fill}}
\begin{{center}}{{\couverturefont\fontsize{{{fmt.letter}}}{{{fmt.letter}}}\selectfont\color{{figue}} {letter}}}\end{{center}}
\vspace*{{\fill}}
\clearpage
\pagestyle{{dictionary}}"""


def _letter_heading(letter: str) -> str:
    return rf"""
\renewcommand{{\currentletter}}{{{letter}}}
\par\needspace{{6\baselineskip}}\vspace{{1.2em}}
\noindent{{\couverturefont\fontsize{{28}}{{30}}\selectfont\color{{figue}} {letter}}}\par\nopagebreak
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


def _see_also(targets, label: str = "Voir aussi", lang: str = i18n.SOURCE_LANG) -> str:
    if not targets:
        return ""
    links = (r"\hspace{3mm}" + "\n").join(
        rf"\mbox{{\hyperlink{{{t.slug}}}{{{escape(t.title)}}}}}" for t in targets)
    return "\n".join([
        r"\par\nopagebreak\vspace{1pt}",
        r"{\raggedright\renvoislabel " + label + i18n.t(lang, "colon") + r"\renvoisfont " + links + r"\par}",
    ])


def _md(content: str, fmt: PdfFormat, d) -> str:
    """Markdown d'une entrée (images, crédits et largeur de code du format)."""
    return markdown_to_latex(content, assets_dir=d.assets_path, code_max_chars=fmt.code_max_chars,
                             color=fmt.color, credits=d.credits)


def _body(content: str, d, fmt: PdfFormat) -> str:
    """Corps d'une entrée ; une note finale tout en italique passe au corps de note."""
    content = clean_content(content).strip()
    paragraphs = re.split(r"\n\s*\n", content)
    note = ""
    if len(paragraphs) > 1 and re.fullmatch(r"\*[^*\n](?:.|\n)*[^*\n]\*", paragraphs[-1].strip()):
        note = _md(paragraphs[-1], fmt, d)
        content = "\n\n".join(paragraphs[:-1])
    body = _md(content, fmt, d)
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
    body = _body(text, d, fmt) if section.version == "developpee" else _md(clean_content(text), fmt, d)
    parts.append(body)
    if section.version == "developpee":
        parts.append(_see_also(book.cross_references(d), i18n.t(book.lang, "see_also"), book.lang))
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
        date = escape(ev.date_label(book.lang))
        out.append(r"\par\needspace{3\baselineskip}\vspace{4pt}")
        out.append(rf"\markboth{{{year}}}{{{year}}}\noindent\vedette{{{date.upper()}}}\enspace{{\itshape {inline(ev.title)}}}\par\nopagebreak")
        out.append(markdown_to_latex(clean_content(ev.text), inline_only=True))
        out.append(_see_also(book.related(ev.related), i18n.t(book.lang, "see"), book.lang))
    return "\n".join(out)


def _status_label(doc, lang: str = i18n.SOURCE_LANG) -> str:
    return ", ".join(i18n.status_label(lang, s) for s in doc.status)


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
            status = _status_label(doc, book.lang)
            c = i18n.t(book.lang, "colon")
            if status:
                meta.append(rf"{i18n.t(book.lang, 'status')}{c}{escape(status)}")
            if doc.type:
                meta.append(rf"{i18n.t(book.lang, 'type')}{c}{escape(doc.type)}")
            if doc.created:
                meta.append(rf"{i18n.t(book.lang, 'created')}{c}{escape(doc.created)}")
            if meta:
                out.append(r"\noindent\categorie{" + r"\enspace·\enspace ".join(meta) + r"}\par\nopagebreak")
            if doc.title:
                out.append(rf"\noindent\textenglish{{\textit{{{inline(doc.title)}}}}}\par\nopagebreak")
            if doc.summary:
                out.append(markdown_to_latex(clean_content(doc.summary), inline_only=True) + r"\par")
            out.append(_see_also(book.related(doc.related), i18n.t(book.lang, "see"), book.lang))
            linked = book.definition_for(doc)
            if section.detail and linked:
                out.append(r"\vspace{0.2em}")
                out.append(_body(linked.content, linked, fmt))
    return "\n".join(out)


# --------------------------------------------------------------------------
# Assemblage et compilation
# --------------------------------------------------------------------------

def build_latex(book: Book, fmt: PdfFormat, legal: Optional[dict] = None) -> str:
    legal = legal or load_legal(book.lang)
    s = [_preamble(fmt, legal, book), r"\begin{document}", r"\frontmatter", r"\pagestyle{frontmatter}",
         _half_title(book), r"\cleardoublepage", _title_page(book, legal), _copyright_page(book, legal, fmt),
         r"\clearpage\thispagestyle{empty}\null",
         _front_text(i18n.t(book.lang, "contributors"), "contributors.md", book.lang),
         _front_text(i18n.t(book.lang, "author_note"), "introduction.md", book.lang),
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


def generate(book: Book, output_dir: Optional[Path] = None) -> Optional[Path]:
    """Génère le PDF d'une édition, au format qu'elle demande. Retourne le chemin, ou None en cas d'échec."""
    fmt = FORMATS.get(book.edition.format)
    if fmt is None:
        print(f"[ERREUR] format PDF inconnu : {book.edition.format} (formats : {', '.join(FORMATS)})")
        return None
    output_dir = output_dir or BUILD_DIR / book.edition.id
    workdir = output_dir / "tex"
    workdir.mkdir(parents=True, exist_ok=True)
    name = book.edition.file
    tex_path = workdir / f"{name}.tex"
    pdf = workdir / f"{name}.pdf"
    if fmt.color:
        ready = images.prepare(sorted(DEFINITIONS_DIR.glob("*/*/assets/*.svg")))
        if not images.find_chrome():
            print("  [ATTENTION] Chrome introuvable : schémas en PNG couleur (CHROME_PATH=<chemin> pour le PDF vectoriel).")
        elif ready:
            print(f"  {ready} schéma(s) SVG convertis en PDF couleur ({images.CACHE_DIR})")

    for attempt in range(2):
        tex_path.write_text(build_latex(book, fmt), encoding="utf-8")
        rel = tex_path.relative_to(BASE_DIR) if tex_path.is_relative_to(BASE_DIR) else tex_path
        print(f"  Compilation de {rel} ({fmt.label}, marge intérieure {fmt.inner} mm)…")
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
        # Livre épais : si KDP exige une marge intérieure plus large, on recompose une fois.
        required = kdp_gutter(pages)
        if pages and fmt.inner < required and attempt == 0:
            fmt = replace(fmt, inner=round(required + 0.2, 1))
            continue
        break

    final = output_dir / f"{name}.pdf"
    shutil.move(str(pdf), final)
    print(f"[OK] PDF : {final} ({pages} pages, {fmt.label})")
    if pages and not KDP_MIN_PAGES <= pages <= KDP_MAX_PAGES:
        print(f"[ATTENTION] {pages} pages : KDP imprime de {KDP_MIN_PAGES} à {KDP_MAX_PAGES} pages "
              f"(broché, papier blanc{', couleur premium' if fmt.color else ''}).")
    elif fmt.color and pages > 600:
        print(f"  {pages} pages : couleur premium obligatoire chez KDP (la couleur standard s'arrête à 600 pages).")
    return final
