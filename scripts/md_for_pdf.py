import os
import re

def ajuster_liens_et_images(contenu):
    contenu = re.sub(r'\[([^\]]+)\]\(\.\/(?:.*?)\.md#(.*?)\)', r'[\1](#\2)', contenu)
    contenu = re.sub(r'\!\[\]\((assets\/.*?)\)', r'![](../../dictionnaire/\1)', contenu)
    return contenu

def creer_page_titre(lettre):
    return f"""
\\newpage
\\vspace*{{\\fill}}
\\begin{{center}}
\\fontsize{{95}}{{105}}\\selectfont\\textbf{{{lettre}}}
\\end{{center}}
\\vspace*{{\\fill}}
\\newpage
"""


chemin_dossier_dictionnaire = '../dictionnaire'
chemin_markdown_final = 'PDF/dictionnaire_MD_for_PDF.md'

os.makedirs(os.path.dirname(chemin_markdown_final), exist_ok=True)

with open(chemin_markdown_final, 'w', encoding='utf-8') as fichier_complet:
    for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
        lettre = fichier_lettre.upper().replace('.MD', '')
        page_titre = creer_page_titre(lettre)
        fichier_complet.write(page_titre)
        
        chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
        if os.path.isfile(chemin_complet):
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                contenu = ajuster_liens_et_images(contenu)
                fichier_complet.write(contenu + '\n\n')

print(f'Le fichier Markdown a été créé avec succès : {chemin_markdown_final}')
