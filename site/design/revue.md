# Revue des gabarits

Chaque gabarit (accueil, définition, lettre, catégorie, recherche, 404) a été capturé en 390, 768 et 1440 px, mesuré par l'inspecteur du skill design-taste-frontend, critiqué par moi selon `references/critique.md`, puis noté sur 10 par un relecteur indépendant (un sous-agent qui n'a vu ni la direction ni mon raisonnement : seulement le brief de Loïc, les captures, les vidéos et le site en marche). Objectif : 8,5 au moins partout, en mobile et sur ordinateur.

## Mesures

- **Inspecteur** (1440, 768, 390 px) : 0 échec sur l'accueil. Sur les pages de lecture, il reste la règle « au moins quatre photos » et « une vidéo », écrite pour des pages vitrines : une page de définition, de lettre ou de recherche n'a pas de photo à montrer, et en inventer une serait de la décoration. Défendu, pas corrigé. Restent aussi « le h1 est un nom seul » sur la définition (c'est la vedette d'un dictionnaire ; la catégorie et « Entrée 1 346 sur 1 408 du dictionnaire » suivent dans le premier écran) et « la même grande ligne reste à l'écran » sur la lettre B (l'en-tête de groupe collant, voulu, comme un mot-repère).
- **Lighthouse mobile** (page de définition) : voir le tableau final.
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
