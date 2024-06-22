
## NESTED SEGWIT

Standard de scripts utilisés pour envelopper des scripts SegWit natifs, au sein d'un script P2SH. Les scripts Nested SegWit ont été inventé au lancement de SegWit pour faciliter son adoption. Ils permettent d'utiliser ce nouveau standard, même sur des wallets pas encore compatibles nativement avec SegWit. C'est une sorte de script de transition vers la nouvelle norme. Aujourd'hui, il n'est donc plus très pertinent d'utiliser ce type de scripts SegWit wrappés, puisque la plupart des wallets ont implémenté du SegWit natif.

> *Pour plus d'informations, voir la définition de [**P2SH-P2WPKH**](./P.md#p2sh-p2wpkh).*

## NETWORK-ADJUSTED TIME (NAT)

Estimation du temps universel basée sur les horloges des nœuds du réseau. Chaque nœud calcule son NAT en prenant la médiane des différences de temps entre son horloge locale (UTC) et celles des nœuds avec lesquels il est connecté, puis en additionnant son horloge locale avec la médiane de ces différences, jusqu'à un maximum de 70 minutes. Le network-adjusted time est donc une médiane du temps des nœuds calculée en local par chaque nœud. Ce référentiel est ensuite utilisé pour vérifier la validité des horodatages des blocs. En effet, pour qu'un bloc soit accepté par un nœud, son horodatage doit se situer entre le MTP (temps médian des 11 derniers blocs minés) et le NAT plus 2 heures : `MTP < Horodatage valide < (NAT + 2h)`.

## NEW YORK AGREEMENT (NYA)

Réunion privée qui s'est tenue en 2017, rassemblant plus de 50 entreprises de l'écosystème Bitcoin, à la suite de la conférence Consensus 2017. L'objectif de cette réunion était de finir le débat de longue date sur le passage à l'échelle de Bitcoin en parvenant à un accord. De cette rencontre est née la proposition SegWit2x, s'inspirant de la précédente proposition SegWit2Mb. Elle prévoyait deux modifications majeures du protocole Bitcoin : 
* L'adoption de SegWit avec un seuil d'activation fixé à 80 % de signalisation ;
* Un hard fork destiné à augmenter la taille maximale des blocs de 1 Mo à 2 Mo.

Malgré le signalement positif de plus de 80 % des mineurs, le projet n'a pas su rallier un consensus suffisant, aboutissant à son abandon. Cet événement a été interprété par de nombreux utilisateurs et développeurs comme une tentative d'attaque de Bitcoin.

## NLOCKTIME

Champ intégré dans les transactions qui définit une condition temporelle avant laquelle la transaction ne peut être ajoutée à un bloc valide. Ce paramètre permet de spécifier un temps précis (timestamp Unix) ou un nombre de blocs spécifique comme condition pour que la transaction soit considérée comme valide. C'est donc un timelock absolu (pas relatif). Le `nLockTime` agit sur l'intégralité de la transaction et permet effectivement de vérifier le temps, alors que l'opcode `OP_CHECKLOCKTIMEVERIFY` permet uniquement de comparer la valeur en haut de la pile avec la valeur du `nLockTime`.

> *Pour plus d'informations, voir la définition de [**OP_CHECKLOCKTIMEVERIFY**](./O.md#op_checklocktimeverify-0xb1) et [**TIMELOCK**](./T.md#timelock).*

## NO2X

Nom de la campagne lancée en août 2017 suite au verrouillage du soft fork SegWit dont le but est de convaincre les utilisateurs de ne pas implémenter le doublement de la taille des blocs de 1 Mo à 2 Mo tel que prévu dans la mise à jour SEGWIT2X.

> *Pour plus d'informations, voir la définition de **[BLOCKSIZE WAR](./B.md#blocksize-war)** et [**SEGWIT2X**](./S.md#segwit2x).*

## NOEUD

Dans le réseau Bitcoin, un nœud (ou « node » en anglais) est un ordinateur qui exécute un client du protocole Bitcoin (comme Bitcoin Core par exemple). Il participe au réseau en maintenant une copie de la blockchain, en relayant et en vérifiant les transactions et les nouveaux blocs et, optionnellement, en participant au processus de minage. La somme de tous les nœuds Bitcoin représente le réseau Bitcoin en lui-même. Il existe plusieurs types de nœuds sur Bitcoin, dont les plus notables sont les nœuds complets et les nœuds légers. Les nœuds complets conservent une copie intégrale de la blockchain, vérifient toutes les transactions et les blocs selon les règles de consensus, et participent activement à la diffusion de transactions et de blocs sur le réseau. En revanche, les nœuds légers, ou nœuds SPV (*Simple Payment Verification*), ne conservent qu'une partie de la blockchain et comptent sur les nœuds complets pour obtenir des informations sur les transactions. 

