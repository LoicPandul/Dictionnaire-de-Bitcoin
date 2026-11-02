# Direction artistique : « Le livre ouvert »

Version 2. La version 1 a été relue par un directeur artistique indépendant (sous-agent sans accès à mon raisonnement) ; ses objections et ce que j'en ai fait sont en annexe (section 14). Cette version est celle qu'on construit.

## 1. Ce qui a été rejeté

La première version mélangeait des gravures de l'*Encyclopédie* (hors sujet), un gris terne, du bleu nuit et un orange de signalisation, du Computer Modern partout (fragile à l'écran en petit), et des cartes grises empilées. Rien ne disait « c'est le *Dictionnaire de Bitcoin* » ; tout disait « gabarit éditorial ».

Leçon : l'identité existe déjà, dans le livre. Il faut la prendre au sérieux, la moderniser, et la faire vivre à l'écran, sans la déguiser.

## 2. Inventaire du sujet

1. **Le nom** : *Dictionnaire de Bitcoin*, sous-titre « Tout le vocabulaire technique de Bitcoin ».
2. **La jaquette** : au dos, trois paragraphes (« Plus de 1400 définitions techniques », « Un projet ouvert », « Un ouvrage rédigé par Loïc Morel ») ; sur la tranche, le titre vertical et une feuille composée ; devant, un arbre gravé gris-bleu sur bleu nuit `#193042`, le titre en capitales Computer Modern couleur os, « Loïc Morel, Édition 2026 » sur le tronc.
3. **Les nombres** : 1 408 définitions, 19 catégories, 26 lettres (B en compte 334, dont 197 BIP ; Y seulement 2), 2 625 renvois, 208 termes anglais, 51 définitions avec formules, 53 avec schémas, 594 pages.
4. **L'intérieur du livre** : vedettes en grotesque grasse capitale dans un cartouche bleu nuit, étiquette de catégorie avec pictogramme, terme anglais, « Termes associés » en fin d'entrée, mots-repères en tête de page.
5. **Les 19 pictogrammes** de catégorie.
6. **L'objet imprimé** : broché et relié, ISBN 9798250570664 et 9798251996579, Bitcoin Bazar et Amazon ; PDF gratuit.
7. **Le projet ouvert** : un dossier par définition sur GitHub, cinq contributeurs GitHub nommés dans le livre, licence CC BY-NC-SA 4.0, dons Lightning `sats@pandul.fr`.
8. **L'auteur** : Loïc Morel (Pandul). Ses mots (README) : « Je gagne une petite marge sur chaque exemplaire physique vendu. »
9. **Les gestes du dictionnaire papier** : feuilleter, chercher par lettre, suivre un renvoi, lire les mots-repères.

## 3. Le concept

> Sur ce site, **la jaquette, la tranche et les pages du *Dictionnaire de Bitcoin*** deviennent **l'interface** : on entre par la jaquette dépliée, on feuillette la tranche pour parcourir les 1 408 mots, on lit chaque définition sur une page composée comme celles du livre.

**Test du concurrent.** Un glossaire Bitcoin d'exchange ou un wiki n'a ni cette jaquette gravée, ni ce livre de 594 pages, ni cette tranche de 1 408 traits faite de ses propres données. La phrase ne marche que pour ce livre.

**La chose vivante : « Feuilleter ».** La tranche du livre, dessinée avec les vraies données : un trait par définition, dans l'ordre alphabétique, la hauteur en racine carrée de la longueur du texte. Deux niveaux, parce que 1 408 traits ne tiennent pas lisiblement sur une ligne :

- **Bureau** : une rangée de 26 blocs-lettres (largeur proportionnelle au nombre de mots, 28 px au minimum, la capitale CMU dessus). Survoler ou choisir un bloc déploie ses traits dans une bande de lecture pleine largeur, espacés de 4 px ou plus ; le trait sous le curseur se surligne et l'aperçu au-dessus affiche le mot en grand, sa catégorie et le début de sa définition. Clic : ouvre la page.
- **Téléphone** : la bande défile sous une aiguille fixe (défilement natif, inertie, un trait tous les 4 px) ; l'aperçu suit ; on le touche pour ouvrir. Les 26 lettres au-dessus servent de raccourcis.
- **Clavier** : la bande est un curseur (`role="slider"`) ; flèches mot par mot, Page précédente / suivante lettre par lettre, Entrée pour ouvrir.
- **Sans script** : les 26 lettres restent des liens vers les pages de lettre.

## 4. L'argument de l'accueil

| # | Affirmation | Preuve | Section |
| --- | --- | --- | --- |
| 1 | C'est le *Dictionnaire de Bitcoin*, et on y cherche un mot tout de suite. | La jaquette dépliée du livre, le champ de recherche sur la couverture. | **Jaquette** (héros, bleu nuit) |
| 2 | Chaque jour, un mot. | Le mot du jour en cartouche, avec sa définition. | **Le mot du jour** |
| 3 | Les 1 408 mots tiennent dans une tranche. | La tranche interactive. | **Feuilleter** |
| 4 | Dix-neuf domaines, du minage à la cryptographie. | Index typographique : nom, nombre, trois mots par catégorie. | **Les catégories** |
| 5 | Le dictionnaire existe aussi sur papier. | Le livre en volume, six vraies pages, les ISBN, le PDF gratuit. | **Le livre** |
| 6 | C'est un projet ouvert, écrit par Loïc Morel. | Portrait, sa phrase du README, les contributeurs, GitHub. | **Un projet ouvert** |
| 7 | Toutes les lettres, partout. | L'alphabet A–Z en grand, animé, dans le pied de chaque page. | **Le dos** (pied, bleu nuit) |

