# <div align="center">***Le Dictionnaire de Bitcoin 2024***</div>

<div align="center">

*Tout le vocabulaire technique de Bitcoin et de son environnement.*

</div>


&nbsp;

&nbsp;



# Version en ligne
Afin de naviguer facilement dans *Le Dictionnaire de Bitcoin* sur cette version en ligne, vous pouvez utiliser la commande **ctrl + F** ou **commande + F**.

Vous lisez actuellement la version en ligne du livre *Le Dictionnaire de Bitcoin*, un ouvrage rédigé par Loïc Morel, publié sous licence [CC-BY-NC-SA 4.0](/README.md#licence-et-réutilisation). Si ce projet vous plait, vous êtes libre d'y [contribuer pour l'améliorer](/README.md#demandes-de-modification-et-contributions). Vous pouvez également me soutenir en achetant la version imprimée et brochée de cet ouvrage sur Amazon.fr.

Merci et bonne lecture !

&nbsp;

&nbsp;


# Sommaire




___ 


&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**A**</div>

&nbsp;


**ADRESSE DE RÉCEPTION -** Information utilisée pour recevoir des bitcoins. Une adresse est construite en hachant une clé publique, à l'aide de `SHA256` et de `RIMPEMD160`, et en ajoutant des métadonnées à ce condensat. Les clés publiques utilisées pour construire une adresse de réception font partie du portefeuille de l'utilisateur et sont donc dérivées depuis sa graine. Les adresses SegWit sont composées des informations suivantes : 
* Un HRP pour désigner « bitcoin » : `bc` ; 
* Un séparateur : `1` ; 
* La version de SegWit utilisée : `q` ou `p` ; 
* La charge utile : le condensat de la clé publique ; 
* La somme de contrôle : un code BCH.

Une adresse de réception peut être représentée sous la forme d'une chaîne de caractères alphanumériques ou sous la forme d'un QR code. Chaque adresse peut être utilisée plusieurs fois, mais c'est une pratique très déconseillée. En effet, dans le but de maintenir un certain niveau de confidentialité, il est conseillé de n'utiliser chaque adresse Bitcoin qu'une seule fois. Il faut en générer une nouvelle pour tout paiement entrant vers son portefeuille. Une adresse est encodée en `Bech32` pour les adresses SegWit V0, en `Bech32m` pour les adresses SegWit V1, et en `Base58check` pour les adresses Legacy. D'un point de vue technique, une adresse ne permet pas réellement de recevoir des bitcoins, mais plutôt de bloquer des bitcoins à l'aide d'un script, en mettant des contraintes sur leur dépense.

&nbsp;

**AJUSTEMENT DE LA DIFFICULTÉ (OU RECIBLAGE) -** L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin. Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L’ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d’un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. Le calcul qu'effectuent les nœuds pour calculer la nouvelle cible est le suivant : $N = A \cdot \left(\frac{T}{1,209,600}\right)$
Où :
* $N$ : La nouvelle cible ;
* $A$ : L'ancienne cible des 2016 derniers blocs ;
* $T$ : Le temps total réel des 2016 derniers blocs en secondes ;
* $1,209,600$ : Le temps cible en secondes pour produire 2016 blocs avec un intervalle de 10 minutes entre chacun.
> *En français, on parle parfois également de « reciblage » pour évoquer l'ajustement. En anglais, on parle de « Difficulty Adjustment ».*

&nbsp;

**ARBRE DE MERKLE -**

Un Arbre de Merkle est un accumulateur cryptographique. C’est une méthode pour justifier l’appartenance d’une information donnée à un ensemble plus grand. C'est une structure de données qui facilite la vérification d’informations dans un format compact. Dans le système Bitcoin, les arbres de Merkle sont utilisés pour regrouper et condenser les transactions d'un bloc en un unique hachage, appelé la racine de Merkle (ou « Top Hash »). Chaque transaction est hachée, puis les hachages adjacents sont hachés ensemble de façon hiérarchique jusqu'à ce que la racine de Merkle soit obtenue.
![Schéma arbre de Merkle](/dictionnaire/images/Arbre%20de%20Merkle.png)

Cette structure permet de vérifier rapidement si une transaction spécifique est incluse dans un bloc donné sans avoir à analyser l'ensemble des transactions. Par exemple, si je dispose seulement de la racine de Merkle et que je souhaite vérifier que la `TX 7` fait bien partie de l'arbre, j'aurai uniquement besoin des preuves suivantes :
* `TX 7` ;
* `HASH 8` ;
* `HASH 5-6` ;
* `HASH 1-2-3-4`.
Grâce à ces quelques informations, je suis en capacité de calculer les nœuds intermédiaires jusqu'à la racine de Merkle.
![Schéma 2 arbre de Merkle](/dictionnaire/images/Arbre%20de%20Merkle%202.png)

Les arbres de Merkle sont notamment utilisés pour les nœuds légers, dits « SPV Node », qui ne conservent que les entêtes de blocs, mais pas les transactions.
>*L'arbre de Merkle porte le nom de Ralph Merkle, un cryptographe pionnier qui a conçu cette structure en 1979. Un arbre de Merkle peut également être nommé « arbre de hachage ». En anglais, on dit « Merkle Tree » ou « Hash Tree ».*

&nbsp;

**ASIC (CIRCUIT INTÉGRÉ SPÉCIFIQUE À UNE APPLICATION) -** Un ASIC est un composant électronique conçu pour exécuter une fonction spécifique avec une efficacité optimale. Dans le contexte du minage de Bitcoin, les ASIC sont des circuits intégrés spécialisés qui effectuent des opérations de hachage à haute vitesse et faible consommation d'énergie. Ils sont spécialisés dans l'exécution de la fonction de hachage `SHA256` utilisée dans le mécanisme de la preuve de travail. L'ASIC est initialement le nom de la puce. Par extension, l'acronyme « ASIC » vise souvent à désigner également la machine qui héberge cette puce. Ainsi, les ordinateurs spécialisés dans le minage de Bitcoin sont parfois appelés des « ASIC », ou bien des « mineurs ». Les ASIC ont progressivement remplacé les autres méthodes de minage, telles que l'utilisation de processeurs (CPU) et de cartes graphiques (GPU), en raison de leur efficacité énergétique supérieure et de leur taux de hachage bien plus élevé.
>*L'acronyme « ASIC » désigne en anglais « Application-Specific Integrated Circuit ». En français, ce terme peut être traduit par « Circuit intégré spécifique à une application ».*

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**B**</div>

&nbsp;

**BARE-MULTISIG -** Script P2MS. Voir définition de « P2MS ».

&nbsp;

**BASE (ARITHMÉTIQUE) -** Une base est un système de numération positionnel qui utilise un nombre fixe de caractères pour représenter tous les nombres possibles. La base détermine le nombre de symboles distincts disponibles pour représenter les chiffres dans ce système. Par exemple, le système le plus connu dans nos vies quotidiennes est la base 10, également appelée système décimal. Elle utilise dix symboles distincts `(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)` pour représenter tous les nombres. D'autres systèmes de numération couramment utilisés dans les domaines informatique et mathématique incluent le système binaire (base 2), avec deux symboles `(0, 1)`, et le système hexadécimal (base 16), avec seize symboles `(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)`. Dans le cadre de Bitcoin, vous rencontrerez parfois des encodages en base 58 ou en base 32 adaptée (nommée `Bech32`).

&nbsp;

**BASE58CHECK -** La `Base58Check` est un encodage utilisé dans le système Bitcoin pour représenter les adresses de réception Legacy et certaines autres données, telles que les clés étendues, sous forme de chaînes de caractères lisibles par l'homme. C’est une variante du système `Base58`, une représentation positionnelle de base 58 conçue pour minimiser les erreurs de transcription humaine. Elle utilise un ensemble de 58 caractères alphanumériques, composé des chiffres de `1` à `9`, des lettres majuscules `A` à `Z` (à l'exception des lettres `I` et `O` pour éviter la confusion avec les chiffres `1` et `0`) et des lettres minuscules de `a` à `z` (à l'exception de la lettre `l` pour éviter la confusion avec le chiffre `1`). La `Base58Check` se distingue de la `Base58` par l'ajout d'une somme de contrôle (checksum). Elle est représentée par une version réduite d'un double hachage `SHA256` des données originales (`SHA256d` ou `HASH256`), à la fin des données encodées en `Base58`. Lors de la vérification, la somme de contrôle est recalculée et comparée à celle qui a été ajoutée lors de l'encodage. Si les deux empreintes correspondent, les données sont considérées comme valides, sinon une erreur de corruption ou de transcription est signalée. L'utilisation de la `Base58Check` dans les adresses Bitcoin et les clés privées procure plusieurs avantages. Premièrement, elle permet de réduire les erreurs humaines lors de la transcription et de la lecture en évitant les caractères ambigus. Deuxièmement, elle protège contre les erreurs de saisie en détectant et signalant les erreurs grâce au hachage de vérification. Troisièmement, la représentation compacte des données en `Base58Check` permet de réduire l'espace requis pour stocker et partager les adresses et les clés. Les adresses de réception les plus récentes (post-SegWit) ont abandonné cet encodage `Base58check` pour des encodages `Bech32` et `Bech32m`, disposant d'une somme de contrôle plus évoluée (code BCH).

&nbsp;

**BECH32 ET BECH32M -** `Bech32` et `Bech32m` sont deux formats d'encodage d'adresse pour recevoir des bitcoins. Ils sont établis sur une base 32 légèrement modifiée. Ils embarquent une somme de contrôle établie sur un algorithme de correction d'erreurs appelé BCH (Bose-Chaudhuri-Hocquenghem). Par rapport aux adresses Legacy, encodées en `Base58check`, les adresses `Bech32` et `Bech32m` disposent d'une somme de contrôle plus performante, permettant de détecter et potentiellement de modifier automatiquement les fautes de frappe. Leur format dispose également d'une meilleure lisibilité, avec uniquement des caractères minuscules. Voici la matrice d'addition de ce format depuis la base 10 : 

<div align="center">

|   $+$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|
| $0$   | $q$ | $p$ | $z$ | $r$ | $y$ | $9$ | $x$ | $8$ |
| $8$   | $g$ | $f$ | $2$ | $t$ | $v$ | $d$ | $w$ | $0$ |
| $16$  | $s$ | $3$ | $j$ | $n$ | $5$ | $4$ | $k$ | $h$ |
| $24$  | $c$ | $e$ | $6$ | $m$ | $u$ | $a$ | $7$ | $l$ |

</div>


`Bech32` et `Bech32m` sont des formats d'encodage utilisés pour représenter les adresses SegWit. `Bech32` est un format d'encodage d'adresse introduit par la BIP173 en 2017. Il utilise un ensemble de caractères spécifiques, composé de chiffres et de lettres minuscules, pour minimiser les erreurs de frappe et faciliter la lecture. Les adresses `Bech32` commencent généralement par `bc1` pour indiquer qu'elles sont natives de SegWit. Ce format est uniquement utilisé sur les adresses SegWit V0, avec les scripts `P2WPKH` (Pay to Witness Public Key Hash) et `P2WSH` (Pay to Witness Script Hash). Toutefois, il existe une petite faille inattendue propre au format `Bech32`. Chaque fois que le dernier caractère de l'adresse est un `p`, l'ajout ou la suppression d'un nombre quelconque de caractères `q` le précédant immédiatement n'invalide pas la somme de contrôle. Cela n'affecte pas les utilisations existantes des adresses SegWit V0 (BIP173) en raison de leur restriction à deux longueurs définies. Cependant, cela pourrait affecter des utilisations futures de l'encodage `Bech32`. Le format `Bech32m` est simplement un format `Bech32` avec cette erreur rectifiée. Il a été introduit avec le BIP350 en 2020. Les adresses `Bech32m` commencent également par `bc1`, mais elles sont spécifiquement conçues pour être compatibles avec la version SegWit V1 (Taproot) et les versions ultérieures, avec le script `P2TR` (Pay to TapRoot).

&nbsp;

**BIP (BITCOIN IMPROVEMENT PROPOSAL) -** Une proposition d'amélioration de Bitcoin (BIP) est un processus formel de proposition et de documentation des améliorations et des modifications apportées au protocole Bitcoin et à ses normes. Inspiré du processus des Python Enhancement Proposals (PEP), le BIP vise à faciliter la communication et la collaboration entre les développeurs, les chercheurs, les utilisateurs et les parties prenantes de l'écosystème Bitcoin. Le processus BIP assure une approche structurée et transparente pour l'évaluation et l'adoption de nouvelles fonctionnalités, optimisations et mises à jour. Chaque BIP est un document détaillé qui décrit précisément les objectifs de l'amélioration proposée, la justification de sa mise en œuvre, les éventuels problèmes de compatibilité, les avantages et les inconvénients. Il décrit également les étapes techniques nécessaires pour réaliser l'amélioration. Les BIP peuvent être rédigés par n'importe qui. Ils doivent cependant être soumis à un examen approfondi et à l'approbation d'autres membres de la communauté Bitcoin.

> *BIP est l'acronyme anglais pour « Bitcoin Improvment Proposal ». En français, on peut le traduire par « Proposition d'amélioration de Bitcoin ». Toutefois, la plupart des textes français utilisent directement l'acronyme « BIP » comme un nom commun, parfois au féminin, parfois au masculin.*

&nbsp;

**BIT -** Le mot « bit » est la contraction des termes « binary » et « digit » en anglais. Dans le contexte des sciences informatiques et de la cryptologie, un bit est l'unité fondamentale d'information numérique et représente la plus petite quantité d'information possible. Un bit ne peut prendre que deux valeurs distinctes : `0` ou `1`. Ces valeurs sont également appelées états binaires et peuvent représenter diverses choses, telles que les réponses `oui` ou `non`, `vrai` ou `faux` et `on` ou `off`. Les bits sont la base des systèmes numériques et sont utilisés pour stocker et transmettre de l'information dans les ordinateurs et les réseaux. Le nom de « Bitcoin » provient sûrement de la concaténation du terme « Bit », pour évoquer la nature électronique du système de paiement, et du terme « Coin », pour évoquer son objectif monétaire.

> *En français, on utilise souvent directement le mot « bit ». La traduction de ce terme anglais pourrait être « chiffre binaire ».*

Dans le contexte de Bitcoin, le terme « bit » est aussi utilisé pour désigner une subdivision monétaire du bitcoin. Un bit est égal à 100 satoshis, qui représentent la plus petite unité indivisible de bitcoin. Ainsi, un bitcoin est égal à 1 000 000 de bits ou 100 000 000 de satoshis. Cependant, l'utilisation de ce terme comme subdivision monétaire est sujet à controverse. La majorité des bitcoiners emploient soit le « sats », soit le « btc », mais pas le « bit ».

&nbsp;

**BITCOIN (« B » MAJUSCULE) -** Bitcoin est le nom du système de cash électronique pair-à-pair créé par Satoshi Nakamoto en 2009. L'utilisation du terme Bitcoin avec un « B » majuscule peut vouloir évoquer trois choses différentes :
* Le système Bitcoin ;
* Le protocole Bitcoin ;
* Le réseau Bitcoin.

Le terme de bitcoin avec un « b » minuscule est généralement réservé pour évoquer l'unité monétaire échangée sur ce système.

&nbsp;

**BITCOIN (« B » MINUSCULE) -** Le bitcoin (écrit avec un « b » minuscule) fait référence à l'unité monétaire utilisée pour les échanges sur le système de cash électronique Bitcoin (avec un "B" majuscule). Le bitcoin est souvent abrégé en « BTC » ou « XBT » et sert de moyen d'échange, de réserve de valeur et d'unité de compte au sein du réseau. Chaque bitcoin est divisible en 100 millions d'unités plus petites, appelées « satoshis » ou « sats », en l'honneur de son créateur, Satoshi Nakamoto. Les bitcoins sont émis par le processus de la preuve de travail (minage). Le nombre total de bitcoins est limité à 21 millions, assurant une offre finie et prévisible.

&nbsp;

**BITCOIN.CONF -** Fichier de configuration utilisé pour personnaliser le fonctionnement d'un nœud Bitcoin exécutant le client Bitcoin Core. Situé dans le répertoire de données de Bitcoin Core, ce fichier texte permet aux opérateurs de nœuds de spécifier divers paramètres et options qui influencent le comportement du nœud. Parmi les paramètres que l'on peut définir dans `bitcoin.conf`, on trouve des éléments tels que la taille de la Mempool, les restrictions sur les connexions réseau, les frais de transaction minimum de relai, ainsi que d'autres options de sécurité et de performances. La personnalisation via `bitcoin.conf` est essentielle pour adapter un nœud aux besoins spécifiques de son opérateur.

&nbsp;

**BITCOIN-CLI -** `Bitcoin-cli`, acronyme pour « *Bitcoin Command Line Interface* », est une interface de ligne de commande conçue pour interagir avec une instance de Bitcoin Core en exécution, en particulier le daemon, `bitcoind`. Il s’agit d’un programme indépendant qui offre à l’utilisateur un moyen de communiquer et d’exécuter des commandes pour contrôler et interroger l'état de l'instance de `bitcoind`. En plus des capacités de gestion du réseau, telles que la surveillance des transactions et des blocs, `bitcoin-cli` offre également des fonctionnalités de portefeuille, permettant aux utilisateurs d’effectuer des transactions Bitcoin en envoyant et recevant des fonds.

&nbsp;

**BITCOIN CORE -** Bitcoin Core est le logiciel open-source de référence pour le système Bitcoin, et constitue la principale implémentation du protocole Bitcoin à ce jour. Il est développé et maintenu par un large groupe de contributeurs bénévoles. Initialement nommé « Bitcoin Qt », c'est le troisième client de l'histoire de Bitcoin après Bitcoin, de Satoshi Nakamoto, et Bitcoind. Il a été développé à partir du code original de Satoshi et a introduit une interface graphique pour l'utilisateur. Par ailleurs, encore aujourd'hui, l'interface graphique de Bitcoin Core s'appelle `bitcoin-qt`. Il est fourni avec `bitcoind` depuis la version 0.5. Le logiciel Bitcoin Core sert à plusieurs fins. Tout d'abord, il agit comme un client nœud complet. Bitcoin Core inclut également un portefeuille (wallet) pour les utilisateurs qui souhaitent stocker, gérer et effectuer des transactions directement avec Bitcoin Core.

&nbsp;

**BITCOIND -** Acronyme de « *Bitcoin Daemon* ». C’est un logiciel qui implémente le protocole Bitcoin et permet aux utilisateurs d'exécuter un nœud pour des appels de procédure à distance dits RPC ( « *Remote Procedure Call* »). Il s'agit d'un programme en ligne de commande (sans GUI) qui sert d'interface de communication avec Bitcoin. Autrement dit, c’est un programme qui tourne en fond avec lequel l’utilisateur peut interagir (daemon). `Bitcoind` faisait partie du client original de Satoshi Nakamoto. Certains le considèrent comme le deuxième client de l’histoire de Bitcoin, après le premier de Satoshi, puisque la version 0.2.6 du logiciel permet cette exécution comme daemon sans interface graphique. Il fut par la suite regroupé avec Bitcoin QT en 2011, client renommé par la suite « Bitcoin Core », en 2014. Aujourd’hui, `bitcoind` est donc pleinement intégré au client Bitcoin Core.

&nbsp;

**BITCOIN QT -** Bitcoin QT est un client Bitcoin intégrant une interface graphique publié en mai 2011. Il s’inscrit dans la lignée du client de Satoshi lui-même. En 2014, Bitcoin QT est renommé « Bitcoin Core ». C’est aujourd’hui l’implémentation de référence du protocole Bitcoin. Il est fourni avec `bitcoind` depuis la version 0.5. Par ailleurs, encore aujourd'hui, l'interface graphique de Bitcoin Core s'appelle `bitcoin-qt` en référence aux origines du logiciel. 

> *« QT » provient du nom de la bibliothèque utilisée pour l’interface graphique, qui s’appelle donc « QT ». Le nom « Qt » est parfois interprété comme un jeu de mots sur la sonorité du terme « cute » (mignon en anglais).*

&nbsp;

**BLOC -**  Un bloc est une structure de données dans le système Bitcoin. Un bloc contient un ensemble de transactions valides et des métadonnées contenues dans son entête. Chaque bloc est lié au suivant par le hachage de son entête, formant ainsi la blockchain (chaîne de blocs). La blockchain agit comme un serveur d'horodatage qui permet à chaque utilisateur de connaître l'ensemble des transactions passées, afin de vérifier la non-existence d'une transaction et éviter la double dépense. Les transactions sont organisées dans un arbre de Merkle. Cet accumulateur cryptographique permet de produire un condensat de toutes les transactions d'un bloc, appelé « Racine de Merkle » (Merkle root). L'entête d'un bloc contient 6 éléments :
* La version du bloc ;
* L'empreinte du bloc précédent ;
* La racine de l'arbre de Merkle des transactions ;
* L'horodatage du bloc ;
* La cible de difficulté ;
* Le nonce (« *Number only used ONCE* »).

Pour être valide, un bloc doit disposer d'un entête qui, une fois haché avec `SHA256d`, produit un condensat inférieur ou égal à la cible de difficulté.

&nbsp;

**BLOC CANDIDAT -** Un bloc candidat est un bloc en cours de création par un mineur participant au processus de minage du système Bitcoin. Le bloc candidat est une structure de données temporaire qui contient des transactions en attente d'être confirmées, mais ne dispose pas encore d'une preuve de travail valide (proof-of-work) pour être ajouté à la blockchain. Le mineur sélectionne les transactions à inclure dans le bloc candidat en fonction de divers facteurs, tels que les frais de transaction associés et les contraintes de taille de bloc. Une fois les transactions sélectionnées, le mineur génère l'entête du bloc, qui comprend la version, un condensat des transactions (racine de Merkle), un horodatage, le hash du bloc précédent, la cible de difficulté et un nonce. Le mineur tente ensuite de trouver un hash de son entête satisfaisant la difficulté cible du moment. Pour ce faire, il modifie le nonce présent dans l'entête. Il peut également modifier d'autres informations présentes dans son bloc candidat. C'est le mécanisme de la preuve de travail. Si le mineur réussit à trouver un hash valide, le bloc candidat devient un bloc valide et est diffusé au réseau pour être ajouté à la blockchain.


&nbsp;


**BLOCKCHAIN -** La blockchain est le nom communément donné au serveur d'horodatage distribué du système Bitcoin. C'est une chaîne de blocs. Chaque bloc est lié au suivant par son empreinte cryptographique. Pour éviter la double dépense sur Bitcoin sans recourir à une autorité centrale, il faut que chaque utilisateur vérifie la non-existence d'une transaction dans le système. Le seul moyen de s'assurer de l'absence d'une transaction est d'être au courant de toutes les transactions Bitcoin passées. Dans cet objectif, les transactions sont horodatées au sein de blocs, et chaque utilisateur dispose de l'entièreté de la blockchain.

> *Suite aux nombreuses utilisations marketing abusives du terme de « Blockchain », notamment à la fin des années 2010, beaucoup de bitcoiners refusent l'emploi de ce mot. Certains préfèrent parler de « TimeChain » pour évoquer ce concept. D'autres, se référant au White Paper de Satoshi Nakamoto, évoquent une « Proof-of-Work Chain ». En français, le terme anglais de « Blockchain » est globalement admis. On peut également utiliser la traduction « chaîne de blocs ».*

&nbsp;

**BRC-20 -** BRC-20 définit un ensemble de règles et de méthodes à respecter pour permettre une interaction avec des jetons non natifs sur Bitcoin. Il s'appuie sur les inscriptions du protocole Ordinals afin de définir des fonctions interprétées en dehors de la chaine. Ce standard a été créé par le développeur Domo, au début du mois de mars 2023. Selon son créateur, ce standard n'est qu'une expérimentation. Cela n'a pas empêché la machine spéculative de prendre le dessus durant les mois d'avril et de mai 2023. Des milliers d'investisseurs se sont emparés de ce standard, en achetant massivement les jetons BRC-20, créant au passage une hausse soudaine et historique des frais de transaction sur Bitcoin. Les jetons BRC-20 sont dénués d'existence concrète sur Bitcoin. Ils sont off-chain. Ce protocole utilise simplement Bitcoin, à travers le protocole Ordinals, pour stocker et horodater des fonctions permettant la gestion des jetons BRC-20. Ces fonctions sont encodées dans un format texte JSON, puis elles sont diffusées sous forme d’inscription Ordinals sur Bitcoin. Il en existe trois :
* `deploy`, qui permet de créer un nouveau jeton BRC-20 et de définir ses conditions d'utilisation ;
* `mint`, qui permet de réclamer des jetons BRC-20 spécifiques. Cela représente leur émission ;
* `transfer`, qui permet de transférer des jetons BRC-20 entre plusieurs utilisateurs.

Pour exécuter ce protocole, il faut que des personnes maintiennent des serveurs qui recensent l'intégralité des fonctions. Le standard BRC-20 est alors une utilisation très peu optimisée de Bitcoin par rapport à un protocole tel que RGB.






&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**C**</div>

&nbsp;

&nbsp;

**CHIFFRER -** C

&nbsp;

**CIBLE DE DIFFICULTÉ -** Le facteur de difficulté, aussi connu sous le nom de cible de difficulté, est un paramètre crucial dans le mécanisme de consensus par preuve de travail (Proof of Work, PoW) utilisé par Bitcoin. La cible représente une valeur numérique qui détermine la difficulté pour les mineurs de résoudre un problème cryptographique spécifique, appelé preuve de travail, lors de la création d'un nouveau bloc dans la blockchain. La cible de difficulté est un nombre ajustable de 256 bits (64 octets) déterminant une limite d’acceptabilité pour le hachage de l’entête des blocs. Autrement dit, pour qu’un bloc soit valide, le hachage de son entête avec `SHA256d` (double `SHA256`) doit être numériquement inférieur ou égal à la cible de difficulté. La preuve de travail consiste à modifier le champ `nonce` de l'entête du bloc ou de la transaction coinbase jusqu'à ce que le hachage résultant soit inférieur à la valeur cible. Cette cible est ajustée tous les 2016 blocs (environ toutes les deux semaines), lors d'un évènement que l'on appelle « ajustement ». Le facteur de difficulté est recalculé en fonction du temps qu'il a fallu pour miner les 2016 blocs précédents. Si le temps total est inférieur à deux semaines, la difficulté augmente en ajustant la cible à la baisse. Si le temps total est supérieur à deux semaines, la difficulté diminue en ajustant la cible à la hausse. L’objectif est de conserver un temps de minage par bloc moyen à 10 minutes. Ce temps entre chaque bloc permet d'éviter les divisions du réseau Bitcoin, résultant en un gaspillage de la puissance de calcul. La cible de difficulté se trouve dans chaque entête de bloc, au sein du champ `nBits`. Puisque ce champ est réduit à 32 bits et que la cible fait en réalité 256 bits, la cible est compactée dans un format scientifique moins précis.

> *La cible de difficulté est parfois également nommée « facteur de difficulté ». Par extension, on peut l'évoquer avec son encodage dans les entêtes de bloc avec le terme « nBits ».*

&nbsp;

**CLÉ PRIVÉE -** Une clé privée est un élément fondamental de la cryptographie asymétrique. Il s'agit d'une chaîne de caractères alphanumériques de 256 bits qui représente un secret cryptographique. Cette clé est utilisée pour signer numériquement des transactions et prouver la possession d'une clé publique Bitcoin (et par extension, d'une adresse de réception). Les clés privées permettent donc de dépenser des bitcoins en débloquant les UTXO associés à la clé publique correspondante. Les clés privées doivent être conservées strictement confidentielles, car leur divulgation pourrait permettre à des tiers malveillants de prendre le contrôle des fonds associés. Dans le système Bitcoin, la clé privée est liée à une clé publique par le biais d'un algorithme de signature numérique à courbes elliptiques (ECDSA ou Schnorr). La clé publique est dérivée de la clé privée, mais l'inverse est pratiquement impossible à réaliser en raison de la difficulté computationnelle inhérente à la résolution du problème mathématique sous-jacent (problème du logarithme discret). La clé publique est généralement utilisée pour générer une adresse Bitcoin, qui sert à bloquer des bitcoins à l'aide d'un script. En cryptographie, les clés privées sont souvent des nombres aléatoires ou pseudo-aléatoires. Dans le contexte spécifique des portefeuilles déterministes et hiérarchiques Bitcoin, les clés privées sont dérivées de manière déterministe depuis la graine (seed). Les clés privées sont fréquemment confondues avec la graine (seed) ou avec la phrase de récupération (mnémonique). Pourtant, ces éléments sont bien différents.

