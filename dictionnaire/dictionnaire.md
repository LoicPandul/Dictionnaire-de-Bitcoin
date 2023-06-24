# Le Dictionnaire de Bitcoin 2024
Tout le vocabulaire technique de Bitcoin et de son environnement.


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

# **A**
**ADRESSE DE RÉCEPTION -**

Information utilisée pour recevoir des bitcoins. Une adresse est construite en hachant une clé publique, à l'aide de `SHA256` et de `RIMPEMD160`, et en ajoutant des métadonnées à ce condensat. Les clés publiques utilisées pour construire une adresse de réception font partie du portefeuille de l'utilisateur et sont donc dérivées depuis sa graine.

Les adresses SegWit sont composées des informations suivantes : 
* Un HRP pour désigner « bitcoin » : `bc` ; 
* Un séparateur : `1` ; 
* La version de SegWit utilisée : `q` ou `p` ; 
* La charge utile : le condensat de la clé publique ; 
* La somme de contrôle : un code BCH.

Une adresse de réception peut être représentée sous la forme d'une chaîne de caractères alphanumériques ou sous la forme d'un QR code. Chaque adresse peut être utilisée plusieurs fois, mais c'est une pratique très déconseillée. En effet, dans le but de maintenir un certain niveau de confidentialité, il est conseillé de n'utiliser chaque adresse Bitcoin qu'une seule fois. Il faut en générer une nouvelle pour tout paiement entrant vers son portefeuille.

Une adresse est encodée en Bech32 pour les adresses SegWit V0, en Bech32m pour les adresses SegWit V1, et en Base58check pour les adresses Legacy.

D'un point de vue technique, une adresse ne permet pas réellement de recevoir des bitcoins, mais plutôt de bloquer des bitcoins à l'aide d'un script, en mettant des contraintes sur leur dépense.

&nbsp;

**AJUSTEMENT DE LA DIFFICULTÉ (OU RECIBLAGE) -**

L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin.

Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L’ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d’un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. Le calcul qu'effectuent les nœuds pour calculer la nouvelle cible est le suivant : $N = A \cdot \left(\frac{T}{1,209,600}\right)$


Où :
* $N$ : La nouvelle cible ;
* $A$ : L'ancienne cible des 2016 derniers blocs ;
* $T$ : Le temps total réel des 2016 derniers blocs en secondes ;
* $1,209,600$ : Le temps cible en secondes pour produire 2016 blocs avec un intervalle de 10 minutes entre chacun.
> *En français, on parle parfois également de « reciblage » pour évoquer l'ajustement. En anglais, on parle de « Difficulty Adjustment ».*

&nbsp;

**ARBRE DE MERKLE -**

Un Arbre de Merkle est un accumulateur cryptographique. C’est une méthode pour justifier l’appartenance d’une information donnée à un ensemble plus grand. C'est une structure de données qui facilite la vérification d’informations dans un format compact.

Dans le système Bitcoin, les arbres de Merkle sont utilisés pour regrouper et condenser les transactions d'un bloc en un unique hachage, appelé la racine de Merkle (ou « Top Hash »). Chaque transaction est hachée, puis les hachages adjacents sont hachés ensemble de façon hiérarchique jusqu'à ce que la racine de Merkle soit obtenue.
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

**ASIC (CIRCUIT INTÉGRÉ SPÉCIFIQUE À UNE APPLICATION) -**

Un ASIC est un composant électronique conçu pour exécuter une fonction spécifique avec une efficacité optimale. Dans le contexte du minage de Bitcoin, les ASIC sont des circuits intégrés spécialisés qui effectuent des opérations de hachage à haute vitesse et faible consommation d'énergie. Ils sont spécialisés dans l'exécution de la fonction de hachage SHA256 utilisée dans le mécanisme de la preuve de travail.

L'ASIC est initialement le nom de la puce. Par extension, l'acronyme « ASIC » vise souvent à désigner également la machine qui héberge cette puce. Ainsi, les ordinateurs spécialisés dans le minage de Bitcoin sont parfois appelés des « ASIC », ou bien des « mineurs ».

Les ASIC ont progressivement remplacé les autres méthodes de minage, telles que l'utilisation de processeurs (CPU) et de cartes graphiques (GPU), en raison de leur efficacité énergétique supérieure et de leur taux de hachage bien plus élevé.

>*L'acronyme « ASIC » désigne en anglais « Application-Specific Integrated Circuit ». En français, ce terme peut être traduit par « Circuit intégré spécifique à une application ».*

&nbsp;

&nbsp;

___ 

&nbsp;

&nbsp;

# **B**


**BASE (ARITHMÉTIQUE) -**