Le bleu nuit n'apparaît qu'aux deux bouts, comme sur un livre : la jaquette en tête, le dos en pied. Tout l'intérieur est sur papier.

## 5. Palette

Une impression en deux encres sur un papier, plus un or de dorure réservé aux états (ce qu'on vise, ce qu'on sélectionne, ce qui correspond) : un trait sous les noms survolés, le fond des correspondances de recherche. Jamais un aplat de décor.

| Rôle | Nom | Hex |
| --- | --- | --- |
| Fond des pages | Papier | `#F4F3F0` (pierre claire, l'os du titre éclairci et désaturé) |
| Pas de ton | Sable | `#E3DFD6` |
| Encre | Bleu nuit | `#193042` (la couverture ; `#193040` pour les fonds pleins, la valeur que l'image de l'arbre restitue) |
| Encre douce | Ardoise | `#4F5F6E` (notes secondaires seulement) |
| Texte sur bleu nuit | Os | `#ECEAE5` (le titre imprimé) |
| Trait sur bleu nuit | Gravure | `#A9BAC8` (l'arbre) |
| Surface sur bleu nuit | Lavis | `#22405A` |
| États | Or de dorure | `#E9C46A` (remplace le surligneur fluo après la première relecture, voir revue.md) |

| Texte / fond | Rapport | Niveau |
| --- | --- | --- |
| Bleu nuit sur Papier | 12,27 | AAA |
| Bleu nuit sur Sable | 9,96 | AAA |
| Ardoise sur Papier | 5,93 | AA |
| Ardoise sur Sable | 4,81 | AA |
| Os sur Bleu nuit | 11,33 | AAA |
| Gravure sur Bleu nuit | 6,83 | AA |
| Os sur Lavis | 8,97 | AAA |
| Bleu nuit sur Or | 8,15 | AAA |
| Papier / Sable (pas de ton) | 1,23 | visible sans filet |

Boutons : Bleu nuit plein, texte Os, sur papier ; Os plein, texte Bleu nuit, sur bleu nuit.

**Mode sombre** (préférence système, interrupteur dans la barre) : fond `#0E1A24`, surfaces `#1F3548` (pas de ton 1,39), texte Os (14,67), notes Gravure (8,85), cartouche inversé (fond Os, texte Bleu nuit), surligneur inchangé. La jaquette et le dos restent `#193042` (1,29 contre le fond) : le livre garde ses deux bouts.

## 6. Typographie

Le livre a déjà son système : Computer Modern sur la couverture, une grotesque grasse pour les vedettes et le texte à l'intérieur.

- **CMU Serif Roman** (`fonts/cmunrm.ttf` du dépôt, OFL) : titre de la jaquette, vedette (h1) des définitions, grandes lettres, titres de section, alphabet du pied, logotype de la barre. Jamais sous 19 px (logotype), 36 px pour les titres. Approche −0,01 em.
- **Host Grotesk** (Element Type, OFL) : tout le reste. Romain variable (400–700) et italique 400, limités à l'alphabet latin. Les noms de termes dans les listes, renvois et cartouches sont en Host Grotesk 600 capitales (c'est la forme des titres dans les données et dans le livre), à 17 px ou plus, sans espacement ajouté.
- **Code** : chasse fixe du système, uniquement dans `<code>` et `<pre>`.
- **Formules** : KaTeX composé au build.

| Pas | Taille | Police | Usage |
| --- | --- | --- | --- |
| Affiche | vedette : de 28 px à 128 px, calculée sur la longueur du mot ; titre de jaquette et grandes lettres : jusqu'à 200 px | CMU | h1 |
| Titre | `clamp(36px, 4.6vw, 64px)` | CMU | h2 de section |
| Énoncé | `clamp(21px, 1.9vw, 28px)` | Host 400 | Phrases d'appui, aperçu de la tranche |
| Lecture | `clamp(17px, 0.6vw + 13px, 20px)`, interligne 1,62 | Host 400 | Corps des définitions |
| Note | 15 px (14 px au plus petit) | Host 500 | Compteurs, fil d'Ariane, crédits |

Lecture : 62 à 68 caractères par ligne, alignée à gauche, `hyphens: auto`. Les vedettes : taille en unités de conteneur, calculée au build depuis la longueur totale et le mot le plus long, coupures permises après `_` et `-`, plafond 128 px, plancher 28 px ; deux lignes au plus partout.

## 7. Grille et espace

- 12 colonnes, marges extérieures `clamp(20px, 2.4vw, 32px)` égales, gouttière `clamp(16px, 1.6vw, 24px)`.
- Base 8 : 8, 16, 24, 32, 48, 64, 96, 128, 160. Entre sections : 128 à 160 px sur ordinateur, 96 sur téléphone ; dans une section, 48 au plus.
- Coins carrés. Boutons pleins rectangulaires de 48 px (56 sur la jaquette) ; cibles tactiles de 44 px minimum.

## 8. Composants communs

- **Barre** : la feuille du dos + « DICTIONNAIRE DE BITCOIN » (CMU 19 px) ; « Lettres », « Catégories », « Le livre » ; bouton de recherche (loupe + « Rechercher » + `Ctrl K`) ; interrupteur clair / sombre. Fond plein, pas de flou. Elle se cache quand on descend, revient dès qu'on remonte. Sur l'accueil, le bouton de recherche n'apparaît qu'une fois le champ de la jaquette sorti de l'écran (le champ « se range » dans la barre).
- **Mots-repères** (pages de définition) : sous la barre, « ← UTREEXO · U · UTXO SET → » : le mot précédent et le suivant dans l'ordre du livre, la lettre au centre, chacun un lien.
- **En-têtes collants** (listes) : la lettre ou les deux premières lettres du groupe (« BI ») restent en haut de l'écran tant qu'on est dans le groupe ; dans la catégorie BIP, des groupes par centaine (BIP-0001 à 0099, 0100 à 0199…).
- **Cartouche** : le nom du terme en Host Grotesk 600 capitales, Os sur Bleu nuit, comme les vedettes du livre. Mot du jour, résultat actif de la recherche.
- **Étiquettes** : catégorie (pictogramme + nom) et terme anglais, en blocs Sable pleins.
- **Renvoi** : nom en Host 600 capitales, description en dessous ; au survol, le surligneur glisse derrière le nom (de gauche à droite, 240 ms).
- **Pictogrammes** : à la taille du texte (18 à 24 px), jamais en grand ; les symboles nécessaires sont intégrés dans la page (aucune requête).
- **Recherche** : fenêtre (bureau) ou feuille plein écran (téléphone), champ de 64 px, résultats à chaque frappe, correspondances surlignées, clavier complet, état vide utile, « aucun résultat » qui propose les mots proches. Moteur sans accents ni casse : début du titre, début d'un mot, terme anglais, description, puis fautes de frappe (distance 1 ou 2).
- **Le dos (pied de page)** : sur Bleu nuit, l'alphabet A–Z en capitales CMU sur toute la largeur (13 × 2 sur ordinateur, 7 × 4 sur téléphone, cibles de 44 px au moins) ; chaque lettre est un lien vers sa page ; au survol, elle monte et se remplit de surligneur, et son nombre de mots apparaît. Dessous : liens, licence, crédits des polices.

## 9. Gabarits

### Accueil

```
┌─────────────────────────────────────────────────────────────────┐ Bleu nuit, 100svh
│ ❦ DICTIONNAIRE DE BITCOIN        Lettres Catégories Le livre  ◐ │
│ ┌────────────────────┐┌─┐┌──────────────────────────────────────┐│
│ │ (dos)              ││❦││  ░▒▒▒▒▒▒▒▒ arbre gravé ▒▒▒▒▒▒▒▒▒░    ││
│ │ Plus de 1 400      ││D││   DICTIONNAIRE                       ││
│ │ définitions…       ││I││   DE BITCOIN        (h1, CMU)        ││
│ │ Un projet ouvert…  ││C││  Tout le vocabulaire technique…      ││
│ │ Un ouvrage rédigé  ││T││            ▒▒▒▒                      ││
│ │ par Loïc Morel…    ││.││ [ Chercher un terme…      ][Chercher]││
│ │                    ││ ││        Loïc Morel, édition 2026      ││
│ └────────────────────┘└─┘└──────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
│ Le mot du jour  ██ TAPROOT ██  [Protocole] [EN …]  définition…  │ Papier
│                 [Lire la définition] [Un autre mot]             │
├─────────────────────────────────────────────────────────────────┤
│ Feuilleter les 1 408 mots          APERÇU DU MOT VISÉ (grand)   │
│ [A][   B   ][ C ][D][E][F]…[S]…[Z]   ← 26 blocs-lettres         │
│ ||||||||||||||||||||||||||||||||||||  ← traits de la lettre     │
├─────────────────────────────────────────────────────────────────┤
│ Les catégories   ⚙ Protocole 168  UTXO, NONCE, …                │ Sable
│ (3 colonnes)     ⚡ Lightning 134  CANAL, HTLC, …                │
├─────────────────────────────────────────────────────────────────┤
│ Le livre  [livre en volume]  texte, Commander, PDF, ISBN        │ Papier
│ ▯ ▯ ▯ ▯ ▯ ▯  six vraies pages, sur Sable, coupées par le bas     │
├─────────────────────────────────────────────────────────────────┤
│ Un projet ouvert [portrait] « Je gagne une petite marge… »      │ Papier
├─────────────────────────────────────────────────────────────────┤
│  A  B  C  D  E  F  G  H  I  J  K  L  M        (CMU, grandes)    │ Bleu nuit : le dos
│  N  O  P  Q  R  S  T  U  V  W  X  Y  Z                          │
│  liens · licence · polices                                       │
└─────────────────────────────────────────────────────────────────┘
```

- **Jaquette** (ordinateur) : la jaquette du livre dépliée, à plat. À gauche le dos (les trois paragraphes réels de la quatrième de couverture), au centre la tranche étroite (feuille + titre vertical), à droite la couverture : l'arbre extrait à 300 ppp, le h1 posé exactement où le titre imprimé a été effacé (ce qui masque la retouche), le sous-titre, le champ de recherche sur le tronc, « Loïc Morel, édition 2026 ». **Téléphone** : la couverture seule, plein écran ; le texte du dos passe sous le champ. Toucher le champ ouvre directement la feuille de recherche.
- **Le mot du jour** : le titre de section (h2) « Le mot du jour », puis le cartouche, les étiquettes, la description, « Lire la définition » et « Un autre mot » (les lettres du nouveau mot roulent en place).
- **Feuilleter** : comme décrit en section 3.
- **Les catégories** : index typographique sur Sable, trois colonnes sur ordinateur, une sur téléphone ; chaque ligne : pictogramme à la taille du texte, nom, nombre, trois mots de la catégorie (liens). Au survol, la ligne passe au papier et le nom se surligne.
- **Le livre** : le livre en volume (le rendu du dépôt, sur son fond bleu nuit, recadré), deux paragraphes, « Commander chez Bitcoin Bazar » (bouton), Amazon et PDF (liens), ISBN ; en dessous, six pages réelles du PDF debout sur un bandeau Sable, hauteurs différentes, coupées par le bas, qui montent à des vitesses légèrement différentes au défilement.
- **Un projet ouvert** : portrait, la phrase réelle du README, comment contribuer (un dossier par définition), les cinq contributeurs GitHub, licence, Lightning.

### Définition (`/<slug>/`)

```
┌──────────────────────────────────────────────────────────────┐ Papier
│ ❦ DICTIONNAIRE DE BITCOIN               Lettres …     ⌕  ◐  │
│ ← UTREEXO                U                    UTXO SET →     │ mots-repères
│ UTXO                                  (h1 CMU, ≤ 128 px)     │
│ [⚙ Protocole]  [EN Unspent Transaction Output]               │
│                                                              │
│ Corps de lecture (col. 1–7, 62–68 car.)  │ Termes associés    │
│                                          │ (col. 9–12, collant)│
│                                          │ UTXO SET …         │
│ Renvoient ici : BATCHED SPENDING, BIP-0064, …                 │
│ À la suite dans le dictionnaire : UTXO SET, V3 TRANSACTIONS  │
│ ┌───────────────────────────┬───────────────────────────┐    │
│ │ ← UTREEXO                 │                 UTXO SET → │    │ page tournée
│ └───────────────────────────┴───────────────────────────┘    │
│ Entrée 1 312 sur 1 408 · Proposer une correction sur GitHub   │
├──────────────────────────────────────────────────────────────┤
│ le dos : A … Z                                               │
└──────────────────────────────────────────────────────────────┘
```

Une seule logique de « suivant » : l'ordre alphabétique du livre (mots-repères en haut, page tournée en bas, flèches ← → du clavier). Sous chaque définition, les deux entrées suivantes en abrégé, ce qui remplit aussi l'espace sous les définitions courtes. Tablette et téléphone : une colonne, renvois après le corps.

### Lettre (`/lettre/<l>/`)

Une très grande capitale CMU, le nombre de mots, la plage (« de ACINQ à AXOLOTL »), lettres voisines. Puis la liste : en-têtes collants par deux lettres quand la lettre compte plus de 40 mots ; chaque ligne : nom (Host 600 capitales), pictogramme et catégorie, une ligne de description.

### Catégorie (`/categorie/<slug>/`)

Sur papier : pictogramme (48 px), nom en CMU (h1), nombre, description tirée de `templates/categories.yaml`, alphabet de la catégorie (lettres absentes atténuées). Liste groupée par lettre avec en-têtes collants ; BIP groupé par centaines.

### Recherche (`/recherche/` et la fenêtre)

La fenêtre s'ouvre depuis toutes les pages (`Ctrl K`, `⌘ K`, `/`, bouton). La page `/recherche/?q=` reprend le moteur en pleine page avec un filtre par catégorie ; sans script, elle renvoie vers les lettres.

### 404

Bleu nuit, la couverture (arbre), « Ce mot n'est pas dans le dictionnaire », puis « Vouliez-vous dire… » : les trois mots les plus proches de l'adresse demandée, calculés sur place. Champ de recherche, mot au hasard.

## 10. Système de mouvement

Le mouvement sert la lecture : il montre d'où vient une chose, confirme un geste, garde le fil entre deux pages. Il ne cache jamais un mot plus de 300 ms.

```css
--ease-out: cubic-bezier(0.22, 1, 0.36, 1);
--ease-expo: cubic-bezier(0.16, 1, 0.3, 1);
--ease-in-out: cubic-bezier(0.76, 0, 0.24, 1);
--ease-soft: cubic-bezier(0.33, 1, 0.68, 1);
--t-press: 140ms; --t-hover: 180ms; --t-ui: 240ms; --t-reveal: 800ms; --t-open: 1100ms;
--stagger-line: 90ms; --stagger-item: 60ms;
```

1. **Moment signature, la jaquette se grave** : au chargement, l'arbre se révèle des racines vers la ramure (masque de bas en haut, 1,1 s), les deux lignes du titre montent de leur ligne de base, le champ arrive ; tout est lisible avant 900 ms. Au défilement, l'arbre dérive lentement (moins de 6 % de sa hauteur) et le champ se range dans la barre.
2. **Lettres animées** : l'alphabet du pied monte lettre par lettre à son entrée (30 ms d'écart) et réagit au survol ; la grande lettre des pages de lettre se pose (montée masquée) ; « Un autre mot » fait rouler les lettres du nouveau mot en place.
3. **Transitions entre pages** (View Transitions entre documents ; ailleurs, navigation normale) : depuis une liste ou un renvoi, le nom cliqué se transforme en vedette ; « précédent / suivant » tourne la page (l'ancienne glisse à gauche, la nouvelle arrive de droite, 450 ms, in-out) ; le reste se fond en 200 ms. Pas de seconde animation de vedette après une transition.
4. **Vedette** : visible dès la première image ; elle se pose de 0,12 em en 500 ms (opacité pleine, pour ne pas retarder le LCP).
5. **Entrées de section, une fois, chacune la sienne** : le cartouche du mot du jour s'ouvre de gauche à droite, les blocs-lettres de la tranche se dressent l'un après l'autre, les lignes des catégories arrivent ligne par ligne, les pages du livre montent à des vitesses différentes.
6. **Retours sous la main** : boutons qui s'enfoncent (0,97), surligneur derrière les noms survolés, lignes d'index qui changent de fond, lettres du pied qui montent.

**Mouvement réduit** : aucune transformation animée, aucune transition entre pages, tout visible d'emblée ; la tranche reste manipulable. **Sans JavaScript** : tout est visible et lisible ; les états cachés n'existent que sous `html.js`.

## 11. Interactions souris et tactiles

| Élément | Souris et clavier | Doigt |
| --- | --- | --- |
| Champ de la jaquette | Saisie : résultats sous le champ ; ↑ ↓ Entrée | Toucher : feuille de recherche plein écran, clavier ouvert |
| Tranche | Survol d'un bloc-lettre : ses traits se déploient ; survol d'un trait : surligné, aperçu ; clic : ouvre ; flèches, Page préc./suiv., Entrée | Défilement natif sous l'aiguille, aperçu à toucher, lettres-raccourcis |
| Mot du jour | « Un autre mot » : lettres qui roulent | Même bouton, 48 px |
| Index des catégories | Ligne survolée : fond papier, nom surligné | Appui : fond papier immédiat |
| Renvois et listes | Surligneur qui glisse derrière le nom ; focus identique | État appuyé immédiat |
| Mots-repères et page tournée | ← → au clavier ; transition de page tournée | Grandes cibles pleine largeur |
| Recherche | `Ctrl K`, `⌘ K`, `/` ; ↑ ↓ Entrée Échap | Feuille plein écran, cibles de 56 px |
| Alphabet du pied | Lettre survolée : monte, se remplit, montre son nombre | Appui : même état, puis la page de la lettre |

## 12. Images (toutes tirées du projet)

1. **L'arbre gravé** de la couverture, extrait à 300 ppp (2 351 × 3 425 px) du PDF de la jaquette, titre effacé, sur le bleu nuit exact, en AVIF et WebP (40 à 93 Ko).
2. **La feuille de la tranche**, vectorisée, en masque teintable et en favicon.
3. **Le livre en volume** : le rendu de `assets/images/cover.png`, fond ramené au bleu nuit.
4. **La couverture à plat** et **six pages intérieures** rendues depuis les PDF.
5. **Le portrait de Loïc Morel**.
6. **Les 19 pictogrammes**, retracés en SVG d'un seul tracé (0,7 à 10 Ko).
7. **Les 53 schémas** des définitions.

Manque (à demander à Loïc, non bloquant) : de vraies photos du livre imprimé (en main, ouvert, sur la tranche). Le rendu 3D en tient lieu.

## 13. Budget de performance (pages de définition)

HTML de moins de 30 Ko ; CSS d'environ 25 Ko (7 Ko compressé) ; un script différé de moins de 10 Ko ; deux polices préchargées (CMU 26 Ko, Host Grotesk 20 Ko) ; aucune image hors schémas ; pictogrammes intégrés. Objectif Lighthouse mobile : 95 ou plus en performance et en accessibilité. L'index de recherche (environ 230 Ko, 60 Ko compressé) se charge à la première ouverture de la recherche ou à l'approche de la tranche.

## 14. Annexe : la critique de la version 1 et ce que j'en ai fait

Note donnée à la version 1 : potentiel 6/10, utilisabilité 5/10, originalité 6/10.

| Objection | Décision |
| --- | --- |
| Bleu nuit + jaune `#FFD93D` évoque Binance ; surfaces indiscernables (1,11). | **Adoptée.** Papier chaud tiré de l'os du titre, pas de ton 1,23, surligneur fluo `#E4FF5A` réservé aux états. Bleu nuit aux deux bouts seulement. |
| Computer Modern partout, c'est la version refusée ; le livre met ses vedettes en grotesque. | **Adoptée.** CMU pour les titres, la vedette h1, les grandes lettres et l'alphabet ; listes, renvois et cartouches en Host Grotesk 600 capitales. Vedettes plafonnées à 128 px, plancher 28 px. |
| La couverture pivotante épinglée date (turn.js) et cache la recherche. | **Adoptée.** Plus d'épinglage. Révélation au chargement, champ qui se range dans la barre ; à la place, la jaquette dépliée (dos, tranche, couverture) comme héros. |
| L'onglet du bord droit gêne les gestes du téléphone et la barre de défilement. | **Adoptée.** Supprimé ; la lettre des mots-repères est un lien. |
| Trop d'idées, trois motifs à rayures (tranche, dos de volumes, code-barres) ; logotype à points de Bézier repris d'Ascend. | **Adoptée.** Dos de volumes, code-barres et logotype supprimés. Alphabet A–Z animé dans le pied de chaque page ; catégories en index typographique. |
| « Le mot du jour » posé au-dessus du cartouche est un surtitre. | **Adoptée.** C'est maintenant le titre de la section (h2, taille Titre). |
| Tranche inutilisable à la souris (moins d'un pixel par trait). | **Adoptée.** Deux niveaux (blocs-lettres puis traits espacés de 4 px), racine carrée, pas d'œil-de-poisson ; téléphone en défilement natif sous aiguille. |
| Page de définition : colonne « Fiche » redondante, vide sous les définitions courtes, deux ordres de « suivant ». | **Adoptée.** Deux colonnes, ordre alphabétique partout, les deux entrées suivantes en abrégé ; pas d'animation de vedette après une transition, vedette jamais masquée. |
| Mots-repères dans une barre qui se cache. | **Adoptée.** En-têtes collants dans les listes ; mots-repères sous la barre, dans la page, sur les définitions. |
| Une seule vraie photo ; arbre trop petit et retouché. | **Adaptée.** Arbre réextrait à 300 ppp ; le h1 couvre la zone retouchée. Les photos du livre imprimé sont listées comme ressource manquante (non bloquant) ; le rendu 3D, la couverture et six pages du PDF tiennent lieu. |
| Pictogrammes génériques et lourds. | **Adoptée.** Retracés (0,7 à 10 Ko), utilisés à la taille du texte, intégrés dans la page. |
| Mode sombre qui efface la métaphore. | **Adoptée.** Fond `#0E1A24`, surfaces `#1F3548`, cartouche inversé ; jaquette et dos restent bleu nuit. |
| BIP : 195 entrées sous B ; polices trop optimistes. | **Adoptée.** Groupes par centaine ; romain variable et italique 400, sous-ensemble latin. |

## 15. Après la première relecture du site

La relecture indépendante des gabarits construits (voir `revue.md`) a fait changer : l'accent fluo, remplacé par un or ; le mot du jour, qui quitte son bandeau pour le dos de la jaquette ; un menu pour la navigation sur téléphone ; des renvois dans le texte des définitions.

## 16. Passage à la charte de l'édition 2027 (25 octobre 2026)

Loïc a demandé que le site prenne dès maintenant l'identité de l'édition 2027, fixée dans `design/charte-2027.md` (branche feat/couverture-2027, commit f5a3a13b). Elle remplace les sections 5, 6 et 12 ci-dessus ; le concept (« le livre ouvert » : jaquette, tranche, pages, signet) ne change pas.

- **Couleur** : Figue `#AA226A`, Figue sombre, Canopée, Figue vive, Figue claire et Nuit pour le mode sombre, Rose, Brume, Encre, Écorce, Galet. Toutes dans `palette` (`config.mjs`) ; le build écrit les jetons CSS. Contrastes de la charte gardés : Blanc sur Figue 6,67, Encre sur Blanc 17,20, Écorce sur Blanc 5,82, Figue claire sur Nuit 7,30. Paires ajoutées et vérifiées : Rose sur Figue 4,87 (texte court seulement), Blanc sur Canopée 13,50, Brume sur Figue sombre 10,19. Aucune paire interdite par la charte n'est utilisée.
- **Proportions** : Blanc domine. La Figue sert aux liens (toujours soulignés), au bouton principal, à la jaquette de l'accueil et au bandeau de la 404 ; le pied de page est en Canopée.
- **Caractères** : Archivo pour tout (Titre 75 / 800 pour les titres et vedettes, Vedette 75 / 750 pour les noms dans les listes, Couverture 62 / 900 pour le titre de la jaquette, les lettres et l'alphabet), Atkinson Hyperlegible Mono pour le code. Un seul fichier variable réduit au latin (69 Ko), préchargé. Computer Modern et Host Grotesk sont retirés.
- **La jaquette** : le banian de la couverture 2027, calculé par le générateur de la couverture (`banyan.py`, graine du bloc de genèse), rendu sans ses textes par `tools/jaquette-2027.py` en deux calques (couronne, racines). Le titre du site est composé en HTML exactement à la place où la couverture l'imprime : les racines se posent sur ses lettres, et les trois piliers sur les trois I de « DICTIONNAIRE ». Au chargement, les racines descendent de la couronne puis le titre monte.
- **Favicon** : un carré Figue et trois barres blanches, les trois piliers.
- **Schémas** : posés sur le fond ; en mode sombre, sur une carte blanche de 16 px ; sous 640 px, 640 px de large dans un cadre qui défile, et un lien « Agrandir le schéma ».
- **Restent de 2026** : les 19 pictogrammes (la charte en prévoit de nouveaux, pas encore dessinés) et les pages et la vidéo du livre imprimé (l'édition 2026 est la seule parue).

## 17. Charte officielle et teinte validée (26 octobre 2026)

Loïc a validé la Figue `#AA226A` pour l'édition 2027. La référence devient `charte-officielle.md`. Vérifié valeur par valeur : les 14 couleurs écran de `config.mjs` sont celles de sa palette, et les rôles du mode sombre suivent son tableau (fond Nuit, surface `#3B1026`, texte Brume, texte secondaire `#A8979F`, liens et bouton en Figue claire, focus Figue claire). Aucune paire interdite n'est utilisée. Seul écart corrigé : les ombres portées (bouton « Haut », barres collantes, carte d'aperçu, loupe, fenêtre de recherche), que la charte exclut, sont remplacées par un filet Galet.


## 18. Édition 2027 : l'Allée des baobabs, les nouveautés et l'anglais (27 octobre 2026)

La couverture validée remplace le banian : l'Allée des baobabs au couchant (*Adansonia grandidieri*), sur fond Figue. Le concept « Le livre ouvert » ne change pas, la jaquette dépliée reste l'entrée du site.

- **La jaquette** : l'avant reprend la première du broché, mesure pour mesure (sol à 61 % de la hauteur, allée sur 80,6 % de la largeur, titre en Archivo 62/900). Les baobabs viennent du générateur de la couverture (`baobab.py`, même graine) par `tools/allee.py`, en SVG dans la page, un calque par arbre. Au chargement, le soleil se lève, les trois baobabs du fond poussent l'un après l'autre, puis le grand ; le titre monte de sa ligne. Souris : chaque plan suit le pointeur selon sa distance. Doigt : le soleil descend derrière l'horizon quand on fait défiler la page. Rien de tout cela avec `prefers-reduced-motion`. Le dos porte la recherche et le mot du jour ; sur téléphone, ils passent sous l'avant, en section blanche.
- **Les nouveautés** : une rangée de cartes sur l'accueil (chronologie, spécifications, personnes, entreprises, schémas), dont les chiffres viennent des fichiers. La chronologie tient sur une page, avec une frise des années (une barre par année, sa hauteur suit le nombre de dates) et une barre des années collante. Les spécifications ont une page par série, filtrable par statut ; la définition d'un document affiche sa fiche dans la marge, et les dates qui la concernent sous le texte.
- **Les parties du livre** remplacent les « dix-neuf catégories » : technique, écosystème, personnes, chacune avec ses catégories et leurs pictogrammes 2027.
- **L'anglais** : un bouton FR / EN dans la barre mène à la même page dans l'autre langue. Une définition pas encore traduite s'affiche en français sous un encadré « In French for now », marqué `lang="fr"`.

## 19. Épuration avant la mise en ligne (1er novembre 2026)

Loïc n'était « vraiment pas satisfait » de l'interface : trop d'éléments, et une jaquette dépliée qui rendait mal selon l'écran (titre de la tranche rogné, texte qui sortait du dos sur téléphone, couverture seule et sans recherche sur tablette, objet réduit au centre d'un grand écran). Le concept « le livre ouvert » reste dans les pages (mots-repères, signet, pages tournées, lettres) ; l'accueil le dit plus simplement. Cette section remplace la jaquette des sections 4, 9 (Accueil), 10.1, 16 et 18.

- **La couverture** remplace la jaquette dépliée : un bandeau Figue pleine largeur sous la barre. À gauche le titre de la couverture 2027 (Archivo 62/900, en capitales, réglé sur la largeur de sa colonne en unités de conteneur : « DICTIONNAIRE » mesure 5,35 em et tient donc sur sa ligne à toutes les tailles), le sous-titre en Rose, le champ de recherche (56 px, bouton Canopée) et une ligne « 1 536 définitions libres et gratuites, par Loïc Morel. Édition 2027. ». À droite, l'Allée des baobabs posée sur un sol Canopée qui court sur toute la largeur du bandeau. Sous 720 px, l'allée passe au-dessus du titre, comme sur le livre, et le champ reste dans le premier écran dès 320 px. Plus de dos, de tranche verticale, de parallaxe au pointeur ni de soleil qui se couche au défilement : au chargement seulement, le titre monte de sa ligne, le soleil se lève et les baobabs poussent (rien avec `prefers-reduced-motion`).
- **Le mot du jour** sort de la jaquette : une section blanche, le titre à gauche avec « Un autre mot » (à côté du titre sous 1 024 px, dessous au-delà : le bouton ne bouge pas quand le mot change ; le nouveau mot monte d'un bloc, avec son soulignement), et à droite le mot, sa catégorie, sa définition courte et « Lire la définition ».
- **Nouveau en 2027** devient un sommaire (une ligne par contenu : son nom, puis ce qu'il contient) au lieu d'une mosaïque de cartes roses.
- **Retirés** : les trois mots cités sous chaque catégorie de l'index, la rangée des quatre pages du livre, le grand alphabet animé du pied sur l'accueil (le pied compact sert partout), l'aperçu et la tranche des pages de lettre (la tranche reste sur l'accueil et en signet des définitions), les fondus en dégradé des rangées qui défilent.
- **Barre** : le bouton de langue montre seulement l'autre langue (« EN » sur une page française, « FR » sur une page anglaise). La loupe vient juste après la marque, avant la navigation : tant que le champ de la couverture (ou celui de la page de recherche) est à l'écran, elle s'efface et sa place se fond dans l'espace libre. Entre 1 024 et 1 279 px, elle se réduit à l'icône pour que la navigation tienne sur une ligne ; sous 480 px, l'interrupteur de thème passe dans le menu. Le raccourci `Ctrl K` n'est montré qu'avec une souris, dès 1 280 px.
- **Le menu** (sous 1 024 px) : un en-tête collant (« Parcourir » et Fermer), la recherche, une liste de liens (Accueil, Chronologie, Spécifications, Le livre imprimé, l'autre langue, le thème sous 480 px), l'alphabet en 7 colonnes, puis les catégories repliées par partie (`<details>`, une ligne de 52 px par partie avec son effectif et un chevron).
- **Rangées de pastilles** (lettres d'une catégorie, groupes d'une lettre, filtres de recherche) : sur téléphone, portrait ou paysage, une ligne qui défile bord à bord, avec la place de l'anneau de focus ; ailleurs, elles tiennent entières (lettres en 13 colonnes de 640 à 1 279 px, une ligne au-delà). Les en-têtes de groupe collent juste sous la rangée, dont la hauteur est mesurée (`--rangee`) ; un clic sur une pastille range la barre et pose le groupe 16 px sous la rangée.
- **Alphabets** : 7 colonnes sur téléphone, 6 sous 360 px pour garder des cases de 44 px, 13 dès 640 px (tranche « Feuilleter » comprise, au doigt comme à la souris).
- **Boutons secondaires** (« Un autre mot », « Citer cette définition ») : un contour de 2 px à la couleur du texte, sans fond ; le bouton principal reste plein, Figue.
- **Définition** : le texte vient avant la marge dans le HTML (le clavier et les lecteurs d'écran lisent la définition d'abord) ; dès 1 024 px, la marge (signet, termes associés) est à droite et ne colle plus au défilement. Une définition de moins de 360 caractères sans schéma s'affiche au corps de l'énoncé. L'étiquette « En anglais » n'a plus de fond : seule la catégorie, qui est un lien, en garde un. Un bloc de code plus large que la colonne déborde jusqu'au bord sur téléphone et porte un filet Figue à droite tant qu'il reste à voir. La ponctuation qui suit une formule ne part jamais seule en début de ligne.
- **Page lettre** : le titre reprend la taille des titres de section ; plus de lettres voisines ni d'aperçu, la rangée de l'alphabet suffit.
- **Index des catégories** : seul le nom est souligné, pas l'effectif ; 3 colonnes de 1 024 à 1 279 px, 4 au-delà ; sous 1 280 px chaque partie prend toute la largeur.
- **États** : chaque cible qui réagit au survol réagit aussi à la pression du doigt (`:active`). La loupe des schémas garde les couleurs du thème clair (le schéma est dessiné sur blanc), boutons et anneau de focus compris, et centre le schéma verticalement.
- **Barre et clavier** : quand le défilement vient du focus (Tab, Maj+Tab), la barre garde son état, rangée ou visible ; la page a placé l'élément sous la pile collante d'après la hauteur de la barre, qui ne doit pas revenir le recouvrir. En haut de page (200 px), elle est toujours là. Les flèches ← → changent de mot, sauf dans un bloc qui défile en largeur (code, schéma ; focus ou dernier clic dedans), qu'elles font défiler.
- **Chronologie** : la rangée des années suit la règle des rangées (une ligne qui défile sur téléphone ; ailleurs entière, en cases égales, « Avant 2009 » sur deux cases : deux lignes équilibrées, puis une seule dès 1 120 px) et marque l'année lue, comme les lettres ; sa hauteur mesurée règle les ancres. La barre « <2009 » de la frise prend deux parts. Les liens « Voir aussi » et « Sources » sont soulignés de leur couleur et font 44 px de haut au doigt (de même pour les liens des fiches de spécifications).
- **Spécifications** : autant de colonnes que de séries ; l'effectif d'une carte reste lisible au survol. La grille des numéros (214 BIP) ne colle qu'en rangée d'une ligne, sur téléphone ; sur grand écran, où elle passe sur plusieurs lignes, elle reste en place. Elle marque la fiche lue. Le filtre de statut masque aussi les numéros et les séries sans fiche ; les statuts gardent le vocabulaire anglais des BIP (« Actif » des BOLT devient Active, « Retiré » Closed). Les références des résumés et de la chronologie ne se coupent pas. Au doigt, les liens isolés d'une fiche (définition, remplace, lire le document) et de la chronologie ont une zone de 44 × 44 px sans que rien ne bouge : 12 px de marge intérieure en haut et en bas (le texte garde sa ligne de base, ses espaces et son soulignement continu ; au doigt, les métadonnées passent à un pas de 44 px pour que deux zones empilées se touchent sans se chevaucher), et un nom court s'élargit par un `::after` centré, sans écarter ses voisins. Dans les rangées serrées (alphabets, années, tranche), la case qui a le focus passe au-dessus de ses voisines : son anneau reste entier.
- **Cibles courtes** : un lien dont le nom est très court (I2P, API) garde 44 px de large (nom de la tranche, mot voisin, pastilles « renvoient ici »). Dans la feuille de recherche, la souris choisit la ligne qu'elle survole : pas de second fond de survol à côté du choix clavier.
- **404** : « Chercher » mène à la première suggestion affichée ; sans suggestion, à la page de recherche ; champ vide, rien.
- **Pages courtes** : le pied reste au bas de l'écran ; sur la 404, la couverture remplit la hauteur libre. Le bouton « ↑ » (pages de liste) apparaît en remontant, 2,5 s : sur téléphone, où il peut couvrir une fin de ligne le temps d'un geste, et dès 1 392 px, centré dans la marge ; de 640 à 1 391 px, il couvrirait le texte, il n'existe pas.
- **Lettres** : chaque mot est rangé sous l'initiale de son titre, en français comme en anglais (« ALGORITHME DE GROVER », slug `grover-algorithme`, est en A) ; les adresses ne changent pas. La tranche « Feuilleter » reçoit cette lettre dans `tranche.json` : chaque lettre y a autant de traits que sa page, et la choisir pose l'aiguille sur son premier mot. Sa description tient en trois lignes, coupée au mot (une phrase entière qui tient finit sur son point), dans une hauteur réservée : la page ne saute pas au glissé. Les résumés des listes sont coupés au mot au build ; la limite de lignes du CSS ne sert que de filet et ne coupe jamais un mot.
- **Recherche** : dans un résultat, la partie trouvée passe à l'encre et le reste du nom reste Figue (pas de surlignage de fond, lisible sur la ligne sélectionnée et en sombre) ; les autres noms d'un terme ne répètent pas son titre. Une seule liste de résultats ; chaque filtre compte ses résultats et le filtre choisi la découpe. Un filtre qui n'a plus rien pour la nouvelle requête revient à « Toutes » ; le filtre choisi reste toujours visible. Changer de filtre ne reconstruit pas la rangée (le focus clavier reste). À la fermeture de la feuille, le focus revient là où il était ; ouverte depuis le champ de la couverture, ce qui a été tapé y revient, et un champ vidé (deuxième Échap, croix) ne la rouvre pas. Entrée sur une feuille vide ne fait rien. « Vos derniers mots » est tenu par langue : chaque lien mène à une page de la langue affichée.
- **Typographie au build** : une référence (« BIP-0347 », « RFC 8391 », « SHA-2 ») ne se coupe pas, les groupes de chiffres et « 51 % » restent ensemble (espace fine insécable), un nombre et son unité aussi, en toutes lettres ou en symbole, même quand l'unité est un renvoi (« 256 bits », « 2 000 vB », « 4 Mo », « 150 EH/s », « 100 000 octets virtuels » : espace insécable, `lib/typo.mjs`, cartes d'aperçu comprises), et en français une date (« 15 mars 2012 »), et en français la ponctuation haute et les guillemets prennent l'espace fine insécable ; de même pour l'index de recherche, les textes alternatifs des schémas (légende de la loupe) et les noms de catégorie (apostrophe ’). Les textes posés par le navigateur (résultats, mot du jour, tranche, 404, carte d'aperçu) appliquent la même règle des références. Un résumé coupé ne finit jamais sur un mot qui appelle une suite (mot-outil, élision, nombre, « permet », « sont », « tous », « being »…) : une seule liste, recopiée dans `lib/templates.mjs`, `static/js/site.js` et `static/js/accueil.js`, et `check.mjs` vérifie que les trois copies sont identiques.
- **La 404** reprend le bandeau de la couverture : le message, le champ, les mots proches, et l'allée.
- **Règles vérifiées par script à 12 largeurs (320 à 2 560 px)** : aucun défilement horizontal ni texte qui sort de sa boîte, contrastes de 4,5:1 au moins (clair et sombre), cibles tactiles de 44 px au moins sur téléphone (les liens dans une phrase exceptés), contour de focus visible sur chaque élément atteint au clavier. Avant chaque mise en ligne, trois relecteurs (téléphone, tablette, bureau) repassent les pages témoins en captures.