> *En anglais, une clé privée se dit « private key ».*

&nbsp;

**CLÉ PUBLIQUE -** La clé publique est un élément essentiel de la cryptographie asymétrique. Elle est générée à partir d'une clé privée en utilisant une fonction mathématique irréversible. Sur Bitcoin, les clés publiques sont dérivées depuis leur clé privée associée grâce aux algorithmes de signature numérique à courbes elliptiques ECDSA ou Schnorr. La clé publique, contrairement à la clé privée, peut être partagée librement sans compromettre la sécurité des fonds. Dans le cadre du protocole Bitcoin, la clé publique sert de base pour créer une adresse Bitcoin, qui est ensuite utilisée pour créer des conditions de dépense sur un UTXO. Les clés publiques sont fréquemment confondues avec la clé maîtresse ou avec les clés étendues (xpub...). Pourtant, ces éléments sont bien différents.

> *En anglais, une clé publique se dit « public key ». Ce terme est parfois abrégé avec « pubkey », ou « PK ».*

&nbsp;

**CODE DE CHAÎNE -** Dans le contexte de la dérivation hiérarchique et déterministe (HD) des portefeuilles Bitcoin, le code de chaîne est une valeur de sel cryptographique de 256 bits utilisée pour générer des clés enfants à partir d'une clé parent, selon le standard BIP32. Le code de chaîne est utilisé en combinaison avec la clé parente et l’index de l’enfant pour générer de manière sécurisée et déterministe une nouvelle paire de clés (clé privée et clé publique) sans révéler la clé parente ou les autres clés enfants dérivées. Il existe donc un code de chaîne unique pour chaque paire de clés. Le code de chaîne est obtenu soit en hachant la graine du portefeuille, et en prenant la moitié des bits à droite. Dans ce cas, on parle d'un code de chaîne maître, associé à la clé privée maîtresse. Ou bien, il peut être obtenu en hachant une clé parent avec son code de chaîne parent et un index, et en conservant les bits à droite. On parle alors de code de chaîne enfant. Cette approche permet aux utilisateurs de gérer plusieurs adresses Bitcoin à partir d'une seule graine (seed), améliorant ainsi la confidentialité dans les transactions Bitcoin. Il est impossible de dériver des clés sans avoir la connaissance du code de chaîne associé à chaque paire parent. Il permet d'introduire des données pseudo-aléatoires dans le processus de dérivation pour garantir que la génération des clés cryptographiques reste imprévisible pour les attaquants tout en étant déterministe pour le détenteur du portefeuille.

