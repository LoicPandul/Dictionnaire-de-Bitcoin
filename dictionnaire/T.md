## TAPROOT

Mise à jour majeure du protocole Bitcoin, adoptée par le biais d'un soft fork en novembre 2021. Cette mise à jour apporte des améliorations significatives en termes de confidentialité, d'efficacité et de flexibilité. Elle permet l'utilisation du protocole de Schnorr et l'utilisation d'un script qui peut être révélé lors de la dépense. Le protocole de Schnorr, intégré à cette mise à jour, est un algorithme de signature numérique établi sur la cryptographie sur les courbes elliptiques (ECC), comme ECDSA. Dans le contexte de Bitcoin, Schnorr est utilisé pour générer une clé publique à partir d'une clé privée et pour signer une transaction avec une clé privée. Comme ECDSA sur Bitcoin, Schnorr utilise la courbe elliptique `secp256k1`, définie par l'équation $y^2 = x^3 + 7$. Les bitcoins bloqués avec Taproot peuvent être dépensés soit en satisfaisant l'un des scripts, soit en fournissant une signature valide correspondant à la clé publique, ce qui permet de garder les scripts privés. On y utilise un MAST pour permettre l'utilisation de plusieurs scripts. N'importe lequel peut-être utiliser pour dépenser les bitcoins associés. Cela permet des fonctionnalités plus complexes et des contrats intelligents plus sophistiqués.

> *Pour plus d'informations, voir la définition de [**SCHNORR (PROTOCOLE)**](./S.md#schnorr-(protocole)).*

## TAPROOT ASSETS PROTOCOL

Protocole développé par Lightning Labs permettant d'émettre des actifs sur la blockchain principale de Bitcoin, en tirant partie de la mise à jour Taproot. Taproot Assets permet la création d'actifs fongibles comme des stablecoins et non fongibles comme de NFT. Les Taproot Assets peuvent être transférés via des transactions Bitcoin classiques ou via le Lightning Network. Ce protocole utilise des Merkle-Sum Sparse Merkle Trees (MS-SMT), une sorte de combinaison des MST et des SMT, pour assurer la validité et l’audibilité des actifs.

> *Taproot Assets Protocol s'appelait « TARO » auparavant.*

## TAPSCRIPT

Mise à jour qui a pour objet de modifier certains opcodes du langage de script classique de Bitcoin, afin de définir le nouveau langage de script utilisé pour les dépenses Taproot. Tapscript a été introduit par le BIP342 au sein du soft fork SegWit.

Afin de mettre en œuvre les diverses modifications associées à Taproot, il s'est avéré nécessaire de revisiter le langage de script. C'est là l'objet de Tapscript qui désactive ou modifie certains opcodes, et vient en ajouter de nouveaux. 

> *Pour plus d'informations, voir la définition de [**SCHNORR (PROTOCOLE)**](./S.md#schnorr-(protocole)) et [**TAPROOT**](./T.md#taproot).*

## TARO

Ancien nom du protocole Taproot Assets Protocol. Pour plus d'informations, voir la définition de **TAPROOT ASSETS PROTOCOL**.

## TAUX DE HACHAGE

Voir la définition de **HASHRATE**.

## TCP (TRANSMISSION CONTROL PROTOCOL)

Protocole de communication fondamental dans les réseaux, conçu pour assurer une transmission de données fiable sur Internet. Il établit une connexion, garantit l'ordre des données envoyées, gère la retransmission en cas de perte de paquets, et contrôle la congestion.

## TÉMOIN DE TRANSACTION

Fait référence à une composante des transactions Bitcoin qui a été déplacée avec le soft fork SegWit afin de résoudre le problème de la malléabilité des transactions. Le témoin contient les signatures et les clés publiques nécessaires pour déverrouiller les bitcoins dépensés dans une transaction. Dans les transactions Legacy, le témoin représentait la somme des `ScriptSig` de tous les inputs. Dans les transactions SegWit, le témoin représente la somme des `ScriptWitness` de chaque input, et cette partie de la transaction est dorénavant déplacée dans un arbre de Merkle séparé au sein du bloc. Avant SegWit, les signatures pouvaient être légèrement modifiées sans être invalidées avant qu'une transaction ne soit confirmée, ce qui changeait l'identifiant de la transaction. Cela rendait difficile la construction de divers protocoles, car une transaction non confirmée pouvait voir son identifiant changer. En séparant les témoins, SegWit rend les transactions non malléables, car tout changement dans les signatures n'affecte plus l'identifiant de la transaction (TXID), mais uniquement l'identifiant du témoin (WTXID). En plus de résoudre le problème de la malléabilité, cette séparation permet d'augmenter la capacité de chaque bloc.

> *En anglais, « témoin » se traduit par « witness ». Pour plus d'informations, voir la définition de **SEGWIT**.*

## TESTNET

Version alternative de Bitcoin utilisée exclusivement à des fins de test et de développement. Il s'agit d'un réseau séparé du réseau principal (mainnet), avec ses propres blocs et transactions, permettant aux développeurs de tester de nouvelles fonctionnalités, applications et mises à jour sans risque pour le réseau principal. Le testnet permet également d'éviter de payer des frais de transaction lors de tests. Les bitcoins utilisés sur le testnet n'ont aucune valeur réelle.

## TIDES (TRANSPARENT INDEX OF DISTINCT EXTENDED SHARES)

Méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage introduite par la pool OCEAN en 2023. Cette méthode répartit les récompenses en fonction d'un pourcentage pondéré du travail consacré aux preuves les plus récemment trouvées. Chaque preuve est rémunérée plusieurs fois, avec un calcul de récompense incluant les frais de transaction. Ce système assure une grande précision dans les paiements des mineurs, sans nécessiter un intermédiaire de garde pour le traitement des paiements, contrairement à d'autres méthodes comme FPPS. TIDES est conçu pour des rémunérations transparentes et auditables.

