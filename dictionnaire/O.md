## OBJECTIF

Dans les portefeuilles déterministes et hiérarchiques (HD), l'objectif (ou _purpose_ en anglais), défini par le BIP43, représente un niveau de dérivation spécifique. Cet index, situé à la première profondeur de l'arborescence de dérivation (`m / purpose' /`), identifie le standard de dérivation adopté par le portefeuille, afin de faciliter la compatibilité entre différents logiciels de gestion de portefeuille. Par exemple, dans le cas des adresses SegWit (BIP84), l'objectif est noté `/84'/`. Cette méthode permet d'organiser efficacement les clés entre les différents types d'adresses au sein d'un même portefeuille HD. Les index standards utilisés sont :
* Pour du P2PKH : `44'` ;
* Pour du P2WPKH-nested-in-P2SH : `49'` ;
* Pour du P2WPKH : `84'` ;
* Pour du P2TR : `86'`.

![](assets/20.png)

► ***NOTE :** Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## OBOE (OFF-BY-ONE ERROR)

Erreur de logique où une boucle itère une fois de trop ou de moins, souvent due à une mauvaise utilisation des opérateurs de comparaison ou de mauvais indices dans la gestion des structures de données. Dans le contexte de Bitcoin, on retrouve ce bug dans le cas du « *dummy element* » dans `OP_CHECKMULTISIG`, où un élément supplémentaire est consommé par erreur.

► ***NOTE :** En français, on peut traduire ce terme par « erreur de décalage unitaire ». Pour plus d'informations, voir les définitions de [**DUMMY ELEMENT**](./D.md#dummy-element) et [**BIP147**](./B.md#bip147).*

## OBSOLÈTE

Fait référence à un bloc sans enfant : un bloc valide mais exclu de la chaîne principale de Bitcoin. Il se produit lorsque deux mineurs trouvent un bloc valide sur une même hauteur de chaîne durant un court laps de temps et le diffusent sur le réseau. Les nœuds finissent par choisir un seul bloc à inclure dans la chaîne, selon le principe de la chaîne avec le plus de quantité de travail accumulé, rendant l'autre « obsolète ». Le processus menant à la production d'un bloc obsolète est le suivant :
* Deux mineurs trouvent un bloc valide à une même hauteur de chaîne durant un court intervalle de temps. Nommons les `Bloc A` et `Bloc B` ;
* Chacun diffuse son bloc au réseau de nœuds Bitcoin. Chaque nœud dispose maintenant de 2 blocs à une même hauteur. Il existe donc deux chaînes valides ;
* Les mineurs continuent de chercher des preuves de travail pour les blocs suivants, mais pour ce faire, ils doivent obligatoirement choisir un seul bloc entre le `Bloc A` et le `Bloc B` au-dessus duquel ils vont miner ;
* Un mineur trouve finalement un bloc valide au-dessus du `Bloc B`. Appelons le `Bloc B+1` ;
* Il diffuse `Bloc B+1` aux nœuds du réseau ;
* Puisque les nœuds suivent la chaîne la plus longue (avec le plus de quantité de travail accumulé), ils vont estimer que la `Chaîne B` est celle qu'il faut suivre ;
* Ils vont donc abandonner le `Bloc A` qui ne fait plus partie de la chaîne principale. Il est donc devenu un bloc obsolète.

![](assets/9.png)

► ***NOTE :** En anglais, on parle de « Stale Block ». En français, on peut également dire « bloc périmé » ou « bloc abandonné ». Même si je ne suis pas en accord avec cet usage, certains bitcoiners utilisent le terme de « bloc orphelin » pour désigner ce qui est en réalité un bloc obsolète. Pour plus d'informations, voir la définition de **[ORPHELIN](./O.md#orphelin)**.*

## OCTET (BYTE)

Unité de mesure de données informatiques équivalant à 8 bits. Chaque bit est un chiffre binaire (0 ou 1), ce qui signifie qu'un octet peut représenter 256 (2^8) combinaisons uniques.

## OFFCHAIN

Fait référence aux transactions ou activités plus ou moins liées à Bitcoin qui se produisent en dehors de la blockchain principale, mais qui disposent d'un lien ou d'un ancrage avec celle-ci. Elles ne sont pas immédiatement enregistrées sur la blockchain, mais nécessitent des mécanismes supplémentaires pour assurer leur sécurité et leur finalité. Ces opérations se justifient souvent par un désir d'outre-passer les limitations techniques inhérentes à Bitcoin afin de disposer de transactions à finalité rapide, à bas frais, avec plus de capacité ou de fonctionnalités.

## ONCHAIN

Désigne les transactions enregistrées directement sur la blockchain Bitcoin. Ce terme s'oppose à « offchain » qui désigne des opérations ayant un rapport plus ou moins prononcé avec la blockchain Bitcoin, mais qui se déroulent en dehors de la blockchain principale.

## ONION_PRIVATE_KEY

Fichier anciennement utilisé dans Bitcoin Core pour stocker une clé privée associée à un service caché Tor V2 pour l'option `-listenonion`. Ce fichier n'est plus utilisé depuis la version 0.21.0 au profit de la V3 de Tor.

## ONION_V3_PRIVATE_KEY

Fichier utilisé dans Bitcoin Core pour stocker une clé privée associée à un service caché Tor pour l'option `-listenonion`. Lorsque cette option est activée, bitcoind crée automatiquement un service caché Tor, permettant au nœud de communiquer sur le réseau Tor.

## OP_0 (0X00)

Pousse la valeur 0 sur la pile. Il est souvent utilisé pour représenter la valeur booléenne `faux` dans les scripts. OP_0 est également utilisé pour initialiser les scripts.

