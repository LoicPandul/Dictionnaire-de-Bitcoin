# Plan des visuels de l'édition 2027

Deux fichiers :

- `plan-schemas.tsv` : les schémas techniques à dessiner avec le skill `schemas-dictionnaire`, une ligne par schéma, triés par priorité puis par slug.
- `plan-logos-captures.tsv` : les logos et captures d'écran de la partie « Entreprises, applications et logiciels », avec la source officielle et les conditions d'usage trouvées. Rien n'est téléchargé : Loïc tranche d'abord la question des droits.

## Chiffres

| | Nombre |
|---|---|
| Schémas | 277 (76 A, 162 B, 39 C) |
| dont nouveaux | 235 |
| dont refaits au style 2027 | 42 (images de 2026 en noir et blanc) |
| Logos | 94 |
| Captures d'écran | 34 |
| Total des visuels | 405 pour 1 408 entrées, soit 1 pour 3,5 |

Dans le dictionnaire technique seul : 270 schémas pour 990 entrées, soit 1 pour 3,7. Deux schémas servent deux fois (même dessin) : `bip-0044` reprend celui de `chemin-de-derivation`, `bip-0156` celui de `dandelion`. Il y a donc 275 schémas à dessiner. Les 39 schémas C servent de marge : sans eux, le total tombe à 366.

Schémas par partie et par priorité :

| Partie, groupe de catégories | A | B | C | Total | Entrées |
|---|---|---|---|---|---|
| Protocole, transactions, mempool, évolution, nœud, réseau | 27 | 46 | 1 | 74 | 207 |
| Script, opcodes, covenants | 4 | 16 | 2 | 22 | 119 |
| Clés, portefeuille, cryptographie, informatique | 13 | 22 | 9 | 44 | 209 |
| Minage et pools | 4 | 7 | 3 | 14 | 68 |
| Confidentialité, analyse de chaîne, attaques | 6 | 24 | 13 | 43 | 90 |
| Lightning et paiements Lightning | 12 | 19 | 4 | 35 | 87 |
| Ark, statechains, sidechains, RGB, actifs, rollups, Nostr, ecash, couche supérieure | 9 | 15 | 4 | 28 | 120 |
| Économie, altcoins et forks, histoire | 0 | 8 | 2 | 10 | 90 |
| Spécifications (BIP) | 1 | 5 | 1 | 7 | 220 |

