## TAPROOT

Mise à jour majeure du protocole Bitcoin, adoptée par le biais d'un soft fork en novembre 2021. Cette mise à jour apporte des améliorations significatives en termes de confidentialité, d'efficacité et de flexibilité. Elle permet l'utilisation du protocole de Schnorr et l'utilisation d'un script qui peut être révélé lors de la dépense. Le protocole de Schnorr, intégré à cette mise à jour, est un algorithme de signature numérique établi sur la cryptographie sur les courbes elliptiques (ECC), comme ECDSA. Dans le contexte de Bitcoin, Schnorr est utilisé pour générer une clé publique à partir d'une clé privée et pour signer une transaction avec une clé privée. Comme ECDSA sur Bitcoin, Schnorr utilise la courbe elliptique `secp256k1`, définie par l'équation $y^2 = x^3 + 7$. Les bitcoins bloqués avec Taproot peuvent être dépensés soit en satisfaisant l'un des scripts, soit en fournissant une signature valide correspondant à la clé publique, ce qui permet de garder les scripts privés. On y utilise un MAST pour permettre l'utilisation de plusieurs scripts. N'importe lequel peut-être utiliser pour dépenser les bitcoins associés. Cela permet des fonctionnalités plus complexes et des contrats intelligents plus sophistiqués.

> ► *Pour plus d'informations, voir la définition de [**SCHNORR (PROTOCOLE)**](./S.md#schnorr-protocole).*

## TAPROOT ASSETS PROTOCOL

Protocole développé par Lightning Labs permettant d'émettre des actifs sur la blockchain principale de Bitcoin, en tirant partie de la mise à jour Taproot. Taproot Assets permet la création d'actifs fongibles comme des stablecoins et non fongibles comme de NFT. Les Taproot Assets peuvent être transférés via des transactions Bitcoin classiques ou via le Lightning Network. Ce protocole utilise des Merkle-Sum Sparse Merkle Trees (MS-SMT), une sorte de combinaison des MST et des SMT, pour assurer la validité et l’audibilité des actifs.

> ► *Taproot Assets Protocol s'appelait « TARO » auparavant.*

## TAPSCRIPT

Mise à jour qui a pour objet de modifier certains opcodes du langage de script classique de Bitcoin, afin de définir le nouveau langage de script utilisé pour les dépenses Taproot. Tapscript a été introduit par le BIP342 au sein du soft fork SegWit.

Afin de mettre en œuvre les diverses modifications associées à Taproot, il s'est avéré nécessaire de revisiter le langage de script. C'est là l'objet de Tapscript qui désactive ou modifie certains opcodes, et vient en ajouter de nouveaux. 

> ► *Pour plus d'informations, voir la définition de [**SCHNORR (PROTOCOLE)**](./S.md#schnorr-protocole) et [**TAPROOT**](./T.md#taproot).*

## TARO

Ancien nom du protocole Taproot Assets Protocol. 

> ► *Pour plus d'informations, voir la définition de [**TAPROOT ASSETS PROTOCOL**](./T.md#taproot-assets-protocol).*

## TAUX DE HACHAGE

Indicateur de la puissance de calcul du réseau, mesurée en hachages par seconde (H/s). Il indique la capacité des mineurs à exécuter des opérations de hachage dans le cadre de la preuve de travail. Un taux de hachage élevé signifie une plus grande sécurité de l'historique économique de Bitcoin et une plus grande résistance aux attaques, car il faudrait une quantité substantielle de puissance de calcul pour compromettre le réseau. Le taux de hachage est également indicatif de la concurrence entre les mineurs : plus le taux de hachage est élevé, plus la difficulté de minage est grande, ce qui influence la récompense et donc la rentabilité des mineurs. C'est donc un indicateur clé de la santé et de la sécurité du système Bitcoin. De la même manière que le taux de hachage sert à mesure le taux de hachage global du réseau Bitcoin, il peut également être utilisé pour mesurer le taux de hachage d'une machine, d'une ferme de minage ou encore d'une pool de minage.

> ► *En anglais, on parle de « hashrate ».*

## TCP

Sigle de « *Transmission Control Protocol* ». C'est un protocole de communication fondamental dans les réseaux, conçu pour assurer une transmission de données fiable sur Internet. Il établit une connexion, garantit l'ordre des données envoyées, gère la retransmission en cas de perte de paquets, et contrôle la congestion.

