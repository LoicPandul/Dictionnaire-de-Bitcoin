# Scripts et génération

Le projet utilise des scripts Python pour générer le PDF et maintenir les fichiers d'index et de statistiques.

## Prérequis

- Python 3.8+
- XeLaTeX (pour la génération PDF)

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez le script principal et choisissez une option dans le menu :

```bash
python main.py
```

Options disponibles :
- **0** : Build complet (PDF, INDEX, stats)
- **1** : Générer le PDF
- **2** : Mettre à jour index.md
- **3** : Générer les statistiques
- **4** : Vérifier le markdown
- **5** : Corriger le markdown (auto-fix)
- **6** : Afficher les informations
- **7** : Quitter