Logos et captures : 94 logos, 34 captures. 100 lignes citent une licence ou des conditions lues (45 logos tirés d'un dépôt de code avec sa licence, 21 kits presse ou pages de marque, 34 captures de logiciels avec la licence du logiciel) ; 28 logos pris sur un site officiel n'ont aucune condition écrite (`non trouvée`).

## Méthode

1. Inventaire des 1 408 entrées (catégorie, partie d'après `templates/parts.yaml`, nombre de mots, images existantes).
2. Lecture des définitions en quatre lots (protocole et script ; clés, minage, confidentialité et attaques ; Lightning, surcouches, économie et histoire ; écosystème), plus les spécifications.
3. Un schéma seulement quand il montre ce que la prose ne donne pas : un ordre, une structure, une simultanéité, une proportion, un avant/après. Il doit tenir dans la charte (un sujet en Figue, quatre rôles au plus, 40 mots au plus, rien sous 30 px). Priorité A aux notions qu'un débutant cherche.
4. Pas de doublon : quand deux entrées voisines expliquent le même mécanisme, le schéma va à l'entrée de référence.
5. Les 52 entrées déjà illustrées : chaque image de 2026 a été ouverte et comparée à la définition.
6. Contrôle par script (`/tmp/ed2027/t10-plan-visuels/controle.py`, hors dépôt) : chaque slug existe, la catégorie correspond, chaque `apres` fait 6 à 10 mots et ouvre exactement un paragraphe de `definition.md`, les rôles sont pris dans la liste de la charte, au plus deux lignes par entrée. Résultat : 277 lignes, 0 erreur.

## Images de 2026

Refaites (42 schémas sur 40 entrées), dont trois qui changent de contenu :

- `adresse-de-reception` : l'image de 2026 est l'arbre BIP-0084, hors sujet ; le schéma 2027 montre l'anatomie d'une adresse SegWit, après le premier paragraphe.
- `bsv-bitcoin-satoshi-vision` : le logo est remplacé par la lignée BTC, BCH (2017), BSV (2018), XEC (2020). À confirmer : Loïc peut préférer garder le logo.
- `orphelin`, `resynchronisation` et `scriptsig` changent d'angle (bloc reçu sans parent, changement de branche, ordre d'évaluation sur la pile ; l'ancienne image de `scriptsig` était celle de `scriptpubkey`).

Non refaites (12 entrées) :

- logos, pas des schémas : `bitcoin-b-majuscule`, `bch-bitcoin-cash`, `bitcoin-core` et `bitcoin-knots` (les deux derniers passent dans `plan-logos-captures.tsv`) ;
- même arbre BIP-0084 avec une flèche sur un niveau : `cle-maitresse`, `objectif`, `type-de-devise`, `profondeur`, `chaine-interne` (l'arbre reste sur `chemin-de-derivation`, `compte` et `chaine-externe`) ;
- image en double : `osint` (celle de `point-d-entree`), `policy-miniscript` (celle de `miniscript`) ;
- pas un schéma : `paynym` (des robots).

## Schémas auxquels j'ai renoncé

- Variantes d'un même mécanisme : les 7 variantes de SigHash (couvertes par `sighash-flag`), `fee-bumping` et `full-rbf` (par RBF et CPFP), `loop-in`, `loop-out` et `autoloop` (par `submarine-swap`), `peg-in`, `peg-out` et `lbtc` (par `ancrage-bilateral`), `inbound-capacity`, `outbound-capacity` et `liquidites` (par `capacite-de-canal-lightning`), les variantes de rémunération des pools (`smpps`, `dgm`, `tides`…, par `pps-pay-per-share` et `pplns-pay-per-last-n-shares`).
- Textes jumeaux : `goldfinger` (même texte que l'attaque des 51 %), `forced-address-reuse` (même texte que `dusting-attack`), `inflation` (même courbe que `limite-d-emission`).
- Opcodes : 5 schémas sur 76 (`OP_ROLL`, `OP_CHECKSIGADD`, `OP_SUCCESS`, `OP_CHECKLOCKTIMEVERIFY`, `OP_CHECKSEQUENCEVERIFY`, plus `OP_CAT` et `OP_CHECKTEMPLATEVERIFY` dans COVENANTS) ; la pile du script standard est dessinée une fois, sur P2PKH.
- Notions abstraites ou purement historiques : `qubit`, `shor-algorithme`, `segwit2x`, `nya-new-york-agreement`, l'essentiel d'HISTOIRE ET CULTURE et d'INFORMATIQUE.
- Spécifications : les BOLT et bLIP sont des résumés de 50 à 120 mots. Leurs mécanismes principaux ont déjà un schéma côté technique (`transaction-de-financement`, `transaction-d-engagement`, `htlc`, `sphinx`, `invoice-lightning`, `offer`). Le *handshake* Noise (BOLT-08) et le *gossip* (BOLT-07) n'en ont pas : les définitions ne détaillent pas assez les étapes pour un dessin juste. Côté BIP, seuls restent les mécanismes propres à la spécification : machine d'états du BIP-0009, verrouillage forcé du BIP-0008, TXID dupliqués du BIP-0030, bug du 64e halving du BIP-0042, chaîne des en-têtes de filtres du BIP-0157.

## Points à trancher

- Droits des logos et captures : marques de mempool.space hors de la licence AGPL du code ; Umbrel et myNode interdisent l'usage commercial, Peach ajoute une Commons Clause, ce qui compte pour un livre vendu. Les archives zip des kits presse (Blockstream, Ledger…) n'ont pas été ouvertes, et le manuel de marque de Trezor n'a pas pu être lu.
- Quelques logos de dépôt sont l'icône de l'application, sans le nom (Phoenix, Blixt, Blue Wallet, Green).
- Deux définitions à corriger, vues en passant : `raw-transaction` place le locktime avant le témoin (la sérialisation met le témoin avant le locktime ; le schéma suit l'ordre réel) ; `entete-de-bloc` écrit « entête » au lieu de « en-tête ».
