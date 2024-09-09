## HACHEUR

► ***EN : HASHER***

Dans le contexte des pools de minage, les participants sont souvent désignés sous le terme de « hacheurs ». Ces mineurs individuels ont pour tâche principale de hacher des blocs templates fournis par le serveur de la pool, en recherchant des hachages qui satisfont la cible de difficulté définie pour les shares, et non celle de Bitcoin. Le reste du processus de minage, qui inclut la construction effective des blocs, la sélection des transactions ou la recherche de la preuve de travail selon la difficulté propre à Bitcoin, ainsi que la diffusion, est effectué directement par les pools.

> ► *Pour plus d'informations, voir la définition de **[POOL (MINING)](./P.md#pool-mining)**.*

## HALVING

Le terme « halving » (division par deux) fait référence à un événement programmé qui réduit de moitié la récompense attribuée aux mineurs pour chaque bloc miné via la subvention de bloc. Cette réduction s'applique spécifiquement à la partie de la subvention de bloc constituée de nouveaux bitcoins créés ex-nihilo. Le halving a été conçu par Satoshi Nakamoto, le créateur de Bitcoin, comme un mécanisme permettant de contrôler l'inflation et d'assurer un approvisionnement limité en bitcoins.

La récompense de bloc initiale était de 50 bitcoins, et le halving se produit tous les 210 000 blocs minés, ce qui prend environ quatre ans. Les halvings ont eu lieu :
* Au bloc 210 000 le 28 novembre 2012 pour réduire la subvention à 25 BTC ;
* Au bloc 420 000 le 9 juillet 2016 pour réduire la subvention à 12,5 BTC ;
* Au bloc 630 000 le 11 mai 2020 pour réduire la subvention à 6,25 BTC ;
* Au bloc 840 000 le 20 avril 2024 pour réduire la subvention à 3,125 BTC.

Les halvings continueront à se produire jusqu'à ce que la récompense de bloc atteigne zéro, moment auquel l'offre maximale d'environ 21 millions de bitcoins aura été atteinte. Le prochain halving de Bitcoin devrait avoir lieu aux alentours du printemps 2028, bien que la date exacte puisse légèrement varier en fonction du temps de minage des blocs. À ce moment-là, la récompense de bloc sera réduite de 3,125 à 1,5625 bitcoins. Ce sera le cinquième halving de l'histoire de Bitcoin. À mesure que les subventions de bloc baissent, les frais de transaction deviennent une source de revenus de plus en plus importante pour les mineurs, ce qui garantit leur motivation à continuer à participer à la preuve de travail.

## HARD FORK

Modification des règles du protocole de manière non rétrocompatible. Cette modification donne lieu à une séparation définitive du réseau de nœuds Bitcoin en deux groupes distincts : les nœuds avec la mise à jour et les nœuds sans la mise à jour. Cette scission se matérialise par la division de la blockchain originale en deux blockchains distinctes, partageant toutefois un historique commun, d'où l'usage du terme « fork », traduisible en français par « embranchement, bifurcation ».

Une modification est dite non rétrocompatible lorsqu'elle est soit extensive, c'est-à-dire qu'elle supprime ou rend moins restrictives certaines règles du protocole, soit bilatérale, c'est-à-dire qu'elle ajoute des règles incompatibles avec les anciennes. En d'autres termes, un hard fork s'observe lorsque certains nœuds font en sorte qu'un bloc invalide devienne valide. En résulte alors la formation d'une nouvelle version du protocole, qui peut soit remplacer le Bitcoin original si une majorité est trouvée, soit devenir un altcoin indépendant s'il n'est qu'utilisé en marge. Par exemple, Bitcoin Cash (BCH) est un hard fork de Bitcoin. L'embranchement a eu lieu au bloc n° 478 559, le 1er août 2017.

## HARDWARE WALLET

Un hardware wallet, ou portefeuille matériel, est un dispositif électronique dédié à la sécurisation et à la gestion des clés privées d'un portefeuille Bitcoin. Ces périphériques sont conçus pour procurer une sécurité renforcée par rapport aux portefeuilles logiciels qui sont sur des machines polyvalentes et directement connectées à internet. Les hardwares wallets stockent la phrase mnémonique hors ligne, sur un matériel qui dispose d'une infime surface d'attaque, ce qui l'isole des environnements potentiellement vulnérables. Lorsqu'une transaction est effectuée, le portefeuille matériel signe la transaction à l'intérieur du dispositif lui-même, sans exposer la clé privée à l'extérieur. Une fois la transaction signée, elle est transmise au réseau Bitcoin pour être confirmée et incluse dans la blockchain Bitcoin. Parmi les modèles de hardwares wallets les plus populaires, on peut citer : Ledger, Trezor, Coldcard, Passport, BitBox, Satochip, Jade ou encore SeedSigner (liste non exhaustive).