Une base est un système de numération positionnel qui utilise un nombre fixe de caractères pour représenter tous les nombres possibles. La base détermine le nombre de symboles distincts disponibles pour représenter les chiffres dans ce système.

Par exemple, le système le plus connu dans nos vies quotidiennes est la base 10, également appelée système décimal. Elle utilise dix symboles distincts (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) pour représenter tous les nombres. D'autres systèmes de numération couramment utilisés dans les domaines informatique et mathématique incluent le système binaire (base 2), avec deux symboles (0, 1), et le système hexadécimal (base 16), avec seize symboles (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F).

Dans le cadre de Bitcoin, vous rencontrerez parfois des encodages en base 58 ou en base 32 adaptée (nommée Bech32).

&nbsp;

**BASE58CHECK -**

La Base58Check est un encodage utilisé dans le système Bitcoin pour représenter les adresses de réception Legacy et certaines autres données, telles que les clés étendues, sous forme de chaînes de caractères lisibles par l'homme. C’est une variante du système Base58, une représentation positionnelle de base 58 conçue pour minimiser les erreurs de transcription humaine. Elle utilise un ensemble de 58 caractères alphanumériques, composé des chiffres de 1 à 9, des lettres majuscules A à Z (à l'exception des lettres « I » et « O » pour éviter la confusion avec les chiffres « 1 » et « 0 ») et des lettres minuscules de a à z (à l'exception de la lettre « l » pour éviter la confusion avec le chiffre « 1 »).

La Base58Check se distingue de la Base58 par l'ajout d'une somme de contrôle (checksum). Elle est représentée par une version réduite d'un double hachage SHA-256 des données originales (SHA256d ou HASH256), à la fin des données encodées en Base58. Lors de la vérification, la somme de contrôle est recalculée et comparée à celle qui a été ajoutée lors de l'encodage. Si les deux empreintes correspondent, les données sont considérées comme valides, sinon une erreur de corruption ou de transcription est signalée.

L'utilisation de la Base58Check dans les adresses Bitcoin et les clés privées procure plusieurs avantages. Premièrement, elle permet de réduire les erreurs humaines lors de la transcription et de la lecture en évitant les caractères ambigus. Deuxièmement, elle protège contre les erreurs de saisie en détectant et signalant les erreurs grâce au hachage de vérification. Enfin, la représentation compacte des données en Base58Check permet de réduire l'espace requis pour stocker et partager les adresses et les clés.

Les adresses de réception les plus récentes (post-SegWit) ont abandonné cet encodage Base58check pour des encodages Bech32 et Bech32m, disposant d'une somme de contrôle plus évoluée (code BCH).

&nbsp;

**BECH32 ET BECH32M -**

Bech32 et Bech32m sont deux formats d'encodage d'adresse pour recevoir des bitcoins. Ils sont établis sur une base 32 légèrement modifiée. Ils embarquent une somme de contrôle établie sur un algorithme de correction d'erreurs appelé BCH (Bose-Chaudhuri-Hocquenghem).

Par rapport aux adresses Legacy, encodées en Base58check, les adresses Bech32 et Bech32m disposent d'une somme de contrôle plus performante, permettant de détecter et potentiellement de modifier automatiquement les fautes de frappe. Leur format dispose également d'une meilleure lisibilité, avec uniquement des caractères minuscules. Voici la table de conversion de ce format depuis la base 10 : 

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|----|---|---|---|---|---|---|---|---|
| 0  | q | p | z | r | y | 9 | x | 8 |
| 8  | g | f | 2 | t | v | d | w | 0 |
| 16 | s | 3 | j | n | 5 | 4 | k | h |
| 24 | c | e | 6 | m | u | a | 7 | l |


Bech32 et Bech32m sont des formats d'encodage utilisés pour représenter les adresses SegWit. Bech32 est un format d'encodage d'adresse introduit par la BIP173 en 2017. Il utilise un ensemble de caractères spécifiques, composé de chiffres et de lettres minuscules, pour minimiser les erreurs de frappe et faciliter la lecture. Les adresses Bech32 commencent généralement par "bc1" pour indiquer qu'elles sont natives de SegWit. Ce format est uniquement utilisé sur les adresses SegWit V0, avec les scripts P2WPKH (Pay to Witness Public Key Hash) et P2WSH (Pay to Witness Script Hash).

Toutefois, il existe une petite faille inattendue propre au format Bech32. Chaque fois que le dernier caractère de l'adresse est un « p », l'ajout ou la suppression d'un nombre quelconque de symboles « q » le précédant immédiatement n'invalide pas la somme de contrôle. Cela n'affecte pas les utilisations existantes des adresses SegWit V0 (BIP173) en raison de leur restriction à deux longueurs définies. Cependant, cela pourrait affecter des utilisations futures de l'encodage Bech32. Le format Bech32m est simplement un format Bech32 avec cette erreur rectifiée. Il a été introduit avec le BIP350 en 2020. Les adresses Bech32m commencent également par "bc1", mais elles sont spécifiquement conçues pour être compatibles avec la version SegWit V1 (Taproot) et les versions ultérieures, avec le script P2TR (Pay to TapRoot).

&nbsp;

**BIP (BITCOIN IMPROVEMENT PROPOSAL) -**
Une proposition d'amélioration de Bitcoin (BIP) est un processus formel de proposition et de documentation des améliorations et des modifications apportées au protocole Bitcoin et à ses normes.

Inspiré par le processus des Python Enhancement Proposals (PEP), le BIP vise à faciliter la communication et la collaboration entre les développeurs, les chercheurs, les utilisateurs et les parties prenantes de l'écosystème Bitcoin. Le processus BIP assure une approche structurée et transparente pour l'évaluation et l'adoption de nouvelles fonctionnalités, optimisations et mises à jour.

Chaque BIP est un document détaillé qui décrit précisément les objectifs de l'amélioration proposée, la justification de sa mise en œuvre, les éventuels problèmes de compatibilité, les avantages et les inconvénients. Il décrit également les étapes techniques nécessaires pour réaliser l'amélioration. Les BIP peuvent être rédigés par n'importe qui. Ils doivent cependant être soumis à un examen approfondi et à l'approbation d'autres membres de la communauté Bitcoin.

> *BIP est l'acronyme anglais pour « Bitcoin Improvment Proposal ». En français, on peut le traduire par « Proposition d'amélioration de Bitcoin ». Toutefois, la plupart des textes français utilisent directement l'acronyme « BIP » comme un nom commun, parfois au féminin, parfois au masculin.*

&nbsp;

### **BIT**
Le mot « bit » est la contraction des termes « binary » et « digit » en anglais. Dans le contexte des sciences informatiques et de la cryptologie, un bit est l'unité fondamentale d'information numérique et représente la plus petite quantité d'information possible.

Un bit ne peut prendre que deux valeurs distinctes : 0 ou 1. Ces valeurs sont également appelées états binaires et peuvent représenter diverses choses, telles que les réponses « oui » ou « non », « vrai » ou « faux » et « on » ou « off ». Les bits sont la base des systèmes numériques et sont utilisés pour stocker et transmettre de l'information dans les ordinateurs et les réseaux.

Le nom de « Bitcoin » provient sûrement de la concaténation du terme « Bit », pour évoquer la nature électronique du système de paiement, et du terme « Coin », pour évoquer son objectif monétaire.

> *En français, on utilise souvent directement le mot « bit ». La traduction de ce terme anglais pourrait être « chiffre binaire ».*

Dans le contexte de Bitcoin, le terme « bit » est aussi utilisé pour désigner une subdivision monétaire du bitcoin. Un bit est égal à 100 satoshis, qui représentent la plus petite unité indivisible de bitcoin. Ainsi, un bitcoin est égal à 1 000 000 de bits ou 100 000 000 de satoshis. Cependant, l'utilisation de ce terme comme subdivision monétaire est sujet à controverse. La majorité des bitcoiners utilisent soit le « sats », soit le « btc », mais pas le « bit ».

&nbsp;

**BITCOIN (« B » MAJUSCULE) -**
Bitcoin est le nom du système de cash électronique pair-à-pair créé par Satoshi Nakamoto en 2009.

L'utilisation du terme Bitcoin avec un « B » majuscule peut vouloir évoquer trois choses différentes :
* Le système Bitcoin ;
* Le protocole Bitcoin ;
* Le réseau Bitcoin.

Le terme de bitcoin avec un « b » minuscule est généralement réservé pour évoquer l'unité monétaire échangée sur ce système.

&nbsp;

**BITCOIN (« B » MINUSCULE) -**
Le bitcoin (écrit avec un « b » minuscule) fait référence à l'unité monétaire utilisée pour les échanges sur le système de cash électronique Bitcoin (avec un "B" majuscule).

Le bitcoin est souvent abrégé en « BTC » ou « XBT » et sert de moyen d'échange, de réserve de valeur et d'unité de compte au sein du réseau. Chaque bitcoin est divisible en 100 millions d'unités plus petites, appelées « satoshis » ou « sats », en l'honneur de son créateur, Satoshi Nakamoto.

Les bitcoins sont émis par le processus de la preuve de travail (minage). Le nombre total de bitcoins est limité à 21 millions, assurant une offre finie et prévisible.

&nbsp;

**BITCOIN.CONF -**










