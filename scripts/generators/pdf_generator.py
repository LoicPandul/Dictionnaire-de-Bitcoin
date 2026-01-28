#!/usr/bin/env python3
"""
Génération du PDF via Pandoc + XeLaTeX.
"""

import os
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import locale

from ..core.dictionary import Dictionary
from ..config import (
    BASE_DIR, TEMPLATES_DIR, OUTPUT_PDF, DEFINITIONS_DIR,
    PDF_ENGINE, PDF_FONT, PDF_MARGIN, AUTHOR, PROJECT_NAME, PROJECT_SUBTITLE,
    LICENSE, GITHUB_URL
)


def generate(dictionary: Dictionary, output_path: Path = None):
    """Génère le PDF du dictionnaire."""
    if output_path is None:
        output_path = OUTPUT_PDF

    print(f"Génération du PDF: {output_path}")

    # 1. Générer le markdown intermédiaire
    md_content = _build_markdown_for_pdf(dictionary)

    # 2. Écrire le fichier temporaire
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_content)
        temp_md = f.name

    try:
        # 3. Appeler Pandoc avec le template LaTeX
        template_path = TEMPLATES_DIR / "pdf" / "template.tex"

        cmd = [
            "pandoc",
            temp_md,
            f"--pdf-engine={PDF_ENGINE}",
            "-V", f"geometry:top={PDF_MARGIN}",
            "-V", f"geometry:bottom={PDF_MARGIN}",
            "-V", f"geometry:left={PDF_MARGIN}",
            "-V", f"geometry:right={PDF_MARGIN}",
            "-V", f"mainfont={PDF_FONT}",
            f"--pdf-engine-opt=-shell-escape",
            "-o", str(output_path)
        ]

        # Ajouter le template s'il existe
        if template_path.exists():
            cmd.insert(2, f"--template={template_path}")

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"[ERROR] Pandoc failed: {result.stderr}")
            return False

        print(f"[OK] PDF généré: {output_path}")
        return True

    finally:
        # Nettoyer le fichier temporaire
        os.unlink(temp_md)


def _build_markdown_for_pdf(dictionary: Dictionary) -> str:
    """Construit le markdown formaté pour le PDF."""
    sections = []

    # En-tête YAML pour Pandoc
    sections.append(_generate_yaml_header())

    # Page de copyright
    sections.append(_generate_copyright_page())

    # Page de titre
    sections.append(_generate_title_page())

    # Page des contributeurs
    contributors_content = _load_contributors()
    if contributors_content:
        sections.append(_generate_contributors_page(contributors_content))

    # Table des matières
    sections.append(_generate_toc(dictionary))

    # Contenu par lettre
    for letter in dictionary.letters():
        # Page de titre de lettre
        sections.append(_create_letter_page(letter))

        # Définitions de cette lettre
        for definition in dictionary.get_by_letter(letter):
            md = definition.to_markdown(format_type="full")
            # Ajuster les chemins d'images
            md = _adjust_image_paths(md, definition)
            # Convertir les listes markdown en LaTeX
            md = _markdown_to_latex_lists(md)
            # Convertir les blocs de code
            md = _markdown_to_latex_code_blocks(md)
            sections.append(md)

    return "\n\n".join(sections)


def _generate_yaml_header() -> str:
    """Génère l'en-tête YAML pour Pandoc."""
    return """---
header-includes:
  - \\usepackage{fancyhdr}
  - \\usepackage{colortbl}
  - \\usepackage{listings}
  - \\usepackage{tcolorbox}
  - \\usepackage{fontspec}
  - \\definecolor{customgray}{RGB}{246, 248, 250}
  - \\lstdefinelanguage{text}{
      basicstyle=\\ttfamily\\small,
      morekeywords={}
    }
  - \\lstdefinelanguage{plaintext}{
      basicstyle=\\ttfamily\\small,
      morekeywords={}
    }
  - \\lstset{
      backgroundcolor=\\color{customgray},
      frame=none,
      basicstyle=\\ttfamily\\small,
      aboveskip=0.5em,
      belowskip=0.5em
    }
  - \\tcbuselibrary{listingsutf8}
  - \\tcbset{listing engine=listings}
  - \\newtcblisting{codeblock}{
      colback=customgray,
      colframe=white,
      listing only,
      listing options={basicstyle=\\ttfamily\\small},
      left=1em,
      right=1em
    }
  - \\pagestyle{fancy}
  - \\fancyfoot[C]{\\thepage}
  - \\renewcommand{\\headrulewidth}{0pt}
  - \\renewcommand{\\footrulewidth}{0pt}
  - \\arrayrulecolor{white}
---
"""


def _generate_copyright_page() -> str:
    """Génère la page de copyright."""
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    except:
        try:
            locale.setlocale(locale.LC_TIME, 'fr_FR')
        except:
            pass

    date_str = datetime.now().strftime('%d %B %Y')
    year = datetime.now().year

    return f"""\\newpage
\\thispagestyle{{empty}}
\\begin{{minipage}}[b][\\textheight][b]{{\\textwidth}}
\\textbf{{© {year} {AUTHOR}}}\\newline
\\textbf{{\\textit{{{PROJECT_NAME} : {PROJECT_SUBTITLE}}}}}\\newline
\\newline
Version du {date_str}\\newline
{GITHUB_URL}\\newline
\\newline
Cet ouvrage est sous licence {LICENSE}\\newline
https://creativecommons.org/licenses/by-nc-sa/4.0/\\newline
\\newline
Lightning : pandul@sats.rs\\newline
Email : loic@pandul.fr\\newline
Site web : https://www.pandul.fr/\\newline
GitHub : https://github.com/LoicPandul/\\newline
\\end{{minipage}}
\\newpage
"""