> *Certains différencient également les nœuds dits « élagués » (« pruned node » en anglais). Ce sont des nœuds complets, qui téléchargent et vérifient tous les blocs depuis le bloc Genesis, mais qui ne conserve que les blocs les plus récents en mémoire.*

## NOEUD COMPLET

Un nœud complet, ou « Full Node » en anglais, fait référence à un ordinateur qui exécute un client du protocole Bitcoin, et qui télécharge, vérifie et stocke la totalité de la blockchain, soit l'historique complet des transactions depuis le bloc Genesis. Un nœud complet vérifie de manière autonome toutes les transactions et les blocs en fonction des règles de consensus de Bitcoin. C’est donc ce type de nœud qui procure le plus haut niveau de vérification pour son utilisateur, et qui permet de réduire au maximum le besoin de confiance envers une tierce partie. Le nœud complet nécessite plus de ressources de stockage, de puissance de calcul, de RAM et de bande passante qu'un nœud léger (SPV).

## NOEUD ÉLAGUÉ

Un nœud élagué, en anglais « Pruned Node », est un nœud complet qui exécute un élagage de la blockchain. Cela consiste à supprimer de manière progressive les blocs les plus anciens, après les avoir dûment vérifiés, pour conserver seulement les blocs les plus récents. La limite de conservation est renseignée dans le fichier `bitcoin.conf` via le paramètre `prune=n`, ou `n` est la taille maximale prise par les blocs en mégaoctets (Mo). Si `0` est noté après ce paramètre, alors l’élagage est désactivé, et le nœud conserve la blockchain dans son intégralité. Les nœuds élagués sont parfois considérés comme des types de nœuds différents des nœuds complets. L'utilisation d'un nœud élagué peut s'avérer particulièrement intéressante pour les utilisateurs confrontés à des contraintes en termes de capacité de stockage. Actuellement, un nœud complet doit disposer d’environ 500 Go pour le stockage de la blockchain. Un nœud élagué peut limiter le stockage requis jusqu’à 550 Mo. Bien qu’il utilise moins d’espace disque, un nœud élagué maintient un niveau de vérification et de validation semblable à celui d'un nœud complet. Les nœuds élagués offrent donc plus de confiance à leurs utilisateurs en comparaison avec les nœuds légers (SPV).

## NOEUD LIGHTNING

Ordinateur qui exécute une implémentation du Lightning Network (Eclair, LND, C-Lightning...). Un nœud Lightning est établi sur un nœud Bitcoin, et permet de créer et de gérer des canaux de paiement bidirectionnels entre différents utilisateurs. Les nœuds Lightning sont connectés les uns aux autres ce qui forme un réseau de canaux de paiement. Ces canaux permettent de réaliser un nombre presque illimité de transactions sans avoir besoin de les publier individuellement sur la blockchain Bitcoin.

## NOEUD SPV (NOEUD LÉGER)

Un nœud SPV (*Simple Payment Verification*), parfois nommé « nœud léger », est un client léger d'un nœud Bitcoin qui permet aux utilisateurs de valider les transactions sans avoir à stocker l'intégralité de la blockchain. Au lieu de cela, un nœud SPV stocke seulement les entêtes des blocs, et obtient des informations sur des transactions spécifiques en interrogeant des nœuds complets lorsque nécessaire. Ce principe de vérification est rendu possible par la structure des transactions dans les blocs Bitcoin, qui sont organisées au sein d’un accumulateur cryptographique (Arbre de Merkle). Cette approche est avantageuse pour les appareils avec des ressources limitées, tels que les téléphones portables. Cependant, les nœuds SPV font confiance aux nœuds complets pour la disponibilité des informations, ce qui implique un niveau de confiance supplémentaire et, par conséquent, une moindre sécurité par rapport aux nœuds complets. Les nœuds SPV ne peuvent pas valider les transactions de manière autonome, mais ils peuvent vérifier si une transaction est incluse dans un bloc en consultant les preuves de Merkle.

## NONCE

