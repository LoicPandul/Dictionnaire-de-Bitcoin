# <div align="center">Le Dictionnaire de Bitcoin 2024</div>

<div align="center">

*Tout le vocabulaire technique de Bitcoin et de son environnement.*

Loïc Morel

<img src="/dictionnaire/images/Logo%20Pandul%20NOIR%20point%20bleu.png" width="200">


</div>

&nbsp;

&nbsp;



# <div align="center">Version en ligne</div>

Afin de naviguer facilement dans *Le Dictionnaire de Bitcoin* sur cette version en ligne, vous pouvez utiliser la commande **ctrl + F** ou **commande + F**.

Vous lisez actuellement la version en ligne du livre *Le Dictionnaire de Bitcoin*, un ouvrage rédigé par Loïc Morel, publié sous licence [CC-BY-NC-SA 4.0](/README.md#licence-et-réutilisation). Si ce projet vous plait, vous êtes libre d'y [contribuer pour l'améliorer](/README.md#demandes-de-modification-et-contributions). Vous pouvez également me soutenir en achetant la version imprimée et brochée de cet ouvrage sur Amazon.fr.

Merci et bonne lecture !

&nbsp;

&nbsp;


# <div align="center">Sommaire</div>




&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


# <div align="center">A</div>

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

<table align="center">
  <tr>
    <td align="center" width="600">
      <img src="/dictionnaire/images/Arbre%20de%20Merkle.png" width="600"><br/>
    </td>
  </tr>
</table>

Cette structure permet de vérifier rapidement si une transaction spécifique est incluse dans un bloc donné sans avoir à analyser l'ensemble des transactions. Par exemple, si je dispose seulement de la racine de Merkle et que je souhaite vérifier que la `TX 7` fait bien partie de l'arbre, j'aurai uniquement besoin des preuves suivantes :
* `TX 7` ;
* `HASH 8` ;
* `HASH 5-6` ;
* `HASH 1-2-3-4`.
Grâce à ces quelques informations, je suis en capacité de calculer les nœuds intermédiaires jusqu'à la racine de Merkle.

<table align="center">
  <tr>
    <td align="center" width="600">
      <img src="/dictionnaire/images/Arbre%20de%20Merkle%202.png" width="600"><br/>
    </td>
  </tr>
</table>

Les arbres de Merkle sont notamment utilisés pour les nœuds légers, dits « SPV Node », qui ne conservent que les entêtes de blocs, mais pas les transactions. On retrouve également cette structure dans le protocole UTREEXO, une structure permettant de condenser l'UTXO set des nœuds, et dans le MAST Taproot.

>*L'arbre de Merkle porte le nom de Ralph Merkle, un cryptographe pionnier qui a conçu cette structure en 1979. Un arbre de Merkle peut également être nommé « arbre de hachage ». En anglais, on dit « Merkle Tree » ou « Hash Tree ».*

&nbsp;

**ASIC (CIRCUIT INTÉGRÉ SPÉCIFIQUE À UNE APPLICATION) -** Un ASIC est un composant électronique conçu pour exécuter une fonction spécifique avec une efficacité optimale. Dans le contexte du minage de Bitcoin, les ASIC sont des circuits intégrés spécialisés qui effectuent des opérations de hachage à haute vitesse et faible consommation d'énergie. Ils sont spécialisés dans l'exécution de la fonction de hachage `SHA256` utilisée dans le mécanisme de la preuve de travail. L'ASIC est initialement le nom de la puce. Par extension, l'acronyme « ASIC » vise souvent à désigner également la machine qui héberge cette puce. Ainsi, les ordinateurs spécialisés dans le minage de Bitcoin sont parfois appelés des « ASIC », ou bien des « mineurs ». Les ASIC ont progressivement remplacé les autres méthodes de minage, telles que l'utilisation de processeurs (CPU) et de cartes graphiques (GPU), en raison de leur efficacité énergétique supérieure et de leur taux de hachage bien plus élevé.
>*L'acronyme « ASIC » désigne en anglais « Application-Specific Integrated Circuit ». En français, ce terme peut être traduit par « Circuit intégré spécifique à une application ».*

&nbsp;

&nbsp;



# <div align="center">B</div>

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



# <div align="center">C</div>

&nbsp;

**CANAL DE PAIMENT -** 

&nbsp;

**CHARGE UTILE (PAYLOAD) -** C

&nbsp;

**CHIFFRER -** C

&nbsp;

**CIBLE DE DIFFICULTÉ -** Le facteur de difficulté, aussi connu sous le nom de cible de difficulté, est un paramètre crucial dans le mécanisme de consensus par preuve de travail (Proof of Work, PoW) utilisé par Bitcoin. La cible représente une valeur numérique qui détermine la difficulté pour les mineurs de résoudre un problème cryptographique spécifique, appelé preuve de travail, lors de la création d'un nouveau bloc dans la blockchain. La cible de difficulté est un nombre ajustable de 256 bits (64 octets) déterminant une limite d’acceptabilité pour le hachage de l’entête des blocs. Autrement dit, pour qu’un bloc soit valide, le hachage de son entête avec `SHA256d` (double `SHA256`) doit être numériquement inférieur ou égal à la cible de difficulté. La preuve de travail consiste à modifier le champ `nonce` de l'entête du bloc ou de la transaction coinbase jusqu'à ce que le hachage résultant soit inférieur à la valeur cible. Cette cible est ajustée tous les 2016 blocs (environ toutes les deux semaines), lors d'un évènement que l'on appelle « ajustement ». Le facteur de difficulté est recalculé en fonction du temps qu'il a fallu pour miner les 2016 blocs précédents. Si le temps total est inférieur à deux semaines, la difficulté augmente en ajustant la cible à la baisse. Si le temps total est supérieur à deux semaines, la difficulté diminue en ajustant la cible à la hausse. L’objectif est de conserver un temps de minage par bloc moyen à 10 minutes. Ce temps entre chaque bloc permet d'éviter les divisions du réseau Bitcoin, résultant en un gaspillage de la puissance de calcul. La cible de difficulté se trouve dans chaque entête de bloc, au sein du champ `nBits`. Puisque ce champ est réduit à 32 bits et que la cible fait en réalité 256 bits, la cible est compactée dans un format scientifique moins précis.

> *La cible de difficulté est parfois également nommée « facteur de difficulté ». Par extension, on peut l'évoquer avec son encodage dans les entêtes de bloc avec le terme « nBits ».*

&nbsp;

**CLÉ ÉTENDUE -** Suite de caractère qui combine une clé (publique ou privée), son code de chaîne associé et une série de métadonnées. Une clé étendue rassemble en une seule chaîne de caractère tous les éléments nécessaires à la dérivation de clés enfants. Elles sont utilisées dans les portefeuilles déterministes et hiérarchiques, et peuvent être de deux types : une clé publique étendue (utilisée pour dériver des clés publiques enfants) ou une clé privée étendue (utilisée pour dériver à la fois des clés privées et des clés publiques enfants). Une clé étendue inclut donc plusieurs données différentes, décrites au sein du BIP32, dans l'ordre : 
* Le préfixe. `prv` et `pub` sont des HRP permettant d'indiquer si l'on a à faire à une clé privée étendue (`prv`) ou à une clé publique étendue (`pub`). La première lettre du préfixe permet, elle, de désigner la version de la clé étendue : 
	* `x` permet d'indiquer un objectif Legacy ou SegWit V1 sur Bitcoin ;
	* `t` permet d'indiquer un objectif Legacy ou SegWit V1 sur Bitcoin Testnet ;
	* `y` permet d'indiquer un objectif Nested SegWit sur Bitcoin ;
	* `u` permet d'indiquer un objectif Nested SegWit sur Bitcoin Testnet ;
	* `z` permet d'indiquer un objectif SegWit V0 sur Bitcoin ;
	* `v` permet d'indiquer un objectif SegWit V0 sur Bitcoin Testnet.
* La profondeur, qui indique le nombre de dérivations intervenues depuis la clé maîtresse pour arriver jusqu'à la clé étendue ;
* L'empreinte du parent. Cela représente les 4 premiers octets du `HASH160` de la clé publique parent ;
* L'index. C'est le numéro de la paire parmi ses sœurs dont est issue la clé étendue ;
* Le code de chaîne ;
* Un octet de rembourrage si c'est une clé privée `0x00` ;
* La clé privée ou la clé publique ;
* Une somme de contrôle. Elle incarne les 4 premiers octets du `HASH256` de tout le reste de la clé étendue.

Dans la pratique, la clé publique étendue est utilisée pour générer des adresses de réception et pour observer les transactions d'un compte, sans exposer les clés privées associées. Cela peut permettre, par exemple, la création d'un portefeuille dit « watch-only ». Il est toutefois important de noter que la clé publique étendue est une information sensible pour la confidentialité de l'utilisateur, car sa divulgation peut permettre à des tiers de tracer les transactions et de visualiser le solde du compte associé.

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

**CODE DE PAIMENT RÉUTILISABLE -** 

&nbsp;

**COINJOIN -** Le CoinJoin est une technique permettant de casser le traçage des bitcoins. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction CoinJoin. Les transactions CoinJoin permettent d'améliorer la protection de la vie privée des utilisateurs de Bitcoin en rendant l'analyse des transactions plus difficile pour les observateurs extérieurs. Cette structure permet la combinaison de plusieurs transactions indépendantes en une seule transaction, rendant difficile la détermination des liens entre les adresses d'entrée et de sortie. Le fonctionnement général du CoinJoin est le suivant : différents utilisateurs souhaitant mixer déposent un montant en input d'une transaction. Ces inputs ressortiront en différents outputs de même montant. À la sortie de la transaction, il est donc impossible de déterminer quel output appartient à quel utilisateur. Il n'y a techniquement aucun lien entre les entrées et les sorties de la transaction CoinJoin. Le lien entre chaque utilisateur et chaque UTXO est cassé, de la même manière que l'historique de chaque pièce.

<table align="center">
  <tr>
    <td align="center" width="600">
      <img src="/dictionnaire/images/Sch%C3%A9ma%20coinjoin%20wp.png" width="600"><br/>
    </td>
  </tr>
</table>

Pour permettre le CoinJoin sans qu'aucun utilisateur ne perde la main sur ses fonds à aucun moment, la transaction est d'abord construite par un coordinateur puis transmise à chaque utilisateur. Chacun d'eux signe alors la transaction de son côté en vérifiant qu'elle lui convient, puis toutes les signatures sont ajoutées à la transaction. Si un utilisateur ou le coordinateur tente de voler les fonds des autres en modifiant les outputs de la transaction CoinJoin, alors les signatures seront invalides et la transaction sera refusée par les nœuds. Ce mécanisme augmente la confidentialité des transactions sans nécessiter de modifications du protocole Bitcoin. Des implémentations spécifiques de CoinJoin, telles que Whirlpool, JoinMarket ou Wabisabi, proposent des solutions pour faciliter le processus de coordination entre les participants et renforcer l'efficacité de la transaction CoinJoin. Exemple de transaction coinjoin : https://mempool.space/fr/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2

> *Le terme de « CoinJoin » ne dispose pas de traduction française. Certains bitcoiners utilisent également les termes de « mix », de « mixing » ou encore de « mixage » pour évoquer la transaction CoinJoin. Selon moi, cette utilisation est une erreur puisque le « mixage » évoque plutôt l'activité d'un acteur central qui mélange des pièces. Cela n'a rien à voir avec le CoinJoin où l'utilisateur ne perd à aucun moment la main sur ses bitcoins durant le processus. Toutefois, ces termes sont globalement admis, même s'ils peuvent parfois porter à confusion.*


&nbsp;

**CONCATÉNATION -** La concaténation, dans le contexte de la cryptographie et des systèmes informatiques, désigne le processus d'assemblage de deux opérandes, en les mettant bout à bout, formant ainsi une nouvelle chaîne de caractères ou de données. Cette opération se note généralement avec un symbole de deux barres verticales $\Vert$, ou avec le symbôle $\circ$. Par exemple, la concaténation de $45$ avec $87$ sera égale à $4587$. Nous noterons : $45 \Vert 87 = 4587$. On a mis bout à bout les deux opérandes.

&nbsp;

**CONDENSAT (HASH) -** Le condensat, dans le contexte de la cryptographie, désigne le résultat (ou l'output) produit par l'application d'une fonction de hachage cryptographique à un ensemble de données. Le condensat est une chaîne de caractères de taille fixe généralement représentée sous forme d'une série de chiffres et de lettres en notation hexadécimale (base 16). Ce résultat a la particularité d'être presque unique et spécifique aux données d'entrée, de sorte qu'un changement minime dans l'entrée produira un condensat complètement différent. Les fonctions de hachage cryptographiques sont conçues pour être unidirectionnelles et résistantes aux collisions, rendant très difficile de retrouver les données initiales à partir du condensat ou de trouver deux entrées distinctes produisant le même condensat.

> *Voir la définition de « fonction de hachage » pour plus de précisions sur ce sujet.*

&nbsp;

**CONFIRMATION -**

&nbsp;

**CONSENSUS -**

&nbsp;

**COURBE ELLIPTIQUE -** Dans le contexte de la cryptographie, une courbe elliptique est une courbe algébrique définie par une équation de la forme $y^2 = x^3 + ax + b$. Ces courbes sont utilisées dans la cryptographie à courbes elliptiques (ECC), qui est une méthode de cryptographie à clé publique permettant de créer des algorithmes de chiffrement, de signature numérique et d'échange de clés. Dans le contexte de Bitcoin, l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm) ou le protocole de Schnorr sont utilisés avec la courbe `secp256k1`. Cette courbe a été choisie pour ses propriétés de performance et de sécurité. Ces algorithmes sont utilisés pour générer des clés publiques à partir de clés privées, ainsi que pour signer des transactions, et donc débloquer des bitcoins.

&nbsp;

**CRYPTER -** Ce terme n'existe pas. On dit « chiffrer ».












&nbsp;

&nbsp;



# <div align="center">D</div>

&nbsp;

**DISTRIBUÉ -** Attribut d'un réseau informatique dans lequel le pouvoir de décision et le contrôle sont répartis de manière équitable entre tous les participants du réseau. Cette répartition garantit la résilience du système. On parle également de réseau pair-à-pair. Contrairement à un réseau décentralisé, où le pouvoir est fragmenté et dispersé parmi plusieurs entités, mais où certaines autorités centrales demeurent dotées d'un pouvoir supérieur à celui des utilisateurs, un réseau distribué élimine l'autorité centrale en confiant la gestion et le contrôle aux utilisateurs eux-mêmes. Bitcoin est un exemple de réseau distribué. Comme protocole de cash électronique pair-à-pair, Bitcoin se distingue par son absence de hiérarchie et d'autorité centrale. La tenue du consensus, la vérification des transactions et l'émission de nouvelles unités monétaires sont réalisées par les utilisateurs du réseau. Cette structure distribuée assure la résilience et la résistance à la censure du système, rendant très difficile pour une entité unique de contrôler ou de manipuler le réseau.

> *Certaines personnes parlent de Bitcoin comme d'un système décentralisé. En effet, il n'est pas rare d'observer une interchangeabilité de ces deux termes. Un synonyme plus évocateur de l'adjectif « distribué » pourrait être « pair-à-pair », parfois abrégé « P2P », le sigle de la traduction anglaise « Peer-to-Peer ».*

&nbsp;

**DIVISION -**

&nbsp;

**DOUBLE-DÉPENSE -** 




































&nbsp;

&nbsp;



# <div align="center">E</div>

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

**EXTRA-NONCE -** 
























&nbsp;

&nbsp;


# <div align="center">F</div>

&nbsp;

**FIAT -**

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

**FORK -**

















&nbsp;

&nbsp;



# <div align="center">G</div>

&nbsp;


**GENÈSE (BLOC) -** Le bloc de genèse Bitcoin, également connu sous le nom de bloc Genesis ou bloc #0, est le premier bloc du système Bitcoin. Il incarne le lancement concret de Bitcoin. Le bloc de genèse a été créé par le fondateur anonyme de Bitcoin, Satoshi Nakamoto, le 3 janvier 2009. Son hash est [`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`](https://mempool.space/fr/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f). Ce bloc contient seulement une transaction coinbase qui génère 50 bitcoins en récompense pour le mineur (dans ce cas, Satoshi Nakamoto lui-même). Il est particulièrement significatif en raison de son message incorporé dans la transaction coinbase : `The Times 03/Jan/2009 Chancellor on brink of second bailout for banks`. Cette citation est une référence à un article du journal *The Times*. Le message est interprété comme une critique du système financier traditionnel et de ses dérives, ce qui a en partie motivé la création de Bitcoin en tant qu'alternative. Puisqu’il incarne le tout premier bloc de la blockchain Bitcoin, le bloc de genèse ne possède évidemment pas de champ contenant le hachage du bloc antérieur (car il n'y en pas). Par ailleurs, les 50 bitcoins générés en récompense dans ce bloc ne sont pas dépensables au niveau protocolaire.

> *J’aime différencier les bitcoins perdus pour cause protocolaire, des bitcoins perdus pour cause applicative. Par définition, les bitcoins perdus au niveau protocolaire ne seront jamais dépensables, sauf à refaire la preuve de travail postérieure. J’y inclus notamment les pertes liées à la non-réclamation de la récompense coinbase, ou celles liées à un script OP_RETURN. Au contraire, les bitcoins perdus au niveau applicatif, souvent pour cause de perte de clés, seront sûrement un jour débloqués à cause des limitations de la cryptographie employée.*

&nbsp;

**GNPA (PRNG) -** 

&nbsp;

**GRAINE (SEED) -** Dans le cadre spécifique d'un portefeuille déterministe hiérarchique Bitcoin, une graine (ou « seed » en anglais) est une information de 512 bits issue d'un aléa. Elle permet de générer de manière déterministe et hiérarchique un ensemble de clés privées, et leurs clés publiques correspondantes, pour un portefeuille Bitcoin. La graine (seed) est souvent confondue avec la phrase de récupération en elle-même. Pourtant, c'est une information différente. La graine est obtenue en appliquant la fonction `PBKDF2` sur la phrase mnémonique et sur l’éventuelle passphrase. La graine a été inventée avec le BIP32 qui définit les bases du portefeuille déterministe hiérarchique. Dans ce standard, la graine mesurait 128 bits. Cela permet de dériver toutes les clés d'un portefeuille depuis une information unique, contrairement aux portefeuilles JBOK (Just a Bunch Of Keys) qui nécessitent de réaliser de nouvelles sauvegardes pour toute clé générée. Le BIP39 est par la suite venu proposer un encodage de cette graine, afin de simplifier sa lecture par l'humain. Cet encodage se fait sous la forme d'une phrase, que l'on nomme généralement phrase mnémonique ou phrase de récupération. Ce standard permet d'éviter les erreurs au niveau de la sauvegarde de la graine, notamment grâce à l'utilisation d'une somme de contrôle.

De manière plus générale, en cryptographie, une graine est un morceau de données aléatoires utilisé comme point de départ pour générer des clés cryptographiques, des chiffrements ou des séquences aléatoires. La qualité et la sécurité de nombreux processus cryptographiques dépendent de la nature aléatoire et de la confidentialité de la graine.

> *La traduction anglaise de « graine » est « seed ». En français, beaucoup utilisent directement le mot anglais pour désigner la graine.*

&nbsp;

**GUI -** C















&nbsp;

&nbsp;



# <div align="center">H</div>

&nbsp;

**HALVING -** Le terme « halving » (division par deux) fait référence à un événement programmé qui réduit de moitié la récompense attribuée aux mineurs pour chaque bloc miné via la subvention de bloc. Cette réduction s'applique spécifiquement à la partie de la subvention de bloc constituée de nouveaux bitcoins créés ex-nihilo. Le halving a été conçu par Satoshi Nakamoto, le créateur de Bitcoin, comme un mécanisme permettant de contrôler l'inflation et d'assurer un approvisionnement limité en bitcoins. La récompense de bloc initiale était de 50 bitcoins, et le halving se produit tous les 210 000 blocs minés, ce qui prend environ quatre ans. Le premier halving a eu lieu en novembre 2012, réduisant la récompense de bloc à 25 bitcoins, et les suivants ont réduit la récompense à 12,5, puis 6,25 bitcoins respectivement. Les halvings continueront à se produire jusqu'à ce que la récompense de bloc atteigne zéro, moment auquel l'offre maximale de 21 millions de bitcoins aura été (presque) atteinte. Le prochain halving de Bitcoin devrait avoir lieu aux alentours du printemps 2024, bien que la date exacte puisse légèrement varier en fonction du temps de minage des blocs. À ce moment-là, la récompense de bloc sera réduite de 6,25 à 3,125 bitcoins. Ce sera le quatrième halving de l'histoire de Bitcoin. Les bitcoiners étudient attentivement les effets des halvings sur le système, car les incitations pour les mineurs diminuent avec le temps. À mesure que les récompenses de bloc baissent, les frais de transaction deviennent une source de revenus de plus en plus importante pour les mineurs, ce qui garantit leur motivation à continuer à participer à la preuve de travail.

&nbsp;

**HARDFORK -**

&nbsp;

**HARDWARE WALLET -** Un hardware wallet, ou portefeuille matériel, est un dispositif électronique dédié à la sécurisation et à la gestion des clés privées d'un portefeuille Bitcoin. Ces périphériques sont conçus pour procurer une sécurité renforcée par rapport aux portefeuilles logiciels qui résident sur des machines polyvalentes et directement connectées à internet. Les hardwares wallets stockent la phrase mnémonique hors ligne, sur un matériel qui dispose d'une infime surface d'attaque, ce qui l'isole des environnements potentiellement vulnérables. Lorsqu'une transaction est effectuée, le portefeuille matériel signe la transaction à l'intérieur du dispositif lui-même, sans exposer la clé privée à l'extérieur. Une fois la transaction signée, elle est transmise au réseau Bitcoin pour être confirmée et incluse dans la blockchain Bitcoin. Parmi les modèles de hardwares wallets les plus populaires, on peut citer : Ledger, Trezor, Coldcard, Passport, BitBox, Satochip, Jade ou encore SeedSigner (liste non exhaustive).

> *Le hardware wallet peut être exprimé de différentes manières en français. Certains parlent de « portefeuille matériel » ou bien de « portefeuille froid ». Certains bitcoiners préfèrent que l'on emploie le terme de « périphérique de signature », ou « signing device » en anglais, afin d'éviter de faire penser que les bitcoins se trouvent physiquement dans le portefeuille.*

&nbsp;

**HD -** 

&nbsp;

**HMAC-SHA512 -** `HMAC-SHA512` est l’acronyme de « Hash-based Message Authentication Code - Secure Hash Algorithm 512 ». C’est un algorithme cryptographique utilisé pour vérifier l'intégrité et l'authenticité des messages échangés entre deux parties. Il combine la fonction de hachage cryptographique `SHA512` (Secure Hash Algorithm 512) avec une clé secrète partagée pour générer un code d'authentification de message (MAC) unique pour chaque message. Dans le contexte de Bitcoin, l'utilisation naturelle de `HMAC-SHA512` est légèrement dérivée. On utilise cet algorithme dans le processus de dérivation déterministe et hiérarchique de l'arbre de clés cryptographiques d'un portefeuille. `HMAC-SHA512` est notamment utilisé pour passer de la graine (seed) à la clé maîtresse, puis pour chaque dérivation d’une paire parent vers des paires enfants. On retrouve également cet algorithme au sein d'un autre algorithme de dérivation, nommé `PBKDF2`, utilisé pour passer de la phrase de récupération et de la passphrase à la graine.

&nbsp;

**HASHLOCKS -** 

&nbsp;

**HORODATAGE (TIMESTAMP) -** L'horodatage, ou « timestamp » en anglais, est un mécanisme qui consiste à associer un repère temporel précis à un événement, une donnée ou un message. Dans le contexte de la cryptographie et des systèmes informatiques, l'horodatage sert à déterminer l'ordre chronologique des opérations et à vérifier l'intégrité des données en fonction du temps. Dans le cas spécifique de Bitcoin, les horodatages jouent un rôle crucial pour établir la chronologie des transactions et des blocs. Chaque bloc dans la blockchain contient un horodatage indiquant le moment approximatif de sa création. Satoshi Nakamoto parle même d'un « serveur d'horodatage », dans son White Paper, pour décrire ce que l'on appellerait aujourd'hui la « blockchain ». Le rôle de l'horodatage sur Bitcoin est de déterminer la chronologie des transactions, afin de pouvoir déterminer, sans l'intervention d'une autorité centrale, quelle transaction est arrivée en première. Ce mécanisme permet à chaque utilisateur de vérifier la non-existence d'une transaction par le passé, et donc d'éviter qu'un utilisateur malintentionné opère une double dépense. Ce mécanisme est justifié par Satoshi Nakamoto dans son White Paper par la célèbre phrase : « *Le seul moyen pour confirmer l’absence d’une transaction est d’être au courant de toutes les transactions.* » Cette norme est établie sur l'heure Unix, qui représente le total de secondes passées depuis le premier janvier 1970.

> *L'horodatage des blocs est relativement flexible sur Bitcoin, car pour qu'un horodatage soit considéré comme valide, il est simplement nécessaire qu'il soit plus grand que le temps médian des 11 blocs qui le précèdent.*

&nbsp;

**HRP -**

&nbsp;

**HTLC -** 



















&nbsp;

&nbsp;


# <div align="center">I</div>

&nbsp;

**Initial Block Download (IBD) -** Fait référence au processus par lequel un nœud télécharge et vérifie la blockchain depuis le bloc Genesis, et se synchronise aux autres nœuds du réseau Bitcoin. L'IBD doit être réalisée au lancement d'un nouveau nœud complet Bitcoin. Lors du lancement de cette synchronisation initiale, le nœud ne dispose d'aucune information sur les transactions précédentes. Il télécharge donc chaque bloc depuis les autres nœuds du réseau, vérifie sa validité, puis l'ajoute à sa version locale de la blockchain. Il convient de noter que l'IBD peut être longue et exigeante en ressources en raison de la taille croissante de la blockchain et de l'UTXO set. La rapidité de son exécution dépend des capacités de calcul de l'ordinateur qui héberge le nœud, de ses capacités en RAM, de la vitesse du dispositif de stockage et de la bande passante. Pour vous donner une idée, si vous disposez d'une connexion internet puissante, et que le nœud est hébergé sur le dernier MacBook avec beaucoup de RAM, l'IBD ne prendra que quelques heures. En revanche, si vous utilisez un micro-ordinateur comme un Raspberry Pi, l'IBD pourra prendre une semaine ou plus.

> *En français, il est globalement admis de parler directement d'un(e) IBD. La traduction parfois employée est « synchronisation initiale », ou « téléchargement initial des blocs ».*

&nbsp;

**INDEX (NUMÉRO DE CLÉ) -** Dans le contexte d'un portefeuille HD (Hierarchical Deterministic), fait référence au numéro séquentiel attribué à une clé enfant générée à partir d'une clé parent. Cet index est utilisé en combinaison avec la clé parent et le code chaîne parent pour dériver de manière déterministe des clés enfants uniques. Il permet une organisation structurée et la génération reproductible de multiples paires de clés enfants soeur depuis une même clé parent. C’est un entier de 32 bits utilisé dans la fonction de dérivation `HMAC-SHA512`. Ce nombre permet donc de différencier les clés enfants sœurs au sein d’un portefeuille HD.

&nbsp;

**INPUT -** Voir définition du terme « Entrée ».
















&nbsp;

&nbsp;


# <div align="center">J</div>

&nbsp;

**JBOK (PORTEFEUILLE) -** Les portefeuilles JBOK, acronyme pour « Just a Bunch Of Keys » (en français « juste un trousseau de clés »), font référence aux portefeuilles Bitcoin initiaux qui stockaient un ensemble de paires de clés générées de manière indépendante et pseudo-aléatoire. Contrairement aux portefeuilles HD (Hierarchical Deterministic) modernes, qui génèrent des clés de manière déterministe et hiérarchique à partir d'une graine unique, les portefeuilles JBOK ne présentaient aucune relation hiérarchique ou déterministe entre les clés. Elles étaient toutes indépendantes les unes des autres. En raison de leur gestion moins efficace et de la difficulté de sauvegarde, ces portefeuilles sont devenus obsolètes et ont été spontanément remplacés par des solutions HD plus avancées, comme standardisées dans le BIP32.

&nbsp;













&nbsp;

&nbsp;


# <div align="center">K</div>

&nbsp;

**KYC -** 













&nbsp;

&nbsp;


# <div align="center">L</div>

&nbsp;

**LEVELDB -** 

&nbsp;

**LIGHTNING NETWORK -** Protocole de couche supérieure, construit au-dessus du protocole Bitcoin, visant à permettre des transactions rapides et à faible coût. Il permet la création de canaux de paiement entre les participants, au sein desquels les transactions peuvent être effectuées presque instantanément et avec des frais minimes, sans avoir à enregistrer chaque transaction individuellement sur la blockchain. Les canaux peuvent rester ouverts quasi indéfiniment, et ne nécessitent des transactions sur la blockchain que lors de leur ouverture et de leur clôture. Le Lightning Network vise à améliorer la scalabilité de Bitcoin et à rendre possible son utilisation pour des paiements de faible valeur. Toutefois, le Lightning Network n’est pas une solution parfaite. Ce protocole a une tendance naturelle à la centralisation sur de gros nœuds institutionnels. Il peut également être difficile de l’utiliser durant les périodes de très fortes congestions, comme on a pu le voir durant l’épisode BRC-20 en mai 2023. Aussi, sa structure rend très complexe la confidentialité des paiements.

&nbsp;

**LOCKTIME -**

&nbsp;

**LOGARITHME DISCRET (PROBLÈME) -** Le logarithme discret est un problème mathématique qui joue un rôle central en cryptographie à clé publique. Dans un groupe cyclique d’ordre $q$, avec un générateur $g$, si l'on a une équation de la forme $g^x = h$, alors $x$ est appelé le logarithme discret de $h$ par rapport à la base $g$, modulo $q$. En termes simples, il s’agit de déterminer l’exposant $x$ lorsqu’on connaît $g$, $h$, et $q$. Le logarithme discret est donc la réciproque de l'exponentielle dans un groupe cyclique fini. Cependant, pour de grandes valeurs de $q$, résoudre le problème du logarithme discret est considéré comme algorithmiquement difficile. Cette propriété est exploitée pour assurer la sécurité de nombreux protocoles cryptographiques, tels que le protocole de Diffie-Hellman pour l'échange de clés. Le logarithme discret est aussi utilisé dans la cryptographie à courbes elliptiques (ECC), entre autres dans l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm). Dans le contexte des courbes elliptiques, le problème du logarithme discret s'étend à la recherche d'un scalaire $k$ tel que $k \cdot G = K$, où $G$ et $K$ sont des points sur la courbe, et $\cdot$ représente l'opération de multiplication de points. Dans le contexte de Bitcoin, les transactions standard utilisent soit ECDSA, soit le protocole de Schnorr, afin de bloquer des UTXO. Ils reposent tous deux sur l’impossibilité de calculer le logarithme discret.























&nbsp;

&nbsp;



# <div align="center">M</div>

&nbsp;

**MALLÉABILITÉ (TRANSACTION)-** 

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


# <div align="center">N</div>

&nbsp;

**NESTED SEGWIT -** Standard de scripts utilisés pour envelopper des scripts SegWit natifs, au sein d'un script P2SH. Les scripts Nested SegWit ont été inventé au lancement de SegWit pour faciliter son adoption. Ils permettent d'utiliser ce nouveau standard, même sur des wallets pas encore compatibles nativement avec SegWit. C'est une sorte de script de transition vers la nouvelle norme. Aujourd'hui, il n'est donc plus très pertinent d'utiliser ce type de scripts SegWit wrappés, puisque la plupart des wallets ont implémenté du SegWit natif (voir « P2SH-P2WPKH »).

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



# <div align="center">O</div>

&nbsp;

**OFFCHAIN -** 

&nbsp;

**ONCHAIN -** 

&nbsp;

**OPCODE -**

&nbsp;

**OP_RETURN** -

&nbsp;

**ORPHELIN (BLOC) -**

&nbsp;

**OU EXCLUSIF -** Voir la définition du terme « Xor ».

&nbsp;

**OUTPUT -** Voir définition du terme « Sortie ».








&nbsp;

&nbsp;


# <div align="center">P</div>

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

**P2SH-P2WPKH** - `P2SH-P2WPKH` est le sigle pour *Pay to Script Hash - Pay to Witness Public Key Hash* (en français « payer au hachage du script - payer au témoin du hachage de la clé publique »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO, également connu sous le nom de « Nested SegWit ». `P2SH-P2WPKH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script décrit un `P2WPKH` enveloppé au sein d'un `P2SH`. Il verrouille des bitcoins sur la base du hachage d'une clé publique. La différence avec `P2WPKH` simple est que le script est enveloppé dans le `redeemScript` d'un `P2SH` classique. Ce script a été créé au lancement de SegWit pour faciliter son adoption. Il permet d'utiliser ce nouveau standard, même sur des wallets pas encore compatibles nativement avec SegWit. C'est une sorte de script de transition vers la nouvelle norme. Aujourd'hui, il n'est donc plus très pertinent d'utiliser ce type de scripts SegWit wrappés, puisque la plupart des wallets ont implémenté du SegWit natif. Les adresses `P2SH-P2WPKH` sont écrites en utilisant l'encodage `Base58Check` et commencent toujours par `3`, comme n'importe quelle adresse `P2SH`.

&nbsp;

**P2SH-P2WSH** - `P2SH-P2WSH` est le sigle pour *Pay to Script Hash - Pay to Witness Script Hash* (en français « payer au hachage du script - payer au témoin du hachage du script »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO, également connu sous le nom de « Nested SegWit ». `P2SH-P2WSH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script décrit un `P2WSH` enveloppé au sein d'un `P2SH`. Il verrouille des bitcoins sur la base du hachage d'un script. La différence avec `P2WSH` simple est que le script est enveloppé dans le `redeemScript` d'un `P2SH` classique. Ce script a été créé au lancement de SegWit pour faciliter son adoption. Il permet d'utiliser ce nouveau standard, même sur des wallets pas encore compatibles nativement avec SegWit. C'est une sorte de script de transition vers la nouvelle norme. Aujourd'hui, il n'est donc plus très pertinent d'utiliser ce type de scripts SegWit wrappés, puisque la plupart des wallets ont implémenté du SegWit natif. Les adresses `P2SH-P2WSH` sont écrites en utilisant l'encodage `Base58Check` et commencent toujours par `3`, comme n'importe quelle adresse `P2SH`.

&nbsp;

**P2TR -** `P2TR` est le sigle pour *Pay to Taproot* (en français « payer à la racine »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2TR` a été introduit avec l'implémentation de Taproot en novembre 2021. `P2TR` utilise le protocole de Schnorr pour agréger des clés cryptographiques, ainsi que des arbres de Merkle pour des scripts alternatifs, connus sous le nom de MAST (*Merkelized Alternative Script Tree*). Contrairement aux transactions traditionnelles où les conditions de dépense sont exposées publiquement (parfois à la réception, parfois à la dépense) `P2TR` permet de masquer des scripts complexes derrière une seule clé publique apparente. Techniquement, un script `P2TR` verrouille des bitcoins sur une clé publique Schnorr unique, dénommée $K$. Cependant, cette clé $K$ est en réalité un agrégat d'une clé publique $P$ et d'une clé publique $M$, cette dernière étant calculée à partir de la racine de Merkle d'une liste de `ScriptPubKeys`. L'agrégation de clés est réalisée à l'aide du protocole de signature de Schnorr. Les bitcoins verrouillés avec un script `P2TR` peuvent être dépensés de deux manières distinctes : soit en publiant une signature pour la clé publique $P$, soit en satisfaisant l'un des scripts contenus dans l'arbre de Merkle. La première option est appelée « key path » (chemin de clé) et la seconde « script path » (chemin de script). Ainsi, `P2TR` permet aux utilisateurs d'envoyer des bitcoins soit à une clé publique, soit à plusieurs scripts de leur choix. Un autre avantage de ce script est que, bien qu'il y ait de multiples façons de dépenser une sortie `P2TR`, seule celle qui est utilisée doit être révélée à la dépense, permettant ainsi aux alternatives inutilisées de rester privées. Par exemple, grâce à l'agrégation des clés Schnorr, la clé publique $P$ peut elle-même être une clé agrégée, représentant éventuellement un multisig. `P2TR` est une sortie SegWit de version 1, ce qui signifie que les signatures pour les entrées `P2TR` sont stockées dans le témoin d'une transaction, et non dans le `ScriptSig`. Les adresses `P2TR` utilisent un encodage `Bech32m` et commencent par `bc1p`.

&nbsp;

**P2WPKH -** `P2WPKH` est le sigle pour *Pay to Witness Public Key Hash* (en français « payer au témoin du hachage de la clé publique »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2WPKH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script est similaire à `P2PKH` (Pay to Public Key Hash), en ce sens qu'il verrouille également des bitcoins sur la base du hachage d'une clé publique, c’est-à-dire d’une adresse de réception. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Dans le cadre de `P2WPKH`, les informations du script de signature (`ScriptSig`) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée `Witness` (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (*Segragated Witness*). Cette technique présente l'avantage de réduire la taille des données de transaction dans le corps principal, tout en conservant les informations de script nécessaires à la validation dans une section séparée. Par conséquent, les transactions `P2WPKH` sont généralement moins coûteuses en termes de frais par rapport aux transactions Legacy. Les adresses `P2WPKH` sont écrites en utilisant l'encodage `Bech32`, ce qui contribue à une écriture plus concise et moins sujette aux erreurs typographiques grâce à la somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par `bc1q`, ce qui permet de les distinguer facilement des adresses de réception Legacy. `P2WPKH` est une sortie SegWit de version 0.

&nbsp;

**P2WSH -** `P2WSH` est le sigle pour *Pay to Witness Script Hash* (en français « payer au témoin du hachage du script »). C’est un standard de script de transaction utilisé pour établir des conditions de dépenses sur un UTXO. `P2WSH` a été introduit avec l'implémentation de SegWit en août 2017. Ce script est similaire à `P2SH` (*Pay to Public Script Hash*), en ce sens qu'il verrouille également des bitcoins sur la base du hachage d'un script. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Pour dépenser les bitcoins sur ce type de script, le bénéficiaire doit fournir le script d'origine, appelé `RedeemScript`, ainsi que les signatures requises. Ce mécanisme permet d'implémenter des conditions de dépense plus sophistiquées, telles que des multisig. Dans le cadre de `P2WSH`, les informations du script de signature (`ScriptSig`) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée `Witness` (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (*Segragated Witness*). Cette technique présente l'avantage de réduire la taille des données de transaction dans le corps principal, tout en conservant les informations de script nécessaires à la validation dans une section séparée. Par conséquent, les transactions `P2WSH` sont généralement moins coûteuses en termes de frais par rapport aux transactions `P2SH`. Les adresses `P2WSH` sont écrites en utilisant l'encodage `Bech32`, ce qui contribue à une écriture plus concise et moins sujette aux erreurs typographiques grâce à la somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par `bc1q`, ce qui permet de les distinguer facilement des adresses de réception Legacy. `P2WSH` est une sortie SegWit de version 0.

&nbsp;

**PAIR-À-PAIR (P2P) -** Fait référence à un modèle de communication et de distribution de données dans lequel les participants, souvent appelés nœuds ou pairs, partagent leurs ressources (comme des fichiers, de la puissance de traitement, de la bande passante, des actifs…) directement entre eux, sans nécessiter d'intermédiaire centralisé. Dans un système P2P, chaque participant agit simultanément comme client (consommateur de ressources) et serveur (fournisseur de ressources). Dans le contexte de Bitcoin, le terme pair-à-pair revêt une importance particulière. Le réseau Bitcoin fonctionne selon un modèle P2P, où les nœuds sont responsables de la validation des transactions et de la conservation de la blockchain. Cela signifie que, contrairement aux systèmes bancaires traditionnels qui dépendent d'entités centralisées, Bitcoin opère sur une structure distribuée où aucune entité unique ne détient le contrôle. Les nœuds du réseau Bitcoin communiquent entre eux pour diffuser les transactions et les blocs, et trouver un consensus sur l'état du registre.

&nbsp;

**PAPER WALLET (PORTEFEUILLE PAPIER) -** 

&nbsp;

**PASSPHRASE (BIP39) -** Mot de passe optionnel qui, combiné à la phrase de récupération, offre une couche de sécurité supplémentaire pour les portefeuilles Bitcoin déterministes et hiérarchiques. Les portefeuilles HD sont généralement générés à partir d’une phrase de récupération constituée de 12 ou de 24 mots. Cette phrase de récupération est cruciale, car elle permet de restaurer l'ensemble des clés d'un portefeuille en cas de perte. Cependant, elle constitue un point de défaillance unique (SPOF). Si elle est compromise, les actifs sont en danger. C'est là qu'intervient la passphrase. C'est un mot de passe optionnel, choisi par l'utilisateur, qui s'ajoute à la phrase de récupération pour renforcer la sécurité du portefeuille. À ne pas confondre avec un code PIN ou un mot de passe ordinaire, la passphrase joue un rôle dans la dérivation des clés cryptographiques. Elle fonctionne en tandem avec la phrase de récupération, modifiant la graine à partir de laquelle sont générées les clés. Ainsi, même si une personne obtient votre phrase de récupération, sans la passphrase, elle ne peut pas accéder à vos fonds. L'utilisation d'une passphrase crée essentiellement un nouveau portefeuille avec des clés distinctes. Modifier (même légèrement) la passphrase générera un portefeuille différent. La passphrase est arbitraire et peut-être n'importe quelle combinaison de caractères choisie par l'utilisateur. L'utilisation d'une passphrase offre plusieurs avantages. Tout d'abord, elle réduit les risques liés à la compromission de la phrase de récupération en nécessitant un second facteur pour accéder aux fonds. Ensuite, elle peut être utilisée stratégiquement pour créer des portefeuilles d’appât contenant de petites quantités de bitcoins, dans le cas d'une contrainte physique pour voler vos bitcoins. Enfin, son utilisation est intéressante lorsque l’on souhaite maitriser le caractère aléatoire de la génération de la graine du portefeuille HD. La passphrase doit être suffisamment complexe pour résister aux attaques par brute force et doit être sauvegardée de manière fiable. La perte de la passphrase peut entraîner l'incapacité d'accéder aux fonds, tout comme la perte de la phrase de récupération.

> *La passphrase est parfois également nommée : « two-factor seed phrase », « password », « seed extension », « extention word » ou encore « 13ème ou 25ème mot ». Notons qu’il existe deux types de passphrases sur Bitcoin. La plus connue est celle décrite ci-dessus, qui dépend du BIP39, et qui permet de sécuriser tout un portefeuille HD entier. Toutefois, le BIP38 avait également spécifié une manière de sécuriser une clé privée unique à l’aide d’une passphrase. Ce second type de passphrase n’est presque plus utilisé aujourd’hui.* 

&nbsp;

**PATOSHI -** Fait référence à un motif distinct de nonces et d’horodatages observés dans les blocs minés au cours des premiers mois de l'existence de Bitcoin. Ce modèle est soupçonné d'être attribuable à une seule entité ou individu, très probablement Satoshi Nakamoto lui-même, l’inventeur de Bitcoin. Le terme de « Patoshi » est un mot-valise combinant « pattern » et « Satoshi ». Plusieurs analyses des premiers blocs de Bitcoin ont révélé des motifs dans la façon dont les nonces et extra-nonces étaient choisis, et comment les horodatages étaient définis. Ces motifs étaient suffisamment distincts pour suggérer qu'un mineur ou un groupe de mineurs particulier était responsable d'une grande proportion des blocs minés pendant cette période, tout en utilisant un client modifié. Sergio Demian Lerner, un chercheur en informatique, est crédité de la découverte de ce motif en 2013. Lerner a estimé que le mineur Patoshi avait miné environ 1,1 million de bitcoins. Cela a conduit à des spéculations généralisées sur les motivations, l'identité et les intentions actuelles du mineur Patoshi. Certains pensent que Patoshi était Satoshi lui-même, en train de miner des bitcoins pour soutenir et sécuriser le réseau naissant. Il est important de noter que, bien que le motif Patoshi soit largement accepté comme preuve d'une activité de minage précoce concentrée, il n'y a pas de confirmation définitive de l'identité derrière le Patoshi ou de ses intentions.

&nbsp;

**PAYJOIN -** 

&nbsp;

**PAYNYM -** 

&nbsp;

**PBKDF2 -** `PBKDF2` est le sigle de *Password-Based Key Derivation Function 2*. C’est une méthode pour créer des clés cryptographiques à partir d'un mot de passe en utilisant une fonction de dérivation. Elle prend en entrée un mot de passe, un sel cryptographique, et applique de manière itérative une fonction prédéterminée (souvent une fonction de hachage comme `SHA256` ou un `HMAC`) sur ces données. Ce processus est répété de nombreuses fois afin de générer une clé cryptographique. Dans le contexte de Bitcoin, `PBKDF2` est utilisée en conjonction avec la fonction `HMAC-SHA512` pour créer la graine d'un portefeuille déterministe et hiérarchique (seed) à partir d'une phrase de récupération de 12 ou de 24 mots. Le sel cryptographique utilisé dans ce cas est la passphrase BIP39, et le nombre d’itérations est de `2048`.

&nbsp;

**PÉRIMÉ (BLOC) -** 

&nbsp;

**PÉRIODE DE MATURITÉ -** 

&nbsp;

**PHRASE DE RÉCUPÉRATION (MNÉMONIQUE) -** Une phrase de récupération, également parfois nommée comme mnémonique, seed phrase, ou phrase secrète, est une séquence composée habituellement de 12 ou 24 mots, qui est générée de manière pseudo-aléatoire à partir d'une source d'entropie. La séquence pseudo-aléatoire est toujours complétée d'une somme de contrôle (checksum). La phrase mnémonique, conjointement avec une passphrase optionnelle, est utilisée pour dériver de façon déterministe l'intégralité des clés associées à un portefeuille HD (déterministe et hiérarchique). Cela signifie qu’à partir de cette phrase, il est possible de générer et de recréer déterministiquement l'ensemble des clés privées et publiques du portefeuille Bitcoin, et par conséquent d'accéder aux fonds qui y sont associés. La raison d'être de la phrase de récupération est de fournir un moyen de sauvegarde et de récupération des bitcoins qui est à la fois sécurisé et facile à utiliser. Il est impératif de conserver cette phrase en lieu sûr et de manière sécurisée, car toute personne en possession de cette phrase aurait accès aux fonds du portefeuille correspondant. Si elle est utilisée dans le cadre d’un portefeuille classique, et sans passphrase optionnelle, elle constitue souvent un SPOF (point de défaillance unique). La phrase de récupération est donc un encodage de la séquence pseudo aléatoire et de la checksum dans des mots du quotidien afin de faciliter sa notation et sa lisibilité par l’Homme. Elle est construite en fonction du standard BIP39, qui défini et ordonne une liste de 2048 mots utilisés pour cet encodage.

&nbsp;

**POOL DE MINAGE -** Fait référence à un ensemble de mineurs qui collaborent en combinant leur puissance de calcul pour participer à la preuve de travail sur Bitcoin. Ce groupement en une seule organisation est une solution à la difficulté croissante de l'extraction de bitcoins, qui rend trop improbable pour un mineur individuel de rivaliser et de gagner des récompenses de manière stable. Les mineurs au sein d'un pool de minage contribuent avec leur matériel de calcul à la recherche d’une preuve de travail valide requise pour trouver un bloc. Lorsqu'un bloc est miné par le pool, la récompense, qui comprend les bitcoins nouvellement créés ainsi que les frais de transaction inclus dans le bloc, est distribuée parmi les membres du pool. Cette distribution est proportionnelle à la puissance de calcul que chaque mineur a contribué. En joignant leurs forces, les mineurs au sein d'un pool augmentent leurs chances de résoudre un bloc. Cela permet d’assurer une source de revenus plus régulière et prévisible par rapport au minage en solo, où un mineur peut ne pas gagner de récompense pendant de longues périodes. Cela permet de lisser les gains, et donc d’avoir d’une meilleure visibilité sur cette activité industrielle, notamment pour faire face aux différentes charges qu'elle induit.

> *En anglais, on dit « Mining pool ».*

&nbsp;

**PORTE DÉROBÉE (BACKDOOR) -** Une backdoor est un mécanisme secret qui permet de disposer d'un accès privilégié à un système informatique, un logiciel, une fonction, un algorithme ou des données, sans passer par les procédures d'authentification ou de sécurité habituelles. À la différence d'une faille de sécurité, les portes dérobées sont introduites intentionnellement dans le code source par des développeurs malveillants. Elles peuvent être utilisées pour espionner, manipuler ou voler des informations sensibles.

> *Le terme de « porte dérobée » est assez peu utilisé en français. On préfère généralement employer directement la traduction anglaise qui est « backdoor ».*

&nbsp;

**PORTEFEUILLE -** Outil logiciel spécialement conçu pour sécuriser et gérer les clés privées d'un utilisateur. Si le portefeuille est stocké et géré sur un dispositif logiciel lui-même installé sur une machine polyvalente, on parle alors de « portefeuille chaud ». En revanche, s'il est stocké dans un logiciel, lui-même installé sur un dispositif matériel dédié uniquement à cette tâche et non connecté à internet, on parle alors de « portefeuille froid ». Le portefeuille permet notamment d'utiliser les clés privées de l'utilisateur pour signer des transactions et ainsi remplir les conditions permettant la dépense des bitcoins.

> *En français, beaucoup utilisent directement la traduction anglaise « wallet » pour évoquer un portefeuille.*

&nbsp;

**PORTEFEUILLE CHAUD (LOGICIEL) -** Un portefeuille chaud (ou « hot wallet ») est un dispositif logiciel dédié à la sécurisation et à la gestion des clés privées d'un portefeuille Bitcoin. On parle de portefeuille chaud lorsque la phrase de récupération d’un portefeuille Bitcoin est conservée sur un appareil informatique, via un logiciel, qui n’est pas dédié uniquement à une utilisation de Bitcoin et qui est connecté directement à internet. Par exemple, l'application Samourai Wallet sur votre smartphone serait considérée comme un portefeuille chaud.

&nbsp;

**PORTEFEUILLE FROID -** Voir la définition de « Hardware Wallet ».

&nbsp;

**PREUVE DE TRAVAIL -** Mécanisme de protection face aux attaques Sybil, qui se caractérisent par la multiplication de fausses identités, dans le but de prendre un avantage illégitime. Ainsi, la preuve de travail permet d'établir un coût marginal non négligeable à la multiplication des votes sur Bitcoin. La preuve de travail est à la base du protocole de consensus de Nakamoto, qui est le principe utilisé pour établir un accord sur une version unique du registre distribué entre les différents nœuds du réseau. Concrètement, la preuve de travail est la recherche d’une valeur qui, une fois passée dans une fonction mathématique aléatoire, donne un résultat inférieur à un nombre cible. Cette cible de la preuve de travail est ajustée tous les 2016 blocs par les nœuds. C’est ce que l’on appelle l’ajustement de la difficulté. On abaisse le nombre cible pour augmenter la difficulté de minage, ou on l’augmente pour baisser la difficulté, en fonction de l’évolution de la puissance de calcul déployée par les mineurs durant la période précédente. Ce travail effectué par les mineurs est récompensé à chaque bloc valide trouvé. Le mineur gagnant empoche une récompense pécuniaire, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction. Aujourd’hui, la difficulté de la preuve de travail sur Bitcoin est telle que le minage nécessite une grande puissance de calcul pour parvenir à gagner des blocs. En conséquence, il faut souvent disposer de puces électroniques spécialisées dans l’exécution de `SHA256`, c’est ce que l’on appelle un ASIC, et participer dans des pools de minage.

> *En anglais, on parle de « Proof-of-Work », parfois abrégé avec le sigle « PoW ».*

&nbsp;

**PROBLÈME DES GÉNÉRAUX BYZANTINS -** 

&nbsp;

**PSEUDO-ALÉATOIRE -** Cet adjectif est employé pour décrire une séquence de nombres qui, bien qu'étant le résultat d'un processus déterministe, affiche des caractéristiques qui se rapprochent de celles idéales d'une séquence véritablement aléatoire. La notion d'aléatoire idéal implique une absence totale de prévisibilité et de corrélation entre les éléments successifs. Un nombre pseudo-aléatoire est généré par un algorithme déterministe et est donc, en théorie, il est entièrement prévisible si l'on connaît l'état initial du générateur. Un générateur de nombres pseudo-aléatoires (« PRNG » en anglais, ou « GNPA » en français) est un algorithme utilisé pour produire de tels nombres. Il commence généralement à partir d'une valeur initiale, ou « graine », et applique ensuite une série de transformations mathématiques pour produire la suite de nombres. Du fait de cette déterminabilité, il est crucial pour la sécurité cryptographique que la graine initiale reste secrète. Les suites pseudo-aléatoires sont largement utilisées dans divers domaines, notamment la cryptographie, car elles manifestent un comportement apparemment aléatoire qui suffit pour de nombreuses applications. L'évaluation de la qualité d'un PRNG repose sur la mesure dans laquelle sa sortie se rapproche d'un véritable aléa en termes de distribution, de corrélations et d'autres propriétés statistiques. Dans le cadre de Bitcoin, les nombres pseudo-aléatoires sont utilisés pour produire des clés privées, ou bien pour produire une graine pour les portefeuilles déterministes et hiérarchique. 

&nbsp;

**PTLC -** 












&nbsp;

&nbsp;



# <div align="center">Q</div>

&nbsp;


























&nbsp;

&nbsp;



# <div align="center">R</div>

&nbsp;

**RACINE DE MERKLE -** Condensat ou « top hash » d'un arbre de Merkle, qui représente un résumé de toutes les informations présentes dans l'arbre. Un arbre de Merkle est une structure d'accumulateur cryptographique, parfois également nommée « arbre de hachage ». Dans le cadre de Bitcoin, des arbres de Merkle sont utilisés pour organiser les transactions dans un bloc et pour faciliter la vérification rapide de l'inclusion d'une transaction spécifique. Ainsi, dans les blocs de Bitcoin, la racine de Merkle est obtenue en hachant de manière successive les transactions par paires jusqu'à ce qu'il ne reste qu'un seul hachage (la racine de Merkle). Cette dernière est ensuite incluse dans l'en-tête du bloc correspondant. On retrouve également cette structure dans UTREEXO, une structure permettant de condenser l'UTXO set des nœuds, et dans le MAST Taproot.

> *Voir la définition d'« Arbre de Merkle » pour plus d'informations.*

&nbsp;

**REDEEMSCRIPT -** 

&nbsp;

**RÈGLES DE CONSENSUS -** 

&nbsp;

**RÉORGANISATION -** 

&nbsp;

**RÉSEAU BITCOIN -** 

&nbsp;

**RIPEMD160 -** Acronyme de *Research and development in Advanced Communications technologies in Europe Integrity Primitives Evaluation Message Digest 160*, est une fonction de hachage cryptographique qui génère un condensat de 160 bits à partir d'une entrée arbitraire. Elle est utilisée sur Bitcoin pour transformer une clé publique en une adresse de réception. Le processus implique d'abord l'application de la fonction de hachage `SHA256` sur la clé publique, suivie de l'application de `RIPEMD160` sur le résultat. Cette combinaison de deux fonctions de hachage distinctes est connue sous le nom de `HASH160` dans le contexte de Bitcoin. `RIPEMD160` est également utilisé dans les portefeuilles déterministes et hiérarchiques pour calculer des empreintes de clés. On utilise notamment `HASH160` pour calculer l'empreinte d'une clé parent, ensuite incluse dans les métadonnées d'une clé étendue (xpub).

> *Pour en savoir plus, voir la définition de « Fonction de hachage ».*

&nbsp;

























&nbsp;

&nbsp;



# <div align="center">S</div>

&nbsp;

**SAMOURAI WALLET -** 

&nbsp;

**SATOSHI (SAT) -** Le satoshi, souvent abrégé en « sat », est la plus petite subdivision du bitcoin qui peut être enregistrée sur la blockchain. Il est nommé en l'honneur de l'inventeur de Bitcoin, Satoshi Nakamoto. Un seul Bitcoin se divise en 100 000 000 sats, ce qui signifie qu'un satoshi équivant à 0,00000001 bitcoin. En raison de sa petite valeur unitaire, le sat est souvent utilisé pour établir des prix, en particulier dans les petites transactions. Son utilisation est souvent préférée au btc sur le Lightning Network.

&nbsp;

**SATOSHI NAKAMOTO -** 

&nbsp;

**SCHNORR (PROTOCOLE) -** Le protocole de Schnorr est un algorithme de signatures électroniques établi sur la cryptographie sur les courbes elliptiques (ECC). Il est utilisé sur Bitcoin pour dériver une clé publique à partir d'une clé privée et pour signer une transaction avec une clé privée. Sur Bitcoin, tout comme ECDSA, Schnorr est établi sur l'exploitation de la courbe elliptique `secp256k1`, caractérisée par l'équation : $y^2 = x^3 + 7$. Le protocole de signature de Schnorr est implémenté dans le protocole Bitcoin depuis Novembre 2021 avec l'activation de la mise à jour de Taproot.

&nbsp;

**SCRIPT -** 

&nbsp;

**SCRIPTPUBKEY -** 

&nbsp;

**SCRIPTSIG -** 

&nbsp;

**SECP256K1 -** Nom donné à une courbe elliptique spécifique utilisée dans le cadre du protocole Bitcoin pour l'implémentation des algorithmes de signatures numériques ECDSA (*Elliptic Curve Digital Signature Algorithm*) et Schnorr. La courbe `secp256k1` a été choisie par l’inventeur de Bitcoin, Satoshi Nakamoto. Elle présente certaines propriétés intéressantes, notamment des avantages en termes de performance. L'utilisation de `secp256k1` sur Bitcoin implique que chaque clé privée (un nombre aléatoire de 256 bits) est mappée à une clé publique correspondante par multiplication de la clé privée par le point générateur de la courbe `secp256k1`. Cette opération est facile à réaliser dans un sens, mais pratiquement impossible à inverser, ce qui constitue la base de la sécurité des signatures numériques sur Bitcoin. La courbe `secp256k1` est spécifiée par l'équation de la courbe elliptique $y^2 = x^3 + 7$, ce qui signifie qu'elle a des coefficients $a$ égal à `0` et $b$ égal à `7` dans la forme générale de l'équation d'une courbe elliptique $y^2 = x^3 + ax + b$. `Secp256k1` est définie sur un corps fini dont l'ordre est un nombre premier très grand, spécifiquement $p = 2^{256} - 2^{32} - 977$. La courbe a également un ordre de groupe, qui est le nombre de points distincts sur la courbe, un point générateur (ou point $G$) prédéfini, qui est utilisé dans les opérations de cryptographie pour générer des paires de clés, et un cofacteur qui est égal à `1`.

> *« SEC » désigne « Standards for Efficient Cryptography ». « P256 » désigne le fait que la courbe est définie sur un corps $\mathbb{Z}_p$ où $p$ est un nombre premier de 256 bits. « K » désigne le nom de son inventeur, Neal Koblitz. Enfin, « 1 » désigne que c’est la première version de cette courbe.*

&nbsp;

**SECP256R1 -** Nom

&nbsp;

**SEGWIT -** SegWit, acronyme pour « Segregated Witness » (Témoin Séparé), est une mise à jour du protocole Bitcoin, introduite en août 2017. Elle vise à résoudre plusieurs problèmes techniques, dont la question de la capacité transactionnelle du réseau, le problème de malléabilité des transactions et la facilitation des modifications futures du protocole. Ce Soft Fork modifie la structure des transactions en déplaçant les données de signature de la transaction vers un répertoire séparé. Concrètement, avec SegWit, les signatures sont retirées du bloc principal et insérées dans une structure de données distincte à la fin du bloc, ce sont les témoins (witness). Cette séparation permet d'augmenter la capacité de chaque bloc sans modifier la taille maximale des blocs elle-même, qui est de 1 Mo sur Bitcoin. Cette modification résout également le problème de la malléabilité des transactions. Avant SegWit, les signatures pouvaient être modifiées avant qu'une transaction ne soit confirmée, ce qui changeait l'identifiant de la transaction. Cela rendait difficile la construction de transactions complexes, car une transaction non confirmée pouvait voir son identifiant changer. En séparant les signatures, SegWit rend les transactions non malléables, car tout changement dans les signatures n'affecte plus l'identifiant de la transaction (TXID), mais uniquement l'identifiant du témoin (WTXID). En résolvant le problème de la malléabilité, SegWit a ouvert la voie à d'autres développements en surcouche du système Bitcoin, notamment le réseau Lightning Network, qui permet des transactions rapides et à faible coût.

&nbsp;

**SEGWIT V0 -** Version de script post-SegWit zéro. Les scripts SegWit V0 représentent la première famille de scripts introduite après la mise à jour SegWit de 2017. Les scripts `P2WPKH` et `P2WSH` incarnent la version SegWit V0. Les adresses correspondantes commencent toujours par `bc1q` et sont encodées en format `Bech32`.

&nbsp;

**SEGWIT V1 -** Version de script post-SegWit un. Les scripts SegWit V1 représentent la seconde famille de scripts introduite après la mise à jour SegWit de 2017. En l'occurrence, les scripts SegWit V1 ont été présenté avec la mise à jour Taproot en 2021. Le script `P2TR` est de la version SegWit V1. Les adresses correspondantes commencent toujours par `bc1p` et sont encodées en format `Bech32m`.

&nbsp;

**SHA256 -** Sigle pour « Secure Hash Algorithm 256 bits ». C'est une fonction de hachage cryptographique produisant un condensat de 256 bits. Conçue par la *National Security Agency* (NSA) au début des années 2000, elle est devenue une norme fédérale pour le traitement des données sensibles. Dans le protocole Bitcoin, la fonction `SHA256` est omniprésente. Elle est employée pour hacher les entêtes des blocs dans le cadre de la preuve de travail. `SHA256` est également utilisée dans le processus de dérivation d'une adresse de réception à partir d'une clé publique. On l'utilise également pour l'agrégation des transactions et des témoins au sein des arbres de Merkle dans les blocs. On retrouve aussi `SHA256` dans le calcul d'empreinte de clés, le calcul de certaines sommes de contrôle et dans de nombreux autres processus autour de Bitcoin. Lorsqu'elle est appliquée deux fois de suite, on parle d'un `HASH256`. Cette double application est celle utilisée majoritairement sur Bitcoin. Lorsque `SHA256` est utilisé conjointement à la fonction `RIPEMD160`, on parle d'un `HASH160`. Ce double hachage est utilisé pour les empreintes de clés et pour le hachage de clés publiques. La fonction `SHA256` fait partie de la famille des SHA 2.

> *Pour en savoir plus, voir la définition de « Fonction de hachage ».*

&nbsp;

**SHA512 -** Sigle pour « Secure Hash Algorithm 512 bits ». C'est une fonction de hachage cryptographique produisant un condensat de 512 bits. Elle a été conçue par la *National Security Agency* (NSA) au début des années 2000. Dans le protocole Bitcoin, la fonction `SHA512` est exclusivement utilisée dans le cadre des dérivations de clés enfants. Dans ce processus, elle est utilisée plusieurs fois dans l'algorithme `HMAC`, ainsi que dans la fonction de dérivation de clés `PBKDF2`. La fonction `SHA512` fait partie de la famille des SHA 2, comme `SHA256`. Son fonctionnement est d'ailleurs très similaire à cette dernière.

> *Pour en savoir plus, voir la définition de « Fonction de hachage ».*

&nbsp;

**SIGNATURE NUMÉRIQUE -** Preuve cryptographique qui démontre la possession d'une clé privée spécifique, associée à une clé publique unique, sans avoir à la divulguer. Sur Bitcoin, on la construit à l'aide de la clé privée et du hash d'une transaction. Elle atteste la propriété des bitcoins concernés et permet de satisfaire les conditions de dépense. Elle est générée grâce à un algorithme de signature numérique sur courbe elliptique tel qu'ECDSA ou le protocole de Schnorr.

&nbsp;

**SIMPLIFIED PAYMENT VERIFICATION (SPV)** -

&nbsp;

**SOFTFORK -** 

&nbsp;

**SOMME DE CONTRÔLE (CHECKSUM) -** La somme de contrôle est une valeur calculée à partir d'un ensemble de données, utilisée pour vérifier l'intégrité et la validité de ces données lors de leur transmission ou de leur stockage. Les algorithmes de somme de contrôle sont conçus pour détecter des erreurs accidentelles ou des altérations involontaires des données, comme les erreurs de transmission ou les corruptions de fichiers. Différents types d'algorithmes de somme de contrôle existent, tels que le contrôle de parité, les sommes de contrôle modulaires, les fonctions de hachage cryptographiques, ou encore les codes BCH (*Bose, Ray-Chaudhuri et Hocquenghem*). Dans le système Bitcoin, les sommes de contrôle sont employées pour assurer l'intégrité des adresses de réception. Une somme de contrôle est calculée à partir de la charge utile d'une adresse d'un utilisateur, puis ajoutée à cette adresse afin de détecter d'éventuelles erreurs lors de sa saisie. Une somme de contrôle est également présente dans les phrases de récupération (mnémonique).

> *La traduction anglaise de « somme de contrôle » est « checksum ». Il est généralement admis d'utiliser directement le terme de « checksum » en français.*

&nbsp;

**SORTIE (OUTPUT) -** Dans le contexte de Bitcoin, une « sortie » (ou « output » en anglais) au sein d’une transaction fait référence aux *Unspent Transaction Outputs* (UTXO) qui sont créés comme fonds de destination pour le paiement. Plus précisément, il s'agit d'un mécanisme par lequel une transaction distribue des fonds. Une transaction prend des UTXO, c’est-à-dire des morceaux de bitcoins, comme « inputs » (entrées) et crée de nouveaux UTXO comme « outputs » (sorties). Ces outputs stipulent une certaine quantité de bitcoins, souvent attribués à une adresse spécifique, ainsi que les conditions sous lesquelles ces fonds peuvent être dépensés ultérieurement. Le rôle de la transaction Bitcoin est donc de consommer des UTXO en entrées, et de créer des nouveaux UTXO en sorties. La différence entre les deux correspond aux frais de transactions qui peuvent être récupérés par le mineur gagnant du bloc. Un UTXO est, en essence, la sortie d'une transaction précédente qui n'a pas encore été dépensée. Les outputs de transaction sont donc les créations de nouveaux UTXO qui seront, à leur tour, potentiellement utilisés comme inputs dans les transactions futures. D'un point de vue plus large, en informatique, le terme « output » ou « sortie » désigne généralement les données en résultat d’une fonction, d’un algorithme, ou d’un système. Par exemple, lorsque l’on passe une donnée dans une fonction de hachage cryptographique, cette information est nommée « entrée » ou « input », et le résultat est nommé « sortie » ou « output ». 

&nbsp;

**SPOF (POINT DE DÉFAILLANCE UNIQUE) -** Un point de défaillance unique (SPOF, de l'anglais « Single Point of Failure ») désigne dans le domaine informatique un composant ou un élément d’un système dont la défaillance entraînerait l’arrêt complet ou une perte significative de fonctionnalités de l'ensemble du système. Il peut s'agir d'une pièce matérielle, d'une information, d'un logiciel, ou d'une partie d’un réseau. Par exemple, dans le contexte spécifique des portefeuilles HD Bitcoin, la phrase de récupération de 12 ou de 24 mots constitue souvent un SPOF pour le portefeuille. Si son secret n’est pas assuré, l’intégralité du portefeuille pourrait être subtilisé. De la même manière, sa simple perte pourrait entrainer la perte de l'intégralité des bitcoins du portefeuille.

&nbsp;

**STAMPS -**

&nbsp;

**SRC-20 -** 

&nbsp;

**SUBVENTION DE BLOC -** 

&nbsp;

**SURCOUCHE (LAYER) -** Une « surcouche » (ou « layer » en anglais) est un protocole ou un réseau construit en supplément, en s'empilant sur le réseau Bitcoin principal. Elle utilise le réseau Bitcoin comme une fondation et est donc dépendante de son protocole. Cependant, le réseau Bitcoin n'est pas dépendant de ses surcouches. Un exemple d'une telle surcouche est le Lightning Network. Ces surcouches sont conçues pour étendre les capacités du réseau Bitcoin en ajoutant des fonctionnalités ou des capacités supplémentaires, telles que des transactions plus rapides, des jetons ou des micropaiements. Elles sont souvent créées pour résoudre certaines limitations du réseau Bitcoin, tout en bénéficiant de sa sécurité et de sa décentralisation. Il est important de noter que bien que ces surcouches soient construites sur le réseau Bitcoin, elles ont leurs propres protocoles et mécanismes distincts de ceux du réseau Bitcoin lui-même.

&nbsp;

**Synchronisation initiale d'un nœud (IBD) -** Voir la définition de « Initial Block Download (IBD) ».
























&nbsp;

&nbsp;



# <div align="center">T</div>

&nbsp;

**TAPROOT -** Mise à jour majeure du protocole Bitcoin, adoptée par le biais d'un soft fork en novembre 2021. Cette mise à jour apporte des améliorations significatives en termes de confidentialité, d'efficacité et de flexibilité. Elle permet l'utilisation du protocole de Schnorr et l'utilisation d'un script qui peut être révélé lors de la dépense. Le protocole de Schnorr, intégré à cette mise à jour, est un algorithme de signature numérique établi sur la cryptographie sur les courbes elliptiques (ECC), comme ECDSA. Dans le contexte de Bitcoin, Schnorr est utilisé pour générer une clé publique à partir d'une clé privée et pour signer une transaction avec une clé privée. Comme ECDSA sur Bitcoin, Schnorr utilise la courbe elliptique `secp256k1`, définie par l'équation $y^2 = x^3 + 7$. Les bitcoins bloqués avec Taproot peuvent être dépensés soit en satisfaisant l'un des scripts, soit en fournissant une signature valide correspondant à la clé publique, ce qui permet de garder les scripts privés. On y utilise MAST pour permettre l'utilisation de plusieurs scripts. N'importe lequel peut-être utiliser pour dépenser les bitcoins associés. Cela permet des fonctionnalités plus complexes et des contrats intelligents plus sophistiqués.

> *Pour plus d'informations, voir la définition de « Schnorr (protocole) ».*

&nbsp;

**TÉMOIN DE TRANSACTION -**

&nbsp;

**TESTNET -** 

&nbsp;

**TIMELOCKS -**

&nbsp;

**TPRV -** Préfixe de clé privée étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**TPUB -** Préfixe de clé publique étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**TRANSACTION (TX) -** Dans le contexte de Bitcoin, une transaction (abrégée « TX ») est une opération enregistrée sur la blockchain qui transfère la propriété de bitcoins d'une ou plusieurs entrées (inputs) vers une ou plusieurs sorties (outputs). Chaque transaction consomme des UTXO en entrées, qui sont des outputs de transactions précédentes, et crée de nouveaux UTXO en sorties, qui peuvent être utilisés comme entrants dans des transactions futures. Chaque entrée comporte une référence à un output existant ainsi qu'un script de signature qui rempli les conditions de dépense établies par l'output auquel il fait référence. C'est ce qui permet de débloquer des bitcoins. Les outputs définissent de nouvelles conditions de dépense pour les bitcoins transférés, souvent sous la forme d'une clé publique ou d'une adresse à laquelle les bitcoins sont maintenant associés.

&nbsp;

**TRANSACTION COINBASE -** La transaction coinbase est une transaction spéciale et unique incluse dans chaque bloc de la blockchain Bitcoin. Elle représente la première transaction d'un bloc et est créée par le mineur qui a réussi à trouver un entête validant la preuve de travail (Proof-of-Work). La transaction coinbase sert principalement deux objectifs : attribuer la récompense de bloc au mineur et ajouter de nouvelles unités de bitcoins à la masse monétaire en circulation. La récompense de bloc, qui est l'incitation économique pour les mineurs à contribuer à s'adonner à la preuve de travail, comprend les frais accumulés pour les transactions incluses dans le bloc et un montant déterminé de bitcoins nouvellement créés ex-nihilo (subvention de bloc). Ce montant, initialement fixé à 50 bitcoins par bloc en 2009, est réduit de moitié tous les 210 000 blocs (environ tous les 4 ans) lors d'un événement appelé « halving ». La transaction coinbase diffère des transactions régulières de plusieurs manières. Tout d'abord, elle n'a pas d'entrée (input), ce qui signifie qu'aucune sortie de transaction existante (UTXO) n'y est dépensée. Ensuite, le script de signature `scriptSig` pour la transaction coinbase contient généralement un champ arbitraire permettant d'incorporer des données supplémentaires, telles que des messages personnalisés ou des informations de version de logiciel de minage. Enfin, les bitcoins générés par la transaction coinbase sont soumis à une période de maturité de 100 blocs (101 confirmations) avant de pouvoir être dépensés, afin de prévenir les dépenses potentielles de bitcoins non existants en cas de réorganisation de la chaîne.

&nbsp;

**TXID -**





















&nbsp;

&nbsp;



# <div align="center">U</div>

&nbsp;

**UPRV -** Préfixe de clé privée étendue pour les comptes Nested SegWit sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**UPUB -** Préfixe de clé publique étendue pour les comptes Nested SegWit sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;




&nbsp;

**UTREEXO -**

&nbsp;

**UTXO -** Sigle de *Unspent Transaction Output*. Un UTXO est une sortie de transaction qui n'a pas encore été dépensée ou utilisée comme entrée pour une nouvelle transaction. Les UTXOs représentent la fraction de bitcoins que possède un utilisateur et qui sont actuellement disponibles pour être dépensés. Chaque UTXO est associé à un script de sortie spécifique, qui définit les conditions nécessaires pour dépenser les bitcoins. Les transactions dans Bitcoin consomment ces UTXOs en entrées (inputs) et créent de nouveaux UTXOs en sorties (outputs). Le modèle d'UTXO est fondamental sur Bitcoin, car il permet de vérifier facilement que les transactions n'essaient pas de dépenser des bitcoins qui n'existent pas ou qui ont déjà été dépensés.

&nbsp;

UTXO SET - Le terme « UTXO set » désigne l'ensemble de tous les UTXOs existants à un moment donné. Autrement dit, c'est une grosse liste de tous les différents morceaux de bitcoins qui attendent d'être dépensés. Si l'on additionne les montants de tous les UTXOs de l'UTXO set, cela nous donne la masse monétaire totale de bitcoins en circulation. Chaque nœud du réseau Bitcoin conserve son propre UTXO set en temps réel. Il l'actualise au fur et à mesure de la confirmation de nouveaux blocs valides, avec les transactions qu'ils incluent, qui consomment certains UTXOs de l'UTXO set, et qui en créent de nouveaux en contrepartie. Cet UTXO set est conservé par chaque nœud afin de pouvoir vérifier rapidement si les UTXOs dépensés dans les transactions sont bien légitimes. Cela leur permet de détecter et de rejeter les tentatives de doubles dépenses. L'UTXO set est souvent au cœur d'inquiétudes sur la décentralisation de Bitcoin, car sa taille augmente naturellement très rapidement. Puisqu'il faut en conserver une partie en RAM pour pouvoir procéder à la vérification des transactions en temps raisonnable, il est possible que l'UTXO set rende progressivement l'opération d'un nœud complet trop couteuse. L'UTXO set a également un fort impact sur l'IBD (Initial Block Download). Au plus on peut mettre une grande part de l'UTXO en RAM, au plus l'IBD est rapide.

> *Voir la définition du terme « UTXO » pour plus de précisions.*






















&nbsp;

&nbsp;


# <div align="center">V</div>

&nbsp;

**VPRV -** Préfixe de clé privée étendue pour les comptes SegWit V0 sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**VPUB -** Préfixe de clé publique étendue pour les comptes SegWit V0 sur Bitcoin Testnet. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;


























&nbsp;

&nbsp;


# <div align="center">W</div>

&nbsp;

**WABISABI -**

&nbsp;

**WALLET -** Traduction anglaise de « portefeuille ». Voir la définition de « portefeuille » pour plus d'informations.

&nbsp;

**WALLET IMPORT FORMAT (WIF) -**

&nbsp;

**WASABI WALLET -**

&nbsp;

WATCH-ONLY WALLET -

&nbsp;

**WHIRLPOOL -**

&nbsp;

**WTXID -** 
























&nbsp;

&nbsp;


# <div align="center">X</div>

&nbsp;

**XOR -** Sigle de l'opération « Exclusive or », en français « Ou exclusif ». C'est une fonction fondamentale de la logique booléenne. Cette opération prend deux opérandes booléens, chacun étant `vrai` ou `faux`, et produit une sortie `vraie` uniquement lorsque les deux opérandes diffèrent. Autrement dit, la sortie de l'opération `XOR` est `vraie` si exactement un (mais pas les deux) des opérandes est `vrai`. Par exemple, l'opération `XOR` entre `1` et `0` donnera comme résultat `1`. Nous noterons : $1 \oplus 0 = 1$. De même, l'opération `XOR` peut être effectuée sur des séquences plus longues de bits. Par exemple, $10110 \oplus 01110 = 11000$. Chaque bit de la séquence est comparé à son homologue et l'opération `XOR` est appliquée. Voici la table de vérité de l'opération `XOR` :

<div align="center">

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

</div>

L'opération `XOR` est utilisée dans de nombreux domaines de l'informatique, notamment dans la cryptographie, pour ses attributs intéressants comme : 
* Sa commutativité : L'ordre des opérandes n'affecte pas le résultat. Pour deux variables $D$ et $E$ données : $D \oplus E = E \oplus D$ ;
* Son associativité : Le regroupement des opérandes n'affecte pas le résultat. Pour trois variables $A$, $B$ et $C$ données : $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ ;
* Il dispose d'un élément neutre `0` : Une opérande xorée à 0 sera toujours égal à l'opérande. Pour une variable $A$ donnée : $A \oplus 0 = A$ ;
* Chaque élément est son propre inverse. Pour une variable $A$ donnée : $A \oplus A = 0$.

Dans le cadre de Bitcoin, on utilise évidement l'opération `XOR` à de nombreux endroits. Par exemple, le `XOR` est massivement utilisé dans la fonction `SHA256`, elle-même largement utilisée dans le protocole Bitcoin. Certains protocoles comme le *SeedXOR* de Coldcard utilisent également cette primitive pour d'autres applications.

&nbsp;

**XPRV -** Préfixe de clé privée étendue pour les comptes Legacy et SegWit V1 sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**XPUB -** Préfixe de clé publique étendue pour les comptes Legacy et SegWit V1 sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

















&nbsp;

&nbsp;


# <div align="center">Y</div>

&nbsp;

**YPRV -** Préfixe de clé privée étendue pour les comptes Nested SegWit sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**YPUB -** Préfixe de clé publique étendue pour les comptes Nested SegWit sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;






























&nbsp;

&nbsp;


# <div align="center">Z</div>

&nbsp;

**ZPRV -** Préfixe de clé privée étendue pour les comptes SegWit V0 sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;

**ZPUB -** Préfixe de clé publique étendue pour les comptes SegWit V0 sur Bitcoin. Pour plus d'information, voir la définition « Clé étendue ».

&nbsp;































































