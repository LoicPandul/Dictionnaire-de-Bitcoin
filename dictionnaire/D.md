## DAEMON

Type de programme informatique qui fonctionne en arrière-plan, indépendamment du contrôle de l'utilisateur. Ces programmes effectuent des tâches telles que la gestion de services réseau, la surveillance de systèmes, et la réponse à des requêtes sans nécessiter d'intervention directe. Dans le contexte de Bitcoin Core, le daemon s'appelle « bitcoind ». Il représente la version de Bitcoin Core sans interface utilisateur, qui fonctionne exclusivement en ligne de commande.

## DANDELION

Proposition qui vise à améliorer la confidentialité du routage des transactions dans le réseau Bitcoin pour contrer la désanonymisation. Dans le fonctionnement classique de Bitcoin, les transactions sont immédiatement diffusées à de multiples nœuds. Ce phénomène peut potentiellement permettre à des observateurs de lier des transactions, normalement anonymes, avec des adresses IP. L'objectif du BIP156 est de traiter ce problème. Pour ce faire, il introduit une phase supplémentaire dans la diffusion permettant de préserver l'anonymat avant la propagation publique. Ainsi, Dandelion utilise d'abord une phase de « tige » où la transaction est envoyée à travers un chemin aléatoire de nœuds, avant d'être diffusée à l'ensemble du réseau dans la phase de « capitule ». La tige et le capitule sont des références au comportement de la propagation de la transaction à travers le réseau, qui ressemble à la forme d'un pissenlit (« *a dandelion* » en anglais). Cette méthode de routage brouille la piste menant au nœud source, rendant difficile de retracer une transaction via le réseau jusqu'à son origine.

![](assets/36.png)

> ► *Pour plus d'informations, voir la définition de [**BIP156**](./B.md#bip156).*

## DARKWALLET

Logiciel de portefeuille Bitcoin axé sur la confidentialité, lancé par Amir Taaki et Cody Wilson en 2014, fonctionnant comme une extension pour le navigateur Google Chrome. DarkWallet disposait de fonctionnalités pour améliorer la confidentialité de l'utilisateur de Bitcoin, telles que les paiements furtifs et les coinjoins. Son développement a été abandonné depuis janvier 2015.

## DATABASE/

Ancien dossier contenant des bases de données pour le portefeuille Bitcoin Core. Depuis la version 0.16, cette base de données a été déplacée dans le dossier wallet/.

## DB.LOG

Ancien fichier log (historique des événements) du portefeuille Bitcoin Core déplacé dans le dossier wallet/ depuis la version 0.16.

## DDOS

Forme de DOS où l'attaque provient de multiples sources simultanément, rendant la défense plus complexe. Les attaquants utilisent souvent des réseaux d'ordinateurs infectés par des virus (botnets) pour lancer des requêtes massives vers une seule cible. Cette stratégie multiplie l'efficacité de l'attaque en surchargeant les capacités du système ciblé afin de provoquer des interruptions de service.

> ► *En français, on peut le traduire par « attaque par déni de service distribué ».*

## DEBUG.LOG

Fichier contenant l'historique des événements de Bitcoin Core. Il contient des données de journalisation, telles que les messages d'erreur, les avertissements et d'autres informations de débogage. Ce fichier est utilisé pour résoudre d'éventuels problèmes techniques.

## DEPEG

Fait référence à la situation où la valeur d'un actif numérique, typiquement une reconnaissance de dette, se désolidarise de l'actif sous-jacent auquel il est normalement indexé, entraînant ainsi des fluctuations de prix par rapport à cet actif. Ce phénomène est particulièrement observé avec les stablecoins, conçus pour maintenir une parité stricte avec des monnaies fiduciaires ou d'autres actifs de référence. Le depeg peut aussi survenir dans le cas de représentations de bitcoins sur des sidechains ou des ETF, où en cas de problème, la valeur nominale peut diverger de celle du bitcoin.

## DÉPÔT

Structure de données centrale utilisée dans Git où sont stockées les informations de versionnage d'un projet. Un dépôt contient l'historique complet de toutes les modifications, les branches et les tags. Chaque dépôt est une collection indépendante de fichiers et de dossiers, accompagnée d'un historique des commits, permettant la collaboration et le suivi des changements au fil du temps. Par exemple, le dépôt de Bitcoin Core est stocké sur GitHub ici : https://github.com/bitcoin/bitcoin.