def _generate_title_page() -> str:
    """Génère la page de titre."""
    return f"""\\newpage
\\thispagestyle{{empty}}
\\begin{{minipage}}[c][\\textheight]{{\\textwidth}}
\\vspace*{{\\fill}}
\\centering
{{\\fontsize{{40}}{{50}} \\selectfont \\textbf{{{PROJECT_NAME}}}}}\\newline
\\newline
\\newline
\\newline
{{\\fontsize{{15}}{{25}} \\selectfont{{{PROJECT_SUBTITLE.upper()}}}}}\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
\\newline
{{\\Large \\textbf{{\\textit{{{AUTHOR}}}}}}}
\\vspace*{{\\fill}}
\\end{{minipage}}
\\newpage
"""


def _load_contributors() -> str:
    """Charge le fichier des contributeurs."""
    contributors_path = TEMPLATES_DIR / "contributors.md"
    if contributors_path.exists():
        return contributors_path.read_text(encoding='utf-8')
    return ""


def _generate_contributors_page(content: str) -> str:
    """Génère la page des contributeurs."""
    formatted = _markdown_to_latex_lists(content)
    return f"""\\newpage
\\thispagestyle{{empty}}
\\begin{{center}}
\\Huge \\textbf{{CONTRIBUTEURS}}
\\end{{center}}
\\vspace*{{1cm}}
{formatted}\\newline
"""


def _generate_toc(dictionary: Dictionary) -> str:
    """Génère la table des matières."""
    toc = """\\newpage
\\thispagestyle{empty}
\\begin{center}
\\Huge \\textbf{TABLE DES MATIÈRES}
\\end{center}
\\vspace*{0.5cm}
"""

    for letter in dictionary.letters():
        definitions = dictionary.get_by_letter(letter)
        titles = [d.title for d in definitions]

        toc += f"\n\\section*{{{letter}}}\n"
        toc += "| | |\n|:---------------------------|:---------------------------|\n"

        # Diviser en deux colonnes
        mid = (len(titles) + 1) // 2
        col1 = titles[:mid]
        col2 = titles[mid:]

        while len(col1) < len(col2):
            col1.append("")
        while len(col2) < len(col1):
            col2.append("")

        toc += "| | |\n"
        for t1, t2 in zip(col1, col2):
            toc += f"| {t1:<30} | {t2:<30} |\n"
        toc += "| | |\n"

    toc += "\\arrayrulecolor{black}\n"
    return toc


def _create_letter_page(letter: str) -> str:
    """Crée une page de séparation pour chaque lettre."""
    return f"""
\\newpage
\\thispagestyle{{empty}}
\\fancyhead[C]{{\\textbf{{\\textit{{{letter}}}}}}}
\\vspace*{{\\fill}}
\\begin{{center}}
\\fontsize{{80}}{{95}}\\selectfont\\textbf{{{letter}}}
\\end{{center}}
\\vspace*{{\\fill}}
\\newpage
"""


def _adjust_image_paths(content: str, definition) -> str:
    """Ajuste les chemins des images pour le PDF."""
    import re
    # Construire le chemin absolu vers les assets
    assets_path = definition.path / "assets"
    # Remplacer les chemins relatifs par des chemins absolus
    content = re.sub(
        r'!\[\]\(\./assets/([^)]+)\)',
        f'![]({assets_path}/\\1)',
        content
    )
    return content


def _markdown_to_latex_lists(content: str) -> str:
    """Convertit les listes markdown en listes LaTeX."""
    lines = content.split('\n')
    new_content = []
    in_list = False

    for line in lines:
        if line.strip().startswith('* '):
            if not in_list:
                new_content.append('\\begin{itemize}')
                in_list = True
            item_content = line.strip()[2:]  # Enlever "* "
            # Gérer le code inline
            if '`' in item_content:
                parts = item_content.split('`')
                result = parts[0]
                for i in range(1, len(parts), 2):
                    if i < len(parts):
                        result += f'\\texttt{{{parts[i]}}}'
                        if i + 1 < len(parts):
                            result += parts[i + 1]
                item_content = result
            new_content.append(f'  \\item {item_content}')
        else:
            if in_list:
                new_content.append('\\end{itemize}')
                in_list = False
            new_content.append(line)

    if in_list:
        new_content.append('\\end{itemize}')

    return '\n'.join(new_content)


def _markdown_to_latex_code_blocks(content: str) -> str:
    """Convertit les blocs de code markdown en blocs LaTeX."""
    import re

    def replacer(match):
        code = match.group(2).strip()
        return f'\\begin{{codeblock}}\n{code}\n\\end{{codeblock}}'

    return re.sub(r'```(.*?)\n(.*?)```', replacer, content, flags=re.DOTALL)
