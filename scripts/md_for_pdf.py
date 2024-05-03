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
                        new_content.append(parts[i+1].strip())
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

chemin_dossier_dictionnaire = '../dictionnaire'
chemin_markdown_final = 'PDF/dictionnaire_MD_for_PDF.md'

os.makedirs(os.path.dirname(chemin_markdown_final), exist_ok=True)

with open(chemin_markdown_final, 'w', encoding='utf-8') as fichier_complet:
    fichier_complet.write("# Index\n\n")
    for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
        if fichier_lettre.endswith(".md"):
            with open(os.path.join(chemin_dossier_dictionnaire, fichier_lettre), 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                titres = re.findall(r'^##\s*(.*)$', contenu, flags=re.MULTILINE)
                for titre in titres:
                    anchor = titre.lower().replace(' ', '-').replace('.', '.')
                    anchor = re.sub(r'[«»|]', ' ', anchor)
                    anchor = re.sub(r'\s+', '-', anchor.strip())
                    anchor = re.sub(r'--+', '-', anchor)
                    anchor = re.sub(r'[^\w.-]', '', anchor)
                    fichier_complet.write(f"- [{titre}](#{anchor})\n")
                fichier_complet.write("\n")

    for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
        if fichier_lettre.endswith(".md"):
            lettre = fichier_lettre.upper().replace('.MD', '')
            page_titre = creer_page_titre(lettre)
            fichier_complet.write(page_titre)
            
            chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                contenu = ajuster_liens_et_images(contenu)
                contenu = markdown_to_latex_lists(contenu)
                fichier_complet.write(contenu + '\n\n')

print(f'Le fichier Markdown a été créé avec succès : {chemin_markdown_final}')
