## C (LANGAGE)

Langage de programmation de haut niveau, créé dans les années 1970 par Dennis Ritchie. Il est connu pour sa performance, sa flexibilité et sa portabilité, ce qui en fait un choix populaire pour le développement de logiciels. Sa syntaxe a servi de base à de nombreux autres langages, y compris C++, Java et C#.

## C++ (PLUS PLUS)

Langage de programmation polyvalent, évoluant du C, connu pour sa puissance et sa flexibilité. Utilisé pour le développement logiciel complexe, il prend en charge la programmation orientée objet et offre de riches fonctionnalités pour la gestion de la mémoire et des ressources système. 

Bitcoin Core, l'implémentation majoritaire du protocole Bitcoin, est écrite en C++. C'est un héritage du tout premier client de Satoshi qui était aussi dans ce langage de programmation. Pour garantir une cohérence stricte du comportement des nœuds sur le réseau, notamment pour éviter les forks, il a été choisi de ne pas changer de langage depuis 2009.

## CAHOOTS

Dans le cadre du portefeuille Samourai Wallet et d'autres logiciels de portefeuilles qui l'implémente, un Cahoot désigne tous les types de transactions réalisées en collaboration entre plusieurs utilisateurs. Procéder à un Cahoot signifie donc participer conjointement à une transaction. Cette collaboration s'articule autour de l'échange de transactions partiellement signées. Ces échanges peuvent se faire soit manuellement, via des codes QR, soit de manière automatisée, via le réseau de communication Soroban. Parmi les cahoots, on retrouve :
* Les transactions Stowaway (Payjoin) ;
* Les transactions Stonewall x2 ;
* Les transactions Joinbot.

## CANAL DE PAIMENT

Dans le cadre du Lightning Network, un canal de paiement est une connexion bidirectionnelle entre deux nœuds Lightning qui permet de faire des échanges de bitcoins off-chain. On-chain, un canal de paiement est représenté par une adresse multisignatures 2/2 détenue par les deux participants. Le canal de paiement nécessite une transaction on-chain pour son ouverture et une autre pour sa fermeture. Entre ces deux évènements, les utilisateurs du canal peuvent réaliser un très grand nombre d'échanges de bitcoins off-chain, sur le Lightning Network, sans nécessiter une activité on-chain. Sur Lightning, il est possible de router un paiement à travers plusieurs canaux et plusieurs nœuds, afin d'envoyer des bitcoins sans forcément ouvrir un canal direct avec le receveur.

## CAPACITÉ DE CANAL LIGHTNING

Quantité de bitcoins bloqués sur une adresse multisignatures qui représente un canal de paiement sur le Lightning Network. La capacité d'un canal est donc la quantité maximale de sats qui peut être transmise via ce canal spécifique. Elle est définie au moment de la création du canal par la somme des fonds qu'une partie engage dans le canal. L'« *inbound capacity* », ou « capacité entrante », désigne la quantité maximale de bitcoins qu'un nœud peut recevoir via un canal. L'« *outbound capacity* », ou « capacité sortante » représente la quantité maximale de bitcoins qu'un nœud peut envoyer à travers un canal spécifique.

## CASHU

Protocole open-source de monnaie électronique chaumienne, similaire au système eCash de David Chaum, mais qui fonctionne sur Bitcoin et le Lightning Network. Plus précisément, Cashu est inspiré d'une variante d'eCash proposée en 1996 par David Wagner nommée « *Chaumian ecash without RSA* ». Cashu peut être utilisé sur des portefeuilles custodiaux afin que le serveur ne puisse identifier ni les propriétaires des fonds, ni les détails des transactions, offrant ainsi une amélioration de la confidentialité. Les utilisateurs peuvent générer des jetons Cashu en échange de bitcoins, qui sont signés par le serveur sans connaitre l'utilisateur. Les jetons peuvent ensuite être transférés entre utilisateurs de manière instantanée, privée et sans frais. 

> ► *Pour plus d'informations, voir la définition de [**ECASH**](./E.md#ecash-david-chaum).*

## CET

Sigle de « *Contract Execution Transaction* ». C'est une transaction spécifique au sein d'un DLC qui permet le règlement final entre les parties en fonction de l'issue d'un événement futur. Lorsque l'oracle publie une signature correspondant au résultat de l'événement, les parties utilisent cette signature pour compléter et déverrouiller la CET qui envoie les fonds à la partie gagnante. La CET signée est ensuite minée, et le gagnant reçoit les bitcoins qui lui sont dus selon les conditions du contrat intelligent. Toutes les autres CET potentielles, qui auraient été exécutées en cas de résultats différents, deviennent obsolètes et sont abandonnées.

> ► *Pour plus d'informations, voir la définition de [**DLC (DISCREET LOG CONTRACT)**](./D.md#dlc-discreet-log-contract).*

## CHAINE EXTERNE

Dans la dérivation des portefeuilles déterministes et hiérarchiques, la chaîne externe est une branche de dérivation utilisée pour générer des adresses de réception destinées à recevoir des paiements venus de l'extérieur, c'est-à-dire d'un autre portefeuille. Chaque compte tel que défini en profondeur 3 dispose de deux chaînes en profondeur 4 : une chaîne externe et une chaîne interne (également appelée « change »). La chaine externe est dérivée avec un index de `/0/`.  La chaîne externe dérive des adresses destinées à être communiquées publiquement, c’est-à-dire les adresses que l’on nous propose lorsque l’on clique sur le bouton « recevoir » dans notre logiciel de portefeuille.

![](assets/22.png)

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## CHAINE INTERNE

Dans la dérivation des portefeuilles déterministes et hiérarchiques, la chaîne interne est une branche de dérivation utilisée pour générer des adresses de réception destinées à recevoir des paiements venus du même portefeuille, c'est-à-dire uniquement des adresses de change. Chaque compte tel que défini en profondeur 3 dispose de deux chaînes en profondeur 4 : une chaîne externe et une chaîne interne (également appelée « chaîne de change »). La chaine interne est dérivée avec un index de `/1/`.

![](assets/22.png)

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## CHANNEL FACTORIES

Mécanisme avancé en cours de travail sur Lightning, permettant la création et la gestion de plusieurs canaux de paiement à partir d'un seul UTXO. Les channel factories utilisent des adresses multisig `n-of-n` pour qu'un groupe d'utilisateurs puisse détenir collectivement un seul UTXO. De là, ils peuvent ouvrir et fermer des canaux de paiement entre eux sans transactions supplémentaires on-chain, sauf lorsqu'ils souhaitent retirer leurs fonds de la factory. Cette méthode permettrait de réduire considérablement les coûts et l'espace occupé sur Bitcoin pour des transactions Lightning. En pratique, cela signifie que des opérations qui nécessiteraient normalement des transactions on-chain pour chaque ouverture ou fermeture de canal peuvent être effectuées hors chaîne, avec la sécurité garantie par la capacité de publier les transactions non publiées si nécessaire. Pour reprendre les mots de David A. Harding, les channel factories peuvent être décrites comme des canaux Lightning utilisés pour générer d'autres canaux Lightning.

## CHAINSPLIT

Nom parfois donné à un embranchement naturel, c'est-à-dire une séparation temporaire de la blockchain résultant de la diffusion quasi simultanée de plusieurs blocs par différents mineurs à une même hauteur.

> ► *Pour plus d'informations, voir les définitions de [**EMBRANCHEMENT NATUREL**](./E.md#embranchement-naturel) et de **[FORK](./F.md#fork)**.*

## CHAINSTATE/

Nom technique donné au dossier utilisé pour stocker l'UTXO set sur Bitcoin Core. C'est donc en réalité un synonyme d'« UTXO set ». 

> ► *Pour plus d'informations, voir la définition de [**UTXO SET**](./U.md#utxo-set).*

## CHANGE