## TÉMOIN DE TRANSACTION

Fait référence à une composante des transactions Bitcoin qui a été déplacée avec le soft fork SegWit afin de résoudre le problème de la malléabilité des transactions. Le témoin contient les signatures et les clés publiques nécessaires pour déverrouiller les bitcoins dépensés dans une transaction. Dans les transactions Legacy, le témoin représentait la somme des `ScriptSig` de tous les inputs. Dans les transactions SegWit, le témoin représente la somme des `ScriptWitness` de chaque input, et cette partie de la transaction est dorénavant déplacée dans un arbre de Merkle séparé au sein du bloc. Avant SegWit, les signatures pouvaient être légèrement modifiées sans être invalidées avant qu'une transaction ne soit confirmée, ce qui changeait l'identifiant de la transaction. Cela rendait difficile la construction de divers protocoles, car une transaction non confirmée pouvait voir son identifiant changer. En séparant les témoins, SegWit rend les transactions non malléables, car tout changement dans les signatures n'affecte plus l'identifiant de la transaction (TXID), mais uniquement l'identifiant du témoin (WTXID). En plus de résoudre le problème de la malléabilité, cette séparation permet d'augmenter la capacité de chaque bloc.

> ► *En anglais, « témoin » se traduit par « witness ». Pour plus d'informations, voir la définition de **[SEGWIT](./S.md#segwit)**.*

## TESTNET

Version alternative de Bitcoin utilisée exclusivement à des fins de test et de développement. Il s'agit d'un réseau séparé du réseau principal (mainnet), avec ses propres blocs et transactions, permettant aux développeurs de tester de nouvelles fonctionnalités, applications et mises à jour sans risque pour le réseau principal. Le testnet permet également d'éviter de payer des frais de transaction lors de tests. Les bitcoins utilisés sur le testnet n'ont aucune valeur réelle.

## THE DAO

Projet lancé en 2016 sur Ethereum, qui visait à créer un fonds d'investissement autonome géré par des smart contracts. Bien que principalement lié à Ethereum, The DAO a eu un impact important sur l'évolution de Bitcoin. En juin 2016, The DAO a été victime d'un piratage massif. En réaction, la communauté Ethereum a réalisé un hardfork, qui s'est avéré être un échec retentissant. Cet incident a consolidé les positions conservatrices des small blockers durant la Blocksize War de Bitcoin. Ils ont utilisé cet événement pour argumenter contre les changements rapides dans le protocole Bitcoin, comme ceux prônés par les big blockers, et contre l'idée de réaliser des hardforks, comme cela a été le cas sur Ethereum suite au hack de The DAO.

> ► *Pour plus d'informations, voir la définition de **[BLOCKSIZE WAR](./B.md#blocksize-war)**.*

## TIDES

Sigle de « *Transparent Index Of Distinct Extended Shares* ». C'est une méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage introduite par la pool Ocean en 2023. Cette méthode répartit les récompenses en fonction d'un pourcentage pondéré du travail consacré aux shares les plus récemment trouvées. Chaque preuve est rémunérée plusieurs fois, avec un calcul de récompense incluant les frais de transaction. Ce système assure une grande précision dans les paiements des mineurs, sans nécessiter un intermédiaire de garde pour le traitement des paiements, contrairement à d'autres méthodes comme FPPS. TIDES est conçu pour des rémunérations transparentes et auditables.

> ► *Pour plus d'informations, voir la définition de **[SHARES](./S.md#shares)**.*

## TIMELOCK

Primitive de contrat intelligent qui permet de définir une condition temporelle à remplir pour qu'une transaction puisse être ajoutée à un bloc. Il existe deux types de timelocks sur Bitcoin : 
* Le timelock absolu, qui spécifie un moment précis avant lequel la transaction ne peut être incluse dans un bloc ; 
* Le timelock relatif, qui définit un délai à partir de l'acceptation d'une transaction antérieure. 
Le timelock peut être défini soit sous la forme d'une date exprimée en temps Unix, soit sous la forme d'un numéro de bloc. Enfin, le timelock peut s'appliquer soit à un output de transaction grâce à l'utilisation d'un opcode spécifique dans le script de verrouillage (`OP_CHECKLOCKTIMEVERIFY` ou `OP_CHECKSEQUENCEVERIFY`), soit à une transaction entière grâce à l'utilisation de champs de transaction spécifiques (`nLockTime` ou `nSequence`).