> ► *En anglais, on parle d'un « repository ». Il est courant d'employer la troncation « repo » pour désigner un dépôt Git.*

## DER
#### Distinguished Encoding Rules (DER)

Sous-ensemble stricte des règles d'encodage ASN.1 définies dans la spécification [ITU-T X.690, 2002.](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) et utilisée pour encoder n'importe quel type de données dans une séquence binaire. DER est surtout utilisé dans des domaines spécifiques, comme en **cryptographie**, ou les données doivent êtes encodées de manière prédictibles et standard.

Sur Bitcoin, les signatures **ECDSA** ([bip 66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)) sont encodées au format **DER**. <br>
Elles se composent de deux nombres de 32 octets (`r`,`s`) encodés. Le format de signature se compose des éléments suivants :

`0x30 | length |  0x02 | r_length | r | 0x02 | s_length | s` (71 octets)

- `0x30`     (1 octet)   : identifiant d'une **structure composée**
- `length`   (1 octet)   : longueur des données suivantes
- `0x02`     (1 octet)   : identifiant de donnée type `INTEGER` (nombre entier)
- `r_length` (1 octet)   : longueur de la valeur `r` suivante (32 octets)
- `r`        (32 octets) : valeur `r` entant qu'entier gros-boutiste (big-endian)
- `0x02`     (1 octet)   : identifiant de donnée type `INTEGER` (nombre entier)
- `s_length` (1 octet)   : longueur de la valeur `s` suivante (32 octets)
- `s`        (32 octets) : valeur `s` entant qu'entier gros-boutiste (big-endian)

Notez que les valeurs r et s doivent être précédées de 0x00 si leur premier octet est supérieur à 0x7F. Cela entraîne des longueurs de signature variables dans le cas où la valeur r se situe dans la moitié supérieure de la plage (appelée « high r »). Les signatures avec des valeurs s élevées ne sont pas standard et n'apparaissent généralement pas dans la nature. Notez également que dans de rares cas, r ou s peuvent être inférieurs à 32 octets, ce qui est légal et permet d'obtenir des signatures plus courtes. Dans les transactions en bitcoins, un octet est ajouté à la fin d'une signature DER pour indiquer le type de `SigHash` utilisé.

## DÉRIVATION

Désigne le processus de génération de paires de clés enfants à partir d'une paire de clés parent (clé privée et clé publique) et d'un code de chaîne au sein d'un portefeuille déterministe et hiérarchique (HD). Ce processus permet de segmenter des branches et d’organiser un portefeuille en différents niveaux avec de nombreuses paires de clés enfants, qui peuvent toutes être récupérées en connaissant uniquement les informations de récupération de base (la phrase mnémonique et l'éventuelle passphrase). Pour dériver une clé enfant, on utilise la fonction `HMAC-SHA512` avec le code de chaîne parent et la concaténation de la clé parent et d’un index de 32 bits. Il existe deux types de dérivations :
* La dérivation normale, qui utilise la clé publique parent à la base de la fonction `HMAC-SHA512` ;
* La dérivation endurcie, qui utilise la clé privée parent à la base de la fonction `HMAC-SHA512` ;

Le résultat de HMAC-SHA512 est divisé en deux : les premiers 256 bits deviennent la clé enfant (privée ou publique après un passage dans ECDSA), et les 256 bits restants deviennent le code de chaîne enfant.

> ► *Pour plus d'informations, voir la définition de [**INDEX**](./I.md#index-numéro-de-clé).*

## DÉRIVATION ENDURCIE

