# Taxonomie de l'édition 2027

Proposition de catégories pour les quatre parties du livre, et reclassement des 1 408 entrées
(détail ligne par ligne dans `reclassement.tsv`). Chaque catégorie appartient à une seule partie.
Les descriptions sont prêtes à devenir les commentaires de `templates/categories.yaml` : elles
restent sans balisage Markdown, parce que le site lit ces commentaires tels quels.

Pictogramme « existant » : le fichier existe déjà dans `assets/pictograms/` sous ce slug.
« nouveau » : SVG et PDF à dessiner en phase 2.

| Partie | Catégories | Entrées |
|---|---|---|
| `technique` | 32 | 990 |
| `ecosysteme` | 12 | 195 |
| `personnes` | 6 | 3 |
| `specifications` | 4 | 220 |
| Total | 54 | 1 408 |

## Partie technique

### PROTOCOLE

Pictogramme : `protocole` (existant). Entrées : 37.

Les définitions des structures et des règles de base du protocole Bitcoin : blocs, blockchain,
preuve de travail, consensus, émission monétaire et horodatage du réseau. Elle exclut les
transactions, la mempool, le réseau pair-à-pair, le nœud et les mises à jour du protocole, qui ont
chacun leur propre catégorie.

### TRANSACTIONS

Pictogramme : `transactions` (nouveau). Entrées : 41.

Toutes les définitions liées à la structure d'une transaction Bitcoin : entrées et sorties, UTXO,
identifiants, champs de la transaction, témoin, SigHash et timelocks. Elle couvre aussi les sorties
particulières (poussière, OP_RETURN) et la notion de confirmation.

### MEMPOOL ET FRAIS

Pictogramme : `mempool` (nouveau). Entrées : 21.

Les définitions relatives aux transactions en attente de confirmation : mempool, politique de
relais, règles de standardisation, frais et taux de frais, et mécanismes qui permettent d'accélérer
une transaction (RBF, CPFP).

### ÉVOLUTION DU PROTOCOLE

Pictogramme : `evolution-du-protocole` (nouveau). Entrées : 24.

Les définitions qui décrivent la manière dont les règles de Bitcoin changent : processus des BIP et
rôles des développeurs de Bitcoin Core, soft forks et hard forks, méthodes d'activation, mises à jour
déployées (SegWit, Taproot) et propositions de modification du consensus, hors covenants.

### FONCTIONNEMENT DU NŒUD

Pictogramme : `noeud` (nouveau). Entrées : 43.

Les définitions qui concernent le nœud Bitcoin : types de nœuds, synchronisation initiale, élagage,
clients légers, index et serveurs d'adresses. Elle regroupe aussi les fichiers et dossiers du
répertoire de données de Bitcoin Core. Le logiciel Bitcoin Core lui-même est dans la partie
écosystème.

### RÉSEAU

Pictogramme : `reseau` (existant). Entrées : 41.

Toutes les définitions liées au réseau pair-à-pair de Bitcoin : découverte et gestion des pairs,
messages, propagation des blocs et des transactions, réseaux d'anonymisation (Tor, I2P) et réseaux
de test.

### SCRIPT

Pictogramme : `script` (existant). Entrées : 30.

Toutes les définitions concernant le langage Script, hors opcodes : scripts de verrouillage et de
déverrouillage, modèles de scripts standards (P2PKH, P2WPKH, P2TR…), versions de SegWit, Tapscript
et langages de plus haut niveau comme Miniscript ou Simplicity.

### OPCODES

Pictogramme : `opcodes` (nouveau). Entrées : 76.

Une définition par opcode du langage Script, qu'il soit actif, désactivé ou réservé (OP_NOP,
OP_SUCCESS), plus la définition générale des opcodes. Les opcodes proposés pour introduire des
covenants sont dans la catégorie « Covenants ».

### COVENANTS

Pictogramme : `covenants` (nouveau). Entrées : 13.

Les définitions des covenants, c'est-à-dire des conditions qui restreignent la manière dont une pièce
pourra être dépensée, et des propositions de soft fork qui les rendraient possibles : opcodes
(OP_CHECKTEMPLATEVERIFY, OP_CAT, OP_VAULT…), SigHash ANYPREVOUT et constructions comme MATT.