Dans le contexte de l’informatique, le terme « nonce » désigne un nombre utilisé seulement une seule fois, puis remplacé. Il est souvent aléatoire ou pseudo-aléatoire. On l'utilise dans divers protocoles cryptographiques pour garantir la sécurité du procédé. Par exemple, les signatures ECDSA utilisées au sein du protocole Bitcoin incluent l’utilisation d’un nonce. Cela veut dire que ce nombre doit être nouveau pour chaque signature. Si ce n’est pas le cas, il est possible de calculer la clé privée utilisée en rapprochant deux signatures qui utilisent le même Nonce. On utilise également des nonces dans le processus de minage sur Bitcoin. Les mineurs incrémentent ces valeurs modifiables au sein de leurs blocs candidats. Ils modifient la valeur du nonce dans le but de trouver une empreinte cryptographique inférieure ou égale à la cible de difficulté. Ce processus nécessite une grande puissance de calcul, car il s’agit d’une recherche exhaustive parmi un grand nombre de nonces possibles. Lorsqu'un mineur trouve un nonce qui, lorsqu'il est inclus dans son bloc, produit un condensat répondant aux critères de difficulté, le bloc est diffusé au réseau, et le mineur remporte la récompense.

> *En 2010, des chercheurs ont découvert que la PlayStation 3 de Sony utilisait le même nonce lors de la signature de différents paquets de code. Cette réutilisation du nonce a permis aux attaquants de calculer la clé privée utilisée pour signer le logiciel. Avec la clé privée en main, les attaquants pouvaient créer des signatures valides pour n'importe quel code, ce qui leur permettait d'exécuter des logiciels non autorisés, y compris des jeux piratés ou des systèmes d'exploitation personnalisés, directement sur la PS3.*

## NSEQUENCE

Le champ `nSequence` dans une entrée de transaction Bitcoin est utilisé pour indiquer la manière dont cette entrée est verrouillée dans le temps. À l'origine, il visait à permettre le remplacement dynamique de transactions dans les mempools afin de permettre un système de paiement en surcouche similaire à Lightning. Toutefois, son utilisation a évolué avec l'introduction du timelock relatif via le BIP68. Le champ `nSequence` peut désormais spécifier un délai relatif avant qu'une transaction soit incluse dans un bloc. Ce délai peut être défini en terme de nombre de bloc, ou bien comme un multiple de 512 secondes (c'est-à-dire, du temps réel). Notons que cette nouvelle interprétation du champs `nSequence` est uniquement valide si le champs `nVersion` est supérieur ou égal à `2`. Cette interprétation du champs `nSequence` se fait au niveau des règles de consensus de Bitcoin. Par ailleurs, au niveau des règles de standardisation, ce champ est également utilisé pour le signalement de RBF. Si une transaction inclue un `nSequence` inférieur à `0xfffffffe`, alors elle pourra être remplacée via RBF sur les nœuds qui suivent cette politique.

> *Pour plus d'informations, voir la définition de [**OP_CHECKSEQUENCEVERIFY**](./O.md#op_checksequenceverify-0xb2) et [**TIMELOCK**](./T.md#timelock).*

## NULL DATA

Type de transaction Bitcoin qui permet d'insérer une petite quantité de données arbitraires grâce à un `OP_RETURN`. Les bitcoins éventuellement associés à ce type d'output sont non dépensables de manière prouvée, car l'`OP_RETURN` signale un script invalide.

## NULLDUMMY

Règle de consensus introduite avec le BIP147 dans le soft fork SegWit qui exige que l'élément factice (« *dummy element* ») utilisé dans les opcodes `OP_CHECKMULTISIG` et `OP_CHECKMULTISIGVERIFY` soit un tableau d'octets vide (`OP_0`). Cette mesure a été mise en place pour éliminer un vecteur de malléabilité en interdisant toute valeur autre que `OP_0` pour cet élément.

> *Pour plus d'informations, voir la définition de [**DUMMY ELEMENT**](./D.md#dummy-element) et [**BIP147**](./B.md#bip147).*

## NVERSION

Le champ `nVersion` dans une transaction Bitcoin sert à indiquer la version du format de transaction utilisé. Il permet au réseau de distinguer les différentes évolutions du format de transaction au fil du temps, et d'appliquer les règles correspondantes. Ce champ n'a aucun impact au niveau des règles de consensus. Cela signifie que toute valeur attribuée à ce champ n'entraîne pas l'invalidation de la transaction. En revanche, le champ `nVersion` dispose de règles de standardisation qui n'acceptent que la valeur de `1` et de `2` actuellement. Pour le moment, ce champ est seulement utile pour l'activation du champ `nSequence`.

> *Pour plus d'informations, voir la définition de [**NSEQUENCE**](./N.md#nsequence).*
