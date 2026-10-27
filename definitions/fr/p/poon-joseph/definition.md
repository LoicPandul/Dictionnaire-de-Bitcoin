Développeur, coauteur avec Thaddeus Dryja du livre blanc du Lightning Network et premier à proposer pour Segregated Witness le drapeau de signature `SIGHASH_NOINPUT`, déjà nommé dans le livre blanc et ancêtre de `SIGHASH_ANYPREVOUT`.

Le brouillon 0.5 de « The Bitcoin Lightning Network », signé Poon et Dryja, est en ligne dès le 28 février 2015, et la version 0.5.9.2, intitulée « The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments », est datée du 14 janvier 2016. Le texte décrit un réseau de canaux de paiement : Alice peut payer Dave par l'intermédiaire de Bob et de Carol sans leur faire confiance, grâce à des contrats à verrous temporels dégressifs, que chacun peut faire appliquer sur la chaîne si un participant refuse de coopérer. Il suppose un nouveau type de *sighash* qui corrige la malléabilité des transactions.

Le 26 février 2016, Poon écrit sur bitcoin-dev, sous le titre « SIGHASH_NOINPUT in Segregated Witness », qu'un drapeau de signature qui ne couvre pas l'identifiant ni l'index de l'entrée serait utile à Lightning. Il permettrait de confier à un tiers chargé de surveiller un canal une seule transaction qui vaut pour tous les états antérieurs, au lieu de lui remettre toutes les signatures une à une.

BIP-0118 reprend ce drapeau, renommé `SIGHASH_ANYPREVOUT`, et cite Poon dans ses remerciements. Le protocole eltoo en dépend.
