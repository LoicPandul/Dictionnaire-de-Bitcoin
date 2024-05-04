import os
import re

def ajuster_liens_et_images(contenu):
    """ Ajuste les liens internes et les chemins des images. """
    contenu = re.sub(r'\[([^\]]+)\]\(\.\/(?:.*?)\.md#(.*?)\)', r'[\1](#\2)', contenu)
    contenu = re.sub(r'\!\[\]\((assets\/.*?)\)', r'![](../../dictionnaire/\1)', contenu)
    return contenu

def markdown_to_latex_lists(contenu):
    """ Convertit les listes Markdown en listes LaTeX. """
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

def creer_page_titre(lettre):
    """ Crée une page de titre pour chaque lettre. """
    return f"""
\\newpage
\\thispagestyle{{empty}}
\\vspace*{{\\fill}}
\\begin{{center}}
{{\\fontfamily{{cmr}}\\selectfont \\fontsize{{105}}{{115}}\\selectfont\\textbf{{{lettre}}}}}
\\end{{center}}
\\vspace*{{\\fill}}
\\newpage
"""

def generer_tableau_index_par_lettre(lettre, titres):
    """ Génère un index en tableau à quatre colonnes avec une première ligne vide. """
    index = "\n| | | | |\n|:---------------------------|:--|:---------------------------|:--|\n"
    
    # Séparer les titres des numéros de page
    titres_separes = [titre.rsplit(' ', 1) for titre in titres]
    
    # Organiser en deux colonnes de titres avec leurs numéros respectifs
    mi_point = (len(titres_separes) + 1) // 2
    colonne_1 = titres_separes[:mi_point]
    colonne_2 = titres_separes[mi_point:]
    
    # Compléter avec des cases vides si nécessaire
    while len(colonne_1) < len(colonne_2):
        colonne_1.append(("", ""))
    while len(colonne_2) < len(colonne_1):
        colonne_2.append(("", ""))

    # Ajouter les lignes au tableau
    for (titre_1, page_1), (titre_2, page_2) in zip(colonne_1, colonne_2):
        index += f"| {titre_1:<30} | {page_1:>5} | {titre_2:<30} | {page_2:>5} |\n"
    
    return index

def ajouter_numeros_page(titre, page_num):
    """ Crée une ancre correcte et associe le numéro de page. """
    anchor = titre.lower().replace(' ', '-').replace('.', '.')
    anchor = re.sub(r'[«»|]', ' ', anchor)
    anchor = re.sub(r'\s+', '-', anchor.strip())
    anchor = re.sub(r'--+', '-', anchor)
    anchor = re.sub(r'[^\w.-]', '', anchor)
    return f"[{titre}](#{anchor}) {page_num}"

chemin_dossier_dictionnaire = '../dictionnaire'
chemin_markdown_final = 'PDF/dictionnaire_MD_for_PDF.md'

os.makedirs(os.path.dirname(chemin_markdown_final), exist_ok=True)

# Dictionnaire contenant les titres organisés par lettre
titres_par_lettre = {}

for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
    if fichier_lettre.endswith(".md"):
        lettre = fichier_lettre.upper().replace('.MD', '')[0]
        titres_par_lettre.setdefault(lettre, [])
        with open(os.path.join(chemin_dossier_dictionnaire, fichier_lettre), 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            titres = re.findall(r'^##\s*(.*)$', contenu, flags=re.MULTILINE)
            for page_num, titre in enumerate(titres, start=1):
                titre_avec_page = ajouter_numeros_page(titre, page_num)
                titres_par_lettre[lettre].append(titre_avec_page)

# Écrire la table des matières organisée par lettre
with open(chemin_markdown_final, 'w', encoding='utf-8') as fichier_complet:
    fichier_complet.write("# Table des matières\n\n")
    for lettre, titres in sorted(titres_par_lettre.items()):
        fichier_complet.write(f"## {lettre}\n")
        fichier_complet.write(generer_tableau_index_par_lettre(lettre, titres) + "\n")

    for lettre, titres in sorted(titres_par_lettre.items()):
        page_titre = creer_page_titre(lettre)
        fichier_complet.write(page_titre)
        
        chemin_complet = os.path.join(chemin_dossier_dictionnaire, f"{lettre.lower()}.md")
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            contenu = ajuster_liens_et_images(contenu)
            contenu = markdown_to_latex_lists(contenu)
            fichier_complet.write(contenu + '\n\n')

print(f'Le fichier Markdown a été créé avec succès : {chemin_markdown_final}')
