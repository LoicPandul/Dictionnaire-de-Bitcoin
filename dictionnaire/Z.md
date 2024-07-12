## ZEROCONF

Pratique risquée consistant à considérer une transaction Bitcoin comme définitive, et à procéder à l'exécution de l'acte associé en contrepartie (tel que la vente d'un bien ou d'un service), avant que la transaction ne soit réellement incluse dans un bloc sur la blockchain. Les transactions non confirmées, ou en zeroconf, sont vulnérables à des attaques de double dépense, car elles ne sont pas encore irrévocablement inscrites dans le registre. Le zeroconf peut éventuellement être envisagé dans des contextes très spécifiques, où la rapidité est prioritaire, comme dans le cas de petites transactions commerciales ou dans le cas d'une transaction entre proches. Dans ces situations, le risque de double dépense est souvent considéré comme acceptable en comparaison de l'avantage d'une transaction rapide. Néanmoins, pour des transactions importantes, en particulier lorsqu'on ne connaît pas l'expéditeur, il est crucial d'attendre plusieurs confirmations avant de considérer la transaction comme immuable. La norme généralement acceptée est d'attendre 6 confirmations, ce qui signifie que 5 blocs supplémentaires doivent être minés après celui incluant la transaction, pour la considérer comme définitive.

## ZEROLINK

Protocole de Chaumian coinjoin qui vise à briser toutes les liaisons entre des ensembles de pièces séparées à travers des techniques avancées de mixage. Le protocole ZeroLink se distingue par sa capacité à protéger l’anonymat des utilisateurs contre diverses formes d'analyse de chaîne au niveau de la transaction et du réseau. ZeroLink introduit un cadre pour les portefeuilles de coinjoin, avec l'utilisation de comptes pré-mix et post-mix ségrégués, ainsi qu’une technique de mixage propre : le Chaumian coinjoin. À ce jour, la seule implémentation de coinjoins ZeroLink est Whirlpool, disponible sur Samourai Wallet et Sparrow Wallet. Ce protocole [a été introduit par nopara73 et TDevD en 2017](https://github.com/nopara73/ZeroLink/blob/master/README.md).

> ► *Pour plus d'informations, voir la définition de **[CHAUMIAN COINJOIN](./C.md#chaumian-coinjoin)**.*

## ZEROSYNC

Projet développé pour tirer partie des ZKP (preuves à divulgation nulle de connaissance) dans l'écosystème Bitcoin, afin d'améliorer le passage à l'échelle et la confidentialité du système. Leur protocole principal (également nommé *ZeroSync*) permet de compresser l'historique de la blockchain Bitcoin, afin d'accélérer la synchronisation initiale des nœuds avec le réseau via l'utilisation d'une preuve compacte, sans pour autant compromettre la vérification.

## ZKP (ZERO-KNOWLEDGE PROOF)

Méthode cryptographique permettant à une partie (le prouveur) de prouver à une autre partie (le vérificateur) qu'une information est vraie, sans révéler l'information ni aucun aspect de celle-ci. Une ZKP permet de garantir l'exactitude d'une affirmation, tout en préservant la confidentialité des données sous-jacente.

> ► *En français, on traduit Zero-Knowledge Proof par « Preuve à divulgation nulle de connaissance ».*

## ZPRV

Préfixe de clé privée étendue pour les comptes SegWit V0 sur Bitcoin.

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*

## ZPUB

Préfixe de clé publique étendue pour les comptes SegWit V0 sur Bitcoin.

> ► *Pour plus d'informations, voir la définition de [**CLÉ ÉTENDUE**](./C.md#clé-étendue).*
