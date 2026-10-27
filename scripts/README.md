# Scripts et génération

Les scripts Python valident le contenu du dépôt et génèrent le livre, en PDF à imprimer et en
EPUB, pour deux éditions décrites dans `templates/editions.yaml` :

| Édition | Contenu | PDF imprimé (Amazon KDP, broché) |
|---|---|---|
| `complete` | définitions développées, personnes, chronologie, BIP, BOLT et bLIP | 7 × 10 po, intérieur couleur premium, papier blanc |
| `essentiel` | définitions courtes des parties technique et écosystème | 5 × 8 po (poche), intérieur noir et blanc |

Le format vient de la clé `format` de l'édition (`couleur` par défaut, ou `poche`). La mise en
page suit la charte graphique 2027 : polices Archivo et Atkinson Hyperlegible Mono (`fonts/`),
couleurs de la charte en recettes CMJN pour le livre couleur (Figue pour les titres, les mots
vedettes, les renvois et les titres courants ; texte courant en noir). Le livre couleur prend les
schémas en couleur : le SVG de chaque schéma est converti en PDF vectoriel par Chrome sans
interface (cache dans `build/cache/schemas/`), à défaut le PNG couleur ; le poche prend les
versions noir et blanc (`image-N-nb.pdf`). La marge intérieure est relevée si le nombre de pages
dépasse le seuil KDP (19,1 mm de 501 à 700 pages, 22,3 mm de 701 à 828), et `build` signale un
livre hors des 24 à 828 pages acceptées par KDP.

## Prérequis

- Python 3.10 ou plus récent, et les dépendances : `pip install -r scripts/requirements.txt`
- Un moteur LaTeX pour les PDF, au choix :
  - `xelatex` (TeX Live ou MiKTeX), utilisé en priorité s'il est installé ;
  - [Tectonic](https://tectonic-typesetting.github.io/), un moteur XeTeX autonome qui s'installe
    sans droits administrateur : déposez le binaire dans `.tools/bin/tectonic` (dossier ignoré par git).
- Chrome ou Chromium (facultatif) pour les schémas vectoriels du livre couleur : commande
  `google-chrome` ou `chromium`, Chromium de Playwright, ou chemin donné par `CHROME_PATH`.
  Sans lui, le livre couleur prend les PNG couleur des schémas.
- [epubcheck](https://github.com/w3c/epubcheck) pour valider l'EPUB (Java) : décompressez l'archive
  dans `.tools/` (`.tools/epubcheck-5.4.0/epubcheck.jar`), ou installez la commande `epubcheck`.

`python3 scripts/main.py info` indique les outils trouvés.

## Commandes

```bash
python3 scripts/main.py check                     # tout valider, sans rien modifier
python3 scripts/main.py fix                       # corrections automatiques (listes, renvois invalides)
python3 scripts/main.py build                     # toutes les éditions, tous les formats
python3 scripts/main.py build --edition complete --format pdf,epub
python3 scripts/main.py index                     # INDEX.md
python3 scripts/main.py stats                     # stats.md et badge du README
```

Sans argument, `python3 scripts/main.py` ouvre un menu.

`build` lance d'abord `check` et s'arrête en cas d'erreur (`--force` pour passer outre). Les
fichiers sortent dans `build/<édition>/` (ignoré par git), avec les sources LaTeX dans
`build/<édition>/tex/` et le rapport d'epubcheck à côté de chaque EPUB.

## Ce que vérifie `check`

- **Métadonnées** : UUID et slugs uniques, dossier = slug, titres en majuscules, catégorie connue,
  renvois vers des UUID existants, images déclarées et présentes. Une image de `assets:` n'a que
  deux champs : `filename`, et `credit` pour une image de tiers (logo, capture), sur une ligne de
  200 caractères au plus ; ce crédit s'imprime en petit sous l'image, dans le PDF et l'EPUB.
- **Versions courtes** : chaque `definition.md` a sa `courte.md` (et inversement), qui tient en une
  ou deux phrases et 45 mots au plus, sans liste, image, formule, lien, gras ni titre.
- **Markdown** : listes et citations au format du dépôt.
- **Spécifications** (`specifications/*.yaml`) : champs obligatoires, résumés de 60 mots au plus,
  liens vers des entrées existantes.
- **Chronologie** (`chronologie/fr/*.yaml`) : dates ISO, au moins deux sources par événement,
  renvois existants, un fichier par année.

## Organisation

| Dossier | Rôle |
|---|---|
| `core/` | modèle : définitions, taxonomie (parties et catégories), spécifications, chronologie, livre |
| `generators/` | PDF (`pdf_generator.py`, conversion markdown dans `latex.py`), EPUB, INDEX.md, stats.md |
| `validators/` | métadonnées, versions courtes, markdown, spécifications et chronologie |