### CLÉS ET DÉRIVATION

Pictogramme : `cles-et-derivation` (nouveau). Entrées : 45.

Les définitions relatives aux clés et à leur dérivation : clés privées et publiques, portefeuilles
HD, chemins de dérivation, phrases de récupération et passphrase, clés étendues et leurs préfixes,
descriptors, ainsi que les formats d'encodage des clés et des adresses.

### PORTEFEUILLE

Pictogramme : `portefeuille` (existant). Entrées : 34.

Les définitions concernant l'usage et la sécurisation d'un portefeuille Bitcoin : types de
portefeuilles, multisig, sélection des pièces, étiquetage, PSBT, signature hors ligne et vaults.
Les noms de logiciels de portefeuille et de hardware wallets sont dans la partie écosystème.

### MINAGE

Pictogramme : `minage` (existant). Entrées : 36.

L'ensemble des termes se rapportant à l'activité de minage : construction du bloc candidat,
difficulté et hashrate, matériel (ASIC, hashboards, refroidissement), énergie et installations.
Les pools et la rémunération des mineurs ont leur propre catégorie.

### POOLS DE MINAGE

Pictogramme : `pools-de-minage` (nouveau). Entrées : 32.

Les définitions relatives au minage en commun : fonctionnement des pools, shares, méthodes de
rémunération des mineurs (PPS, FPPS, PPLNS, TIDES…), protocoles de communication entre la pool et
les mineurs (Stratum), pools décentralisées et minage solo.

### CRYPTOGRAPHIE

Pictogramme : `cryptographie` (existant). Entrées : 63.

Toutes les définitions liées aux principes et techniques cryptographiques appliqués en général :
fonctions de hachage, courbes elliptiques, signatures numériques et multisignatures, chiffrement,
engagements et preuves à divulgation nulle de connaissance.

### INFORMATIQUE

Pictogramme : `informatique` (existant). Entrées : 65.

L'ensemble des définitions relatives aux concepts informatiques généraux qui ne sont pas propres à
Bitcoin, hors cryptographie : numération et encodage, structures de données, systèmes distribués,
développement logiciel (Git, licences) et outils généralistes utilisés par Bitcoin Core (LevelDB,
ZeroMQ…).

### INFORMATIQUE QUANTIQUE

Pictogramme : `quantique` (nouveau). Entrées : 2 (environ 25 termes à venir en phase 5).

Les définitions liées à l'informatique quantique et à ses conséquences pour la cryptographie de
Bitcoin : notions de base, algorithmes quantiques (Shor, Grover), signatures post-quantiques et
propositions de migration.

### CONFIDENTIALITÉ

Pictogramme : `confidentialite` (existant). Entrées : 37.

L'ensemble des définitions traitant de la protection de la vie privée sur Bitcoin : coinjoin et ses
protocoles (Whirlpool, WabiSabi…), payjoin, Silent Payments, codes de paiement réutilisables et
autres structures de transaction conçues pour casser le traçage. Les logiciels sont dans la partie
écosystème.

### ANALYSE DE CHAÎNE

Pictogramme : `analyse-de-chaine` (nouveau). Entrées : 21.

Les définitions relatives à l'analyse de chaîne, c'est-à-dire aux méthodes qui servent à tracer les
flux de bitcoins : heuristiques internes et externes, modèles de transaction, réutilisation
d'adresse, empreintes de portefeuille et indicateurs de confidentialité (anonsets, score de
Boltzmann).

### ATTAQUE

Pictogramme : `attaque` (existant). Entrées : 32.

Les définitions des attaques et vulnérabilités associées à Bitcoin et à ses surcouches : double
dépense, attaques sur le minage, sur le réseau pair-à-pair, sur les canaux Lightning et sur les
utilisateurs.

### ÉCONOMIE ET RÉGULATION

Pictogramme : `economie-et-regulation` (existant). Entrées : 55.

Toutes les définitions relatives aux aspects économiques, politiques, réglementaires et légaux qui
touchent Bitcoin : théorie monétaire, marché et unités de compte, garde des fonds, réglementation
(KYC, AML, PSAN).

