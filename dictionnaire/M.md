## MACAROON

Mécanisme d'authentification conçu pour sécuriser l'accès à des services sur des systèmes distribués. Les macaroons sont notamment utilisés sur Lightning pour authentifier les utilisateurs lorsqu'ils accèdent à des services délégués. Par exemple, avec un nœud Lightning, il est possible de générer un macaroon qui autorise la réalisation de transactions à partir de votre smartphone via votre nœud distant. À la différence des cookies, les macaroons offrent l'avantage de pouvoir être validés cryptographiquement par l'émetteur ou d'être délégués pour vérification.

## MAGICAL BITCOIN

Ancien nom de la collection d'outils et de bibliothèques pour développeurs BDK.

> ► *Pour plus d'informations, voir la définition de [**BDK (BITCOIN DEV KIT)**](./B.md#bdk-bitcoin-dev-kit).*

## MAGIC NETWORK

Constantes utilisées dans le protocole Bitcoin pour identifier le réseau spécifique (mainnet, testnet, regtest...) d'un message échangé entre des nœuds. Ces valeurs sont inscrites au début de chaque message pour faciliter leur identification dans le flux de données. Les Magic Network sont conçus pour être rarement présents dans des données de communication ordinaires. En effet, ces 4 octets sont peu fréquents dans l'ASCII, sont invalides en UTF-8 et génèrent un très grand entier de 32 bits, peu importe le format de stockage des données. Les Magic Network sont (en format little-endian) :
* Mainnet :

```text
f9beb4d9
```

* Testnet :

```text
0b110907
```

* Regtest :

```text
fabfb5da
```

> ► *C'est 4 octets sont parfois également nommés « Magic Number », « Magic Bytes » ou encore « Start String ».*

## MAINNET

Désigne le réseau principal où les transactions réelles de Bitcoin sont enregistrées et exécutées. Le mainnet est tout simplement le réseau Bitcoin. Contrairement aux testnets, regtests et signets, le mainnet implique l'utilisation de bitcoins ayant une valeur économique réelle.

## MAINTENEUR (CORE)

Dans le contexte du projet Bitcoin Core, l'implémentation majoritaire de nœuds sur le réseau Bitcoin, les mainteneurs sont des individus chargés de la gestion du projet. Ils portent la responsabilité de l'implémentation. Ils sont chargés de la modération sur le dépôt GitHub Bitcoin Core et de l'établissement du calendrier pour la publication des nouvelles versions. Ils sont surtout chargés de conduire la fusion des pull requests (PR) proposées par les contributeurs. 

Autrement dit, lorsqu'une proposition de modification du code a passé les divers stades de validation, ce sont ces mainteneurs qui assument la grande responsabilité de fusionner le nouveau code avec le logiciel Bitcoin Core. Avant de procéder à cette fusion, les mainteneurs vérifient si le code respecte bien les principes fondamentaux du projet, s'il a atteint les standards minimums requis pour être inclus, et ils jugent également le consensus général des contributeurs à propos de cette modification. Lorsque j'écris cette définition, seuls quatre mainteneurs subsistent sur Bitcoin Core : Hennadii Stepanov, Michael Ford, Andrew Chow et Gloria Zhao.

## MAINTENEUR PRINCIPAL (CORE)

Le mainteneur principal était un rôle au sein de la hiérarchie sur Bitcoin Core. Ce rôle n'existe plus depuis février 2023. Cette personne était chargée de diriger le projet et avait donc plus de pouvoir que les mainteneurs. Le rôle de mainteneur principal fut naturellement endossé par Satoshi Nakamoto jusqu'à son départ au début de l'année 2011. Par la suite, Gavin Andresen, ayant déjà contribué aux côtés de Satoshi, prit la relève à la tête du logiciel jusqu'au début de l'année 2014. À partir de cette date, Wladimir J. van der Laan a pris ce rôle jusqu'en février 2023. Depuis, il n'y a plus aucun mainteneur principal pour le projet.

