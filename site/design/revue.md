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