Dans le cadre des transactions Bitcoin, fait référence à l'UTXO créé avec les fonds restants après que le paiement effectif a été satisfait. Lorsque l'on utilise en entrées des UTXOs avec une quantité de bitcoins supérieure au montant nécessaire pour le paiement effectif et les frais de transaction, le surplus est un UTXO renvoyé à une adresse interne du portefeuille, appelée adresse de change. Le change représente cet UTXO. Par exemple, si vous souhaitez payer une baguette qui coute `4 000 sats` avec un UTXO de `10 000 sats`, vous allez créer dans votre transaction un change de `6 000 sats` (si l'on néglige les frais de transaction).

![](assets/16.png)

> ► *Même si c'est très peu utilisé, on pourrait également parler de « monnaie » (rendu de monnaie) pour évoquer le change.*

## CHARGE UTILE (PAYLOAD)

Dans le contexte général de l'informatique, une charge utile désigne les données essentielles transportées dans un paquet de données plus large. Par exemple, dans une adresse SegWit V0 sur Bitcoin, la charge utile correspond au hachage de la clé publique, sans les diverses métadonnées (le HRP, le séparateur, la version de SegWit et la somme de contrôle). Par exemple, sur l'adresse `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, nous avons : 
* `bc` : la partie lisible par l'homme (HRP) ;
* `1` : le séparateur ;
* `q` : la version de SegWit. Ici, c'est la version 0 ;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : la charge utile, ici, le hachage de la clé publique ;
* `ys50gj` : la somme de contrôle.

## CHAUMIAN COINJOIN

Amélioration du concept de coinjoin, introduit pour la première fois en 2013 par Gregory Maxwell, qui utilise les signatures aveugles de Chaum pour renforcer l'anonymat des transactions coinjoins. Dans ce protocole, les utilisateurs soumettent des entrées et une adresse de réception cryptographiquement aveuglées à un coordinateur. Cette adresse privée est destinée à recevoir les bitcoins en sortie de coinjoin. Le coordinateur signe ces tokens et les renvoie aux utilisateurs. Les utilisateurs se reconnectent ensuite de manière anonyme au serveur du coordinateur et révèlent ensuite leurs adresses de sortie en clair pour la construction de la transaction. Le coordinateur peut vérifier que toutes ces adresses de réception proviennent bien d'utilisateurs légitimes, puisqu'il a signé leur version aveuglée auparavant. En revanche, il ne peut pas associer une adresse de sortie spécifique à un utilisateur donné en entrée. Il n'y a donc aucun lien entre les entrées et les sorties, même du point de vue du coordinateur. Cette méthode garantit que le coordinateur ne peut ni compromettre l'anonymat des participants, ni voler les bitcoins durant tout le processus de coinjoin.

> ► *Pour plus d'informations, voir la définition de **[COINJOIN](./C.md#coinjoin)**.*

## CHEMIN DE DÉRIVATION

Dans le cadre des portefeuilles déterministes et hiérarchiques (HD), un chemin de dérivation désigne la séquence d'index utilisée pour dériver des clés enfants à partir d'une clé maîtresse. Décrit dans le BIP32, ce chemin permet d'identifier la structure arborescente de dérivation des clés enfants. Un chemin de dérivation est représenté par une série d'index séparés par des barres obliques, et commence toujours par la clé maîtresse (notée `m/`). Par exemple, un chemin typique pourrait être `m/84'/0'/0'/0/0`. Chaque niveau de dérivation est associé à une profondeur spécifique :
* `m /` indique la clé privée maîtresse. Elle est unique pour un portefeuille et ne peut pas avoir de sœurs à la même profondeur. La clé maîtresse est dérivée directement depuis la graine ;
* `m / purpose' /` indique l'objectif de dérivation qui permet d'identifier le standard suivi. Ce champ est décrit dans le BIP43. Par exemple, si le portefeuille respecte le standard BIP84 (SegWit V0), l'index sera alors `84'` ;
* `m / purpose' / coin-type' /` indique le type de cryptomonnaie. Cela permet de bien différencier les branches dédiées à une cryptomonnaie, des branches dédiées à une autre cryptomonnaie sur un portefeuille multi-coin. L'index dédié au bitcoin est le `0'` ;
* `m / purpose' / coin-type' / account' /` indique le numéro de compte. Cette profondeur permet de différencier et d’organiser facilement un portefeuille en différents comptes. Ces comptes sont numérotés à partir de `0'`. Les clés étendues (`xpub`, `xprv`...) se trouvent à ce niveau de profondeur ;
* `m / purpose' / coin-type' / account' / change /` indique la chaîne. Chaque compte tel que défini en profondeur 3 dispose de deux chaînes en profondeur 4 : une chaîne externe et une chaîne interne (également appelée « change »). La chaîne externe dérive des adresses destinées à être communiquées publiquement, c’est-à-dire les adresses que l’on nous propose lorsque l’on clique sur « recevoir » dans notre logiciel de portefeuille. La chaîne interne dérive les adresses destinées à ne pas être échangées publiquement, c’est-à-dire principalement les adresses de change. La chaîne externe est identifiée avec l'index `0` et la chaîne interne est identifiée avec l'index `1`. Vous remarquerez qu'à partir de cette profondeur, on ne réalise plus une dérivation endurcie, mais une dérivation normale (il n'y a pas d'apostrophe). C'est grâce à ce mécanisme que l'on est capable de dériver l'ensemble des clés publiques enfants à partir de leur `xpub` ;
* `m / purpose' / coin-type' / account' / change / address-index` indique simplement le numéro de l’adresse de réception et de sa paire de clés, afin de la différencier de ses sœurs à la même profondeur sur la même branche. Par exemple, la première adresse dérivée dispose de l’index `0`, la deuxième adresse dispose de l’index `1`, etc...

Par exemple, si mon adresse de réception dispose du chemin de dérivation `m / 86' / 0' / 0' / 0 / 5`, on peut en déduire les informations suivantes :
* `86'` indique que nous suivons le standard de dérivation du BIP86 (Taproot / SegWit V1) ;
* `0'` indique que c'est une adresse Bitcoin ;
* `0'` indique que l'on est sur le premier compte du portefeuille ;
* `0` indique que c'est une adresse externe ;
* `5` indique que c'est la sixième adresse externe de ce compte.

![](assets/18.png)

## CHEMIN DE RÉCUPÉRATION

Dans un logiciel de portefeuille utilisant Miniscript, comme Liana par exemple, le ou les chemins de récupération désignent des ensembles de clés qui ne deviennent opérationnels qu'après une période d'inactivité définie dans le script qui bloque les bitcoins (timelock). Les chemins de récupération sont utilisables seulement une fois que les timelocks sont passés, et offrent ainsi une méthode de récupération des fonds lorsque le chemin primaire n'est pas disponible. Prenons l'exemple d'un script qui intègre 2 clés distinctes : la clé A, qui autorise la dépense immédiate des bitcoins, et la clé B, qui permet de les dépenser après un délai défini par un timelock de 52 560 blocs. Dans cet exemple, la clé A provient du chemin primaire, tandis que la clé B provient du chemin de récupération.

> ► *Pour plus d'informations, voir la définition de [**MINISCRIPT**](./M.md#miniscript).*

## CHEMIN PRIMAIRE

Dans un logiciel de portefeuille utilisant Miniscript, comme Liana par exemple, le chemin primaire fait référence à l'ensemble de clés permettant des dépenses immédiates des fonds, sans aucune condition temporelle. Ce chemin est toujours accessible et est utilisé pour la gestion quotidienne des bitcoins, sans nécessiter d'attente (timelock) contrairement aux chemins de récupérations. Prenons l'exemple d'un script qui intègre 2 clés distinctes : la clé A, qui autorise la dépense immédiate des bitcoins, et la clé B, qui permet de les dépenser après un délai défini par un timelock de 52 560 blocs. Dans cet exemple, la clé A provient du chemin primaire, tandis que la clé B provient du chemin de récupération.

> ► *Pour plus d'informations, voir la définition de [**MINISCRIPT**](./M.md#miniscript).*

## CHIFFRER (CHIFFREMENT)

Méthode cryptographique permettant de convertir une information brute en information chiffrée. Une information chiffrée masque la signification originale des données pour empêcher qu'elles ne soient connues. Le chiffrement consiste en une série de transformations effectuées sur l'information originale à l'aide d'une clé. Si ces transformations sont réversibles, le processus d'inversion correspondant est appelé « déchiffrement », et il permet de restaurer les informations à leur état brut.

## CIBLE DE DIFFICULTÉ

Le facteur de difficulté, aussi connu sous le nom de cible de difficulté, est un paramètre utilisé dans le mécanisme de consensus par preuve de travail (Proof of Work, PoW) sur Bitcoin. La cible représente une valeur numérique qui détermine la difficulté pour les mineurs de résoudre un problème cryptographique spécifique, appelé preuve de travail, lors de la création d'un nouveau bloc sur la blockchain. 

La cible de difficulté est un nombre ajustable de 256 bits (64 octets) déterminant une limite d’acceptabilité pour le hachage de l’entête des blocs. Autrement dit, pour qu’un bloc soit valide, le hachage de son entête avec `SHA256d` (double `SHA256`) doit être numériquement inférieur ou égal à la cible de difficulté. La preuve de travail consiste à modifier le champ `nonce` de l'entête du bloc ou de la transaction coinbase jusqu'à ce que le hachage résultant soit inférieur à la valeur cible. 

Cette cible est ajustée tous les 2016 blocs (environ toutes les deux semaines), lors d'un évènement que l'on appelle « ajustement ». Le facteur de difficulté est recalculé en fonction du temps qu'il a fallu pour miner les 2016 blocs précédents. Si le temps total est inférieur à deux semaines, la difficulté augmente en ajustant la cible à la baisse. Si le temps total est supérieur à deux semaines, la difficulté diminue en ajustant la cible à la hausse. L’objectif est de conserver un temps de minage par bloc moyen à 10 minutes. Ce temps entre chaque bloc permet d'éviter les divisions du réseau Bitcoin, résultant en un gaspillage de la puissance de calcul. La cible de difficulté se trouve dans chaque entête de bloc, au sein du champ `nBits`. Puisque ce champ est réduit à 32 bits et que la cible fait en réalité 256 bits, la cible est compactée dans un format scientifique moins précis.

![](assets/34.png)

> ► *La cible de difficulté est parfois également nommée « facteur de difficulté ». Par extension, on peut l'évoquer avec son encodage dans les entêtes de bloc avec le terme « nBits ».*

## CIOH

Sigle de « *Common Input Ownership Heuristic* ». C'est une heuristique utilisée dans le domaine de l'analyse de chaîne sur Bitcoin qui suppose que toutes les entrées d'une transaction appartiennent à une même entité ou à un même utilisateur. Lorsque l'on observe les données publiques d'une transaction Bitcoin, et que l'on y repère plusieurs entrées (inputs), alors, s'il n'y a pas de paternes où d'autres informations qui viendraient infirmer cela, on peut estimer que toutes les entrées de cette transaction appartenaient à une seule et même personne (ou entité). 

Cette heuristique d'analyse a été découverte par Satoshi Nakamoto lui-même, qui en parle dans la partie 10 du White Paper :

> « *Toutefois, la liaison est inévitable avec les transactions multi-entrées, qui révèlent nécessairement que leurs entrées étaient détenues par un même propriétaire. Le risque est que si le propriétaire d'une clef est révélé, les liaisons peuvent révéler d'autres transactions qui ont appartenu au même propriétaire.* » - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Consulté à l'adresse https://bitcoin.org/bitcoin.pdf.

Encore aujourd'hui, le CIOH demeure la principale heuristique employée par les sociétés d'analyse de chaîne, avec la réutilisation d'adresse.

![](assets/13.png)

> ► *En français, on pourrait traduire « CIOH » par « Heuristique de propriété commune des entrée ».*

## CLÉ ÉTENDUE

Suite de caractères qui combine une clé (publique ou privée), son code de chaîne associé et une série de métadonnées. Une clé étendue rassemble en un seul identifiant tous les éléments nécessaires à la dérivation de clés enfants. Elles sont utilisées dans les portefeuilles déterministes et hiérarchiques, et peuvent être de deux types : une clé publique étendue (utilisée pour dériver des clés publiques enfants) ou une clé privée étendue (utilisée pour dériver à la fois des clés privées et des clés publiques enfants). Une clé étendue inclut donc plusieurs données différentes, décrites au sein du BIP32, dans l'ordre :
* Le préfixe : `prv` et `pub` sont des HRP permettant d'indiquer si l'on a affaire à une clé privée étendue (`prv`) ou à une clé publique étendue (`pub`). La première lettre du préfixe permet, elle, de désigner la version de la clé étendue : `x` pour Legacy ou SegWit V1 sur Bitcoin, `t` pour Legacy ou SegWit V1 sur Bitcoin Testnet, `y` pour Nested SegWit sur Bitcoin, `u` pour Nested SegWit sur Bitcoin Testnet, `z` pour SegWit V0 sur Bitcoin, `v` pour SegWit V0 sur Bitcoin Testnet.
* La profondeur, qui indique le nombre de dérivations intervenues depuis la clé maîtresse pour arriver jusqu'à la clé étendue ;
* L'empreinte du parent. Cela représente les 4 premiers octets du `HASH160` de la clé publique parent ;
* L'index. C'est le numéro de la paire parmi ses sœurs dont est issue la clé étendue ;
* Le code de chaîne ;
* Un octet de rembourrage si c'est une clé privée `0x00` ;
* La clé privée ou la clé publique ;
* Une somme de contrôle. Elle représente les 4 premiers octets du `HASH256` de tout le reste de la clé étendue.

Dans la pratique, la clé publique étendue est utilisée pour générer des adresses de réception et pour observer les transactions d'un compte, sans exposer les clés privées associées. Cela peut permettre, par exemple, la création d'un portefeuille dit « watch-only ». Il est toutefois important de noter que la clé publique étendue est une information sensible pour la confidentialité de l'utilisateur, car sa divulgation peut permettre à des tiers de tracer les transactions et de voir le solde du compte associé.

## CLÉ MAITRESSE

Dans le cadre des portefeuilles HD (déterministes et hiérarchiques) la clé privée maîtresse est une clé privée unique dérivée depuis la graine (seed) du portefeuille. Pour obtenir la clé maîtresse, on applique la fonction `HMAC-SHA512` à la graine, en utilisant littéralement les mots « *Bitcoin seed* » comme clé. Le résultat de cette opération donne un output de 512 bits, dont les 256 premiers bits constituent la clé maîtresse, et les 256 bits restants forment le code de chaîne maître. La clé maîtresse et le code de chaîne maître servent de point de départ pour dériver toutes les clés privées et publiques enfants dans l'arborescence du portefeuille HD. La clé privée maîtresse est donc en profondeur 0 de dérivation.

![](assets/19.png)

## CLÉ PRIVÉE

Une clé privée est un élément fondamental de la cryptographie asymétrique. Il s'agit d'un nombre (de 256 bits dans le cadre de Bitcoin) qui représente un secret cryptographique. Cette clé est utilisée pour signer numériquement des transactions et prouver la possession d'une clé publique Bitcoin (et par extension, d'une adresse de réception) en satisfaisant un ScriptPubKey. Les clés privées permettent donc de dépenser des bitcoins en débloquant les UTXO associés à la clé publique correspondante. Les clés privées doivent être conservées strictement confidentielles, car leur divulgation pourrait permettre à des tiers malveillants de prendre le contrôle des fonds associés. 