## MAJORITÉ ÉCONOMIQUE

Désigne la plus grande proportion de l'activité économique liée à la monnaie bitcoin, générée par les commerçants. Un commerçant désigne toute entité physique ou morale acceptant d'échanger un bien ou un service contre du BTC. Ces commerçants, qui incluent les commerces, les utilisateurs, les plateformes d'échange, et les mineurs, varient en taille et en influence économique. Certains sont des acteurs majeurs, générant une activité économique substantielle, tandis que d'autres sont plus modestes. La majorité économique est donc définie par ceux dont l'activité économique combinée représente la part prépondérante sur cette monnaie. Cette majorité a une influence sur les règles de consensus, notamment en cas de fork.

## MALLÉABILITÉ (TRANSACTION)

Se réfère à la possibilité de modifier légèrement la structure d'une transaction Bitcoin, sans en altérer l'effet, mais tout en changeant l'identifiant de transaction (*TXID*). Cette propriété peut être exploitée malicieusement pour induire en erreur les parties prenantes sur le statut d'une transaction, causant ainsi des problèmes comme la double dépense. La malléabilité était rendue possible par la flexibilité de la signature numérique utilisée. Le soft fork SegWit a notamment été introduit pour empêcher cette malléabilité des transactions Bitcoin, rendant compliquée une implémentation du Lightning Network. Il y parvient en écartant les données malléables de la transaction du calcul du TXID.

> ► *Bien que ce soit rare, on retrouve parfois le terme de « mutabilité » pour évoquer le même concept.*

## MAN-IN-THE-MIDDLE (MITM)

Attaque dans laquelle un acteur malveillant se place clandestinement entre deux parties communiquant, afin d'intercepter et potentiellement de modifier les messages échangés, sans que les deux parties ne remarquent sa présence.

> ► *En français, on parle d'une « attaque de l'homme du milieu » ou « HDM ».*

## MAPPER (TO MAP)

Dans le contexte de l'informatique, mapper désigne le processus d'associer des éléments d'un ensemble de données à des éléments d'un autre ensemble de données de manière systématique. Cette association permet aux données du premier ensemble de se substituer à celles du second ensemble ou de transitionner de l'un à l'autre. Cette technique est souvent utilisée dans les opérations de transformation de données.

## MARKET CAP (CAPITALIZATION)

Représente la valeur totale d'un actif en circulation, comme le bitcoin. Elle est calculée en multipliant le nombre total de pièces en circulation par le prix actuel de chaque unité. Ce chiffre donne une indication de la taille globale et de la valeur du marché de Bitcoin.

> ► *En français, on pourrait le traduire par « capitalisation boursière ».*

## MASF

Sigle de « *Miner-Activated Soft Fork* ». Qualifie un soft fork dans Bitcoin lorsque son activation provient d'une action des mineurs. Les MASF sont une famille de méthodes d'activation de soft fork sur Bitcoin. Dans ces approches, les mineurs signalent leur accord et leur préparation pour une mise à jour du protocole en minant des blocs qui soutiennent le verrouillage du soft fork. Si une majorité significative de mineurs se prononce en faveur du soft fork, la mise à jour est considérée comme acceptée et est activée ultérieurement. Ce processus permet d'éviter la division de la blockchain et de maintenir l'unité du réseau. Le MASF est préféré pour son approche plus douce et consensuelle, réduisant le risque de scission de la blockchain tout en assurant que la majorité de la puissance de calcul soutient la nouvelle mise à jour. Les méthodes d'activation BIP34, BIP9, BIP8 (si `LOT=false` ou si le seuil de vote est atteint) ou encore Speedy Trial sont des MASF.

## MAST