► ***NOTE :** OP_0 est identique à **[OP_FALSE](./O.md#op_false-0x00)** et **OP_PUSHNUM_0**.*

## OP_0NOTEQUAL (0X92)

Vérifie si l'élément au sommet de la pile est différent de zéro. Si l'élément est autre que zéro, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OP_1 (0X51)

Pousse la valeur `1` sur la pile. Il est souvent utilisé pour représenter la valeur booléenne `vrai` dans les scripts.

► ***NOTE :** OP_1 est identique à **[OP_TRUE](./O.md#op_true-0x51)** et **OP_PUSHNUM_1**.*

## OP_1ADD (0X8B)

Ajoute `1` à la valeur en haut de la pile.

## OP_1NEGATE (0X4F)

Pousse la valeur `-1` sur la pile. Cet opcode est utilisé dans les scripts pour représenter la valeur négative `-1`.

## OP_1SUB (0X8C)

Soustrait `1` à la valeur en haut de la pile.

## OP_2 À OP_16 (0X52 À 0X60)

Les opcodes de OP_2 jusqu'à OP_16 poussent les valeurs numériques respectives de 2 à 16 sur la pile. On les utilise pour simplifier les scripts en permettant l'insertion de petites valeurs numériques. Ce type d'opcode est notamment utilisé dans les scripts multisignatures. Voici un exemple de `ScriptPubKey` pour un multisig 2/3 : `OP_2 Clé publique A Clé publique B Clé publique C OP_3 OP_CHECKMULTISIG`

► ***NOTE :** Tous ces opcodes sont parfois également nommés **OP_PUSHNUM_N**.*

## OP_2DROP (0XD6)

Supprime les deux éléments en haut de la pile. Autrement dit, `OP_2DROP` supprime le sommet de la pile et le deuxième élément de la pile. Cet opcode est l'équivalent de l'enchainement de deux `OP_DROP`.

## OP_2DUP (0X6E)

Duplique les deux éléments en haut de la pile, puis les place en haut de la pile. Par exemple, si la pile est `D C B A`, `OP_2DUP` produira : `D C B A B A`.

## OP_2OVER (0X70)

Copie les deux éléments qui se trouvent à la quatrième et à la troisième place en partant du haut de la pile, puis les place en haut de la pile. Par exemple, si la pile est `D C B A`, `OP_2OVER` produira : `D C B A D C`.

## OP_2ROT (0X71)

Déplace les deux éléments qui se trouvent à la sixième et à la cinquième place du sommet de la pile vers le sommet. Par exemple, si la pile est `F E D C B A`, `OP_2ROT` produira : `D C B A F E`.

## OP_2SWAP (0X72)

Échange les deux éléments situés au sommet de la pile avec les deux éléments situés juste en dessous d'eux. Par exemple, si la pile est `D C B A`, `OP_2SWAP` produira : `B A D C`.

## OP_3DUP (0X6F)

Duplique les trois éléments en haut de la pile, puis les place en haut de la pile. Par exemple, si la pile est `D C B A`, `OP_3DUP` produira : `D C B A C B A`.

## OP_ABS (0X90)

Remplace l'élément supérieur de la pile par sa valeur absolue. Cette opération supprime le signe de l'élément, transformant toute valeur négative en positive, sans changer les valeurs positives.

## OP_ADD (0X93)

Additionne les deux éléments au sommet de la pile. Il prend les deux valeurs en haut de la pile, il les additionne et il les remplace par le résultat.

## OP_BOOLAND (0X9A)

Reproduit le comportement d'une porte logique `AND`. Il prend deux valeurs au sommet de la pile et renvoie `1` seulement si les deux valeurs sont non nulles. Dans le cas contraire, il renvoie `0`.

## OP_BOOLOR (0X9B)

Reproduit le comportement d'une porte logique `OR`. Il prend deux valeurs au sommet de la pile et renvoie `1` si l'un ou l'autre des éléments ou les deux sont non nuls. Dans le cas contraire, il renvoie `0`.

## OP_CAT (0X7E)

Permet de concaténer les deux éléments en haut de la pile (c'est-à-dire de les mettre bout-à-bout). Cet opcode a été désactivé, il est donc actuellement impossible de l'utiliser. Toutefois, il est récemment revenu sur le devant de la scène. Certains souhaiteraient pouvoir l'ajouter à Tapscript afin de permettre la combinaison d'objets sur la pile et ainsi améliorer l'expressivité de ce langage. Ce simple outil supplémentaire pourrait permettre :
* L'utilisation des signatures de Lamport qui sont à priori résistantes aux attaques quantiques ;
* La mise en place de Vaults ;
* L'utilisation de covenants ;
* Ou encore, l'utilisation de contrat de non équivocation.

## OP_CHECKHASHVERIFY (CHV)

Nouvel opcode proposé en 2012 dans le BIP17 par Luke Dashjr qui permet de disposer des mêmes fonctionnalités que `OP_EVAL` ou P2SH. Il aurait dû permettre de hacher la fin du `scriptSig`, de comparer le résultat avec le haut de la pile et rendre la transaction invalide si les deux hachages ne correspondaient pas. Cet opcode n'a jamais été implémenté.

## OP_CHECKLOCKTIMEVERIFY (0XB1)

Rend la transaction invalide sauf si toutes ces conditions sont réunies :
* La pile n'est pas vide ;
* La valeur du haut de la pile est supérieure ou égale à `0` ;
* Le type de timelock est le même entre le champ `nLockTime` et la valeur du haut de la pile (temps réel ou numéro de bloc) ;
* Le champ `nSequence` de l'input n'est pas égal à `0xffffffff` ;
* La valeur du haut de la pile est supérieure ou égale à la valeur du champ `nLockTime` de la transaction.

Si une seule de ces conditions n'est pas remplie, le script contenant l'`OP_CHECKLOCKTIMEVERIFY` ne peut être satisfait. Si toutes ces conditions sont valides, alors `OP_CHECKLOCKTIMEVERIFY` agit comme un `OP_NOP`, c'est-à-dire qu'il ne fait aucune action sur le script. C'est un peu comme s'il disparaissait. `OP_CHECKLOCKTIMEVERIFY` impose donc une contrainte de temps sur la dépense de l'UTXO sécurisé avec le script le contenant. Il peut le faire soit sous la forme d'une date exprimée en temps Unix, soit sous la forme d'un numéro de bloc. Pour ce faire, il restreint les valeurs possibles pour le champs `nLockTime` de la transaction qui le dépense, et ce champs `nLockTime` restreint lui-même le moment où la transaction peut être incluse dans un bloc.

► ***NOTE :** Cet opcode est un remplaçant d'`OP_NOP`. Il a été placé sur l'`OP_NOP2`. Il est souvent appelé par con acronyme « CLTV ». Attention, `OP_CLTV` ne doit pas être confondu avec le champs `nLockTime` d'une transaction. Le premier utilise le second, mais leurs natures et leurs actions sont différentes.*

## OP_CHECKMULTISIG (0XAE)

Vérifie plusieurs signatures contre plusieurs clés publiques. Il prend en entrée une série de `N` clés publiques et `M` signatures, où `M` peut être inférieur ou égal à `N`. `OP_CHECKMULTISIG` vérifie si au moins `M` signatures correspondent à `M` des `N` clés publiques. À noter qu'en raison d'un bug off-by-one historique, un élément supplémentaire est supprimé par `OP_CHECKMULTISIG` sur la pile. Cet élément est appelé « *dummy element* ». Pour éviter une erreur dans le `ScriptSig`, on inclue donc un `OP_0` qui est un élément inutile afin de satisfaire la suppression et outrepasser le bug. Depuis le BIP147 (introduit avec SegWit en 2017), l'élément inutile consommé à cause du bug doit forcément être `0` pour que le script soit valide, car c'était un vecteur de malléabilité. Cet opcode a été supprimé dans Tapscript.

## OP_CHECKMULTISIGVERIFY (0XAF)

Combine un `OP_CHECKMULTISIG` et un `OP_VERIFY`. Il prend plusieurs signatures et clés publiques pour vérifier que `M` parmi `N` signatures sont valides, comme le fait `OP_CHECKMULTISIG`. Puis, à l'instar d'`OP_VERIFY`, si la vérification échoue, le script s'arrête immédiatement avec une erreur. Si la vérification est réussie, le script continue sans pousser de valeur sur la pile. Cet opcode a été supprimé dans Tapscript.

## OP_CHECKSEQUENCEVERIFY (0XB2)

Rend la transaction invalide si une seule de ces caractéristiques est observée :
* La pile est vide ;
* La valeur du haut de la pile est inférieure à `0` ;
* L'indicateur de désactivation de la valeur en haut de la pile est non défini et ;
*- La version de la transaction est inférieure à `2` ou ;
*- L'indicateur de désactivation du champ `nSequence` de l'input est défini ou ;
*- Le type de timelock n'est pas le même entre le champ `nSequence` et la valeur du haut de la pile (temps réel ou nombre de blocs) ;
*- La valeur en haut de la pile est supérieure à la valeur du champ `nSequence` de l'input.

Si une ou plusieurs de ces caractéristiques est observée, le script contenant l'`OP_CHECKSEQUENCEVERIFY` ne peut être satisfait. Si toutes les conditions sont valides, alors `OP_CHECKSEQUENCEVERIFY` agit comme un `OP_NOP`, c'est-à-dire qu'il ne fait aucune action sur le script. C'est un peu comme s'il disparaissait. `OP_CHECKSEQUENCEVERIFY` impose donc une contrainte de temps relative sur la dépense de l'UTXO sécurisé avec le script le contenant. Il peut le faire soit sous la forme d'un temps réel, soit sous la forme d'un nombre de blocs. Pour ce faire, il restreint les valeurs possibles pour le champs `nSequence` de l'input qui le dépense, et ce champs `nSequence` restreint lui-même le moment où la transaction qui comprend cet input peut être incluse dans un bloc.

► ***NOTE :** Cet opcode est un remplaçant d'`OP_NOP`. Il a été placé sur l'`OP_NOP3`. Il est souvent appelé par con acronyme « CSV ». Attention, `OP_CSV` ne doit pas être confondu avec le champs `nSequence` d'une transaction. Le premier utilise le second, mais leurs natures et leurs actions sont différentes.*

## OP_CHECKSIG (0XAC)

Vérifie la validité d'une signature par rapport à une clé publique donnée. Il prend les deux éléments du sommet de la pile : la signature et la clé publique, et évalue si la signature est correcte pour le hachage de la transaction et la clé publique spécifiée. Si la vérification est réussie, il pousse la valeur `1` (`vrai`) sur la pile, sinon `0` (`faux`). Cet opcode a été modifié dans Tapscript afin de vérifier des signatures de Schnorr.

## OP_CHECKSIGADD (0XBA)

Extrait les trois valeurs en haut de la pile : une `clé publique`, un `CScriptNum` `n` et une `signature`. Si la signature n'est pas le vecteur vide et n'est pas valide, le script se termine avec une erreur. Si la signature est valide ou est le vecteur vide (`OP_0`), deux cas de figure se présente :
* Si la signature est le vecteur vide : un `CScriptNum` avec la valeur de `n` est poussé sur la pile et l'exécution continue ;
* Si la signature n'est pas le vecteur vide et demeure valide : un `CScriptNum` avec la valeur de `n + 1` est poussé sur la pile et l'exécution continue.
Pour vulgariser, `OP_CHECKSIGADD` effectue une opération similaire à `OP_CHECKSIG`, mais au lieu de pousser `vrai` ou `faux` sur la pile, il ajoute `1` à la deuxième valeur en haut de la pile si la signature est valide, ou laisse cette valeur inchangée si la signature représente le vecteur vide.`OP_CHECKSIGADD` permet de créer les mêmes politiques multisignatures dans Tapscript qu'avec `OP_CHECKMULTISIG` et `OP_CHECKMULTISIGVERIFY` mais de manière vérifiable par lots, c'est-à-dire qu'il supprime le processus de recherche dans la vérification d'un multisig traditionnel et accélère donc la vérification tout en réduisant la charge opérationnelle sur les CPU des nœuds. Cet opcode a été ajouté dans Tapscript uniquement pour les besoins de Taproot.

## OP_CHECKSIGVERIFY (0XAD)

Effectue la même opération que `OP_CHECKSIG`, mais si la vérification de la signature échoue, le script s'arrête immédiatement avec une erreur et la transaction est donc invalide. Si la vérification réussit, le script continue sans pousser de valeur `1` (`vrai`) sur la pile. Pour résumer, `OP_CHECKSIGVERIFY` réalise l'opération `OP_CHECKSIG` suivie de `OP_VERIFY`. Cet opcode a été modifié dans Tapscript afin de vérifier des signatures de Schnorr.

## OP_CODESEPARATOR (0XAB)

Modifie le script de sortie en cours, en indiquant que seules les opérations qui suivent cet opcode seront prises en compte dans la vérification des signatures des entrées correspondantes. Cela permet de segmenter un script complexe en plusieurs parties, où chaque segment peut être signé indépendamment.

## OP_DEPTH (0X74)

Pousse le nombre d'éléments dans la pile sur la pile elle-même. Si la pile contient `N` éléments, `OP_DEPTH` ajoutera le nombre `N` en tant que nouvel élément en haut de la pile.

## OP_DROP (0X75)

Supprime l'élément situé au sommet de la pile. `OP_DROP` permet d'enlever des données devenues inutiles au cours de l'exécution du script.

## OP_DUP (0X76)

Duplique le sommet de la pile. L'élément en haut de la pile est donc copié et la copie est placée en haut de la pile.

## OP_ELSE (0X67)

Modifie le flux d'exécution dans un script conditionnel : il indique que les opérations qui le suivent doivent être exécutées si la condition précédente spécifiée par un `OP_IF`, un `OP_NOTIF` ou un autre `OP_ELSE` n'est pas remplie.

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_IF**](./O.md#op_if-0x63).*

## OP_ENDIF (0X68)

Marque la fin d'une structure de contrôle conditionnelle initiée par un `OP_IF` ou un `OP_NOTIF`, normalement suivis par un ou plusieurs `OP_ELSE`. Il indique que l'exécution du script doit continuer au-delà de la structure conditionnelle, quelle que soit la branche qui a été exécutée. Autrement dit, `OP_ENDIF` permet de délimiter la fin des blocs conditionnels dans les scripts.

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_IF**](./O.md#op_if-0x63).*

## OP_EQUAL (0X87)

Compare les deux valeurs les plus hautes de la pile et pousse `1` sur la pile si elles sont égales, sinon pousse 0. `OP_EQUAL` permet de vérifier l'égalité des données dans les scripts de transaction.

## OP_EQUALVERIFY (0X88)

Combine les fonctions de `OP_EQUAL` et `OP_VERIFY`. Il vérifie d'abord l'égalité des deux valeurs supérieures de la pile, puis exige que le résultat soit non nul, faute de quoi la transaction est invalide. `OP_EQUALVERIFY` est notamment utilisé dans les scripts de vérification d'adresse.

## OP_EVAL

Opcode proposé par Gavin Andresen en 2011. Il prend le script situé au sommet de la pile, l'exécute comme s'il faisait partie du `scriptPubKey`, et place son résultat sur la pile. `OP_EVAL` a été abandonné en raison de préoccupations liées à la complexité de cet opcode, qui sera finalement supplanté par `P2SH`.

## OP_FALSE (0X00)

Identique à `OP_0`.

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_0**](./O.md#op_0-0x00).*

## OP_FROMALTSTACK (0X6C)

Retire le sommet de la pile alternative (alt stack) et le place sur le sommet de la pile principale (main stack). Cet opcode est utilisé pour récupérer des données stockées temporairement sur la pile alternative. Pour simplifier, c'est l'opération inverse de `OP_TOALTSTACK`.

## OP_GREATERTHAN (0XA0)

Compare les deux éléments au sommet de la pile et vérifie si le premier élément est supérieur au deuxième. Si le premier élément est supérieur au deuxième, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OP_GREATERTHANOREQUAL (0XA2)

Compare les deux éléments au sommet de la pile et vérifie si le premier élément est supérieur ou égal au deuxième. Si le premier élément est supérieur ou égal au deuxième, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OP_HASH160 (0XA9)

Prend l'élément en haut de la pile et le remplace par son hachage en utilisant simultanément les fonctions `SHA256` et `RIPEMD160`. Ce processus en deux étapes génère une empreinte de 160 bits.

► ***NOTE :** Pour plus d'informations, voir la définition de [**SHA256**](./S.md#sha256) et [**RIPEMD160**](./R.md#ripemd160).*

## OP_HASH256 (0XAA)

Prend l'élément en haut de la pile et le remplace par son hachage en utilisant deux fois la fonction `SHA256`. L'entrée est hachée une première fois avec `SHA256` et le condensat est haché une seconde fois avec `SHA256`. Ce processus en deux étapes génère une empreinte de 256 bits.

► ***NOTE :** Pour plus d'informations, voir la définition de [**SHA256**](./S.md#sha256).*

## OP_IF (0X63)

Exécute la portion suivante du script si la valeur au sommet de la pile est non nulle (vraie). Si la valeur est nulle (fausse), ces opérations sont sautées, passant directement à celles après `OP_ELSE`, s'il est présent. `OP_IF` permet d'initier une structure de contrôle conditionnelle dans un script. Il détermine le flux de contrôle dans un script en fonction d'une condition fournie au moment de l'exécution de la transaction. `OP_IF` s'utilise avec `OP_ELSE` et `OP_ENDIF` de la manière suivante : `<condition> OP_IF <opérations si la condition est vraie> OP_ELSE <opérations si la condition est fausse> OP_ENDIF`.

## OP_IFDUP (0X73)

Duplique le sommet de la pile si celui-ci est non nul. Si la valeur en haut de la pile est vraie (c'est-à-dire non nulle), cette valeur est dupliquée sur la pile ; sinon, la pile reste inchangée.

## OP_LESSTHAN (0X9F)

Compare les deux éléments au sommet de la pile et vérifie si le premier élément est inférieur au deuxième. Si le premier élément est inférieur au deuxième, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OP_LESSTHANOREQUAL (0XA1)

Compare les deux éléments au sommet de la pile et vérifie si le premier élément est inférieur ou égal au deuxième. Si le premier élément est inférieur ou égal au deuxième, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OP_MAX (0XA4)

Sélectionne le plus grand des deux éléments en haut de la pile et le pousse sur la pile. Cette opération conserve uniquement la plus grande des deux valeurs au sommet.

## OP_MIN (0XA3)

Sélectionne le plus petit des deux éléments en haut de la pile et le pousse sur la pile. Cette opération conserve uniquement la plus petite des deux valeurs au sommet.

## OP_NEGATE (0X8F)

Inverse le signe de l'élément supérieur de la pile. Si la valeur est positive, elle devient négative, et vice versa.

## OP_NIP (0X77)

Supprime l'élément situé juste en dessous du sommet de la pile (le second en partant du haut).

## OP_NOP (0X61)

Ne produit aucun effet sur la pile ou l'état du script. Il ne fait aucun déplacement, aucune vérification, ni aucune modification. Il ne fait juste rien, à moins que l'on ait décidé qu'il fasse quelque chose via un soft fork. En effet, depuis leurs modifications par Satoshi Nakamoto en 2010, les commandes `OP_NOP` (`OP_NOP1` (`0XB0`) jusqu'à `OP_NOP10` (`0XB9`)) sont utilisées pour ajouter de nouveaux opcodes sous forme de soft fork. Ainsi, l'`OP_NOP2` (`0XB1`) et l'`OP_NOP3` (`0XB2`) ont déjà été utilisés pour implémenter respectivement l'`OP_CHECKLOCKTIMEVERIFY` et l'`OP_CHECKSEQUENCEVERIFY`. On les utilise en combinaison avec `OP_DROP` afin de supprimer de la pile les valeurs temporelles associées, et ainsi pouvoir continuer l'exécution du script, que le nœud soit à jour ou non. Les `OP_NOP` permettent donc d'insérer un point d'interruption dans un script pour vérifier des conditions supplémentaires déjà existantes ou pouvant être ajoutées avec de futurs soft fork. Depuis Tapscript, l'utilisation des `OP_NOP` a été remplacée par l'utilisation des `OP_SUCCESS` étant plus efficace.

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_SUCCESS**](./O.md#op_success).*

## OP_NOT (0X91)

Inverse la valeur booléenne du sommet de la pile : si cette valeur est non nulle, l'opérateur la remplace par 0, sinon par 1.

## OP_NOTIF (0X64)

Fonctionne de manière opposée à `OP_IF`, exécutant la portion suivante du script si la valeur au sommet de la pile est nulle (fausse).

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_IF**](./O.md#op_if-0x63).*

## OP_NUMEQUAL (0X9C)

Compare les deux éléments au sommet de la pile pour vérifier s'ils sont numériquement égaux. Si les valeurs sont égales, il pousse `1` (vrai) sur la pile, sinon, il pousse `0` (faux).

## OP_NUMEQUALVERIFY (0X9D)

Combine les opérations `OP_NUMEQUAL` et `OP_VERIFY`. Il compare numériquement les deux éléments au sommet de la pile. Si les valeurs sont égales, `OP_NUMEQUALVERIFY` supprime le résultat `vrai` de la pile et continue l'exécution du script. Si les valeurs ne sont pas égales, le résultat est `faux` et le script échoue immédiatement.

## OP_NUMNOTEQUAL (0X9E)

Compare les deux éléments au sommet de la pile pour vérifier s'ils sont numériquement non égaux. Si les valeurs ne sont pas égales, il pousse `1` (vrai) sur la pile, sinon, il pousse `0` (faux). C'est l'inverse de `OP_NUMEQUAL`.

## OP_OVER (0X78)

Duplique le deuxième élément à partir du haut de la pile et le place sur le haut de la pile.

## OP_PICK (0X79)

Duplique un élément de la pile et le place en haut de la pile, en fonction de la profondeur spécifiée par la valeur en haut de la pile avant l'opération. Par exemple, si la valeur en haut de la pile est `4`, `OP_PICK` va dupliquer le quatrième élément de la pile en partant du sommet, et il va placer cette copie au sommet.

## OP_PUSHDATA1 (0X4C)

Pousse une certaine quantité de données sur la pile. Il est suivi d'un octet qui indique la longueur des données à pousser (jusqu'à 255 octets). Cet opcode est utilisé pour inclure des données de taille variable dans les scripts.

## OP_PUSHDATA2 (0X4D)

Permet de pousser une grande quantité de données sur la pile. Il est suivi de deux octets (petit-boutistes) qui spécifient la longueur des données à pousser (jusqu'à 65535 octets). Il est utilisé pour insérer des données plus volumineuses dans les scripts.

## OP_PUSHDATA4 (0X4E)

Permet de pousser une très grande quantité de données sur la pile. Il est suivi de quatre octets (petit-boutistes) qui indiquent la longueur des données à pousser (jusqu'à 4 294 967 295 octets). Cet opcode est utilisé pour insérer de très grandes données dans les scripts, bien que son usage soit extrêmement rare en raison des limitations pratiques de la taille des transactions.

## OP_RETURN (0X6A)

Signale un script invalide, ce qui rend l'output qui le contient comme non dépensable de manière prouvée. Les nœuds du réseau peuvent donc supprimer cet output de leurs UTXO set. `OP_RETURN` est souvent utilisé pour inscrire des données arbitraires dans la blockchain.

## OP_RIPEMD160 (0XA6)

Prend l'élément en haut de la pile et le remplace par son hachage en utilisant la fonction `RIPEMD160`.

► ***NOTE :** Pour plus d'informations, voir la définition de [**RIPEMD160**](./R.md#ripemd160).*

## OP_ROLL (0X7A)

Déplace un élément de la pile et en haut de la pile, en fonction de la profondeur spécifiée par la valeur en haut de la pile avant l'opération. Par exemple, si la valeur en haut de la pile est `4`, `OP_ROLL` va sélectionner le quatrième élément de la pile en partant du sommet, et il va déplacer cette valeur au sommet. `OP_ROLL` joue le même rôle que `OP_PICK`, mis à part qu'il retire l'élément de sa position initiale.

## OP_ROT (0X7B)

Déplace au sommet de la pile le troisième élément à partir du sommet de la pile. Les deux éléments qui étaient au-dessus de lui sont poussés en dessous dans l'ordre inverse.

## OP_SHA1 (0XA7)

Prend l'élément en haut de la pile et le remplace par son hachage en utilisant la fonction `SHA1`. L'utilisation de cette fonction est aujourd'hui déconseillée dans un cadre sécurisé.

## OP_SHA256 (0XA8)

Prend l'élément en haut de la pile et le remplace par son hachage en utilisant la fonction `SHA256`.

► ***NOTE :** Pour plus d'informations, voir la définition de [**SHA256**](./S.md#sha256).*

## OP_SIZE (0X82)

Mesure la taille en nombre d'octets de l'élément en haut de la pile et renvoie cette taille au sommet de la pile, sans pour autant modifier l'élément analysé en lui-même.

## OP_SUB (0X94)

Soustrait les deux éléments au sommet de la pile. Il prend les deux valeurs en haut de la pile, il les soustrait et il les remplace par le résultat.

## OP_SUCCESS

Les `OP_SUCCESS` représentent une série d'opcodes qui ont été désactivés par le passé et qui sont dorénavant réservés pour une utilisation future dans Tapscript. Leur but final est de faciliter des mises à jour et des extensions du langage script, en permettant l'introduction de nouvelles fonctionnalités via des soft forks. Lorsqu'un de ces opcodes est rencontré dans un script, il indique un succès automatique de cette partie du script, peu importe les données ou les conditions présentes. Cela signifie que le script continue son exécution sans échec, indépendamment des opérations précédentes. Ainsi, lorsque l'on ajoute un nouvel opcode sur un `OP_SUCCESS`, cela représente forcément l'ajout d'une règle plus restrictive que la règle précédente. Les nœuds à jour peuvent alors vérifier le respect de cette règle et les nœuds pas à jour ne refuseront pas les transactions associées et les blocs qui les incluent, car l'`OP_SUCCESS` valide cette partie du script. Il n'y a donc pas de hard fork. En comparaison, les `OP_NOP` (*No Operation*) servent également de marqueurs de place dans le script, mais ils n'ont aucun effet sur l'exécution du script. Lorsqu'un `OP_NOP` est rencontré, le script continue simplement sans modifier l'état de la pile ou le déroulement du script. La différence clé est donc dans leur impact sur l'exécution : `OP_SUCCESS` garantit un passage réussi à travers cette portion du script, tandis que `OP_NOP` est neutre, n'affectant ni la pile ni le flux du script. Ces opcodes sont désignés par `OP_SUCCESSN` où `N` est un numéro permettant de différencier les `OP_SUCCESS`.

## OP_SWAP (0X7C)

Échange les deux éléments en haut de la pile. L'élément qui était au sommet est déplacé en deuxième position, et l'élément qui était en deuxième position est placé au sommet de la pile.

## OP_TOALTSTACK (0X6B)

Prend le sommet de la pile principale (main stack) et le déplace vers la pile alternative (alt stack). Cet opcode permet de stocker temporairement des données à part pour une utilisation ultérieure dans le script. L'élément déplacé est donc supprimé de la pile principale. On utilisera ensuite `OP_FROMALTSTACK` pour le remettre au sommet de la pile principale.

## OP_TRUE (0X51)

Identique à OP_1.

► ***NOTE :** Pour plus d'informations, voir la définition de [**OP_1**](./O.md#op_1-0x51).*

## OP_TUCK (0X7D)

Copie l'élément situé au sommet de la pile et l'insère entre le deuxième élément et le troisième élément de la pile. Par exemple, si la pile est `D C B A`, `OP_TUCK` va dupliquer le sommet `A` et le placer en troisième position. La pile en sortie sera : `D C A B A`.

## OP_VER (0X62)

Permettait de pousser la version du client sur la pile. Cet opcode a été désactivé car s'il avait été utilisé, chaque mise à jour aurait conduit à un hard fork. Le BIP342 a modifié cet opcode en `OP_SUCCESS`.

## OP_VERIFY (0X69)

Exige que la valeur du sommet de la pile soit non nulle (vraie). La transaction est invalide si ce n'est pas le cas. `OP_VERIFY` est utilisé pour confirmer les conditions des scripts.

## OP_WITHIN (0XA5)

Vérifie si le premier élément en haut de la pile se trouve dans l'intervalle défini par les deuxième et troisième éléments supérieurs. Autrement dit, `OP_WITHIN` vérifie si le premier élément est supérieur ou égal au deuxième et inférieur au troisième. Si cette condition est vraie, il pousse `1` (`vrai`) sur la pile, sinon, il pousse `0` (`faux`).

## OPCODES

Ensemble des commandes utilisées dans le système script de Bitcoin. Script est un langage de programmation à pile utilisé pour établir des conditions de dépense, et donc, indirectement, sécuriser des bitcoins. Les instructions utilisées en langage script sont appelées « OPcodes ». Ce sont des opérateurs logiques et des commandes pour manipuler les piles (stacks). Ces instructions spécifiques sont exécutées par les nœuds du réseau lors de l'ajout d'une transaction à la blockchain. Script est un langage non-Turing complet. Il peut-être catégorisé comme un langage de niveau intermédiaire (presque bas niveau) inspiré du Forth.

► ***NOTE :** « OPcode » peut être traduit en français par « code opératoire ». Dans la pratique, on utilise directement le terme « OPcode » dans le langage courant. Pour plus d'informations, voir les définitions de **[PILE (STACK)](./P.md#pile-stack)** et **[SCRIPT](./S.md#script)**.*

## OPEN ASSETS PROTOCOL (OAP)

Le Protocole Open Assets (OAP), conçu par Flavien Charlon en 2013, représente la première mise en œuvre fonctionnelle des Colored Coins. Ce protocole permettait de stocker et de transférer des actifs non natifs sur la blockchain Bitcoin, sous la forme de tokens dénommés « Colored Coins ». Ces derniers sont marqués spécifiquement pour symboliser une promesse, qu'elle soit formelle ou informelle, d'échange contre des biens ou services réels.

## ORACLE

Source d'informations tierce qui fournit des données du monde réel pouvant être interprétées sur Bitcoin. Les oracles permettent aux contrats intelligents, tels que les DLC, d'exécuter des conditions contractuelles en fonction d'événements extérieurs. En général, ils fournissent une signature spécifique qui correspond au résultat d'un événement. Cette signature est ensuite utilisée pour compléter et rendre valide une transaction d'exécution qui envoie les bitcoins à la partie qui est censée les recevoir selon les conditions du contrat intelligent.

► ***NOTE :** Pour plus d'informations, voir la définition de [**DLC (DISCREET LOG CONTRACT)**](./D.md#dlc-discreet-log-contract).*

## ORDINAL NUMBER

Dans le cadre du protocole Ordinals, c'est un identifiant unique attribué à chaque sat en fonction de son ordre de minage dans un bloc. Ces numéros permettent de rendre non fongibles ces sats selon le protocole Ordinals, et donc de suivre et de transférer ces sats spécifiques.

► ***NOTE :** En français, on peut traduire ce terme par « Nombre Ordinal ». Pour plus d'informations, voir les définitions de **[ORDINALS THEORY](./O.md#ordinals-theory)**, **[INSCRIPTIONS](./I.md#inscriptions)** et de **[DIGITAL ARTIFACTS](./D.md#digital-artifacts)**.*

## ORDINALS THEORY

Protocole externe à Bitcoin qui attribue des numéros de série aux sats (la plus petite unité de bitcoin), qui permettent de les tracer de manière individuelle et de les transférer via des transactions Bitcoin. Selon la théorie des Ordinals, chaque sat est numéroté selon l'ordre dans lequel il a été miné et est transféré de manière FIFO (*First-In-First-Out*). L'objectif de cette théorie est de rendre des sats non fongibles selon leur interprétation au sein du protocole Ordinals, afin de leur associer des informations externes comme des images (NFT) que l'on appelle des "inscriptions".

► ***NOTE :** En français, on peut traduire ce terme par « Théorie des Ordinals ». Pour plus d'informations, voir les définitions de **[INSCRIPTIONS](./I.md#inscriptions)** et de **[DIGITAL ARTIFACTS](./D.md#digital-artifacts)**.*

## ORPHELIN

Théoriquement, un bloc orphelin désigne un bloc valide réceptionné par un nœud qui n'a pas encore acquis le bloc parent, c'est-à-dire le précédent dans la chaîne. Ce bloc, bien que valide, demeure isolé localement en tant qu'orphelin. Cependant, dans l'usage courant, l'expression « bloc orphelin » fait souvent référence à un bloc sans enfant : un bloc valide mais non retenu dans la chaîne principale de Bitcoin. Il se produit lorsque deux mineurs trouvent un bloc valide sur une même hauteur de chaîne durant un court laps de temps et le diffusent sur le réseau. Le réseau finit par choisir un seul bloc à inclure dans la chaîne, selon le principe de la chaîne avec le plus de quantité de travail accumulé, rendant l'autre « orphelin ».

![](assets/9.png)

► ***NOTE :** Personnellement, je préfère employer le terme de « bloc orphelin » pour parler d'un bloc sans parent et le terme de « bloc obsolète » (stale block) pour désigner un bloc qui n'a pas d'enfant. Je trouve cela plus logique et compréhensible, bien qu'une majorité de bitcoiners ne suivent pas cet usage. Pour plus d'informations, voir la définition de [**OBSOLÈTE**](./O.md#obsolète).*

## OSINT

Acronyme de « *Open Source Intelligence* ». L'OSINT désigne la collecte et l'analyse d'informations disponibles publiquement à partir de sources accessibles à tous. Ces sources peuvent inclure des sites web, des forums, des réseaux sociaux, des bases de données publiques, des publications académiques, des documents gouvernementaux, etc... L'objectif principal de l'OSINT est de transformer des données brutes en informations exploitables, en identifiant des tendances, des corrélations, et des pistes d'investigation. Dans le cadre de Bitcoin, l'OSINT peut être utilisée dans le but d'appuyer une analyse de chaîne pour tracer des fonds, notamment afin d'identifier un point d'entrée, c'est-à-dire un lien entre une activité onchain et une forme d'identité appartenant à une entité réelle. Par exemple, si vous publiez votre adresse de réception sur Twitter sous votre nom, un analyste pourrait la retrouver et l'associer à votre identité.

![](assets/28.png)

## OU EXCLUSIF

Fonction fondamentale de la logique booléenne. Le « Ou exclusif » ou XOR (« Exclusive or ») prend deux opérandes booléens, chacun étant `vrai` ou `faux`, et produit une sortie `vraie` uniquement lorsque les deux opérandes diffèrent. Autrement dit, la sortie de l'opération `XOR` est `vraie` si exactement un (mais pas les deux) des opérandes est `vrai`. Par exemple, l'opération `XOR` entre `1` et `0` donnera comme résultat `1`. Nous noterons : $1 \oplus 0 = 1$. De même, l'opération `XOR` peut être effectuée sur des séquences plus longues de bits. Par exemple, $10110 \oplus 01110 = 11000$. Chaque bit de la séquence est comparé à son homologue et l'opération `XOR` est appliquée. Voici la table de vérité de l'opération `XOR` :

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
* Il dispose d'un élément neutre `0` : Une opérande xorée à 0 sera toujours égale à l'opérande. Pour une variable $A$ donnée : $A \oplus 0 = A$ ;
* Chaque élément est son propre inverse. Pour une variable $A$ donnée : $A \oplus A = 0$.

Dans le cadre de Bitcoin, on utilise évidement l'opération `XOR` à de nombreux endroits. Par exemple, le `XOR` est massivement utilisé dans la fonction `SHA256`, elle-même largement utilisée dans le protocole Bitcoin. Certains protocoles comme le *SeedXOR* de Coldcard utilisent également cette primitive pour d'autres applications. On le retrouve aussi dans le BIP47 pour chiffrer le code de paiement réutilisable lors de sa transmission. Dans le domaine plus général de la cryptographie, le `XOR` peut être utilisé tel quel comme un algorithme de chiffrement symétrique. On appelle cet algorithme le « Masque Jetable » ou le « Chiffre Vernam » du nom de son inventeur. Cet algorithme, bien qu'inutile en pratique du fait de la longueur de la clé, est un des seuls algorithmes de chiffrement reconnus comme inconditionnellement sûrs.

## OUTBOUND CAPACITY

Désigne la quantité maximale de bitcoins qu'un nœud peut envoyer à travers un canal spécifique sur le Lightning Network. Elle dépend des fonds que le nœud a engagés dans le canal lors de son ouverture, ou qu'il a reçus lors d'un paiement Lightning.

► ***NOTE :** En français, on peut le traduire par « capacité sortante ».*

## OUTPOINT

Référence unique à une sortie de transaction non dépensé (UTXO). Il est constitué de deux éléments :
* `txid` : l'identifiant de la transaction qui a créé l'output ;
* `vout` : l'index de l'output dans la transaction.

La combinaison de ces deux éléments permet d'identifier précisément un UTXO. Par exemple, si une transaction a un "txid" de `abc123` et que l'index de l'output est `0`, l'outpoint sera noté comme `abc123:0`. L'outpoint est utilisé dans les inputs ("vin") d'une nouvelle transaction pour indiquer quel UTXO est dépensé.

► ***NOTE :** Le terme « outpoint » est souvent utilisé comme synonyme de « UTXO ».*

## OUTPUT

Traduction anglaise de « sortie ». Dans le contexte de Bitcoin, une « sortie » au sein d’une transaction fait référence aux _Unspent Transaction Outputs_ (UTXO) qui sont créés comme fonds de destination pour le paiement. Plus précisément, il s'agit d'un mécanisme par lequel une transaction distribue des fonds. Une transaction prend des UTXO, c’est-à-dire des morceaux de bitcoins, comme « inputs » (entrées) et crée de nouveaux UTXO comme « outputs » (sorties). Ces outputs stipulent une certaine quantité de bitcoins, souvent attribués à une adresse spécifique, ainsi que les conditions sous lesquelles ces fonds peuvent être dépensés ultérieurement. Le rôle de la transaction Bitcoin est donc de consommer des UTXO en entrées, et de créer des nouveaux UTXO en sorties. La différence entre les deux correspond aux frais de transactions qui peuvent être récupérés par le mineur gagnant du bloc. Un UTXO est, en essence, la sortie d'une transaction précédente qui n'a pas encore été dépensée. Les outputs de transaction sont donc les créations de nouveaux UTXO qui seront, à leur tour, potentiellement utilisés comme inputs dans les transactions futures. D'un point de vue plus large, en informatique, le terme « output » ou « sortie » désigne généralement les données en résultat d’une fonction, d’un algorithme, ou d’un système. Par exemple, lorsque l’on passe une donnée dans une fonction de hachage cryptographique, cette information est nommée « entrée » ou « input », et le résultat est nommé « sortie » ou « output ».

## OUTPUT LINKING

Synonyme parfois utilisé pour parler de réutilisation d'adresse. L'output linking se réfère à la pratique d'utiliser une même adresse de réception pour bloquer plusieurs UTXO, parfois au sein de plusieurs transactions différentes. Les bitcoins sont généralement bloqués à l'aide d'une paire de clés cryptographique qui correspond à une adresse unique. Puisque la blockchain est publique, il est facile de pouvoir consulter quelles adresses sont associées à combien de bitcoins. En cas de réutilisation d'une même adresse pour plusieurs paiements, on peut raisonnablement imaginer que tous les UTXO associés appartiennent à une même entité. La réutilisation d'adresse pause donc un problème pour la vie privée de l'utilisateur. Elle permet de faire des liens déterministes entre plusieurs transactions et plusieurs UTXO, ainsi que de perpétuer un traçage de fonds on-chain.

► ***NOTE :** Pour plus d'informations, voir la définition de [RÉUTILISATION D'ADRESSE](./R.md#réutilisation-dadresse).*

## OUTPUT SCRIPT DESCRIPTORS

Les output script descriptors, ou simplement descriptors, sont des expressions structurées qui décrivent intégralement un script de sortie (scriptPubKey) et fournissent toutes les informations nécessaires pour suivre les transactions vers ou depuis un script particulier. Ces descriptors facilitent la gestion des clés dans les portefeuilles HD grâce à une description standard de la structure et des types d'adresses utilisés.

L'intérêt principal des descriptors réside dans leur capacité à encapsuler toutes les informations essentielles à la restauration d'un portefeuille dans une unique chaîne de caractères (en plus de la phrase de récupération). En sauvegardant un descriptor avec les phrases mnémonique correspondantes, il est possible de restaurer non seulement les clés privées, mais aussi la structure précise du portefeuille et les paramètres de script associés. En effet, la récupération d’un portefeuille requiert non seulement la connaissance de la graine initiale, mais aussi des index spécifiques pour la dérivation des paires de clés enfants, ainsi que des `xpub` de chaque facteur dans le cadre d'un portefeuille multisig. Autrefois, on présumait que ces informations étaient implicitement sues de tous. Cependant, avec la diversification des scripts et l'émergence de configurations plus complexes, ces informations pourraient devenir difficiles à extrapoler, transformant ainsi ces données en informations privées et difficilement bruteforçables. L'utilisation de descriptors simplifie grandement le processus : il suffit de connaître la ou les phrases de récupération et le descriptor correspondant pour tout restaurer de façon fiable et sécurisée.

Un descriptor se compose de plusieurs éléments :
* Des fonctions de script comme `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) et `sortedmulti` (Multisignature avec clés triées) ;
* Des chemins de dérivation, par exemple `[d34db33f/44h/0h/0h]` qui indique un chemin dérivé et une empreinte de clé maîtresse spécifique ;
* Des clés en divers formats tels que des clés publiques en hexadécimal ou des clés publiques étendues (`xpub`) ;
* Une somme de contrôle, précédée d'un dièse, pour vérifier l'intégrité du descriptor.

Par exemple, un descriptor pour un portefeuille P2WPKH pourrait ressembler à :

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt
7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

Dans ce descriptor, la fonction de dérivation `wpkh` indique un type de script Pay-to-Witness-Public-Key-Hash. Elle est suivie par le chemin de dérivation qui contient :
* `cdeab12f` : l'empreinte de la clé maîtresse ;
* `84h` : qui signifie l'utilisation d'un objectif BIP84, destiné aux adresses SegWit v0 ;
* `0h` : qui indique qu'il s'agit d'une devise BTC sur le mainnet ;
* `0h` : qui fait référence au numéro de compte spécifique utilisé dans le portefeuille.

Le descriptor inclut également la clé publique étendue utilisée sur ce portefeuille : 

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2
mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Ensuite, la notation `/<0;1>/*` spécifie que le descriptor peut générer des adresses à partir de la chaîne externe (`0`) et interne (`1`), avec un wildcard (`*`) permettant la dérivation séquentielle de plusieurs adresses de manière paramétrable, similaire à la gestion d'un « gap limit » sur des logiciels de portefeuille classiques.

Enfin, `#jy0l7nr4` représente la somme de contrôle pour vérifier l'intégrité du descriptor.

## OVERT ASICBOOST

Version ouverte et transparente d'AsicBoost. AsicBoost est une technique d'optimisation algorithmique utilisée dans le minage de Bitcoin. Les mineurs utilisant la version Overt manipulent le champ `nVersion` du bloc candidat et utilisent cette modification comme un nonce supplémentaire. Cette méthode laisse le véritable champ `Nonce` du bloc inchangé lors de chaque tentative de hachage, ce qui réduit ainsi les calculs nécessaires pour chaque SHA256, en conservant certaines données identiques entre les tentatives. Cette version est détectable publiquement et ne dissimule pas ses modifications au reste du réseau, à l'inverse de la version Covert d'AsicBoost.

► ***NOTE :** Pour plus d'informations, voir les définitions de **[ASICBOOST](./A.md#asicboost)** et **[COVERT ASICBOOST](./C.md#covert-asicboost)**.*