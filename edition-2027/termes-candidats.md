# Termes candidats pour l'édition 2027

Termes techniques absents du dictionnaire, repérés dans l'index des sujets de Bitcoin Optech, les bulletins Optech de janvier 2024 à octobre 2026, les fils de Delving Bitcoin (`/latest`, `/top`), les sujets de la liste bitcoindev (miroir gnusha.org) et les notes de version de Bitcoin Core 28.0 à 31.0. Critère : un débutant qui étudie Bitcoin peut croiser le terme et vouloir le comprendre. L'informatique quantique et Nostr sont traités à part (`termes-quantique-nostr.md`).

Chaque terme a été comparé aux titres, slugs, `english_term` et `french_term` des 1 408 entrées, à `templates/pending_terms.yaml` et au texte des définitions. Un terme seulement cité dans le corps d'une autre entrée reste candidat. Chaque lien a été ouvert et contient le terme. La catégorie suit `templates/categories.yaml` (55 catégories).

Total : 150 candidats (A : 18, B : 89, C : 43).

- A : terme courant aujourd'hui (Optech, notes de version, débats récents).
- B : terme utile mais plus spécialisé.
- C : terme de niche ou proposition marginale.

## Candidats

| Priorité | Terme | Slug proposé | Catégorie actuelle probable | Où on le croise (2 liens max) | Pourquoi |
|---|---|---|---|---|---|
| A | Bitcoin Kernel (libbitcoinkernel) | `libbitcoinkernel` | IMPLÉMENTATION | [Optech, 19/12/2025](https://bitcoinops.org/en/newsletters/2025/12/19/) ; [Optech, 17/07/2026](https://bitcoinops.org/en/newsletters/2026/07/17/) | Bibliothèque qui isole le code de consensus de Bitcoin Core ; son API C est entrée dans Bitcoin Core en 2025 (revue Optech de l'année). |
| A | Budget de sécurité (security budget) | `budget-de-securite` | ÉCONOMIE ET RÉGULATION | [Delving Bitcoin](https://delvingbitcoin.org/t/addressing-the-diminishing-block-subsidy/2640) ; [Delving Bitcoin](https://delvingbitcoin.org/t/is-it-time-to-increase-the-blocksize-cap/941) | Expression reprise dans les débats sur la baisse de la subvention de bloc et sur la taille des blocs ; aucune entrée ne la définit. |
| A | Collision (fonction de hachage) | `collision` | CRYPTOGRAPHIE | [Optech, 13/03/2026](https://bitcoinops.org/en/newsletters/2026/03/13/) ; [bitcoindev](https://gnusha.org/pi/bitcoindev/CAEM=y+W2jyFoJAq9XrE9whQ7EZG4HRST01TucWHJtBhQiRTSNQ@mail.gmail.com/T/) | Notion de base des fonctions de hachage, citée dans 6 définitions et dans les fils sur ColliderScript ; aucune entrée. |
| A | datacarriersize | `datacarriersize` | MEMPOOL ET FRAIS | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 26/06/2026](https://bitcoinops.org/en/newsletters/2026/06/26/) | Option qui borne la taille des sorties OP_RETURN relayées, objet du débat de 2025 ; Bitcoin Core 30.0 la porte à 100 000 par défaut. |
| A | Delving Bitcoin | `delving-bitcoin` | COMMUNAUTÉ ET FONDATION | [Delving Bitcoin](https://delvingbitcoin.org/t/public-archive-for-delving-bitcoin/87) ; [Optech, 14/02/2024](https://bitcoinops.org/en/newsletters/2024/02/14/) | Forum de discussion technique cité dans 121 des 146 bulletins Optech de 2024 à 2026 ; bitcoin-dev a déjà son entrée, pas ce forum. |
| A | Divulgation responsable (responsible disclosure) | `divulgation-responsable` | INFORMATIQUE | [Optech, sujet](https://bitcoinops.org/en/topics/responsible-disclosures/) ; [Optech, 04/09/2026](https://bitcoinops.org/en/newsletters/2026/09/04/) | Sujet Optech lié dans 26 bulletins depuis 2024, à chaque annonce de faille corrigée dans Bitcoin Core ou une implémentation Lightning. |
| A | Estimation des frais (fee estimation) | `estimation-des-frais` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/fee-estimation/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/mempool-based-fee-estimation-on-bitcoin-core/703) | Sujet Optech lié dans 25 bulletins de 2024 à 2026, utilisé par tout portefeuille ; le dictionnaire n'a que le fichier fee-estimates-dat. |
| A | Key path (chemin de clé) | `key-path` | SCRIPT | [Optech, 07/08/2026](https://bitcoinops.org/en/newsletters/2026/08/07/) ; [Optech, 20/02/2026](https://bitcoinops.org/en/newsletters/2026/02/20/) | Dépense d'une sortie Taproot par la seule clé ; revient avec CISA et P2MR, expliquée seulement dans p2tr et taproot. |
| A | Lightning Address | `lightning-address` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/lnurl/) ; [Optech, 21/08/2026](https://bitcoinops.org/en/newsletters/2026/08/21/) | Identifiant de type courriel pour recevoir en Lightning, repris par BIP-0353 ; seule breez le mentionne. |
| A | minrelaytxfee (frais de relais minimum) | `minrelaytxfee` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/default-minimum-transaction-relay-feerates/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/changing-the-minimum-relay-feerate/1886) | Seuil sous lequel un nœud ne relaie pas une transaction ; Bitcoin Core 30.0 l'abaisse à 0,1 sat/vB. Cité dans 3 définitions sans entrée propre. |
| A | P2A (Pay-to-Anchor) | `p2a` | SCRIPT | [Optech, sujet](https://bitcoinops.org/en/topics/ephemeral-anchors/) ; [Bitcoin Core 28.0](https://bitcoincore.org/en/releases/28.0/) | Type de sortie standard depuis Bitcoin Core 28.0 pour les ancres de frais ; décrit seulement dans bip-0433 et ephemeral-anchors. |
| A | Portefeuille à descripteurs (descriptor wallet) | `descriptor-wallet` | PORTEFEUILLE | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 09/01/2026](https://bitcoinops.org/en/newsletters/2026/01/09/) | Seul format de portefeuille de Bitcoin Core depuis la version 30.0, qui ne charge plus les portefeuilles BDB ; output-script-descriptors ne couvre pas le portefeuille. |
| A | Preuve de Merkle (Merkle proof) | `preuve-de-merkle` | CRYPTOGRAPHIE | [Optech, 06/09/2024](https://bitcoinops.org/en/newsletters/2024/09/06/) ; [Optech, 19/07/2024](https://bitcoinops.org/en/newsletters/2024/07/19/) | Base de la vérification SPV et du débat sur les transactions de 64 octets ; seule arbre-de-merkle l'aborde. |
| A | Script path (chemin de script) | `script-path` | SCRIPT | [Optech, 25/07/2025](https://bitcoinops.org/en/newsletters/2025/07/25/) ; [Optech, 28/02/2025](https://bitcoinops.org/en/newsletters/2025/02/28/) | Dépense Taproot par une feuille de script et un *control block* ; citée dans 7 définitions sans entrée propre. |
| A | Spam (débat sur les données arbitraires) | `spam` | MEMPOOL ET FRAIS | [Delving Bitcoin](https://delvingbitcoin.org/t/bug-spammers-get-bitcoin-blockspace-at-discounted-price-lets-fix-it/327) ; [Delving Bitcoin](https://delvingbitcoin.org/t/dust-expiry-clean-the-utxo-set-from-spam/1707) | Mot employé dans les débats sur les données arbitraires (BRC-20, poussière, OP_RETURN) ; une définition neutre aide à suivre ces fils. |
| A | Transaction orpheline (orphan transaction) | `transaction-orpheline` | MEMPOOL ET FRAIS | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 14/02/2025](https://bitcoinops.org/en/newsletters/2025/02/14/) | Transaction dont le parent est inconnu du nœud ; Bitcoin Core 30.0 a revu l'*orphanage* qui les garde. Le dictionnaire n'a que le bloc orphelin. |
| A | TRUC (Topologically Restricted Until Confirmation) | `truc-topologically-restricted-until-confirmation` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/version-3-transaction-relay/) ; [Bitcoin Core 28.0](https://bitcoincore.org/en/releases/28.0/) | Transactions de version 3 standard depuis Bitcoin Core 28.0, base des parades au *pinning* ; seule l'entrée bip-0431 en parle et elle part dans la partie Spécifications. |
| A | Witness discount (remise sur les données de témoin) | `witness-discount` | TRANSACTIONS | [Delving Bitcoin](https://delvingbitcoin.org/t/bug-spammers-get-bitcoin-blockspace-at-discounted-price-lets-fix-it/327) ; [Optech, 02/10/2026](https://bitcoinops.org/en/newsletters/2026/10/02/) | Le poids réduit des données de témoin revient dans les débats sur les inscriptions et sur les signatures post-quantiques ; seule vbytes l'évoque. |
| B | 1P1C (one parent, one child) | `1p1c-one-parent-one-child` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/package-relay/) ; [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) | Relais d'un parent à faibles frais avec son enfant, depuis Bitcoin Core 28.0 et étendu en 30.0 ; mentionné dans package-relay. |
| B | Accumulateur cryptographique | `accumulateur` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/utreexo/) ; [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) | Structure qui résume un ensemble et prouve l'appartenance (Utreexo, MuHash) ; citée dans 7 définitions sans entrée. |
| B | Agrégation de signatures (half et full aggregation) | `agregation-de-signatures` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/cross-input-signature-aggregation/) ; [Optech, 24/07/2026](https://bitcoinops.org/en/newsletters/2026/07/24/) | Agrégation partielle ou complète de signatures Schnorr, avec un brouillon de BIP en 2026 ; cisa existe, pas le terme général. |
| B | Attaque des anniversaires (birthday attack) | `attaque-des-anniversaires` | ATTAQUE | [Optech, 11/04/2025](https://bitcoinops.org/en/newsletters/2025/04/11/) | Attaque générique sur les fonctions de hachage, citée à propos de MuHash ; complète l'entrée collision. |
| B | Attaque par canal auxiliaire (side-channel attack) | `attaque-par-canal-auxiliaire` | ATTAQUE | [Optech, sujet](https://bitcoinops.org/en/topics/side-channels/) ; [Optech, 23/08/2024](https://bitcoinops.org/en/newsletters/2024/08/23/) | Attaque qui exploite le temps de calcul ou la consommation d'un appareil de signature ; sujet Optech, seule secure-element l'évoque. |
| B | Attributable failures | `attributable-failures` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/attributable-failures/) ; [Optech, 30/05/2025](https://bitcoinops.org/en/newsletters/2025/05/30/) | Messages d'erreur Lightning qui désignent le nœud responsable d'un échec de paiement ; sujet Optech. |
| B | Bitcoin Stack Exchange | `bitcoin-stack-exchange` | COMMUNAUTÉ ET FONDATION | [Optech, 27/03/2026](https://bitcoinops.org/en/newsletters/2026/03/27/) ; [Optech, 25/09/2026](https://bitcoinops.org/en/newsletters/2026/09/25/) | Site de questions et réponses dont Optech publie une sélection régulière ; aucune entrée. |
| B | BitVM2 | `bitvm2` | ROLLUPS ET BITVM | [Optech, 24/01/2025](https://bitcoinops.org/en/newsletters/2025/01/24/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/how-ctv-csfs-improves-bitvm-bridges/1591) | Version de BitVM utilisée par le *bridge* Strata (2025) ; citée dans citrea et clementine, pas dans bitvm. |
| B | Blocksonly (mode) | `blocksonly` | FONCTIONNEMENT DU NŒUD | [Optech, 10/07/2026](https://bitcoinops.org/en/newsletters/2026/07/10/) | Mode de nœud qui ne relaie pas les transactions ; cité dans les discussions sur les *compact blocks*. Aucune entrée. |
| B | Bridge (pont vers une surcouche) | `bridge` | ROLLUPS ET BITVM | [Delving Bitcoin](https://delvingbitcoin.org/t/how-ctv-csfs-improves-bitvm-bridges/1591) ; [Optech, 24/01/2025](https://bitcoinops.org/en/newsletters/2025/01/24/) | Mot courant pour les liaisons vers les surcouches (BitVM, Citrea) ; cité dans 7 définitions sans entrée propre. |
| B | Canal zero-conf (zero-conf channel) | `zero-conf-channel` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/zero-conf-channels/) ; [Optech, 16/10/2026](https://bitcoinops.org/en/newsletters/2026/10/16/) | Canal utilisable avant que sa transaction d'ouverture soit confirmée ; sujet Optech, cité seulement dans swap-in-potentiam. |
| B | Chain Code Delegation | `chain-code-delegation` | PORTEFEUILLE | [Delving Bitcoin](https://delvingbitcoin.org/t/chain-code-delegation-private-access-control-for-bitcoin-keys/1837) ; [Optech, 19/12/2025](https://bitcoinops.org/en/newsletters/2025/12/19/) | Mécanisme de 2025 pour les multisig avec un cosignataire qui ne voit pas les transactions ; seule l'entrée bip-0089 le décrit. |
| B | ChillDKG | `chilldkg` | CRYPTOGRAPHIE | [Optech, 03/01/2025](https://bitcoinops.org/en/newsletters/2025/01/03/) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Protocole de génération de clés distribuée pour FROST, en brouillon de BIP depuis 2024 ; dkg existe, pas ce protocole. |
| B | Chunk (mempool en clusters) | `chunk` | MEMPOOL ET FRAIS | [Bitcoin Core 31.0](https://bitcoincore.org/en/releases/31.0/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/post-clustermempool-package-rbf-per-chunk-processing/190) | Groupe de transactions d'un cluster triées ensemble par taux de frais dans Bitcoin Core 31.0 ; cluster-mempool l'effleure. |
| B | Circuits brouillés (garbled circuits) | `garbled-circuits` | CRYPTOGRAPHIE | [Optech, 30/01/2026](https://bitcoinops.org/en/newsletters/2026/01/30/) ; [Optech, 29/08/2025](https://bitcoinops.org/en/newsletters/2025/08/29/) | Technique cryptographique derrière les « garbled locks » et les contrats de type BitVM ; citée dans 3 bulletins récents. |
| B | Clé interne (internal key, Taproot) | `internal-key` | SCRIPT | [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) ; [Optech, 21/08/2026](https://bitcoinops.org/en/newsletters/2026/08/21/) | Clé de départ d'une sortie Taproot avant le *tweak* ; à distinguer de la chaîne interne (chaine-interne). |
| B | Clé NUMS (nothing-up-my-sleeve) | `nums-nothing-up-my-sleeve` | CRYPTOGRAPHIE | [Delving Bitcoin](https://delvingbitcoin.org/t/unspendable-keys-in-descriptors/304) ; [Optech, 24/01/2025](https://bitcoinops.org/en/newsletters/2025/01/24/) | Clé publique sans clé privée connue, qui désactive le *key path* Taproot ; brouillons de BIP en 2025 et 2026. |
| B | CLTV expiry delta | `cltv-expiry-delta` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/cltv-expiry-delta/) ; [Optech, 23/10/2026](https://bitcoinops.org/en/newsletters/2026/10/23/) | Marge de temps qu'un nœud Lightning réserve à chaque saut ; sujet Optech, seule replacement-cycling la nomme. |
| B | Compatibilité incitative (incentive compatibility) | `compatibilite-incitative` | MEMPOOL ET FRAIS | [Delving Bitcoin](https://delvingbitcoin.org/t/mempool-incentive-compatibility/553) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Principe qui guide les règles de mempool et de RBF : un mineur doit gagner à les suivre. Aucune entrée ne le définit. |
| B | CPFP carve-out | `cpfp-carve-out` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/cpfp-carve-out/) ; [Bitcoin Core 31.0](https://bitcoincore.org/en/releases/31.0/) | Exception de mempool utilisée par Lightning, retirée dans Bitcoin Core 31.0 au profit de TRUC et de la *sibling eviction*. |
| B | CVE (Common Vulnerabilities and Exposures) | `cve-common-vulnerabilities-and-exposures` | INFORMATIQUE | [Optech, sujet](https://bitcoinops.org/en/topics/cve/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/cve-2024-38365-public-disclosure-btcd-findanddelete-bug/1184) | Identifiant public des failles que citent toutes les annonces de sécurité ; sujet Optech. |
| B | CVE-2018-17144 (entrées dupliquées) | `cve-2018-17144` | HISTOIRE ET CULTURE | [Optech, sujet](https://bitcoinops.org/en/topics/cve-2018-17144/) ; [Optech, 23/01/2026](https://bitcoinops.org/en/newsletters/2026/01/23/) | Faille de Bitcoin Core découverte en 2018 qui laissait un bloc dépenser deux fois la même entrée ; Rust Bitcoin s'y réfère encore en janvier 2026. Aucune entrée. |
| B | Dark Skippy | `dark-skippy` | ATTAQUE | [Optech, 09/08/2024](https://bitcoinops.org/en/newsletters/2024/08/09/) ; [Optech, sujet](https://bitcoinops.org/en/topics/exfiltration-resistant-signing/) | Attaque d'exfiltration rapide de la graine par un appareil de signature piégé, publiée en 2024 ; seule anti-exfil-signing la cite. |
| B | DATUM | `datum` | POOLS DE MINAGE | [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) ; [Optech, 18/10/2024](https://bitcoinops.org/en/newsletters/2024/10/18/) | Protocole d'OCEAN qui laisse le mineur construire son modèle de bloc, annoncé en 2024 ; ocean ne le cite pas. |
| B | dbcache | `dbcache` | FONCTIONNEMENT DU NŒUD | [Bitcoin Core 31.0](https://bitcoincore.org/en/releases/31.0/) ; [Optech, 24/04/2026](https://bitcoinops.org/en/newsletters/2026/04/24/) | Réglage de mémoire qui accélère l'IBD ; Bitcoin Core 31.0 le porte à 1 024 Mio par défaut sur les machines d'au moins 4 096 Mio de RAM. |
| B | Éditeur de BIP (BIP editor) | `editeur-de-bip` | ÉVOLUTION DU PROTOCOLE | [Optech, 24/04/2024](https://bitcoinops.org/en/newsletters/2024/04/24/) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Rôle débattu en 2024, quand cinq éditeurs ont été ajoutés ; champion existe, pas ce rôle. |
| B | Ephemeral dust | `ephemeral-dust` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/ephemeral-anchors/) ; [Optech, 22/05/2026](https://bitcoinops.org/en/newsletters/2026/05/22/) | Sortie de poussière tolérée si elle est dépensée dans le même paquet ; seulement mentionnée dans ephemeral-anchors. |
| B | External signer (signataire externe) | `external-signer` | PORTEFEUILLE | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 02/05/2025](https://bitcoinops.org/en/newsletters/2025/05/02/) | Interface de Bitcoin Core pour signer avec un appareil externe ; réactivée sous Windows dans la version 30.0. |
| B | Feerate diagram (diagramme de taux de frais) | `feerate-diagram` | MEMPOOL ET FRAIS | [Bitcoin Core 31.0](https://bitcoincore.org/en/releases/31.0/) ; [Optech, 28/11/2025](https://bitcoinops.org/en/newsletters/2025/11/28/) | Critère d'acceptation des remplacements RBF dans Bitcoin Core 31.0 ; absent du dictionnaire. |
| B | Frais exogènes et endogènes | `frais-exogenes` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/fee-sourcing/) ; [Optech, 31/01/2024](https://bitcoinops.org/en/newsletters/2024/01/31/) | Frais apportés par une entrée externe plutôt que pris dans le contrat, distinction qui revient dans les débats sur CTV et Lightning ; sujet Optech. |
| B | Frais hors bande (out-of-band fees) | `out-of-band-fees` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/out-of-band-fees/) ; [Optech, 06/06/2025](https://bitcoinops.org/en/newsletters/2025/06/06/) | Frais payés au mineur hors de la transaction ; Optech y voit un risque de centralisation du minage. |
| B | Free relay (relais gratuit) | `free-relay` | ATTAQUE | [Optech, sujet](https://bitcoinops.org/en/topics/free-relay/) ; [Optech, 07/08/2026](https://bitcoinops.org/en/newsletters/2026/08/07/) | Attaque qui fait relayer des données sans payer les frais correspondants ; sujet Optech et plusieurs divulgations en 2024. |
| B | Fuzzing | `fuzzing` | INFORMATIQUE | [Delving Bitcoin](https://delvingbitcoin.org/t/differential-fuzzing-of-bitcoin-implementations/208) ; [Optech, 29/08/2025](https://bitcoinops.org/en/newsletters/2025/08/29/) | Méthode de test citée dans 15 bulletins Optech, y compris le *fuzzing* différentiel entre implémentations ; absente du dictionnaire. |
| B | GETDATA (message P2P) | `getdata` | RÉSEAU | [Optech, 05/07/2024](https://bitcoinops.org/en/newsletters/2024/07/05/) ; [Optech, 31/05/2024](https://bitcoinops.org/en/newsletters/2024/05/31/) | Message P2P qui demande un bloc ou une transaction annoncés ; aucune entrée. |
| B | Great Script Restoration | `great-script-restoration` | ÉVOLUTION DU PROTOCOLE | [Delving Bitcoin](https://delvingbitcoin.org/t/benchmarking-bitcoin-script-evaluation-for-the-varops-budget-great-script-restoration/2094) ; [Optech, 19/12/2025](https://bitcoinops.org/en/newsletters/2025/12/19/) | Série de quatre BIP qui rétablirait des opcodes désactivés sous un budget de calcul ; résumée par Optech en 2025. |
| B | Guix | `guix` | INFORMATIQUE | [Optech, sujet](https://bitcoinops.org/en/topics/reproducible-builds/) ; [Optech, 14/08/2026](https://bitcoinops.org/en/newsletters/2026/08/14/) | Outil de compilation reproductible qui produit les binaires officiels de Bitcoin Core. |
| B | Hachage quadratique (quadratic hashing) | `hachage-quadratique` | ATTAQUE | [Optech, 13/02/2026](https://bitcoinops.org/en/newsletters/2026/02/13/) | Coût de validation des scripts *legacy* qui croît au carré ; Bitcoin Core a ajouté en 2026 un cache qui le réduit. |
| B | Hashlock | `hashlock` | SCRIPT | [Optech, sujet](https://bitcoinops.org/en/topics/htlc/) | Condition de dépense par révélation d'une préimage, moitié d'un HTLC ; seule bip-0199 la nomme. |
| B | Headers presync | `headers-presync` | FONCTIONNEMENT DU NŒUD | [Optech, 02/10/2026](https://bitcoinops.org/en/newsletters/2026/10/02/) ; [Optech, 21/03/2025](https://bitcoinops.org/en/newsletters/2025/03/21/) | Étape anti-DoS de l'IBD qui a permis à Bitcoin Core de retirer les checkpoints en 2025. |
| B | Inbound fees (frais entrants) | `inbound-fees` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/inbound-forwarding-fees/) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Frais de routage appliqués à l'entrée d'un canal, introduits par LND en 2024 ; sujet Optech. |
| B | Introspection | `introspection` | COVENANTS | [Delving Bitcoin](https://delvingbitcoin.org/t/op-cc-a-simple-introspection-opcode-to-enable-cheaper-consolidations/2177) ; [Optech, 07/08/2026](https://bitcoinops.org/en/newsletters/2026/08/07/) | Capacité d'un script à lire la transaction qui le dépense, au centre des propositions de covenants ; citée dans 7 définitions. |
| B | INV (message P2P) | `inv` | RÉSEAU | [Optech, 14/03/2025](https://bitcoinops.org/en/newsletters/2025/03/14/) | Message P2P d'annonce des transactions et des blocs, cité dans les analyses de trafic des nœuds ; aucune entrée. |
| B | Job Declaration (Stratum V2) | `job-declaration` | POOLS DE MINAGE | [Delving Bitcoin](https://delvingbitcoin.org/t/pplns-with-job-declaration/1099) ; [Optech, 10/07/2026](https://bitcoinops.org/en/newsletters/2026/07/10/) | Rôle de Stratum V2 qui laisse le mineur choisir ses transactions ; stratum-v2 ne le détaille pas. |
| B | Legacy wallet (portefeuille hérité) | `legacy-wallet` | PORTEFEUILLE | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 09/01/2026](https://bitcoinops.org/en/newsletters/2026/01/09/) | Ancien format BDB de Bitcoin Core, retiré en 30.0 ; un bug de migration a été signalé en janvier 2026. |
| B | Libre Relay | `libre-relay` | IMPLÉMENTATION | [Optech, 28/03/2025](https://bitcoinops.org/en/newsletters/2025/03/28/) ; [bitcoindev](https://gnusha.org/pi/bitcoindev/Znbf17x8TWuGBTYr@petertodd.org/T/) | Variante de Bitcoin Core de Peter Todd aux règles de relais plus larges (remplacements, annexe Taproot). |
| B | Linéarisation de cluster (cluster linearization) | `linearisation-de-cluster` | MEMPOOL ET FRAIS | [Delving Bitcoin](https://delvingbitcoin.org/t/how-to-linearize-your-cluster/303) ; [Optech, sujet](https://bitcoinops.org/en/topics/cluster-mempool/) | Algorithme qui ordonne les transactions d'un cluster, fondement du mempool de Bitcoin Core 31.0 ; seule cluster-mempool l'évoque. |
| B | LN-Penalty | `ln-penalty` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/ln-penalty/) ; [Optech, 04/04/2025](https://bitcoinops.org/en/newsletters/2025/04/04/) | Nom du mécanisme de punition des canaux actuels, opposé à LN-Symmetry ; sujet Optech, aucune entrée sous ce nom. |
| B | LNHANCE | `lnhance` | COVENANTS | [Delving Bitcoin](https://delvingbitcoin.org/t/lnhance-bips-and-implementation/376) ; [Optech, 22/11/2024](https://bitcoinops.org/en/newsletters/2024/11/22/) | Paquet de soft fork proposé en 2024 (CTV, CSFS, INTERNALKEY, puis PAIRCOMMIT) ; aucune entrée ne le nomme. |
| B | Low-R grinding | `low-r-grinding` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/low-r-grinding/) ; [Optech, 25/09/2026](https://bitcoinops.org/en/newsletters/2026/09/25/) | Technique qui fait gagner un octet aux signatures ECDSA ; sujet Optech et brouillon de BIP informatif en 2026. |
| B | LSPS (spécifications LSP) | `lsps` | LIGHTNING NETWORK | [Optech, 09/10/2026](https://bitcoinops.org/en/newsletters/2026/10/09/) ; [Optech, 26/06/2026](https://bitcoinops.org/en/newsletters/2026/06/26/) | Spécifications communes des LSP (LSPS0 à LSPS5) ; décrites une par une dans les entrées blip-0050 et suivantes, qui partent dans les Spécifications. |
| B | MEV (Miner Extractable Value) | `mev-miner-extractable-value` | MINAGE | [Delving Bitcoin](https://delvingbitcoin.org/t/ephemeral-anchors-and-mevil/383) ; [Optech, 17/01/2024](https://bitcoinops.org/en/newsletters/2024/01/17/) | Revenu qu'un mineur tire de l'ordre ou du choix des transactions ; discuté pour les ancres et les places de marché de modèles de blocs. |
| B | Multiprocess (bitcoin-node, IPC) | `multiprocess` | IMPLÉMENTATION | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Optech, 10/07/2026](https://bitcoinops.org/en/newsletters/2026/07/10/) | Découpage de Bitcoin Core en processus séparés, dont dépend l'interface de minage IPC expérimentale de la version 30.0. |
| B | NAT-PMP | `nat-pmp` | RÉSEAU | [Bitcoin Core 30.0](https://bitcoincore.org/en/releases/30.0/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/tcp-hole-punching-for-bitcoin-nodes-behind-home-nats/2497) | Protocole d'ouverture de port activé par défaut dans Bitcoin Core 30.0 pour accepter des connexions entrantes. |
| B | Node fingerprinting (empreinte de nœud) | `node-fingerprinting` | CONFIDENTIALITÉ | [Delving Bitcoin](https://delvingbitcoin.org/t/fingerprinting-nodes-via-addr-requests/1786) ; [Optech, 27/06/2025](https://bitcoinops.org/en/newsletters/2025/06/27/) | Recoupement d'un même nœud sur plusieurs réseaux à partir de ses messages P2P (addr) ; travaux publiés en 2025 et 2026. |
| B | OP_CHECKCONTRACTVERIFY (OP_CCV) | `op-checkcontractverify-0xbb` | COVENANTS | [Optech, sujet](https://bitcoinops.org/en/topics/matt/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/op-checkcontractverify-and-its-amount-semantic/1527) | Opcode de covenant de Salvatore Ingala (BIP-0443) ; matt et bip-0443 l'évoquent, sans entrée d'opcode comme op-checksigfromstack-0xcc. |
| B | OP_PAIRCOMMIT | `op-paircommit-0xcd` | COVENANTS | [Delving Bitcoin](https://delvingbitcoin.org/t/op-paircommit-as-a-candidate-for-addition-to-lnhance/1216) ; [Optech, 02/10/2026](https://bitcoinops.org/en/newsletters/2026/10/02/) | Opcode candidat au paquet LNHANCE (BIP-0442) ; aucune entrée d'opcode. |
| B | OP_TEMPLATEHASH | `op-templatehash-0xce` | COVENANTS | [Delving Bitcoin](https://delvingbitcoin.org/t/ctv-op-templatehash-and-op-inputamounts/1344) ; [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) | Variante de CTV pour Tapscript (BIP-0446), proposée avec CSFS et INTERNALKEY ; liée dans 16 bulletins. |
| B | Package RBF | `package-rbf` | MEMPOOL ET FRAIS | [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) ; [Optech, 11/10/2024](https://bitcoinops.org/en/newsletters/2024/10/11/) | Remplacement d'un paquet parent et enfant, activé sous une forme limitée dans Bitcoin Core 28.0. |
| B | Payment secret | `payment-secret` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/payment-secrets/) ; [Optech, 11/07/2025](https://bitcoinops.org/en/newsletters/2025/07/11/) | Champ des factures BOLT11 que le payeur doit trouver avant de payer ; sujet Optech, absent du dictionnaire. |
| B | Peer storage | `peer-storage` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/peer-storage/) ; [Optech, 19/12/2025](https://bitcoinops.org/en/newsletters/2025/12/19/) | Sauvegarde chiffrée de l'état d'un canal chez son pair, ajoutée à Core Lightning 25.02 ; sujet Optech. |
| B | Pickhardt payments (flux à coût minimal) | `pickhardt-payments` | PAIEMENTS LIGHTNING | [Optech, 29/11/2024](https://bitcoinops.org/en/newsletters/2024/11/29/) ; [Optech, 23/01/2026](https://bitcoinops.org/en/newsletters/2026/01/23/) | Routage par flux à coût minimal issu des travaux de René Pickhardt, utilisé par le plugin askrene de Core Lightning. |
| B | Preuve de fraude (fraud proof) | `preuve-de-fraude` | ROLLUPS ET BITVM | [Optech, 08/05/2026](https://bitcoinops.org/en/newsletters/2026/05/08/) ; [Optech, 20/02/2026](https://bitcoinops.org/en/newsletters/2026/02/20/) | Preuve qu'une partie a triché, base des schémas optimistes (BitVM, rollups, canaux JIT) ; seules rollup et bip-0180 l'évoquent. |
| B | Preuve de paiement (proof of payment) | `preuve-de-paiement` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/proof-of-payment/) ; [Optech, 02/05/2025](https://bitcoinops.org/en/newsletters/2025/05/02/) | Garantie qu'un paiement a eu lieu (en Lightning, la préimage) ; sujet Optech sans entrée dédiée. |
| B | Preuve de validité (validity proof) | `preuve-de-validite` | CRYPTOGRAPHIE | [Optech, 23/10/2026](https://bitcoinops.org/en/newsletters/2026/10/23/) ; [bitcoindev](https://gnusha.org/pi/bitcoindev/8DFE4646-9E8B-4A92-BBA2-EBD4A785C1D3@zerosync.org/T/) | Preuve qu'un calcul est correct (ZeroSync, rollups), pendant de la preuve de fraude ; aucune entrée. |
| B | Preuve DLEQ (Discrete Log Equality) | `dleq-discrete-log-equality` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/discrete-log-equivalency/) ; [Optech, 01/11/2024](https://bitcoinops.org/en/newsletters/2024/11/01/) | Preuve d'égalité de logarithmes discrets utilisée pour envoyer des silent payments ; seule l'entrée bip-0374 la décrit. |
| B | Private broadcast (diffusion privée) | `private-broadcast` | CONFIDENTIALITÉ | [Bitcoin Core 31.0](https://bitcoincore.org/en/releases/31.0/) ; [Optech, sujet](https://bitcoinops.org/en/topics/transaction-origin-privacy/) | Option de Bitcoin Core 31.0 qui diffuse ses propres transactions par Tor ou I2P seulement. |
| B | Reproducible builds (compilation reproductible) | `reproducible-builds` | INFORMATIQUE | [Optech, sujet](https://bitcoinops.org/en/topics/reproducible-builds/) ; [Optech, 04/09/2026](https://bitcoinops.org/en/newsletters/2026/09/04/) | Compilation qui donne des binaires identiques à partir du même code, pour vérifier ce qu'on installe ; sujet Optech. |
| B | Réutilisation de nonce (nonce reuse) | `reutilisation-de-nonce` | CRYPTOGRAPHIE | [Optech, 05/06/2026](https://bitcoinops.org/en/newsletters/2026/06/05/) ; [Optech, 24/04/2024](https://bitcoinops.org/en/newsletters/2024/04/24/) | Erreur qui révèle la clé privée en ECDSA comme en Schnorr, rappelée par Optech en 2024 ; seule musig2 l'évoque. |
| B | RFC 6979 (nonce déterministe) | `rfc-6979` | CRYPTOGRAPHIE | [Optech, 25/09/2026](https://bitcoinops.org/en/newsletters/2026/09/25/) ; [Optech, 12/12/2025](https://bitcoinops.org/en/newsletters/2025/12/12/) | Méthode de nonce déterministe pour ECDSA ; le BIP-0461 de 2026 fixe un algorithme unique. |
| B | Sharechain | `sharechain` | POOLS DE MINAGE | [Delving Bitcoin](https://delvingbitcoin.org/t/bmax-pricing-sats-now-vs-sats-later-via-a-mining-sharechain-no-l1-changes-no-custodians-no-oracles/2165) | Chaîne de parts des pools décentralisés ; citée dans p2pool et braidpool sans entrée propre. |
| B | Sibling eviction | `sibling-eviction` | MEMPOOL ET FRAIS | [Optech, sujet](https://bitcoinops.org/en/topics/kindred-replace-by-fee/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/sibling-eviction-for-v3-transactions/472) | Règle de Bitcoin Core 28.0 qui laisse un nouvel enfant d'une transaction TRUC évincer l'enfant existant ; sujet Optech. |
| B | Signature à seuil (threshold signature) | `signature-a-seuil` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/threshold-signature/) ; [Optech, 10/10/2025](https://bitcoinops.org/en/newsletters/2025/10/10/) | Signature t-sur-n qui produit une seule signature (FROST) ; citée dans 9 définitions, sujet Optech. |
| B | Slow block (bloc lent à valider) | `slow-block` | ATTAQUE | [Delving Bitcoin](https://delvingbitcoin.org/t/consensus-cleanup-demo-of-slow-blocks-on-signet/2367) ; [Delving Bitcoin](https://delvingbitcoin.org/t/can-parallel-validation-side-step-the-slow-block-issue/1288) | Bloc conçu pour être très long à valider, visé par le consensus cleanup et démontré sur signet. |
| B | SuperScalar | `superscalar` | LIGHTNING NETWORK | [Delving Bitcoin](https://delvingbitcoin.org/t/superscalar-laddered-timeout-tree-structured-decker-wattenhofer-factories/1143) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Construction de *channel factory* à base de *timeout trees*, proposée en 2024 ; aucune entrée. |
| B | SwiftSync | `swiftsync` | FONCTIONNEMENT DU NŒUD | [Optech, sujet](https://bitcoinops.org/en/topics/swiftsync/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/swiftsync-speeding-up-ibd-with-pre-generated-hints-poc/1562) | Accélération de l'IBD par indices précalculés, environ 5 fois plus rapide dans le prototype de 2025. |
| B | Tapleaf (feuille de script) | `tapleaf` | SCRIPT | [Optech, 24/01/2025](https://bitcoinops.org/en/newsletters/2025/01/24/) ; [Optech, 24/04/2026](https://bitcoinops.org/en/newsletters/2026/04/24/) | Feuille de cet arbre, avec sa version de feuille ; revient dans les propositions qui ajoutent une nouvelle version de Tapscript. |
| B | Taptree (arbre de scripts Taproot) | `taptree` | SCRIPT | [Optech, 21/08/2026](https://bitcoinops.org/en/newsletters/2026/08/21/) ; [Optech, 03/07/2026](https://bitcoinops.org/en/newsletters/2026/07/03/) | Arbre de Merkle des scripts d'une sortie Taproot ; cité dans plusieurs définitions sans entrée propre. |
| B | TEE (Trusted Execution Environment) | `tee-trusted-execution-environment` | INFORMATIQUE | [Delving Bitcoin](https://delvingbitcoin.org/t/confidential-script-emulate-soft-forks-using-stateless-tees/1918) ; [Optech, 21/08/2026](https://bitcoinops.org/en/newsletters/2026/08/21/) | Enclave matérielle utilisée par des portefeuilles et pour émuler des soft forks ; hsm et secure-element existent, pas TEE. |
| B | Template Provider (Stratum V2) | `template-provider` | POOLS DE MINAGE | [Optech, 05/07/2024](https://bitcoinops.org/en/newsletters/2024/07/05/) ; [Optech, 01/05/2024](https://bitcoinops.org/en/newsletters/2024/05/01/) | Rôle de Stratum V2 tenu par un nœud qui fournit les modèles de blocs, relié à l'interface de minage de Bitcoin Core. |
| B | Timeout tree | `timeout-tree` | COUCHE SUPÉRIEURE | [Optech, sujet](https://bitcoinops.org/en/topics/timeout-trees/) ; [Optech, 01/11/2024](https://bitcoinops.org/en/newsletters/2024/11/01/) | Arbre de transactions qui expire au profit d'un fournisseur, base de SuperScalar et d'Ark ; sujet Optech. |
| B | Transaction de 64 octets | `transaction-de-64-octets` | ATTAQUE | [Optech, sujet](https://bitcoinops.org/en/topics/merkle-tree-vulnerabilities/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/great-consensus-cleanup-revival/710) | Transaction dont la taille permet de tromper une preuve de Merkle ; le consensus cleanup (BIP-0054) les interdit. |
| B | Transaction pré-signée | `transaction-pre-signee` | TRANSACTIONS | [Optech, 23/10/2026](https://bitcoinops.org/en/newsletters/2026/10/23/) ; [Optech, 02/10/2026](https://bitcoinops.org/en/newsletters/2026/10/02/) | Brique des vaults et des protocoles de type BitVM ; citée dans 7 définitions sans entrée propre. |
| B | Transactions dupliquées (duplicate transactions) | `transaction-dupliquee` | TRANSACTIONS | [Optech, sujet](https://bitcoinops.org/en/topics/duplicate-transactions/) ; [Optech, 07/02/2025](https://bitcoinops.org/en/newsletters/2025/02/07/) | Deux transactions au même txid, à l'origine du problème du bloc 1 983 702 que traite le *consensus cleanup* ; seule bip-0030 en parle, et elle part dans la partie Spécifications. |
| B | Vardiff | `vardiff` | POOLS DE MINAGE | [Delving Bitcoin](https://delvingbitcoin.org/t/research-a-clockless-vardiff-strands-a-slowing-miner/2718) ; [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) | Ajustement automatique de la difficulté des parts par le pool, étudié en 2026 ; aucune entrée. |
| B | Version rolling | `version-rolling` | MINAGE | [Optech, 06/03/2026](https://bitcoinops.org/en/newsletters/2026/03/06/) ; [Optech, 12/06/2026](https://bitcoinops.org/en/newsletters/2026/06/12/) | Usage de bits de nVersion comme espace de nonce par les mineurs ; Bitcoin Core applique le BIP-0323 en 2026. |
| B | Vulnérabilité de l'arbre de Merkle (CVE-2012-2459) | `vulnerabilite-de-l-arbre-de-merkle` | ATTAQUE | [Optech, sujet](https://bitcoinops.org/en/topics/merkle-tree-vulnerabilities/) ; [Optech, 06/09/2024](https://bitcoinops.org/en/newsletters/2024/09/06/) | Défauts de l'arbre de Merkle de Bitcoin (CVE-2012-2459, CVE-2017-12842) ; sujet Optech lié au consensus cleanup. |
| B | Weak blocks (blocs faibles) | `weak-blocks` | RÉSEAU | [Delving Bitcoin](https://delvingbitcoin.org/t/second-look-at-weak-blocks/805) ; [Optech, 24/04/2024](https://bitcoinops.org/en/newsletters/2024/04/24/) | Blocs à preuve de travail partielle relayés pour améliorer la reconstruction des *compact blocks*, proposés en 2024. |
| B | Zero-fee commitments | `zero-fee-commitments` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/v3-commitments/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/zero-fee-commitments-for-mobile-wallets/1453) | Transactions d'engagement Lightning sans frais, construites sur TRUC et P2A ; sujet Optech. |
| B | zkVM | `zkvm` | CRYPTOGRAPHIE | [Delving Bitcoin](https://delvingbitcoin.org/t/running-cores-real-consensus-code-inside-a-zkvm/2811) ; [Optech, 03/07/2026](https://bitcoinops.org/en/newsletters/2026/07/03/) | Machine virtuelle qui prouve son exécution par une preuve à divulgation nulle ; testée avec le code de consensus de Bitcoin Core. |
| C | Accidental confiscation | `accidental-confiscation` | ÉVOLUTION DU PROTOCOLE | [Optech, sujet](https://bitcoinops.org/en/topics/accidental-confiscation/) | Risque qu'un soft fork rende des fonds indépensables ; sujet Optech de niche. |
| C | Anonymous usage tokens | `anonymous-usage-tokens` | CRYPTOGRAPHIE | [Optech, 17/05/2024](https://bitcoinops.org/en/newsletters/2024/05/17/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/anonymous-usage-tokens-from-curve-trees-or-autct/862) | Jetons anonymes anti-Sybil proposés en 2024, par exemple pour les annonces de canaux. |
| C | Arithmétique 64 bits (Script) | `arithmetique-64-bits` | SCRIPT | [Delving Bitcoin](https://delvingbitcoin.org/t/64-bit-arithmetic-soft-fork/397) ; [Optech, 21/02/2024](https://bitcoinops.org/en/newsletters/2024/02/21/) | Proposition d'opérations sur 64 bits dans Script, discutée en 2024. |
| C | BINANA | `binana` | ÉVOLUTION DU PROTOCOLE | [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) ; [Optech, 23/10/2026](https://bitcoinops.org/en/newsletters/2026/10/23/) | Dépôt de spécifications hors BIP de Bitcoin Inquisition ; cité dans les bulletins Optech. |
| C | Block template sharing | `block-template-sharing` | MINAGE | [Delving Bitcoin](https://delvingbitcoin.org/t/sharing-block-templates/1906) ; [Optech, 22/08/2025](https://bitcoinops.org/en/newsletters/2025/08/22/) | Partage des modèles de blocs entre nœuds pour repérer les écarts de mempool ; brouillon de BIP en 2025. |
| C | BTC Lisp (bll) | `btc-lisp` | SCRIPT | [Optech, sujet](https://bitcoinops.org/en/topics/basic-bitcoin-lisp-language/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/btc-lisp-as-an-alternative-to-script/682) | Langage de script de type Lisp proposé comme alternative à Script, encore expérimental. |
| C | Canal de Spillman | `canal-de-spillman` | LIGHTNING NETWORK | [Optech, 01/11/2024](https://bitcoinops.org/en/newsletters/2024/11/01/) | Premier canal de paiement unidirectionnel, cité pour l'histoire des canaux. |
| C | CJDNS | `cjdns` | RÉSEAU | [Optech, 05/07/2024](https://bitcoinops.org/en/newsletters/2024/07/05/) ; [doc Bitcoin Core](https://github.com/bitcoin/bitcoin/blob/master/doc/cjdns.md) | Réseau chiffré pris en charge par Bitcoin Core à côté de Tor et I2P. |
| C | CMake | `cmake` | INFORMATIQUE | [Optech, 16/08/2024](https://bitcoinops.org/en/newsletters/2024/08/16/) ; [Optech, 26/06/2026](https://bitcoinops.org/en/newsletters/2026/06/26/) | Système de compilation de Bitcoin Core depuis 2024. |
| C | CoinGrinder | `coingrinder` | PORTEFEUILLE | [Delving Bitcoin](https://delvingbitcoin.org/t/gutterguard-and-coingrinder-simulation-results/279) ; [Optech, 21/02/2024](https://bitcoinops.org/en/newsletters/2024/02/21/) | Algorithme de sélection des pièces ajouté à Bitcoin Core en 2024, à côté de branch-and-bound et knapsack-solver. |
| C | ColliderScript | `colliderscript` | COVENANTS | [Optech, 29/11/2024](https://bitcoinops.org/en/newsletters/2024/11/29/) ; [bitcoindev](https://gnusha.org/pi/bitcoindev/CAEM=y+W2jyFoJAq9XrE9whQ7EZG4HRST01TucWHJtBhQiRTSNQ@mail.gmail.com/T/) | Covenants sans soft fork à partir de collisions de hachage de 160 bits, très coûteux ; résultat de recherche de 2024. |
| C | Countersign | `countersign` | PORTEFEUILLE | [Optech, sujet](https://bitcoinops.org/en/topics/countersign/) | Proposition ancienne de contre-signature ; sujet Optech sans activité récente. |
| C | Dépassement des horodatages en 2106 | `depassement-2106` | PROTOCOLE | [Optech, 02/01/2026](https://bitcoinops.org/en/newsletters/2026/01/02/) ; [bitcoindev](https://gnusha.org/pi/bitcoindev/CAPnXYtPdbFwc1mOsP2eHQBwuJhn2XxLCWC-pt6+N-bu3BRRbiA@mail.gmail.com/T/) | Débordement des horodatages de blocs sur 32 bits en 2106, discuté en 2026. |
| C | Duplex micropayment channels | `duplex-micropayment-channels` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/duplex-micropayment-channels/) ; [Optech, 20/12/2024](https://bitcoinops.org/en/newsletters/2024/12/20/) | Ancien modèle de canal de paiement, repris dans les travaux sur les *timeout trees*. |
| C | Dynamic commitments (mise à niveau de canal) | `dynamic-commitments` | LIGHTNING NETWORK | [Optech, sujet](https://bitcoinops.org/en/topics/channel-commitment-upgrades/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/upgrading-existing-lightning-channels/881) | Mise à niveau d'un canal Lightning sans le fermer ; sujet Optech, discussions surtout entre développeurs. |
| C | Fee sponsorship | `fee-sponsorship` | ÉVOLUTION DU PROTOCOLE | [Optech, sujet](https://bitcoinops.org/en/topics/fee-sponsorship/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/improving-transaction-sponsor-blockspace-efficiency/696) | Proposition de transaction qui paie les frais d'une autre sans la dépenser ; sujet Optech. |
| C | Floresta | `floresta` | IMPLÉMENTATION | [Optech, 18/09/2026](https://bitcoinops.org/en/newsletters/2026/09/18/) ; [Optech, 17/04/2026](https://bitcoinops.org/en/newsletters/2026/04/17/) | Nœud complet léger en Rust fondé sur Utreexo. |
| C | Fountain codes (codes fontaines) | `fountain-codes` | FONCTIONNEMENT DU NŒUD | [Delving Bitcoin](https://delvingbitcoin.org/t/fountain-codes-a-way-to-reduce-blockchain-storage-costs/2624) ; [Optech, 10/07/2026](https://bitcoinops.org/en/newsletters/2026/07/10/) | Codes correcteurs proposés pour que les nœuds élagués servent l'IBD ; recherche de 2026. |
| C | MuHash | `muhash` | CRYPTOGRAPHIE | [Optech, 17/07/2026](https://bitcoinops.org/en/newsletters/2026/07/17/) ; [Optech, 11/04/2025](https://bitcoinops.org/en/newsletters/2025/04/11/) | Fonction de hachage d'ensemble utilisée par coinstatsindex et SwiftSync. |
| C | Mutation testing | `mutation-testing` | INFORMATIQUE | [Optech, 16/01/2026](https://bitcoinops.org/en/newsletters/2026/01/16/) ; [Optech, 29/05/2026](https://bitcoinops.org/en/newsletters/2026/05/29/) | Méthode de test appliquée à Bitcoin Core depuis 2024. |
| C | Mutinynet | `mutinynet` | RÉSEAU | [Optech, 22/08/2025](https://bitcoinops.org/en/newsletters/2025/08/22/) ; [Optech, 04/04/2025](https://bitcoinops.org/en/newsletters/2025/04/04/) | Signet à blocs de 30 secondes très utilisé pour tester Lightning et les covenants. |
| C | Oblivious shares | `oblivious-shares` | POOLS DE MINAGE | [Optech, sujet](https://bitcoinops.org/en/topics/block-withholding/) ; [Optech, 30/08/2024](https://bitcoinops.org/en/newsletters/2024/08/30/) | Parts de minage qui empêchent un mineur de savoir s'il tient un bloc, parade à la rétention de bloc. |
| C | OHTTP (Oblivious HTTP) | `ohttp-oblivious-http` | CONFIDENTIALITÉ | [Optech, 12/06/2026](https://bitcoinops.org/en/newsletters/2026/06/12/) ; [BIP-0077](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0077.md) | Protocole qui masque l'adresse IP de l'émetteur, utilisé par Payjoin v2 (BIP-0077). |
| C | OP_EXPIRE | `op-expire` | OPCODES | [Optech, 07/08/2026](https://bitcoinops.org/en/newsletters/2026/08/07/) | Opcode proposé par Peter Todd pour faire expirer une transaction ; cité dans les débats sur l'expiration. |
| C | OP_TWEAKADD | `op-tweakadd` | COVENANTS | [Optech, 29/05/2026](https://bitcoinops.org/en/newsletters/2026/05/29/) ; [Optech, 19/12/2025](https://bitcoinops.org/en/newsletters/2025/12/19/) | Opcode proposé (BIP-0449) pour calculer une clé Taproot dans un script. |
| C | Paiements probabilistes | `paiements-probabilistes` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/probabilistic-payments/) ; [Optech, 14/02/2025](https://bitcoinops.org/en/newsletters/2025/02/14/) | Paiement de très petites sommes par loterie, discuté en 2025 ; seule trimmed-htlc l'évoque. |
| C | PeerSwap | `peerswap` | LOGICIEL LIGHTNING | [Optech, 24/01/2025](https://bitcoinops.org/en/newsletters/2025/01/24/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/forwardable-peerswap-incentives-and-closing-surreptitious-communications-tunnels/2917) | Protocole d'échange de liquidité entre pairs Lightning par *atomic swap*. |
| C | Quiescence (protocole Lightning) | `quiescence` | LIGHTNING NETWORK | [Optech, 04/09/2026](https://bitcoinops.org/en/newsletters/2026/09/04/) ; [Optech, 20/03/2026](https://bitcoinops.org/en/newsletters/2026/03/20/) | État d'un canal Lightning gelé le temps d'un *splicing* ; lié dans 13 bulletins, mentionné dans splicing. |
| C | Redundant overpayments (paiements surdimensionnés) | `redundant-overpayments` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/redundant-overpayments/) ; [Optech, 10/10/2025](https://bitcoinops.org/en/newsletters/2025/10/10/) | Paiement Lightning envoyé en plus de parts que nécessaire pour éviter les nouvelles tentatives ; proposition de ZmnSCPxj suivie par Optech. |
| C | Shielded CSV | `shielded-csv` | COUCHE SUPÉRIEURE | [Optech, sujet](https://bitcoinops.org/en/topics/client-side-validation/) ; [Optech, 27/09/2024](https://bitcoinops.org/en/newsletters/2024/09/27/) | Validation côté client qui masque l'historique par des preuves à divulgation nulle, publiée en 2024. |
| C | Signatures BLS | `signature-bls` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/bls-signatures/) | Schéma de signature agrégeable non retenu pour Bitcoin ; sujet Optech peu actif. |
| C | Signer delegation | `signer-delegation` | SCRIPT | [Optech, sujet](https://bitcoinops.org/en/topics/signer-delegation/) ; [Optech, 04/09/2026](https://bitcoinops.org/en/newsletters/2026/09/04/) | Délégation du droit de signer à une autre clé (CSFS, graftroot) ; sujet Optech. |
| C | Single Random Draw (SRD) | `srd-single-random-draw` | PORTEFEUILLE | [Delving Bitcoin](https://delvingbitcoin.org/t/gutterguard-and-coingrinder-simulation-results/279) ; [Optech, sujet](https://bitcoinops.org/en/topics/coin-selection/) | Troisième algorithme de sélection des pièces de Bitcoin Core ; les deux autres ont leur entrée. |
| C | Spacechain | `spacechain` | SIDECHAIN | [Delving Bitcoin](https://delvingbitcoin.org/t/thoughts-on-scaling-and-consensus-changes-2023/32) | Sidechain de Ruben Somsen fondée sur le minage fusionné aveugle ; citée sans détail dans les discussions. |
| C | Stateless invoices | `stateless-invoices` | PAIEMENTS LIGHTNING | [Optech, sujet](https://bitcoinops.org/en/topics/stateless-invoices/) | Factures Lightning qui ne demandent aucun stockage au destinataire ; sujet Optech de niche. |
| C | Transitory soft fork | `transitory-soft-fork` | ÉVOLUTION DU PROTOCOLE | [Optech, sujet](https://bitcoinops.org/en/topics/transitory-soft-forks/) ; [Delving Bitcoin](https://delvingbitcoin.org/t/transitory-soft-forks-for-consensus-cleanup-forks/1333) | Soft fork qui expire s'il n'est pas reconduit, proposé pour le consensus cleanup. |
| C | Upfront fees | `upfront-fees` | PAIEMENTS LIGHTNING | [Optech, 28/03/2025](https://bitcoinops.org/en/newsletters/2025/03/28/) ; [Optech, 24/04/2026](https://bitcoinops.org/en/newsletters/2026/04/24/) | Frais payés d'avance pour limiter le *jamming* Lightning ; proposition en discussion. |
| C | Varops budget | `varops-budget` | SCRIPT | [Delving Bitcoin](https://delvingbitcoin.org/t/benchmarking-bitcoin-script-evaluation-for-the-varops-budget-great-script-restoration/2094) ; [Optech, 10/04/2026](https://bitcoinops.org/en/newsletters/2026/04/10/) | Budget de calcul des scripts proposé par le BIP-0440, pièce de la Great Script Restoration. |
| C | Vérification formelle | `verification-formelle` | INFORMATIQUE | [Optech, 17/07/2026](https://bitcoinops.org/en/newsletters/2026/07/17/) ; [Optech, 21/08/2026](https://bitcoinops.org/en/newsletters/2026/08/21/) | Preuve mathématique qu'un code respecte sa spécification, appliquée à libsecp256k1 et au protocole en 2026. |
| C | Warnet | `warnet` | OUTIL DE DÉVELOPPEMENT | [Delving Bitcoin](https://delvingbitcoin.org/t/warnet-increase-tx-relay-rate/294) ; [Optech, 01/05/2024](https://bitcoinops.org/en/newsletters/2024/05/01/) | Outil de simulation de réseaux de nœuds Bitcoin pour tester des attaques P2P. |
| C | Waste metric (sélection des pièces) | `waste-metric` | PORTEFEUILLE | [Delving Bitcoin](https://delvingbitcoin.org/t/gutterguard-and-coingrinder-simulation-results/279) | Score de la sélection des pièces de Bitcoin Core qui départage les solutions ; selection-des-pieces ne le détaille pas. |
| C | Zawy's alternating timestamp attack | `alternating-timestamp-attack` | ATTAQUE | [Delving Bitcoin](https://delvingbitcoin.org/t/zawys-alternating-timestamp-attack/1062) | Variante d'attaque sur les horodatages étudiée avec le *time warp*. |
| C | ZKCP (Zero-Knowledge Contingent Payment) | `zkcp-zero-knowledge-contingent-payment` | CRYPTOGRAPHIE | [Optech, sujet](https://bitcoinops.org/en/topics/acc/) ; [Optech, 28/02/2024](https://bitcoinops.org/en/newsletters/2024/02/28/) | Paiement conditionné à une preuve à divulgation nulle, cité avec BitVM et l'ecash. |

## Déjà couverts sous un autre nom

Sujets de l'index Optech (et quelques synonymes croisés dans les fils) qui ont déjà une entrée. Ne pas les recréer ; au besoin, ajouter le synonyme dans l'entrée existante.

| Terme rencontré | Entrée existante |
|---|---|
| 2pECDSA, multisignatures sans script | `multisig`, `scriptless-scripts` |
| Adaptor signatures, signature adaptors | `adaptor-signature` |
| Addr v2 | `addrv2` |
| Address reuse, output linking | `reutilisation-d-adresse` |
| AMP (atomic multipath payments) | `atomic-multi-path-payments` |
| Ancestor feerate mining | `ancestor-mining`, `cpfp-child-pay-for-parent` |
| Anchor outputs, simplified commitments | `anchor-outputs` |
| Annex | `annex` |
| Anonymity networks (Tor, I2P) | `tor-the-onion-router`, `i2p` |
| Anti fee sniping | `fee-sniping` |
| Ark protocol | `ark` |
| ASICBoost (covert, overt) | `asicboost` |
| AssumeUTXO | `assume-utxo` |
| Async payments | `async-payments` |
| Base AMP, multipart payments | `mpp-multi-path-payments` |
| Payment batching | `batched-spending` |
| Bech32, bech32m | `bech32-et-bech32m` |
| BetterHash, pooled mining | `betterhash`, `mining-pool` |
| Braidpool | `braidpool` |
| BIP8, BIP9, soft fork activation | `methode-d-activation` |
| HD key generation, HD wallets | `hd-hierarchical-deterministic` |
| Transaction bloom filtering | `bloom-filter` |
| Consensus cleanup soft fork (BIP-0054) | `consensus-cleanup` |
| BIP70 payment protocol | `bip-0070` |
| Payjoin, Pay-to-EndPoint | `payjoin` |
| Codex32 | `codex32` |
| Replace-by-fee, full-RBF | `rbf-replace-by-fee`, `full-rbf` |
| Version 2 P2P transport (BIP-0324) | `p2p-transport-v2` |
| Compact block relay | `compact-block-relay` |
| Dandelion | `dandelion` |
| Compact block filters, Neutrino | `compact-block-filters` |
| PSBT | `psbt` |
| Generic signmessage (BIP-0322) | `bip-0322` |
| Blinded paths, route blinding | `blinded-paths` |
| Block explorers | `explorateur-de-bloc` |
| Offers (BOLT-12) | `offer`, `bolt-12` |
| Channel announcements, gossip | `channel-announcement`, `gossip` |
| Channel factories | `channel-factories` |
| Channel jamming attacks | `channel-jamming` |
| Coinjoin | `coinjoin` |
| Joinpools, coinpools, payment pools | `joinpool` |
| Coinswap | `coinswap` |
| Covenants | `covenant` |
| Cluster mempool | `cluster-mempool` |
| Output script descriptors | `output-script-descriptors` |
| Difficulty adjustment algorithms | `ajustement-de-la-difficulte` |
| Discreet Log Contracts | `dlc-discreet-log-contract` |
| Dual funding | `dual-funding` |
| Dust, uneconomical outputs | `dust` |
| Ecash (au sens chaumien) | `ecash-david-chaum`, `cashu` |
| Eclipse attacks | `eclipse` |
| Eltoo, LN-Symmetry | `eltoo` |
| Ephemeral anchors | `ephemeral-anchors` |
| Erlay | `erlay` |
| Expiration floods, flood and loot | `flood-and-loot` |
| Gap limits | `gap-limit` |
| Hardware wallet interface (HWI) | `hwi` |
| Hold invoices | `hodl-invoice` |
| HTLC endorsement | `htlc-endorsement` |
| JIT channels | `jit-channel` |
| JIT routing | `jit-routing` |
| Keysend, spontaneous payments | `keysend` |
| Large channels, wumbo | `wumbo-channel` |
| Minisketch | `minisketch` |
| Liquidity advertisements | `liquidity-ads` |
| MAST | `mast` |
| Miniscript | `miniscript` |
| MuSig | `musig` |
| Onion messages | `onion-message` |
| OP_CAT | `op-cat-0x7e` |
| OP_CHECKSIGFROMSTACK | `op-checksigfromstack-0xcc` |
| OP_CHECKTEMPLATEVERIFY | `op-checktemplateverify-0xb3` |
| OP_CODESEPARATOR | `op-codeseparator-0xab` |
| Package relay | `package-relay` |
| Pay-to-contract | `pay-to-contract` |
| Payment probes, probing | `probing` |
| PTLC | `ptlc` |
| Unannounced channels, private channels | `private-channel` |
| Proof of reserves | `preuve-de-reserves` |
| Replacement cycling | `replacement-cycling` |
| Schnorr signatures | `schnorr-protocole` |
| Segregated witness | `segwit` |
| Selfish mining | `selfish-mining` |
| Sidechains | `sidechain` |
| SIGHASH_ANYPREVOUT, SIGHASH_NOINPUT | `sighash-anyprevout` |
| Signet | `signet` |
| Silent payments | `silent-payments` |
| Simple taproot channels | `taproot-channel` |
| Simplicity | `simplicity` |
| Splicing | `splicing` |
| Statechains | `statechain` |
| Static channel backups | `scb-static-channel-backup` |
| Stratum V2 | `stratum-v2` |
| Submarine swaps | `submarine-swap` |
| Swap-in-potentiam | `swap-in-potentiam` |
| Taproot | `taproot` |
| Tapscript | `tapscript` |
| Testnet, testnet3, testnet4 | `testnet` |
| Time warp | `time-warp` |
| Timelocks | `timelock` |
| Trampoline payments | `trampoline-routing` |
| Transaction pinning | `transaction-pinning` |
| Trimmed HTLC | `trimmed-htlc` |
| Utreexo | `utreexo` |
| Vaults | `vault` |
| Wallet labels | `etiquetage` |
| Watchtowers | `watchtower` |
| X-only public keys | `x-only-public-keys` |

Hors périmètre de cette liste : Quantum resistance et Nostr, traités dans `termes-quantique-nostr.md`.
