# Fiche KDP — Dictionnaire de Bitcoin, édition 2027

Valeurs à saisir dans KDP. Les chiffres du livre (entrées, pages) sont ceux du dépôt au 25 octobre 2026 : les mettre à jour après le dernier build.

## Métadonnées

| Champ KDP | Valeur |
|---|---|
| Langue | Français |
| Titre | Dictionnaire de Bitcoin |
| Sous-titre | Tout le vocabulaire technique de Bitcoin |
| Numéro d'édition | 2 (la première édition est celle de 2026) |
| Auteur | Loïc Morel |
| Contributeurs | aucun (les contributeurs GitHub sont remerciés dans le livre) |
| Public | adulte : non ; « contenu pour un public adulte » : non |
| ISBN broché / relié | nouveaux ISBN à obtenir pour l'édition 2027 (question pour Loïc : ISBN gratuits KDP ou ISBN propres) ; les reporter dans `templates/legal.yaml` |
| Date de publication | celle de la mise en ligne (ne pas en saisir une à l'avance) |

## Description (4 000 caractères au plus ; saisie en texte simple, KDP accepte quelques balises HTML)

> Bitcoin a son vocabulaire : UTXO, mempool, Taproot, HTLC, preuve de travail, *seed*, Lightning, Nostr. Ce dictionnaire le définit, terme par terme, sans jargon inutile et sans promesse marketing.
>
> L'édition 2027 se lit de deux façons. Chaque terme technique a une définition courte, une ou deux phrases pour comprendre vite, et une définition développée, qui explique le fonctionnement pas à pas avec des exemples concrets, des schémas et l'histoire de chaque mécanisme.
>
> Le livre réunit plusieurs parties :
>
> - le dictionnaire technique : protocole, transactions, mempool, minage, portefeuilles et clés, cryptographie, confidentialité, Lightning Network, Ark, Liquid, RGB, ecash, Nostr, informatique quantique ;
> - les entreprises, applications et logiciels de l'écosystème ;
> - les personnes qui ont fait Bitcoin et ses précurseurs : cypherpunks, cryptographes, économistes, développeurs ;
> - une chronologie de plus de 700 événements, de la cryptographie à clé publique de 1976 à aujourd'hui, chaque date recoupée par deux sources ;
> - les spécifications : les 214 BIP, les BOLT et bLIP du Lightning Network et les 100 NIP de Nostr, avec leur statut et un résumé en français.
>
> Les définitions s'appuient sur les sources primaires : le code de Bitcoin Core, les BIP, les spécifications des protocoles et les discussions des développeurs.
>
> Le dictionnaire est un projet ouvert, publié en accès libre sur GitHub sous licence CC BY-NC-SA 4.0. Acheter le livre imprimé, c'est soutenir son auteur, Loïc Morel (pandul.fr), et la suite de ce travail.

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

### Barèmes utilisés (aide KDP, lue le 25 octobre 2026)

- **Broché, impression noir et blanc, marchés en euros** (format « regular », jusqu'à 6,12 × 9 po) : 0,75 € par livre + 0,012 € par page, de 110 à 828 pages.
- **Relié, noir et blanc** : environ 4,65 € (ou 4,50 € selon la page d'aide) + 0,012 € par page, de 110 à 550 pages. Les deux pages d'aide de KDP divergent : vérifier dans le calculateur.
- **Redevance papier sur Amazon.fr** : 60 % du prix hors TVA pour un prix public d'au moins 9,99 €, 50 % en dessous (changement du 10 juin 2025), moins le coût d'impression. Distribution étendue : 40 %.
- **Ebook** : option 70 % pour un prix compris entre 2,69 € et 12,99 €, moins les frais de livraison au Mo ; option 35 % au-delà. TVA du livre (numérique et papier) en France : 5,5 %.

### Calculs

| Format | Hypothèse de pages | Coût d'impression | Prix public conseillé | Prix HT | Redevance par exemplaire |
|---|---|---|---|---|---|
| Broché complet | 780 | 0,75 + 0,012 × 780 = 10,11 € | 32,90 € | 31,18 € | 0,60 × 31,18 − 10,11 = 8,60 € |
| Broché complet | 694 (premier build) | 9,08 € | 32,90 € | 31,18 € | 9,63 € |
| Relié complet | 550 (plafond KDP) | 4,65 + 0,012 × 550 = 11,25 € | 44,90 € | 42,56 € | 0,60 × 42,56 − 11,25 = 14,29 € |
| Ebook complet | — | frais de livraison au Mo (l'aide KDP prend l'exemple de 0,10 €/Mo en Espagne) | 9,99 € | 9,47 € | 0,70 × (9,47 − 3 × 0,10) ≈ 6,42 € pour un fichier de 3 Mo, si le tarif français est du même ordre |
| Broché « essentiel » (si publié) | à mesurer | 0,75 + 0,012 × pages | 14,90 € | 14,12 € | 0,60 × 14,12 − coût |

Les prix publics sont des propositions : à caler sur le prix de l'édition 2026 en librairie et sur Bitcoin Bazar. Garder le broché au-dessus de 9,99 € (seuil des 60 %) n'est pas un problème à ces volumes.

## Questions ouvertes pour Loïc

- ISBN 2027 : gratuits KDP ou propres ?
- Publier aussi l'édition « essentiel » (versions courtes seules), en broché et en ebook ?
- Relié : un volume en corps 9 / 11,5 pt, ou deux volumes ?
- Prix définitifs.