> *En anglais, un code de chaîne se dit « chain code », et un code de chaîne maître se dit « master chain code ».*

&nbsp;

**COINJOIN -** Le CoinJoin est une technique permettant de casser le traçage des bitcoins. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction CoinJoin. Les transactions CoinJoin permettent d'améliorer la protection de la vie privée des utilisateurs de Bitcoin en rendant l'analyse des transactions plus difficile pour les observateurs extérieurs. Cette structure permet la combinaison de plusieurs transactions indépendantes en une seule transaction, rendant difficile la détermination des liens entre les adresses d'entrée et de sortie. Le fonctionnement général du CoinJoin est le suivant : différents utilisateurs souhaitant mixer déposent un montant en input d'une transaction. Ces inputs ressortiront en différents outputs de même montant. À la sortie de la transaction, il est donc impossible de déterminer quel output appartient à quel utilisateur. Il n'y a techniquement aucun lien entre les entrées et les sorties de la transaction CoinJoin. Le lien entre chaque utilisateur et chaque UTXO est cassé, de la même manière que l'historique de chaque pièce.
![Schéma Coinjoin](/dictionnaire/images/Sch%C3%A9ma%20coinjoin%20wp.png)
Pour permettre le CoinJoin sans qu'aucun utilisateur ne perde la main sur ses fonds à aucun moment, la transaction est d'abord construite par un coordinateur puis transmise à chaque utilisateur. Chacun d'eux signe alors la transaction de son côté en vérifiant qu'elle lui convient, puis toutes les signatures sont ajoutées à la transaction. Si un utilisateur ou le coordinateur tente de voler les fonds des autres en modifiant les outputs de la transaction CoinJoin, alors les signatures seront invalides et la transaction sera refusée par les nœuds. Ce mécanisme augmente la confidentialité des transactions sans nécessiter de modifications du protocole Bitcoin. Des implémentations spécifiques de CoinJoin, telles que Whirlpool, JoinMarket ou Wabisabi, proposent des solutions pour faciliter le processus de coordination entre les participants et renforcer l'efficacité de la transaction CoinJoin. Exemple de transaction coinjoin : https://mempool.space/fr/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2

