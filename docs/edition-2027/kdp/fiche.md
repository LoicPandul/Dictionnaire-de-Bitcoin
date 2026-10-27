# Fiche KDP — Dictionnaire de Bitcoin, édition 2027

Valeurs à saisir dans KDP, pour deux livres imprimés (le complet et le poche « essentiel ») et leurs deux ebooks. Les chiffres du livre (entrées, pages) sont ceux du dépôt au 27 octobre 2026 : les mettre à jour après le dernier build.

## Métadonnées

| Champ KDP | Valeur |
|---|---|
| Langue | Français |
| Titre | Dictionnaire de Bitcoin |
| Sous-titre | Tout le vocabulaire technique de Bitcoin (pour le poche : à décliner, par exemple « L'essentiel », à trancher par Loïc) |
| Numéro d'édition | 2 (la première édition est celle de 2026) |
| Auteur | Loïc Morel |
| Contributeurs | aucun (les contributeurs GitHub sont remerciés dans le livre) |
| Public | adulte : non ; « contenu pour un public adulte » : non |
| ISBN | un ISBN par livre imprimé (broché complet, poche essentiel), à obtenir pour l'édition 2027 (question pour Loïc : ISBN gratuits KDP ou ISBN propres) ; les reporter dans `templates/fr/legal.yaml` |
| Date de publication | celle de la mise en ligne (ne pas en saisir une à l'avance) |

## Description (4 000 caractères au plus ; saisie en texte simple, KDP accepte quelques balises HTML)

### Broché complet (7 × 10 po, couleur premium, 730 pages)

> Bitcoin a son vocabulaire : UTXO, mempool, Taproot, HTLC, preuve de travail, *seed*, Lightning, Nostr. Ce dictionnaire le définit, terme par terme, sans jargon inutile et sans promesse marketing.
>
> Chaque terme technique a une définition développée, qui explique le fonctionnement pas à pas avec des exemples concrets, des schémas en couleur et l'histoire de chaque mécanisme.
>
> Le livre réunit cinq parties :
>
> - le dictionnaire technique, 1 060 entrées : protocole, transactions, mempool, minage, portefeuilles et clés, cryptographie, confidentialité, Lightning Network, Ark, Liquid, RGB, ecash, Nostr, informatique quantique ;
> - les entreprises, applications et logiciels de l'écosystème, 208 entrées ;
> - 48 personnes qui ont fait Bitcoin et ses précurseurs : cypherpunks, cryptographes, économistes, développeurs ;
> - une chronologie de 160 événements, de la cryptographie à clé publique de 1976 à aujourd'hui ;
> - les spécifications : 214 BIP, 13 BOLT et 15 bLIP, avec leur statut et un résumé en français.
>
> Les définitions s'appuient sur les sources primaires : le code de Bitcoin Core, les BIP, les spécifications des protocoles et les discussions des développeurs.
>
> Le dictionnaire est un projet ouvert, publié en accès libre sur GitHub sous licence CC BY-NC-SA 4.0 (les logos de tiers en sont exclus et portent leur crédit). Acheter le livre imprimé, c'est soutenir son auteur, Loïc Morel (pandul.fr), et la suite de ce travail.

### Poche « essentiel » (5 × 8 po, noir et blanc, 302 pages)

> Bitcoin a son vocabulaire : UTXO, mempool, Taproot, HTLC, preuve de travail, *seed*, Lightning, Nostr. Cette édition de poche le résume en définitions courtes, une ou deux phrases par terme, pour comprendre vite et garder le livre sous la main.
>
> Elle réunit les 1 060 termes du dictionnaire technique et les 208 entrées des entreprises, applications et logiciels de l'écosystème. Les définitions développées, les personnes, la chronologie et les spécifications se trouvent dans l'édition complète.
>
> Le dictionnaire est un projet ouvert, publié en accès libre sur GitHub sous licence CC BY-NC-SA 4.0 (les logos de tiers en sont exclus et portent leur crédit). Acheter le livre imprimé, c'est soutenir son auteur, Loïc Morel (pandul.fr), et la suite de ce travail.

Les ebooks reprennent la description de leur édition.

## Mots-clés (7 cases, 50 caractères chacune)

1. dictionnaire bitcoin français
2. lexique bitcoin blockchain
3. vocabulaire technique bitcoin
4. lightning network explication
5. portefeuille bitcoin clé privée
6. minage et preuve de travail
7. comprendre bitcoin débutant

Pas de nom de marque tierce ni de mot trompeur (« gratuit », « best-seller ») : KDP les refuse.

## Catégories (3 au plus, à choisir dans l'arborescence KDP d'Amazon.fr)

Les libellés exacts dépendent de l'arborescence affichée par KDP ; viser, par ordre de préférence :

1. Informatique et Internet › Sécurité informatique › Cryptographie
2. Économie et finance › Monnaie (ou Banque, monnaie et finance)
3. Dictionnaires et encyclopédies › Dictionnaires techniques et spécialisés

## Prix conseillés

### Barèmes utilisés (aide KDP, lue le 27 octobre 2026)

- **Format** : KDP appelle « standard » un livre jusqu'à 6,12 × 9 po et « grand » au-delà. Le 7 × 10 po du complet est « grand » ; le 5 × 8 po de l'essentiel est « standard » ([formats et pages](https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6)).
- **Complet, broché en couleur premium, papier blanc, format grand, marchés en euros** : 0,75 € par livre + 0,0715 € par page (de 42 à 828 pages) ([coûts d'impression](https://kdp.amazon.com/fr_FR/help/topic/G201834340)). Pour mémoire, le barème « standard » en couleur premium est de 0,0525 € par page, et la couleur standard (0,035 € par page en format grand) ne va que de 72 à 600 pages : elle ne convient pas à 730 pages.
- **Essentiel, broché en noir et blanc, papier blanc, format standard, marchés en euros** : 0,75 € par livre + 0,012 € par page, de 110 à 828 pages (même page).
- **Redevance papier sur Amazon.fr** : 60 % du prix pour un prix public d'au moins 9,99 €, 50 % à 9,98 € et en dessous (changement du 10 juin 2025), moins le coût d'impression. Formule de KDP : (taux × prix public) − coût d'impression ; prix public minimum = coût d'impression ÷ taux. Distribution étendue : 40 % ([redevances](https://kdp.amazon.com/en_US/help/topic/G201834330)). Prix public maximal en euros : 250 €.
- **Ebook** : option 70 % pour un prix compris entre 2,69 € et 12,99 €, moins les frais de livraison au Mo ; option 35 % au-delà. TVA du livre (numérique et papier) en France : 5,5 %.

Le prix HT ci-dessous est le prix public divisé par 1,055. La page d'aide de KDP n'indique pas si le taux de redevance s'applique au prix TTC ou HT : le calcul avec TVA est le plus prudent, et le calculateur de KDP tranche.

### Prix minimum

| Livre | Pages | Coût d'impression | Prix minimum, formule KDP (coût ÷ taux) | Prix minimum, TVA 5,5 % comprise |
|---|---|---|---|---|
| Complet (couleur premium, 7 × 10 po) | 730 | 0,75 + 0,0715 × 730 = 52,945 € | 52,945 ÷ 0,60 = 88,24 € | 93,10 € |
| Essentiel (noir et blanc, 5 × 8 po) | 302 | 0,75 + 0,012 × 302 = 4,374 € | 4,374 ÷ 0,50 = 8,75 € (tranche 50 %, sous 9,99 €) | 9,23 € |

### Propositions de prix et redevance

| Livre | Prix public proposé | Prix HT | Redevance par exemplaire |
|---|---|---|---|
| Complet | 99,00 € | 93,84 € | 0,60 × 93,84 − 52,945 = 3,36 € |
| **Complet** | **109,00 €** | 103,32 € | 0,60 × 103,32 − 52,945 = **9,05 €** |
| Complet | 119,00 € | 112,80 € | 0,60 × 112,80 − 52,945 = 14,73 € |
| Essentiel | 12,90 € | 12,23 € | 0,60 × 12,23 − 4,374 = 2,96 € |
| **Essentiel** | **14,90 €** | 14,12 € | 0,60 × 14,12 − 4,374 = **4,10 €** |
| Essentiel | 16,90 € | 16,02 € | 0,60 × 16,02 − 4,374 = 5,24 € |
| Ebook complet | 9,99 € | 9,47 € | 0,70 × (9,47 − 3 × 0,10) ≈ 6,42 € pour un fichier de 3 Mo |
| Ebook essentiel | 4,99 € | 4,73 € | 0,70 × (4,73 − 2 × 0,10) ≈ 3,17 € pour un fichier de 2 Mo |

Les lignes en gras sont ma proposition ; le prix reste à décider par Loïc. Sur les ebooks, les frais de livraison (l'aide KDP prend l'exemple de 0,10 €/Mo en Espagne) et les poids de fichier sont des hypothèses : le tarif français n'est pas lu et les EPUB ne sont pas pesés ici. Le coût du complet est dominé par la couleur premium (52,945 € d'impression pour 730 pages) : chaque euro de prix public en plus rapporte environ 0,57 € de redevance. Le prix est à comparer avec celui de l'édition 2026 en librairie.

## Questions ouvertes pour Loïc

- ISBN 2027 : un ISBN par livre imprimé (complet et essentiel), gratuits KDP ou propres ?
- Prix définitifs des deux livres imprimés et des deux ebooks.
