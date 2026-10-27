# Scripts et génération

Les scripts Python valident le contenu du dépôt et génèrent le livre : PDF broché, PDF relié et
EPUB, pour deux éditions décrites dans `templates/editions.yaml` (`complete` et `essentiel`).

## Prérequis

- Python 3.10 ou plus récent, et les dépendances : `pip install -r scripts/requirements.txt`
- Un moteur LaTeX pour les PDF, au choix :
  - `xelatex` (TeX Live ou MiKTeX), utilisé en priorité s'il est installé ;
  - [Tectonic](https://tectonic-typesetting.github.io/), un moteur XeTeX autonome qui s'installe
    sans droits administrateur : déposez le binaire dans `.tools/bin/tectonic` (dossier ignoré par git).
- [epubcheck](https://github.com/w3c/epubcheck) pour valider l'EPUB (Java) : décompressez l'archive
  dans `.tools/` (`.tools/epubcheck-5.4.0/epubcheck.jar`), ou installez la commande `epubcheck`.

`python3 scripts/main.py info` indique les outils trouvés.

## Commandes

```bash
python3 scripts/main.py check                     # tout valider, sans rien modifier
python3 scripts/main.py fix                       # corrections automatiques (listes, renvois invalides)
python3 scripts/main.py build                     # toutes les éditions, tous les formats
python3 scripts/main.py build --edition complete --format pdf,pdf-relie,epub
python3 scripts/main.py index                     # INDEX.md
python3 scripts/main.py stats                     # stats.md et badge du README
python3 scripts/main.py sync                      # état de la traduction anglaise (voir docs/traduction.md)
python3 scripts/main.py sync --list "en retard"   # traductions à mettre à jour
python3 scripts/main.py sync --mark <slug>        # enregistrer qu'une traduction est à jour
```

Sans argument, `python3 scripts/main.py` ouvre un menu.

`build` lance d'abord `check` et s'arrête en cas d'erreur (`--force` pour passer outre). Les
fichiers sortent dans `build/<édition>/` (ignoré par git), avec les sources LaTeX dans
`build/<édition>/tex-*/` et le rapport d'epubcheck à côté de chaque EPUB.

## Ce que vérifie `check`

- **Métadonnées** : UUID et slugs uniques, dossier = slug, titres en majuscules, catégorie connue,
  renvois vers des UUID existants, images déclarées et présentes.
- **Versions courtes** : chaque `definition.md` a sa `courte.md` (et inversement), qui tient en une
  ou deux phrases et 45 mots au plus, sans liste, image, formule, lien, gras ni titre.
- **Markdown** : listes et citations au format du dépôt.
- **Spécifications** (`specifications/*.yaml`) : champs obligatoires, résumés de 60 mots au plus,
  liens vers des entrées existantes.
- **Chronologie** (`chronologie/fr/*.yaml`) : dates ISO, au moins deux sources par événement,
  renvois existants, un fichier par année.

- **Traductions** (`definitions/en/`) : métadonnées et trace de la source (`source_*`), version
  courte, markdown, images ; une traduction dont la source a disparu est une erreur. Une ligne
  `[INFO]` donne l'état de la synchro ; une traduction en retard n'est pas une erreur (`sync
  --strict` pour l'exiger).

## Organisation

| Dossier | Rôle |
|---|---|
| `core/` | modèle : définitions, taxonomie (parties et catégories), spécifications, chronologie, livre |
| `generators/` | PDF (`pdf_generator.py`, conversion markdown dans `latex.py`), EPUB, INDEX.md, stats.md |
| `validators/` | métadonnées, versions courtes, markdown, spécifications, chronologie et traductions |
| `core/translations.py` | empreintes, paires français / anglais, statuts de synchro |
| `migrations/` | scripts de rangement à usage unique (`structure_bilingue.py`, voir docs/structure.md) |