Sigle de « *Merkelised Alternative Script Tree* ». Technique employant un arbre de Merkle pour résumer un nombre arbitraire de conditions de dépenses sélectionnées par l'utilisateur dans une adresse de réception, dont une doit être remplie pour dépenser les bitcoins concernés. L'arbre de Merkle permet à l'utilisateur de choisir quelle condition il souhaite remplir sans révéler les détails des autres conditions sur la blockchain. Cela permet de réduire les frais liés à ces scripts, de créer des conditions beaucoup plus lourdes et, sur un temps plus long, d'améliorer la confidentialité de l'utilisateur (en plus de l'utilisation conjointe de Schnorr). Ce concept a fait l'objet de plusieurs propositions, mais il a finalement était ajouté à Bitcoin via le soft fork Taproot en 2021.

> ► *Initialement, « MAST » était l'acronyme de « Merklized Abstract Syntax Tree ». L'utilisation qui en est faite dans le cadre de Taproot n'a plus rien à voir avec un « Abstract Syntax Tree ». Toutefois, les utilisateurs continuaient d'employer ce terme de MAST. Anthony Towns a donc proposé de modifier la signification initiale tout en conservant cet acronyme largement employé avec : « Merklized Alternative Script Tree ».*

## MASTER FINGERPRINT

Empreinte de 4 octets (32 bits) de la clé privée maîtresse dans un portefeuille hiérarchique déterministe (HD). Elle est obtenue en calculant le hash `SHA256` de la clé privée maîtresse, suivi d'un hash `RIPEMD160`, procédé désigné par `HASH160` sur Bitcoin. La Master Fingerprint sert à identifier un portefeuille HD, indépendamment des chemins de dérivation, mais en prenant en compte la présence ou non d'une passphrase. C'est une information concise qui permet de faire référence à l'origine d'un ensemble de clés, sans pour autant dévoiler des informations sensibles sur le portefeuille.

## MAX_BLOC_SIZE

Constante qui spécifie la taille maximale qu'un bloc peut avoir sur Bitcoin. Historiquement, cette limite était fixée à 1 Mo, une mesure mise en place par Satoshi Nakamoto en 2010, afin de prévenir le spam et de maintenir une certaine décentralisation du réseau.

## MEMPOOL

Contraction des termes « memory » et « pool ». Cela désigne un espace virtuel dans lequel les transactions Bitcoin en attente d'inclusion dans un bloc sont regroupées. Lorsqu'une transaction est créée et diffusée sur le réseau Bitcoin, elle est d'abord vérifiée par les nœuds du réseau. Si elle est considérée comme valide, elle est alors placée dans la Mempool de chaque nœud, où elle reste jusqu'à ce qu'elle soit sélectionnée par un mineur pour être incluse dans un bloc. 

Il est important de noter que chaque nœud du réseau Bitcoin maintient sa propre Mempool, et donc, il peut y avoir des variations dans le contenu de la Mempool entre différents nœuds à un moment donné. Notamment, le paramètre `maxmempool` dans le fichier `bitcoin.conf` de chaque nœud permet aux opérateurs de contrôler la quantité de RAM (mémoire vive) que leur nœud utilisera pour stocker les transactions en attente dans la Mempool. En limitant la taille de la Mempool, les opérateurs de nœuds peuvent éviter que celle-ci ne consomme trop de ressources sur leur système. Ce paramètre est spécifié en mégaoctets (MB). La valeur par défaut de Bitcoin Core à ce jour est de 300 Mo. 

Les transactions présentent dans les mempool sont provisoires. Elles ne doivent pas être considérées comme immuable tant qu’elles ne sont pas incluses dans un bloc, et après un certain nombre de confirmations. Celles-ci peuvent souvent être remplacées ou purgées.

## MEMPOOL.DAT

Nom du fichier de données utilisé par le logiciel Bitcoin Core pour stocker l'état actuel de la mempool, qui est l'ensemble des transactions non confirmées en attente d'être ajoutées à un bloc.

## MERGE

Dans le cadre de Git, représente l'action d'intégrer les modifications d'une branche à une autre, typiquement de ramener les développements d'une branche secondaire dans la branche principale. Cette opération permet de combiner les historiques de commit des branches concernées et de résoudre les éventuels conflits pour maintenir l'intégrité du logiciel.