### ALTCOINS ET FORKS

Pictogramme : `altcoins` (nouveau). Entrées : 10.

Les définitions des cryptomonnaies autres que le bitcoin, des forks de Bitcoin (Bitcoin Cash,
Bitcoin SV…) et des mécanismes propres à ces systèmes, comme la preuve d'enjeu. Les sidechains de
Bitcoin ont leur propre catégorie.

### HISTOIRE ET CULTURE

Pictogramme : `histoire` (existant, catégorie renommée depuis « HISTOIRE »). Entrées : 25.

Les définitions des événements, des précurseurs et des concepts historiques de Bitcoin : monnaies
électroniques d'avant 2009, Blocksize War, incidents marquants. Elle couvre aussi la culture de la
communauté (HODL, pilule orange, Pizza Day). Les personnes sont dans la partie personnes.

### LIGHTNING NETWORK

Pictogramme : `lightning-network` (existant). Entrées : 55.

Tous les termes du Lightning Network qui concernent les canaux de paiement : ouverture, mise à jour
et fermeture, transactions d'engagement et de pénalité, HTLC, gestion de la liquidité et swaps avec
la chaîne principale. Les logiciels et implémentations Lightning sont dans la partie écosystème.

### PAIEMENTS LIGHTNING

Pictogramme : `paiements-lightning` (nouveau). Entrées : 32.

Les définitions relatives à l'envoi et au routage des paiements sur le Lightning Network : factures
et offers, recherche de chemin, routage en oignon, frais de routage, paiements multi-chemins et
protocoles applicatifs comme LNURL ou L402.

### ARK

Pictogramme : `ark` (nouveau). Entrées : 9.

Toutes les définitions spécifiques au protocole Ark : VTXO, rounds, rôle de l'Ark Service Provider,
transactions propres au protocole et variantes comme clArk.

### SPARK ET STATECHAINS

Pictogramme : `spark` (nouveau). Entrées : 8.

Les définitions des statechains et du protocole Spark, qui transfèrent la propriété d'un UTXO hors
chaîne grâce à une clé partagée avec un groupe d'opérateurs.

### SIDECHAIN

Pictogramme : `sidechain` (existant). Entrées : 15.

Les termes relatifs aux sidechains : ancrage bilatéral, peg-in et peg-out, minage fusionné,
drivechains et fédérations, ainsi que les réseaux Liquid et RSK.

### RGB

Pictogramme : `rgb` (existant). Entrées : 37.

Toutes les définitions spécifiques au protocole RGB et à la validation côté client sur laquelle il
repose.

### ACTIFS SUR BITCOIN

Pictogramme : `actifs` (nouveau). Entrées : 23.

Les définitions des protocoles qui émettent ou représentent des actifs sur Bitcoin, hors RGB :
colored coins, Omni et Counterparty, Ordinals et inscriptions, Runes, BRC-20, Stamps et Taproot
Assets.

### ROLLUPS ET BITVM

Pictogramme : `rollups` (nouveau). Entrées : 8.

Les définitions relatives aux rollups construits sur Bitcoin et à BitVM : principes de
fonctionnement, séquenceurs, ponts et réseaux déployés comme Citrea.

### NOSTR

Pictogramme : `nostr` (nouveau). Entrées : 9 (environ 20 termes à venir en phase 5).

Toutes les définitions spécifiques au protocole Nostr : événements, relais, clés et leurs encodages,
le terme générique NIP, et les usages liés à Bitcoin (zaps, Nostr Wallet Connect).

### COUCHE SUPÉRIEURE

Pictogramme : `couche-superieure` (existant). Entrées : 11.

Les notions générales sur les surcouches (off-chain, joinpool, échange atomique) et les protocoles
construits sur Bitcoin qui n'ont pas leur propre catégorie : monnaie électronique chaumienne (Cashu,
Fedimint), contrats à oracle (DLC) et horodatage (OpenTimestamps).

## Partie écosystème

### PORTEFEUILLE LOGICIEL

Pictogramme : `portefeuille-logiciel` (nouveau). Entrées : 27.

