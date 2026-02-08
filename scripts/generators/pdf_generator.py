#!/usr/bin/env python3
"""
Génération du PDF via XeLaTeX.
Format KDP : 5.5" x 8.5" (13.97cm x 21.59cm)
"""

import os
import subprocess
import tempfile
import re
import yaml
from pathlib import Path
from datetime import datetime

from ..core.dictionary import Dictionary
from ..config import BASE_DIR, TEMPLATES_DIR, OUTPUT_PDF, DEFINITIONS_DIR


# Noms des mois en français (pour éviter les problèmes d'encodage avec locale)
MOIS_FR = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril",
    5: "mai", 6: "juin", 7: "juillet", 8: "août",
    9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"
}


def _load_legal_info() -> dict:
    """Charge les informations légales depuis le fichier YAML."""
    legal_path = TEMPLATES_DIR / "legal.yaml"
    if legal_path.exists():
        with open(legal_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    # Valeurs par défaut si le fichier n'existe pas
    return {
        'title': "Dictionnaire de Bitcoin",
        'subtitle': "Tout le vocabulaire technique de Bitcoin",
        'author': "Loïc Morel",
        'license': "CC BY-NC-SA 4.0",
        'license_url': "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        'github_url': "https://github.com/LoicPandul/Dictionnaire-de-Bitcoin",
        'website': "https://pandul.fr/",
        'github_profile': "https://github.com/LoicPandul/",
        'lightning_address': "sats@pandul.fr",
        'email': "loic@pandul.fr",
        'isbn': "XXXX"
    }


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère le PDF du dictionnaire au format KDP."""
    if output_path is None:
        output_path = OUTPUT_PDF

    print(f"Génération du PDF: {output_path}")

    # Charger les informations légales
    legal = _load_legal_info()

    # 1. Générer le contenu LaTeX complet
    latex_content = _build_latex_content(dictionary, legal)

    # 2. Écrire le fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', suffix='.tex', delete=False, encoding='utf-8') as f:
        f.write(latex_content)
        temp_tex = f.name

    try:
        # 3. Compiler avec XeLaTeX (2 passes pour les références de pages)
        output_dir = output_path.parent

        for pass_num in range(2):
            print(f"  Passe {pass_num + 1}/2...")
            cmd = [
                "xelatex",
                "-interaction=nonstopmode",
                "-output-directory", str(output_dir),
                "-jobname", "dictionnaire_temp",
                temp_tex
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=str(output_dir))

        # Vérifier si le PDF a été généré
        temp_pdf = output_dir / "dictionnaire_temp.pdf"

        if not temp_pdf.exists():
            print(f"[ERROR] XeLaTeX n'a pas généré de PDF")
            if result.stderr:
                print(f"Stderr: {result.stderr[-2000:]}")
            return False

        # Renommer le fichier de sortie
        if output_path.exists():
            output_path.unlink()
        temp_pdf.rename(output_path)

        # Nettoyer les fichiers auxiliaires
        for ext in ['.aux', '.log', '.out', '.toc']:
            aux_file = output_dir / f"dictionnaire_temp{ext}"
            if aux_file.exists():
                aux_file.unlink()

        print(f"[OK] PDF généré: {output_path}")
        return True

    finally:
        # Nettoyer le fichier temporaire
        if os.path.exists(temp_tex):
            os.unlink(temp_tex)


def _build_latex_content(dictionary: Dictionary, legal: dict) -> str:
    """Construit le document LaTeX complet."""
    sections = []

    # Préambule
    fonts_path = str(BASE_DIR / "fonts").replace('\\', '/') + '/'
    sections.append(_generate_preamble(fonts_path))

    # Début du document
    sections.append("\\begin{document}")

    # === PAGES LIMINAIRES ===
    sections.append("\\frontmatter")
    sections.append("\\pagestyle{frontmatter}")

    # 1. Faux-titre
    sections.append(_generate_half_title(legal))

    # 2. Verso blanc
    sections.append("\\cleardoublepage")

    # 3. Page de titre
    sections.append(_generate_title_page(legal))

    # 4. Mentions légales
    sections.append(_generate_copyright_page(legal))

    # 5. Page blanche unique
    sections.append("\\clearpage\\thispagestyle{frontmatter}\\null")

    # 6. Contributeurs et remerciements
    sections.append(_generate_contributors())

    # 7. Note de l'auteur (anciennement Introduction)
    sections.append(_generate_author_note())

    # 8. Page blanche si nécessaire
    sections.append("\\cleardoublepage")

    # 9. Table des matières (juste avant le contenu)
    sections.append(_generate_toc(dictionary))

    # === CORPS DU DICTIONNAIRE ===
    sections.append("\\mainmatter")
    sections.append("\\pagestyle{dictionary}")
    sections.append("\\setcounter{page}{1}")

    # Contenu par lettre
    for letter in dictionary.letters():
        sections.append(_create_letter_page(letter))
        for definition in dictionary.get_by_letter(letter):
            sections.append(_format_definition(definition))

    # === PAGES FINALES ===
    sections.append("\\backmatter")
    sections.append("\\pagestyle{frontmatter}")
    sections.append("\\cleardoublepage")
    sections.append(_generate_final_page(legal))
    sections.append("\\clearpage\\thispagestyle{frontmatter}\\null")
    sections.append("\\end{document}")

    return "\n\n".join(sections)


def _generate_preamble(fonts_path: str = "") -> str:
    """Génère le préambule LaTeX."""
    preamble = r"""% Dictionnaire de Bitcoin - Format KDP
\documentclass[9pt,twoside,openright]{book}

% Encodage et langue
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{french}
\setotherlanguage{english}

% Géométrie KDP 5.5" x 8.5" - Gutter accentué
\usepackage[
    paperwidth=13.97cm,
    paperheight=21.59cm,
    top=7mm,
    bottom=7mm,
    outer=7mm,
    inner=18mm,
    headheight=12pt,
    headsep=5mm,
    footskip=8mm,
    includehead,
    includefoot
]{geometry}

% Polices
\setmainfont{Arial}
\setsansfont{Arial}
\setmonofont{Fira Code}[
    Path=%%FONTSPATH%%,
    Extension=.ttf,
    UprightFont=FiraCode-Regular,
    BoldFont=FiraCode-Bold,
    Scale=0.85
]

% Typographie
\usepackage{microtype}
\usepackage{setspace}
\setstretch{1.10}

% Alinéa réduit de moitié et espacement entre paragraphes doublé
\setlength{\parindent}{0.5em}
\setlength{\parskip}{0.6em}

% Césure et justification
\usepackage{ragged2e}
\justifying
\tolerance=1000
\emergencystretch=3em
\hyphenpenalty=50
\exhyphenpenalty=50

% Éviter orphelines et veuves
\widowpenalty=10000
\clubpenalty=10000

% Couleurs
\usepackage{xcolor}
\definecolor{customgray}{RGB}{246, 248, 250}
\definecolor{inlinecodebg}{RGB}{239, 241, 243}
\definecolor{inlinecodeborder}{RGB}{208, 215, 222}
\definecolor{linkcolor}{RGB}{0, 0, 0}

% Liens (même police que le texte)
\usepackage[
    colorlinks=true,
    linkcolor=linkcolor,
    urlcolor=linkcolor,
    pdfborder={0 0 0}
]{hyperref}
\urlstyle{same}

% Images et TikZ pour les drapeaux
\usepackage{graphicx}
\usepackage{float}
\usepackage{tikz}

% Tableaux
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{colortbl}
\usepackage{multicol}
\arrayrulecolor{white}

% Listes avec espacement personnalisé
\usepackage{enumitem}
\setlist[itemize]{itemsep=0.6em, parsep=0pt, topsep=0.3em}

% Configuration multicol pour la TDM
\setlength{\multicolsep}{0pt}
\setlength{\columnsep}{0.5em}

% Code
\usepackage{listings}
\usepackage{tcolorbox}
\tcbuselibrary{listings,breakable,skins}

\lstset{
    basicstyle=\ttfamily\fontsize{9}{10}\selectfont,
    breaklines=true,
    breakatwhitespace=true,
    aboveskip=0.5em,
    belowskip=0.5em
}

% Bloc de code style GitHub (angles droits, breakable)
\newtcolorbox{codeblock}{
    colback=inlinecodebg,
    colframe=inlinecodeborder,
    boxrule=0.3pt,
    arc=0pt,
    boxsep=0pt,
    left=6pt,
    right=6pt,
    top=4pt,
    bottom=4pt,
    breakable,
    fontupper=\ttfamily\fontsize{9}{10}\selectfont\raggedright
}

% Code inline style GitHub - version courte (design complet avec bordure et coins arrondis)
\newtcbox{\inlinecode}{
    on line,
    colback=inlinecodebg,
    colframe=inlinecodeborder,
    boxrule=0.3pt,
    arc=2pt,
    boxsep=0pt,
    left=2.5pt,
    right=2.5pt,
    top=1pt,
    bottom=1pt,
    tcbox raise base,
    fontupper=\ttfamily\fontsize{9}{10}\selectfont
}

% Code inline - version longue (support saut de ligne, design simplifié)
\usepackage{soul}
\DeclareRobustCommand{\inlinecodelong}[1]{%
    \begingroup
    \sethlcolor{inlinecodebg}%
    \ttfamily\fontsize{9}{10}\selectfont
    \hl{\,#1\,}%
    \endgroup
}

% Mathématiques
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

% En-têtes et pieds de page
\usepackage{fancyhdr}

% Variable pour la lettre courante
\newcommand{\currentletter}{}

% Style dictionnaire
\fancypagestyle{dictionary}{
    \fancyhf{}
    \fancyhead[CE]{\small\textit{\currentletter}}
    \fancyhead[CO]{\small\textit{\currentletter}}
    \fancyhead[LE]{\scriptsize\textit{\leftmark}}
    \fancyhead[RO]{\scriptsize\textit{\rightmark}}
    \fancyfoot[C]{\small\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Style pages liminaires
\fancypagestyle{frontmatter}{
    \fancyhf{}
    \fancyfoot[C]{\small\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Style TDM
\fancypagestyle{toc}{
    \fancyhf{}
    \fancyfoot[C]{\small\thepage}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Style page lettre
\fancypagestyle{letterpage}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}

% Listes
\usepackage{enumitem}
\setlist[itemize]{
    topsep=0.2em,
    itemsep=0.05em,
    parsep=0pt,
    leftmargin=1.2em
}

% Citations
\usepackage{csquotes}

% Commande pour les URLs sans espace français avant les deux-points
\newcommand{\cleanurl}[1]{\textenglish{\url{#1}}}
\newcommand{\cleanhref}[2]{\textenglish{\href{#1}{#2}}}

% Commande pour vedette ajustée à la largeur du texte (cartouche noire)
\newcommand{\vedettefit}[1]{%
    \noindent\fcolorbox{black}{black}{%
        \hspace{0.3em}%
        {\color{white}\fontsize{10}{12}\selectfont\bfseries\addfontfeature{LetterSpace=3.0}#1}%
        \hspace{0.3em}%
    }%
}

% Commande pour cartouche lettre dans TDM (plus petit)
\newcommand{\tocletterbox}[1]{%
    \fcolorbox{black}{black}{%
        \hspace{0.2em}%
        {\color{white}\fontsize{11}{13}\selectfont\bfseries #1}%
        \hspace{0.2em}%
    }%
}

% Drapeaux en nuances de gris
\newcommand{\flagGB}{%
    \begin{tikzpicture}[baseline=-0.3ex, scale=0.12]
        \fill[gray!30] (0,0) rectangle (3,2);
        \fill[gray!60] (1.35,0) rectangle (1.65,2);
        \fill[gray!60] (0,0.85) rectangle (3,1.15);
        \draw[gray!80, line width=0.3pt] (0,0) -- (3,2);
        \draw[gray!80, line width=0.3pt] (0,2) -- (3,0);
    \end{tikzpicture}%
}

\newcommand{\flagFR}{%
    \begin{tikzpicture}[baseline=-0.3ex, scale=0.12]
        \fill[gray!40] (0,0) rectangle (1,2);
        \fill[gray!15] (1,0) rectangle (2,2);
        \fill[gray!60] (2,0) rectangle (3,2);
    \end{tikzpicture}%
}

% Pour éviter les orphelins de lettres dans TDM
\usepackage{needspace}
"""
    return preamble.replace('%%FONTSPATH%%', fonts_path)


def _generate_half_title(legal: dict) -> str:
    """Génère la page de faux-titre."""
    title = legal.get('title', 'Dictionnaire de Bitcoin')
    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}
\begin{{center}}
{{\fontsize{{18}}{{22}}\selectfont\bfseries {title}}}
\end{{center}}
\vspace*{{\fill}}
\clearpage
"""


def _generate_title_page(legal: dict) -> str:
    """Génère la page de titre."""
    title = legal.get('title', 'Dictionnaire de Bitcoin')
    subtitle = legal.get('subtitle', '')
    author = legal.get('author', '')
    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{3cm}}
\begin{{center}}
{{\fontsize{{22}}{{26}}\selectfont\bfseries {title}}}\\[0.6cm]
{{\fontsize{{11}}{{14}}\selectfont {subtitle.upper()}}}
\end{{center}}
\vfill
\begin{{center}}
{{\fontsize{{12}}{{16}}\selectfont\itshape {author}}}
\end{{center}}
\vspace*{{2cm}}
\clearpage
"""


def _generate_copyright_page(legal: dict) -> str:
    """Génère la page de mentions légales."""
    now = datetime.now()
    date_str = f"{now.day:02d} {MOIS_FR[now.month]} {now.year}"
    year = now.year

    title = legal.get('title', 'Dictionnaire de Bitcoin')
    subtitle = legal.get('subtitle', '')
    author = legal.get('author', '')
    license_name = legal.get('license', 'CC BY-NC-SA 4.0')
    license_url = legal.get('license_url', '')
    github_url = legal.get('github_url', '')
    website = legal.get('website', '')
    github_profile = legal.get('github_profile', '')
    lightning = legal.get('lightning_address', '')
    email = legal.get('email', '')
    isbn = legal.get('isbn', '')

    # Section ISBN (vide si non renseigné)
    isbn_line = rf"\noindent ISBN : {isbn}" if isbn else ""

    # Interligne uniforme de 0.4em entre chaque ligne
    sp = "0.4em"

    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}

\small
\setstretch{{1.0}}
\noindent\textbf{{© {year} {author}}}\\[{sp}]
\noindent\textbf{{\textit{{{title} : {subtitle}}}}}\\[{sp}]
\noindent Version du {date_str}\\[{sp}]
\noindent\textenglish{{\href{{{github_url}}}{{{github_url}}}}}\\[{sp}]
\noindent Cet ouvrage est sous licence {license_name}\\[{sp}]
\noindent\textenglish{{\href{{{license_url}}}{{{license_url}}}}}\\[{sp}]
\noindent Lightning : {lightning}\\[{sp}]
\noindent Email : {email}\\[{sp}]
\noindent Site web : \textenglish{{\href{{{website}}}{{{website}}}}}\\[{sp}]
\noindent GitHub : \textenglish{{\href{{{github_profile}}}{{{github_profile}}}}}\\[{sp}]
{isbn_line}

\clearpage
"""


def _generate_toc(dictionary: Dictionary) -> str:
    """Génère la table des matières avec numéros de page et cartouches."""
    toc_parts = []

    toc_parts.append(r"""
\clearpage
\thispagestyle{toc}
\begin{center}
{\fontsize{14}{18}\selectfont\bfseries TABLE DES MATIÈRES}
\end{center}
\vspace{0.3cm}
""")

    first_letter = True
    for letter in dictionary.letters():
        definitions = list(dictionary.get_by_letter(letter))
        count = len(definitions)

        # Espace entre les lettres (sauf avant la première)
        if not first_letter:
            toc_parts.append(r"\vspace{2.5em}")
        first_letter = False

        # Calcul de l'espace nécessaire pour éviter les orphelins
        # Règle : au moins 5 lignes de définitions (= 10 défs en 2 colonnes)
        # OU toutes les définitions si la lettre en a moins de 10
        if count <= 10:
            # Petite lettre : garder cartouche + toutes les définitions ensemble
            lines_for_defs = (count + 1) // 2  # division par 2 (2 colonnes)
            lines_needed = 2 + lines_for_defs  # cartouche + espacement + défs
        else:
            # Grande lettre : cartouche + au moins 5 lignes de définitions
            lines_needed = 8  # 1 cartouche + 2 espacement + 5 lignes minimum

        toc_parts.append(rf"\needspace{{{lines_needed}\baselineskip}}")

        # Lettre avec cartouche noire
        toc_parts.append(rf"\noindent\tocletterbox{{{letter}}}")
        toc_parts.append(r"\vspace{0.45em}")  # Espace après cartouche (+50%)

        # Utiliser multicols - laisser LaTeX gérer l'équilibrage naturellement
        # (pas de columnbreak manuel car ça casse la répartition sur plusieurs pages)
        toc_parts.append(r"\begin{multicols}{2}")
        toc_parts.append(r"\scriptsize\raggedright")
        toc_parts.append(r"\setlength{\parskip}{0.18em}")  # Interligne entre défs (+50%)

        for defn in definitions:
            slug = _make_slug(defn.title)
            safe_title = _escape_latex(defn.title)
            toc_parts.append(
                rf"\noindent\hyperlink{{{slug}}}{{{safe_title}}}"
                rf"\dotfill\pageref*{{def:{slug}}}\par"
            )

        toc_parts.append(r"\end{multicols}")

    return "\n".join(toc_parts)


def _generate_author_note() -> str:
    """Génère la page Note de l'auteur."""
    intro_path = TEMPLATES_DIR / "introduction.md"
    if intro_path.exists():
        content = intro_path.read_text(encoding='utf-8')
        content = _clean_content(content)
        content = _markdown_to_latex(content, use_cartouche_h1=True)
    else:
        content = ""

    return rf"""
\cleardoublepage
\thispagestyle{{frontmatter}}
\begin{{center}}
{{\fontsize{{14}}{{18}}\selectfont\bfseries NOTE DE L'AUTEUR}}
\end{{center}}
\vspace{{-0.2em}}

\small
{content}
\clearpage
"""


def _generate_contributors() -> str:
    """Génère la page des contributeurs."""
    contributors_path = TEMPLATES_DIR / "contributors.md"
    if contributors_path.exists():
        content = contributors_path.read_text(encoding='utf-8')
        content = _clean_content(content)
        content = _markdown_to_latex(content)
    else:
        content = ""

    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\begin{{center}}
{{\fontsize{{14}}{{18}}\selectfont\bfseries CONTRIBUTEURS ET REMERCIEMENTS}}
\end{{center}}
\vspace{{-0.2em}}

\small
{content}
\clearpage
"""


def _create_letter_page(letter: str) -> str:
    """Crée une page de séparation pour chaque lettre."""
    return rf"""
\cleardoublepage
\thispagestyle{{letterpage}}
\renewcommand{{\currentletter}}{{{letter}}}
\vspace*{{\fill}}
\begin{{center}}
{{\fontsize{{60}}{{72}}\selectfont\bfseries {letter}}}
\end{{center}}
\vspace*{{\fill}}
\clearpage
\pagestyle{{dictionary}}
"""


def _format_definition(definition) -> str:
    """Formate une définition pour le PDF."""
    parts = []

    slug = _make_slug(definition.title)
    title = definition.title
    safe_title = _escape_latex(title)

    # Empêcher vedette orpheline : garder vedette + catégorie + début de définition ensemble
    parts.append(r"\needspace{5\baselineskip}")

    # Label pour référence de page (utilisé dans TDM)
    parts.append(rf"\label{{def:{slug}}}")

    # Marquage pour les en-têtes
    parts.append(rf"\markboth{{{safe_title}}}{{{safe_title}}}")

    # Ancre hypertexte
    parts.append(rf"\hypertarget{{{slug}}}{{}}")

    # Vedette (cartouche noire)
    parts.append(rf"\vedettefit{{{safe_title}}}")
    parts.append(r"\vspace{-0.3em}")
    parts.append("")

    # Ligne de métadonnées
    metadata_parts = []

    if definition.category:
        cat = definition.category
        cat_formatted = cat[0].upper() + cat[1:].lower() if cat else ""
        safe_cat = _escape_latex(cat_formatted)
        metadata_parts.append(safe_cat)

    if definition.english_term:
        safe_term = _escape_latex(definition.english_term)
        metadata_parts.append(rf"\flagGB\ {safe_term}")
    elif definition.french_term:
        safe_term = _escape_latex(definition.french_term)
        metadata_parts.append(rf"\flagFR\ {safe_term}")

    if metadata_parts:
        metadata_line = r" \textperiodcentered\ ".join(metadata_parts)
        parts.append(rf"\noindent{{\scriptsize {metadata_line}}}")
        parts.append(r"\vspace{-0.3em}")
        parts.append("")

    # Contenu
    content = definition.content
    content = _clean_content(content)
    content = _fix_math_commands(content)
    content = _adjust_image_paths(content, definition)
    content = _markdown_to_latex(content)
    parts.append(content)

    parts.append(r"\vspace{0.8em}")

    return "\n".join(parts)


def _generate_final_page(legal: dict) -> str:
    """Génère la page finale."""
    year = datetime.now().year
    title = legal.get('title', '')
    subtitle = legal.get('subtitle', '')
    author = legal.get('author', '')
    license_name = legal.get('license', '')
    github_url = legal.get('github_url', '')
    website = legal.get('website', '')
    lightning = legal.get('lightning_address', '')

    sp = "0.4em"

    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}

\begin{{center}}
\small
\setstretch{{1.0}}
{{\bfseries {title}}}\\[{sp}]
{{\itshape {subtitle}}}\\[0.8em]
© {year} {author}\\[{sp}]
\textenglish{{\href{{{github_url}}}{{{github_url}}}}}\\[{sp}]
Licence {license_name}\\[0.8em]
Lightning : {lightning}\\[{sp}]
Site web : \textenglish{{\href{{{website}}}{{{website}}}}}
\end{{center}}

\vspace*{{\fill}}
\clearpage
"""


def _make_slug(title: str) -> str:
    """Crée un slug pour les ancres hypertexte."""
    import unicodedata
    slug = unicodedata.normalize('NFKD', title)
    slug = slug.encode('ASCII', 'ignore').decode('ASCII')
    slug = re.sub(r'[^a-zA-Z0-9]', '-', slug.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


def _clean_content(content: str) -> str:
    """Nettoie le contenu avant conversion."""
    content = content.replace('&nbsp;', ' ')
    content = content.replace('nbsp;', ' ')
    content = content.replace('\u00A0', ' ')
    content = content.replace('\u202F', ' ')
    # Corriger les URLs avec espaces
    content = re.sub(r'(https?)[\s\u00A0\u202F]*:[\s\u00A0\u202F]*//', r'\1://', content)
    content = re.sub(r'[ \t]+', ' ', content)
    return content


def _fix_math_commands(content: str) -> str:
    """Corrige les commandes mathématiques."""
    content = re.sub(r'\\text\{([^}]+)\}', r'\\mathrm{\1}', content)
    content = re.sub(r'\\mathbb\{([^}]+)\}', r'\\mathbf{\1}', content)
    content = re.sub(r'\\mod\b', r'\\bmod', content)
    return content


def _adjust_image_paths(content: str, definition) -> str:
    """Ajuste les chemins des images."""
    assets_path = str(definition.path / "assets").replace('\\', '/')

    def replace_image(match):
        filename = match.group(1)
        return rf'\includegraphics[width=0.9\linewidth]{{{assets_path}/{filename}}}'

    content = re.sub(r'!\[\]\(\./assets/([^)]+)\)', replace_image, content)
    return content


def _escape_latex(text: str) -> str:
    """Échappe les caractères spéciaux LaTeX."""
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def _markdown_to_latex(content: str, use_cartouche_h1: bool = False) -> str:
    """Convertit le markdown en LaTeX."""

    # 1. Protéger les blocs de code
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"<<<CODEBLOCK{len(code_blocks)-1}>>>"
    content = re.sub(r'```(\w*)\n(.*?)```', save_code_block, content, flags=re.DOTALL)

    # 2. Protéger le code inline
    inline_codes = []
    def save_inline_code(match):
        code = match.group(1)
        code = code.replace('\\', r'\textbackslash{}')
        code = code.replace('_', r'\_')
        code = code.replace('{', r'\{')
        code = code.replace('}', r'\}')
        code = code.replace('$', r'\$')
        code = code.replace('%', r'\%')
        code = code.replace('#', r'\#')
        code = code.replace('&', r'\&')
        code = code.replace('^', r'\textasciicircum{}')
        code = code.replace('~', r'\textasciitilde{}')
        # Tous les codes inline utilisent soul (supporte le saut de ligne)
        inline_codes.append(rf'\inlinecodelong{{{code}}}')
        return f"<<<INLINECODE{len(inline_codes)-1}>>>"
    content = re.sub(r'`([^`]+)`', save_inline_code, content)

    # 3. Protéger les formules mathématiques
    math_blocks = []
    def save_math(match):
        math_blocks.append(match.group(0))
        return f"<<<MATH{len(math_blocks)-1}>>>"
    content = re.sub(r'\$\$[^$]+\$\$', save_math, content)
    content = re.sub(r'\$[^$]+\$', save_math, content)

    # 4. Titres H1 (AVANT d'échapper les #)
    if use_cartouche_h1:
        # Titres H1 en cartouche noire style vedette
        content = re.sub(r'^# (.+)$', r'\\vspace{0.8em}\\noindent\\vedettefit{\1}\\vspace{0.4em}', content, flags=re.MULTILINE)
    else:
        content = re.sub(r'^# (.+)$', r'\\section*{\1}', content, flags=re.MULTILINE)

    # 5. Italique avec underscore
    content = re.sub(r'(?<![\\a-zA-Z0-9])_([^_\n]+)_(?![a-zA-Z0-9])', r'\\textit{\1}', content)

    # 6. Gras
    content = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', content)

    # 7. Italique avec astérisque
    content = re.sub(r'(?<![\\*])\*([^*\n]+)\*', r'\\textit{\1}', content)

    # 8. Échapper les caractères spéciaux restants
    content = content.replace('&', r'\&')
    content = content.replace('%', r'\%')
    content = content.replace('#', r'\#')
    content = re.sub(r'(?<!\\)_', r'\\_', content)

    # 9. Titres H2 et H3
    content = re.sub(r'^### (.+)$', r'\\subsubsection*{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'\\subsection*{\1}', content, flags=re.MULTILINE)

    # 9. Listes
    lines = content.split('\n')
    new_lines = []
    in_list = False
    just_ended_list = False

    for line in lines:
        stripped = line.strip()
        is_list_item = (stripped.startswith('* ') or
                        stripped.startswith('- ') or
                        re.match(r'^\d+\.\s', stripped))

        if is_list_item:
            if not in_list:
                new_lines.append(r'\begin{itemize}')
                in_list = True
            just_ended_list = False
            if stripped.startswith('* ') or stripped.startswith('- '):
                item = stripped[2:]
            else:
                item = re.sub(r'^\d+\.\s*', '', stripped)
            new_lines.append(rf'  \item {item}')
        else:
            if in_list and stripped:
                new_lines.append(r'\end{itemize}')
                in_list = False
                just_ended_list = True
            # Ajouter l'alinéa au premier paragraphe après une liste
            if just_ended_list and stripped:
                new_lines.append(r'\par\noindent\hspace{\parindent}' + stripped)
                just_ended_list = False
            else:
                new_lines.append(line)
                if not stripped:
                    just_ended_list = False

    if in_list:
        new_lines.append(r'\end{itemize}')

    content = '\n'.join(new_lines)

    # 10. Citations
    content = re.sub(
        r'^> (.+)$',
        r'\\begin{quote}\\small\1\\end{quote}',
        content,
        flags=re.MULTILINE
    )

    # 11. Liens markdown (retirer le lien, garder le texte)
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', content)

    # 12. URLs brutes - envelopper dans \textenglish pour éviter l'espace français
    content = re.sub(
        r'(https?://[^\s\)\]]+)',
        r'\\textenglish{\1}',
        content
    )

    # 13. Restaurer les formules
    for i, math in enumerate(math_blocks):
        content = content.replace(f"<<<MATH{i}>>>", math)

    # 14. Restaurer le code inline
    for i, code in enumerate(inline_codes):
        content = content.replace(f"<<<INLINECODE{i}>>>", code)

    # 15. Restaurer les blocs de code
    for i, block in enumerate(code_blocks):
        match = re.match(r'```(\w*)\n(.*?)```', block, flags=re.DOTALL)
        if match:
            code = match.group(2).strip()
            code = _format_code_block(code)
            latex_block = r'\begin{codeblock}' + '\n' + code + '\n' + r'\end{codeblock}'
            content = content.replace(f"<<<CODEBLOCK{i}>>>", latex_block)

    return content


def _format_code_block(code: str) -> str:
    """Formate un bloc de code pour le rendu LaTeX dans un tcolorbox.

    Préserve les sauts de ligne originaux du markdown,
    coupe les lignes trop longues, échappe les caractères LaTeX.
    """
    MAX_CHARS = 66

    def escape_code_char(text: str) -> str:
        text = text.replace('\\', r'\textbackslash{}')
        text = text.replace('{', r'\{')
        text = text.replace('}', r'\}')
        text = text.replace('$', r'\$')
        text = text.replace('%', r'\%')
        text = text.replace('#', r'\#')
        text = text.replace('&', r'\&')
        text = text.replace('_', r'\_')
        text = text.replace('^', r'\textasciicircum{}')
        text = text.replace('~', r'\textasciitilde{}')
        return text

    def wrap_line(line: str) -> list:
        if len(line) <= MAX_CHARS:
            return [line]
        chunks = []
        while len(line) > MAX_CHARS:
            chunks.append(line[:MAX_CHARS])
            line = line[MAX_CHARS:]
        if line:
            chunks.append(line)
        return chunks

    lines = code.split('\n')
    result_lines = []

    for line in lines:
        wrapped = wrap_line(line)
        for chunk in wrapped:
            result_lines.append(escape_code_char(chunk))

    return r'\noindent ' + (r'\\' + '\n').join(result_lines)