> ► *En français, on peut traduire « merge » par « fusion ».*

## MERKLE BLOCK

Structure de données utilisée dans le cadre du BIP37 (*Transaction Bloom Filtering*) pour fournir une preuve compacte de l'inclusion de transactions spécifiques dans un bloc. C'est notamment utilisé pour les portefeuilles SPV. Le Merkle Block contient les en-têtes de bloc, les transactions filtrées et un arbre de Merkle partiel, permettant aux clients légers de vérifier rapidement si une transaction appartient à un bloc sans télécharger toutes les transactions.

## MÉTADONNÉES

Dans le domaine général de l'informatique, cela désigne les données qui fournissent des informations sur d'autres données. Elles décrivent les caractéristiques, le contenu, la qualité, le format et la structure des données qu’elles accompagnent. On différencie ainsi la charge utile (payload), qui représente le cœur de l'information, et les métadonnées. Par exemple, pour un document, les métadonnées peuvent inclure l'auteur, la date de création, la taille du fichier et les mots-clés associés. Sur Bitcoin, on retrouve des métadonnées dans de nombreux éléments. On en utilise dans les adresses de réception, les clés étendues, les blocs...

## MÉTHODE D'ACTIVATION

Une méthode d'activation est le processus par lequel la communauté d'utilisateurs décide de l'implémentation d'un soft fork sur le protocole Bitcoin, en cherchant à éviter une séparation de la blockchain. Ce processus consiste à solliciter l'opinion des mineurs pour approuver un soft fork avant son activation. Si une majorité importante accepte le soft fork, le risque de scission de la blockchain est minimisé. Ce consensus est crucial car, si une majorité de mineurs refusent de faire la modification, le soft fork pourrait créer deux chaînes distinctes - une avec les règles modifiées et l'autre sans. Il existe 2 grandes catégories de méthodes d'activation : 
* Les UASF (User-Activated Soft Fork) lorsque ce sont les nœuds qui imposent la mise à jour ;
* Les MASF (Miner-Activated Soft Fork) lorsque ce sont les mineurs qui déclenchent l'activation.

Il existe de nombreuses méthodes d'activation différentes qui ont été testées au fur et à mesure de l'évolution de Bitcoin. À l'époque de Satoshi, le processus d'activation n'était pas formellement établi. Les modifications étaient souvent arbitraires et parfois même réalisées sans informer la communauté. Plus tard, la méthode du *Flag Day* a été adoptée. Après le retrait de Satoshi, d'autres méthodes ont été successivement utilisées, notamment le BIP34, le BIP9, le BIP8, et enfin, le *Speedy Trial*.

## MÉTHODE GÉOMÉTRIQUE

Méthode de calcul de la rémunération des mineurs dans le contexte des pools de minage. Ce système de paiement est établi sur un score, conçu pour contrer le phénomène de pool hopping. Elle assure que le paiement par share soumise reste constant, indépendamment du moment de soumission. Les mineurs accumulent des scores, calculés avec un facteur de décroissance, et les paiements sont calculés à la fin du cycle. Ils sont proportionnels à leur score. Cette méthode implique des frais variables et fixes pour le mineur, et réduit la variance des paiements par share.

> ► *Pour plus d'informations, voir la définition de **[SHARES](./S.md#shares)**.*

## MINAGE

Action de participer à la preuve de travail (*Proof-of-Work*) du système Bitcoin. La preuve de travail est un mécanisme de résistance aux attaques Sybil. Elle est à la base du mécanisme de consensus de Nakamoto, qui est le principe utilisé pour établir un accord sur une version unique du registre distribué entre les différents nœuds du réseau. 