Les logiciels de portefeuille Bitcoin sur mobile, ordinateur ou navigateur, y compris les
portefeuilles Lightning et ecash, et ceux qui ne sont plus maintenus.

### PORTEFEUILLE MATÉRIEL

Pictogramme : `portefeuille-materiel` (nouveau). Entrées : 16.

Les hardware wallets et autres dispositifs de signature, les firmwares qui transforment un appareil
en dispositif de signature, et les supports physiques au porteur (cartes NFC, clés USB à usage
unique, pièces Casascius).

### IMPLÉMENTATION

Pictogramme : `implementation` (nouveau). Entrées : 16.

Les implémentations du protocole Bitcoin (Bitcoin Core et ses programmes, Bitcoin Knots, btcd…),
leurs forks historiques, et les implémentations d'autres protocoles construits sur Bitcoin, hors
Lightning.

### LOGICIEL LIGHTNING

Pictogramme : `logiciel-lightning` (nouveau). Entrées : 30.

Les implémentations du Lightning Network (LND, Core Lightning, Eclair, LDK…), les interfaces et
outils de gestion de nœud, et les services de liquidité et de swap propres à Lightning.

### OUTIL DE DÉVELOPPEMENT

Pictogramme : `outil` (existant). Entrées : 9.

Les bibliothèques, kits de développement et outils en ligne de commande destinés aux développeurs
d'applications Bitcoin, hors Lightning.

### NŒUD ET EXPLORATEUR

Pictogramme : `noeud-et-explorateur` (nouveau). Entrées : 10.

Les distributions de nœud clé en main, les serveurs d'indexation (implémentations d'Electrum Server,
Dojo) et les explorateurs de blocs ou outils d'exploration de la blockchain.

### OUTIL DE CONFIDENTIALITÉ

Pictogramme : `outil-de-confidentialite` (nouveau). Entrées : 8.

Les logiciels de coinjoin, les services de mixage et les outils de mesure de la confidentialité.
Les portefeuilles orientés confidentialité restent dans « Portefeuille logiciel ».

### ACTEURS DU MINAGE

Pictogramme : `acteurs-du-minage` (nouveau). Entrées : 20.

Les pools de minage, les fabricants de machines, les entreprises de minage, ainsi que les logiciels
et matériels de minage désignés par leur nom.

### PLATEFORME D'ÉCHANGE

Pictogramme : `plateforme-d-echange` (nouveau). Entrées : 9.

Les plateformes d'achat et de vente de bitcoins, centralisées ou pair-à-pair, actives ou fermées.

### SERVICE ET PAIEMENT

Pictogramme : `service-et-paiement` (nouveau). Entrées : 12.

Les services en ligne qui fonctionnent avec Bitcoin, les processeurs et terminaux de paiement pour
commerçants, et les services historiques de monnaie numérique ou de commerce en ligne (e-gold,
Silk Road).

### ENTREPRISE

Pictogramme : `organisation` (existant). Entrées : 26.

Les entreprises qui développent des produits ou des services autour de Bitcoin, quand la fiche porte
sur l'entreprise plutôt que sur un produit précis.

### COMMUNAUTÉ ET FONDATION

Pictogramme : `communaute` (existant). Entrées : 12.

Les associations, fondations, centres de recherche et programmes de financement, ainsi que les
médias, forums et listes de diffusion de la communauté Bitcoin.

## Partie personnes

### CYPHERPUNK

Pictogramme : `cypherpunk` (nouveau). Entrées : 1.

Les membres du mouvement cypherpunk et les militants de la cryptographie dont les travaux ou les
idées ont préparé Bitcoin.

### CRYPTOGRAPHE ET INFORMATICIEN

Pictogramme : `cryptographe-et-informaticien` (nouveau). Entrées : 0.

Les chercheurs en cryptographie et en informatique dont les travaux sont utilisés par Bitcoin :
cryptographie à clé publique, fonctions de hachage, signatures, systèmes distribués.

### ÉCONOMISTE

Pictogramme : `economiste` (nouveau). Entrées : 0.