> *Le terme de « CoinJoin » ne dispose pas de traduction française. Certains bitcoiners utilisent également les termes de « mix », de « mixing » ou encore de « mixage » pour évoquer la transaction CoinJoin. Selon moi, cette utilisation est une erreur puisque le « mixage » évoque plutôt l'activité d'un acteur central qui mélange des pièces. Cela n'a rien à voir avec le CoinJoin où l'utilisateur ne perd à aucun moment la main sur ses bitcoins durant le processus. Toutefois, ces termes sont globalement admis, même s'ils peuvent parfois porter à confusion.*


&nbsp;

**CONCATÉNATION -** La concaténation, dans le contexte de la cryptographie et des systèmes informatiques, désigne le processus d'assemblage de deux opérandes, en les mettant bout à bout, formant ainsi une nouvelle chaîne de caractères ou de données. Cette opération se note généralement avec un symbole de deux barres verticales $\Vert$, ou avec le symbôle $\circ$. Par exemple, la concaténation de $45$ avec $87$ sera égale à $4587$. Nous noterons : $45 \Vert 87 = 4587$. On a mis bout à bout les deux opérandes.

&nbsp;

**CONDENSAT (HASH) -** Le condensat, dans le contexte de la cryptographie, désigne le résultat (ou l'output) produit par l'application d'une fonction de hachage cryptographique à un ensemble de données. Le condensat est une chaîne de caractères de taille fixe généralement représentée sous forme d'une série de chiffres et de lettres en notation hexadécimale (base 16). Ce résultat a la particularité d'être presque unique et spécifique aux données d'entrée, de sorte qu'un changement minime dans l'entrée produira un condensat complètement différent. Les fonctions de hachage cryptographiques sont conçues pour être unidirectionnelles et résistantes aux collisions, rendant très difficile de retrouver les données initiales à partir du condensat ou de trouver deux entrées distinctes produisant le même condensat.

> *Voir la définition de « fonction de hachage » pour plus de précisions sur ce sujet.*

&nbsp;

**COURBE ELLIPTIQUE -** Dans le contexte de la cryptographie, une courbe elliptique est une courbe algébrique définie par une équation de la forme $y^2 = x^3 + ax + b$. Ces courbes sont utilisées dans la cryptographie à courbes elliptiques (ECC), qui est une méthode de cryptographie à clé publique permettant de créer des algorithmes de chiffrement, de signature numérique et d'échange de clés. Dans le contexte de Bitcoin, l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm) ou le protocole de Schnorr sont utilisés avec la courbe `secp256k1`. Cette courbe a été choisie pour ses propriétés de performance et de sécurité. Ces algorithmes sont utilisés pour générer des clés publiques à partir de clés privées, ainsi que pour signer des transactions, et donc débloquer des bitcoins.

&nbsp;

**CRYPTER -** Ce terme n'existe pas. On dit « chiffrer ».












&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**D**</div>

&nbsp;

**DISTRIBUÉ -** Attribut d'un réseau informatique dans lequel le pouvoir de décision et le contrôle sont répartis de manière équitable entre tous les participants du réseau. Cette répartition garantit la résilience du système. On parle également de réseau pair-à-pair. Contrairement à un réseau décentralisé, où le pouvoir est fragmenté et dispersé parmi plusieurs entités, mais où certaines autorités centrales demeurent dotées d'un pouvoir supérieur à celui des utilisateurs, un réseau distribué élimine l'autorité centrale en confiant la gestion et le contrôle aux utilisateurs eux-mêmes. Bitcoin est un exemple de réseau distribué. Comme protocole de cash électronique pair-à-pair, Bitcoin se distingue par son absence de hiérarchie et d'autorité centrale. La tenue du consensus, la vérification des transactions et l'émission de nouvelles unités monétaires sont réalisées par les utilisateurs du réseau. Cette structure distribuée assure la résilience et la résistance à la censure du système, rendant très difficile pour une entité unique de contrôler ou de manipuler le réseau.

> *Certaines personnes parlent de Bitcoin comme d'un système décentralisé. En effet, il n'est pas rare d'observer une interchangeabilité de ces deux termes. Un synonyme plus évocateur de l'adjectif « distribué » pourrait être « pair-à-pair », parfois abrégé « P2P », le sigle de la traduction anglaise « Peer-to-Peer ».*








































&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**E**</div>

&nbsp;

**ECDSA -** ECDSA (Elliptic Curve Digital Signature Algorithm) est un algorithme de signature numérique établi sur la cryptographie à courbes elliptiques (ECC). Il s'agit d'une variante de l'algorithme DSA (Digital Signature Algorithm). Il exploite les propriétés des courbes elliptiques pour procurer des niveaux de sécurité comparables à ceux des algorithmes de clé publique traditionnels, tels que RSA, tout en utilisant des clés de taille nettement inférieure. ECDSA permet la génération de paires de clés (clé publique et clé privée) ainsi que la création et la vérification de signatures numériques. Dans le contexte de Bitcoin, ECDSA est utilisé pour dériver des clés publiques, à partir de clés privées. Il est également utilisé pour signer les transactions afin de prouver que l'expéditeur possède les bitcoins. La courbe elliptique utilisée sur Bitcoin au sein d'ECDSA est `secp256k1`, définie par l'équation $y^2 = x^3 + ax + b$. Cet algorithme est celui utilisé dès les débuts de Bitcoin en 2009. Aujourd'hui, il partage sa place avec le protocole de Schnorr, un autre algorithme de signature électronique introduit avec Taproot en 2021.

&nbsp;

**ENTÊTE DE BLOC -** 
L'entête de bloc est une structure de données servant de composant principal dans la construction d'un bloc Bitcoin. Chaque bloc est composé d'un entête et d'une liste de transactions. L'entête de bloc contient les informations cruciales qui permettent d'assurer l'intégrité et la validité d'un bloc au sein de la chaîne de blocs (blockchain). L'entête de bloc contient 80 octets de métadonnées et se compose des éléments suivants :
* La version du bloc ;
* L'empreinte du bloc précédent ;
* La racine de l'arbre de Merkle des transactions ;
* L'horodatage du bloc ;
* La cible de difficulté ;
* Le nonce (Number only used ONCE).

Par exemple, voici l'entête du [bloc n° 785 530](https://mempool.space/fr/block/000000000000000000039a294df2039d5fc759f5fd4dde06f09a17efc29a01e4) au format hexadécimal, miné par Foundry USA le 15 avril 2023 : `00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e0051743f09a40`

Si l'on décompose cet entête, on peut reconnaitre :
* La version : `00e0ff3f` ;
* L'empreinte précédente : `5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000` ;
* La racine de Merkle : 
`206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0` ;
* L'horodatage : `bcb13a64` ;
* La cible : `b2e00517` ;
* Le nonce : `43f09a40`.

Pour être valide, un bloc doit disposer d'un entête qui, une fois haché avec `SHA256d`, produit un condensat inférieur ou égal à la cible de difficulté.

> *En anglais, on parle d'un « Block Header ».*

&nbsp;

**ENTRÉE (INPUT) -** Dans le contexte de Bitcoin, une « entrée » (ou « input » en anglais) au sein d’une transaction fait référence aux *Unspent Transaction Outputs* (UTXO) utilisés comme fonds d'origine pour une transaction. Chaque entrée contient des références aux UTXO précédents, qui seront alors « consommés » par la transaction. Ces entrées sont utilisées pour alimenter de nouveaux UTXO qui seront créés comme « sorties » (ou « outputs » en anglais) de la transaction, et qui peuvent ensuite être dépensés dans des transactions futures. Le rôle de la transaction Bitcoin est donc de consommer des UTXO en entrées, et de créer des nouveaux UTXO en sorties. La différence entre les deux correspond aux frais de transactions qui peuvent être récupérés par le mineur gagnant du bloc. D'un point de vue plus large, en informatique, le terme « input » ou « entrée » désigne généralement les données fournies à une fonction, un algorithme, ou un système en tant qu'opérandes ou informations requises pour effectuer une opération ou un calcul. Dans ce sens, le terme est utilisé de manière plus générique pour décrire tout ce qui est fourni à un processus en vue d'obtenir un résultat ou une « sortie » (output). Par exemple, lorsque l’on passe une donnée dans une fonction de hachage cryptographique, cette information est nommée « entrée » ou « input ». 

&nbsp;

**ENTROPIE -** L'entropie, dans le contexte de la cryptographie et de l'information, est une mesure quantitative de l'incertitude ou de l'imprévisibilité associée à une source de données ou à un processus aléatoire. L'entropie joue un rôle crucial dans la sécurité des systèmes cryptographiques, notamment dans la génération de clés et de nombres aléatoires. Une entropie élevée garantit que les clés générées sont suffisamment imprévisibles et résistantes aux attaques par force brute, où un attaquant essaie toutes les combinaisons possibles pour deviner la clé. Dans le contexte de Bitcoin, l'entropie est utilisée pour générer des clés privées ou des graines. Lors de la création d'un portefeuille déterministe et hiérarchique, la construction de la phrase mnémonique se fait à partir d'un nombre aléatoire, lui-même issu d'une source d'entropie. La phrase est ensuite utilisée pour générer plusieurs clés privées, de manière déterministe et hiérarchique, afin de créer des conditions de dépense sur des UTXO. Il est essentiel de disposer d'une source d'entropie de qualité pour garantir la sécurité des systèmes cryptographiques. Les sources d'entropie peuvent être des processus physiques, tels que le bruit électronique ou les variations thermiques, ou des processus logiciels, tels que les générateurs de nombres pseudo-aléatoires.

Dans le contexte spécifique de l'analyse de chaîne, l'entropie est également le nom d'un indicateur, dérivé de l'entropie de Shannon, inventé par LaurentMT. Cet indicateur permet de mesurer le manque de connaissance des analystes sur la configuration exacte d'une transaction Bitcoin. Ressource : https://gist.github.com/LaurentMT/e758767ca4038ac40aaf.


























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**F**</div>

&nbsp;

**FONCTION DE HACHAGE CRYPTOGRAPHIQUE -** Une fonction de hachage, également appelée algorithme de hachage, est une fonction mathématique qui prend une entrée de taille variable (appelée message) et produit une sortie de taille fixe (appelée hash, hachage, condensat ou empreinte). Les fonctions de hachage sont des primitives largement utilisées en cryptographie. Elles présentent des propriétés spécifiques qui les rendent appropriées pour une utilisation dans des contextes sécurisés :
* Résistance aux préimages : Il doit être très difficile de trouver un message donnant un hachage spécifique, c'est-à-dire de trouver une préimage $m$ pour un hash $h$ tel que $h = H(m)$, où $H$ est la fonction de hachage ;
* Résistance aux secondes préimages : Étant donné un message $m_1$, il doit être très difficile de trouver un autre message $m_2$ (différent de $m_1$) tel que $H(m_1) = H(m_2)$ ;
* Résistance aux collisions : Il doit être très difficile de trouver deux messages distincts $m_1$ et $m_2$ tels que $H(m_1) = H(m_2)$ ;
* Résistance à la falsification : De petites modifications dans l'entrée doivent provoquer des changements significatifs et imprévisibles dans la sortie.

Dans le contexte de Bitcoin, les fonctions de hachage sont utilisées à plusieurs fins, notamment pour le mécanisme de preuve de travail (Proof-of-Work), les identifiants de transaction, la génération d'adresses, le calcul de sommes de contrôle et la création de structures de données telles que les arbres de Merkle. Sur la partie protocolaire, Bitcoin utilise exclusivement la fonction `SHA256d`, également nommée `HASH256`, qui consiste en un double hachage `SHA256`. On utilise aussi `HASH256` dans le calcul de certaines sommes de contrôle, notamment pour les clés étendues (`xpub`, `xprv`...). Sur la partie portefeuille, on utilise également :
* `SHA256` simple pour les sommes de contrôle des phrases mnémoniques ;
* `SHA512` au sein des algorithmes `HMAC` et `PBKDF2` utilisés dans le processus de dérivation des portefeuilles déterministes et hiérarchiques ;
* `HASH160`, qui décrit une utilisation successive d'un `SHA256` et d'un `RIPEMD160`. `HASH160` est utilisé dans le processus de génération des adresses de réception et dans le calcul des empreintes de clés parents pour les clés étendues.

> *En anglais, on parle de « hash function ».*

&nbsp;

**FRAIS DE TRANSACTION -** Les frais de transaction représentent une somme qui vise à rémunérer les mineurs pour leur participation au mécanisme de la preuve de travail. Ces frais incitent les mineurs à inclure les transactions dans les blocs qu'ils créent. Ils sont le résultat de la différence entre le montant total des inputs et le montant total des outputs d’une transaction. $frais = inputs - outputs$

Ils sont exprimés en `sats/vBytes`, ce qui veut dire que les frais ne dépendent pas du montant des bitcoins envoyés, mais du poids de la transaction. Ils sont choisis librement par l'émetteur d’une transaction et déterminent la vitesse d’inclusion de la transaction dans un bloc par un mécanisme d'enchère. Par exemple, imaginons que je réalise une transaction avec un input de `100 000 sats`, un output de `40 000 sats` et un output de `58 500 sats`. Le total des outputs est de `98 500 sats`. Les frais alloués à cette transaction sont de `1 500 sats`. Le mineur qui inclut ma transaction pourra créer `1 500 sats` dans sa transaction coinbase en contrepartie des `1 500 sats` que je n'ai pas récupérés dans mes outputs. 

Les transactions avec des frais plus élevés, en fonction de leur taille, sont traitées en priorité par les mineurs, ce qui peut accélérer le processus de confirmation. Inversement, les transactions avec des frais plus faibles peuvent être retardées lors des périodes de forte congestion. Il convient de noter que les frais de transaction Bitcoin sont distincts de la subvention de bloc, qui est une incitation supplémentaire pour les mineurs. La récompense de bloc est composée de nouveaux bitcoins créés à chaque bloc miné (subvention de bloc), ainsi que des frais de transaction collectés. Tandis que la subvention de bloc diminue au fil du temps en raison de la limitation de l'offre totale de bitcoins, les frais de transaction, eux, continueront de jouer un rôle crucial pour encourager les mineurs à participer. 

Au niveau protocolaire, rien n'empêche les utilisateurs d’inclure des transactions sans aucuns frais dans un bloc. En réalité, ce type de transaction sans frais fait exception. Par défaut, les nœuds Bitcoin ne relaient pas les transactions disposant de frais inférieurs à `1 sat/vBytes`. Si certaines transactions sans frais ont pu passer, c'est parce qu'elles ont été intégrées directement par le mineur gagnant, sans parcourir le réseau de nœuds. Par exemple, la transaction [`fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3`](https://mempool.space/tx/fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3) n'inclut aucuns frais. Dans cet exemple précis, c'était une transaction initiée par le directeur de la pool de minage F2Pool. En tant qu'utilisateur normal, la limite inférieure est donc actuellement de `1 sat/vBytes`.
Il convient également de tenir compte les limites de purge. En période de forte congestion, les mempools des nœuds purgent leurs transactions en attente en dessous d'un certain seuil, afin de respecter leur limite de RAM attribuée. Cette limite est librement choisie par l'utilisateur, mais beaucoup laissent la valeur Bitcoin Core par défaut. Pour le moment, cette limite est de 300 Go par défaut, elle peut être modifiée dans le fichier `bitcoin.conf` avec le paramètre `maxmempool`.

> *En anglais, on parle de « transaction fees ».*



















&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**G**</div>

&nbsp;


**GENÈSE (BLOC) -** Le bloc de genèse Bitcoin, également connu sous le nom de bloc Genesis ou bloc #0, est le premier bloc du système Bitcoin. Il incarne le lancement concret de Bitcoin. Le bloc de genèse a été créé par le fondateur anonyme de Bitcoin, Satoshi Nakamoto, le 3 janvier 2009. Son hash est [`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`](https://mempool.space/fr/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f). Ce bloc contient seulement une transaction coinbase qui génère 50 bitcoins en récompense pour le mineur (dans ce cas, Satoshi Nakamoto lui-même). Il est particulièrement significatif en raison de son message incorporé dans la transaction coinbase : `The Times 03/Jan/2009 Chancellor on brink of second bailout for banks`. Cette citation est une référence à un article du journal *The Times*. Le message est interprété comme une critique du système financier traditionnel et de ses dérives, ce qui a en partie motivé la création de Bitcoin en tant qu'alternative. Puisqu’il incarne le tout premier bloc de la blockchain Bitcoin, le bloc de genèse ne possède évidemment pas de champ contenant le hachage du bloc antérieur (car il n'y en pas). Par ailleurs, les 50 bitcoins générés en récompense dans ce bloc ne sont pas dépensables au niveau protocolaire.

> *J’aime différencier les bitcoins perdus pour cause protocolaire, des bitcoins perdus pour cause applicative. Par définition, les bitcoins perdus au niveau protocolaire ne seront jamais dépensables, sauf à refaire la preuve de travail postérieure. J’y inclus notamment les pertes liées à la non-réclamation de la récompense coinbase, ou celles liées à un script OP_RETURN. Au contraire, les bitcoins perdus au niveau applicatif, souvent pour cause de perte de clés, seront sûrement un jour débloqués à cause des limitations de la cryptographie employée.*

&nbsp;

**GRAINE (SEED) -** Dans le cadre spécifique d'un portefeuille déterministe hiérarchique Bitcoin, une graine (ou « seed » en anglais) est une information de 512 bits issue d'un aléa. Elle permet de générer de manière déterministe et hiérarchique un ensemble de clés privées, et leurs clés publiques correspondantes, pour un portefeuille Bitcoin. La graine (seed) est souvent confondue avec la phrase de récupération en elle-même. Pourtant, c'est une information différente. La graine est obtenue en appliquant la fonction `PBKDF2` sur la phrase mnémonique et sur l’éventuelle passphrase. La graine a été inventée avec le BIP32 qui définit les bases du portefeuille déterministe hiérarchique. Dans ce standard, la graine mesurait 128 bits. Cela permet de dériver toutes les clés d'un portefeuille depuis une information unique, contrairement aux portefeuilles JBOK (Just a Bunch Of Keys) qui nécessitent de réaliser de nouvelles sauvegardes pour toute clé générée. Le BIP39 est par la suite venu proposer un encodage de cette graine, afin de simplifier sa lecture par l'humain. Cet encodage se fait sous la forme d'une phrase, que l'on nomme généralement phrase mnémonique ou phrase de récupération. Ce standard permet d'éviter les erreurs au niveau de la sauvegarde de la graine, notamment grâce à l'utilisation d'une somme de contrôle.

De manière plus générale, en cryptographie, une graine est un morceau de données aléatoires utilisé comme point de départ pour générer des clés cryptographiques, des chiffrements ou des séquences aléatoires. La qualité et la sécurité de nombreux processus cryptographiques dépendent de la nature aléatoire et de la confidentialité de la graine.

> *La traduction anglaise de « graine » est « seed ». En français, beaucoup utilisent directement le mot anglais pour désigner la graine.*

&nbsp;

**GUI -** C















&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**H**</div>

&nbsp;

**HALVING -** Le terme « halving » (division par deux) fait référence à un événement programmé qui réduit de moitié la récompense attribuée aux mineurs pour chaque bloc miné via la subvention de bloc. Cette réduction s'applique spécifiquement à la partie de la subvention de bloc constituée de nouveaux bitcoins créés ex-nihilo. Le halving a été conçu par Satoshi Nakamoto, le créateur de Bitcoin, comme un mécanisme permettant de contrôler l'inflation et d'assurer un approvisionnement limité en bitcoins. La récompense de bloc initiale était de 50 bitcoins, et le halving se produit tous les 210 000 blocs minés, ce qui prend environ quatre ans. Le premier halving a eu lieu en novembre 2012, réduisant la récompense de bloc à 25 bitcoins, et les suivants ont réduit la récompense à 12,5, puis 6,25 bitcoins respectivement. Les halvings continueront à se produire jusqu'à ce que la récompense de bloc atteigne zéro, moment auquel l'offre maximale de 21 millions de bitcoins aura été (presque) atteinte. Le prochain halving de Bitcoin devrait avoir lieu aux alentours du printemps 2024, bien que la date exacte puisse légèrement varier en fonction du temps de minage des blocs. À ce moment-là, la récompense de bloc sera réduite de 6,25 à 3,125 bitcoins. Ce sera le quatrième halving de l'histoire de Bitcoin. Les bitcoiners étudient attentivement les effets des halvings sur le système, car les incitations pour les mineurs diminuent avec le temps. À mesure que les récompenses de bloc baissent, les frais de transaction deviennent une source de revenus de plus en plus importante pour les mineurs, ce qui garantit leur motivation à continuer à participer à la preuve de travail.

&nbsp;

**HARDWARE WALLET -** Un hardware wallet, ou portefeuille matériel, est un dispositif électronique dédié à la sécurisation et à la gestion des clés privées d'un portefeuille Bitcoin. Ces périphériques sont conçus pour procurer une sécurité renforcée par rapport aux portefeuilles logiciels qui résident sur des machines polyvalentes et directement connectées à internet. Les hardwares wallets stockent la phrase mnémonique hors ligne, sur un matériel qui dispose d'une infime surface d'attaque, ce qui l'isole des environnements potentiellement vulnérables. Lorsqu'une transaction est effectuée, le portefeuille matériel signe la transaction à l'intérieur du dispositif lui-même, sans exposer la clé privée à l'extérieur. Une fois la transaction signée, elle est transmise au réseau Bitcoin pour être confirmée et incluse dans la blockchain Bitcoin. Parmi les modèles de hardwares wallets les plus populaires, on peut citer : Ledger, Trezor, Coldcard, Passport, BitBox, Satochip, Jade ou encore SeedSigner (liste non exhaustive).

> *Le hardware wallet peut être exprimé de différentes manières en français. Certains parlent de « portefeuille matériel » ou bien de « portefeuille froid ». Certains bitcoiners préfèrent que l'on emploie le terme de « périphérique de signature », ou « signing device » en anglais, afin d'éviter de faire penser que les bitcoins se trouvent physiquement dans le portefeuille.*

&nbsp;

**HMAC-SHA512 -** `HMAC-SHA512` est l’acronyme de « Hash-based Message Authentication Code - Secure Hash Algorithm 512 ». C’est un algorithme cryptographique utilisé pour vérifier l'intégrité et l'authenticité des messages échangés entre deux parties. Il combine la fonction de hachage cryptographique `SHA512` (Secure Hash Algorithm 512) avec une clé secrète partagée pour générer un code d'authentification de message (MAC) unique pour chaque message. Dans le contexte de Bitcoin, l'utilisation naturelle de `HMAC-SHA512` est légèrement dérivée. On utilise cet algorithme dans le processus de dérivation déterministe et hiérarchique de l'arbre de clés cryptographiques d'un portefeuille. `HMAC-SHA512` est notamment utilisé pour passer de la graine (seed) à la clé maîtresse, puis pour chaque dérivation d’une paire parent vers des paires enfants. On retrouve également cet algorithme au sein d'un autre algorithme de dérivation, nommé `PBKDF2`, utilisé pour passer de la phrase de récupération et de la passphrase à la graine.

&nbsp;

**HORODATAGE (TIMESTAMP) -** L'horodatage, ou « timestamp » en anglais, est un mécanisme qui consiste à associer un repère temporel précis à un événement, une donnée ou un message. Dans le contexte de la cryptographie et des systèmes informatiques, l'horodatage sert à déterminer l'ordre chronologique des opérations et à vérifier l'intégrité des données en fonction du temps. Dans le cas spécifique de Bitcoin, les horodatages jouent un rôle crucial pour établir la chronologie des transactions et des blocs. Chaque bloc dans la blockchain contient un horodatage indiquant le moment approximatif de sa création. Satoshi Nakamoto parle même d'un « serveur d'horodatage », dans son White Paper, pour décrire ce que l'on appellerait aujourd'hui la « blockchain ». Le rôle de l'horodatage sur Bitcoin est de déterminer la chronologie des transactions, afin de pouvoir déterminer, sans l'intervention d'une autorité centrale, quelle transaction est arrivée en première. Ce mécanisme permet à chaque utilisateur de vérifier la non-existence d'une transaction par le passé, et donc d'éviter qu'un utilisateur malintentionné opère une double dépense. Ce mécanisme est justifié par Satoshi Nakamoto dans son White Paper par la célèbre phrase : « *Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.* » Cette norme est établie sur l'heure Unix, qui représente le total de secondes passées depuis le premier janvier 1970.

> *L'horodatage des blocs est relativement flexible sur Bitcoin, car pour qu'un horodatage soit considéré comme valide, il est simplement nécessaire qu'il soit plus grand que le temps médian des 11 blocs qui le précèdent.*























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**I**</div>

&nbsp;

**INDEX (NUMÉRO DE CLÉ) -** Dans le contexte d'un portefeuille HD (Hierarchical Deterministic), fait référence au numéro séquentiel attribué à une clé enfant générée à partir d'une clé parent. Cet index est utilisé en combinaison avec la clé parent et le code chaîne parent pour dériver de manière déterministe des clés enfants uniques. Il permet une organisation structurée et la génération reproductible de multiples paires de clés enfants soeur depuis une même clé parent. C’est un entier de 32 bits utilisé dans la fonction de dérivation `HMAC-SHA512`. Ce nombre permet donc de différencier les clés enfants sœurs au sein d’un portefeuille HD.

&nbsp;

**INPUT -** Voir définition du terme « Entrée ».
















&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**J**</div>

&nbsp;

**JBOK (PORTEFEUILLE) -** Les portefeuilles JBOK, acronyme pour « Just a Bunch Of Keys » (en français « juste un trousseau de clés »), font référence aux portefeuilles Bitcoin initiaux qui stockaient un ensemble de paires de clés générées de manière indépendante et pseudo-aléatoire. Contrairement aux portefeuilles HD (Hierarchical Deterministic) modernes, qui génèrent des clés de manière déterministe et hiérarchique à partir d'une graine unique, les portefeuilles JBOK ne présentaient aucune relation hiérarchique ou déterministe entre les clés. Elles étaient toutes indépendantes les unes des autres. En raison de leur gestion moins efficace et de la difficulté de sauvegarde, ces portefeuilles sont devenus obsolètes et ont été spontanément remplacés par des solutions HD plus avancées, comme standardisées dans le BIP32.

&nbsp;













&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**K**</div>

&nbsp;















&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**L**</div>

&nbsp;

**LIGHTNING NETWORK -** Protocole de couche supérieure, construit au-dessus du protocole Bitcoin, visant à permettre des transactions rapides et à faible coût. Il permet la création de canaux de paiement entre les participants, au sein desquels les transactions peuvent être effectuées presque instantanément et avec des frais minimes, sans avoir à enregistrer chaque transaction individuellement sur la blockchain. Les canaux peuvent rester ouverts quasi indéfiniment, et ne nécessitent des transactions sur la blockchain que lors de leur ouverture et de leur clôture. Le Lightning Network vise à améliorer la scalabilité de Bitcoin et à rendre possible son utilisation pour des paiements de faible valeur. Toutefois, le Lightning Network n’est pas une solution parfaite. Ce protocole a une tendance naturelle à la centralisation sur de gros nœuds institutionnels. Il peut également être difficile de l’utiliser durant les périodes de très fortes congestions, comme on a pu le voir durant l’épisode BRC-20 en mai 2023. Aussi, sa structure rend très complexe la confidentialité des paiements.

&nbsp;

**LOGARITHME DISCRET (PROBLÈME) -** Le logarithme discret est un problème mathématique qui joue un rôle central en cryptographie à clé publique. Dans un groupe cyclique d’ordre $q$, avec un générateur $g$, si l'on a une équation de la forme $g^x = h$, alors $x$ est appelé le logarithme discret de $h$ par rapport à la base $g$, modulo $q$. En termes simples, il s’agit de déterminer l’exposant $x$ lorsqu’on connaît $g$, $h$, et $q$. Le logarithme discret est donc la réciproque de l'exponentielle dans un groupe cyclique fini. Cependant, pour de grandes valeurs de $q$, résoudre le problème du logarithme discret est considéré comme algorithmiquement difficile. Cette propriété est exploitée pour assurer la sécurité de nombreux protocoles cryptographiques, tels que le protocole de Diffie-Hellman pour l'échange de clés. Le logarithme discret est aussi utilisé dans la cryptographie à courbes elliptiques (ECC), entre autres dans l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm). Dans le contexte des courbes elliptiques, le problème du logarithme discret s'étend à la recherche d'un scalaire $k$ tel que $k \cdot G = K$, où $G$ et $K$ sont des points sur la courbe, et $\cdot$ représente l'opération de multiplication de points. Dans le contexte de Bitcoin, les transactions standard utilisent soit ECDSA, soit le protocole de Schnorr, afin de bloquer des UTXO. Ils reposent tous deux sur l’impossibilité de calculer le logarithme discret.























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**M**</div>

&nbsp;

**MAPPER (TO MAP) -** Dans le contexte de l'informatique et du traitement des données, mapper désigne le processus d'associer des éléments d'un ensemble de données à des éléments d'un autre ensemble de données de manière systématique et cohérente. Cette association permet aux données du premier ensemble de se substituer à celles du second ensemble ou de transitionner de l'un à l'autre. Cette technique est souvent utilisée dans les opérations de transformation de données, la programmation orientée objet, et le mappage objet-relationnel, où il est essentiel de convertir et de correspondre les données entre différents formats ou structures.

&nbsp;

**MAST -** M

&nbsp;

**MEMPOOL -** Contraction des termes « memory » et « pool ». Cela désigne un espace virtuel dans lequel les transactions Bitcoin en attente d'inclusion dans un bloc sont regroupées. Lorsqu'une transaction est créée et diffusée sur le réseau Bitcoin, elle est d'abord vérifiée par les nœuds du réseau. Si elle est considérée comme valide, elle est alors placée dans la Mempool, où elle reste jusqu'à ce qu'elle soit sélectionnée par un mineur pour être incluse dans un bloc. Il est important de noter que chaque nœud du réseau Bitcoin maintient sa propre Mempool, et donc, il peut y avoir des variations dans le contenu de la Mempool entre différents nœuds à un moment donné. Notamment, le paramètre `maxmempool` dans le fichier `bitcoin.conf` de chaque nœud permet aux opérateurs de contrôler la quantité de RAM (mémoire vive) que leur nœud utilisera pour stocker les transactions en attente dans la Mempool. En limitant la taille de la Mempool, les opérateurs de nœuds peuvent éviter que celle-ci ne consomme trop de ressources sur leur système. Ce paramètre est spécifié en mégaoctets (MB). La valeur par défaut de Bitcoin Core à ce jour est de 300 Mo. Les transactions présentent dans les mempool sont provisoires. Elles ne doivent pas être considérées comme immuable tant qu’elles ne sont pas incluses dans un bloc, et après un certain nombre de confirmations. Celles-ci peuvent souvent être remplacées, purgées ou double-dépensées.

&nbsp;

**MINAGE -** Action de participer à la preuve de travail (Proof-of-Work) du système Bitcoin. La preuve de travail est un mécanisme de résistance aux attaques Sybil. Elle est à la base du protocole de consensus de Nakamoto, qui est le principe utilisé pour établir un accord sur une version unique du registre distribué entre les différents nœuds du réseau. Concrètement, le minage est la recherche d’une valeur qui, une fois passée dans une fonction mathématique aléatoire, donne un résultat inférieur à un nombre cible. Cette cible de la preuve de travail est ajustée tous les 2016 blocs par les nœuds. C’est ce que l’on appelle l’ajustement de la difficulté. On abaisse le nombre cible pour augmenter la difficulté de minage, ou on l’augmente pour baisser la difficulté, en fonction de l’évolution de la puissance de calcul déployée par les mineurs durant la période précédente. Ce travail effectué par les mineurs est récompensé à chaque bloc valide trouvé. Le mineur gagnant empoche une récompense pécuniaire, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction. Aujourd’hui, la difficulté de la preuve de travail sur Bitcoin est telle que le minage nécessite une grande puissance de calcul pour parvenir à gagner des blocs. En conséquence, il faut souvent disposer de puces électroniques spécialisées dans l’exécution de `SHA256`, c’est ce que l’on appelle un ASIC, et participer dans des pools de minage.

&nbsp;

**MINEUR -** Dans le contexte de Bitcoin, un mineur fait référence à un ordinateur engagé dans le processus de minage, qui consiste à participer à la preuve de travail (Proof-of-Work). Le mineur regroupe les transactions en attente dans sa mempool pour former un bloc candidat. Ensuite, il recherche un hachage valide, inférieur ou égal à la cible, pour l’entête de ce bloc en modifiant les différents nonces. S’il trouve un hachage valide, il diffuse son bloc au réseau Bitcoin et empoche la récompense pécuniaire associée, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction. Par extension, le terme de « mineur » désigne également la personne ou l'entité qui possède et opère un ou plusieurs de ces ordinateurs.






















&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**N**</div>

&nbsp;

**NŒUD -** Dans le réseau Bitcoin, un nœud (ou « node » en anglais) est un ordinateur qui exécute un client du protocole Bitcoin (comme Bitcoin Core par exemple). Il participe au réseau en maintenant une copie de la blockchain, en relayant et en vérifiant les transactions et les nouveaux blocs et, optionnellement, en participant au processus de minage. La somme de tous les nœuds Bitcoin représente le réseau Bitcoin en lui-même. Il existe plusieurs types de nœuds sur Bitcoin, dont les plus notables sont les nœuds complets et les nœuds légers. Les nœuds complets conservent une copie intégrale de la blockchain, vérifient toutes les transactions et les blocs selon les règles de consensus, et participent activement à la diffusion de transactions et de blocs sur le réseau. En revanche, les nœuds légers, ou nœuds SPV (Simple Payment Verification), ne conservent qu'une partie de la blockchain et comptent sur les nœuds complets pour obtenir des informations sur les transactions. 

> *Certains différencient également les nœuds dits « élagués » (« pruned node » en anglais). Ce sont des nœuds complets, qui téléchargent et vérifient tous les blocs depuis le bloc Genesis, mais qui ne conserve que les blocs les plus récents en mémoire.*

&nbsp;

**NŒUD COMPLET -** Un nœud complet, ou « Full Node » en anglais, fait référence à un ordinateur qui exécute un client du protocole Bitcoin, et qui télécharge, vérifie et stocke la totalité de la blockchain, soit l'historique complet des transactions depuis le bloc Genesis. Un nœud complet vérifie de manière autonome toutes les transactions et les blocs en fonction des règles de consensus de Bitcoin. C’est donc ce type de nœud qui procure le plus haut niveau de vérification pour son utilisateur, et qui permet de réduire au maximum le besoin de confiance envers une tierce partie. Le nœud complet nécessite plus de ressources de stockage, de puissance de calcul, de RAM et de bande passante qu'un nœud léger (SPV).

&nbsp;

**NŒUD ÉLAGUÉ -** Un nœud élagué, en anglais « Pruned Node », est un nœud complet qui exécute un élagage de la blockchain. Cela consiste à supprimer de manière progressive les blocs les plus anciens, après les avoir dûment vérifiés, pour conserver seulement les blocs les plus récents. La limite de conservation est renseignée dans le fichier `bitcoin.conf` via le paramètre `prune=n`, ou `n` est la taille maximale prise par les blocs en mégaoctets (Mo). Si `0` est noté après ce paramètre, alors l’élagage est désactivé, et le nœud conserve la blockchain dans son intégralité. Les nœuds élagués sont parfois considérés comme des types de nœuds différents des nœuds complets. L'utilisation d'un nœud élagué peut s'avérer particulièrement intéressante pour les utilisateurs confrontés à des contraintes en termes de capacité de stockage. Actuellement, un nœud complet doit disposer d’environ 500 Go pour le stockage de la blockchain. Un nœud élagué peut limiter le stockage requis jusqu’à 550 Mo. Bien qu’il utilise moins d’espace disque, un nœud élagué maintient un niveau de vérification et de validation semblable à celui d'un nœud complet. Les nœuds élagués offrent donc plus de confiance à leurs utilisateurs en comparaison avec les nœuds légers (SPV).

&nbsp;

**NŒUD SPV (OU NŒUD LÉGER)-** Un nœud SPV (Simple Payment Verification), parfois nommé « nœud léger », est un client léger d'un nœud Bitcoin qui permet aux utilisateurs de valider les transactions sans avoir à stocker l'intégralité de la blockchain. Au lieu de cela, un nœud SPV stocke seulement les entêtes des blocs, et obtient des informations sur des transactions spécifiques en interrogeant des nœuds complets lorsque nécessaire. Ce principe de vérification est rendu possible par la structure des transactions dans les blocs Bitcoin, qui sont organisées au sein d’un accumulateur cryptographique (Arbre de Merkle). Cette approche est avantageuse pour les appareils avec des ressources limitées, tels que les téléphones portables. Cependant, les nœuds SPV font confiance aux nœuds complets pour la disponibilité des informations, ce qui implique un niveau de confiance supplémentaire et, par conséquent, une moindre sécurité par rapport aux nœuds complets. Les nœuds SPV ne peuvent pas valider les transactions de manière autonome, mais ils peuvent vérifier si une transaction est incluse dans un bloc en consultant les preuves de Merkle.

&nbsp;

**NONCE -** Dans le contexte de l’informatique, le terme « Nonce » est l’acronyme de *Number only used Once* (nombre utilisé seulement une seule fois). Il s'agit d'un nombre, souvent aléatoire ou pseudo-aléatoire, utilisé dans divers protocoles cryptographiques pour garantir la sécurité du procédé. Par exemple, les signatures ECDSA utilisées au sein du protocole Bitcoin incluent l’utilisation d’un Nonce. Cela veut dire que ce nombre doit être nouveau pour chaque signature. Si ce n’est pas le cas, il est possible de calculer la clé privée utilisée en rapprochant deux signatures qui utilisent le même Nonce. On utilise également des Nonces dans le processus de minage sur Bitcoin. Les mineurs incrémentent ces valeurs modifiables au sein de leurs blocs candidats. Ils modifient la valeur du nonce dans le but de trouver une empreinte cryptographique inférieure ou égale à la cible de difficulté. Ce processus nécessite une grande puissance de calcul, car il s’agit d’une recherche exhaustive parmi un grand nombre de nonces possibles. Lorsqu'un mineur trouve un nonce qui, lorsqu'il est inclus dans son bloc, produit un condensat répondant aux critères de difficulté, le bloc est diffusé au réseau, et le mineur remporte la récompense.

> *En 2010, des chercheurs ont découvert que la PlayStation 3 de Sony utilisait le même nonce lors de la signature de différents paquets de code. Cette réutilisation du nonce a permis aux attaquants de calculer la clé privée utilisée pour signer le logiciel. Avec la clé privée en main, les attaquants pouvaient créer des signatures valides pour n'importe quel code, ce qui leur permettait d'exécuter des logiciels non autorisés, y compris des jeux piratés ou des systèmes d'exploitation personnalisés, sur la PS3.*

































&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**O**</div>

&nbsp;








&nbsp;

**OUTPUT -** Voir définition du terme « Sortie ».








&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**P**</div>

&nbsp;

**P2PK -**  `P2PK` est le sigle pour *Pay to Public Key* (en français « payer à une clé publique »). C’est un standard de script utilisé sur Bitcoin pour établir des conditions de dépenses sur un UTXO. Il permet de bloquer des bitcoins directement sur une clé publique, plutôt que sur une adresse. 
Techniquement, le script `P2PK` contient une clé publique et une instruction qui exige une signature numérique correspondante pour débloquer les fonds. Lorsque le propriétaire souhaite dépenser les bitcoins, il doit fournir une signature produite avec la clé privée associée. Cette signature est vérifiée avec l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm). `P2PK` était souvent utilisé dans les premières versions de Bitcoin, notamment par Satoshi Nakamoto. Il n’est presque plus utilisé à ce jour.

