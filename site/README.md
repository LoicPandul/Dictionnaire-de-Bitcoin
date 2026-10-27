# Site du Dictionnaire de Bitcoin

Site statique généré depuis le dépôt : une page par définition (1 643 en octobre 2026), par lettre, par catégorie et par partie du livre, la chronologie, les résumés des spécifications (BIP, BOLT, bLIP, NIP), la recherche instantanée, le sitemap, les données structurées et le PDF. Le français est à la racine, l'anglais sous `/en/`. Il est pensé pour Cloudflare Pages.

La direction artistique (« Le livre ouvert ») et sa relecture sont dans `design/` : `direction.md`, `inspirations.md`, `revue.md`.

## Construire et vérifier

```bash
cd site
npm ci
npm run build      # écrit le site dans site/dist, français puis anglais (environ 25 s)
npm run check      # pages, contrat d'URL, sitemap, JSON-LD, anglais, et tous les liens internes (ancres comprises)
npm run serve      # aperçu local sur http://127.0.0.1:4318/
```

`check.mjs` compare aussi les slugs avec le dépôt pandul.fr s'il est présent (`--pandul <chemin>`), et interroge un serveur avec `--base http://hôte:port`.

`serve.mjs` imite Cloudflare Pages : `index.html` des dossiers, redirection vers la barre finale, la `404.html` la plus proche servie avec le code 404 (`/en/404.html` sous `/en/`), en-têtes de `_headers`. Pour l'ouvrir depuis un autre appareil du réseau : `npm run preview` (écoute sur 0.0.0.0, port 4318).

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

Le domaine vit dans une seule clé : `url` dans `config.mjs`, aujourd'hui `https://dictionnaire-bitcoin.com`. Elle sert aux adresses canoniques, au sitemap, au JSON-LD, aux cartes sociales et à la citation des définitions.

## Couleurs, polices et édition

Le site suit la charte 2027 (`design/charte-2027.md`, branche `feat/couverture-2027`) et la couverture validée, l'Allée des baobabs : Figue `#AA226A`, Archivo et Atkinson Hyperlegible Mono. La palette de `config.mjs` reprend ses valeurs écran une à une, et les rôles du mode sombre suivent son tableau (fond Nuit, liens et bouton en Figue claire). Pas d'ombre portée, liens toujours soulignés.

- **Couleurs** : toutes dans `palette`, dans `config.mjs`. Le build en réécrit le bloc de jetons en tête de `static/css/site.css` (entre `palette:début` et `palette:fin`), la couleur de la barre des navigateurs et le manifeste ; les rôles (fond, texte, lien, bouton, mode sombre) sont définis juste dessous. Pour changer de palette : modifier `palette`, relancer le build.
- **Polices** : `static/fonts/archivo.woff2` (variable, largeurs 62 à 100, graisses 400 à 900, latin), `archivo-italique.woff2` et `atkinson-mono.woff2`, tirées de `fonts/` (OFL). `tools/chasses.py` refait `lib/archivo-advances.json`, qui sert à dimensionner les vedettes.
- **Jaquette de l'accueil** : `tools/allee.py` reprend `design/couverture/baobab.py` (même graine, même dessin) et écrit l'Allée des baobabs dans `lib/allee.json`, un calque par arbre ; le site la pose en SVG dans la page, ce qui permet de faire pousser les arbres et de les faire suivre le pointeur. À refaire si la couverture change : `python3 site/tools/allee.py <worktree couverture>/design/couverture > site/lib/allee.json`.
- **Favicon et carte sociale** : copiés de `design/couverture/export/` (`favicon.svg`, `favicon-32/180/512.png`, `couverture-2027-partage.png` converti en JPEG).
- **Pictogrammes** : ceux du livre 2027, lus au build dans `assets/pictograms` d'après `templates/parts.yaml` (un par catégorie).
- **Millésime** : `site.edition` dans `config.mjs`. Les pages et la vidéo du livre imprimé restent celles de l'édition 2026, la seule parue.

## Adresses

Elles reprennent celles de pandul.fr sans le préfixe `/dictionnaire`, pour que les redirections tombent juste. L'anglais reprend les mêmes slugs de définition sous `/en/`, avec des segments traduits :

| Page | Français | Anglais |
| --- | --- | --- |
| Accueil | `/` | `/en/` |
| Définition | `/<slug>/` (slug de `metadata.yaml`) | `/en/<slug>/` |
| Catégorie | `/categorie/<slug>/` | `/en/category/<nom anglais>/` |
| Lettre | `/lettre/<lettre>/` | `/en/letter/<lettre>/` |
| Partie du livre | `/partie/<id>/` | `/en/part/<id anglais>/` |
| Chronologie | `/chronologie/` | `/en/timeline/` |
| Spécifications | `/specifications/` et `/specifications/<série>/` | `/en/specifications/…` |
| Recherche | `/recherche/?q=…` | `/en/search/?q=…` |

