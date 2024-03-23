import os
import re

def nettoyer_nom_fichier(nom):
    caracteres_interdits = '<>:"/\\|*'
    for car in caracteres_interdits:
        nom = nom.replace(car, '')  # Supprime les caractères interdits
    nom = nom.replace('?', '0')  # Remplace '?' par '0'
    return nom

def ajuster_liens(contenu, type_document):
    if type_document == 'complet':
        # Pour dictionnaire_complet, conserver uniquement le texte et l'ancre
        contenu = re.sub(r'\[([^\]]+)\]\(\.\/(?:.*?)\.md#(.*?)\)', r'[\1](#\2)', contenu)
    elif type_document == 'individuel':
        # Pour definitions_individuelles, ajuster directement sans le formatage markdown intermédiaire
        contenu = re.sub(r'\[([^\]]+)\]\(\.\/(.*?)\.md#(.*?)\)', r'[\1](/dictionnaire/\2.md#\3)', contenu)
    return contenu

# Chemin vers le dossier contenant les fichiers md initiaux
chemin_dossier_dictionnaire = '../dictionnaire'
# Chemin pour les dossiers de sortie dans autres_formats
chemin_autres_formats = '../autres_formats'
chemin_dictionnaire_complet = os.path.join(chemin_autres_formats, 'dictionnaire_complet/dictionnaire_complet.md')
chemin_definitions_individuelles = os.path.join(chemin_autres_formats, 'definitions_individuelles')

# S'assurer que les dossiers de sortie existent
os.makedirs(os.path.dirname(chemin_dictionnaire_complet), exist_ok=True)
os.makedirs(chemin_definitions_individuelles, exist_ok=True)

# Création du dictionnaire complet
with open(chemin_dictionnaire_complet, 'w', encoding='utf-8') as fichier_complet:
    for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
        chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
        if os.path.isfile(chemin_complet):
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                contenu = ajuster_liens(contenu, 'complet')
                fichier_complet.write(contenu + '\n\n')

# Extraction et création des fichiers de définitions individuelles
for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
    chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
    if os.path.isfile(chemin_complet):
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            contenu = ajuster_liens(contenu, 'individuel')
            definitions = contenu.split('## ')[1:] 
            for defi in definitions:
                titre = defi.split('\n', 1)[0].strip()
                titre_nettoye = nettoyer_nom_fichier(titre)
                chemin_fichier_def = os.path.join(chemin_definitions_individuelles, titre_nettoye + ".md")
                with open(chemin_fichier_def, 'w', encoding='utf-8') as fichier_def:
                    fichier_def.write(f"## {defi}")
