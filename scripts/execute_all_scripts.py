import os
import subprocess

chemin_dossier_scripts = '.'

script_actuel = os.path.basename(__file__)

print("Début de l'exécution des scripts Python :")

for fichier in os.listdir(chemin_dossier_scripts):
    chemin_complet = os.path.join(chemin_dossier_scripts, fichier)
    if fichier.endswith('.py') and fichier != script_actuel:
        print(f"Exécution de {fichier}...")
        subprocess.run(['python', chemin_complet], check=True)
        print(f"{fichier} exécuté avec succès.")

print("Tous les scripts ont été exécutés.")

