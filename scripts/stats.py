import os
import re
from collections import Counter

def normaliser_terme(mot):
    mot = mot.lower()
    if mot.endswith('s'):
        mot = mot[:-1]
    return mot

def compter_definitions_par_lettre(chemin_index):
    with open(chemin_index, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        lettres = re.findall(r'\[([ÉA-Z])', contenu, re.IGNORECASE)
        compteur_lettres = Counter([lettre.upper() for lettre in lettres if lettre.isalpha()])
        if 'É' in compteur_lettres:
            compteur_lettres['E'] += compteur_lettres.pop('É')
        return dict(sorted(compteur_lettres.items(), key=lambda item: (-item[1], item[0])))

def termes_les_plus_frequents(chemin_dictionnaire_complet):
    with open(chemin_dictionnaire_complet, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        mots = re.findall(r'\b[a-zéèàêA-ZÉÈÀÊ]{4,}\b', contenu, re.IGNORECASE)
        mots_normalises = [normaliser_terme(mot) for mot in mots]
        compteur_mots = Counter(mots_normalises)
        mots_ignores = {'dan', 'sont', 'pour', 'chaque', 'avec', 'san', 'sou', 'plu', 'permet', 'être', 'peut', 'Cette', 'comme', 'cette', 'elle', 'leur', 'même', 'utilisé', 'deux', 'autre', 'voir', 'définition'}
        for mot in list(compteur_mots):
            if mot in mots_ignores:
                del compteur_mots[mot]
        return compteur_mots.most_common(20)

chemin_base = os.path.dirname(os.path.dirname(__file__))
chemin_index = os.path.join(chemin_base, 'INDEX.md')
chemin_dictionnaire_complet = os.path.join(chemin_base, 'autres_formats/dictionnaire_complet/dictionnaire_complet.md')
chemin_stats = os.path.join(chemin_base, 'stats.md')

stats_lettres = compter_definitions_par_lettre(chemin_index)
termes_frequents = termes_les_plus_frequents(chemin_dictionnaire_complet)
total_definitions = sum(stats_lettres.values())

with open(chemin_stats, 'w', encoding='utf-8') as fichier_stats:
    fichier_stats.write("## Statistiques du *Dictionnaire de Bitcoin*\n\n")
    fichier_stats.write(f"### Nombre total de définitions : \n**-> {total_definitions}**\n\n")
    fichier_stats.write("### Nombre de définitions par lettre :\n")
    for i, (lettre, nombre) in enumerate(stats_lettres.items(), start=1):
        fichier_stats.write(f"{i}. ***{lettre}*** - {nombre}\n")
    fichier_stats.write("\n### Termes techniques les plus rencontrés :\n")
    for i, (mot, compteur) in enumerate(termes_frequents, start=1):
        fichier_stats.write(f"{i}. ***{mot}*** - {compteur}\n")

print(f"Statistiques générées dans {chemin_stats}")
