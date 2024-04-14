## L402



## LABEL

Étiquette ou annotation attribuée à un UTXO afin de se souvenir de sa provenance. 

> *Pour plus d'informations, voir la définition de [**ÉTIQUETAGE**](./E.md#étiquetage).*

## LCB/FT

La lutte contre le blanchiment des capitaux et le financement du terrorisme (LCB/FT) fait référence aux mesures réglementaires adoptées pour prévenir l'utilisation de Bitcoin dans des activités illégales. Ces mesures incluent l'identification et la vérification de l'identité des clients (KYC), la surveillance des transactions pour détecter des schémas « suspects », et la collaboration avec les autorités pour signaler des activités considérées comme illégales. Les plateformes d'échange régulées sont tenues de s'y conformer pour opérer dans de nombreuses juridictions, notamment en France.

## LDB (.LDB)



## LDK (LIGHTNING DEV KIT)

Kit de développement (SDK) pour Lightning. LDK est une collection de bibliothèques et d'outils destinés aux développeurs pour intégrer facilement Lightning à leurs logiciels ou pour créer des applications Lightning en réduisant la complexité. LDK gère les aspects complexes de l'intégration de fonctionnalités liées à Lightning. Ce projet a été lancé par Spiral, une entreprise créée par Jack Dorsey, et s'est basée sur Rust-Lightning (RL).

## LEVELDB

Bibliothèque de stockage de clés-valeurs légère, rapide et open-source, conçue par Google. On l'utilise sur Bitcoin pour stocker l'UTXO set, l'index des transactions et l'index des blocs. Ce système de base de données a été introduit en 2012 dans le cadre de la Pull Request « *Ultraprune* » visant à remplacer BerkeleyDB. Ce changement a eu des répercussions significatives, notamment la création d'une première division de la blockchain avec une réorganisation majeure de 24 blocs le 12 mars 2013. Cet incident a été détaillé dans le BIP50. Plus tard, ce changement de système a même conduit à un hard fork non intentionnel le 15 mai 2013.

## LIBBITCOIN


## LIBSECP256K1



## LIGHTNING LABS

Entreprise spécialisée dans le développement sur le Lightning Network. Fondée en 2016, elle est à l'origine de Lightning Network Daemon (LND), une des implémentations majeures du protocole. Lightning Labs est également à l'origine des services Pool, Loop et Faraday. Plus récemment, ils ont annoncé travailler sur le protocole Taproot Assets (anciennement TARO).

## LIGHTNING NETWORK

Protocole de couche supérieure, construit au-dessus du protocole Bitcoin, visant à permettre des transactions rapides et à faible coût. Il permet la création de canaux de paiement entre les participants, au sein desquels les transactions peuvent être effectuées presque instantanément et avec des frais minimes, sans avoir à enregistrer chaque transaction individuellement sur la blockchain. Les canaux peuvent rester ouverts quasi indéfiniment, et ne nécessitent des transactions sur la blockchain que lors de leur ouverture et de leur clôture. Le Lightning Network vise à améliorer la scalabilité de Bitcoin et à rendre possible son utilisation pour des paiements de faible valeur. Toutefois, le Lightning Network n’est pas une solution parfaite. Ce protocole a une tendance naturelle à la centralisation sur de gros nœuds institutionnels. Il peut également être difficile de l’utiliser durant les périodes de très fortes congestions, comme on a pu le voir durant l’épisode BRC-20 en mai 2023. Aussi, sa structure rend très complexe la confidentialité des paiements.

## LIGHTNING NETWORK DAEMON (LND)

Implémentation majeure du protocole Lightning Network écrite en langage Go. Développée par Lightning Labs, LND permet la création et la gestion de canaux de paiement et de nœuds sur le réseau Lightning.

## LIGHTNING SERVICE PROVIDER (LSP)


## LIMITE D'ÉMISSION

21 millions

## LIQUIDITÉS (LIGHTNING)