> ► *Pour plus d'informations, voir la définition de [**OP_CHECKLOCKTIMEVERIFY**](./O.md#op_checklocktimeverify-0xb1), [**OP_CHECKSEQUENCEVERIFY**](./O.md#op_checksequenceverify-0xb2), [**NLOCKTIME**](./N.md#nlocktime) et [**NSEQUENCE**](./N.md#nsequence).*

## TOR (THE ONION ROUTER)

Réseau de serveurs relais (nodes) qui permet d'anonymiser l'origine des connexions TCP sur internet. Il fonctionne en encapsulant les données dans plusieurs couches de chiffrement. Chaque nœud de relais enlève une couche pour révéler l'adresse du nœud suivant, jusqu'à atteindre la destination finale. Le réseau Tor assure l'anonymat en empêchant les nœuds intermédiaires de connaître à la fois l'origine et la destination des données, ce qui rend très difficile pour un observateur de retracer l'activité de l'utilisateur. Le réseau TOR peut être utilisé dans le cadre de Bitcoin pour éviter d'associer son adresse IP à un nœud Bitcoin, et donc éviter de faire fuiter certaines informations personnelles.

> ► *« TOR » signifie « The Onion Router ». Il est important de différencier TOR le réseau, et TOR Browser, un navigateur web établi sur Firefox qui est spécialement conçu pour utilise le réseau TOR.*

## TPRV

Préfixe de clé privée étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet.

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## TPUB

Préfixe de clé publique étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet. 

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## TRANSACTION (TX)

Dans le contexte de Bitcoin, une transaction (abrégée « TX ») est une opération enregistrée sur la blockchain qui transfère la propriété de bitcoins d'une ou plusieurs entrées (inputs) vers une ou plusieurs sorties (outputs). Chaque transaction consomme des UTXO en entrées, qui sont des outputs de transactions précédentes, et crée de nouveaux UTXO en sorties, qui peuvent être utilisés comme entrants dans des transactions futures. Chaque entrée comporte une référence à un output existant ainsi qu'un script de signature qui rempli les conditions de dépense établies par l'output auquel il fait référence. C'est ce qui permet de débloquer des bitcoins. Les outputs définissent de nouvelles conditions de dépense pour les bitcoins transférés, souvent sous la forme d'une clé publique ou d'une adresse à laquelle les bitcoins sont maintenant associés.

## TRANSACTION COINBASE

La transaction coinbase est une transaction spéciale et unique incluse dans chaque bloc de la blockchain Bitcoin. Elle représente la première transaction d'un bloc et est créée par le mineur qui a réussi à trouver un entête validant la preuve de travail (Proof-of-Work). La transaction coinbase sert principalement deux objectifs : attribuer la récompense de bloc au mineur et ajouter de nouvelles unités de bitcoins à la masse monétaire en circulation. La récompense de bloc, qui est l'incitation économique pour les mineurs à contribuer à s'adonner à la preuve de travail, comprend les frais accumulés pour les transactions incluses dans le bloc et un montant déterminé de bitcoins nouvellement créés ex-nihilo (subvention de bloc). Ce montant, initialement fixé à 50 bitcoins par bloc en 2009, est réduit de moitié tous les 210 000 blocs (environ tous les 4 ans) lors d'un événement appelé « halving ». La transaction coinbase diffère des transactions régulières de plusieurs manières. Tout d'abord, elle n'a pas d'entrée (input), ce qui signifie qu'aucune sortie de transaction existante (UTXO) n'y est dépensée. Ensuite, le script de signature `scriptSig` pour la transaction coinbase contient généralement un champ arbitraire permettant d'incorporer des données supplémentaires, telles que des messages personnalisés ou des informations de version de logiciel de minage. Enfin, les bitcoins générés par la transaction coinbase sont soumis à une période de maturité de 100 blocs (101 confirmations) avant de pouvoir être dépensés, afin de prévenir les dépenses potentielles de bitcoins non existants en cas de réorganisation de la chaîne.

## TRANSACTION COLLABORATIVE

