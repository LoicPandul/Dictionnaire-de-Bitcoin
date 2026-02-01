#!/usr/bin/env python3
"""
Génération du PDF via XeLaTeX.
Format KDP : 5.5" x 8.5" (13.97cm x 21.59cm)
"""

import os
import subprocess
import tempfile
import re
from pathlib import Path
from datetime import datetime
import locale

from ..core.dictionary import Dictionary
from ..config import (
    BASE_DIR, TEMPLATES_DIR, OUTPUT_PDF, DEFINITIONS_DIR,
    PDF_ENGINE, AUTHOR, PROJECT_NAME, PROJECT_SUBTITLE,
    LICENSE, GITHUB_URL
)


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère le PDF du dictionnaire au format KDP."""
    if output_path is None:
        output_path = OUTPUT_PDF

    print(f"Génération du PDF: {output_path}")

    # 1. Générer le contenu LaTeX complet
    latex_content = _build_latex_content(dictionary)

    # 2. Écrire le fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', suffix='.tex', delete=False, encoding='utf-8') as f:
        f.write(latex_content)
        temp_tex = f.name

    try:
        # 3. Compiler avec XeLaTeX (2 passes pour les références)
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

            result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(output_dir))

        # Vérifier si le PDF a été généré (même si returncode != 0 à cause de warnings)
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


def _build_latex_content(dictionary: Dictionary) -> str:
    """Construit le document LaTeX complet."""
    sections = []

    # Préambule
    sections.append(_generate_preamble())

    # Début du document
    sections.append("\\begin{document}")

    # === PAGES LIMINAIRES ===
    sections.append("\\frontmatter")
    sections.append("\\pagestyle{frontmatter}")

    # 1. Faux-titre (page de droite)
    sections.append(_generate_half_title())

    # 2. Verso blanc
    sections.append("\\cleardoublepage")

    # 3. Page de titre (page de droite)
    sections.append(_generate_title_page())

    # 4. Mentions légales (page de gauche)
    sections.append(_generate_copyright_page())

    # 5. Page blanche
    sections.append("\\clearpage\\thispagestyle{frontmatter}\\null\\clearpage")

    # 6. Table des matières
    sections.append(_generate_toc(dictionary))

    # 7. Page blanche si nécessaire
    sections.append("\\cleardoublepage")

    # 8. Introduction
    sections.append(_generate_introduction())

    # 9. Contributeurs et remerciements
    sections.append(_generate_contributors())

    # === CORPS DU DICTIONNAIRE ===
    sections.append("\\mainmatter")
    sections.append("\\pagestyle{dictionary}")
    sections.append("\\setcounter{page}{1}")

    # Contenu par lettre
    for letter in dictionary.letters():
        # Page de séparation de lettre
        sections.append(_create_letter_page(letter))

        # Définitions de cette lettre
        for definition in dictionary.get_by_letter(letter):
            sections.append(_format_definition(definition))

    # === PAGES FINALES ===
    sections.append("\\backmatter")
    sections.append("\\pagestyle{frontmatter}")

    # Page blanche si nécessaire pour finir sur page paire
    sections.append("\\cleardoublepage")

    # Rappel mentions légales (page de gauche)
    sections.append(_generate_final_page())

    # Page blanche finale
    sections.append("\\clearpage\\thispagestyle{frontmatter}\\null")

    # Fin du document
    sections.append("\\end{document}")

    return "\n\n".join(sections)


def _generate_preamble() -> str:
    """Génère le préambule LaTeX."""
    return r"""% Dictionnaire de Bitcoin - Format KDP
\documentclass[9pt,twoside,openright]{book}

% Encodage et langue
\usepackage{fontspec}
\usepackage{polyglossia}
\setdefaultlanguage{french}

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
\setmonofont{Courier New}[Scale=0.85]

% Typographie
\usepackage{microtype}
\usepackage{setspace}
\setstretch{1.10}

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
\definecolor{linkcolor}{RGB}{0, 0, 0}
\definecolor{darkgray}{RGB}{80, 80, 80}

% Liens
\usepackage[
    colorlinks=true,
    linkcolor=linkcolor,
    urlcolor=linkcolor,
    pdfborder={0 0 0}
]{hyperref}

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

% Code
\usepackage{listings}
\usepackage{tcolorbox}
\tcbuselibrary{listings,breakable,skins}

