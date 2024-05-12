import os
import re
import fitz  # PyMuPDF
import unicodedata
import datetime
import locale
import requests


# Paths and constants
pdf_path = '../Dictionnaire de Bitcoin.pdf'
chemin_dossier_dictionnaire = '../dictionnaire'
chemin_markdown_final = 'PDF/dictionnaire_MD_for_PDF.md'

def read_contributor_paragraph():
    with open('PDF/contributeurs_paragraphe.md', 'r', encoding='utf-8') as file:
        return file.read()

# Normalize titles by removing special characters and accents
def normalize_title(title):
    # Remove accents
    nfkd_form = unicodedata.normalize('NFKD', title)
    title_no_accent = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    # Remove non-alphanumeric characters
    title_cleaned = re.sub(r'[^a-zA-Z0-9]', '', title_no_accent)
    return title_cleaned.strip().lower()

# Function to adjust links and images
def ajuster_liens_et_images(contenu):
    contenu = re.sub(r'\[([^\]]+)\]\(\.\/(?:.*?)\.md#(.*?)\)', r'[\1](#\2)', contenu)
    contenu = re.sub(r'\!\[\]\((assets\/.*?)\)', r'![](../../dictionnaire/\1)', contenu)
    return contenu

# Function to convert markdown lists to LaTeX lists
def markdown_to_latex_lists(contenu):
    lines = contenu.split('\n')
    new_content = []
    in_list = False
    for line in lines:
        if line.strip().startswith('* '):
            if not in_list:
                new_content.append('\\begin{itemize}')
                in_list = True
            if '`' in line:
                parts = line.split('`')
                new_content.append(f'  \\item {parts[0].strip().lstrip("* ")}')
                for i in range(1, len(parts), 2):
                    new_content.append(f'\\texttt{{{parts[i]}}}')
                    if i + 1 < len(parts):
                        new_content.append(parts[i + 1].strip())
            else:
                new_content.append(f'  \\item {line.strip().lstrip("* ")}')
        else:
            if in_list:
                new_content.append('\\end{itemize}')
                in_list = False
            new_content.append(line)
    if in_list:
        new_content.append('\\end{itemize}')
    return '\n'.join(new_content)

# Create a new title page for each letter
def creer_page_titre(lettre):
    return f"""
\\newpage
\\thispagestyle{{empty}}
\\fancyhead[C]{{\\textbf{{\\textit{{{lettre}}}}}}}
\\vspace*{{\\fill}}
\\begin{{center}}
\\fontsize{{80}}{{95}}\\selectfont\\textbf{{{lettre}}}
\\end{{center}}
\\vspace*{{\\fill}}
\\newpage
"""

# Create an index table by letter
def generer_tableau_index_par_lettre(lettre, titres):
    index = f"\n\\section*{{{lettre}}}\n| | | | |\n|:---------------------------|--:|:---------------------------|--:|\n"
    titres_separes = [titre.rsplit(' ', 1) for titre in titres]
    mi_point = (len(titres_separes) + 1) // 2
    colonne_1 = titres_separes[:mi_point]
    colonne_2 = titres_separes[mi_point:]

    while len(colonne_1) < len(colonne_2):
        colonne_1.append(("", ""))
    while len(colonne_2) < len(colonne_1):
        colonne_2.append(("", ""))

    index += "| | | | |\n"
    for (titre_1, page_1), (titre_2, page_2) in zip(colonne_1, colonne_2):
        index += f"| {titre_1:<30} | {page_1:>5} | {titre_2:<30} | {page_2:>5} |\n"
    index += "| | | | |\n"

    return index

# Create an anchor for each title
def ajouter_numeros_page(titre, page_num):
    anchor = titre.lower().replace(' ', '-').replace('.', '.')
    anchor = re.sub(r'[«»|]', ' ', anchor)
    anchor = re.sub(r'\s+', '-', anchor.strip())
    anchor = re.sub(r'--+', '-', anchor)
    anchor = re.sub(r'[^\w.-]', '', anchor)
    return f"[{titre}](#{anchor}) {page_num}"

# Extract page numbers for definitions
def extraire_pages_definitions(pdf_path):
    doc = fitz.open(pdf_path)
    page_mapping = {}
    definition_regex = r'^[A-ZÀÉÈÊËÔÇÏA-Z0-9 /()\'’_.\-+?]+$'



    # Locate pages where the grand letter appears
    grand_letters = {}
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        texte_page = page.get_text("text").strip()
        if len(texte_page) == 1 and texte_page.isalpha():
            grand_letters[texte_page.upper()] = page_num + 1

    # Extract definition titles and their respective pages
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        texte_page = page.get_text("text").strip().splitlines()

        for line in texte_page:
            normalized_line = normalize_title(line)
            if re.match(definition_regex, line) and normalized_line:
                page_mapping[normalized_line] = page_num + 1

    return page_mapping

# Extract page numbers for definitions from the PDF
pages_definitions = extraire_pages_definitions(pdf_path)

# Organize titles by letter
titres_par_lettre = {}