> ► *Le hardware wallet peut être exprimé de différentes manières en français. Certains parlent de « portefeuille matériel » ou bien de « portefeuille froid ». Certains bitcoiners préfèrent que l'on emploie le terme de « périphérique de signature », ou « signing device » en anglais, afin d'éviter de faire penser que les bitcoins se trouvent physiquement dans le portefeuille.*

## HASH160

Fonction cryptographique utilisée sur Bitcoin notamment pour générer des adresses de réception Legacy et SegWit v0. Elle combine deux fonctions de hachage qui s'exécute successivement sur l'input : d'abord SHA256, puis RIPEMD160. La sortie de cette fonction est donc de 160 bits.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$

## HASH256

Fonction cryptographique utilisée pour diverses applications sur Bitcoin. Elle consiste en l'application double de la fonction SHA256 sur les données en entrée. Le message est passé une première fois dans SHA256, et le résultat de cette opération est utilisé comme entrée pour passer une seconde fois dans SHA256. La sortie de cette fonction est donc de 256 bits.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$

## HASHCASH

Système de preuve de travail conçu par Adam Back en 1997 pour lutter contre le spam et les attaques DoS. Il repose sur le principe qu'un expéditeur doit effectuer un travail de calcul (spécifiquement, la recherche d'une collision partielle sur une fonction de hachage cryptographique) pour prouver son travail. Cette tâche est coûteuse en temps et en énergie pour l'expéditeur, mais la vérification du résultat par le destinataire est rapide et simple. Ce protocole s'est révélé particulièrement adapté à la lutte contre le spam dans les messageries électroniques, car il est peu contraignant pour les utilisateurs légitimes, tout en constituant un obstacle majeur pour les spammeurs. En effet, l'envoi d'un seul courriel requiert quelques secondes de calcul, mais reproduire cette opération des millions de fois rend l'opération extrêmement coûteuse en termes d'énergie et de temps, ce qui vient souvent annuler l'intérêt économique des campagnes de spam, qu'elles soient à but marketing ou malveillant. De plus, il permet de préserver l'anonymat de l'expéditeur. 

HashCash a rapidement été adopté par des cypherpunks qui cherchaient à développer un système de monnaie électronique anonyme sans intermédiaire. En effet, l'innovation d'Adam Back a introduit pour la première fois la notion de rareté dans le monde numérique. On retrouve alors le concept de preuve de travail dans plusieurs systèmes de monnaies électroniques antérieurs à Bitcoin, dont :
* b-money de Wei Dai publié en 1998 ;
* R-POW de Hal Finney publié en 2004 ;
* BitGold de Nick Szabo publié en 2005.

Le principe de HashCash se retrouve également au sein du protocole Bitcoin, où il est utilisé comme mécanisme de protection face aux attaques Sybil.

## HASHRATE

► ***FR : TAUX DE HACHAGE***

Indicateur de la puissance de calcul du réseau, mesurée en hachages par seconde (H/s). Il indique la capacité des mineurs à exécuter des opérations de hachage dans le cadre de la preuve de travail. Un hashrate élevé signifie une plus grande sécurité de l'historique économique de Bitcoin et une plus grande résistance aux attaques, car il faudrait une importante quantité de puissance de calcul pour compromettre le réseau. 

Le hashrate est également indicatif de la concurrence entre les mineurs : plus le hashrate est élevé, plus la difficulté de minage est grande, ce qui influence la répartition des récompenses, et donc la rentabilité des mineurs. C'est donc un indicateur clé de la santé et de la sécurité du système Bitcoin. De la même manière que le hashrate sert à mesurer la puissance de calcul globale du réseau Bitcoin, il peut également être utilisé pour mesurer la puissance de calcul d'une machine, d'une ferme de minage ou encore d'une pool de minage.

## HAUTEUR DE BLOC

► ***EN : BLOCK HEIGHT***

