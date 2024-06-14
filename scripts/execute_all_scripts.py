import os
import subprocess

chemin_dossier_scripts = '.'

script_actuel = os.path.basename(__file__)

scripts_prioritaires = [
    'puces_et_citations.py',
    'generate_dictionary_files.py',
    'md_for_pdf.py',
    'update_index.py',
    'stats.py',
    'termes_manquants.py'
]

print("Début de l'exécution des scripts Python :\n")

for script in scripts_prioritaires:
    chemin_complet = os.path.join(chemin_dossier_scripts, script)
    if os.path.isfile(chemin_complet):
        subprocess.run(['python', chemin_complet], check=True)
        print(f" - {script}")
    else:
        print(f"Le fichier {script} n'a pas été trouvé et n'a pas pu être exécuté.")

for fichier in os.listdir(chemin_dossier_scripts):
    if fichier.endswith('.py') and fichier not in scripts_prioritaires + [script_actuel]:
        chemin_complet = os.path.join(chemin_dossier_scripts, fichier)
        subprocess.run(['python', chemin_complet], check=True)
        print(f" - {fichier}")

print("\nTous les scripts ont été exécutés.")
