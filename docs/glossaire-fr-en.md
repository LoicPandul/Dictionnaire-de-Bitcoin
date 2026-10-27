# Glossaire français → anglais

Terminologie de la version anglaise du dictionnaire (voir [traduction.md](./traduction.md)). Le titre anglais de chaque entrée est dans le `metadata.yaml` de `definitions/en/` : quand une définition parle d'une autre entrée, elle reprend ce terme, en casse normale, jamais une variante.

Méthode : les termes ci-dessous viennent d'un comptage de fréquence sur les `definition.md` français (bigrammes et trigrammes les plus courants), complété par les pièges de traduction repérés à la lecture. Les sources de référence, par ordre de priorité : Bitcoin Core (code, RPC, documentation), BIP et BOLT, Bitcoin Optech, *Mastering Bitcoin*, Learn Me a Bitcoin.

## 1. Conventions

* **Orthographe américaine** : *-ize* (*decentralization*, *reorganize*, *analyze*), *-or* (*behavior*, *color*), *-er* (*center*), *-se* pour les noms (*defense*, *license*), consonne simple devant le suffixe (*labeling*, *canceled*), *program*, *gray*, *judgment*.
* **Numérotation des spécifications** : *BIP-0032* (toujours 4 chiffres, avec tiret), *BOLT-02*, *bLIP-0001*, *NIP-05*. Ne change ni la casse ni les zéros. Un BIP s'écrit *BIP-0039*, jamais *BIP39* ni *BIP 39*, sauf dans un nom de code ou un identifiant (`bip39`).
* **Bitcoin / bitcoin** : « Bitcoin » (majuscule) = le système, le protocole, le réseau (*the Bitcoin network*, *Bitcoin Core*). « bitcoin » (minuscule) = l'unité et la monnaie (*0.5 bitcoin*, *send bitcoin*). Le mot **bitcoin** reste invariable (*21 million bitcoin*, *the bitcoin in a wallet*) ; n'ajoute pas de *s*. Ticker : *BTC* (et *XBT* seulement dans l'entrée qui porte ce nom).
* **Satoshis** : *sat* au singulier, *sats* au pluriel (*100 million sats = 1 bitcoin*). *satoshi* (minuscule) en toutes lettres à la première mention, *sats* ensuite. *millisatoshi* (*msat*) pour Lightning.
* **Nombres** : séparateur de milliers = virgule (*1,000,000*, *210,000 blocks*), séparateur décimal = point (*0.5*, *1.5 MB*). Pas d'espace avant `%` (*51%*, pas *51 %*). Dates à l'américaine : *January 3, 2009*. Devises : *$100*, *€50*. Unités : *Mo → MB*, *Go → GB*, *ko → kB*, *octet → byte* (le *o* français devient *B*). *sat/vB* inchangé.
* **Guillemets** : guillemets droits doubles `"..."` partout (jamais « », ni guillemets courbes). Apostrophe droite `'`. Les citations dans une citation : guillemets simples droits.
* **Ponctuation** : **aucun tiret cadratin (em dash) ni demi-cadratin (en dash)**. Remplace par une virgule, deux-points, des parenthèses ou une phrase séparée. Pour les intervalles : *from 5 to 10*, ou *5-10* avec un trait d'union ordinaire. Pas d'espace avant `:`, `;`, `?`, `!`.
* **Anglicismes du français** : le français met en italique les termes anglais (*output*, *hashrate*, *mempool*). En anglais, ce ne sont plus des mots étrangers : **retire l'italique**. Garde l'italique seulement pour un terme cité comme terme (*a stale block is...*), pour un titre d'ouvrage, ou pour un mot qui reste étranger (*lex mercatoria*).
* **Casse** : *blockchain*, *mempool*, *hashrate*, *txid*, *testnet*, *mainnet* en minuscules. *SegWit*, *Taproot*, *Schnorr*, *Miniscript*, *Lightning Network*, *Bitcoin Core*, *Nostr*, *Ark*, *RGB* avec majuscule. *Script* (majuscule) quand on parle du langage de Bitcoin, *script* sinon. Après la première mention, *Lightning* seul et *Core* seul sont acceptés.
* **Code, fichiers, opcodes, RPC, options** : inchangés, en `code` (`OP_CHECKSIG`, `bitcoin.conf`, `getblocktemplate`, `-prune`). Les noms de champs de la spécification restent aussi tels quels (`nSequence`, `scriptPubKey`).
* **Noms propres, personnes, entreprises, produits** : inchangés. Les noms d'événements s'écrivent comme en anglais (*Pizza Day*, *Hong Kong Roundtable*).
* **Titres** : en majuscules, `SIGLE - FORME LONGUE` pour les sigles (*RBF - REPLACE-BY-FEE*). Dans le corps du texte, casse normale : *Replace-by-Fee (RBF)* à la première mention, *RBF* ensuite.
* **Voix** : phrases courtes, présent, ton de dictionnaire, pas de calque du français (*il convient de souligner que* → supprimer ; *on peut* → un acteur concret (*a node can*, *Alice can*) ou la forme passive, jamais *you* : le dictionnaire reste impersonnel ; *permet de* → *allows*, *lets* + acteur, ou le verbe direct). Le détail du style relève de la charte éditoriale, adaptée à l'anglais.
* **Verbes à ne pas confondre** : *valider* = *validate* (un nœud valide un bloc ou une transaction, selon les règles de consensus) ; *vérifier* = *verify* (on vérifie une signature, une preuve, un hachage) ; *diffuser* = *broadcast* (publier sa propre transaction) ou *propagate* (la transmission de nœud en nœud) ; *relayer* = *relay* (un nœud retransmet). *Dépenser* = *spend* ; *miner* = *mine* ; *chiffrer* = *encrypt* ; *signer* = *sign*.

## 2. Glossaire

Les notes ne sont données que s'il y a un piège. « (titre) » = le terme est aussi le titre anglais de l'entrée.

### 2.1 Système, réseau et nœuds

| Français | Anglais | Note |
|---|---|---|
| réseau Bitcoin | Bitcoin network | (titre) |
| réseau pair-à-pair | peer-to-peer (P2P) network | |
| nœud | node | Un participant qui valide et relaie ; ne pas écrire *peer* pour un nœud en général |
| nœud complet | full node | (titre) |
| nœud élagué | pruned node | (titre) |
| nœud léger, client léger | light client, SPV node | *Light client* est le terme courant ; *SPV node* reste pour l'entrée SPV |
| pair | peer | Ne pas confondre avec *paire* (de clés) = *pair* (*key pair*) |
| pair entrant / sortant | inbound / outbound peer | (titre). Connexion entrante/sortante = *inbound/outbound connection* |
| relayer, relais (d'un nœud) | relay | Un nœud *relays* des transactions et des blocs. Le relais Nostr est un *relay* aussi |
| diffusion | propagation | (titre). *Broadcast* seulement pour l'envoi initial d'une transaction par son émetteur |
| synchronisation initiale | initial block download (IBD) | |
| mainnet, réseau principal | mainnet | |
| testnet, signet, regtest | testnet, signet, regtest | Inchangés, minuscules |
| logiciel | software | Jamais *softwares* |
| dépôt (Git) | repository (*repo*) | Piège : *dépôt* bancaire = *deposit* |
| livre blanc | white paper | Le livre blanc de Bitcoin = *the Bitcoin white paper* |
| porte dérobée | backdoor | |
| attaque Sybil, attaque Eclipse | Sybil attack, eclipse attack | |
| point de défaillance unique | single point of failure (SPOF) | |

### 2.2 Blocs, chaîne et consensus

| Français | Anglais | Note |
|---|---|---|
| chaîne de blocs | blockchain | Un seul mot, minuscule |
| en-tête de bloc | block header | Pas *entête* ; *header* seul accepté après |
| transaction coinbase | coinbase transaction | *coinbase* reste tel quel |
| bloc candidat | candidate block | Bitcoin Core dit aussi *block template* (modèle de bloc) |
| bloc obsolète, périmé | stale block | **Piège** : *stale* = valide mais hors de la meilleure chaîne |
| bloc orphelin | orphan block | **Piège** : sens théorique (parent inconnu). N'emploie pas *orphan* pour un bloc *stale* |
| chaîne principale | best chain, main chain | Core dit *best chain* (la chaîne de plus grand travail cumulé) |
| travail accumulé | accumulated work, chainwork | Évite *longest chain* : c'est la chaîne qui a le plus de travail, pas la plus longue |
| réorganisation | chain reorganization (*reorg*) | (titre). Le français *resynchronisation* désigne ce phénomène |
| embranchement naturel | accidental fork | (titre). Deux blocs trouvés presque en même temps |
| scission de la chaîne | chain split | |
| récompense de bloc | block reward | **Piège** : subvention + frais |
| subvention de bloc | block subsidy | **Piège** : seulement les nouveaux bitcoins créés (50, 25, 12.5, 6.25, 3.125...) |
| période de maturité | maturity period | 100 blocs avant dépense d'une sortie coinbase (*coinbase maturity*) |
| halving | halving | Jamais *halvening* |
| délai entre blocs | block time, block interval | |
| horodatage | timestamp | (titre) |
| temps médian passé | median time past (MTP) | |
| unité de poids | weight unit (WU) | |
| octet virtuel | virtual byte (vbyte, vB) | `vB` dans les formules (*sat/vB*) |
| finalité | finality | Sur Bitcoin : probabiliste |
| règles de consensus | consensus rules | **Piège** : jamais *consensus protocol* pour les règles |
| consensus | consensus | Mot invariable, pas de pluriel |
| soft fork, hard fork | soft fork, hard fork | Deux mots, minuscules |
| fork | fork | Évite *bifurcation* et *fourche* |
| méthode d'activation | activation mechanism | (titre) |
| signalisation | signaling | |
| bloc de genèse | genesis block | |
| majorité économique | economic majority | |

### 2.3 Preuve de travail et minage

| Français | Anglais | Note |
|---|---|---|
| preuve de travail | proof of work | Nom : *proof of work* ; adjectif : *proof-of-work* (*a proof-of-work algorithm*) |
| minage | mining | |
| mineur | miner | **Piège** : *miner* est aussi le verbe (*to mine*) ; jamais *minor* |
| difficulté | difficulty | Désigne la difficulté de la cible de hachage, pas une difficulté générale |
| ajustement de la difficulté | difficulty adjustment | (titre). *Retarget* est accepté comme synonyme technique |
| taux de hachage | hashrate | Un seul mot. Le français emploie déjà *hashrate* |
| puissance de calcul | computing power, hash power | |
| hachage (action de miner) | hashing | |
| hacheur | hasher | (titre). Participant d'une pool qui ne fait que hacher |
| pool de minage | mining pool | La *pool* est féminin en français, neutre en anglais |
| ferme de minage | mining farm | |
| part (*share*) | share | **Piège** : *part* dans le sens courant = *part, portion* ; *share* seulement pour le minage en pool |
| attaque des 51% | 51% attack | (titre) |
| minage égoïste | selfish mining | |
| minage fusionné | merged mining | (titre) |
| rétention de bloc | block withholding | |
| ASIC | ASIC | Pluriel : *ASICs* |
| chance (d'une pool) | luck | |

### 2.4 Transactions, frais et mempool

| Français | Anglais | Note |
|---|---|---|
| entrée | input | **Piège** : *input* = entrée de transaction, jamais *entry* |
| sortie | output | **Piège** : *output* = sortie de transaction, jamais *exit* |
| sortie non dépensée (UTXO) | unspent transaction output (UTXO) | Pluriel : *UTXOs* |
| ensemble d'UTXOs | UTXO set | (titre) |
| pièce | coin | **Piège** : *coin* seulement dans *coin selection*, *coin control*, *coinjoin* et quand le français dit « pièce » pour un UTXO. Sinon écris *UTXO*. Pièce physique = *coin* aussi |
| change (monnaie rendue) | change | **Piège** : même mot, ne pas traduire par *exchange*. *Sortie de change* = *change output* ; *adresse de change* = *change address* |
| sélection des pièces | coin selection | (titre) |
| contrôle des pièces | coin control | |
| frais | fees | **Piège** : *transaction fees*, au pluriel. Jamais *costs* ni *charges*. Frais de minage = *mining fees* seulement si le français le dit |
| taux de frais | fee rate | (titre). En *sat/vB*. Ne pas écrire *feerate* en prose |
| estimation des frais | fee estimation | |
| augmentation des frais | fee bumping | |
| remplacement par les frais | Replace-by-Fee (RBF) | |
| transaction enfant | child transaction | CPFP : *Child Pays For Parent* |
| ascendants / descendants | ancestors / descendants | |
| paquet | package | *Package relay* |
| double dépense | double spend | (titre) |
| dépenser, dépense | spend, spending | Nom : *spend* (*a key path spend*) ou *spending* |
| standardisation | standardness | **Piège** : ne pas écrire *standardization* pour la politique de relais. *Règles de standardisation* = *standardness rules* |
| politique de relais | relay policy | **Piège** : *policy* = règles locales d'un nœud, par opposition au consensus |
| mempool | mempool | Masculin en anglais (*the mempool*), un mot |
| purge de mempool | mempool eviction | (titre). *Evicted*, *trimmed* |
| poussière | dust | *Dust limit* = seuil de poussière |
| sortie non rentable | uneconomical output | |
| épinglage de transaction | transaction pinning | |
| identifiant de transaction | transaction ID (txid) | `txid` en minuscules et en code |
| malléabilité | malleability | |
| engagement | commitment | **Piège** : concept cryptographique. *Commit* (Git) est un autre mot |
| verrouillage temporel | timelock | Un mot |
| consolidation | consolidation | |
| paiement groupé | batching, batched payment | |
| témoin | witness | **Piège** : le *témoin* de SegWit est le *witness*, jamais *testimony* ni *token* |
| transaction orpheline | orphan transaction | Parent inconnu du nœud |

### 2.5 Script et adresses

| Français | Anglais | Note |
|---|---|---|
| script | script | *Script* (majuscule) pour le langage |
| pile | stack | *Pile principale* = *main stack*, *pile secondaire* = *alt stack* |
| script de verrouillage | locking script (`scriptPubKey`) | **Piège** : la première mention donne les deux ; ensuite `scriptPubKey` |
| script de déverrouillage | unlocking script (`scriptSig`) | |
| script de rachat | redeem script | |
| script de témoin | witness script | |
| chemin de clé | key path | (titre) |
| chemin de script | script path | |
| arbre de scripts | script tree | |
| feuille | leaf | |
| clé interne | internal key | Taproot. Pas *inner key* |
| ajustement (de clé) | tweak | Verbe : *to tweak*. *Tweaked key* |
| multisignature | multisig | |
| modèle de script | script template | |
| descripteur | descriptor | *Output script descriptor* à la première mention |
| politique (Miniscript) | policy | **Piège** : la *policy* de Miniscript n'est pas la politique de relais |
| adresse de réception | receiving address | (titre) |
| adresse statique | static address | Silent Payments |
| adresse personnalisée | vanity address | |
| ancrage | anchor | **Piège** : *sorties d'ancrage* = *anchor outputs* ; *ancrage bilatéral* = *two-way peg* ; *ancrage entrant/sortant* = *peg-in/peg-out* |
| sceau à usage unique | single-use seal | RGB |
| covenant | covenant | Inchangé |

### 2.6 Clés, portefeuilles et dérivation

| Français | Anglais | Note |
|---|---|---|
| portefeuille matériel | hardware wallet | Évite *hardware signing device* sauf si le français le dit |
| portefeuille déterministe et hiérarchique | hierarchical deterministic (HD) wallet | Jamais *hierarchical-deterministic* en un seul mot |
| clé publique exposée | exposed public key | (titre) |
| clé privée | private key | Jamais *secret key* sauf dans une citation (BIP) |
| clé publique | public key | |
| clé étendue | extended key | `xpub` : *extended public key* à la première mention |
| code de chaîne | chain code | Deux mots |
| dérivation endurcie, renforcée, durcie | hardened derivation | **Piège** : le français hésite (*endurcie*, *renforcée*, *durcie*) ; l'anglais n'a que *hardened* |
| dérivation normale | normal (non-hardened) derivation | BIP-0032 dit *normal*. Premier emploi *normal*, puis *non-hardened* est accepté |
| chemin de dérivation | derivation path | (titre) |
| objectif | purpose | Niveau 1 de BIP-0044 |
| type de devise | coin type | |
| compte | account | **Piège** : compte HD (niveau 3), jamais *bank account* |
| chaîne externe / interne | external / internal keychain | BIP-0044. Le niveau s'appelle `change` |
| index | index | Pluriel *indexes* ou *indices* : utilise *indexes* |
| limite de creux | gap limit | |
| graine | seed | **Piège** : la graine est la valeur binaire dérivée de la phrase par PBKDF2. Ne dis pas *seed* pour la phrase |
| phrase de récupération, phrase mnémonique | mnemonic phrase | **Choix** : BIP-0039 dit *mnemonic code* / *mnemonic sentence* ; *recovery phrase* est l'étiquette commerciale des fabricants ; *seed phrase* confond phrase et graine. Écris toujours *mnemonic phrase*. Cite *recovery phrase* seulement entre guillemets quand tu rapportes l'interface d'un logiciel |
| mot de passe (BIP-0039) | passphrase | **Piège** : *passphrase* = le mot de passe optionnel de BIP-0039 ; *password* pour le chiffrement d'un fichier de portefeuille |
| empreinte | fingerprint | **Piège** : *fingerprint* (BIP-0032 : 4 premiers octets de HASH160 de la clé publique ; empreinte de portefeuille ; empreinte de navigateur). Une « empreinte cryptographique » (résultat de hachage) = *hash*, pas *fingerprint* |
| empreinte maîtresse | master fingerprint | |
| portefeuille | wallet | **Piège** : jamais *purse* ni *portfolio* (*portefeuille* financier = *portfolio*) |
| étiquetage | labeling | Orthographe américaine |
| date de naissance (portefeuille) | birth date | |
| récupération | recovery | *Chemin de récupération* = *recovery path* |
| garde | custody | *Garde autonome* = *self-custody* |
| tiers de confiance | trusted third party | |
| transaction partiellement signée | partially signed bitcoin transaction (PSBT) | |

### 2.7 Cryptographie

| Français | Anglais | Note |
|---|---|---|
| chiffrement | encryption | **Piège** : *chiffrer* = *encrypt* ; jamais *crypt* ni *cipher* comme verbe. *Déchiffrer* = *decrypt* |
| hachage | hash / hashing | Résultat = *hash* (nom) ; action = *hashing* |
| condensat | hash digest | (titre). Le français *haché* (nom) = *hash* |
| préimage | preimage | Un mot. *Résistance à la préimage* = *preimage resistance* |
| signature | signature | Nom ; le verbe est *sign* (*signer*) |
| fonction de hachage taguée | tagged hash | BIP-0340 |
| signature de Schnorr | Schnorr signature | (titre) |
| signature d'adaptateur | adaptor signature | **Piège** : *adaptor* avec *o* |
| signature à seuil | threshold signature | |
| point générateur | generator point | |
| engagement de Pedersen | Pedersen commitment | |
| preuve à divulgation nulle de connaissance | zero-knowledge proof (ZKP) | |
| aléatoire / pseudo-aléatoire | random / pseudorandom | Pseudorandom sans trait d'union |
| code d'authentification de message | message authentication code (MAC) | |
| sérialisation | serialization | |
| gros-boutiste / petit-boutiste | big-endian / little-endian | Pas de traduction |
| chaîne de caractères | string | **Piège** : *chaîne* = *chain* (blockchain), *string* (caractères) ou *keychain* |
| attaque par force brute | brute-force attack | |
| attaque par rejeu | replay attack | |
| attaque de l'homme du milieu | man-in-the-middle (MITM) attack | |

### 2.8 Informatique quantique

| Français | Anglais | Note |
|---|---|---|
| algorithme de Shor | Shor's algorithm | |
| algorithme de Grover | Grover's algorithm | |
| cryptographie à base de réseaux euclidiens | lattice-based cryptography | **Piège** : *réseau euclidien* = *lattice*. Jamais *Euclidean network* |
| encapsulation de clé | key encapsulation | |
| attaque à exposition longue / courte | long-exposure / short-exposure attack | Termes de BIP-0360 |
| migration post-quantique | post-quantum migration | |

### 2.9 Confidentialité et analyse de chaîne

| Français | Anglais | Note |
|---|---|---|
| confidentialité | privacy | **Piège** : *confidentialité* = *privacy*, pas *confidentiality*. *Vie privée* = *privacy* aussi |
| pseudonymat | pseudonymity | |
| heuristique de propriété commune des entrées | common-input-ownership heuristic (CIOH) | |
| regroupement | clustering | **Piège** : *cluster* est aussi un terme de Bitcoin Core (cluster mempool) |
| modèle de transaction | transaction pattern | (titre) |
| paiement simple | simple payment | (titre) |
| empreinte de portefeuille | wallet fingerprint | (titre) |
| mixage, mélange | mixing | Service centralisé = *mixer* |
| coinjoin | coinjoin | Un mot, minuscule |
| pool de coinjoin | coinjoin pool | |
| coordinateur | coordinator | |
| paiements silencieux | Silent Payments | Nom de BIP-0352, majuscules, ne pas traduire |

### 2.10 Lightning Network

| Français | Anglais | Note |
|---|---|---|
| canal | channel | **Piège** : `channel`, pas *chanel* ni *canal* |
| ouverture / fermeture | opening / closing | |
| fermeture coopérative | cooperative close | |
| fermeture forcée | force close | Verbe : *to force-close* |
| liquidité | liquidity | **Piège** : liquidité de canal ≠ liquidité de marché (*market liquidity*). Précise-le |
| capacité entrante / sortante | inbound / outbound capacity | |
| solde local / distant | local / remote balance | |
| réserve de canal | channel reserve | |
| transaction d'engagement | commitment transaction | |
| transaction de financement | funding transaction | |
| facture | invoice | **Piège** : *invoice* seulement pour Lightning (BOLT-11), *offer* pour BOLT-12 |
| offre | offer | **Piège** : BOLT-12 = *offer* ; économie = *supply* |
| HTLC | HTLC | *Hashed time-locked contract* à la première mention |
| route, chemin | route, path | *Route* = chemin choisi ; *path* = chemin dans le graphe |
| frais de base | base fee | |
| paiement multichemin | multi-path payment (MPP) | |
| fraction (de paiement) | shard | |
| tour de garde | watchtower | |
| clé de révocation | revocation key | |
| transaction de pénalité | penalty transaction | |
| sondage | probing | |
| annonce de canal | channel announcement | |
| canal public / privé | public / private channel | |
| échange atomique | atomic swap | **Piège** : *échange* = *swap* (opération) ou *exchange* (plateforme) |
| échange sous-marin | submarine swap | |
| chemin masqué | blinded path | |
| paiement spontané | keysend | |

### 2.11 Monnaie, économie et régulation

| Français | Anglais | Note |
|---|---|---|
| monnaie | money | **Piège** : *monnaie* abstraite = *money* (*sound money*) ; une monnaie précise = *currency* (*the dollar is a currency*). Monnaie rendue = *change* |
| monnaie fiat | fiat currency | Souvent *fiat* seul |
| devise | currency | *Type de devise* (BIP-0044) = *coin type*, pas *currency type* |
| création monétaire, émission | money creation, issuance | |
| limite d'émission | supply cap | (titre) |
| plateforme d'échange | exchange | **Piège** : plateforme d'échange de cryptomonnaies = *exchange* ; échange atomique = *swap* |
| capitalisation boursière | market capitalization (market cap) | |
| préférence temporelle | time preference | |
| risque de contrepartie | counterparty risk | |
| réserves fractionnaires | fractional reserve banking | (titre) |
| actif | asset | **Piège** : *actif* dans Taproot Assets ou RGB = *asset* |

### 2.12 Nostr, RGB et autres protocoles

| Français | Anglais | Note |
|---|---|---|
| étiquette (Nostr) | tag | **Piège** : *étiquette* Nostr = *tag* ; *étiquette* de portefeuille = *label* |
| message privé | private direct message | NIP-17 |
| schéma | schema | **Piège** : *schema* (RGB) ≠ *diagram*. Un schéma graphique d'illustration = *diagram*. *Schéma de signature* / *schéma commit-reveal* = *scheme* |
| consignation | consignment | Orthographe *consignment* |
| genèse (RGB) | genesis | À distinguer de *bloc de genèse* = *genesis block* |
| sidechain, chaîne latérale | sidechain | Un mot |
| surcouche | layer 2 | (titre) |

### 2.13 Divers (informatique, sécurité, projet)

| Français | Anglais | Note |
|---|---|---|
| dossier, répertoire | directory | *Répertoire de données* = *data directory* |
| paramètre, option (Core) | option, parameter | Pour une option de Bitcoin Core (`-prune`) : *option* |
| journal | log | `debug.log` |
| faille, vulnérabilité | vulnerability | |
| bogue | bug | |
| débordement | overflow | |
| proposition d'amélioration de Bitcoin | Bitcoin Improvement Proposal (BIP) | |
| champion (BIP) | champion | |
| fonds | funds | **Piège** : toujours pluriel, jamais *fund* |
| destinataire / expéditeur | recipient / sender | |
| tableau | table, array | *Array* pour une structure de données |
| en chaîne (on-chain) / hors chaîne (off-chain) | on-chain / off-chain | Avec trait d'union comme adjectif |

## 3. Choix arrêtés

* **Virgule de série** (*A, B, and C*) : employée partout, comme le veut l'orthographe américaine.
* **Pluriel de bitcoin** : invariable (*21 million bitcoin*), comme Bitcoin Core et Bitcoin Optech ; *bitcoins* reste correct dans une citation.
* **bloc obsolète / bloc périmé** : les deux entrées françaises désignent le *stale block* ; une seule entrée anglaise est prévue.