Dans le système Bitcoin, la clé privée est liée à une clé publique par le biais d'un algorithme de signature numérique à courbes elliptiques (ECDSA ou Schnorr). La clé publique est dérivée de la clé privée, mais l'inverse est pratiquement impossible à réaliser en raison de la difficulté computationnelle inhérente à la résolution du problème mathématique sous-jacent (problème du logarithme discret). La clé publique est généralement utilisée pour générer une adresse Bitcoin, qui sert à bloquer des bitcoins à l'aide d'un script. En cryptographie, les clés privées sont souvent des nombres aléatoires ou pseudo-aléatoires. Dans le contexte spécifique des portefeuilles déterministes et hiérarchiques Bitcoin, les clés privées sont dérivées de manière déterministe depuis la graine (seed). Les clés privées sont fréquemment confondues avec la graine (seed) ou avec la phrase de récupération (mnémonique). Pourtant, ces éléments sont bien différents.

> ► *En anglais, une clé privée se dit « private key ». Ce terme est parfois abrégé avec « privkey », ou « PV ».*

## CLÉ PUBLIQUE

La clé publique est un élément utilisé dans la cryptographie asymétrique. Elle est générée à partir d'une clé privée en utilisant une fonction mathématique irréversible. Sur Bitcoin, les clés publiques sont dérivées depuis leur clé privée associée grâce aux algorithmes de signature numérique à courbes elliptiques ECDSA ou Schnorr. La clé publique, contrairement à la clé privée, peut être partagée librement sans compromettre la sécurité des fonds. Dans le cadre du protocole Bitcoin, la clé publique sert de base pour créer une adresse Bitcoin, qui est ensuite utilisée pour créer des conditions de dépense sur un UTXO à l'aide d'un ScriptPubKey. Les clés publiques sont fréquemment confondues avec la clé maîtresse ou avec les clés étendues (xpub...). Pourtant, ces éléments sont bien différents.

