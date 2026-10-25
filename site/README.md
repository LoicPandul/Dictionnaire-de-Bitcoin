# Site du Dictionnaire de Bitcoin

Site statique généré depuis `definitions/fr` : une page par définition (1 408), une page par lettre et par catégorie, la recherche instantanée, le sitemap, les données structurées et le PDF. Il est pensé pour Cloudflare Pages.

La direction artistique (« Le livre ouvert ») et sa relecture sont dans `design/` : `direction.md`, `inspirations.md`, `revue.md`.

## Construire et vérifier

```bash
cd site
npm ci
npm run build      # écrit le site dans site/dist (environ 1 s)
npm run check      # une page par définition, contrat d'URL, sitemap, JSON-LD
npm run serve      # aperçu local sur http://127.0.0.1:4318/
```

`check.mjs` compare aussi les slugs avec le dépôt pandul.fr s'il est présent (`--pandul <chemin>`), et interroge un serveur avec `--base http://hôte:port`.

`serve.mjs` imite Cloudflare Pages : `index.html` des dossiers, redirection vers la barre finale, `404.html` servie avec le code 404, en-têtes de `_headers`. Pour l'ouvrir depuis un autre appareil du réseau : `npm run preview` (écoute sur 0.0.0.0, port 4318).

## Publication sur Cloudflare Pages

Le site se publie en reliant ce dépôt GitHub à un projet Cloudflare Pages (offre gratuite). Rien n'est encore créé côté Cloudflare.

Réglages à saisir dans *Workers & Pages > Créer > Pages > Connecter à Git*, après avoir choisi le dépôt `Dictionnaire-de-Bitcoin` :

| Réglage | Valeur |
| --- | --- |
| Branche de production | `main` |
| Préréglage de framework | Aucun (*None*) |
| Commande de build | `npm run build` |
| Répertoire de sortie du build | `dist` |
| Répertoire racine (*Root directory*, dans les paramètres avancés) | `site` |
| Variable d'environnement | `NODE_VERSION` = `22` |

Cloudflare installe les dépendances (`npm ci`, grâce à `package-lock.json`) avant la commande de build. Le build lit `../definitions`, `../templates` et `../dictionnaire-de-bitcoin.pdf` : Cloudflare clone tout le dépôt, le répertoire racine ne fait que fixer le dossier de travail.

Le build écrit lui-même dans `dist/` :

- `_headers` : politique de sécurité du contenu (avec l'empreinte du seul script en ligne), `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `X-Frame-Options` ; cache d'un an pour le CSS et les scripts (leur nom contient une empreinte), les polices et KaTeX ; une semaine pour les images, la vidéo et les schémas ; une heure pour les index de recherche.
- `_redirects` : les anciennes adresses en `/dictionnaire/…` (forme de pandul.fr) vers les nouvelles.
- `404.html` : Cloudflare Pages la sert automatiquement, avec le code 404, pour toute adresse inconnue.

Limites de l'offre gratuite respectées : environ 1 600 fichiers (plafond 20 000), le plus gros est le PDF (2,7 Mo, plafond 25 Mo).

Une fois le domaine acheté : changer `url` dans `config.mjs` (voir plus bas), pousser, puis ajouter le domaine dans *Pages > projet > Domaines personnalisés*. Les branches autres que `main` reçoivent des aperçus automatiques sur `<branche>.<projet>.pages.dev` ; on peut les désactiver dans *Paramètres > Builds > Contrôles des déploiements de branche*.

## Domaine

Le domaine vit dans une seule clé : `url` dans `config.mjs`, aujourd'hui la valeur provisoire `https://dictionnaire-bitcoin.example`. Elle sert aux adresses canoniques, au sitemap, au JSON-LD, aux cartes sociales et à la citation des définitions.

## Couleurs, polices et édition

Le site suit la charte de l'édition 2027 (`design/charte-2027.md`, branche `feat/couverture-2027`) : Figue, banian, Archivo et Atkinson Hyperlegible Mono.

- **Couleurs** : toutes dans `palette`, dans `config.mjs`. Le build en réécrit le bloc de jetons en tête de `static/css/site.css` (entre `palette:début` et `palette:fin`), la couleur de la barre des navigateurs et le manifeste ; les rôles (fond, texte, lien, bouton, mode sombre) sont définis juste dessous. Pour changer de palette : modifier `palette`, relancer le build.
- **Polices** : `static/fonts/archivo.woff2` (variable, largeurs 62 à 100, graisses 400 à 900, latin), `archivo-italique.woff2` et `atkinson-mono.woff2`, tirées de `fonts/` (OFL). `tools/chasses.py` refait `lib/archivo-advances.json`, qui sert à dimensionner les vedettes.
- **Jaquette de l'accueil** : `tools/jaquette-2027.py` réutilise le générateur de la couverture 2027 (`design/couverture/banyan.py` et `typeset.py`) pour dessiner le banian sans ses textes et écrire la position du titre dans `lib/jaquette.json` ; `tools/raster-jaquette.mjs` le rend en images, encodées ensuite en AVIF et WebP (`static/img/jaquette-*`, `avant-*`). À refaire si la couverture 2027 change.
- **Millésime** : `site.edition` dans `config.mjs`. Les pages et la vidéo du livre imprimé restent celles de l'édition 2026, la seule parue.

## Adresses

Elles reprennent celles de pandul.fr sans le préfixe `/dictionnaire`, pour que les redirections tombent juste :

| Page | Adresse |
| --- | --- |
| Accueil | `/` |
| Définition | `/<slug>/` (slug de `metadata.yaml`) |
| Catégorie | `/categorie/<slug>/` |
| Lettre | `/lettre/<lettre>/` |
| Recherche | `/recherche/?q=…` (nouvelle) |

## Fichiers

- `build.mjs` : le générateur. `lib/content.mjs` lit les définitions (même calcul des slugs, catégories, descriptions et voisins que pandul.fr) ; `lib/markdown.mjs` rend le Markdown et compose les formules avec KaTeX au build ; `lib/templates.mjs` écrit les pages ; `lib/seo.mjs` le JSON-LD, le sitemap et robots.txt ; `lib/cloudflare.mjs` `_headers` et `_redirects`.
- `lib/archivo-advances.json` : chasses d'Archivo Titre, pour calculer au build la taille de chaque vedette (deux lignes au plus à toutes les largeurs) ; `lib/jaquette.json` : position du titre sur la jaquette.
- `static/css/site.css` : toute la mise en forme, jetons en tête. `static/js/site.js` : thème, barre, transitions entre pages, recherche, 404. `static/js/accueil.js` : le mot du jour et la tranche.
- `static/fonts/` : Archivo et Atkinson Hyperlegible Mono, sous licence OFL (textes joints).
- `tools/prepare-assets.py` et `tools/raster-pictos.mjs` : refont les images à partir des sources du dépôt (voir l'en-tête du script).

## Images

Toutes viennent du livre et du dépôt, aucune image extérieure :

- le banian de la couverture 2027 (couronne et racines), calculé par le générateur de la couverture ;
- les 19 pictogrammes de `assets/pictograms`, retracés (ceux de 2026, en attendant le jeu 2027) ;
- six pages intérieures et la boucle « feuilletage » (`static/video/feuilletage.mp4`), rendues depuis le PDF de l'édition 2026 ;
- la carte sociale (`tools/carte-sociale.html`) ;
- le portrait de Loïc Morel ;
- les schémas des définitions, copiés depuis leurs dossiers.