Les économistes et penseurs dont les idées éclairent Bitcoin, en particulier ceux de l'École
autrichienne.

### DÉVELOPPEUR BITCOIN

Pictogramme : `developpeur-bitcoin` (nouveau). Entrées : 1.

Le créateur de Bitcoin et les développeurs qui ont contribué au protocole et à ses implémentations.

### DÉVELOPPEUR DE SURCOUCHES

Pictogramme : `developpeur-de-surcouches` (nouveau). Entrées : 0.

Les développeurs et chercheurs à l'origine du Lightning Network et des autres surcouches de Bitcoin
(RGB, Ark, Fedimint, Cashu…).

### FIGURE DE L'ÉCOSYSTÈME

Pictogramme : `figure-de-l-ecosysteme` (nouveau). Entrées : 1.

Les entrepreneurs, investisseurs, auteurs et militants qui ont marqué l'histoire de Bitcoin sans en
être développeurs.

## Partie spécifications

### BIP

Pictogramme : `bip` (existant). Entrées : 194.

Une définition par Bitcoin Improvement Proposal numérotée (BIP-0032, BIP-0341…). Le terme générique
« BIP » reste dans la catégorie « Évolution du protocole ».

### BOLT

Pictogramme : `bolt` (nouveau). Entrées : 12.

Une définition par spécification Basis of Lightning Technology numérotée (BOLT-02, BOLT-11…). Le
terme générique « BOLT » reste dans la catégorie « Lightning Network ».

### BLIP

Pictogramme : `blip` (nouveau). Entrées : 14.

Une définition par Bitcoin Lightning Improvement Proposal numérotée (bLIP-0001…). Le terme générique
« bLIP » reste dans la catégorie « Lightning Network ».

### NIP

Pictogramme : `nip` (nouveau). Entrées : 0.

Une définition par Nostr Implementation Possibility numérotée (NIP-05…). Le terme générique « NIP »
reste dans la catégorie « Nostr ».

## Catégories écartées

* ECASH : `cashu`, `fedimint`, `ecash-david-chaum`, `blind-oracle`, soit 4 entrées, sous le seuil de
  5. Cashu et Fedimint restent dans COUCHE SUPÉRIEURE ; la catégorie se crée dès qu'un cinquième
  terme arrive (*mint*, *guardian*…).
* CONTRATS (DLC, oracles) : `dlc-discreet-log-contract`, `cet`, `oracle`, `blind-oracle`, 4 entrées.
  Même traitement.
* MÉDIA dans l'écosystème : `bitcoin-magazine`, `bitcointalk`, `bitcoin-dev`, 3 entrées, fondues
  dans COMMUNAUTÉ ET FONDATION.
* COMMUNAUTÉ dans la partie technique : une fois les produits et les rôles de Bitcoin Core sortis, il
  restait 2 termes (`maximaliste`, `stacker`), rangés dans HISTOIRE ET CULTURE.
* RÉGULATION séparée d'ÉCONOMIE : une dizaine d'entrées seulement, et ÉCONOMIE ET RÉGULATION reste à
  55.

## Cas limites

* `git`, `github`, `gitlab`, `sourceforge`, `unix`, `gnu` : INFORMATIQUE, logiciels ou services
  nommés mais généralistes, sans lien propre avec l'écosystème Bitcoin.
* `leveldb`, `berkeleydb`, `zmq-zeromq`, `grpc` : INFORMATIQUE, bibliothèques généralistes utilisées
  par Bitcoin Core ou LND, pas des produits de l'écosystème Bitcoin.
* Fichiers de Bitcoin Core (29 entrées : `blk-dat`, `chainstate`, `debug-log`, `peers-dat`,
  `wallet-dat`, `bitcoin-conf`…) : FONCTIONNEMENT DU NŒUD, éléments techniques et non produits.
* `bitcoind`, `bitcoin-qt`, `bitcoin-cli` : IMPLÉMENTATION, programmes livrés avec Bitcoin Core.
* `bitcoin-xt`, `bitcoin-classic`, `bitcoin-unlimited` : IMPLÉMENTATION, logiciels de nœud, même si
  les fiches les présentent par le débat sur la taille des blocs.
