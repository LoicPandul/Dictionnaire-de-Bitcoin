# Audit UI et UX du site, édition 2027 (12 novembre 2026)

Passe du skill `design-ui` sur le site de la branche `feat/site-dictionnaire`, après le passage à la palette B (section 20 de `direction.md`). La palette, Archivo, les liens soulignés, les coins carrés et l'absence d'ombre restent : l'audit porte sur la structure, la hiérarchie, l'espacement, la typographie et les composants.

## Cadrage

- **Design system** : de fait, et écrit dans `direction.md` (sections 19 et 20) ; jetons en tête de `static/css/site.css`, générés depuis `palette` dans `config.mjs`.
- **Pile** : générateur statique Node (`build.mjs`, `lib/templates.mjs`), HTML, CSS et deux scripts sans framework. Pas de React, pas de shadcn ajouté ; shadcn sert seulement de référence pour les états.
- **Genre** : retouche d'un site déjà construit, sur toutes ses pages types.
- **Mode** : Lire (le visiteur cherche un mot et comprend sa définition) ; Opérer pour la recherche.
- **Contenu** : définitions de 1 ligne (`/crypter/`) à environ 5 000 px de texte (`/signature-de-lamport/`) ; lettre B de 338 mots ; partie technique de 1 060 mots et 33 catégories ; chronologie de 160 dates ; 214 BIP.

## Méthode

Captures pilotées par Playwright (mouvement réduit, animations finies), à 390 et 1 440 px : premier écran, page entière (plafonnée à 7 000 px), fenêtre de recherche ouverte, menu ouvert, focus clavier. 17 pages : accueil FR et EN, cinq définitions (longue, avec formules, anglaise, pas encore traduite, courte, BIP), lettre B, catégorie, partie, recherche avec et sans résultat, chronologie, spécifications, série BIP, 404. Captures relues par moi et par un relecteur indépendant (Sonnet), puis chaque constat confronté à `direction.md` : un trait que Loïc a déjà tranché n'est pas un défaut.