## TIMELOCK

Primitive de contrat intelligent qui permet de définir une condition temporelle à remplir pour qu'une transaction puisse être ajoutée à un bloc. Il existe deux types de timelocks sur Bitcoin : 
- Le timelock absolu, qui spécifie un moment précis avant lequel la transaction ne peut être incluse dans un bloc ; 
- Le timelock relatif, qui définit un délai à partir de l'acceptation d'une transaction antérieure. 
Le timelock peut être défini soit sous la forme d'une date exprimée en temps Unix, soit sous la forme d'un numéro de bloc. Enfin, le timelock peut s'appliquer soit à un output de transaction grâce à l'utilisation d'un opcode spécifique dans le script de verrouillage (`OP_CHECKLOCKTIMEVERIFY` ou `OP_CHECKSEQUENCEVERIFY`), soit à une transaction entière grâce à l'utilisation de champs de transaction spécifiques (`nLockTime` ou `nSequence`).

> *Pour plus d'informations, voir la définition de [**OP_CHECKLOCKTIMEVERIFY**](./O.md#op_checklocktimeverify), [**OP_CHECKSEQUENCEVERIFY**](./O.md#op_checksequenceverify), [**NLOCKTIME**](./N.md#nlocktime) et [**NSEQUENCE**](./N.md#nsequence).*

## TOR (THE ONION ROUTER)



## TPRV

Préfixe de clé privée étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet.
> *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## TPUB

Préfixe de clé publique étendue pour les comptes Legacy et SegWit V1 sur Bitcoin Testnet. 
> *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## TRANSACTION (TX)

Dans le contexte de Bitcoin, une transaction (abrégée « TX ») est une opération enregistrée sur la blockchain qui transfère la propriété de bitcoins d'une ou plusieurs entrées (inputs) vers une ou plusieurs sorties (outputs). Chaque transaction consomme des UTXO en entrées, qui sont des outputs de transactions précédentes, et crée de nouveaux UTXO en sorties, qui peuvent être utilisés comme entrants dans des transactions futures. Chaque entrée comporte une référence à un output existant ainsi qu'un script de signature qui rempli les conditions de dépense établies par l'output auquel il fait référence. C'est ce qui permet de débloquer des bitcoins. Les outputs définissent de nouvelles conditions de dépense pour les bitcoins transférés, souvent sous la forme d'une clé publique ou d'une adresse à laquelle les bitcoins sont maintenant associés.

## TRANSACTION COINBASE

La transaction coinbase est une transaction spéciale et unique incluse dans chaque bloc de la blockchain Bitcoin. Elle représente la première transaction d'un bloc et est créée par le mineur qui a réussi à trouver un entête validant la preuve de travail (Proof-of-Work). La transaction coinbase sert principalement deux objectifs : attribuer la récompense de bloc au mineur et ajouter de nouvelles unités de bitcoins à la masse monétaire en circulation. La récompense de bloc, qui est l'incitation économique pour les mineurs à contribuer à s'adonner à la preuve de travail, comprend les frais accumulés pour les transactions incluses dans le bloc et un montant déterminé de bitcoins nouvellement créés ex-nihilo (subvention de bloc). Ce montant, initialement fixé à 50 bitcoins par bloc en 2009, est réduit de moitié tous les 210 000 blocs (environ tous les 4 ans) lors d'un événement appelé « halving ». La transaction coinbase diffère des transactions régulières de plusieurs manières. Tout d'abord, elle n'a pas d'entrée (input), ce qui signifie qu'aucune sortie de transaction existante (UTXO) n'y est dépensée. Ensuite, le script de signature `scriptSig` pour la transaction coinbase contient généralement un champ arbitraire permettant d'incorporer des données supplémentaires, telles que des messages personnalisés ou des informations de version de logiciel de minage. Enfin, les bitcoins générés par la transaction coinbase sont soumis à une période de maturité de 100 blocs (101 confirmations) avant de pouvoir être dépensés, afin de prévenir les dépenses potentielles de bitcoins non existants en cas de réorganisation de la chaîne.

## TRANSACTION D'ENGAGEMENT

Dans le contexte d'un canal bidirectionnel au sein de Lightning, la transaction d'engagement est une transaction que les deux parties créent et signent, sans toutefois la publier sur la chaîne principale. Elle représente l'état actuel de la répartition des fonds entre les parties d'un canal, chaque paiement Lightning résultant en une nouvelle transaction d'engagement. Ces transactions sont valides, mais ne sont diffusées que lorsque le canal est clôturé unilatéralement. Elles contiennent des sorties pour chaque partie, reflétant la répartition des fonds selon les paiements Lightning effectués depuis l'ouverture du canal. Des mécanismes de pénalité sont associés pour dissuader les parties de diffuser des états obsolètes du canal, c'est-à-dire des vielles transactions d'engagement.

## TWO-WAY PEG (2WP)

Voir la définition d'**ANCRAGE BILATÉRAL**.

## TXID (TRANSACTION IDENTIFIER)-

Identifiant unique associé à chaque transaction Bitcoin. Il est généré en calculant le hachage `SHA256d` des données de la transaction. Le TXID sert de référence pour retrouver une transaction spécifique au sein de la blockchain. Il est également utilisé pour pour faire référence à un UTXO, qui est essentiellement la concaténation du TXID d'une transaction précédente et de l'index de l'output désigné (également appelé « vout »). Pour les transaction post-SegWit, le TXID ne prend plus en compte le témoin de la transaction, ce qui permet de supprimer la malléabilité.

> *Pour plus d'informations, voir la définition de [**WTXID**](./W.md#wtxid).*
