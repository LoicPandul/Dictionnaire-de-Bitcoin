# Revue des gabarits

Chaque gabarit (accueil, définition, lettre, catégorie, recherche, 404) a été capturé en 390, 768 et 1440 px, mesuré par l'inspecteur du skill design-taste-frontend, critiqué par moi selon `references/critique.md`, puis noté sur 10 par un relecteur indépendant (un sous-agent qui n'a vu ni la direction ni mon raisonnement : seulement le brief de Loïc, les captures, les vidéos et le site en marche). Objectif : 8,5 au moins partout, en mobile et sur ordinateur.

## Mesures

- **Inspecteur** (1440, 768, 390 px) : 0 échec sur l'accueil. Sur les pages de lecture, il reste la règle « au moins quatre photos » et « une vidéo », écrite pour des pages vitrines : une page de définition, de lettre ou de recherche n'a pas de photo à montrer, et en inventer une serait de la décoration. Défendu, pas corrigé. Restent aussi « le h1 est un nom seul » sur la définition (c'est la vedette d'un dictionnaire ; la catégorie et « Entrée 1 346 sur 1 408 du dictionnaire » suivent dans le premier écran) et « la même grande ligne reste à l'écran » sur la lettre B (l'en-tête de groupe collant, voulu, comme un mot-repère).
- **Lighthouse mobile** (pages de définition, dernier build) :

  | Page | Performance | Accessibilité | Bonnes pratiques | SEO | LCP | CLS |
  | --- | --- | --- | --- | --- | --- | --- |
  | `/adresse-de-reception/` | 99 | 100 | 100 | 100 | 2,1 s | 0 |
  | `/utxo/` | 100 | 100 | 100 | 100 | 1,8 s | 0 |
  | `/adaptor-signature/` | 98 | 100 | 100 | 100 | 2,3 s | 0 |
- **Défilement horizontal** : aucun en 360, 390, 768, 1024 et 1440 px sur 15 pages types (dont les vedettes les plus longues, un tableau, un bloc de code, des formules).

## Tours de relecture

### Tour 1 (relecteur indépendant)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 6,5 | 7,0 |
| Définition | 6,0 | 7,0 |
| Lettre | 5,5 | 6,0 |
| Catégorie | 6,0 | 6,5 |
| Recherche | 6,5 | 6,5 |
| 404 | 7,0 | 7,0 |

Note globale : 6,5. « L'identité est juste et il y a des idées fortes (tranche, signet, Ctrl K). Mais les renvois, le classement de la recherche et la navigation sur mobile ne sont pas encore au niveau de la présentation. »

Ce qui a été corrigé après ce tour :