> ► *En anglais, une clé publique se dit « public key ». Ce terme est parfois abrégé avec « pubkey », ou « PK ».*

## CLÉ PUBLIQUE COMPRESSÉE

Une clé publique est utilisée dans les scripts (soit directement sous la forme d'une clé publique, soit sous la forme d'une adresse) pour recevoir et sécuriser des bitcoins. Une clé publique brute est représentée par un point sur une courbe elliptique, composé de deux coordonnées (`x, y`) chacune de 256 bits. En format brut, une clé publique mesure donc 512 bits, sans compter l'octet supplémentaire pour identifier le format. Une clé publique compressée, en revanche, est une forme plus compacte de représentation d'une clé publique. Elle utilise seulement la coordonnée `x` et un préfixe (`02` ou `03`) qui indique la parité de la coordonnée `y` (pair ou impair). 

Si l'on simplifie cela au corps des réels, la courbe elliptique étant symétrique par rapport à l’axe des abscisses, pour tout point $P$ (`x, y`) sur la courbe, il existe un point $P'$ (`x, -y`) qui sera également sur cette même courbe. Cela signifie qu'à chaque `x` correspondent seulement deux valeurs possibles de `y`, positive et négative. Par exemple, pour une abscisse `x` donnée, il y aurait deux points $P1$ et $P2$ sur la courbe elliptique, qui partagent la même abscisse, mais avec des ordonnées opposées :

![](assets/29.png)
Pour choisir entre les deux points potentiels sur la courbe, on ajoute à `x` un préfixe spécifiant quel `y` choisir. Cette méthode permet de réduire la taille d'une clé publique de 520 bits à seulement 264 bits (8 bits de préfixe + 256 bits pour `x`). Cette représentation est connue sous le nom de forme compressée de la clé publique.

Cependant, dans le cadre de la cryptographie sur les courbes elliptiques, nous utilisons non pas les réels, mais un corps fini d'ordre `p` (un nombre premier). Dans ce contexte, le « signe » de `y` est déterminé par sa parité, c'est-à-dire si `y` est pair ou impair. Le préfixe `0x02` indique alors un `y` pair, tandis que `0x03` indique un `y` impair.

Considérons l'exemple suivant d'une clé publique brute (un point sur la courbe elliptique) en hexadécimal :
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