Concrètement, le minage est la recherche d’une valeur qui, une fois passée dans une fonction mathématique aléatoire, donne un résultat inférieur à un nombre cible. Cette cible de la preuve de travail est ajustée tous les 2016 blocs par les nœuds. C’est ce que l’on appelle l’ajustement de la difficulté. On abaisse le nombre cible pour augmenter la difficulté de minage, ou on l’augmente pour baisser la difficulté, en fonction de l’évolution de la puissance de calcul déployée par les mineurs durant la période précédente. 

![](assets/34.png)

Ce travail effectué par les mineurs est récompensé à chaque bloc valide trouvé. Le mineur gagnant empoche une récompense pécuniaire, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction. Aujourd’hui, la difficulté de la preuve de travail sur Bitcoin est telle que le minage nécessite une grande puissance de calcul pour parvenir à gagner des blocs. En conséquence, il faut souvent disposer de puces électroniques spécialisées dans l’exécution de `SHA256d`, que l’on appelle des ASICs, et participer dans des pools de minage.

## MINAGE ÉGOÏSTE

Stratégie (ou attaque) dans le minage, où un mineur ou un groupe de mineurs conserve intentionnellement des blocs avec une preuve de travail valide sans les diffuser immédiatement sur le réseau. L'objectif est de conserver une avance sur les autres mineurs en termes de preuve de travail, ce qui leur permet potentiellement de miner plusieurs blocs d'affilée et de les publier en une seule fois, maximisant ainsi leurs gains. 

Autrement dit, le groupe de mineur attaquants ne minent pas sur le dernier bloc validé par l'ensemble du réseau, mais plutôt sur un bloc qu'ils ont eux-mêmes créé, qui diffère de celui validé par le réseau. Ce procédé génère une sorte d'embranchement secret de la blockchain, qui reste inconnue de l'ensemble du réseau, jusqu'à ce que cette chaîne alternative dépasse potentiellement la blockchain honnête. Une fois que la chaîne secrète des mineurs attaquants devient plus longue (c'est-à-dire qu'elle contient plus de travail accumulé) que la chaîne honnête et publique, elle est alors diffusée sur l'ensemble du réseau. À ce moment-là, les nœuds du réseau, qui suivent la chaîne la plus longue (avec le plus de travail accumulé), vont se synchroniser sur cette nouvelle chaîne. Il y a donc une réorganisation. 

Le minage égoïste est embêtant, car il diminue la sécurité du système en gaspillant une partie de la puissance de calcul du réseau. En cas de réussite, il conduit également à des réorganisations de la blockchain, affectant ainsi la fiabilité des confirmations de transaction pour les utilisateurs. Cette pratique reste tout de même risquée pour le groupe de mineur attaquant, car il est souvent plus rentable de miner normalement au-dessus du dernier bloc connu publiquement plutôt que d'allouer de la puissance de calcul à un embranchement secret qui ne dépassera probablement jamais la blockchain honnête. Au plus le nombre de blocs dans la réorganisation est grand, au plus la probabilité de réussite de l'attaque est basse.

> ► *La traduction anglaise de « minage égoïste » est « selfish mining ». Attention, une attaque par selfish mining ne doit pas être confondue avec une attaque de block withholding (bloc retenu).*

## MINAGE FUSIONNÉ

Technique de consensus de sidechain permettant aux mineurs de Bitcoin de travailler simultanément sur la chaîne principale et sur une ou plusieurs sidechains, sans pour autant devoir fournir plus de travail de calcul. Il s'agit donc de réutiliser la preuve de travail de Bitcoin pour des applications tierces. Toutefois, le minage fusionné présente un désavantage notable pour le mineur : il nécessite l'installation et l'exécution d'un logiciel de nœud spécifique à chaque sidechain pour permettre la réutilisation de ses preuves de travail. De plus, la récompense obtenue pour le minage d'une sidechain est versée sur celle-ci et non directement en BTC sur la blockchain principale.

> ► *En anglais, on parle de « Merged Mining » ou « MM ».*

## MINAGE FUSIONNÉ AVEUGLE