\lstset{
    basicstyle=\ttfamily\scriptsize,
    backgroundcolor=\color{customgray},
    frame=none,
    breaklines=true,
    breakatwhitespace=true,
    aboveskip=0.3em,
    belowskip=0.3em,
    xleftmargin=0.8em,
    xrightmargin=0.8em
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

% Commande pour la cartouche noire de vedette
\newcommand{\vedette}[1]{%
    \noindent\colorbox{black}{%
        \parbox[c]{\dimexpr\linewidth-2\fboxsep}{%
            \centering\color{white}\fontsize{10}{12}\selectfont\bfseries\addfontfeature{LetterSpace=3.0}#1%
        }%
    }%
}

% Commande pour vedette ajustée à la largeur du texte
\newsavebox{\vedettebox}
\newcommand{\vedettefit}[1]{%
    \sbox{\vedettebox}{\fontsize{10}{12}\selectfont\bfseries\addfontfeature{LetterSpace=3.0}#1}%
    \noindent\colorbox{black}{%
        \hspace{0.4em}\color{white}\usebox{\vedettebox}\hspace{0.4em}%
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
"""


def _generate_half_title() -> str:
    """Génère la page de faux-titre."""
    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}
\begin{{center}}
{{\fontsize{{18}}{{22}}\selectfont\bfseries {PROJECT_NAME}}}
\end{{center}}
\vspace*{{\fill}}
\clearpage
"""


def _generate_title_page() -> str:
    """Génère la page de titre."""
    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}
\begin{{center}}
{{\fontsize{{22}}{{26}}\selectfont\bfseries {PROJECT_NAME}}}\\[1cm]
{{\fontsize{{11}}{{14}}\selectfont {PROJECT_SUBTITLE.upper()}}}\\[3cm]
{{\fontsize{{12}}{{16}}\selectfont\itshape {AUTHOR}}}
\end{{center}}
\vspace*{{\fill}}
\clearpage
"""


def _generate_copyright_page() -> str:
    """Génère la page de mentions légales."""
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    except:
        try:
            locale.setlocale(locale.LC_TIME, 'fr_FR')
        except:
            pass

    date_str = datetime.now().strftime('%d %B %Y')
    year = datetime.now().year

    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}

\small
\noindent\textbf{{© {year} {AUTHOR}}}\\[0.4em]
\noindent\textit{{{PROJECT_NAME} : {PROJECT_SUBTITLE}}}\\[0.8em]
\noindent Version du {date_str}\\[0.4em]
\noindent\url{{{GITHUB_URL}}}\\[0.8em]
\noindent Cet ouvrage est sous licence {LICENSE}\\[0.4em]
\noindent\url{{https://creativecommons.org/licenses/by-nc-sa/4.0/}}\\[1em]
\noindent Lightning: pandul@sats.rs\\[0.2em]
\noindent Email: loic@pandul.fr\\[0.2em]
\noindent Site web: https://pandul.fr/\\[0.2em]
\noindent GitHub: https://github.com/LoicPandul/\\[1.5em]
\noindent ISBN: \underline{{\hspace{{5cm}}}}

\clearpage
"""


def _generate_toc(dictionary: Dictionary) -> str:
    """Génère la table des matières sur deux colonnes avec liens cliquables."""
    toc_parts = []

    toc_parts.append(r"""
\clearpage
\thispagestyle{toc}
\begin{center}
{\fontsize{14}{18}\selectfont\bfseries TABLE DES MATIÈRES}
\end{center}
\vspace{0.8cm}
""")

    for letter in dictionary.letters():
        definitions = dictionary.get_by_letter(letter)

        toc_parts.append(rf"\noindent{{\bfseries {letter}}}")
        toc_parts.append(r"\begin{multicols}{2}")
        toc_parts.append(r"\scriptsize")

        for defn in definitions:
            # Créer un slug pour l'ancre
            slug = _make_slug(defn.title)
            safe_title = _escape_latex(defn.title)
            # Lien cliquable vers la définition
            toc_parts.append(rf"\noindent\hyperlink{{{slug}}}{{{safe_title}}}\\")

        toc_parts.append(r"\end{multicols}")
        toc_parts.append(r"\vspace{0.3em}")

    return "\n".join(toc_parts)


def _generate_introduction() -> str:
    """Génère la page d'introduction."""
    intro_path = TEMPLATES_DIR / "introduction.md"
    if intro_path.exists():
        content = intro_path.read_text(encoding='utf-8')
        content = _clean_content(content)
        content = _markdown_to_latex(content)
    else:
        content = ""

    return rf"""
\cleardoublepage
\thispagestyle{{frontmatter}}
\begin{{center}}
{{\fontsize{{14}}{{18}}\selectfont\bfseries INTRODUCTION}}
\end{{center}}
\vspace{{0.8cm}}

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
\cleardoublepage
\thispagestyle{{frontmatter}}
\begin{{center}}
{{\fontsize{{14}}{{18}}\selectfont\bfseries CONTRIBUTEURS ET REMERCIEMENTS}}
\end{{center}}
\vspace{{0.8cm}}

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

    # Créer l'ancre pour le lien depuis la TDM
    slug = _make_slug(definition.title)
    title = definition.title
    safe_title = _escape_latex(title)

    # Marquage pour les en-têtes
    parts.append(rf"\markboth{{{safe_title}}}{{{safe_title}}}")

    # Ancre hypertexte
    parts.append(rf"\hypertarget{{{slug}}}{{}}")

    # Vedette (cartouche noire)
    parts.append(rf"\vedettefit{{{safe_title}}}")
    parts.append(r"\vspace{0.3em}")
    parts.append("")

    # Ligne de métadonnées : Catégorie · Drapeau Traduction
    metadata_parts = []

    if definition.category:
        # Catégorie avec majuscule au début, minuscules ensuite
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
        parts.append(r"\vspace{0.3em}")
        parts.append("")

    # Contenu
    content = definition.content
    content = _clean_content(content)
    content = _fix_math_commands(content)
    content = _adjust_image_paths(content, definition)
    content = _markdown_to_latex(content)
    parts.append(content)

    # Espacement entre définitions
    parts.append(r"\vspace{0.8em}")

    return "\n".join(parts)


def _generate_final_page() -> str:
    """Génère la page finale avec rappel des mentions."""
    year = datetime.now().year

    return rf"""
\clearpage
\thispagestyle{{frontmatter}}
\vspace*{{\fill}}

\begin{{center}}
\small
{{\bfseries {PROJECT_NAME}}}\\[0.4em]
{{\itshape {PROJECT_SUBTITLE}}}\\[1.5em]
© {year} {AUTHOR}\\[0.8em]
\url{{{GITHUB_URL}}}\\[0.8em]
Licence {LICENSE}\\[1.5em]
Lightning: pandul@sats.rs\\[0.2em]
Site web: https://pandul.fr/
\end{{center}}

\vspace*{{\fill}}
\clearpage
"""


def _make_slug(title: str) -> str:
    """Crée un slug pour les ancres hypertexte."""
    import unicodedata
    # Normaliser et retirer les accents
    slug = unicodedata.normalize('NFKD', title)
    slug = slug.encode('ASCII', 'ignore').decode('ASCII')
    # Remplacer les espaces et caractères spéciaux
    slug = re.sub(r'[^a-zA-Z0-9]', '-', slug.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug


def _clean_content(content: str) -> str:
    """Nettoie le contenu avant conversion."""
    # Supprimer les &nbsp; et les remplacer par des espaces normaux
    content = content.replace('&nbsp;', ' ')
    content = content.replace('nbsp;', ' ')
    # Remplacer les espaces insécables Unicode par des espaces normaux
    content = content.replace('\u00A0', ' ')  # NO-BREAK SPACE
    content = content.replace('\u202F', ' ')  # NARROW NO-BREAK SPACE
    # Corriger les URLs avec espaces (typographie française)
    # Pattern plus robuste pour capturer tous types d'espaces
    content = re.sub(r'(https?)[\s\u00A0\u202F]*:[\s\u00A0\u202F]*//', r'\1://', content)
    # Supprimer les espaces multiples
    content = re.sub(r'[ \t]+', ' ', content)
    return content


def _fix_math_commands(content: str) -> str:
    """Corrige les commandes mathématiques pour la compatibilité."""
    content = re.sub(r'\\text\{([^}]+)\}', r'\\mathrm{\1}', content)
    content = re.sub(r'\\mathbb\{([^}]+)\}', r'\\mathbf{\1}', content)
    content = re.sub(r'\\mod\b', r'\\bmod', content)
    return content


def _adjust_image_paths(content: str, definition) -> str:
    """Ajuste les chemins des images pour le PDF."""
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


def _markdown_to_latex(content: str) -> str:
    """Convertit le markdown basique en LaTeX."""

    # 1. Protéger les blocs de code (fenced)
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
        inline_codes.append(rf'\texttt{{{code}}}')
        return f"<<<INLINECODE{len(inline_codes)-1}>>>"
    content = re.sub(r'`([^`]+)`', save_inline_code, content)

    # 3. Protéger les formules mathématiques
    math_blocks = []
    def save_math(match):
        math_blocks.append(match.group(0))
        return f"<<<MATH{len(math_blocks)-1}>>>"
    content = re.sub(r'\$\$[^$]+\$\$', save_math, content)
    content = re.sub(r'\$[^$]+\$', save_math, content)

    # 4. Traiter l'italique avec underscore AVANT d'échapper les underscores
    # _texte_ -> \textit{texte}
    content = re.sub(r'(?<![\\a-zA-Z0-9])_([^_\n]+)_(?![a-zA-Z0-9])', r'\\textit{\1}', content)

    # 5. Gras (double astérisque)
    content = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', content)

    # 6. Italique (simple astérisque)
    content = re.sub(r'(?<![\\*])\*([^*\n]+)\*', r'\\textit{\1}', content)

    # 7. Maintenant échapper les caractères spéciaux restants
    content = content.replace('&', r'\&')
    content = content.replace('%', r'\%')
    content = content.replace('#', r'\#')
    # Underscore - échapper tous ceux qui ne sont pas déjà échappés
    content = re.sub(r'(?<!\\)_', r'\\_', content)

    # 8. Titres
    content = re.sub(r'^### (.+)$', r'\\subsubsection*{\1}', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'\\subsection*{\1}', content, flags=re.MULTILINE)

    # 9. Listes - détection plus robuste
    lines = content.split('\n')
    new_lines = []
    in_list = False

    for line in lines:
        stripped = line.strip()
        # Détecter les éléments de liste (*, -, ou numérotés)
        is_list_item = (stripped.startswith('* ') or
                        stripped.startswith('- ') or
                        re.match(r'^\d+\.\s', stripped))

        if is_list_item:
            if not in_list:
                new_lines.append(r'\begin{itemize}')
                in_list = True
            # Extraire le contenu après le marqueur
            if stripped.startswith('* ') or stripped.startswith('- '):
                item = stripped[2:]
            else:
                item = re.sub(r'^\d+\.\s*', '', stripped)
            new_lines.append(rf'  \item {item}')
        else:
            if in_list and stripped:  # Fermer la liste si ligne non vide
                new_lines.append(r'\end{itemize}')
                in_list = False
            elif in_list and not stripped:  # Ligne vide dans une liste
                pass  # Garder la liste ouverte
            new_lines.append(line)

    if in_list:
        new_lines.append(r'\end{itemize}')

    content = '\n'.join(new_lines)

    # 10. Blocs de citation
    content = re.sub(
        r'^> (.+)$',
        r'\\begin{quote}\\small\1\\end{quote}',
        content,
        flags=re.MULTILINE
    )

    # 11. Liens (retirer le lien, garder le texte)
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', content)

    # 12. Restaurer les formules mathématiques
    for i, math in enumerate(math_blocks):
        content = content.replace(f"<<<MATH{i}>>>", math)

    # 13. Restaurer le code inline
    for i, code in enumerate(inline_codes):
        content = content.replace(f"<<<INLINECODE{i}>>>", code)

    # 14. Restaurer et convertir les blocs de code
    for i, block in enumerate(code_blocks):
        match = re.match(r'```(\w*)\n(.*?)```', block, flags=re.DOTALL)
        if match:
            code = match.group(2).strip()
            code = code.replace('\\', r'\textbackslash{}')
            code = code.replace('_', r'\_')
            code = code.replace('{', r'\{')
            code = code.replace('}', r'\}')
            code = code.replace('$', r'\$')
            code = code.replace('%', r'\%')
            code = code.replace('#', r'\#')
            code = code.replace('&', r'\&')
            latex_block = rf'\begin{{lstlisting}}' + '\n' + code + '\n' + rf'\end{{lstlisting}}'
            content = content.replace(f"<<<CODEBLOCK{i}>>>", latex_block)

    return content