* `segwit2x` : HISTOIRE ET CULTURE, tentative de hard fork racontée comme un événement, pas un
  logiciel.
* `elements` : IMPLÉMENTATION, plateforme logicielle dont Liquid est la principale mise en
  production ; `liquid-network` reste en SIDECHAIN.
* `tapd` : IMPLÉMENTATION plutôt que LOGICIEL LIGHTNING, implémentation de référence de Taproot
  Assets.
* `neutrino` : IMPLÉMENTATION, la fiche décrit le client léger de Lightning Labs ; le mécanisme est
  `compact-block-filters` (RÉSEAU).
* `electrum-server`, `explorateur-de-bloc` : FONCTIONNEMENT DU NŒUD, types génériques ; `electrs`,
  `fulcrum`, `esplora`, `mempool-space` vont en écosystème.
* `hwi` : OUTIL DE DÉVELOPPEMENT, la fiche dit « bibliothèque en Python et outil en ligne de
  commande ».
* `joinmarket`, `coinmux` : OUTIL DE CONFIDENTIALITÉ, les fiches les ouvrent sur « Implémentation de
  coinjoin » ; `whirlpool`, `wabisabi`, `zerolink`, `soroban`, `joinstr` restent des protocoles.
* `bitcoin-fog`, `sharedcoin` : OUTIL DE CONFIDENTIALITÉ plutôt que SERVICE ET PAIEMENT, services de
  mixage.
* `autoloop`, `loop-in`, `loop-out` : LIGHTNING NETWORK, fonctions de Lightning Loop qui décrivent un
  mécanisme de swap ; `loop` va en LOGICIEL LIGHTNING.
* `channel-db`, `channel-acceptor`, `scb-static-channel-backup` : LIGHTNING NETWORK, mécanismes de
  LND, traités comme les fichiers de Bitcoin Core.
* `channel-lease`, `sidecar-ticket` : LIGHTNING NETWORK, mécanismes de Lightning Pool ; `pool-lightning`
  va en LOGICIEL LIGHTNING.
* `key-teleport` : PORTEFEUILLE, fonction des Coldcard décrite comme un mécanisme.
* `cahoots` : CONFIDENTIALITÉ, transactions collaboratives implémentées par plusieurs portefeuilles.
* `lightning-service-provider` : LIGHTNING NETWORK, rôle générique et non entreprise nommée.
* `mining-management-software` : MINAGE, type de logiciel générique.
* `bitcoin-atm`, `bitcoin-treasury-company`, `etf` : ÉCONOMIE ET RÉGULATION, types génériques.
* `boltz` : LOGICIEL LIGHTNING plutôt que SERVICE ET PAIEMENT, service de swaps Lightning et
  on-chain.
* `btcpay-server` : SERVICE ET PAIEMENT, logiciel auto-hébergé rangé selon son usage (processeur de
  paiement).
* `coinos` : PORTEFEUILLE LOGICIEL, application web d'envoi et de réception.
* `casascius` : PORTEFEUILLE MATÉRIEL, pièces physiques au porteur.
* `krux`, `frostsnap` : PORTEFEUILLE MATÉRIEL, firmware de signature et dispositifs FROST.
* `start9`, `nodl` : ENTREPRISE, les fiches présentent l'entreprise ; `umbrel` (le logiciel) va en
  NŒUD ET EXPLORATEUR.
* `bitmain`, `canaan`, `luxor`, `mara`, `riot-platforms` : ACTEURS DU MINAGE plutôt qu'ENTREPRISE,
  le secteur l'emporte.
* `spiral` : ENTREPRISE, filiale de Block, alors qu'OpenSats et Btrust vont en COMMUNAUTÉ ET
  FONDATION.
* `chaincode-labs`, `mit-dci` : COMMUNAUTÉ ET FONDATION, centres de recherche sans produit.
* `risc-zero` : ENTREPRISE, la fiche s'ouvre sur « Entreprise et framework ».
* `digicash` : ENTREPRISE ; `e-gold`, `liberty-reserve`, `silk-road`, `satoshidice` : SERVICE ET
  PAIEMENT ; `mtgox` : PLATEFORME D'ÉCHANGE.
