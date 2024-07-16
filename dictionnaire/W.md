## WABISABI

Protocole de coinjoins chaumiens avec un coordinateur central utilisé sur le portefeuille Wasabi 2.0. Ce modèle a été conçu Ádám Ficsór (nopara73), Yuval Kogman, Lucas Ontivero et István András Seres en 2021, et a été intégré dans le logiciel Wasabi 2.0 l'année suivante.

> ► *Pour plus d'informations, voir la définition de **[CHAUMIAN COINJOIN](./C.md#chaumian-coinjoin)**.*

## WALLET

Outil logiciel spécialement conçu pour sécuriser et gérer les clés privées d'un utilisateur. Si le portefeuille est stocké et géré sur un dispositif logiciel lui-même installé sur une machine polyvalente, on parle alors de « portefeuille chaud ». En revanche, s'il est stocké dans un logiciel, lui-même installé sur un dispositif matériel dédié uniquement à cette tâche et non connecté à internet, on parle alors de « portefeuille froid ». Le portefeuille permet notamment d'utiliser les clés privées pour signer des transactions, et ainsi remplir les conditions permettant la dépense des bitcoins.

> ► *En français, on peut traduire « wallet » par « portefeuille ».*

## WALLET.DAT

Fichier dans Bitcoin Core qui stocke des informations sur le portefeuille de l'utilisateur, telles que les clés privées et les transactions effectuées. Le fichier `wallet.dat` est chiffré pour assurer la sécurité des fonds. Depuis la version 0.16.0, ce fichier a été déplacé dans le dossier `/wallets`.

## WALLETS/DB.LOG

Fichier journal dans Bitcoin Core spécifique à la base de données des portefeuilles. Il enregistre les opérations et les événements liés à la base de données des portefeuilles pour la résolution de problèmes.

## WALLET IMPORT FORMAT (WIF)

Méthode pour encoder une clé privée Bitcoin de manière à ce qu'elle puisse être importée ou exportée plus facilement entre différents portefeuilles. Le WIF est établi sur un encodage `Base58Check`, qui inclut des informations sur la version, la compression de la clé publique correspondante et une somme de contrôle pour la détection d'erreurs de saisie. Une clé privée WIF commence par les caractères `5` pour les clés non compressées, ou `K` et `L` pour les clés compressées, et contient tous les caractères nécessaires pour reconstituer la clé privée originale. Le format WIF fournit un moyen standardisé pour transférer une clé privée entre différents logiciels de portefeuille.

## WASABI WALLET

Portefeuille Bitcoin axé sur la confidentialité offrant des fonctionnalités telles que le coinjoin.

![](assets/48.png)

## WATCHMEN

Dans le cadre de Liquid (une sidechain de Bitcoin), ce sont des entités chargées de maintenir l'ancrage du L-BTC, le jeton natif de Liquid, en gérant et sécurisant les BTC utilisés en sous-jacent. Ils s'assurent que les actifs transférés entre la blockchain Bitcoin principale et la sidechain Liquid sont correctement verrouillés et déverrouillés. L'objectif de leurs actions est de maintenir la même valeur entre le L-BTC circulant sur Liquid et le BTC circulant sur Bitcoin. Dans Liquid, les watchmen font partie des fonctionnaires avec les blocksigners.

> ► *En français, on peut traduire « watchmen » par « gardiens ».*

## WATCH-ONLY WALLET

Un watch-only wallet (ou portefeuille en lecture seule) est un type de logiciel qui permet à un utilisateur de voir les transactions associées à une clé ou un ensemble de clés Bitcoin spécifiques, sans posséder les clés privées correspondantes. Il offre une visibilité sur le solde et l'historique des transactions, sans pour autant permettre de dépenser les fonds du portefeuille. Par exemple, l'application Sentinel est un watch-only wallet.

## WHALE

Désigne un individu ou une entité qui possède une quantité très importante de bitcoins.

## WHIRLPOOL

Protocole de coinjoins chaumiens ZeroLink, développée par les équipes du portefeuille Samourai Wallet. Whirlpool est actuellement disponible sur les portefeuilles Samourai Wallet (Android), Sparrow Wallet (PC) et Bitcoin Keeper (IOS et Android).

![](assets/44.png)

> ► *Pour plus d'informations, voir la définition de **[CHAUMIAN COINJOIN](./C.md#chaumian-coinjoin)** et de [**ZEROLINK**](./Z.md#zerolink).*

## WHIRLPOOL STAT TOOL

Logiciel en ligne de commandes développé par Samourai Wallet qui permet de fournir les anonsets prospectifs et rétrospectifs d'une pièce mixée au sein de Whirlpool, ainsi que son taux de diffusion dans la pool. WST utilise l'algorithme HyperLogLogPlusPlus qui permet d'estimer le nombre de valeurs distinctes dans un très grand ensemble de données.

## WHITE PAPER

Nom donné au document scientifique nommé « *Bitcoin: A Peer-to-Peer Electronic Cash System* » publié par Satoshi Nakamoto pour la première fois le 31 octobre 2008. Ce document décrit les principes fondamentaux de Bitcoin. Le White Paper que l'on présente de nos jours est une seconde version publiée le 24 mars 2009.

> ► *Pour télécharger le White Paper de Bitcoin : https://bitcoin.org/bitcoin.pdf.*

## WITNESSSCRIPT

Script qui spécifie les conditions sous lesquelles les bitcoins peuvent être dépensés dans les UTXOs P2WSH ou P2SH-P2WSH. Typiquement, les `witnessScript` déterminent les conditions d'un portefeuille multisignatures sous standard SegWit. Dans ces standards de script, le `scriptPubKey` de l'UTXO (la sortie) contient un hachage du `witnessScript`. Pour utiliser cet UTXO comme entrée dans une nouvelle transaction, le détenteur doit révéler le `witnessScript` original, afin de prouver sa correspondance avec l'empreinte dans le `scriptPubKey`. Le `witnessScript` doit alors être inclus dans le `scriptWitness` de la transaction, qui contient également les éléments nécessaires pour valider le script, comme par exemple les signatures.  Le `witnessScript` est donc l'équivalent pour SegWit du `redeemScript` dans une transaction P2SH, à la différence près qu'il est placé dans le témoin de la transaction, et non dans le `scriptSig`.

> ► *Attention, le `witnessScript` ne doit pas être confondu avec le `scriptWitness`. Tandis que le `witnessScript` définit les conditions de dépense d'un UTXO P2WSH ou P2SH-P2WSH et constitue un script à part entière, le `scriptWitness` contient les données de témoin de tout input SegWit.*

## WTXID

Extension du TXID traditionnel, incluant les données de témoin (*witness*) introduites avec SegWit. Alors que le TXID est un hachage des données de transaction hors témoin, le WTXID est le `SHA256d` de l'intégralité des données de la transaction, témoin inclus. Les WTXID sont stockés dans un second arbre de Merkle dont la racine est mise dans la transaction coinbase. Cette séparation permet de supprimer la malléabilité du TXID de la transaction.

> ► *Pour plus d'informations, voir la définition de [**TXID**](./T.md#txid-transaction-identifier) et [**SEGWIT**](./S.md#segwit).*