- **Navigation** : un menu plein écran sur téléphone et tablette (recherche, 26 lettres, 19 catégories, liens) ; une barre A–Z collante sur les pages de lettre et de catégorie ; un index des sous-groupes sur les grandes lettres ; « Lettre suivante » en bas de liste ; un sélecteur de catégorie sous le titre.
- **Renvois dans le texte** : 4 432 liens posés au build (première occurrence d'un terme du dictionnaire, termes associés toujours, autres termes seulement s'ils sont distinctifs), en pointillé, avec une carte d'aperçu au survol et au focus clavier.
- **Recherche** : le terme exact passe en tête (titre, première partie d'un titre composé, terme anglais), puis les débuts de titre et de mot ; à rang égal, le terme le plus renvoyé ; les correspondances au milieu d'un mot ne s'affichent que s'il y a peu de résultats ; « aucun résultat » propose le mot du jour, les lettres et les catégories ; Échap ferme la fenêtre.
- **Accueil** : le dos de la jaquette porte le mot du jour en Computer Modern (plus de bandeau, plus de titre en double) ; texte d'aide du champ raccourci.
- **Couleur** : l'or de dorure remplace le jaune-vert fluo ; au survol, un trait d'or glisse sous les noms au lieu d'un aplat.
- **Définition** : signet et termes associés dans une colonne qui commence en haut (plus de vide) ; schémas fondus dans le papier, inversés en mode sombre, agrandis en plein écran au clic ou au toucher ; mots-repères en cibles de 44 px ; transition de vedette sans fantôme ; « Citer » sur sa ligne, avec repli quand le presse-papiers est indisponible ; formules et code qui ne débordent plus sur téléphone.
- **Lettre** : listes compactes (nom et une ligne de définition, catégorie dans l'aperçu au survol), BIP sans pictogramme répété, grand aperçu de la tranche visible d'emblée, glissé au doigt sur téléphone avec la consigne adaptée.
- **Catégorie** : lettres absentes retirées, « Pour commencer » qui défile au doigt sur téléphone, présentation repliée à quatre lignes.
- **404** : fond de l'arbre aligné sur celui de la page (plus de rectangle), trois suggestions, champ prérempli avec le mot tapé.
- **Dos** : liens en grille, cibles de 44 px.

### Tour 2 (nouveau relecteur indépendant, avec le relevé du tour 1 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,0 | 7,5 |
| Définition | 6,5 | 7,5 |
| Lettre | 6,0 | 6,5 |
| Catégorie | 6,5 | 7,0 |
| Recherche | 6,0 | 6,0 |
| 404 | 7,0 | 7,5 |

Note globale : 6,8. Il confirme la plupart des corrections du tour 1 et relève : recherche multi-mots et « bip32 » sans résultat, premiers mots trop bas sur les pages de lettre et de catégorie, apparition au défilement qui laisse la liste vide après un saut, tranche illisible au doigt, titres hexadécimaux en capitales, définition mobile qui commence trop bas, fantôme résiduel de la transition, pied de page répété trop haut.

Ce qui a été corrigé après ce tour :

- **Recherche** : chaque mot cherché dans tous les champs ; « bip32 », « BIP 32 », « bip-0032 » ramenés à BIP-0032 ; étiquettes de catégorie avec le nombre de résultats, seulement celles qui en ont ; « aucun résultat » propose les mots les plus proches, les lettres et les catégories, aussi sur la page de recherche.
- **Lettre** : en-tête resserré en une bande (lettre, titre, tranche) ; sous-groupes sur une ligne qui défile (ordinateur) et en liste « Aller à » (téléphone) ; plus d'apparition au défilement sur les listes ; sujet des BIP affiché à côté du numéro (tiré des termes associés de l'auteur) ; trait visé de 4 px au moins ; loupe des 21 traits voisins au doigt ; bouton « Haut ».
- **Catégorie** : rayon des 19 catégories avec la courante en évidence (sélecteur sur téléphone) ; alphabet complet, lettres absentes à leur place en gris ; centaines des BIP dans la barre ; présentation repliée avec « Lire la suite » ; « Pour commencer » en liste courte sur téléphone.
- **Définition** : signet placé après le texte sur téléphone ; plus de transformation depuis les listes (la vedette se fond sur place, précédent et suivant tournent la page) ; renvois aussi sur les codes en ligne (`scriptPubKey`, SHA256…) ; schéma ouvert ajusté à la largeur avec « Agrandir » et pincement ; points de suspension rétablis.
- **Partout** : `0x` minuscule dans les titres hexadécimaux ; espaces fines insécables (guillemets, deux-points) ; plus de flash au toucher ; pied de page compact hors accueil ; voile neutre sous les textes posés sur l'arbre ; jaquette centrée, dos et couverture de même largeur ; fichier source réduit à `definition.md` avec lien vers GitHub ; 404 en recherche directe sous le champ, résultats avec extrait.
- **Couleurs** : toute la palette passe par `config.mjs` (préparation de la charte 2027), l'arbre s'adapte seul à la couleur de couverture.

### Tour 3 (nouveau relecteur indépendant, relevés des tours 1 et 2 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,0 | 7,5 |
| Définition | 6,5 | 7,5 |
| Lettre | 6,5 | 7,0 |
| Catégorie | 6,5 | 7,0 |
| Recherche | 6,5 | 7,0 |
| 404 | 7,0 | 7,0 |

Note globale : 6,9. Restaient surtout des incohérences de détail : quatre grilles d'alphabet différentes, hexadécimal repassé en capitales par la feuille de style, tirets qui cassent les titres de codes, fantôme résiduel de la transition, recherche (« satoshi », « hd wallet »), premiers mots trop bas sur les listes mobiles, menus déroulants natifs, arbre coupé net sur la 404.

Entre le tour 3 et le tour 4, **la charte de l'édition 2027 a été appliquée** (voir `direction.md`, section 16) : Figue, banian, Archivo, liens toujours soulignés, bouton Figue, blanc dominant. Corrigé en même temps :

- **Cohérence** : un seul composant d'alphabet (7 colonnes, 13 dès 640 px) pour le menu, le pied, la recherche et la tranche ; hexadécimal en « 0x » minuscule partout, plus aucune capitale forcée ; titres de codes avec un tiret demi-cadratin précédé d'une insécable (« OP_RETURN – 0x6A ») ; césure limitée (`hyphenate-limit-chars`).
- **Transitions** : plus de vedette partagée entre deux pages ; fondu enchaîné sans superposition, page tournée pour précédent et suivant.
- **Recherche** : bonus au mot exact du titre (« satoshi » donne SAT – SATOSHI en tête), synonymes courants (wallet, seed, 12 mots…), fautes de frappe limitées aux mots de même initiale, suggestions sur la page vide, titre à gauche du champ sur ordinateur, filtres en rangée qui défile au doigt (plus de menu déroulant).
- **Listes** : descriptions en 16 px pleine encre, petits groupes fusionnés dans les catégories (« J – L »), rayon des 19 catégories en une ligne qui défile, saut instantané avec « Aller à », bouton « Haut » discret et caché sur le pied, fondu sous les en-têtes collants.
- **Définition** : résumé du mot suivant tronqué au mot avec points de suspension, lettre jamais seule en fin de ligne, schémas à 640 px dans un cadre qui défile sur téléphone avec un lien « Agrandir le schéma » sous la figure.
- **404** : la jaquette entière en bandeau, la couronne court sur toute la largeur, le texte sous les racines courtes du dos.

### Tour 4 (nouveau relecteur indépendant, charte 2027 appliquée, relevés des tours 1 à 3 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,5 | 8,0 |
| Définition | 7,5 | 8,0 |
| Lettre | 7,0 | 7,5 |
| Catégorie | 7,0 | 7,5 |
| Recherche | 7,5 | 7,5 |
| 404 | 7,5 | 8,0 |

Note globale : 7,6. « La charte 2027 est appliquée avec cohérence. » Il confirme l'alphabet unifié, les lettres absentes grisées, l'hexadécimal propre, la recherche pertinente, la 404 avec la jaquette. Restaient : navigation trop haute sur les lettres et les catégories, liste « Aller à » native, tranche de l'accueil (lettres de largeurs trop inégales, carte parasite au survol, grand vide dans l'aperçu), coupes de texte (titre d'opcode, résumés, mots seuls), résumés sur une ligne.

Ce qui a été corrigé après ce tour :

- **Accueil** : la carte d'aperçu parasite venait du bloc d'aperçu de la tranche, qui portait le même attribut que les renvois ; le script ne vise plus que les liens. Lettres de la tranche avec une base commune (B ne fait plus cinq fois A), aperçu en colonne (nom, catégorie, résumé), plus de mot seul en fin de paragraphe (`text-wrap: pretty`), effectifs du pied lisibles, texte du livre avant la vidéo sur téléphone.
- **Définition** : la vedette est découpée après la conversion du tiret, « OP_CHECKLOCKTIMEVERIFY – » reste sur la première ligne et « 0xB1 » passe à la suivante ; résumés précédent et suivant coupés au mot, jamais sur « que » ou une lettre seule ; « ← Précédent » et « Suivant → » sur téléphone au lieu de titres tronqués.
- **Lettre** : la rangée des sous-groupes remplace la liste déroulante sur téléphone, devient collante et marque le groupe lu en le gardant en vue ; deux lignes de résumé partout ; bornes de l'intro en texte simple.
- **Catégorie** : une seule rangée (les 19 catégories) avant le titre ; l'alphabet passe sous l'en-tête, juste avant la liste, et reste collant.
- **Recherche** : plusieurs mots trouvés çà et là, ceux qui touchent le titre passent devant (« hd wallet » donne HD en tête) ; surlignage sans aplat sous le soulignement ; catégorie et terme anglais sur une ligne sur téléphone ; tiret demi-cadratin aussi dans les titres rendus par le script.

### Tour 5 (nouveau relecteur indépendant, relevés du tour 4 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,5 | 8,0 |
| Définition | 7,5 | 8,0 |
| Lettre | 7,0 | 7,5 |
| Catégorie | 7,0 | 7,5 |
| Recherche | 7,5 | 7,5 |
| 404 | 7,5 | 8,0 |

Note globale : 7,6, stable. Il confirme la carte parasite disparue, « hd wallet » corrigé, une seule rangée avant le titre des catégories, les sous-groupes collants. Défaut le plus répété : les résumés coupés en plein mot par la coupe CSS (« constit… », « 500 00… », « au-… »). Restaient aussi : « cle » qui mêle CLEMENTINE, lettres de la tranche encore inégales, catégories en rangée qui défile sans indice, en-têtes de groupe collants sous la rangée des sous-groupes, page tournée trop haute sur téléphone.

Ce qui a été corrigé après ce tour :

- **Résumés** : coupés au build (et dans le script pour la recherche et la 404) à une longueur qui tient dans les lignes données, au mot, jamais sur un mot-outil, un nombre entamé, une lettre seule ni une parenthèse ouverte ; la coupe CSS ne sert plus que de filet. Listes en deux colonnes jusqu'à 1 280 px pour que deux lignes suffisent.
- **Recherche** : quand le mot cherché est un mot entier de cinq titres ou plus, les simples débuts de mot ne s'y mêlent plus (« cle » ne montre que les CLÉ) ; « clef » cherche « clé » ; le terme trouvé est marqué en gras dans la couleur du lien, sans seconde couleur.
- **Catégorie** : les 19 catégories passent en bas de page, en grille complète ; la présentation montre sa première phrase entière, la suite derrière « Lire la suite » ; les barres collantes s'arrêtent à la fin de la liste ; lettres absentes plus pâles.
- **Lettre** : les en-têtes de groupe ne collent plus sous la rangée des sous-groupes, qui marque déjà le groupe lu.
- **Accueil** : lettres de la tranche de largeur égale ; respiration entre sections ramenée de 144 à 112 px ; mots cités des catégories moins gras, retirés sur téléphone.
- **Définition** : page tournée compacte sur téléphone (nom seul) ; bouton « Haut » dès le deuxième écran.

### Tour 6 (nouveau relecteur indépendant, relevés du tour 5 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,8 | 8,3 |
| Définition | 7,7 | 8,2 |
| Lettre | 7,4 | 7,8 |
| Catégorie | 7,3 | 7,7 |
| Recherche | 7,8 | 8,0 |
| 404 | 7,8 | 8,2 |

Note globale : 7,9. « Cohérent, solide et sans bug visible, mais encore plus propre qu'excitant. » Il confirme les résumés coupés au mot, la tranche régulière, la recherche nettoyée (« cle », « clef », « hd wallet »), le bouton « Haut » qui ne couvre plus la lecture. Restaient : la vidéo du livre floue, le titre d'opcode, des résumés qui finissent mal, le mobile trop long (ouverture de catégorie, catégories de l'accueil), deux couleurs dans les titres de BIP.

Ce qui a été corrigé après ce tour :

- **Livre** : boucle « feuilletage » refaite en 640 px (au lieu de 320), nette sur les écrans haute densité.
- **Définition** : les opcodes composent leur nom sur une ligne, et le code passe dessous en étiquette monospace (« OP_CHECKLOCKTIMEVERIFY », puis « 0xB1 ») ; sur téléphone, les repères montrent « ← Précédent » en petit et le nom dessous ; page tournée plus proche du texte ; résumé du mot suivant aligné à gauche.
- **Résumés** : une phrase entière qui tient passe sans points de suspension.
- **Lettre** : sujet des BIP en encre, à côté du numéro en Figue.
- **Catégorie** : « Pour commencer » en noms seuls sur téléphone, pictogramme plus petit ; en-têtes de groupe sur fond plein, sans le fondu qui laissait le texte à demi visible dessous.
- **Accueil** : 19 catégories en deux colonnes sur téléphone ; mots cités en encre soulignée Figue, plus petits ; boutons du mot du jour pleine largeur sur téléphone ; aperçu de la tranche moins haut.
- **404** : jaquette plus basse sur téléphone.

### Tour 7 (nouveau relecteur indépendant, relevés du tour 6 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,8 | 8,3 |
| Définition | 7,8 | 8,1 |
| Lettre | 7,4 | 7,7 |
| Catégorie | 7,5 | 7,7 |
| Recherche | 7,8 | 8,0 |
| 404 | 7,4 | 8,1 |

Note globale : 7,8. « Cohérent, rapide et fidèle à la charte 2027 ; ce qui le retient sous 8,5, c'est le nombre de petits défauts de finition qui se répètent. » Il confirme le titre d'opcode, l'ouverture de catégorie plus courte, les catégories de l'accueil en deux colonnes. Restaient : apostrophes droites et points de suspension dans les résumés, carte « Mot suivant » mal alignée, « Entrée 1 346 sur 1 408 » répété, titres de BIP en deux couleurs, suivi de la rangée des sous-groupes, formulaire de la 404 qui dépasse sur téléphone.

Ce qui a été corrigé après ce tour :

- **Typographie** : apostrophes typographiques dans les textes, les titres et les résumés (jamais dans le code) ; résumés des listes sur trois lignes, une phrase entière dès qu'elle tient.
- **Définition** : cartes précédent et suivant alignées à gauche toutes les deux ; numéro d'entrée seulement sous le signet (retiré du colophon) ; soulignement des codes renvoyés affiné.
- **Lettre** : titre de BIP d'une seule couleur ; pictogrammes des listes en encre, un peu plus grands ; le groupe marqué dans la rangée suit le tiers haut de l'écran.
- **404** : colonne de texte contenue (le formulaire ne dépasse plus de 6 px à droite), titre sous les racines sur téléphone.
- **Accueil** : boutons d'achat du livre l'un sous l'autre sur téléphone.

### Tour 8 (nouveau relecteur indépendant, relevés du tour 7 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,7 | 8,2 |
| Définition | 7,7 | 8,1 |
| Lettre | 7,2 | 7,6 |
| Catégorie | 7,4 | 7,6 |
| Recherche | 7,8 | 8,0 |
| 404 | 7,5 | 8,0 |

Note globale : 7,8. Il confirme les apostrophes, la carte « Mot suivant », le formulaire de la 404, « Lire la suite » qui déplie bien. Il relève un vrai défaut : sur téléphone, la rangée des sous-groupes ne défilait jamais vers le groupe marqué. Restaient aussi : apostrophes droites après un code dans le corps des définitions, trois points droits dans les cartes d'aperçu, titres de BIP en deux poids, terme cherché trop peu marqué, noms des voisins tronqués sur téléphone, tranche de position trop pâle, pages du livre illisibles sur téléphone.

Ce qui a été corrigé après ce tour :

- **Lettre** : la rangée centre maintenant la puce marquée (le calcul par `offsetLeft` donnait toujours 0 ; il passe par les rectangles affichés), au chargement comme au défilement ; sujet des BIP sur sa propre ligne, en petit, sous le numéro.
- **Typographie** : apostrophes aussi après un code en ligne (0 apostrophe droite hors code sur les 1 408 pages, vérifié) ; « ... » remplacés par « … » partout, cartes d'aperçu comprises.
- **Définition** : noms des voisins en entier sur téléphone (trois lignes au plus, coupés au « _ ») ; tranche de position pleine.
- **Recherche** : terme cherché sur un léger fond Figue, sans changer la couleur du texte.
- **Catégorie** : « Pour commencer » en liste verticale de quatre noms sur téléphone.
- **Accueil** : bande des pages du livre retirée sur téléphone.

### Tour 9 (nouveau relecteur indépendant, relevés du tour 8 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,9 | 8,5 |
| Définition | 8,0 | 8,4 |
| Lettre | 7,7 | 8,0 |
| Catégorie | 7,6 | 7,9 |
| Recherche | 8,0 | 8,2 |
| 404 | 7,8 | 8,2 |

Note globale : 8,0. « Plus abouti qu'au tour 8, l'identité du livre y est partout ; il reste du poli plutôt que des défauts de structure. » Il confirme les apostrophes, la rangée des sous-groupes qui suit enfin, le terme cherché marqué, les voisins en entier. Il lit encore des « ... » droits : vérifié, il n'en reste aucun dans le HTML (c'est le glyphe « … » d'Archivo, aux points espacés). Restaient : ouverture de catégorie longue sur téléphone, feuillage haut sur la 404, contrastes faibles (lettres absentes, marquage de recherche), barres collantes sans séparation, petits pictogrammes.

Ce qui a été corrigé après ce tour :

- **Catégorie** : sur téléphone, la présentation entière est repliée derrière « Lire la suite » et « Pour commencer » devient une rangée de quatre puces, le premier mot arrive au premier écran ; lettres absentes en Écorce pleine (5,9:1), sans fond.
- **Barres collantes** (sous-groupes, alphabet des catégories) : une ombre légère seulement quand elles collent.
- **Lettre** : pictogrammes à 18 px ; sujet des BIP en encre ; la puce suit le groupe dès le milieu de l'écran.
- **Recherche** : marquage du terme plus soutenu.
- **404** : arbre remonté et texte plus haut sur téléphone, le champ et la première suggestion tiennent au premier écran ; liens du bas dans le premier écran sur ordinateur.
- **Partout** : respiration entre sections ramenée à 96 px au plus.

### Tour 10 (nouveau relecteur indépendant, relevés du tour 9 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,9 | 8,4 |
| Définition | 8,0 | 8,3 |
| Lettre | 7,8 | 8,0 |
| Catégorie | 7,7 | 7,9 |
| Recherche | 8,1 | 8,2 |
| 404 | 7,9 | 8,2 |

Note globale : 8,0, stable. Il vérifie dans le source qu'il n'y a plus de « ... » (tous en U+2026) et confirme l'ouverture de catégorie raccourcie, la puce qui suit, le feuillage de la 404 ramené. « Les défauts restants sont des finitions, pas des cassures. » Restaient : pages du livre trop petites, mur de 25 renvois entrants, barres collantes sans séparation nette, « Lire la suite » qui ne se referme pas, fond de la fenêtre de recherche net derrière elle.

Ce qui a été corrigé après ce tour :

- **Accueil** : quatre pages intérieures plus grandes au lieu de six vignettes (la page de titre, presque blanche, est retirée) ; vidéo du livre plus large sur téléphone ; boutons d'achat espacés.
- **Définition** : renvois entrants repliés au-delà de 12 partout, plus seulement sur téléphone ; légende de position en encre.
- **Listes** : barres collantes avec un filet et une ombre légère quand elles collent ; sujet des BIP en Écorce, moins dense ; bouton « Haut » plus petit, ombré pour se détacher du texte.
- **Catégorie** : « Lire la suite » se replie ; une suite de moins de 160 signes s'affiche d'emblée.
- **Recherche** : fond flouté derrière la fenêtre.

### Tour 11 (nouveau relecteur indépendant, relevés du tour 10 à vérifier)

| Gabarit | Mobile | Ordinateur |
| --- | --- | --- |
| Accueil | 7,8 | 8,4 |
| Définition | 8,0 | 8,3 |
| Lettre | 7,7 | 8,0 |
| Catégorie | 7,7 | 7,9 |
| Recherche | 8,1 | 8,2 |
| 404 | 7,9 | 8,1 |

Note globale : 8,0, troisième tour au même niveau. Il confirme les voisins d'opcode, la barre collante séparée (aussi en sombre), « Replier », le flou derrière la recherche. Ce qu'il relève encore tient surtout du réglage fin, et contredit parfois les tours précédents (casse des sujets de BIP, place des puces).

Corrigé après ce tour, sans nouvelle relecture : renvois entrants repliés au-delà de 8 ; bouton « Haut » qui se retire après 2,5 s sans défilement ; « Vouliez-vous dire ? » ; bord clair de l'arbre poussé hors champ sur la 404.

## Bilan

L'objectif de 8,5 sur chaque gabarit n'est pas atteint. Notes : 6,5 au tour 1, 6,9 au tour 3 (avant la charte 2027), 7,6 aux tours 4 et 5, puis 7,8 à 8,0 du tour 6 au tour 11. Un seul gabarit a touché 8,5 (l'accueil sur ordinateur, tour 9). Les trois derniers relecteurs, chacun neuf, donnent 8,0 et disent la même chose : plus de défaut de structure, des finitions qui se contredisent d'un tour à l'autre. Les mobiles restent un demi-point sous les ordinateurs, surtout sur les longues listes (lettre, catégorie).