Technique de consensus de sidechain permettant aux mineurs de Bitcoin de travailler simultanément sur la chaîne principale et sur une ou plusieurs sidechains, sans pour autant devoir fournir plus de travail de calcul. Contrairement au minage fusionné classique, cette méthode ne nécessite pas de configurer un nouveau nœud pour chaque sidechain exploitée. Dans le cadre du *Blind Merged Mining* (BMM), chaque sidechain est gérée par des opérateurs de nœud indépendants, responsables de la création des blocs et de la récolte des récompenses associées sur la sidechain. En contrepartie, ces opérateurs doivent acheter des preuves de travail auprès des mineurs de la blockchain principale pour valider leurs blocs sur la sidechain. Ainsi, les mineurs de Bitcoin reçoivent leurs récompenses du minage fusionné des sidechains en BTC, directement sur la chaîne principale. Cette méthode, développée par Paul Sztorc pour les drivechains, nécessite l'implémentation du BIP301 pour être opérationnelle sur le réseau Bitcoin.

> ► *En anglais, on parle de « Blind Merged Mining » ou « BMM ».*

## MINEUR

Dans le contexte de Bitcoin, un mineur fait référence à un ordinateur engagé dans le processus de minage, qui consiste à participer à la preuve de travail (*Proof-of-Work*). Le mineur regroupe les transactions en attente dans sa mempool pour former un bloc candidat. Ensuite, il recherche un hachage valide, inférieur ou égal à la cible, pour l’entête de ce bloc en modifiant les différents nonces. S’il trouve un hachage valide, il diffuse son bloc au réseau Bitcoin et empoche la récompense pécuniaire associée, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction. Par extension, le terme de « mineur » désigne également la personne ou l'entité qui possède et opère un ou plusieurs de ces ordinateurs.

> ► *Dans le cadre spécifique des pools de minage, on différencie parfois le rôle de mineur du rôle de hacheur, étant donné que les mineurs individuels qui participent à la mutualisation doivent uniquement hacher.*

## MINISCRIPT

Framework permettant de fournir un cadre pour programmer des scripts de manière sécurisée sur Bitcoin. Le langage natif de Bitcoin s'appelle script. Celui-ci est assez complexe à utiliser en pratique, notamment pour des applications sophistiquées et personnalisées. Surtout, il est très difficile de vérifier les limitations d'un script. Miniscript utilise un sous-ensemble de scripts Bitcoin pour simplifier leur création, leur analyse et leur vérification. Chaque miniscript est équivalent 1 pour 1 avec un script natif. On utilise un langage de policies facile à utiliser, qui est ensuite compilé en miniscript, pour enfin correspondre à un script natif. 

![](assets/30.png)

Miniscript permet ainsi aux développeurs de construire des scripts sophistiqués d'une manière plus sûre et plus fiable. Les propriétés essentielles de Miniscript sont les suivantes : 
* Il permet une analyse statique du script, notamment des conditions de dépenses qu'il permet et de son coût en termes de ressources ;
* Il permet de réaliser des scripts qui respectent le consensus ;
* Il permet d'analyser si oui ou non, les différents chemins de dépense respectent les règles standards des nœuds ;
* Il permet de mettre en place un standard général, compréhensible et composable, pour l'ensemble des logiciels et matériels de portefeuille.

Le projet Miniscript a été lancé en 2018 par Peter Wuille, Andrew Poelstra et Sanket Kanjalkar, via l'entreprise Blockstream. Miniscript est ajouté au wallet Bitcoin Core en mode watch-only en décembre 2022 avec la version 24.0, puis complètement en mai 2023 avec la version 25.0.

## MINITAPSCRIPT

Version de Miniscript pour Tapscript. Tapscript dispose de quelques différences notables avec Script dans sa version originale. MiniTapscript fournit ainsi la prise en charge de Tapscript dans Miniscript.

> ► *Ce terme est parfois contesté. En effet, certains bitcoiners préfèrent parler de « TapMiniscript ». Pour plus d'informations, voir la définition de **[MINISCRIPT](./M.md#miniscript)** et de **[TAPSCRIPT](./T.md#tapscript)**.*