Processus de génération de clés enfants dans les portefeuilles HD. La dérivation endurcie utilise la clé privée parent comme entrée pour la fonction `HMAC-SHA512`, ce qui rend impossible la génération de clés publiques enfants à partir de la clé publique parent et du code de chaîne parent. Le processus implique la concaténation de la clé privée parent et d’un index supérieur ou égal à $2^{31}$, suivi de l'application de `HMAC-SHA512` avec le code de chaîne parent. Le résultat est divisé en deux parties : les premiers 256 bits sont additionnés à la clé privée parent pour obtenir la clé privée enfant, tandis que les 256 bits restants forment le code de chaîne enfant. Cette méthode garantit que même si une clé publique étendue est compromise, elle ne peut pas être utilisée pour dériver les clés publiques enfants. Dans une dérivation standard, on utilise la dérivation endurcie à tous les niveaux de dérivation jusqu'à la profondeur des comptes. Dans les notations de chemins de dérivation, on identifie une dérivation endurcie avec une apostrophe `'` ou plus rarement avec un `h`.

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## DÉRIVATION NORMALE

Processus de génération de clés enfants dans les portefeuilles HD. La dérivation normale utilise la clé publique parent comme entrée pour la fonction `HMAC-SHA512`, ce qui rend possible la génération de clés publiques enfants à partir de la clé publique parent et du code de chaîne parent. Le processus implique la concaténation de la clé publique parent et d’un index inférieur à $2^{31}$, suivi de l'application de `HMAC-SHA512` avec le code de chaîne parent. Le résultat est divisé en deux parties : les premiers 256 bits sont additionnés à la clé privée parent pour obtenir la clé privée enfant, tandis que les 256 bits restants forment le code de chaîne enfant. Cette méthode garantit que la clé publique étendue peut être utilisée pour dériver les clés publiques enfants. Dans une dérivation standard, on utilise la dérivation normale à tous les niveaux de dérivation à partir de la profondeur des comptes. Dans les notations de chemins de dérivation, on identifie une dérivation normale lorsqu'il y a juste l'index sans aucune apostrophe `'`.

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## DGM

Sigle de « *Double Geometric Method* ». C'est une méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage. DGM est une méthode hybride, censée combiner les avantages de PPLNS et de la méthode dite « géométrique ». Elle dispose d'une faible variance sur les parts, à la manière de PPLNS, puis permet au mineur d'absorber de la variance pour réduire celle de la pool dans un second temps. DGM est résistant au pool hopping en garantissant que le paiement attendu par share reste constant. La méthode est établie sur des scores, rendant les paiements indépendants de l'historique de la pool et presque totalement indépendants des changements futurs de difficulté.

> ► *Pour plus d'informations, voir la définition de **[SHARES](./S.md#shares)**.*

## DIFFICULTÉ

Paramètre ajustable qui détermine la complexité de la preuve de travail nécessaire pour ajouter un nouveau bloc à la blockchain et gagner la récompense associée. Cette difficulté est représentée par la cible de difficulté, une valeur de 256 bits qui fixe la limite supérieure que doit respecter le hachage de l'entête d'un bloc pour être considéré comme valide. Le but est que le hachage, réalisé via une double exécution de SHA256 (SHA256d), soit inférieur ou égal à cette cible. Pour atteindre ce hachage, les mineurs manipulent le `nonce` dans l'entête du bloc. La difficulté s'ajuste tous les 2016 blocs, soit environ toutes les deux semaines, pour maintenir le temps de création de bloc moyen à environ 10 minutes.

## DIFFIE-HELLMAN

Méthode cryptographique permettant à deux parties de générer un secret partagé sur un canal de communication non sécurisé. Ce secret peut ensuite servir à chiffrer la communication entre les deux parties. Diffie-Hellman utilise l'arithmétique modulaire pour que, même si un attaquant puisse observer les échanges, il ne puisse pas déduire le secret partagé sans résoudre un problème mathématique difficile : le logarithme discret. Sur Bitcoin, on utilise parfois une variante de DH utilisant une courbe elliptique nommée ECDH, notamment pour les protocoles d'adresse statiques comme les Silent Payments ou le BIP47.

## DIFFUSION

Processus par lequel les informations, comme les transactions et les blocs, sont transmises de nœud en nœud à travers le réseau Bitcoin. Lorsqu'un utilisateur effectue une transaction, celle-ci est d'abord vérifiée par le nœud auquel il est connecté. Après validation, cette transaction est relayée aux autres nœuds connectés à celui-ci, qui à leur tour la vérifient puis la propagent. Rapidement, une grande partie des nœuds du réseau seront en connaissance de la transaction. Si elle offre suffisamment de frais, les mineurs l'incluront dans leur bloc candidat. Lorsqu'un bloc contenant cette transaction est validé, celle-ci est alors confirmée.

> ► *On parle également parfois de « propagation » pour évoquer ce processus.*

## DIGITAL ARTIFACTS

Dans le contexte du protocole Ordinals, c'est un sat qui a été inscrit avec des données spécifiques via le mécanisme d'inscriptions. Ces artefacts peuvent inclure des images, des textes, ou tout autre type de contenu numérique et sont liés indissociablement au satoshi correspondant.

> ► *En français, on peut traduire ce terme par « artefact numérique ». Pour plus d'informations, voir les définitions de **[INSCRIPTIONS](./I.md#inscriptions)** et de **[ORDINALS THEORY](./O.md#ordinals-theory)**.*

## DISTRIBUÉ

Attribut d'un réseau informatique dans lequel le pouvoir de décision et le contrôle sont répartis de manière équitable entre tous les participants du réseau. Cette répartition garantit la résilience du système. On parle également de réseau pair-à-pair. Contrairement à un réseau décentralisé, où le pouvoir est fragmenté et dispersé parmi plusieurs entités, mais où certaines autorités centrales demeurent dotées d'un pouvoir supérieur à celui des utilisateurs, un réseau distribué élimine l'autorité centrale en confiant la gestion et le contrôle aux utilisateurs eux-mêmes. Bitcoin est un exemple de système distribué. Bitcoin ne dispose pas de hiérarchie ou d'autorité centrale. La tenue du consensus, la vérification des transactions et l'émission de nouvelles unités monétaires sont réalisées par les utilisateurs. Cette structure distribuée assure la résilience et la résistance à la censure du système, rendant très difficile pour une entité unique de le contrôler ou de le manipuler.

> ► *Certaines personnes parlent de Bitcoin comme d'un système décentralisé. En effet, il n'est pas rare d'observer une interchangeabilité de ces deux termes. Un synonyme plus évocateur de l'adjectif « distribué » pourrait être « pair-à-pair », parfois abrégé « P2P », le sigle de la traduction anglaise « Peer-to-Peer ».*

## DLC (DISCREET LOG CONTRACT)

Type de contrat intelligent sur Bitcoin qui permet l'exécution de conditions contractuelles à partir du résultat d'événements externes, validés par un ou plusieurs oracles, sans que ces derniers connaissent les détails du contrat. Les DLC ont été inventés par Tadge Dryja en 2018. Ces contrats intelligents sont principalement utiles dans des applications financières, permettant, par exemple, de créer des instruments financiers ou des paris conditionnels, tout en réduisant les risques de contrepartie. Pour construire un DLC, plusieurs parties bloquent des bitcoins sur une adresse multisig. Ces bitcoins ne peuvent être débloqués que lorsque l'oracle publie les informations spécifiées à un moment donné.

## DLP (DISCREET LOG PROBLEME)

Le problème du logarithme discret (DLP) est un problème mathématique sur lequel s'appuie la sécurité des algorithmes cryptographiques à clé publique, notamment ceux utilisés sur Bitcoin. Dans un groupe cyclique d’ordre $q$, avec un générateur $g$, si l'on a une équation de la forme $g^x = h$, alors $x$ est appelé le logarithme discret de $h$ par rapport à la base $g$, modulo $q$. En termes simples, il s’agit de déterminer l’exposant $x$ lorsqu’on connaît $g$, $h$, et $q$. Le logarithme discret est donc la réciproque de l'exponentielle dans un groupe cyclique fini. Cependant, pour de grandes valeurs de $q$, résoudre le problème du logarithme discret est considéré comme algorithmiquement difficile. Cette propriété est exploitée pour assurer la sécurité de nombreux protocoles cryptographiques, tels que le protocole de Diffie-Hellman pour l'échange de clés. Le logarithme discret est aussi utilisé dans la cryptographie à courbes elliptiques (ECC), entre autres dans l'algorithme ECDSA (*Elliptic Curve Digital Signature Algorithm*). Dans le contexte des courbes elliptiques, le problème du logarithme discret s'étend à la recherche d'un scalaire $k$ tel que $k \cdot G = K$, où $G$ et $K$ sont des points sur la courbe, et $\cdot$ représente l'opération de multiplication de points. Dans le contexte de Bitcoin, les transactions standards utilisent soit ECDSA, soit le protocole de Schnorr, afin de bloquer des UTXOs. Ils reposent tous deux sur l’impossibilité de calculer le logarithme discret.

## DNS SEEDS

Points de connexion initiaux pour les nouveaux nœuds Bitcoin qui rejoignent le réseau. Ces seeds, qui sont en fait des serveurs DNS spécifiques, ont leur adresse intégrée de façon permanente dans le code de Bitcoin Core. Lorsqu'un nouveau nœud se lance, il contacte ces serveurs pour obtenir une liste aléatoire d'adresses IP de nœuds Bitcoin à priori actifs. Le nouveau nœud pourra ainsi établir des connexions avec les nœuds de cette liste afin d'obtenir les informations pour faire son IBD et se synchroniser sur la chaîne avec le plus de travail accumulé. En 2024, voici la liste des DNS seeds de Bitcoin Core et les personnes responsables de leur maintenance (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp) :
* seed.bitcoin.sipa.be : Pieter Wuille ;
* dnsseed.bluematt.me : Matt Corallo ;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us : Luke Dashjr ;
* seed.bitcoinstats.com : Christian Decker ;
* seed.bitcoin.jonasschnelli.ch : Jonas Schnelli ;
* seed.btc.petertodd.net : Peter Todd ;
* seed.bitcoin.sprovoost.nl : Sjors Provoost ;
* dnsseed.emzy.de : Stephan Oeste ;
* seed.bitcoin.wiz.biz : Jason Maurice ;
* seed.mainnet.achownodes.xyz : Ava Chow.

Les DNS seeds représentent le second moyen, par ordre de priorité, pour un nœud Bitcoin d'établir des connexions. Le premier moyen consiste à utiliser le fichier peers.dat que le nœud a lui-même créé. Ce fichier est naturellement vide dans le cas d'un nouveau nœud, à moins que l'utilisateur l'ait modifié manuellement.

> ► *Attention, les DNS seeds ne doivent pas être confondus avec les « seed nodes », qui sont eux la troisième manière d'établir des connexions. Pour plus d'informations, voir la définition de [**SEED NODES**](./S.md#seed-nodes).*

## DOLLAR COST AVERAGING (DCA)

Stratégie d'investissement qui consiste à investir un montant fixe de monnaie fiat dans un actif spécifique à intervalles réguliers, indépendamment du prix de l'actif. Cette méthode permet de réduire l'impact de la volatilité sur l'investissement global en achetant plus d'unités quand les prix sont bas et moins quand ils sont élevés. Le DCA vise généralement à construire une position sur un actif sur le long terme en minimisant les risques. C'est une stratégie très populaire pour l'investissement dans le bitcoin.

## DOS (DENIAL OF SERVICE)

Attaque informatique qui vise à rendre une ressource (site web, nœud, service en ligne...) indisponible pour ses utilisateurs légitimes. Les attaquants surchargent la cible avec un volume de données ou de requêtes excessivement élevé, ce qui épuise les ressources système et réseau de la victime, entraînant des ralentissements ou un arrêt complet. Les méthodes de DoS peuvent varier, mais l'objectif reste le même : empêcher l'accès à des services ou des données. Dans le contexte spécifique de Bitcoin, une attaque DoS peut viser à saturer le réseau ou les nœuds avec un volume excessif de requêtes afin d'entraver leur fonctionnement normal. L'objectif est souvent de nuire à un opérateur de nœud ou à la disponibilité du réseau pour les utilisateurs honnêtes.

> ► *En français, on peut le traduire par « attaque par déni de service ».*

## DOUBLE DÉPENSE (ATTAQUE)

Attaque où un utilisateur malveillant tente d'utiliser le même UTXO (*Unspent Transaction Output*) plus d'une fois afin de s'enrichir sur les contreparties des transactions impliquées. En principe, une fois qu'une transaction est confirmée dans un bloc et ajoutée à la blockchain, l'utilisation de ces bitcoins est enregistrée de manière permanente, empêchant toute dépense ultérieure de ces mêmes bitcoins. Prévenir la double dépense est même l'utilité première de la blockchain. 

Dans le cadre d'une attaque de double dépense, l'attaquant effectue d'abord une transaction légitime auprès d'un commerçant, puis crée une seconde transaction concurrente qui dépense les mêmes pièces, soit en les renvoyant vers lui-même pour récupérer la somme, soit en les utilisant pour acheter un autre bien ou service auprès d'un autre commerçant. 

Deux scénarios principaux peuvent permettre cette attaque. Le premier, et le plus simple pour l'attaquant, consiste à exécuter la transaction frauduleuse avant que la transaction légitime ne soit incluse dans un bloc. Pour permettre la confirmation de sa transaction frauduleuse en première, l'attaquant y associe des frais de transaction nettement plus élevés que la transaction légitime. C'est une sorte de RBF frauduleux. Ce scénario n'est possible que si le commerçant accepte de finaliser la vente en « zeroconf », c'est-à-dire sans aucune confirmation pour la transaction de paiement. C'est pourquoi il est fortement recommandé d'attendre plusieurs confirmations avant de considérer une transaction comme immuable. Le second scénario, beaucoup plus complexe, est celui d'une attaque à 51 %. Si l'attaquant contrôle une part importante de la puissance de calcul du réseau, il peut miner une chaîne concurrente à celle contenant la transaction légitime, mais incluant sa transaction frauduleuse. Lorsque le commerçant a accepté la vente et que l'attaquant a réussi à créer une chaîne plus longue (avec plus de travail accumulé) que la chaîne légitime, il peut alors diffuser sa chaîne frauduleuse qui sera reconnue par les nœuds du réseau comme étant celle valide.

## DRIVECHAIN

Forme spécifique de sidechain où les mineurs de la blockchain principale (Bitcoin) ont un rôle direct dans la gouvernance de l'ancrage bilatéral et éventuellement dans le mécanisme de consensus de la sidechain. Ce protocole a été inventé par Paul Sztorc et pourrait être mis en place grâce aux controversés BIP300, qui permettrait le two-way peg auprès des mineurs, et BIP301, qui permettrait d'utiliser le minage fusionné (merged mining) de manière optimale.

## DUMMY ELEMENT

Fait référence à un élément supplémentaire et inutile consommé par les opcodes `OP_CHECKMULTISIG` et `OP_CHECKMULTISIGVERIFY` lors de la vérification des signatures dans une transaction. En raison d'un bug off-by-one historique (erreur de décalage unitaire), ces 2 opcodes suppriment un élément supplémentaire sur la pile en plus de leur fonction de base. Pour éviter une erreur, il est donc obligatoire d'inclure une valeur factice au début du `scriptSig` afin de satisfaire la suppression et outrepasser le bug. Cette valeur inutile, c'est ce que l'on appelle le « *dummy element* ». Le BIP11, qui a introduit le standard P2MS, conseillait de mettre un `OP_0` comme valeur inutile. Mais ce standard n'était pas imposé au niveau des règles de consensus, ce qui veut dire que n'importe quelle valeur pouvait y être placée, sans invalider la transaction. Le dummy element était donc un vecteur de malléabilité des transactions. Le BIP147, introduit avec le soft fork SegWit, a imposé que cet élément factice soit strictement un tableau d'octets vide (`OP_0`), éliminant ainsi la malléabilité associée à cet élément en rendant toute transaction non conforme invalide selon les règles de consensus. Cette règle, nommée `NULLDUMMY`, s'applique à la fois aux transactions SegWit et pré-SegWit.

> ► *Pour plus d'informations, voir la définition de [**BIP147**](./B.md#bip147) et [**OP_CHECKMULTISIG**](./O.md#op_checkmultisig-0xae).*

## DUST

Fait référence à des montants de pièces bitcoin extrêmement petits qui sont trop minimes pour être envoyés dans une transaction, car les frais de transaction nécessaires pour les inclure dans un bloc seraient proportionnellement plus élevés que leur valeur. La définition précise de « dust » peut varier selon le contexte, mais il s'agit généralement de toute sortie de transaction qui nécessite plus de frais pour être dépensée qu'elle n'incarne de valeur. Pour l'utilisateur de Bitcoin, il est important de gérer ses UTXOs et de pratiquer la consolidation de ceux-ci afin qu'ils ne deviennent pas du dust.

> ► *En français, on pourrait parler de « poussière ».*

## DUSTING ATTACK

Attaque qui consiste à envoyer de minuscules quantités de bitcoins à un grand nombre d'adresses de réception. L'objectif de l'attaquant est de pousser les destinataires à regrouper ces sommes avec d'autres UTXOs. L'attaquant suit ensuite les déplacements futurs de ces faibles quantités de bitcoins, dans le but de former des clusters d'adresses, c'est-à-dire de déterminer si plusieurs adresses appartiennent à une même entité. En croisant les informations recueillies lors d'une dusting attack avec d'autres données et heuristiques utilisées dans l'analyse de chaîne, il est possible pour l'attaquant d'identifier certaines entités et les adresses associées. Cette méthode représente une menace uniquement pour la confidentialité des utilisateurs, mais n'affecte pas la sécurité de leurs fonds.

> ► *Certains bitcoiners suggèrent de ne plus utiliser le terme de « dusting attack » car celui-ci induirait en erreur. En effet, le terme de « dust » décrit quelque chose de bien précis dans Bitcoin Core. Si la dusting attack utilisait réellement du dust comme décris dans Core, l'attaque serait inefficace. Certains suggèrent ainsi d'utiliser le terme de « forced address reuse » (réutilisation d'adresse forcée) pour décrire plus précisément cette attaque.*

## DUST LIMIT

Désigne le seuil en sats en deçà duquel un UTXO est considéré comme de la « poussière » (dust) par un nœud du réseau. Ce seuil fait partie des règles de standardisation qui peuvent être modifiées indépendamment par chaque nœud. Dans Bitcoin Core, cette limite est déterminée par un taux de frais spécifique, fixé par défaut à 3 000 sats par kilo-octet virtuel (sats/kvB). Cette limite vise à restreindre la propagation de transactions comprenant de très petits montants en bitcoins. En effet, un UTXO qualifié de poussière implique que son utilisation n'est économiquement pas rationnelle : dépenser cet UTXO coûterait plus cher que de simplement l'abandonner. Si dépenser de la poussière n'est pas rationnel, cela suggère que de telles dépenses ne puissent être motivées que par des incitations externes, souvent malveillantes. Cela peut notamment poser un problème si un acteur malintentionné cherche à saturer le réseau avec des transactions contenant des montants infimes, dans le but d'accroître la charge opérationnelle des nœuds et potentiellement les empêcher de traiter d'autres transactions légitimes. Pour donner une analogie (un peu bancale, je vous l'accorde), c'est un peu comme si quelqu'un tentait de payer un panier de courses de 100 € uniquement en pièces de 1 centime afin de bloquer les autres clients de la caisse.

> ► *Pour plus d'informations, voir les définitions de [**DUST**](./D.md#dust), [**DUSTING ATTACK**](./D.md#dusting-attack) et de [**DUSTRELAYFEE**](./D.md#dustrelayfee).*

## DUSTRELAYFEE

Règle de standardisation utilisée par les nœuds du réseau pour déterminer ce qu'ils considèrent comme la « limite de poussière » (dust limit). Ce paramètre fixe un taux de frais en sats par kilo-octet virtuel (sats/kvB) qui sert de référence pour calculer si la valeur d'un UTXO est inférieure aux frais nécessaires pour l'inclure dans une transaction. En effet, un UTXO est considéré comme « dust » (poussière) sur Bitcoin s'il requiert plus de frais pour être transféré que la valeur qu'il représente lui-même. Le calcul de cette limite est le suivant :

```text
limite = (taille de l'entrée + taille de la sortie) * taux de frais
```

Comme le taux de frais requis pour qu'une transaction soit incluse dans un bloc Bitcoin varie constamment, le paramètre `DustRelayFee` permet de définir le taux de frais utilisé dans ce calcul par chaque nœud. Par défaut, sur Bitcoin Core, cette valeur est fixée à 3 000 sats/kvB. Par exemple, pour calculer la limite de poussière d'une entrée et d'une sortie P2PKH, qui mesurent respectivement 148 et 34 octets, le calcul serait : 

```text
limite (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Cela signifie que le nœud en question ne relayera pas les transactions incluant un UTXO sécurisé en P2PKH dont la valeur est inférieure à 546 sats.