Désigne le numéro de séquence d'un bloc particulier par rapport au premier bloc, connu sous le nom de « bloc de Genèse », qui est indexé à la hauteur zéro. Cet indicateur nous donne le nombre de blocs qui précèdent le bloc étudié. Par exemple, si un bloc est à la hauteur 650 000, cela signifie qu'il y a 650 000 blocs qui le précèdent. La hauteur de bloc est utilisée pour identifier un bloc spécifique au sein de la blockchain. Contrairement à une croyance répandue, la hauteur de bloc ne détermine pas quelle est la chaine valide, car les nœuds se synchronisent sur la chaîne ayant accumulé le plus de travail, et non sur la chaîne la plus longue.

## HD (HIERARCHICAL-DETERMINISTIC)

► ***FR : DÉTERMINISTE ET HIÉRARCHIQUE***

Se dit d'un portefeuille Bitcoin qui utilise une information unique (la graine ou « seed » en anglais) pour générer une multitude de paires de clés publiques et privées de manière séquentielle et reproductible. Cette manière de gérer des clés est définie par le standard BIP32. L'avantage principal des portefeuilles HD est qu'ils permettent aux utilisateurs de disposer d'une multitude de paires de clés différentes, notamment afin d'éviter la réutilisation d'adresse, tout en pouvant toutes les régénérer depuis une information unique. On dit de cette structure qu'elle est hiérarchique, car elle permet de créer une organisation en arborescence de multiples clés et adresses à partir d'une seule graine. Et elle est déterministe dans le sens où chaque graine génère toujours la même séquence de clés dans n'importe quel portefeuille conforme à ce système.

> ► *Pour plus d'informations, voir les définitions de **[BIP32](./B.md#bip32)** et [**BIP44**](./B.md#bip44).*

## HEURISTIQUE D'ANALYSE

► ***EN : ANALYSIS HEURISTIC***

Une heuristique d'analyse de chaîne sur Bitcoin est une famille de méthodes empiriques utilisées pour tracer les flux de bitcoins sur la blockchain en se basant sur des caractéristiques observées dans les transactions. Une heuristique est une approche pratique qui permet de résoudre des problèmes, souvent par des méthodes approximatives, mais qui représente une solution suffisamment bonne pour atteindre un objectif donné. Ces heuristiques permettent d'obtenir des résultats assez fiables, mais jamais d'une précision absolue. En d'autres termes, l'analyse de chaîne implique toujours une dimension de vraisemblabilité dans les conclusions émises. Par exemple, on pourra estimer avec plus ou moins de certitude que deux adresses appartiennent à une même entité, mais une certitude totale sera toujours hors de portée. Tout l’objectif de l'analyse de chaîne réside précisément dans l'agrégation de diverses heuristiques en vue de minimiser le risque d'erreur. Il s'agit en quelque sorte d'une accumulation de preuves qui nous permet de nous approcher davantage de la réalité. Dans ce cadre, on différencie les heuristiques internes et les heuristiques externes.

Les heuristiques internes se concentrent sur les caractéristiques spécifiques à l'intérieur d'une transaction individuelle. Elles incluent dans leur analyse des éléments tels que les montants des UTXOs, les scripts utilisés, les versions ou encore les locktimes. Par exemple, l'heuristique du paiement rond permet d'identifier une sortie de transaction comme étant vraisemblablement un paiement si son montant est un nombre rond. Ces heuristiques permettent souvent d'identifier le change (rendu de monnaie qui revient vers le même utilisateur) et donc de continuer le traçage.

Les heuristiques externes, quant à elles, analysent les similitudes et les caractéristiques au-delà de la transaction en elle-même. Elles englobent tout l'environnement de la transaction. Par exemple, la réutilisation d'adresse sur plusieurs transactions est une heuristique externe. La CIOH en est également une.

## HEXADÉCIMAL

Système de numération en base 16, qui utilise donc 16 symboles distincts pour représenter les nombres. Les 10 premiers symboles sont les chiffres de 0 à 9, identiques à ceux du système décimal (base 10), et les six symboles suivants sont représentés par les lettres A à F. Ainsi, A représente le nombre 10, B représente 11, jusqu'à F qui représente 15. Ce système est particulièrement utilisé en informatique, car il offre une représentation plus concise des nombres binaires (base 2), et chaque chiffre hexadécimal représente exactement 4 bits, ce qui simplifie les conversions. On retrouve très souvent ce système de numération pour représenter les informations sur Bitcoin.

## HMAC-SHA512