* `the-dao` : HISTOIRE ET CULTURE, la fiche porte sur le piratage de 2016 et ses suites.
* `ecash-david-chaum` : HISTOIRE ET CULTURE, protocole de 1982 rangé avec les précurseurs plutôt
  qu'avec Cashu.
* `faucet` : HISTOIRE ET CULTURE, pratique des débuts de Bitcoin.
* `hodl`, `stacker`, `maximaliste`, `proof-of-key-day` : HISTOIRE ET CULTURE, vocabulaire et usages
  de la communauté.
* `proof-of-stake` : ALTCOINS ET FORKS, mécanisme de consensus étranger à Bitcoin.
* `citrea`, `clementine` : ROLLUPS ET BITVM, réseau et pont décrits comme protocoles ;
  `chainway-labs` va en ENTREPRISE.
* `counterparty`, `omni` : ACTIFS SUR BITCOIN, méta-protocoles d'émission d'actifs.
* `opentimestamps` : COUCHE SUPÉRIEURE, protocole d'horodatage ancré dans Bitcoin.
* `mostro` : NOSTR, protocole d'échange construit sur Nostr.
* `zap`, `nwc-nostr-wallet-connect` : NOSTR plutôt que LIGHTNING NETWORK, définis par des NIP.
* `joinpool` : COUCHE SUPÉRIEURE, concept générique, plutôt qu'ARK.
* `exit-transaction` : SPARK ET STATECHAINS, la fiche décrit le cas de Spark.
* `op-cat-0x7e` : COVENANTS, opcode désactivé que le BIP-0347 propose de réactiver dans Tapscript,
  discuté surtout pour les covenants ; `op-eval` et `op-checkhashverify-chv` restent en OPCODES.
* `apo-anyprevout`, `sighash-anyprevout`, `sighash-anyprevoutanyscript` : COVENANTS, proposition
  BIP-0118 discutée comme covenant.
* `vault`, `revault` : PORTEFEUILLE, schémas de conservation ; `op-vault-0xbb` va en COVENANTS.
* `binohash` : COVENANTS, introspection de transaction sans modification du consensus, même
  famille d'usages que les covenants.
* `nlocktime`, `nsequence` : TRANSACTIONS plutôt que SCRIPT, champs de la transaction.
* `multisig` : PORTEFEUILLE plutôt que SCRIPT, la fiche décrit les portefeuilles multisignatures.
* `aezeed` : CLÉS ET DÉRIVATION plutôt que LIGHTNING NETWORK, format de phrase de récupération.
* `mast` : SCRIPT plutôt que CRYPTOGRAPHIE, structure d'arbre de scripts.
* `noise` : LIGHTNING NETWORK, chiffrement des connexions entre nœuds Lightning.
* `difficulte`, `cible-de-difficulte` : laissés en MINAGE alors qu'`ajustement-de-la-difficulte`
  reste en PROTOCOLE ; à regrouper si Loïc préfère.
* `directed-acyclic-graph` : RGB, la fiche décrit le DAG dans le cadre de RGB.
* `blind-oracle` : COUCHE SUPÉRIEURE, avec les oracles.
* `slip`, `contributeur-core`, `mainteneur-core`, `mainteneur-principal-core`, `bounty` : ÉVOLUTION
  DU PROTOCOLE, processus de développement.
* `bitcoin-dev` : COMMUNAUTÉ ET FONDATION, liste de diffusion.
* `nakamoto-satoshi` : DÉVELOPPEUR BITCOIN plutôt que CYPHERPUNK, créateur et premier développeur.
* `finney-hal` : CYPHERPUNK plutôt que CRYPTOGRAPHE ET INFORMATICIEN, sa fiche le décrit comme
  « cypherpunk engagé ».
* `bitcoin-jesus` : FIGURE DE L'ÉCOSYSTÈME, surnom de l'entrepreneur Roger Ver.

## Erreurs de catégorie actuelles

Repérées par rapport aux descriptions actuelles de `templates/categories.yaml`, indépendamment du
découpage 2027.