&nbsp;

**P2PKH -** `P2PKH` est le sigle pour *Pay to Public Key Hash* (en français « payer au hachage d’une clé publique »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. Il permet de bloquer des bitcoins sur un hachage d’une clé publique, c’est-à-dire sur une adresse de réception. Ce script est associé au standard Legacy, et a été introduit dès les premières versions de Bitcoin par Satoshi Nakamoto. À la différence du `P2PK`, où la clé publique est explicitement incluse dans le script, le `P2PKH` fait appel à une empreinte cryptographique de la clé publique, avec quelques métadonnées, également nommée « adresse de réception ». Ce script inclut le hachage `RIPEMD160` du `SHA256` de la clé publique et stipule que, pour accéder aux fonds, le destinataire doit fournir une clé publique correspondant à ce hachage, ainsi qu'une signature numérique valide générée à partir de la clé privée associée. Les adresses `P2PKH` sont encodées en utilisant le format `Base58Check`, ce qui leur confère une robustesse contre les erreurs typographiques grâce à l'utilisation d'une somme de contrôle. Ces adresses débutent systématiquement par le chiffre `1`.

&nbsp;

**P2MS -** `P2MS` est le sigle pour *Pay to Multisig* (en français « payer aux multiples signatures »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. Il permet de bloquer des bitcoins à l’aide de plusieurs clés publiques. Pour dépenser ces bitcoins, il faut réaliser une signature avec un nombre prédéfini de clés privées associées. Par exemple, un `P2MS 2/3` dispose de `3` clés publiques avec `3` clés privées secrètes associées. Pour dépenser les bitcoins bloqués avec ce script `P2MS`, il faut réaliser une signature avec au moins `2` parmi les `3` clés privées. C’est un système de sécurisation à seuil (threshold). Ce script a été inventé en 2011 par Gavin Andresen alors qu’il venait de récupérer la maintenance du client principal de Bitcoin. Aujourd’hui, le `P2MS` n’est utilisé qu’à la marge par certaines applications. L’extrême majorité des multisignatures modernes emploient d’autres scripts comme le `P2SH` ou le `P2WSH`. Par rapport à ceux-ci, le `P2MS` est extrêmement trivial. Les clés publiques le constituant sont dévoilées dès la réception de la transaction. L’utilisation d’un `P2MS` est également plus chère que les autres scripts multisignature.

> *Les P2MS sont souvent nommés « bare-multisig », ce qui peut être traduit en français par « multi-signature nu », ou « multi-signature brut ». Au début de l'année 2023, les scripts P2MS étaient au centre d'une polémique à cause de leur utilisation détournée au sein du protocole Stamps. Leur impact sur l'UTXO SET était notamment pointé du doigt.*

&nbsp;

**P2SH -** `P2SH` est le sigle pour *Pay to Script Hash* (en français « payer au hachage du script »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. Contrairement aux scripts `P2PK` et `P2PKH`, où les conditions de dépense sont prédéfinies, `P2SH` permet l'intégration de conditions de dépense arbitraires et de fonctionnalités additionnelles au sein d'un script de transaction. Techniquement, dans une transaction `P2SH`, le `ScriptPubKey` contient l'empreinte cryptographique d'un script de rachat, plutôt que de conditions de dépense explicites. Cette empreinte est obtenue en utilisant un hachage `SHA256`. Lors de l'envoi de bitcoins à une adresse `P2SH`, le script de rachat sous-jacent n'est pas révélé. Seule son empreinte est incluse dans la transaction. Les adresses `P2SH` sont encodées en `Base58Check` et commencent par le chiffre `3`. Lorsque le destinataire souhaite dépenser les bitcoins reçus, il doit fournir un script de rachat correspondant à l'empreinte, ainsi que les données nécessaires pour satisfaire les conditions de ce script. Par exemple, dans un `P2SH` multi-signatures, le script pourrait exiger des signatures de plusieurs clés privées. L'utilisation de `P2SH` confère une flexibilité considérable, car il permet la construction de scripts arbitraires sans que l'expéditeur ait à en connaître les détails. `P2SH` est introduit en 2012 avec le BIP16.

&nbsp;

**P2TR -** `P2TR` est le sigle pour *Pay to Taproot* (en français « payer à la racine pivotante »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2TR` a été introduit avec l'implémentation de Taproot en novembre 2021. `P2TR` utilise le protocole de Schnorr pour agréger des clés cryptographiques, ainsi que des arbres de Merkle pour des scripts alternatifs, connus sous le nom de MAST (*Merkelized Alternative Script Tree*). Contrairement aux transactions traditionnelles où les conditions de dépense sont exposées publiquement (parfois à la réception, parfois à la dépense) `P2TR` permet de masquer des scripts complexes derrière une seule clé publique apparente. Techniquement, un script `P2TR` verrouille des bitcoins sur une clé publique Schnorr unique, dénommée $K$. Cependant, cette clé $K$ est en réalité un agrégat d'une clé publique $P$ et d'une clé publique $M$, cette dernière étant calculée à partir de la racine de Merkle d'une liste de `ScriptPubKeys`. L'agrégation de clés est réalisée à l'aide du protocole de signature de Schnorr. Les bitcoins verrouillés avec un script `P2TR` peuvent être dépensés de deux manières distinctes : soit en publiant une signature pour la clé publique $P$, soit en satisfaisant l'un des scripts contenus dans l'arbre de Merkle. La première option est appelée « key path » (chemin de clé) et la seconde « script path » (chemin de script). Ainsi, `P2TR` permet aux utilisateurs d'envoyer des bitcoins soit à une clé publique, soit à plusieurs scripts de leur choix. Un autre avantage de ce script est que, bien qu'il y ait de multiples façons de dépenser une sortie `P2TR`, seule celle qui est utilisée doit être révélée à la dépense, permettant ainsi aux alternatives inutilisées de rester privées. Par exemple, grâce à l'agrégation des clés Schnorr, la clé publique $P$ peut elle-même être une clé agrégée, représentant éventuellement un multisig. `P2TR` est une sortie SegWit de version 1, ce qui signifie que les signatures pour les entrées `P2TR` sont stockées dans le témoin d'une transaction, et non dans le `ScriptSig`. Les adresses `P2TR` utilisent un encodage `Bech32m` et commencent par `bc1p`.

&nbsp;

**P2WPKH -** `P2WPKH` est le sigle pour *Pay to Witness Public Key Hash* (en français « payer au témoin du hachage de la clé publique »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2WPKH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script est similaire à `P2PKH` (Pay to Public Key Hash), en ce sens qu'il verrouille également des bitcoins sur la base du hachage d'une clé publique, c’est-à-dire d’une adresse de réception. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Dans le cadre de `P2WPKH`, les informations du script de signature (`ScriptSig`) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée `Witness` (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (*Segragated Witness*). Cette technique présente l'avantage de réduire la taille des données de transaction dans le corps principal, tout en conservant les informations de script nécessaires à la validation dans une section séparée. Par conséquent, les transactions `P2WPKH` sont généralement moins coûteuses en termes de frais par rapport aux transactions Legacy. Les adresses `P2WPKH` sont écrites en utilisant l'encodage `Bech32`, ce qui contribue à une écriture plus concise et moins sujette aux erreurs typographiques grâce à la somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par `bc1q`, ce qui permet de les distinguer facilement des adresses de réception Legacy. `P2WPKH` est une sortie SegWit de version 0.

&nbsp;

**P2WSH -** `P2WSH` est le sigle pour *Pay to Witness Script Hash* (en français « payer au témoin du hachage du script »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2WSH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script est similaire à `P2SH` (*Pay to Public Script Hash*), en ce sens qu'il verrouille également des bitcoins sur la base du hachage d'un script. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Pour dépenser les bitcoins sur ce type de script, le bénéficiaire doit fournir le script d'origine, appelé `RedeemScript`, ainsi que les signatures requises. Ce mécanisme permet d'implémenter des conditions de dépense plus sophistiquées, telles que des multisig. Dans le cadre de `P2WSH`, les informations du script de signature (`ScriptSig`) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée `Witness` (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (*Segragated Witness*). Cette technique présente l'avantage de réduire la taille des données de transaction dans le corps principal, tout en conservant les informations de script nécessaires à la validation dans une section séparée. Par conséquent, les transactions `P2WSH` sont généralement moins coûteuses en termes de frais par rapport aux transactions `P2SH`. Les adresses `P2WSH` sont écrites en utilisant l'encodage `Bech32`, ce qui contribue à une écriture plus concise et moins sujette aux erreurs typographiques grâce à la somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par `bc1q`, ce qui permet de les distinguer facilement des adresses de réception Legacy. `P2WSH` est une sortie SegWit de version 0.























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**Q**</div>

&nbsp;


























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**R**</div>

&nbsp;

































&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**S**</div>

&nbsp;


































&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**T**</div>

&nbsp;




























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**U**</div>

&nbsp;


























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**V**</div>

&nbsp;




























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**W**</div>

&nbsp;






























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**X**</div>

&nbsp;

























&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**Y**</div>

&nbsp;
































&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">**Z**</div>

&nbsp;


































