## LIQUIDITY ADVERTISEMENTS


## LIQUID NETWORK

Sidechain de Bitcoin conçue par Blockstream pour fournir des transactions rapides et confidentielles. Contrairement à la blockchain principale de Bitcoin, Liquid utilise un mécanisme de consensus basé sur une fédération (un groupe sélectionné d'opérateurs de nœuds, généralement des entreprises liées à Bitcoin), remplaçant ainsi le mécanisme de consensus de Nakamoto. Cette approche accélère considérablement les transactions et réduit les coûts, tout en offrant des fonctionnalités plus avancées. Liquid permet aussi l'émission d'actifs numériques, y compris des jetons représentant d'autres cryptomonnaies. Les bitcoins sur Liquid, appelés L-BTC, sont liés au BTC grâce à un système d'ancrage bilatéral reposant sur une partie de la fédération. Les participants à cette fédération sont appelés des « fonctionnaires », et il peuvent endosser à la fois le rôle de « gardien » (watchmen) et de « signataire de bloc » (blocksigner).

## LITTLE-ENDIAN

Format de stockage de données dans les systèmes informatiques où les octets les moins significatifs (les « petits bouts ») sont placés en premier dans l'ordre des adresses. Dans une séquence comportant plusieurs octets, l'octet ayant le plus petit poids (par exemple, les chiffres les plus à droite en hexadécimale) est stocké en premier.

## LOCK (.LOCK)

Fichier utilisé dans Bitcoin Core pour le verrouillage du répertoire de données. Il est créé lorsque bitcoind ou Bitcoin-qt démarre pour éviter que plusieurs instances du logiciel accèdent simultanément au même répertoire de données. Le but est de prévenir les conflits et les corruptions de données. Si le logiciel s'arrête de manière inattendue, le fichier .lock peut éventuellement rester et doit être supprimé manuellement avant de redémarrer Bitcoin Core.

## LOCKTIME



## LOGARITHME DISCRET (PROBLÈME)

Le logarithme discret est un problème mathématique qui est utilisé dans certains algorithmes cryptographiques à clé publique. Dans un groupe cyclique d’ordre $q$, avec un générateur $g$, si l'on a une équation de la forme $g^x = h$, alors $x$ est appelé le logarithme discret de $h$ par rapport à la base $g$, modulo $q$. En termes simples, il s’agit de déterminer l’exposant $x$ lorsqu’on connaît $g$, $h$, et $q$. Le logarithme discret est donc la réciproque de l'exponentielle dans un groupe cyclique fini. Cependant, pour de grandes valeurs de $q$, résoudre le problème du logarithme discret est considéré comme algorithmiquement difficile. Cette propriété est exploitée pour assurer la sécurité de nombreux protocoles cryptographiques, tels que le protocole de Diffie-Hellman pour l'échange de clés. Le logarithme discret est aussi utilisé dans la cryptographie à courbes elliptiques (ECC), entre autres dans l'algorithme ECDSA (Elliptic Curve Digital Signature Algorithm). Dans le contexte des courbes elliptiques, le problème du logarithme discret s'étend à la recherche d'un scalaire $k$ tel que $k \cdot G = K$, où $G$ et $K$ sont des points sur la courbe, et $\cdot$ représente l'opération de multiplication de points. Dans le contexte de Bitcoin, les transactions standards utilisent soit ECDSA, soit le protocole de Schnorr, afin de bloquer des UTXO. Ils reposent tous deux sur l’impossibilité de calculer le logarithme discret.

## LOOP

Service développé par Lightning Labs conçu pour faciliter l'équilibrage de liquidités dans les canaux Lightning. Loop permet aux utilisateurs de transférer des fonds entre Bitcoin et le Lightning Network, sans avoir à fermer ou ouvrir un canal. Loop aide ainsi à optimiser sa liquidité et à réduire les frais de gestion de ses canaux.