`HMAC-SHA512` est l’acronyme de « *Hash-based Message Authentication Code - Secure Hash Algorithm 512* ». C’est un algorithme cryptographique utilisé pour vérifier l'intégrité et l'authenticité des messages échangés entre deux parties. Il combine la fonction de hachage cryptographique `SHA512` avec une clé secrète partagée pour générer un code d'authentification de message (MAC) unique pour chaque message.

Dans le contexte de Bitcoin, l'utilisation naturelle de `HMAC-SHA512` est légèrement dérivée. On utilise cet algorithme dans le processus de dérivation déterministe et hiérarchique de l'arbre de clés cryptographiques d'un portefeuille. `HMAC-SHA512` est notamment utilisé pour passer de la graine (seed) à la clé maîtresse, puis pour chaque dérivation d’une paire parent vers des paires enfants. On retrouve également cet algorithme au sein d'un autre algorithme de dérivation, nommé `PBKDF2`, utilisé pour passer de la phrase de récupération et de la passphrase à la graine.

## HODL

Terme populaire dans la communauté Bitcoin qui désigne le fait de conserver ses bitcoins sur le long terme, malgré la volatilité des marchés, et de ne pas les vendre. Le terme est né d'une faute de frappe dans [un message posté en 2013 sur le forum Bitcoin Talk](https://bitcointalk.org/index.php?topic=375643.msg4022997#msg4022997) par l'utilisateur *GameKyuubi* qui semblait être en état d'ébriété, dans lequel il écrit « I AM HODLING » au lieu de « I AM HOLDING », ce qui signifie « garder » en anglais. Ce mot est rapidement devenu un mème et un slogan.

## HONG-KONG ROUNDTABLE

Évènement historique de la Blocksize War qui s'est tenu le 20 février 2016 à Hong-Kong. C'était une réunion importante entre les développeurs de Bitcoin Core et les mineurs pour discuter de l'évolutivité du système et de la stratégie à adopter pour le faire passer à l'échelle. Les tensions étaient élevées avant la réunion, notamment à cause de la montée en puissance de Bitcoin Classic, une proposition de hard fork soutenue par Gavin Andressen qui visait à augmenter la taille des blocs à 2 Mo. Lors de cette réunion, des personnalités influentes dans l'écosystème ont pris part aux débats, notamment Jihan Wu et Micree Zhan, les co-fondateurs de Bitmain, Adam Back, le président de Blockstream, ou encore Luke Dashjr, Matt Corallo et Peter Todd.

Les mineurs, frustrés par le manque de progrès, ont menacé de soutenir Bitcoin Classic si un hard fork à 2 Mo n'était pas implémenté. Les développeurs ont défendu SegWit comme une solution viable. Après des heures de négociations tendues, un accord a été trouvé, stipulant que les développeurs de Bitcoin Core travailleraient sur un hard fork après l'implémentation de SegWit. Cet accord était censé apaiser les tensions, mais il a finalement créé davantage de méfiance et de confusion. Chaque camp a interprété l'accord différemment, ce qui a exacerbé les divisions au sein de la communauté. Bien que cet accord ait temporairement freiné l'élan de Bitcoin Classic, il a été perçu par beaucoup comme une solution insatisfaisante et maladroite.

> ► *Pour plus d'informations, voir la définition de **[BLOCKSIZE WAR](./B.md#blocksize-war)**.*

## HORODATAGE

► ***EN : TIMESTAMP***

L'horodatage, ou « timestamp » en anglais, est un mécanisme qui consiste à associer un repère temporel précis à un événement, une donnée ou un message. Dans le contexte généraliste des systèmes informatiques, l'horodatage sert à déterminer l'ordre chronologique des opérations et à vérifier l'intégrité des données en fonction du temps.

Dans le cas spécifique de Bitcoin, les horodatages permettent d'établir la chronologie des transactions et des blocs. Chaque bloc dans la blockchain contient un horodatage indiquant le moment approximatif de sa création. Satoshi Nakamoto parle même d'un « serveur d'horodatage », dans son White Paper, pour décrire ce que l'on appellerait aujourd'hui la « blockchain ». Le rôle de l'horodatage sur Bitcoin est de déterminer la chronologie des transactions, afin de pouvoir déterminer, sans l'intervention d'une autorité centrale, quelle transaction est arrivée en première. Ce mécanisme permet à chaque utilisateur de vérifier la non-existence d'une transaction par le passé, et donc d'éviter qu'un utilisateur malintentionné opère une double dépense. Ce mécanisme est justifié par Satoshi Nakamoto dans son White Paper par la célèbre phrase : « *Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.* » Cette norme est établie sur l'heure Unix, qui représente le total de secondes passées depuis le premier janvier 1970.