Transaction Bitcoin qui implique plusieurs entités différentes en input de la transaction. Il s'agit donc également d'un modèle de transaction qui peut être utilisé en analyse de chaîne. L'exemple typique d'une transaction collaborative est le coinjoin, où plusieurs utilisateurs regroupent des montants équivalents en inputs pour récupérer l'intégralité de la somme (moins les frais de transaction) dans des outputs de même montant, afin d'empêcher le traçage des pièces.

> ► *Pour plus d'informations, voir la définition de **[COINJOIN](./C.md#coinjoin)**.*

## TRANSACTION D'ENGAGEMENT

Dans le contexte d'un canal bidirectionnel au sein de Lightning, la transaction d'engagement est une transaction que les deux parties créent et signent, sans toutefois la publier sur la chaîne principale. Elle représente l'état actuel de la répartition des fonds entre les parties d'un canal, chaque paiement Lightning résultant en une nouvelle transaction d'engagement. Ces transactions sont valides, mais ne sont diffusées que lorsque le canal est clôturé unilatéralement. Elles contiennent des sorties pour chaque partie, reflétant la répartition des fonds selon les paiements Lightning effectués depuis l'ouverture du canal. Des mécanismes de pénalité sont associés pour dissuader les parties de diffuser des états obsolètes du canal, c'est-à-dire des vielles transactions d'engagement.

## TRANSACTION NON CONFIRMÉE

Transaction Bitcoin qui a été diffusée sur le réseau mais n'a pas encore été incluse dans un bloc par un mineur. Elle reste dans les mempools des nœuds, en attente d'avoir des confirmations. La confirmation se produit lorsque la transaction est intégrée dans un bloc valide ajouté à la blockchain. Le temps nécessaire pour qu'une transaction soit confirmée dépend des frais de transaction payés et de la congestion du système.

## TRANSACTION STANDARD

Transaction Bitcoin qui, en plus de respecter les règles de consensus, entre également dans les règles de standardisation configurées par défaut sur les nœuds Bitcoin Core. Ces règles de standardisation sont imposées individuellement par chaque nœud Bitcoin, en plus des règles de consensus, pour définir la structure des transactions non confirmées qu'il accepte dans sa mempool et diffuse à ses pairs.

Ces règles sont donc configurées et exécutées en local par chaque nœud et peuvent varier d'un nœud à l'autre. Elles s'appliquent exclusivement sur les transactions non confirmées. Ainsi, un nœud n'acceptera une transaction qu'il jugerait non standard que si celle-ci est déjà incluse dans un bloc valide. 

Notons que la majorité des nœuds laissent les configurations par défaut telles que préétablies dans Bitcoin Core, engendrant de fait une homogénéité des règles de standardisation à travers le réseau. Une transaction qui, bien que conforme aux règles de consensus, ne respecte pas ces règles de standardisation, aura des difficultés à se propager sur le réseau. Elle pourra toutefois être incluse dans un bloc valide si jamais elle atteint un mineur. Dans la pratique, ces transactions, qualifiées de non standard, sont souvent transmise directement à un mineur par des voies externes au réseau pair-à-pair de Bitcoin. C'est souvent le seul moyen pour confirmer ce type de transaction. Par exemple, une transaction qui n'alloue aucun frais est à la fois valide selon les règles de consensus et non standard car la politique par défaut de Bitcoin Core pour le paramètre `minRelayTxFee` est de `0.00001` (en BTC/kB).

## TUMBLEBIT

Concept de hub de paiement anonyme compatible avec Bitcoin proposé en 2016 par Ethan Heilman, Leen AlShenibr, Foteini Baldimtsi, Alessandra Scafuro et Sharon Goldberg. TumbleBit est un système de mixage de bitcoins qui ne requiert pas la confiance en un intermédiaire. Il permet à des utilisateurs de réaliser des paiements rapides, anonymes et hors-chaîne via un coordinateur appelé le Tumbler. TumbleBit garantit l'anonymat en s'assurant que même le Tumbler ne peut pas lier le paiement d'un payeur à son bénéficiaire. Le protocole TumbleBit assure que le Tumbler ne peut ni voler des bitcoins, ni imprimer de faux bitcoins en s'émettant des paiements à lui-même. L'anonymat offert par TumbleBit est comparable à celui d'un système eCash de Chaum. Cependant, ce concept n'a jamais été largement adopté, les techniques de confidentialité telles que le Chaumian coinjoin lui étant préférées.

