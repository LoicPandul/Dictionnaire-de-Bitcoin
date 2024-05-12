import re

# Chemin du fichier markdown
chemin_fichier = r"C:\Users\loicm\Documents\GitHub\Dictionnaire\dictionnaire\O.md"

# Lire le contenu du fichier
with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
    contenu = fichier.readlines()

# Modifier les titres qui commencent par "## OP "
nouveau_contenu = []
for ligne in contenu:
    if ligne.startswith('## OP '):
        # Remplacer l'espace par un underscore après "## OP"
        ligne_modifiee = re.sub(r'^(## OP) ', r'\1_', ligne)
        nouveau_contenu.append(ligne_modifiee)
    else:
        nouveau_contenu.append(ligne)

# Sauvegarder les modifications dans le fichier
with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
    fichier.writelines(nouveau_contenu)

print("Les modifications ont été apportées avec succès.")