for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
    if fichier_lettre.endswith(".md"):
        lettre = fichier_lettre.upper().replace('.MD', '')[0]
        titres_par_lettre.setdefault(lettre, [])
        with open(os.path.join(chemin_dossier_dictionnaire, fichier_lettre), 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            titres = re.findall(r'^##\s*(.*)$', contenu, flags=re.MULTILINE)
            for titre in titres:
                normalized_titre = normalize_title(titre)
                page_num = pages_definitions.get(normalized_titre, '?')
                titre_avec_page = ajouter_numeros_page(titre, page_num)
                titres_par_lettre[lettre].append(titre_avec_page)

# Generate the final Markdown file
os.makedirs(os.path.dirname(chemin_markdown_final), exist_ok=True)

# Définir la locale à Français
locale.setlocale(locale.LC_TIME, 'fr_FR')

# Define the current date
date_aujourdhui = datetime.datetime.now().strftime('%d %B %Y')

# Generate the final Markdown file
os.makedirs(os.path.dirname(chemin_markdown_final), exist_ok=True)

with open(chemin_markdown_final, 'w', encoding='utf-8') as fichier_complet:
    fichier_complet.write("""---
header-includes:
  - \\usepackage{fancyhdr}
  - \\usepackage{colortbl}
  - \\usepackage{pdfpages}
  - \\pagestyle{fancy}
  - \\fancyfoot[C]{\\thepage}
  - \\renewcommand{\\headrulewidth}{0pt}
  - \\renewcommand{\\footrulewidth}{0pt}
  - \\arrayrulecolor{white}
---
""")

    fichier_complet.write("\\clearpage\n")
    fichier_complet.write("\\pagecolor{black}\n")
    fichier_complet.write("""\\includepdf{cover_front.png}\n""")
    fichier_complet.write("\\nopagecolor\n")

    # Add a custom page before the table of contents
    # Début de la nouvelle page et préparation pour le texte en bas
    fichier_complet.write("\\newpage\n\\thispagestyle{empty}\n")
    fichier_complet.write("\\begin{minipage}[b][\\textheight][b]{\\textwidth}\n")  # Démarre une minipage en bas de la page
    fichier_complet.write("\\textbf{© 2024 Loïc Morel}\\newline\n")
    fichier_complet.write("\\textbf{\\textit{Dictionnaire de Bitcoin : Tout le vocabulaire technique de Bitcoin}}\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("Version du " + date_aujourdhui + "\\newline\n")
    fichier_complet.write("https://github.com/LoicPandul/Dictionnaire-de-Bitcoin\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("Cet ouvrage est sous licence CC BY-NC-SA 4.0\\newline\n")
    fichier_complet.write("https://creativecommons.org/licenses/by-nc-sa/4.0/\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("Email : loic@pandul.fr\\newline\n")  
    fichier_complet.write("Site web : https://www.pandul.fr/\\newline\n")  
    fichier_complet.write("GitHub : https://github.com/LoicPandul/\\newline\n")
    fichier_complet.write("\\end{minipage}\n")
    fichier_complet.write("\\newpage\n\n")

    # Début de la nouvelle page pour "Dictionnaire de Bitcoin" avec minipage
    fichier_complet.write("\\newpage\n\\thispagestyle{empty}\n")
    fichier_complet.write("\\begin{minipage}[c][\\textheight]{\\textwidth}\n")
    fichier_complet.write("\\vspace*{\\fill}\n")
    fichier_complet.write("\\centering\n")  # Assure que le texte est centré horizontalement
    # Augmenter la taille du titre principal avec un facteur d'échelle
    fichier_complet.write("{\\fontsize{40}{50} \\selectfont \\textbf{Dictionnaire de Bitcoin}}\\newline\n")  # 1.5 fois plus gros que \\Huge
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("{\\fontsize{15}{25} \\selectfont{TOUT LE VOCABULAIRE TECHNIQUE DE BITCOIN}}\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n")
    fichier_complet.write("\\newline\n") 
    fichier_complet.write("\\newline\n")
    fichier_complet.write("{\\Large \\textbf{\\textit{Loïc Morel}}}\n")  # Italic et gras pour le nom
    fichier_complet.write("\\vspace*{\\fill}\n")
    fichier_complet.write("\\end{minipage}\n")
    fichier_complet.write("\\newpage\n\n")

    # Récupérer le paragraphe
    contributor_paragraph = read_contributor_paragraph()
    formatted_paragraph = markdown_to_latex_lists(contributor_paragraph)


    # Commencer une nouvelle page et écrire la section Contributeurs
    fichier_complet.write("\\newpage\n\\thispagestyle{empty}\n")
    fichier_complet.write("\\begin{center}\n\\Huge \\textbf{CONTRIBUTEURS}\n\\end{center}\n")
    fichier_complet.write("\\vspace*{1cm}\n")

    # Écrire le paragraphe des contributeurs
    fichier_complet.write(formatted_paragraph + "\\newline\n")


    fichier_complet.write("\\newpage\n\\thispagestyle{empty}\n")
    fichier_complet.write("\\begin{center}\n")
    fichier_complet.write("\\Huge \\textbf{TABLE DES MATIÈRES}\n")
    fichier_complet.write("\\end{center}\n")
    fichier_complet.write("\\vspace*{0.5cm}\n")

    # Create the index in alphabetical order
    for lettre, titres in sorted(titres_par_lettre.items()):
        fichier_complet.write(generer_tableau_index_par_lettre(lettre, titres) + "\n")

    # Switch back to black lines for the body of the definitions
    fichier_complet.write("\\arrayrulecolor{black}\n")

    # Add the detailed content sections for each letter
    for lettre, titres in sorted(titres_par_lettre.items()):
        page_titre = creer_page_titre(lettre)
        fichier_complet.write(page_titre)

        chemin_complet = os.path.join(chemin_dossier_dictionnaire, f"{lettre.lower()}.md")
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            contenu = ajuster_liens_et_images(contenu)
            contenu = markdown_to_latex_lists(contenu)
            fichier_complet.write(contenu + '\n\n')

    fichier_complet.write("\\clearpage\n")
    fichier_complet.write("\\pagecolor{black}\n")
    fichier_complet.write("""\\includepdf{cover_back.png}\n""")
    fichier_complet.write("\\nopagecolor\n")

print(f'Le fichier Markdown a été créé avec succès : {chemin_markdown_final}')
