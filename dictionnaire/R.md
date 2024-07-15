## RACINE DE MERKLE

Condensat ou « top hash » d'un arbre de Merkle, qui représente un résumé de toutes les informations présentes dans l'arbre. Un arbre de Merkle est une structure d'accumulateur cryptographique, parfois également nommée « arbre de hachage ». Dans le cadre de Bitcoin, des arbres de Merkle sont utilisés pour organiser les transactions dans un bloc et pour faciliter la vérification rapide de l'inclusion d'une transaction spécifique. Ainsi, dans les blocs Bitcoin, la racine de Merkle est obtenue en hachant de manière successive les transactions par paires jusqu'à ce qu'il ne reste qu'un seul hachage (la racine de Merkle). Cette dernière est ensuite incluse dans l'entête du bloc correspondant. On retrouve également cet arbre de hachage dans UTREEXO, une structure permettant de condenser l'UTXO set des nœuds, et dans le MAST Taproot.

> ► *Pour plus d'informations, voir la définition d'**[ARBRE DE MERKLE](./A.md#arbre-de-merkle)***

## RAW TRANSACTION

Transaction Bitcoin construite et signée, qui se trouve dans sa forme binaire. Une transaction brute (*raw TX*) est la représentation finale d'une transaction, juste avant qu'elle ne soit diffusée sur le réseau. Cette transaction contient toutes les informations nécessaires à son inclusion dans un bloc :
* La version ;
* Le flag ;
* Les inputs ;
* Les outputs ;
* Le locktime ;
* Le witness.

Ce que l'on appelle « *raw transaction* » représente les données brutes qui sont passées deux fois dans la fonction de hachage SHA256 pour générer le TXID de la transaction. Ces données sont ensuite utilisées dans l'arbre de Merkle du bloc pour intégrer la transaction dans la blockchain.

> ► *Ce concept est également parfois nommé « Serialized Transaction ». En français, on pourrait traduire ces termes respectivement par « transaction brute » et « transaction sérialisée ».*

## RBF (REPLACE-BY-FEE)

Mécanisme transactionnel permettant à l'expéditeur de remplacer une transaction par une autre avec des frais plus élevés, afin d'accélérer la confirmation de celle-ci. Si une transaction avec des frais trop faibles reste bloquée, l'expéditeur peut utiliser *Replace-By-Fee* (remplacement par les frais) pour augmenter les frais et prioriser sa transaction de remplacement dans les mempools. 

RBF est applicable tant que la transaction est dans les mempools ; une fois dans un bloc, elle ne peut plus être remplacée. Lors de l'envoi initial, la transaction doit spécifier sa disponibilité à être remplacée en ajustant la valeur de `nSequence` à une valeur inférieure à `0xfffffffe`. C'est ce que l'on appelle un « flag » RBF. Ce paramètre signale la possibilité de mise à jour de la transaction après sa diffusion, ce qui permet par la suite de faire un RBF. Cependant, il est parfois possible de remplacer une transaction n'ayant pas signalé RBF. Les nœuds utilisant le paramètre de configuration `mempoolfullrbf=1` acceptent ce remplacement même si RBF n'a pas été signalé initialement.

À la différence de CPFP (*Child Pays For Parent*), où c'est le destinataire qui peut agir pour accélérer la transaction, RBF (*Replace-By-Fee*) permet à l'envoyeur de prendre l'initiative d'accélérer sa propre transaction en augmentant les frais.

## RÉCOMPENSE DE BLOC

Total des bitcoins récupérés par un mineur lorsqu'il trouve un bloc valide sur Bitcoin. Cette récompense est composée de deux éléments : la subvention de bloc et les frais de transaction. La subvention de bloc est une quantité fixe de bitcoins que le mineur peut créer ex nihilo. Cette quantité diminue progressivement au fil des halvings. Les frais de transaction sont les frais cumulés payés par les utilisateurs pour effectuer les transactions incluses dans le bloc miné. Les frais sont également des bitcoins créés par le mineur, mais leur quantité est limitée au montant des bitcoins détruits dans les transactions. En effet, les frais d'une transaction représentent la différence entre le total des inputs et le total des outputs.

La récompense de bloc est distribuée au sein d'une transaction spécifique que l'on appelle « coinbase ». Les bitcoins qui en sont extraits sont automatiquement bloqués durant une période de 100 blocs. C'est ce que l'on appelle la période de maturité.

> ► *La traduction anglaise est « Block Reward ».*

## RÉCURSIF (COVENANT)

Un covenant récursif sur Bitcoin est un type de contrat intelligent qui impose des conditions non seulement sur la transaction actuelle, mais aussi sur les transactions futures qui dépensent les sorties de cette transaction. Cela permet de créer des chaînes de transactions où chacune doit respecter certaines règles définies par la première de la chaîne. La récursivité crée une séquence de transactions où chacune hérite des restrictions de sa transaction parent. Cela permettrait d'établir un contrôle complexe et à long terme sur la manière dont les bitcoins peuvent être dépensés, mais cela introduirait également des risques au niveau de la liberté de dépense et de la fongibilité.

Pour résumer, un covenant non récursif se limitera uniquement à la transaction qui succède immédiatement à celle qui a établi les règles. Et au contraire, un covenant récursif aura la capacité d'imposer des conditions spécifiques à un bitcoin de manière indéfinie. Les transactions pourront se succéder, mais le bitcoin en question conservera toujours les conditions initiales qui lui sont attachées. Techniquement, l'instauration d'un covenant non récursif intervient lorsque le `scriptPubKey` d'un UTXO définit des restrictions sur le `scriptPubKey` des sorties d'une transaction qui dépense ledit UTXO. En revanche, l'instauration d'un covenant récursif intervient lorsque le `scriptPubKey` d'un UTXO définit des restrictions sur le `scriptPubKey` des sorties d'une transaction qui dépense ledit UTXO, et de tous les `scriptPubKey` qui suivront la dépense de cet UTXO.

De manière plus générale, en informatique, ce que l’on appelle la « récursivité » est la capacité d’une fonction à s'appeler elle-même, ce qui crée une sorte de mise en abyme.

> ► *Pour plus d'informations, voir la définition de [**COVENANT**](./C.md#covenant).*

## REDEEMSCRIPT

Script qui défini les conditions spécifiques que doivent remplir les inputs pour débloquer les fonds associés à un output P2SH. Dans un UTXO P2SH, le `scriptPubKey` contient le hachage du `redeemScript`. Lorsqu'une transaction souhaite dépenser cet UTXO en entrée, elle doit fournir le `redeemScript` en clair qui correspond au hachage contenu dans le `scriptPubKey`. Le `redeemScript` est donc donné dans le `scriptSig` de l'input, en plus des autres éléments nécessaires pour satisfaire les conditions du script, comme les signatures ou les clés publiques. Cette structure encapsulée garantit que les détails des conditions de dépense restent cachés jusqu'à ce que les bitcoins soient effectivement dépensés. On l'utilise notamment pour les portefeuilles multisignatures Legacy P2SH.

## RÈGLES DE CONSENSUS

Règles fondamentales dans Bitcoin, assurant l'intégrité du réseau en dictant les critères de validation des transactions et des blocs. Une transaction qui ne suit pas les règles de consensus ne peut pas être minée dans un bloc valide. Par exemple, une transaction qui comporterait une signature invalide pour une de ses entrées ne pourrait pas être incluse dans un bloc. On différencie alors les règles de consensus et les règle de standardisation.

## RÈGLES DE STANDARDISATION

Règles adoptées individuellement par chaque nœud Bitcoin, en plus des règles de consensus, pour définir la structure des transactions non confirmées qu'il accepte dans sa mempool et diffuse à ses pairs. Ces règles sont donc configurées et exécutées en local par chaque nœud et peuvent varier d'un nœud à l'autre. Elles s'appliquent exclusivement sur les transactions non confirmées. Ainsi, un nœud n'acceptera une transaction qu'il jugerait non standard que si celle-ci est déjà incluse dans un bloc valide.

Notons que la majorité des nœuds laissent les configurations par défaut telles que préétablies dans Bitcoin Core, engendrant de fait une homogénéité des règles de standardisation à travers le réseau. Une transaction qui, bien que conforme aux règles de consensus, ne respecte pas ces règles de standardisation, aura des difficultés à être diffusée sur le réseau. Elle pourra toutefois être incluse dans un bloc valide si jamais elle atteint un mineur. Dans la pratique, ces transactions, qualifiées de « non standard », sont souvent transmises directement à un mineur par des voies externes au réseau pair-à-pair de Bitcoin. C'est souvent le seul moyen pour confirmer ce type de transaction.

Par exemple, une transaction qui n'alloue aucuns frais est à la fois valide selon les règles de consensus et non standard, car la politique par défaut de Bitcoin Core pour le paramètre `minRelayTxFee` est de `0.00001` (en BTC/kB).

> ► *On parle également parfois de « règles de mempool » pour désigner les règles de standardisation.*

## REGTEST

Environnement de test privé pour Bitcoin permettant aux développeurs de créer un réseau Bitcoin local avec des règles personnalisées. Contrairement au testnet, un regtest est privé, c'est-à-dire qu'il n'est pas possible de s'y connecter librement. Aussi, il offre un contrôle total sur les paramètres du réseau. Il permet notamment le minage rapide de blocs et le test de scénarios spécifiques. Il est utilisé pour le développement, le débogage et l'expérimentation avant la mise en œuvre sur le testnet ou le mainnet. Les bitcoins en circulation sur un regtest n'ont aucune valeur.

> ► *Regtest est la contraction de « Regression » et « Test ». En français, on pourrais le traduire par « Test de régression ».*

## RÉORGANISATION

Se réfère à un phénomène dans lequel la blockchain subit une modification de sa structure à cause de l'existence de blocs concurrents à une même hauteur. Cela survient lorsqu'une portion de la chaîne de blocs est remplacée par une autre chaîne ayant une quantité de travail accumulé plus importante.

Ces réorganisations font partie du fonctionnement naturel de Bitcoin, où différents mineurs peuvent trouver de nouveaux blocs presque simultanément, venant ainsi couper le réseau Bitcoin en deux. Dans de tels cas, le réseau peut se diviser temporairement en chaînes concurrentes. Finalement, lorsque l'une de ces chaînes accumule plus de travail, les autres chaînes sont abandonnées par les nœuds, et leurs blocs deviennent ce que l'on appelle des « blocs obsolètes » ou « blocs orphelins ». Ce processus de remplacement d'une chaîne par une autre est la réorganisation.

![](assets/9.png)

Les réorganisations peuvent avoir diverses conséquences. Tout d'abord, si un utilisateur avait une transaction confirmée dans un bloc qui s'avère être abandonné, mais que celle-ci ne se retrouve pas dans la chaîne finalement valide, alors sa transaction redevient non confirmée. C'est pour cette raison que l'on vous conseille de toujours attendre au moins 6 confirmations pour considérer une transaction comme réellement immuable. Passé 6 blocs de profondeur, les réorganisations sont tellement improbables que la chance qu'il y en ait une peut être considérée comme nulle.

Ensuite, au niveau du système global, les réorganisations impliquent un gaspillage de la puissance de calcul des mineurs. En effet, lorsqu'une division intervient, une partie des mineurs seront sur la chaîne `A`, et une autre partie sur la chaîne `B`. Si la chaîne `B` est finalement abandonnée lors d'une réorganisation, alors toute la puissance de calcul déployée par les mineurs sur cette chaîne est par définition gaspillée. S'il y a trop de réorganisations sur le réseau Bitcoin, la sécurité globale de celui-ci est donc réduite. C'est notamment pour cette raison, en partie, que l'augmentation de la taille des blocs ou la réduction de l'intervalle entre chaque bloc (10 minutes) peuvent être dangereuses.

> ► *Certains bitcoiners préfèrent parler de « bloc orphelin » pour désigner un bloc périmé. Aussi, dans le langage courant, on parle d'une « réorg » pour désigner une « réorganisation ». Le terme de « réorganisation » est un anglicisme. Pour être plus juste, on pourrait parler d'une « resynchronisation ».*

## RÉSEAU BITCOIN

Désigne l'infrastructure globale du système Bitcoin. Le réseau est constitué de l'ensemble des nœuds (ordinateurs) qui exécutent un logiciel implémentant le protocole Bitcoin, et qui se connectent à leurs pairs. Chaque nœud communique en pair-à-pair avec les autres nœuds, afin de télécharger et de vérifier la blockchain, de vérifier et de diffuser les nouveaux blocs, et de vérifier et de diffuser les nouvelles transactions.

## RÉSERVES FRACTIONNAIRES

Principe de la finance traditionnelle selon lequel les banques ne gardent qu'une fraction des dépôts de leurs clients en tant que réserve disponible, et utilisent le reste pour accorder des prêts et générer des profits. Dans le contexte de Bitcoin, bien que la monnaie elle-même ne soit pas soumise à la création de crédit bancaire, le concept de réserve fractionnaire s'applique lorsqu'une plateforme d'échange conserve seulement une partie des BTC déposés par ses utilisateurs, et utilise le reste pour d'autres fins. Cela pose un risque de liquidité et de solvabilité si tous les utilisateurs décident de retirer leurs fonds simultanément. C'est notamment pour cela qu'il est essentiel de conserver soi-même ses bitcoins en self-custody.

## RÉSISTANCE AU PARTITIONNEMENT

Capacité du réseau Bitcoin à rester unifié et à maintenir le consensus entre les utilisateurs, en maintenant des connexions et en évitant la séparation de certains nœuds du reste du réseau, malgré les tentatives de le fragmenter. Pour qu'un nœud demeure en consensus avec le réseau, il doit maintenir au moins une connexion active avec un ensemble de pairs partageant les mêmes règles de consensus.

> ► *En anglais, on dit « Partition Resistance ».*

## RESYNCHRONISATION

Se réfère à un phénomène dans lequel la blockchain subit une modification de sa structure à cause de l'existence de blocs concurrents à une même hauteur. Cela survient lorsqu'une portion de la chaîne de blocs est remplacée par une autre chaîne ayant une quantité de travail accumulé plus importante.

Ces resynchronisations font partie du fonctionnement naturel de Bitcoin, où différents mineurs peuvent trouver de nouveaux blocs presque simultanément, venant ainsi couper le réseau Bitcoin en deux. Dans de tels cas, le réseau peut se diviser temporairement en chaînes concurrentes. Finalement, lorsque l'une de ces chaînes accumule plus de travail, les autres chaînes sont abandonnées par les nœuds, et leurs blocs deviennent ce que l'on appelle des « blocs obsolètes » ou « blocs orphelins ». Ce processus de remplacement d'une chaîne par une autre est la resynchronisation.

![](assets/9.png)

Les resynchronisations peuvent avoir diverses conséquences. Tout d'abord, si un utilisateur avait une transaction confirmée dans un bloc qui s'avère être abandonné, mais que celle-ci ne se retrouve pas dans la chaîne finalement valide, alors sa transaction redevient non confirmée. C'est pour cette raison que l'on vous conseille de toujours attendre au moins 6 confirmations pour considérer une transaction comme réellement immuable. Passé 6 blocs de profondeur, les resynchronisations sont tellement improbables que la chance qu'il y en ait une peut être considérée comme nulle.

Ensuite, au niveau du système global, les resynchronisations impliquent un gaspillage de la puissance de calcul des mineurs. En effet, lorsqu'une division intervient, une partie des mineurs seront sur la chaîne `A`, et une autre partie sur la chaîne `B`. Si la chaîne `B` est finalement abandonnée lors d'une resynchronisation, alors toute la puissance de calcul déployée par les mineurs sur cette chaîne est par définition gaspillée. S'il y a trop de resynchronisations sur le réseau Bitcoin, la sécurité globale de celui-ci est donc réduite. C'est notamment pour cette raison, en partie, que l'augmentation de la taille des blocs ou la réduction de l'intervalle entre chaque bloc (10 minutes) peuvent être dangereuses.

> ► *Certains bitcoiners préfèrent parler de « bloc orphelin » pour désigner un bloc périmé. Aussi, même si c'est un anglicisme, on préfère parler dans le langage courant d'une « réorganisation » ou d'une « réorg » plutôt que d'une « resynchronisation ».*

## RÉTROCOMPATIBILITÉ

Fait référence à la capacité d'une mise à jour des règles du protocole à maintenir la compatibilité avec les versions antérieures. Cela signifie que les modifications sont conçues de manière à ce que les anciens nœuds (les nœuds qui exécutent des versions antérieures au changement de règles) puissent toujours interagir avec le réseau et suivre la chaîne avec le plus de travail accumulé. Il faut donc que les anciens nœuds ne rejettent ni les nouveaux blocs, ni les nouvelles transactions.

La compatibilité rétrospective permet de réduire fortement la probabilité qu'une mise à jour fragmente le réseau, évitant ainsi la division des nœuds en sous-groupes sur des chaînes différentes. Pour assurer une compatibilité avec les versions antérieures du protocole, une mise à jour doit rendre les règles existantes plus strictes ou en introduire de nouvelles. C'est ce principe qui définit un « soft fork ». À l'inverse, si une mise à jour assouplit les règles existantes ou en élimine certaines, alors elle ne sera pas rétrocompatible. Ce sera donc un « hard fork ».

## RÉUTILISATION D'ADRESSE

La réutilisation d'adresse se réfère à la pratique d'utiliser une même adresse de réception pour bloquer plusieurs UTXOs, parfois au sein de plusieurs transactions différentes. Les bitcoins sont généralement bloqués à l'aide d'une paire de clés cryptographique qui correspond à une adresse unique. Puisque la blockchain est publique, il est facile de pouvoir consulter quelles adresses sont associées à combien de bitcoins. En cas de réutilisation d'une même adresse pour plusieurs paiements, on peut raisonnablement imaginer que tous les UTXOs associés appartiennent à une même entité. La réutilisation d'adresse pose donc un problème pour la vie privée de l'utilisateur. Elle permet de faire des liens déterministes entre plusieurs transactions et plusieurs UTXOs, ainsi que de perpétuer un traçage de fonds on-chain. Satoshi Nakamoto évoquait déjà ce problème dans son White Paper :

> « *En guise de pare-feu additionnel, une nouvelle paire de clés pourrait être utilisée pour chaque transaction afin de les garder non liées à un propriétaire commun.* » - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Consulté à l'adresse https://bitcoin.org/bitcoin.pdf.

Pour préserver au minimum sa vie privée, il est vivement conseillé de n'utiliser chaque adresse de réception qu'une seule fois. À chaque nouveau paiement, il convient de générer une nouvelle adresse. Pour les outputs de change, il faut également utiliser une adresse vierge. Heureusement, grâce aux portefeuilles déterministes et hiérarchiques, il est devenu très facile d'utiliser une multitude d'adresses. Toutes les paires de clés associées à un portefeuille peuvent être facilement régénérées à partir de la graine. C'est d'ailleurs pour cette raison que les logiciels de portefeuille vous génèrent toujours une nouvelle adresse différente lorsque vous cliquez sur le bouton « Recevoir ».

> ► *En anglais, on dit « Address Reuse ».*

## RÉUTILISATION D'ADRESSE (EXT)

On dit d'une réutilisation d'adresse qu'elle est "externe" lorsqu'elle survient sur plusieurs transactions différentes. Dans cette configuration, la réutilisation d'adresse externe est une heuristique d'analyse de chaîne qui permet d'émettre une hypothèse vraisemblable selon laquelle toutes ces adresses appartiennent à une même entité.

![](assets/27.png)

## RÉUTILISATION D'ADRESSE (INT)

On dit d'une réutilisation d'adresse qu'elle est "interne" lorsqu'elle survient au sein d'une même transaction en input et en output. Dans cette configuration, la réutilisation d'adresse interne est une heuristique d'analyse de chaîne qui permet d'émettre une hypothèse vraisemblable sur le change de la transaction. En effet, s'il y a deux outputs et que l'un d'eux utilise la même adresse de réception qu'en input, alors il est vraisemblable que le second output quitte la possession de l'utilisateur initial. L'output avec l'adresse réutilisée représente vraisemblablement le change.

![](assets/10.png)

## RICOCHET

Technique consistant à réaliser plusieurs transactions fictives vers soi-même pour simuler un transfert de propriété des bitcoins. Le Ricochet permet d'estomper les spécificités pouvant compromettre la fongibilité d'une pièce Bitcoin. Par exemple, si vous réalisez un coinjoin, votre pièce en sortie de mix sera identifiée comme telle. Cette étiquette de « _pièce issue d'un coinjoin_ » peut affecter la fongibilité d'un UTXO. Des entités réglementées, telles que les plateformes d'échange, peuvent refuser d'accepter un UTXO ayant subi un coinjoin, voire exiger des explications de la part de son propriétaire, avec le risque de voir son compte bloqué ou ses fonds gelés. Dans certains cas, la plateforme peut même signaler votre comportement aux autorités étatiques. C'est là que la méthode du Ricochet entre en jeu. Pour estomper l'empreinte laissée par un coinjoin, Ricochet exécute quatre transactions successives où l'utilisateur transfère ses fonds à lui-même sur des adresses différentes. Après cet enchaînement de transactions, l'outil Ricochet achemine finalement les bitcoins vers leur destination finale, comme par exemple une plateforme d'échange. L'objectif est de créer de la distance entre la transaction coinjoin originale et l'acte de dépense final. De cette manière, les outils d'analyse de chaîne vont penser qu'il y a vraisemblablement eu un transfert de propriété après le coinjoin, et qu'il est donc inutile d'entamer des actions à l'encontre de l'émetteur. Le cas d'utilisation le plus courant de Ricochet se présente quand il est nécessaire de dissimuler une participation antérieure à un coinjoin sur un UTXO, notamment pour éviter d'être la cible des politiques LCB/FT des plateformes régulées ou des blacklists. L'outil Ricochet est disponible sur le portefeuille Samourai Wallet.

## RIPEMD160

Acronyme de *Research and development in Advanced Communications technologies in Europe Integrity Primitives Evaluation Message Digest 160*. C'est une fonction de hachage cryptographique qui génère un condensat de 160 bits à partir d'une entrée arbitraire. Elle est utilisée sur Bitcoin pour transformer une clé publique en une adresse de réception pour les standards Legacy et SegWit v0 (pour SegWit v1, la clé publique n'est pas hachée). Le processus implique d'abord l'application de la fonction de hachage `SHA256` sur la clé publique, suivie de l'application de `RIPEMD160` sur le résultat. Cette combinaison de deux fonctions de hachage distinctes est connue sous le nom de `HASH160` dans le contexte de Bitcoin. `RIPEMD160` est également utilisé dans les portefeuilles déterministes et hiérarchiques pour calculer des empreintes de clés. On utilise notamment `HASH160` pour calculer l'empreinte d'une clé parent, ensuite incluse dans les métadonnées d'une clé étendue (xpub, xprv...).

> ► *Pour plus d'informations, voir la définition de [**FONCTION DE HACHAGE**](./F.md#fonction-de-hachage).*

## RPC (REMOTE PROCEDURE CALL)

Protocole informatique permettant à un programme d'exécuter une procédure sur un autre ordinateur distant, comme si elle était exécutée localement. Spécifiquement dans le cadre de Bitcoin, on l'utilise pour permettre aux applications d'interagir avec bitcoind. Il peut être utilisé pour exécuter des commandes sur un nœud Bitcoin, telles que l'envoi de transactions, la gestion de portefeuilles ou encore l'accès à des informations sur la blockchain. La sécurité de cette interaction est assurée par une authentification via un fichier `.cookie` ou des identifiants, afin que seuls les clients autorisés puissent effectuer des RPC sur le nœud.

> ► *En français, on peut le traduire par « Appel de procédure à distance ».*

## RPOW

Sigle de « *Reusable Proofs Of Work* ». C'est un système de monnaie électronique par transfert de jetons établis sur des preuves de travail, développé et mis en œuvre par Hal Finney en 2004. RPoW se positionnait comme une amélioration des concepts théoriques de b-money et bit gold. Contrairement à ces derniers, RPoW a effectivement vu le jour et a été lancé. RPoW aurait pu prendre la place qu'occupe actuellement Bitcoin. C'était le projet le plus aboutit de monnaie électronique avant l'invention de Satoshi. Toutefois, Bitcoin surpasse RPoW en résolvant deux problèmes critiques. Premièrement, Bitcoin a introduit un ajustement automatique de la difficulté de minage, un mécanisme absent dans RPoW, évitant ainsi l'inflation due à l'augmentation des capacités de minage et au nombre croissant de mineurs. Deuxièmement, contrairement à la dépendance de RPoW aux serveurs centraux, Bitcoin a instauré un mécanisme de consensus distribué. Ce mécanisme repose sur le principe que les nœuds se synchronisent sur la chaîne avec le plus de travail accumulé, éliminant ainsi la nécessité de serveurs connus. RPoW n'a jamais reçu le soutient nécessaire pour émerger et être adopté par le grand public. Contrairement à b-money et bit gold, Satoshi Nakamoto n'a jamais cité RPoW, alors que ce système était sûrement ce qui ressemblait le plus à son invention.

## RSMPPS

Sigle de « *Recent Shared Maximum Pay Per Share* ». C'est une méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage. RSMPPS est similaire à SMPPS, mais avec une priorité accordée aux mineurs ayant contribué récemment. Cette méthode vise à récompenser les contributions actuelles en augmentant la valeur des shares soumises dans les tours de minage les plus récents, afin de favoriser les mineurs qui restent actifs et fidèles.

> ► *Pour plus d'informations, voir la définition de **[SHARES](./S.md#shares)**.*

## RUNES

Protocole développé par la même équipe que les Ordinals qui permet l'utilisation de transactions Bitcoin pour graver, frapper et transférer des actifs numériques fongibles autres que le BTC. Contrairement aux inscriptions Ordinals, où chaque unité est unique, chaque rune est identique aux autres, et donc interchangeable, ce qui permet de créer des cryptomonnaies fongibles différentes du BTC sur Bitcoin. Les messages du protocole Rune, appelés runestones, sont stockés dans des `OP_RETURN`.

> ► *Pour plus d'informations, voir les définitions de **[ORDINALS THEORY](./O.md#ordinals-theory)**, **[INSCRIPTIONS](./I.md#inscriptions)** et de **[DIGITAL ARTIFACTS](./D.md#digital-artifacts)**.*

## RUST

Langage de programmation moderne axé sur la sécurité et la performance. Il est conçu pour éviter les erreurs courantes de programmation. Rust est utilisé dans les systèmes embarqués, les applications Web, et pour le développement de logiciels nécessitant de hautes performances et une grande fiabilité. Ce langage est de plus en plus populaire dans l'environnement de Bitcoin.

## RUST-LIGHTNING

Bibliothèque Lightning développée en Rust par la communauté Rust Bitcoin en collaboration avec Square. Rust-Lightning fournit une implémentation de Lightning. Elle sert de base au *Lightning Development Kit* (LDK).

> ► *Pour plus d'informations, voir la définition de **[LDK](./L.md#ldk-lightning-dev-kit)**.