* Logiciels et produits hors de « OUTIL », alors que les descriptions de PORTEFEUILLE, LIGHTNING
  NETWORK et CONFIDENTIALITÉ les renvoient à « OUTIL » :
  * PORTEFEUILLE : 34 portefeuilles logiciels et matériels (`sparrow-wallet`, `coldcard`, `trezor`…)
    et `hwi`.
  * LIGHTNING NETWORK : 19 logiciels (`lnd`, `eclair`, `cln-core-lightning`, `phoenix`, `zeus`,
    `breez`…).
  * CONFIDENTIALITÉ : 11 logiciels et services (`samourai-wallet`, `joinmarket`, `oxt`, `jam`,
    `bitcoin-fog`…).
  * PROTOCOLE : `bitcoin-core`, `bitcoind`, `bitcoin-qt`, `bitcoin-cli`, `bitcoin-knots`,
    `btcd-btc-suite`, `bcoin`, `libbitcoin`, `libsecp256k1`, `magical-bitcoin`,
    `bitcoin-inquisition`.
  * RÉSEAU : `electrs`, `minisketch`. SIDECHAIN : `elements`.
* `wizardsardine` : COMMUNAUTÉ, alors que c'est une entreprise (ORGANISATION).
* `sortie-non-rentable` : ATTAQUE, alors que la fiche décrit une sortie dont la valeur est inférieure
  au coût de sa dépense ; c'est une notion de transaction.
* `bft-byzantine-fault-tolerance`, `panne-byzantine`, `prob-des-generaux-byzantins` : ATTAQUE, alors
  que ce sont des notions de systèmes distribués.
* `vulnerabilite-de-murch-zawy` : PROTOCOLE, alors que la fiche décrit une attaque théorique.
* `oboe-off-by-one-error` : SCRIPT, alors que c'est une erreur de programmation générale.
* `modele-de-transaction`, `empreinte-de-portefeuille` : PROTOCOLE et PORTEFEUILLE, alors que les
  fiches relèvent de l'analyse de chaîne.
* `premium` : COMMUNAUTÉ, alors que c'est une notion de marché (ÉCONOMIE ET RÉGULATION).
* `demeurage`, `commercant` : PROTOCOLE, alors que ce sont des notions économiques.
* `prime-de-proximite` : PROTOCOLE, alors que la fiche s'ouvre sur « Dans le cadre du minage ».
* `resistance-au-partitionnement` : INFORMATIQUE, alors que la fiche décrit une propriété du réseau
  Bitcoin.
* `p2p-pair-a-pair`, `merkle-block` : PROTOCOLE, alors que la description de PROTOCOLE exclut le
  réseau ; `merkle-block` est un message pair-à-pair du BIP-0037.
* `bare-multisig`, `nested-segwit` (PROTOCOLE) et `segwit-v0`, `segwit-v1` (PORTEFEUILLE) : ce sont
  des modèles et versions de scripts (SCRIPT).
* `cahoots` : PORTEFEUILLE, alors que ce sont des transactions de confidentialité.
* `noise` : RÉSEAU, alors que c'est le chiffrement des connexions Lightning (BOLT-08).
* Nostr réparti entre RÉSEAU (`nostr`, `nip`, `npub`, `nsec`, `relais-nostr`, `evenement-nostr`),
  LIGHTNING NETWORK (`zap`, `nwc-nostr-wallet-connect`) et OUTIL (`mostro`), alors que RÉSEAU désigne
  le réseau de Bitcoin.
* `atomic-swap`, `opentimestamps`, `mostro` : OUTIL, alors que les fiches décrivent une technique ou
  un protocole.
* `leveldb`, `berkeleydb` : PROTOCOLE, alors que ce sont des bibliothèques généralistes
  (INFORMATIQUE).
* `bitcoin-dev` : PROTOCOLE, alors que c'est une liste de diffusion (COMMUNAUTÉ).
* Altcoins incohérents : `litecoin` et `xmr-monero` en ÉCONOMIE ET RÉGULATION, `namecoin`,
  `bch-bitcoin-cash`, `bsv-bitcoin-satoshi-vision`, `btg-bitcoin-gold`, `ecash-xec` en HISTOIRE.