Contrôles automatiques avant et après : aucun défilement horizontal ni texte qui sort de sa boîte (12 largeurs, de 320 à 2 560 px), contrastes de 4,5:1 au moins en clair et en sombre, focus visible partout, cibles de 44 px au téléphone, `npm run check` (liens, contrat d'URL, sitemap).

## Constats, page par page

Phase 1 : gêne l'usage. Phase 2 : sous le niveau voulu. Phase 3 : finition.

### Accueil (FR et EN)

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 | « Nouveau en 2027 » : cinq titres de 32 px soulignés, sans séparation, à des écarts irréguliers (68 à 100 px selon que la description tient en une ou deux lignes) ; la liste remonte de 16 px au-dessus du titre de section. | 2 | **Corrigé** : un filet entre chaque ligne, 20 px au-dessus et au-dessous, noms à la taille de l'énoncé (20 à 24 px), descriptions en Écorce, liste alignée sur le haut du titre. |
| 390 | Même sommaire, mêmes écarts irréguliers. | 2 | **Corrigé** par la même règle. |
| 1440 | « Le livre » : la vidéo du livre commence à la 2e colonne (x 209) alors que tout le reste de la page part de la marge (x 104). | 2 | **Corrigé** : la vidéo part de la 1re colonne. |
| 1440 | « Le mot du jour » : le titre de section est plus petit que le mot. | — | Laissé : c'est le mot qui est le sujet de la section, le titre ne fait que le nommer. |
| 390 | Catégories en deux colonnes, effectif sous le nom. | — | Laissé : la largeur ne permet pas le nom et l'effectif sur une ligne sans couper les noms longs. |

### Définition

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 | « Dans la chronologie » est plus large (710 px) que le texte de la définition (612 px) : deux mesures dans une même colonne. | 2 | **Corrigé** : la liste prend la mesure du texte (34 fois le corps de lecture). |
| 1440 et 390 | Mots-repères (précédent, lettre, suivant) petits et aux deux bords, en double des cartes du bas. | — | Laissé : ce sont les mots-repères du livre (section 8 de la direction) ; leurs zones tactiles font 44 px (vérifié). |
| 1440 | Fiche BIP : statuts en anglais (« Deployed »). | — | Laissé : choix écrit en section 19 (« les statuts gardent le vocabulaire anglais des BIP »). |
| 390 | Définition courte (`/crypter/`) au corps de l'énoncé, plus grand que les autres. | — | Laissé : choix de la section 19 (moins de 360 caractères sans schéma). |
| 1440 et 390 | Chronologie : « 1er mai 2021 » sans « er » en exposant. | 3 | **Corrigé** (décision de Loïc) : rendu à part, `exposants` dans `lib/typo.mjs`, appliqué au texte du `<main>` des pages françaises. « 1er », « 1re », « 2e », « 100 000e » et « XVIIIe siècle » passent en exposant ; le code, les formules, les scripts et les attributs n'y passent pas ; titres, balises meta, JSON-LD, index de recherche et cartes d'aperçu (attribut `data-apercu`) gardent le texte brut. |

### Recherche (page et fenêtre)

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 et 390 | Sans résultat, le constat « Aucun mot ne correspond à… » est en Écorce 15 px, à la taille et à la couleur des pistes qui le suivent ; « Ou par lettre », « Ou par catégorie » se perdent dans le même gris. | 1 | **Corrigé** : le constat passe en encre, à la taille de l'énoncé sur la page (18 px dans la fenêtre) ; les deux libellés deviennent des intertitres (16 px, gras, encre). |
| 1440 | Sans résultat, les 55 catégories forment un nuage de pastilles aux bords irréguliers. | 2 | **Corrigé** : grille de colonnes égales dès 640 px. |
| 1440 et 390 | Partie trouvée d'un nom en encre, reste en Forêt (« SCHNOR » + « R »). | — | Laissé : choix de la section 19 (lisible sur la ligne choisie et en sombre). |
| 1440 | Rangée de filtres sur deux lignes (« Minage » seul). | — | Laissé : la règle des rangées veut qu'elles tiennent entières hors téléphone. |

### Lettre (B)

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 390 | Rangées des lettres et des groupes coupées au bord, sans fondu. | — | Laissé : les fondus ont été retirés exprès (section 19) ; la pastille coupée au bord est l'indice. |
| 1440 | Grande lettre et « Les mots en B » disent la même chose. | 3 | Laissé : la grande capitale est le repère du livre, le titre porte l'effectif et la plage. |

### Catégorie (cryptographie)

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 | « Pour commencer » commence à la hauteur du pictogramme, pas du titre. | 3 | Laissé : la marge s'aligne sur le haut de l'en-tête, comme sur les définitions. |

### Partie (dictionnaire technique)

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 | Les 33 catégories forment sept rangées de pastilles aux bords irréguliers, effectif collé au nom : on ne parcourt pas la liste d'un coup d'œil. | 1 | **Corrigé** : d'abord en colonnes égales (commit `2d4200bb`), puis remplacé par l'index ci-dessous. |
| 390 | Les mêmes pastilles occupent environ 1 800 px avant le premier mot ; page de 124 653 px (1 060 mots, tous les mots de la partie). | 1 | **Corrigé** (décision de Loïc) : la page d'une partie devient l'index de ses catégories (le composant `.index` de l'accueil : pictogramme, nom, effectif), chacune menant à sa page `/categorie/<slug>/`, qui existait déjà avec toutes ses définitions. La page technique passe de 46 020 à 1 403 px à 1 440, et de 124 653 à 2 391 px à 390 ; de même en anglais et pour les deux autres parties. |

### Chronologie

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 | La frise porte les années abrégées (« ’09 ») juste au-dessus de la rangée des années, qui les donne en entier dans les mêmes colonnes : deux fois la même information. | 2 | **Corrigé** : dès que la rangée tient sur une ligne (1 120 px), la frise perd ses étiquettes, descend à 96 px et se pose sur la rangée. Sous 1 120 px, où les colonnes ne correspondent plus, elle les garde. |

### Spécifications et série BIP

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 1440 et 390 | Rien qui gêne. Cartes des séries à cinq niveaux (pictogramme, nom, nom anglais, effectif, texte). | 3 | Laissé. |

### 404

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 390 | Le texte, équilibré (`text-wrap: balance`), s'arrête à 290 px alors que le champ en fait 358 : un bloc étroit au-dessus d'un champ large. | 2 | **Corrigé** : `pretty` au lieu de `balance` sur la 404, 34 em au plus. |
| 1440 et 390 | Champ prérempli avec l'adresse demandée. | — | Laissé : il sert à relancer la recherche sur ce qui a été tapé. |

### Barre, menu, pied

| Largeur | Constat | Phase | Suite |
| --- | --- | --- | --- |
| 390 | « EN » et le menu sans boîte, la loupe encadrée. | — | Laissé : zones de 44 px vérifiées ; la loupe encadrée est le seul champ de la barre. |
| 1440 | Lettres du pied centrées dans leur case, donc 46 px à droite de la marge. | 3 | Laissé : la case entière est la cible et se remplit au survol. |

## Adresses après l'index des parties

- Les adresses des parties (`/partie/<id>/`, `/en/part/<id>/`) et des catégories ne changent pas ; seules les ancres des anciennes sections (`/partie/technique/#c-protocole`) disparaissent. Un fragment n'arrive jamais au serveur, donc `_redirects` ne peut pas le rediriger : chaque ligne de l'index garde l'ancre `c-<slug>`, et `static/js/site.js` remplace l'adresse par la page de la catégorie (vérifié : `/partie/technique/#c-protocole` mène à `/categorie/protocole/`, `/en/part/technical/#c-protocole` à `/en/category/protocol/`). Sans script, l'ancre pose la page sur la bonne ligne de l'index.
- Liens internes : aucun lien du site ne visait ces ancres (seule la page de la partie les produisait). `npm run check` : 0 lien cassé.
- Sitemap : inchangé, il listait déjà les parties et les 55 catégories.
- Données structurées : la `CollectionPage` d'une partie liste ses catégories (33 pour la partie technique) au lieu de ses 1 060 mots.

## Ce qui reste à décider

Rien pour ces pages.

## Contrôles après correction

- Défilement horizontal et texte qui sort de sa boîte : 0 cas sur 120 (12 largeurs × 10 pages, FR et EN).
- Contrastes sous 4,5:1 : 0, en clair et en sombre. Focus sans contour : 0.
- Cibles sous 44 px : le script en compte sur la chronologie (« TOR », « BIP »…), mais ce sont des liens courts dont le `::after` donne déjà 44 px de large (mesuré : 44 px) ; le script mesure la boîte du texte.
- `npm run check` : « Tout est conforme ».