> ► *L'horodatage des blocs est relativement flexible sur Bitcoin, car pour qu'un horodatage soit considéré comme valide, il est simplement nécessaire qu'il soit plus grand que le temps médian des 11 blocs qui le précèdent (MTP) et plus petit que la médiane des temps retournés par les nœuds (network-adjusted time) plus 2 heures.*

## HRP (HUMAN READABLE PART)

Le HRP, pour « *Human Readable Part* » (partie lisible par l'homme), est un composant des adresses de réception bech32 et bech32m (SegWit v0 et SegWit v1). Le HRP fait référence à la portion de l'adresse qui est spécifiquement formatée pour être facilement lue et interprétée par les humains. Prenons l'exemple d'une adresse Bitcoin bech32 :

```text
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqx5
```

Dans cette adresse, le `bc` initial représente le HRP. Ce préfixe permet d'identifier en un coup d'œil que cette suite de caractères que l'on nous présente est une adresse Bitcoin et pas autre chose.

## HTLC

Sigle de « *Hashed Timelock Contract* ». C'est un mécanisme de contrat intelligent principalement utilisé sur Lightning. On le retrouve aussi parfois dans des atomic swaps. Fondamentalement, le HTLC permet de conditionner un transfert de fonds à la révélation d'un secret, et inclut également une condition temporelle pour protéger l'argent de l'envoyeur en cas d'échec de la transaction.

Sur Lightning, les HTLC permettent d’envoyer des bitcoins à un nœud avec lequel on ne dispose pas de canal direct, en passant à travers plusieurs canaux, sans besoin de confiance tout au long de la route. Le paiement entre chaque nœud est conditionné par la fourniture d’une préimage (le secret qui, lorsqu'il est haché, correspond à une valeur convenue). Si le destinataire final fournit cette préimage, il peut réclamer les fonds, et permet forcément à chaque nœud intermédiaire de réclamer, eux aussi, les fonds en cascade. 

Par exemple, si Alice veut envoyer 1 BTC à David, mais qu'elle n'a pas de canal direct avec lui, elle doit passer par Bob et Carol, qui ont des canaux de paiement entre eux. Voici comment la transaction se déroule :
* David présente une invoice Lightning à Alice. Celle-ci contient le hachage $h$ d'un secret $s$ (la préimage) que seul David connait. On a donc : $h = \text{hachage}(s)$ ;
* Alice crée un HTLC avec Bob, qui propose de lui envoyer 1 BTC à condition que Bob lui fournisse un secret $s$ (la préimage) qui correspond au hachage $h$ ;
* Bob crée un HTLC avec Carol, qui propose de lui envoyer 1 BTC à condition qu'elle fournisse le même secret $s$ ;
* Carol crée un HTLC avec David, qui propose encore 1 BTC s'il révèle la préimage $s$ ;
* David révèle $s$ (qu'il était le seul à connaître) à Carol pour recevoir 1 BTC. Carol peut désormais utiliser $s$ pour récupérer le BTC auprès de Bob. Et Bob, qui connait maintenant $s$, fait de même avec Alice.

Finalement, Alice a envoyé 1 BTC à David en passant par Bob et Carol (une action neutre pour ces derniers), sans que personne ait à se faire confiance, car tout est sécurisé en cascade par les conditions des HTLCs.

Les HTLCs permettent ainsi de faire des échanges dits « atomiques » : soit le transfert est entièrement réussi, soit il échoue, et les fonds sont restitués. Cela garantit la sécurité des transactions même entre plusieurs participants sans besoin de confiance.

## HWI

Sigle de « *Hardware Wallet Interface* ». C'est une interface standardisée permettant l'intégration et l'interaction entre des logiciels de gestion de portefeuilles Bitcoin et des portefeuilles matériels (hardware wallets). Plus précisément, HWI est à la fois une bibliothèque en Python et un outil en ligne de commande. Il facilite la communication entre ces composants en utilisant des PSBTs (transactions Bitcoin partiellement signées) et éventuellement des Descriptors (output script descriptors). Cette interface a d'abord été développée pour Bitcoin Core, puis, elle est devenue un standard utilisé par la plupart des logiciels de portefeuilles.
