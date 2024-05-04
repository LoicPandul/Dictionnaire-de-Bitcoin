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
{{\\fontfamily{{cmr}}\\selectfont \\fontsize{{95}}{{105}}\\selectfont\\textbf{{{lettre}}}}}
\\end{{center}}
\\vspace*{{\\fill}}
\\newpage
"""

def generer_tableau_index_par_lettre(lettre, titres):
    """ Génère un index en tableau à deux colonnes verticales avec alignement. """
    index = "\n| | |\n|---|---|\n"
    
    # Réduire la taille de la police des titres
    titres = [f"\\small {titre}" for titre in titres]

    # Organiser les titres en deux colonnes verticales
    mi_point = (len(titres) + 1) // 2
    colonne_1 = titres[:mi_point]
    colonne_2 = titres[mi_point:]

    # Compléter avec des cases vides si nécessaire
    while len(colonne_1) < len(colonne_2):
        colonne_1.append("")
    while len(colonne_2) < len(colonne_1):
        colonne_2.append("")

    # Ajouter les lignes au tableau
    for titre_1, titre_2 in zip(colonne_1, colonne_2):
        index += f"| {titre_1} | {titre_2} |\n"
    
    return index

def ajouter_numeros_page(titre, page_num):
    """ Ajoute le numéro de page avec une ligne de points entre le titre et le numéro. """
    points = '.' * (50 - len(titre))
    return f"{titre} {points} {page_num}"

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
                anchor = titre.lower().replace(' ', '-').replace('.', '.')
                anchor = re.sub(r'[«»|]', ' ', anchor)
                anchor = re.sub(r'\s+', '-', anchor.strip())
                anchor = re.sub(r'--+', '-', anchor)
                anchor = re.sub(r'[^\w.-]', '', anchor)
                titre_avec_page = ajouter_numeros_page(f"[{titre}](#{anchor})", page_num)
                titres_par_lettre[lettre].append(titre_avec_page)

# Écrire l'index organisé par lettre avec deux colonnes et numéros de page
with open(chemin_markdown_final, 'w', encoding='utf-8') as fichier_complet:
    fichier_complet.write("# Index\n\n")
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
