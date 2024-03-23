import os

def nettoyer_nom_fichier(nom):
    caracteres_interdits = '<>:"/\\|*'
    for car in caracteres_interdits:
        nom = nom.replace(car, '')  # Supprime les caractères interdits
    nom = nom.replace('?', '0')  # Remplace '?' par '0'
    return nom

# Chemin vers le dossier contenant les fichiers md initiaux
chemin_dossier_dictionnaire = '../dictionnaire'
# Chemin pour le fichier md unique compilé
chemin_dictionnaire_complet = '../dictionnaire_complet/dictionnaire_complet.md'
# Chemin pour les fichiers de définitions individuelles
chemin_definitions_individuelles = '../definitions_individuelles'

# S'assurer que les dossiers de sortie existent
os.makedirs(os.path.dirname(chemin_dictionnaire_complet), exist_ok=True)
os.makedirs(chemin_definitions_individuelles, exist_ok=True)

# Création du dictionnaire complet
with open(chemin_dictionnaire_complet, 'w', encoding='utf-8') as fichier_complet:
    for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
        chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
        # Vérifier si le chemin pointe vers un fichier avant de tenter de l'ouvrir
        if os.path.isfile(chemin_complet):
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                fichier_complet.write(contenu + '\n\n')

# Extraction et création des fichiers de définitions individuelles
for fichier_lettre in sorted(os.listdir(chemin_dossier_dictionnaire)):
    chemin_complet = os.path.join(chemin_dossier_dictionnaire, fichier_lettre)
    if os.path.isfile(chemin_complet):  # De nouveau, vérifier si c'est un fichier
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            definitions = contenu.split('## ')[1:]  # Ignorer le premier élément vide
            for defi in definitions:
                titre = defi.split('\n', 1)[0].strip()
                titre_nettoye = nettoyer_nom_fichier(titre)
                chemin_fichier_def = os.path.join(chemin_definitions_individuelles, titre_nettoye + ".md")
                with open(chemin_fichier_def, 'w', encoding='utf-8') as fichier_def:
                    fichier_def.write(f"## {defi}")