## MIT X11

Licence de logiciel libre très permissive qui autorise les utilisateurs à copier, modifier, fusionner, publier, distribuer, sous-licencier et vendre le logiciel. Elle exige uniquement que la licence originale et les notifications de droits d'auteur soient conservées dans toutes les copies ou distributions substantielles du logiciel. Contrairement à la licence GPL, la licence MIT ne requiert pas que les adaptations ou les versions dérivées du logiciel soient distribuées sous la même licence. Cette flexibilité fait de la licence MIT X11 un choix populaire pour de nombreux projets open source, y compris dans l'environnement de Bitcoin. Satoshi Nakamoto a d'ailleurs choisi cette licence pour la première version de Bitcoin publiée en 2009, et elle reste en usage pour le projet Bitcoin Core aujourd'hui.

## MIXAGE

Dans le domaine général des mathématiques, le mixage ou le mélange se réfère à la propriété d'un système dynamique où, après un certain temps, toutes les portions de l'espace initial peuvent en théorie se retrouver mêlées avec n'importe quelle autre portion. Le mixage implique que la position d'une particule ou l'état d'un système évolue de telle manière que sa distribution future soit indépendante de sa distribution initiale, atteignant ainsi un état où les caractéristiques de l'état initial sont uniformément distribuées dans tout l'espace du système. Dans le cadre de Bitcoin, on peut utiliser cette notion pour évaluer la qualité d'un processus de mélange de pièces comme un coinjoin.

> ► *En anglais, on parle de « mixing ». Certains bitcoiners différencient la notion de mixage du processus de coinjoin. En effet, ils disent que le mixage se réfère au mélange de pièces effectué par une entité possédant les fonds, contrairement aux coinjoins où l'utilisateur conserve toujours la possession des fonds. Toutefois, selon moi, cette distinction est incorrecte, car le coinjoin implique nécessairement un mixage au sens mathématique du terme. Pour plus d'informations, voir la définition de **[COINJOIN](./C.md#coinjoin)***

## MODÈLE DE SCRIPT

Template permettant l'utilisation de scripts standards. Un modèle de script est essentiellement une petite liste d'opcodes mis ensembles pour former une norme qui spécifie une manière d'établir des conditions de dépenses sur des bitcoins. Voici quelques exemples de modèles de script : P2PK, P2PKH, P2WPKH, P2SH...

## MODÈLE DE TRANSACTION

Un pattern de transaction est simplement un modèle ou une structure globale de transaction typique, que l’on peut retrouver sur la blockchain, et dont on connaît l’interprétation vraisemblable qui nous sera utile dans le cadre d'une analyse de chaîne. Lorsque l’on étudie les patterns, on va s’attarder sur une seule transaction que l’on va analyser à un niveau élevé (contrairement aux heuristiques internes et externes d'analyse de chaîne). En d’autres termes, nous allons uniquement regarder le nombre d’UTXOs en inputs et le nombre d'UTXOs en outputs, sans nous attarder sur les détails plus spécifiques ou l'environnement de la transaction. À partir du modèle observé, nous pourrons interpréter la nature de la transaction. On va alors rechercher des caractéristiques sur sa structure et en déduire une interprétation vraisemblable.

> ► *En anglais, on parle de « patterns ».*

## MODÈLE TEMPOREL

Certains comportements humains sont reconnaissables on-chain. Celui qui est le plus utile dans une analyse de chaîne, c’est peut-être votre rythme de sommeil ! Et oui, lorsque vous dormez, à priori, vous ne diffusez pas de transactions Bitcoin. Or, vous dormez généralement à peu près aux mêmes horaires. Il est donc courant d’utiliser des analyses temporelles dans l’analyse de chaîne. Il s'agit tout simplement du recensement des heures auxquelles les transactions d'une entité donnée sont diffusées au réseau Bitcoin. L’analyse de ces modèles temporels nous permet de déduire de nombreuses informations. 