Les catégories de pandul.fr renommées en 2027 (`histoire`, `organisation`, `communaute`, `outil`) sont redirigées dans `_redirects` vers leur remplaçante, calculée depuis `edition-2027/reclassement.tsv`.

## Contenus de l'édition 2027

Tout est lu dans les fichiers présents, sans liste écrite dans le code : une catégorie, une année, une série ou une fiche ajoutée ou retirée apparaît ou disparaît au build suivant.

- **Parties et catégories** : `templates/parts.yaml` range chaque catégorie dans une partie (technique, écosystème, personnes, spécifications), avec son nom affiché et son pictogramme. Une catégorie absente de ce fichier rejoint la partie technique.
- **Chronologie** : `chronologie/<langue>/*.yaml`, une section par fichier (« avant-2009 » en tête). Chaque date liée à une définition (`related`) apparaît aussi sur la page de cette définition ; un slug qui n'existe plus n'est simplement pas lié.
- **Spécifications** : `specifications/*.yaml`, regroupées comme dans le livre (`templates/editions.yaml` : BOLT et bLIP ensemble). La définition consacrée à un document (`definition`) affiche sa fiche (statut, auteurs, date) ; un champ `summary_en` sera pris pour l'anglais quand il existera.
- **Versions courtes** : `courte.md` sert de résumé dans les listes, les cartes d'aperçu et la recherche.
- **Schémas** : le SVG du dossier `assets/` quand il existe (format préféré de la charte), sinon le PNG ; sous 640 px, l'image garde 640 px dans un cadre qui défile.

## Langues

Le français est la langue par défaut. `lib/i18n.mjs` porte les chemins et tous les textes de l'interface dans les deux langues, scripts compris (`js`), et les noms anglais des catégories (une catégorie sans nom anglais garde son nom français).

Les définitions anglaises viennent de `definitions/en/` (chantier `feat/english-2027`). Format attendu : un dossier par entrée, nommé comme le dossier français (`definitions/en/<lettre>/<slug>/` ou `definitions/en/<slug>/`), avec `definition.md` et, s'ils existent, `courte.md` et un `metadata.yaml` (`title`, `english_term`…) ; le dossier est aussi retrouvé par l'`uuid` ou le `slug` de son `metadata.yaml`. Une entrée sans traduction garde sa page sous `/en/<slug>/`, en français, avec la mention « In French for now » : son adresse canonique est alors la page française, et elle n'entre pas dans le sitemap. La chronologie suit la même règle avec `chronologie/en/`.

## Fichiers

- `build.mjs` : le générateur. `lib/content.mjs` lit les définitions (même calcul des slugs, catégories, descriptions et voisins que pandul.fr) ; `lib/markdown.mjs` rend le Markdown et compose les formules avec KaTeX au build ; `lib/templates.mjs` écrit les pages ; `lib/seo.mjs` le JSON-LD, le sitemap et robots.txt ; `lib/cloudflare.mjs` `_headers` et `_redirects`.
- `lib/i18n.mjs` : langues, chemins et textes de l'interface. `lib/edition.mjs` : parties, chronologie et spécifications.
- `lib/archivo-advances.json` : chasses d'Archivo Titre, pour calculer au build la taille de chaque vedette (deux lignes au plus à toutes les largeurs) ; `lib/allee.json` : l'Allée des baobabs de la couverture.
- `static/css/site.css` : toute la mise en forme, jetons en tête. `static/js/site.js` : thème, barre, transitions entre pages, recherche, 404. `static/js/accueil.js` : le mot du jour et la tranche.
- `static/fonts/` : Archivo et Atkinson Hyperlegible Mono, sous licence OFL (textes joints).
- `tools/allee.py` : l'Allée des baobabs. `tools/prepare-assets.py` : pages et vidéo du livre imprimé (voir l'en-tête du script).

## Images

Toutes viennent du livre et du dépôt, aucune image extérieure :

- l'Allée des baobabs de la couverture 2027, calculée par le générateur de la couverture ;
- les pictogrammes 2027 de `assets/pictograms` ;
- quatre pages intérieures et la boucle « feuilletage » (`static/video/feuilletage.mp4`), rendues depuis le PDF de l'édition 2026 ;
- le favicon et la carte sociale du script de couverture ;
- le portrait de Loïc Morel ;
- les schémas des définitions, copiés depuis leurs dossiers.