On peut isoler le préfixe, `x`, et `y` :
```plaintext
Préfixe = 04
x = 678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
y = 49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Pour déterminer la parité de `y`, on examine le dernier caractère hexadécimal de `y` :
```plaintext
Base 16 (hexadécimal) : f
Base 10 (décimal) : 15
y est impair
```

Le préfixe pour la clé publique compressée sera `03`. La clé publique compressée en hexadécimal devient :
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

## CLI

Acronyme de « Command Line Interface », ou « interface en ligne de commande » en français. C'est une méthode d'interaction avec des logiciels qui repose sur la saisie de commandes textuelles dans un terminal ou une console. La CLI se différencie de la GUI (interface graphique utilisateur) qui dispose de méthodes d'interactions de pointage (avec la souris) et d'éléments visuels interactifs.

## C-LIGHTNING (CLN)

Ancien nom de l'implémentation Core-Lightning. 

> ► *Pour plus d'informations, voir la définition de [**CORE-LIGHTNING**](./C.md#core-lightning-cln).*

## CLONE

Dans le cadre de Git, consiste à créer une copie locale d'un dépôt distant. Cette opération télécharge l'ensemble du dépôt, y compris toutes les branches et l'historique des commits. En tant qu'utilisateur de Bitcoin, il est possible d'avoir à utiliser cette commande lorsque l'on télécharge un logiciel.

## CLUSTER

Dans le cadre de l'analyse de chaîne, un cluster est un ensemble d'adresses de réception qui sont associées à une même entité par un analyste. En utilisant diverses heuristiques, il est possible de détecter des activités on-chain qui semblent émaner d'une unique personne ou organisation. Ce regroupement d'activités forme ce que l'on appelle un cluster. L'objectif de l'analyse de chaîne est souvent d'identifier un point d'entrée dans ce cluster, permettant ainsi de lier toutes ces activités à une forme d'identité dans le monde réel.

## CODE DE CHAINE

Dans le contexte de la dérivation hiérarchique et déterministe (HD) des portefeuilles Bitcoin, le code de chaîne est une valeur de sel cryptographique de 256 bits utilisée pour générer des clés enfants à partir d'une clé parent, selon le standard BIP32. Le code de chaîne est utilisé en combinaison avec la clé parent et l’index de l’enfant pour générer de manière déterministe une nouvelle paire de clés (clé privée et clé publique) sans révéler la clé parent ou les autres clés enfants dérivées. 

Il existe donc un code de chaîne unique pour chaque paire de clés. Le code de chaîne est obtenu soit en hachant la graine du portefeuille, et en prenant la moitié des bits à droite. Dans ce cas, on parle d'un code de chaîne maître, associé à la clé privée maîtresse. Ou bien, il peut être obtenu en hachant une clé parent avec son code de chaîne parent et un index, puis en conservant les bits de droite. On parle alors de code de chaîne enfant. 

Il est impossible de dériver des clés sans avoir la connaissance du code de chaîne associé à chaque paire parent. Il permet d'introduire des données pseudo-aléatoires dans le processus de dérivation pour garantir que la génération des clés cryptographiques reste imprévisible pour les attaquants tout en étant déterministe pour le détenteur du portefeuille.

> ► *En anglais, un code de chaîne se dit « chain code », et un code de chaîne maître se dit « master chain code ».*

## CODE DE CHAINE MAITRE

Désigne le code de chaîne associé à la clé maîtresse du portefeuille, à la base de l'arbre de dérivation de toutes les clés.

> ► *Pour plus d'informations, voir la définition de **[CODE DE CHAINE](./C.md#code-de-chaine)**.*

## CODE DE PAIMENT RÉUTILISABLE

Dans le BIP47, un code de paiement réutilisable est un identifiant statique généré à partir d'un portefeuille Bitcoin permettant d'engager une transaction de notification et de dériver des adresses uniques. Cela permet de ne pas faire de réutilisation d'adresses, qui mènent à une perte de la confidentialité, sans pour autant devoir dériver et transmettre manuellement de nouvelles adresses vierges à chaque paiement. Dans le BIP47, les codes de paiement réutilisables sont construits de la manière suivante :
* L'octet 0 correspond à la version ;
* L'octet 1 est un champ de bits permettant d'ajouter des informations en cas d'utilisation spécifique ;
* L'octet 2 permet d'indiquer la parité du `y` de la clé publique ;
* De l'octet 3 à l'octet 34, on retrouvera la valeur `x` de la clé publique ;
* De l'octet 35 à l'octet 66, il y a le code de chaîne associé à la clé publique ;
* De l'octet 67 à l'octet 79, il y a du rembourrage de zéros.

On ajoute généralement un HRP au départ du code de paiement et une somme de contrôle à la fin, puis on l'encode en base58. La construction d'un code de paiement est donc assez proche de celle d'une clé étendue. Voici mon propre code de paiement BIP47 en base58 par exemple :

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

Dans l'implémentation PayNym du BIP47, les codes de paiement peuvent également être exprimés sous la forme d'identifiants associés à l'image d'un robot. Voici le mien par exemple : 

```text
+throbbingpond8B1
```

L'utilisation de codes de paiements avec l'implémentation PayNym est actuellement disponible sur Sparrow Wallet sur PC et sur Samourai Wallet sur mobile.

## COINBASE (TRANSACTION)

Type spécifique de transaction Bitcoin, unique pour chaque bloc et toujours la première de celui-ci. Elle permet au mineur ayant trouvé une preuve de travail valide de recevoir sa récompense de bloc. Cette récompense se compose de deux éléments : 
* La subvention de bloc, qui génère de nouveaux BTC conformément au calendrier d'émission défini par les règles de consensus ;
* Les frais de transaction, qui correspondent à la différence entre le total des entrées et des sorties de toutes les transactions incluses dans le bloc. 

La particularité de la transaction Coinbase est qu'elle est la seule à ne pas requérir d'entrée (input), ce qui signifie qu'elle crée des bitcoins ex nihilo. Elle inclut également parfois des informations de gestion choisies par le mineur ou la pool de minage, telles que des messages ou des données sur la version du logiciel utilisé. Les bitcoins générés par une transaction Coinbase sont soumis à une période de maturité de 100 blocs pendant laquelle ils ne peuvent pas être dépensés par le mineur.

> ► *Il n'existe aucune traduction de « Coinbase » en français. Il est donc admis d'utiliser directement ce terme. Pour plus d'informations, voir la définition de [**PÉRIODE DE MATURITÉ**](./P.md#période-de-maturité).*

## COIN CONTROL

Fonctionnalité présente dans certains logiciels de portefeuille Bitcoin, qui donne aux utilisateurs la capacité de sélectionner manuellement les UTXOs spécifiques à utiliser en tant qu'entrées pour effectuer une transaction. En d'autres termes, le coin control offre la possibilité de choisir précisément quels morceaux de bitcoins seront dépensés. Cette fonctionnalité est similaire à l'action de choisir une pièce spécifique de votre porte-monnaie pour payer votre baguette. 

Le coin control est particulièrement utile pour gérer ses frais de transaction et pour améliorer sa confidentialité. En effet, en sélectionnant spécifiquement les UTXOs à consommer, les utilisateurs peuvent éviter de fusionner des UTXOs issus de sources différentes, ce qui pourrait révéler des informations sur l'ensemble de leurs fonds (CIOH). Cette fonctionnalité va souvent de pair avec la possibilité d'étiqueter les sorties de transaction.

## COINJOIN

Le coinjoin est une technique permettant de casser le traçage des bitcoins. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction coinjoin. Les transactions coinjoin permettent d'améliorer la protection de la vie privée des utilisateurs de Bitcoin en rendant l'analyse des transactions plus difficile pour les observateurs extérieurs. Cette structure permet la combinaison de plusieurs transactions indépendantes en une seule transaction, rendant difficile la détermination des liens entre les adresses d'entrée et de sortie. Le fonctionnement général du coinjoin est le suivant : différents utilisateurs souhaitant mixer déposent un montant en input d'une transaction. Ces inputs ressortiront en différents outputs de même montant. À la sortie de la transaction, il est donc impossible de déterminer quel output appartient à quel utilisateur. Il n'y a techniquement aucun lien entre les entrées et les sorties de la transaction coinjoin. Le lien entre chaque utilisateur et chaque UTXO est cassé, de la même manière que l'historique de chaque pièce.

![](assets/4.png)

Pour permettre le coinjoin sans qu'aucun utilisateur ne perde la main sur ses fonds à aucun moment, la transaction est d'abord construite par un coordinateur puis transmise à chaque utilisateur. Chacun d'eux signe alors la transaction de son côté en vérifiant qu'elle lui convient, puis toutes les signatures sont ajoutées à la transaction. Si un utilisateur ou le coordinateur tente de voler les fonds des autres en modifiant les outputs de la transaction coinjoin, alors les signatures seront invalides et la transaction sera refusée par les nœuds. Ce protocole spécifique avec un coordinateur central s'appelle « *Chaumian coinjoin* ».

Ce mécanisme augmente la confidentialité des transactions sans nécessiter de modifications du protocole Bitcoin. Des implémentations spécifiques de coinjoin, telles que Whirlpool, JoinMarket ou Wabisabi, proposent des solutions pour faciliter le processus de coordination entre les participants et renforcer l'efficacité de la transaction coinjoin. Voici une transaction coinjoin par exemple : 

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

> ► *Le terme de « coinjoin » ne dispose pas de traduction française. Certains bitcoiners utilisent également les termes de « mix », de « mixing » ou encore de « mixage » pour évoquer la transaction coinjoin. Le mixage est plutôt le processus utilisé au cœur du coinjoin. Aussi, il ne faut pas confondre le mixage par coinjoins et le mixage par un acteur central qui prend possession des bitcoins durant le processus. Cela n'a rien à voir avec le coinjoin où l'utilisateur ne perd à aucun moment la main sur ses bitcoins durant le processus. Pour plus d'informations, voir la définition de **[CHAUMIAN COINJOIN](./C.md#chaumian-coinjoin)**.*

## COINJUMBLE

Logiciel développé par Chris Belcher et lancée en août 2014 conçu pour faciliter l'utilisation de coinjoins avec une GUI. À la différence d'autres implémentations de coinjoins de l'époque nécessitant que les participants souhaitent effectuer un coinjoin simultanément, CoinJumble permettait de partager les parties de transaction de manière asynchrone. Les utilisateurs pouvaient échanger via des canaux de communications externes pour partager les parties de transaction encodées. Aujourd'hui, CoinJumble n'est plus utilisé.

## COINMUX

Implémentation de coinjoin développée en 2014. Coinmux est un protocole de mixage de bitcoins qui repose sur la confiance réciproque entre les participants, sans nécessiter l'intervention d'un acteur central. Le logiciel regroupe les bitcoins de plusieurs utilisateurs dans une transaction unique, où chaque sortie dispose de montants identiques, ce qui permet de casser les liens entre les inputs et les outputs. Le protocole de Coinmux assure que les utilisateurs conservent le contrôle de leurs fonds durant tout le processus, en ne faisant signer les transactions que lorsque les entrées et les sorties correspondent exactement à ce qui a été convenu. Aujourd'hui, ce protocole n'est plus utilisé.

> ► *Pour plus d'informations, voir la définition de [**COINJOIN**](./C.md#coinjoin).*

## COINS/

Nom de l'ancien dossier utilisé dans Bitcoin Core pour stocker l'UTXO set, remplacé par le fichier `chainstate/` dans la version 0.8.0.

> ► *Pour plus d'informations, voir la définition de [**UTXO SET**](./U.md#utxo-set).*

## COINSHUFFLE

Protocole de mixage de bitcoins proposé en 2014 par Tim Ruffing, Pedro Moreno-Sanchez, and Aniket Kate, inspiré de l'idée du coinjoin de Gregory Maxwell. Coinshuffle permet de couper l'historique de pièces sans nécessiter de tiers de confiance. Le protocole assure que même l'intermédiaire ne peut pas relier le payeur au bénéficiaire. Ce concept n'a jamais été largement adopté, les techniques de confidentialité telles que le Chaumian coinjoin lui étant préférées.

> ► *Pour plus d'informations, voir la définition de [**COINJOIN**](./C.md#coinjoin).*

## COLD WALLET

Synonyme de « hardware wallet ». Un hardware wallet, ou portefeuille matériel, est un dispositif électronique dédié à la sécurisation et à la gestion des clés privées d'un portefeuille Bitcoin. Ces périphériques sont conçus pour procurer une sécurité renforcée par rapport aux portefeuilles logiciels qui résident sur des machines polyvalentes et directement connectées à internet. Les hardwares wallets stockent la phrase mnémonique hors ligne, sur un matériel qui dispose d'une infime surface d'attaque, ce qui l'isole des environnements potentiellement vulnérables. Lorsqu'une transaction est effectuée, le portefeuille matériel signe la transaction à l'intérieur du dispositif lui-même, sans exposer la clé privée à l'extérieur. Une fois la transaction signée, elle est transmise au réseau Bitcoin pour être confirmée et incluse dans la blockchain. Parmi les modèles de hardwares wallets les plus populaires, on peut citer : Ledger, Trezor, Coldcard, Passport, BitBox, Satochip, Jade ou encore SeedSigner (liste non exhaustive).

> ► *Le hardware wallet peut être exprimé de différentes manières en français. Certains parlent de « portefeuille matériel » ou bien de « portefeuille froid ». D'autres préfèrent que l'on emploie le terme de « périphérique de signature », ou « signing device » en anglais, afin d'éviter de faire penser que les bitcoins se trouvent physiquement dans le portefeuille.*

## COLORED COINS

Méthode proposée en 2012 par Yoni Assia, Vitalik Buterin et Meni Rosenfeld permettant de représenter et gérer des actifs non natifs sur la blockchain Bitcoin. L'idée était d'attacher des métadonnées à des transactions spécifiques, afin de colorer des bitcoins pour indiquer leur association avec des actifs physiques. La première implémentation fonctionnelle, le protocole Open Assets, a été développée par Flavien Charlon en 2013. Ce protocole permettait de marquer des bitcoins en utilisant des `OP_RETURN`.

## COMMERÇANT

Toute personne physique ou morale qui accepte d'échanger un bien ou un service contre des bitcoins. Ce sont ces commerçants qui confèrent son utilité à la monnaie bitcoin. Plus une monnaie est acceptée par un large éventail de commerçants, plus elle devient utile pour les individus. Puisque les commerçants ont la capacité de déterminer l’utilité d’une monnaie en acceptant de l’échanger contre des biens et des services, dans le cas de Bitcoin, ils ont également un poids considérable dans le choix des règles de consensus. Chacun dispose d'un certain pouvoir proportionnel à l'activité économique qu'il est en capacité d'apporter à un fork. Parmi les commerçants, il y a évidemment les commerces, mais aussi les plateformes d'échange, les mineurs et les utilisateurs.

## COMMIT

Dans le cadre de Git, représente une capture instantanée des modifications apportées à l'ensemble de fichiers d'un dépôt. Chaque commit est identifié par un hachage unique et inclut un message descriptif, l'identité de l'auteur et la date. Il permet de suivre l'évolution du projet et de revenir à des états antérieurs si nécessaire.

## COMPACT BLOCK RELAY

Protocole introduit dans Bitcoin Core en 2016 via le BIP152 qui propose une méthode d'économie de bande passante pour les nœuds du réseau. Compact Block Relay permet de communiquer les informations des blocs de manière compacte, en se basant sur l'hypothèse que les nœuds ont déjà une grande partie des transactions d'un bloc récent dans leur mempool. Plutôt que de transmettre chaque transaction intégralement, ce qui constituerait un doublon, Compact Block Relay propose d'envoyer uniquement de courts identifiants pour les transactions déjà connues des pairs, accompagnés de quelques transactions sélectionnées (notamment la transaction coinbase et celles que le nœud est susceptible de ne pas connaître). Le nœud peut ensuite demander à ses pairs les éventuelles transactions manquantes. Compact Block Relay permet ainsi de diminuer la quantité de données échangées lors de la propagation des blocs, ce qui réduit ainsi les pics de bande passante et améliore l'efficacité globale du réseau.

## COMPATIBILITÉ RÉTROSPECTIVE

Fait référence à la capacité d'une mise à jour des règles du protocole à maintenir la compatibilité avec les versions antérieures. Cela signifie que les modifications sont conçues de manière à ce que les anciens nœuds (les nœuds qui exécutent des versions antérieures au changement de règles) puissent toujours interagir avec le réseau et suivre la chaîne avec le plus de travail accumulé. Il faut donc que les anciens nœuds ne rejettent ni les nouveaux blocs, ni les nouvelles transactions. La compatibilité rétrospective permet de réduire fortement la probabilité qu'une mise à jour fragmente le réseau, évitant ainsi la division des nœuds en sous-groupes sur des chaînes différentes. Pour assurer une compatibilité avec les versions antérieures du protocole, une mise à jour doit rendre les règles existantes plus strictes ou en introduire de nouvelles. C'est ce principe qui définit un « soft fork ». À l'inverse, si une mise à jour assouplit les règles existantes ou en élimine certaines, alors elle ne sera pas rétrocompatible. Ce sera donc un « hard fork ».

## COMPTE

Dans les portefeuilles HD (déterministes hiérarchiques), un compte représente une couche de dérivation à la profondeur 3 selon le BIP32. Chaque compte est numéroté séquentiellement à partir de `/0'/` (dérivation renforcée, donc en réalité `/2^31/` ou `/2 147 483 648/`). C'est à cette profondeur de dérivation que se trouvent les fameuses `xpub`. De nos jours, on utilise généralement un seul compte au sein d'un portefeuille HD. Mais initialement, ils avaient été imaginés pour pouvoir ségréguer diverses catégories d'utilisation au sein d'un même portefeuille. Par exemple, si l'on prend un chemin de dérivation standard pour une adresse de réception Taproot externe (`P2TR`) : `m/86'/0'/0'/0/0`, l'index du compte est le second `/0'/`.

![](assets/17.png)

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## CONCATÉNATION

Dans le contexte de la cryptographie et des systèmes informatiques, désigne le processus d'assemblage de deux opérandes, en les mettant bout à bout, formant ainsi une nouvelle chaîne de caractères ou de données. Cette opération se note généralement avec un symbole de deux barres verticales $\Vert$, ou avec le symbole $\circ$. Par exemple, la concaténation de $45$ avec $87$ sera égale à $4587$. Nous noterons : $45 \Vert 87 = 4587$. On a mis bout à bout les deux opérandes.

## CONDENSAT (HASH)

En cryptographie, désigne le résultat (ou l'output) produit par l'application d'une fonction de hachage cryptographique à un ensemble de données. Le condensat est une chaîne de caractères de taille fixe, généralement représentée sous forme d'une série de chiffres et de lettres en notation hexadécimale (base 16). Ce résultat a la particularité d'être presque unique et spécifique aux données d'entrée, de sorte qu'un changement minime dans l'entrée produira un condensat complètement différent. Les fonctions de hachage cryptographiques sont conçues pour être unidirectionnelles et résistantes aux collisions, rendant très difficile de retrouver les données initiales à partir du condensat ou de trouver deux entrées distinctes produisant le même condensat.

> ► *Pour plus d'informations, voir la définition de [**FONCTION DE HACHAGE**](./F.md#fonction-de-hachage).*

## CONFIRMATION

Correspond au nombre de blocs pour lesquels une transaction bénéficie de leur sécurité. Lorsque l'on diffuse une transaction au réseau Bitcoin, celle-ci est d'abord en attente dans les mempools des nœuds. Elle est ensuite incluse dans un bloc valide par un mineur. À ce stade, la transaction vient d'être ajoutée à la blockchain, elle bénéficie donc d'une première confirmation. Lorsqu'un nouveau bloc sera trouvé par-dessus le bloc où se trouve la transaction en question, elle bénéficiera d'une seconde confirmation, et ainsi de suite. Chaque nouveau bloc miné par dessus le bloc contenant la transaction constitue une nouvelle confirmation. Grâce au comptage du nombre de confirmations pour une transaction, on peut estimer le risque qu'elle puisse être finalement annulée à cause d'une réorganisation. Le nombre de confirmations nous permet de juger du niveau d'immuabilité d'une transaction sur la blockchain.

## CONSENSUS

Mécanisme par lequel tous les nœuds du réseau Bitcoin parviennent à s'accorder sur l'état partagé de la blockchain. Le consensus permet que tous les utilisateurs s'alignent sur un même historique des transactions Bitcoin, afin notamment d'éviter la double dépense. Le mécanisme de consensus de Bitcoin est parfois appelé « Consensus de Nakamoto ». Il s'appuie sur la preuve de travail et spécifie que tous les nœuds du réseau acceptent la chaîne disposant de la plus grande quantité de travail accumulé. 

> ► *Par extension, certaines personnes appellent par « Consensus » les règles tacites du protocole Bitcoin.*

## CONSOLIDATION

Transaction spécifique dans laquelle plusieurs petits UTXOs sont fusionnés en entrée pour former un seul et plus gros UTXO en sortie. Cette opération est une transaction effectuée vers son propre portefeuille. L'objectif de la consolidation est de tirer profit des périodes où les frais sur le réseau Bitcoin sont bas pour fusionner plusieurs petits UTXOs en un seul plus grand en valeur. Ainsi, on anticipe les dépenses obligatoires en cas de hausse des frais, permettant d'économiser sur les frais de transaction futurs. 

En effet, les transactions comportant de nombreuses entrées sont plus lourdes et, par conséquent, plus coûteuses. Outre l'économie réalisable sur les frais de transaction, la consolidation est aussi une forme de planification à long terme. Si votre portefeuille contient de très petits UTXOs, ceux-ci peuvent devenir inutilisables si le réseau Bitcoin entre dans une période prolongée de frais élevés. Par exemple, si vous devez dépenser un UTXO de 10 000 sats mais que les frais de minage minimums s'élèvent à 15 000 sats, la dépense excéderait la valeur de l'UTXO lui-même. Ces petits UTXOs deviennent alors économiquement non rationnels à utiliser et restent inutilisables tant que les frais ne baissent pas. Ces UTXOs sont communément appelés « dust » (poussière). En consolidant régulièrement vos petits UTXOs, vous réduisez ce risque associé aux augmentations de frais.

Cependant, il est important de noter que les transactions de consolidation sont reconnaissables lors d'une analyse de chaîne. Une telle transaction indique une CIOH (*Common Input Ownership Heuristic*), c'est-à-dire que les entrées de la transaction de consolidation sont possédées par une seule entité. Cela peut avoir des implications en termes de confidentialité pour l'utilisateur.

![](assets/7.png)


## CONTRAT INTELLIGENT

Programme qui s'exécute automatiquement lorsque certaines conditions prédéfinies sont remplies. Un contrat intelligent est donc un ensemble de clauses entre plusieurs parties qui peuvent se réaliser sans nécessiter l'intervention d'un tiers de confiance. Ces contrats déclenchent généralement des actions spécifiques comme un transfert de bitcoins.

> ► *En anglais, on parle de « Smart Contract ». En français, on parle également parfois de « contrat autonome ».*

## CONTRIBUTEUR (CORE)

Un contributeur dans le contexte de Bitcoin Core (l'implémentation majoritaire de nœuds sur le réseau Bitcoin) est une personne qui participe activement au développement du logiciel en écrivant du code, en examinant et en testant les modifications proposées par d'autres. Contrairement aux mainteneurs, les contributeurs n'ont pas le pouvoir de fusionner les modifications dans le code principal ; leur rôle est plutôt de soumettre des pull requests (PR) et de participer à la discussion et à la validation de ces propositions. Tout individu intéressé peut devenir contributeur sans nécessité d'une nomination ou d'une approbation formelle, ce qui diffère des mainteneurs qui sont chargés de responsabilités administratives et de décision plus élevées dans le projet.

## COOKIE (.COOKIE)

Fichier utilisé pour l'authentification RPC (*Remote Procedure Call*) dans Bitcoin Core. Lorsque bitcoind démarre, il génère un cookie d'authentification unique et le stocke dans ce fichier. Les clients ou les scripts qui souhaitent interagir avec bitcoind via l'interface RPC peuvent utiliser ce cookie pour s'authentifier de manière sécurisée. Ce mécanisme permet une communication sûre entre le bitcoind et les applications externes (comme les logiciels de portefeuille par exemple), sans nécessiter une gestion manuelle des noms d'utilisateur et des mots de passe. Le fichier `.cookie` est régénéré à chaque redémarrage de bitcoind et supprimé à l'arrêt.

## CORE-LIGHTNING (CLN)

Implémentation majeure du protocole Lightning Network écrite en langage C et Rust. Développée par Blockstream, Core-Lightning est conçue pour être légère et performante. Elle se distingue par son architecture modulaire, permettant aux développeurs d'ajouter facilement des fonctionnalités personnalisées. Cette implémentation a été renommée en 2022. Son nom original était auparavant « C-Lightning ».

## COURBE ELLIPTIQUE

Dans le contexte de la cryptographie, une courbe elliptique est une courbe algébrique définie par une équation de la forme $y^2 = x^3 + ax + b$. Ces courbes sont utilisées dans la cryptographie à courbes elliptiques (ECC), qui est une méthode de cryptographie à clé publique permettant de créer des algorithmes de chiffrement, de signature numérique et d'échange de clés. Dans le contexte de Bitcoin, l'algorithme ECDSA (*Elliptic Curve Digital Signature Algorithm*) ou le protocole de Schnorr sont utilisés avec la courbe `secp256k1`. Cette courbe a été choisie pour ses propriétés de performance et de sécurité. Ces algorithmes sont utilisés pour générer des clés publiques à partir de clés privées, ainsi que pour signer des transactions, et donc débloquer des bitcoins.

## COVENANT

Mécanisme qui permet d'imposer des conditions spécifiques sur la manière dont une pièce donnée peut être dépensée, y compris dans des transactions futures. Au-delà des conditions usuellement autorisées par le langage script sur un UTXO, le covenant force des contraintes supplémentaires sur la manière de dépenser cette pièce Bitcoin dans des transactions ultérieures. Techniquement, l'instauration d'un covenant intervient lorsque le `scriptPubKey` d'un UTXO définit des restrictions sur le `scriptPubKey` des sorties d'une transaction qui dépense ledit UTXO. En élargissant la portée de script, les covenants permettraient de nombreuses évolutions sur Bitcoin comme l'ancrage bilatéral des drivechains, la mise en place de vaults ou encore l'amélioration des systèmes de surcouche comme Lightning. On différencie les propositions de covenants en fonction de trois critères :
* Leur portée ;
* Leur implémentation ;
* Leur récursivité.

Il existe de très nombreuses propositions qui permettraient l'utilisation de covenants sur Bitcoin. Les plus avancées dans le processus d'implémentation sont : `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) et `OP_VAULT`. Parmi les autres propositions, il y a : `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, etc.

Pour bien comprendre le concept de covenant, je vous propose une analogie : imaginez un coffre-fort contenant 500 € en petites coupures. Si vous parvenez à déverrouiller ce coffre avec la clé adéquate, alors vous êtes libre d'utiliser cet argent comme bon vous semble. Ça, c’est la situation normale de Bitcoin. Maintenant, imaginez que ce même coffre-fort ne contient pas 500 € en billets de banque, mais plutôt des tickets restaurants d'une valeur équivalente. Si vous réussissez à ouvrir ce coffre, vous pouvez disposer de cette somme. Cependant, votre liberté de dépense est restreinte, car vous ne pouvez utiliser ces tickets pour payer que dans certains restaurants. Ainsi, il y a une première condition pour dépenser cet argent, qui est de parvenir à ouvrir le coffre avec la clé appropriée. Mais il y a aussi une condition supplémentaire quant à l'usage futur de cette somme : elle doit être dépensée exclusivement dans des restaurants partenaires, et non pas en toute liberté. Ce système de contraintes sur les transactions futures, c’est ce que l’on appelle un covenant.

> ► *En français, il n'existe aucun terme pour capturer précisément la signification du mot « covenant ». On pourrait parler de « clause », de « pacte » ou d' « engagement », mais cela ne correspondrait pas exactement au terme « covenant ». Ce dernier est d'ailleurs emprunté d'une terminologie juridique qui permet de décrire une clause contractuelle imposant des obligations persistantes sur un bien.*

## COVERT ASICBOOST

Version secrète d'AsicBoost. AsicBoost est une méthode d'optimisation algorithmique pour le minage de Bitcoin. Dans sa version Covert, les mineurs manipulent l'arbre de Merkle plutôt que le Nonce, ce qui réduit ainsi les calculs nécessaires pour chaque hachage SHA256 en conservant certaines données inchangées entre les tentatives de hachage. Contrairement à la version Overt d'AsicBoost, la version Covert dissimule l'utilisation d'AsicBoost durant le processus de minage. Cependant, depuis l'introduction de SegWit et son second arbre de Merkle, cette méthode n'est plus efficace, car le nombre de calculs requis pour son utilisation est devenu trop important par rapport à un processus de minage classique.

> ► *Pour plus d'informations, voir les définitions de **[ASICBOOST](./A.md#asicboost)** et **[OVERT ASICBOOST](./O.md#overt-asicboost)**.*

## CPFP (CHILD PAY FOR PARENT)

Mécanisme transactionnel visant à accélérer la confirmation d'une transaction Bitcoin, tout comme le fait Replace-by-Fee (RBF), mais du côté du destinataire. Lorsqu'une transaction avec des frais trop faibles par rapport au marché reste bloquée dans les mempools des nœuds et ne se confirme pas assez rapidement, le destinataire peut faire une nouvelle transaction, en dépensant les bitcoins reçus dans la transaction bloquée, bien qu'elle ne soit pas encore confirmée. Cette seconde transaction nécessite forcément que la première soit minée pour être confirmée. Les mineurs sont donc obligés d'inclure les deux transactions ensemble. La seconde va allouer beaucoup plus de frais de transaction que la première, de telle sorte que la moyenne de frais incite les mineurs à inclure les deux transactions. La transaction enfant (la seconde) paie pour la transaction parent qui est bloquée (la première). C'est pour cela que l'on parle d'un « CPFP ». Ainsi, CPFP permet au destinataire d'obtenir plus rapidement ses fonds malgré les faibles frais initiaux engagés par l'expéditeur.

## CPPSRB

Sigle de « *Capped Pay Per Share Recent Backpay* ». C'est une méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage. Dans ce système, la pool paie autant de shares qu'elle le peut à chaque fois qu'un bloc est trouvé, en donnant la priorité aux shares les plus récentes. Cette méthode permet de garantir la stabilité financière de la pool de minage, tout en offrant une rémunération à la tâche et en incitant les mineurs à rester connectés à la pool pour éviter le pool hopping.

> ► *Pour plus d'informations, voir la définition de **[SHARES](./S.md#shares)**.*

## CPU (CENTRAL PROCESSING UNIT)

Composant principal d'un ordinateur responsable de l'exécution des instructions machines des logiciels. Dans le contexte de Bitcoin, le CPU était initialement utilisé pour le minage par les nœuds avant d'être surpassé par le minage par GPU (cartes graphiques), puis par l'utilisation de puces spécialisées que l'on appelle des « ASIC ».

> ► *En français, on peut parler d'une « unité centrale de calcul » ou bien simplement d'un « processeur ».*

## CRYPTANALYSE

Étude des techniques mathématiques pour tenter de casser les techniques cryptographiques. Cela inclut les processus de recherche d'erreurs ou de faiblesses dans l'implémentation d'une méthode cryptographique ou dans la méthode cryptographique elle-même.

## CRYPTER

Ce terme n'existe pas. On dit « chiffrer ».

## CRYPTO-ACTIF

Terme utilisé dans un contexte juridique et réglementaire pour désigner les divers types de cryptomonnaies, dont le bitcoin.

## CRYPTOGRAPHIE

Discipline qui incarne les principes, les moyens et les méthodes de transformation des informations, notamment avec des techniques mathématiques, afin de masquer leur contenu sémantique, d'empêcher leur utilisation non autorisée, d'assurer leur authenticité ou d'empêcher leur modification non détectée. La cryptographie regroupe l'utilisation de fonctions de hachage, de signatures numériques et d'algorithmes de chiffrement.

## CRYPTOLOGIE

Science mathématique qui traite de la cryptanalyse et de la cryptographie.

## CRYPTOMONNAIE

Qualificatif générique donné à toute forme de monnaie, d'actif, de crédit ou d'unité numérique au sein d'un système informatique dans lequel on utilise de la cryptographie pour les échanges et les transactions entre les utilisateurs.

## C SHARP

Langage de programmation moderne, orienté objet, développé par Microsoft. Il est conçu pour être simple, mais complet.

## CUSTODY

Dans le contexte de Bitcoin, se réfère à la détention et à la gestion des clés privées qui permettent le contrôle de bitcoins. La custody de BTC peut être assurée de deux manières : soit personnellement par l'utilisateur, qui garde lui-même les clés privées nécessaires pour accéder à ses bitcoins (ce que l'on appelle « self-custody »), soit par un tiers, comme une plateforme d'échange, où l'entreprise détient les clés privées et gère les bitcoins au nom de l'utilisateur. Cette seconde option est plus risquée que la self-custody, car cela expose les fonds de l'utilisateur aux risques de piratage, de faillite ou de comportements frauduleux de la part du gestionnaire.

> ► *En français, on utilise généralement le terme anglais de « custody ». On pourrait également le traduire par « garde ».*

## CYPHERPUNK

Communauté informelle et internationale de personnes intéressées par l'utilisation de la cryptographie comme moyen pour assurer les libertés individuelles. Les cypherpunks prônent l'utilisation de la cryptographie pour imposer son droit fondamental de protéger sa vie privée en tant qu'individu, en particulier dans un contexte d'augmentation de la surveillance gouvernementale et de l'exploitation des données par des entités privées. L'histoire des cypherpunks remonte aux années 1980 et 1990, lorsque des groupes de cryptographes, de programmeurs et de libertariens commencent à discuter et à promouvoir l'utilisation de la cryptographie pour protéger l'anonymat et les libertés individuelles. 

Parmi les moments clés de l'histoire des cypherpunks, il y a la fondation, en 1992, de la « Cypherpunks mailing list », une liste de diffusion par courrier électronique qui a servi pour ces discussions. La publication en 1993 du *Cypherpunk's Manifesto* par Eric Hughes a également été un moment important. Ce document décrit les objectifs et les actions des cypherpunks. L'idée d'une monnaie électronique qui ne s'établit pas sur une entité centrale, comme Bitcoin, est enracinée dans la philosophie cypherpunk. La création de Bitcoin est souvent considérée comme une réalisation majeure de cette vision.