Tout d’abord, une analyse temporelle permet parfois d’identifier la nature de l’entité tracée. Si l’on observe que les transactions sont diffusées de manière constante sur 24 heures, alors cela va trahir une forte activité économique. L’entité derrière ces transactions est vraisemblablement une entreprise, potentiellement internationale et peut-être avec des procédures automatisées en interne. Au contraire, si l’on voit que le pattern temporel est plutôt réparti sur 16 heures bien spécifiques, alors on peut estimer que l’on a affaire à un utilisateur individuel, ou peut-être à une entreprise locale en fonction des volumes échangés.

Au-delà de la nature de l’entité observée, le pattern temporel peut également nous indiquer approximativement la localisation de l’utilisateur grâce aux fuseaux horaires. On pourra ainsi rapprocher d’autres transactions, et utiliser l’horodatage de celles-ci comme une heuristique supplémentaire pouvant s’ajouter dans une analyse de chaîne.

Dans un registre différent, c'est également une analyse temporelle de ce type qui a permis de formuler l'hypothèse selon laquelle Satoshi Nakamoto n’opérait pas depuis le Japon, mais bien depuis les États-Unis : [_The Time Zones of Satoshi Nakamoto_](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f).

## M-OF-N

Désigne un portefeuille ou un script multisignatures à seuil. Pour renforcer la sécurité de bitcoins, on peut utiliser un système de sécurisation multisignatures à seuil qui exige que `m` parmi `n` signatures soient faites pour pouvoir dépenser les fonds. Dans un m-de-n, la lettre `m` désigne le seuil de signatures requis et la lettre `n` désigne le nombre total de clés existantes pouvant signer. Par exemple, dans une configuration 2-de-3, deux signatures sur trois possibles sont nécessaires pour exécuter une transaction.

## MTP (MEDIAN TIME PAST)

Concept utilisé dans le protocole Bitcoin pour déterminer une marge sur l'horodatage consensuel du réseau. Le MTP est défini comme la médiane des horodatages des 11 derniers blocs minés. L'utilisation de cet indicateur permet d'éviter les désaccords entre les nœuds sur l'heure exacte en cas de décalage. Le MTP était initialement utilisé pour vérifier la validité de l'horodatage des blocs par rapport au passé. Depuis le BIP113, il est également utilisé comme référentiel du temps du réseau pour vérifier la validité des opérations de verrouillages temporels (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` et `OP_CHECKSEQUENCEVERIFY`).

## MULTISIG

Les portefeuilles multisignatures, souvent abrégés « multisig », sont conçus pour renforcer la sécurisation de bitcoins en exigeant plusieurs signatures provenant de différentes clés privées pour autoriser une dépense. Cette méthode répartit le risque entre plusieurs clés, ce qui permet de réduire à la fois le risque de perte et celui de vol (selon la configuration du multisig). Les portefeuilles multisig fonctionnent selon un modèle « m-de-n », où `m` désigne le nombre minimal de signatures requises pour valider une transaction, et `n` le nombre total de clés impliquées. Par exemple, une configuration 2-de-3 nécessite deux signatures sur trois possibles pour valider une transaction. Cette approche offre une sécurité supérieure par rapport aux portefeuilles à clé unique, mais elle introduit également plus de complexité en termes de gestion et de sauvegarde. De plus, les transactions utilisant les anciens standards de multisig sont moins confidentielles et plus coûteuses en frais que les transactions singlesig classiques. Cependant, des innovations récentes telles que Taproot et l'utilisation de descriptors vont permettre de minimiser voire d'éliminer ces inconvénients des multisigs.

> ► *Certains bitcoiners distinguent les termes « Multisig » et « Multisig à seuil ». En effet, certains affirment qu'un multisig est forcément un n-de-n, tandis qu'un multisig à seuil est un m-de-n. Toutefois, dans le langage courant, il est accepté de parler de « Multisig » même pour m-de-n.*
