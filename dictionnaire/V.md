## VANITY (ADDRESS)

Adresse de réception personnalisée qui contient une séquence spécifique de caractères choisie par l'utilisateur, généralement pour des raisons esthétiques. Ces adresses sont générées en exécutant un processus de calcul, où de multiples clés privées sont créées jusqu'à ce que l'une d'entre elles corresponde à une adresse de réception contenant la séquence désirée. Ce processus ne compromet pas la sécurité de l'adresse, mais peut nécessiter un temps et des ressources de calcul considérables, surtout pour des séquences plus longues ou plus spécifiques. C'est une sorte de processus de brute force.

> ► *En français, on parle d'une « adresse personnalisée ».*

## VANITYGEN

Premier logiciel open source en ligne de commande utilisé pour créer des adresses de réception personnalisées (*vanity address*). Il fonctionne en générant et en testant par tâtonnement des paires de clés jusqu'à ce qu'une adresse de réception correspondant aux critères spécifiés par l'utilisateur (comme une certaine séquence de caractères spécifiques) soit trouvée. Vanitygen nécessite un processus de calcul intensif, particulièrement pour des séquences longues.

## VERSIONNAGE

Dans le contexte de Bitcoin, désigne le processus d'assignation de versions spécifiques à divers éléments du protocole, afin de faciliter leur suivi, leur gestion et leur mise à jour. Les versions sont numérotées de manière séquentielle, permettant d'identifier les modifications apportées, les nouvelles fonctionnalités ou les corrections de bugs. Par exemple, chaque bloc de la blockchain contient un numéro de version, indiquant les règles du consensus et les structures de données appliquées lors de sa création. On retrouve des versionnages pour les types de scripts, pour les transactions, pour les blocs, pour le logiciel Bitcoin Core, pour les communications réseaux...

## VIN

Élément spécifique d'une transaction Bitcoin qui spécifie la source des fonds utilisés pour satisfaire les outputs. Chaque `vin` fait référence à un output non dépensé (UTXO) d'une transaction précédente. Une transaction peut contenir plusieurs inputs, chacun étant identifié par une combinaison du `txid` (l'identifiant de la transaction d'origine) et du `vout` (l'index de l'output dans cette transaction).

Chaque `vin` inclut les informations suivantes :
* `txid` : l'identifiant de la transaction précédente contenant l'output utilisé ici en input ;
* `vout` : l'index de l'output dans la transaction précédente ;
* `scriptSig` ou `scriptWitness` : un script de déverrouillage qui fournit les données nécessaires pour satisfaire les conditions posées par le `scriptPubKey` de la transaction précédente dont les fonds sont dépensés, généralement en fournissant une signature cryptographique ;
* `nSequence` : un champ spécifique utilisé pour indiquer la manière dont cet input est verrouillé dans le temps, ainsi que d'autres options comme RBF.

> ► *Pour plus d'informations, voir la définition de [**NSEQUENCE**](./N.md#nsequence).*

## VOUT

Élément spécifique d'une transaction Bitcoin qui détermine la destination des fonds envoyés. Une transaction peut inclure plusieurs outputs, chacun étant distinctement identifié par la combinaison de l'identifiant de la transaction (`txid`) et d'un index appelé `vout`. Cet index, qui commence à `0`, marque la position de l'output dans la séquence des outputs de la transaction. Ainsi, le premier output sera désigné par `"vout": 0`, le second par `"vout": 1`, et ainsi de suite.

Chaque `vout` encapsule principalement deux informations :
* la valeur, exprimée en bitcoins, qui représente le montant envoyé ;
* un script de verrouillage (`scriptPubKey`) qui stipule les conditions requises pour que les fonds puissent être dépensés à nouveau dans une prochaine transaction.

La combinaison du `txid` et du `vout` d'une pièce spécifique forme ce que l'on appelle un UTXO, par exemple :

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```

## VPRV

Préfixe de clé privée étendue pour les comptes SegWit V0 sur Bitcoin Testnet. 

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## VPUB

Préfixe de clé publique étendue pour les comptes SegWit V0 sur Bitcoin Testnet. 

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*