> ► *Pour plus d'informations, voir la définition de [**COINJOIN**](./C.md#coinjoin).*

## TWO-WAY PEG (2WP)

Mécanisme qui permet d'établir une connexion entre le système principal de Bitcoin et une sidechain (ou une drivechain), c'est-à-dire une chaîne latérale. Le 2WP assure une corrélation de valeur fixe entre les bitcoins sur la blockchain principale et les actifs correspondants sur la sidechain, permettant ainsi de déplacer des bitcoins entre les deux chaînes. Pour ce faire, les bitcoins sont temporairement verrouillés sur la blockchain principale et un montant équivalent d'actifs est émis sur la sidechain. Cela permet de profiter des avantages spécifiques de la sidechain, comme des transactions plus rapides ou des fonctionnalités de confidentialité améliorées, tout en maintenant la valeur des bitcoins utilisés. Lorsque les utilisateurs souhaitent revenir à la blockchain Bitcoin, le processus s'inverse : les actifs sur la sidechain sont détruits et les bitcoins correspondants sont déverrouillés. Il existe de nombreux mécanismes d'ancrages bilatéraux différents qui peuvent reposer sur :
* Un tiers de confiance unique ;
* Une fédération d'entités ;
* Les mineurs de la chaîne principale (drivechain).

> ► *En français, on parle d'un « ancrage bilatéral ».*

## TXID (TRANSACTION IDENTIFIER)

Identifiant unique associé à chaque transaction Bitcoin. Il est généré en calculant le hachage `SHA256d` des données de la transaction. Le TXID sert de référence pour retrouver une transaction spécifique au sein de la blockchain. Il est également utilisé pour pour faire référence à un UTXO, qui est essentiellement la concaténation du TXID d'une transaction précédente et de l'index de l'output désigné (également appelé « vout »). Pour les transaction post-SegWit, le TXID ne prend plus en compte le témoin de la transaction, ce qui permet de supprimer la malléabilité.

> ► *Pour plus d'informations, voir la définition de [**WTXID**](./W.md#wtxid).*

## TYPE DE DEVISE

Dans le cadre des portefeuilles déterministes et hiérarchiques (HD), le type de devise (*coin type* en anglais) est un niveau de dérivation qui permet de différencier les branches du portefeuille en fonction des différentes cryptomonnaies utilisées. Cette profondeur, définie par le BIP 44, se situe en profondeur 2 de la structure de dérivation, après la clé maîtresse et l'objectif. Par exemple, pour Bitcoin, l'index attribué est `0x80000000`, noté `/0'/` dans le chemin de dérivation. Cela signifie que toutes les adresses et comptes dérivés de ce chemin sont associés à Bitcoin. Cet étage de dérivation permet de bien séparer les différents actifs dans un portefeuille multi-devises. Voici les index utilisés pour différentes cryptomonnaies :
* Bitcoin : `0x80000000` ;
* Bitcoin Testnet : `0x80000001` ;
* Litecoin : `0x80000002` ;
* Dogecoin : `0x80000003` ;
* Ethereum : `0x8000003c`...

![](assets/21.png)

> ► *Pour plus d'informations, voir la définition de [**CHEMIN DE DÉRIVATION**](./C.md#chemin-de-dérivation).*

## TWEAK (CLÉ PUBLIQUE)

Dans le domaine de la cryptographie, « tweaker » une clé publique consiste à modifier cette clé en utilisant une valeur additive appelée le « tweak » de telle sorte qu'elle reste utilisable avec la connaissance de la clé privée d'origine et du tweak. Techniquement, un tweak est une valeur scalaire qui est ajoutée à la clé publique initiale. Si `P` est la clé publique et `t` est le tweak, la clé publique tweaked devient `P' = P + tG`, où G est le générateur de la courbe elliptique utilisée. Cette opération permet d'obtenir une nouvelle clé publique dérivée de la clé originale tout en conservant certaines propriétés cryptographiques permettant de l'utiliser. Par exemple, on utilise cette méthode pour les adresses Taproot (P2TR) afin de pouvoir dépenser soit en présentant une signature Schnorr de façon traditionnelle, soit en remplissant l'une des conditions énoncées dans un arbre de Merkle, également appelé « MAST ».

![](assets/26.png)

