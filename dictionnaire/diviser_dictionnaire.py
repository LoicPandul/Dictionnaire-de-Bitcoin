import re
import os

# Chemin vers votre fichier markdown source
fichier_source = 'C:/Users/loicm/Documents/GitHub/Dictionnaire/dictionnaire/dictionnaire.md'
# Dossier de sortie pour les fichiers .md séparés
dossier_sortie = 'C:/Users/loicm/Documents/GitHub/Dictionnaire/dictionnaire'

# Assurez-vous que le dossier de sortie existe
os.makedirs(dossier_sortie, exist_ok=True)

# Initialiser un dictionnaire pour stocker les contenus par lettre
contenus_par_lettre = {}

# Lire le fichier source et traiter chaque définition
with open(fichier_source, 'r', encoding='utf-8') as fichier:
    contenu = fichier.read()

# Séparez les définitions en utilisant le modèle de détection
definitions = re.split(r'\n\s*\n', contenu)  # Sépare sur les paragraphes vides

for definition in definitions:
    match = re.match(r'\*\*(.*?) -\*\* (.+)', definition, re.DOTALL)
    if match:
        titre = match.group(1).strip()
        description = match.group(2).strip()
        lettre = titre[0].upper()  # Utilise la première lettre du titre, en majuscule

        # Ajouter la définition au dictionnaire sous la bonne lettre
        if lettre not in contenus_par_lettre:
            contenus_par_lettre[lettre] = []
        contenus_par_lettre[lettre].append(f'## {titre}\n\n{description}\n')

# Écrire les définitions dans leurs fichiers respectifs
for lettre, contenus in contenus_par_lettre.items():
    with open(f'{dossier_sortie}/{lettre}.md', 'w', encoding='utf-8') as fichier_sortie:
        fichier_sortie.write('\n'.join(contenus))

