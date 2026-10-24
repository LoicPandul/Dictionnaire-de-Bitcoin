# Site du Dictionnaire de Bitcoin

Site statique généré depuis `definitions/fr` : une page par définition, une page par lettre et par catégorie, la recherche instantanée, le sitemap, les données structurées et le PDF.

## Construire et vérifier

```bash
cd site
npm ci
node build.mjs     # écrit le site dans site/dist (environ 2 s)
node check.mjs     # une page par définition, contrat d'URL, sitemap, JSON-LD
```

`check.mjs` compare aussi les slugs avec le dépôt pandul.fr s'il est présent (`--pandul <chemin>`), et interroge un serveur avec `--base http://hôte:port`.

Aperçu local : `python3 -m http.server 4318 --bind 0.0.0.0 -d dist`.

## Domaine

Le domaine vit dans une seule clé : `url` dans `config.mjs`. Elle sert aux adresses canoniques, au sitemap, au JSON-LD et aux cartes sociales. Dès qu'elle ne finit plus par `.example`, le build écrit aussi le fichier `CNAME` pour GitHub Pages.

## Adresses

Elles reprennent celles de pandul.fr sans le préfixe `/dictionnaire`, pour que les redirections tombent juste :

| Page | Adresse |
| --- | --- |
| Accueil | `/` |
| Définition | `/<slug>/` (slug de `metadata.yaml`) |
| Catégorie | `/categorie/<slug>/` |
| Lettre | `/lettre/<lettre>/` |

## Publication

Le workflow `.github/workflows/site-pages.yml` se lance à la main seulement (Actions > « Site du dictionnaire » > Run workflow). Avant le premier lancement : régler `url`, puis choisir « GitHub Actions » comme source dans Settings > Pages.

## Fichiers

- `build.mjs` : le générateur ; `lib/content.mjs` lit les définitions (même calcul des slugs, catégories, descriptions et voisins que pandul.fr) ; `lib/markdown.mjs` rend le Markdown et compose les formules avec KaTeX au build ; `lib/templates.mjs` et `lib/seo.mjs` écrivent les pages.
- `static/` : feuille de style, script (recherche, onglets, terme du jour), polices Computer Modern (OFL) et Fira Code, images.
- `tools/prepare-images.sh` : refait les images à partir de la couverture du livre, des pictogrammes du dépôt, des planches de l'Encyclopédie et du film de 1959 (sources et licences dans `tools/image-credits.json`).

## Images et crédits

- Arbre gravé, couverture et livre en volume : tirés de `assets/` (couverture du livre).
- Planches de l'*Encyclopédie* de Diderot et d'Alembert (Monnoyage : balancier, laminoirs ; page de titre, 1751) : domaine public / CC0, Wikimedia Commons.
- Film *Learning to Set Type* (1959) : domaine public, Internet Archive.
- Portrait de Loïc Morel : repris de pandul.fr.
