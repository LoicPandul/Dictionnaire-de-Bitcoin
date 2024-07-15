## ADAPTOR SIGNATURE

Méthode cryptographique permettant de combiner une vraie signature avec une signature supplémentaire (appelée « adaptor signature ») pour révéler une donnée secrète. Cette méthode fonctionne telle que la connaissance de deux éléments parmi la signature valide, l'adaptor signature et le secret permet de déduire le troisième manquant. Une des propriétés intéressantes de cette méthode est que si nous connaissons l'adaptor signature de notre pair et le point spécifique sur la courbe elliptique lié au secret utilisé pour calculer cette adaptor signature, nous pouvons alors dériver notre propre adaptor signature qui correspondra avec le même secret, et ce, sans jamais avoir accédé directement au secret lui-même. Dans un échange entre deux parties prenantes ne se faisant pas confiance, cette technique permet un dévoilement simultané de deux informations sensibles entre les participants. Ce processus élimine la nécessité de confiance lors de transactions instantanées telles qu'un Coin Swap ou un Atomic Swap. Prenons un exemple pour bien comprendre. Alice et Bob souhaitent s'envoyer 1 BTC chacun, mais ils ne se font pas confiance. Ils vont donc utiliser des adaptors signatures pour annihiler le besoin de confiance envers l'autre partie dans cet échange (c'est donc un échange « atomique »). Ils procèdent comme ceci :
* Alice lance cet échange atomique. Elle crée une transaction $m_A$ qui envoie 1 BTC vers Bob. Elle crée une signature $s_A$ qui permet de valider cette transaction grâce à sa clé privée $p_A$ ($P_A = p_A \cdot G$), et en utilisant un nonce $n_A$ et un secret $t$ ($N_A = n_A \cdot G$ et $T = t \cdot G$) : 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice calcule l'adaptor signature $s_A'$ à partir du secret $t$ et de sa vraie signature $s_A$ :  
$$s_A' = s_A - t$$
&nbsp;
* Alice envoie à Bob son adaptor signature $sA'$, sa transaction non signée $m_A$, le point correspondant au secret $T$ et le point correspondant au nonce $N_A$. Nous appelons ces informations un « adaptor ». Notons qu'avec simplement ces informations, Bob n'est pas en capacité de récupérer le BTC d'Alice.
* En revanche, Bob peut vérifier qu'Alice n'est pas en train de l'entourlouper. Pour ce faire, il vérifie que l'adaptor signature d'Alice $s_A'$ correspond bien à la transaction promise $m_A$. Si l'équation suivante est juste, alors il est persuadé que l'adaptor signature d'Alice est valide : 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Cette vérification donne à Bob des garanties de la part d'Alice, de telle sorte qu'il peut continuer le processus d'échange atomique sereinement. Il va alors créer à son tour sa propre transaction $m_B$ envoyant 1 BTC à Alice et sa propre adaptor signature $s_B'$ qui sera liée avec le même secret $t$ que seule Alice connait pour le moment (Bob n'a pas connaissance de cette valeur $t$, mais uniquement de son point correspondant $T$ qu'Alice lui a fourni) : 
$$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob envoie à Alice son adaptor signature $s_B'$, sa transaction non signée $m_B$, le point correspondant au secret $T$ et le point correspondant au nonce $N_B$. Alice peut désormais combiner l'adaptor signature de Bob $s_B'$ avec le secret $t$, dont elle seule a connaissance, afin de calculer une signature valide $s_B$ pour la transaction $m_B$ qui lui envoie le BTC de Bob : 
$$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice diffuse cette transaction $m_B$ signée sur la blockchain Bitcoin afin de récupérer le BTC que Bob lui a promis. Bob prend connaissance de cette transaction sur la blockchain. Il est donc en capacité d'en extraire la signature $s_B = s_B' + t$. À partir de cette information, Bob peut isoler le fameux secret $t$ dont il avait besoin :
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Or, ce secret $t$ était la seule information manquante à Bob pour produire la signature valide $s_A$, à partir de l'adaptor signature d'Alice $s_A'$, qui lui permettra de valider la transaction $m_A$ qui envoie un BTC depuis Alice vers Bob. Il calcule alors $s_A$ et diffuse à son tour la transaction $m_A$ : $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;

## ADDR

Message réseau anciennement utilisé sur Bitcoin pour communiquer les adresses des nœuds qui acceptent des connexions entrantes. Cet ancien format, se limitant à 128 bits par adresse, était seulement adapté aux adresses IPv6, IPv4 et aux adresses Tor de version 2. Face à l'arrivée de nouveaux protocoles comme Tor V3 et la nécessité de disposer d'une meilleure évolutivité pour de futurs protocoles réseau, le format `addr` a été supplanté par `addrv2`, introduit dans le BIP155.

## ADDR.DAT

Nom de l'ancien fichier utilisé dans Bitcoin Core pour stocker des informations sur les pairs (c'est-à-dire, les nœuds) du réseau avec lesquels le nœud de l'utilisateur a interagi ou peut potentiellement interagir. Ce fichier a été remplacé par le fichier peers.dat depuis la version 0.7.0.

## ADDRV2

Évolution proposée avec le BIP155 du message `addr` sur le réseau Bitcoin. Le message `addr` servait à diffuser les adresses de nœuds qui acceptent des connexions entrantes, mais il était limité à des adresses de 128 bits. Cette taille était adéquate pour les adresses IPv6, IPv4, et Tor V2, mais insuffisante pour d'autres protocoles. La version mise à jour `addrv2` est conçue pour supporter des adresses plus longues, notamment les services cachés Tor v3 de 256 bits, ainsi que d'autres protocoles réseau tels que I2P ou de futurs protocoles.

## ADRESSE DE RÉCEPTION

Information utilisée pour recevoir des bitcoins. Une adresse est généralement construite en hachant une clé publique, à l'aide de `SHA256` et de `RIMPEMD160`, et en ajoutant des métadonnées à ce condensat. Les clés publiques utilisées pour construire une adresse de réception font partie du portefeuille de l'utilisateur et sont donc dérivées depuis sa graine. Par exemple, les adresses SegWit sont composées des informations suivantes : 
* Un HRP pour désigner « bitcoin » : `bc` ; 
* Un séparateur : `1` ; 
* La version de SegWit utilisée : `q` ou `p` ; 
* La charge utile : le condensat de la clé publique (ou directement la clé publique dans le cas de Taproot) ; 
* La somme de contrôle : un code BCH.

Mais une adresse de réception peut également représenter autre chose en fonction du modèle de script utilisé. Par exemple, les adresses P2SH sont construites à l'aide du hachage du script. Les adresses Taproot, elles, contiennent directement la clé publique tordue (*tweaked*) sans qu'elle soit hachée.

Une adresse de réception peut être représentée sous la forme d'une chaîne de caractères alphanumériques ou sous la forme d'un QR code. Chaque adresse peut être utilisée plusieurs fois, mais c'est une pratique très déconseillée. En effet, dans le but de maintenir un certain niveau de confidentialité, il est conseillé de n'utiliser chaque adresse Bitcoin qu'une seule fois. Il faut en générer une nouvelle pour tout paiement entrant vers son portefeuille. Une adresse est encodée en `Bech32` pour les adresses SegWit V0, en `Bech32m` pour les adresses SegWit V1, et en `Base58check` pour les adresses Legacy. D'un point de vue technique, une adresse ne permet pas réellement de recevoir des bitcoins, mais plutôt de bloquer des bitcoins à l'aide d'un script, en mettant des contraintes sur leur dépense.

![](assets/23.png)

## ADRESSE STATIQUE

Dans le cadre des Silent Payments, désigne un identifiant unique qui permet de recevoir des paiements sans pour autant produire de réutilisation d'adresse, sans interaction et sans lien visible on-chain entre les différents paiements et l'adresse statique. Cette technique élimine le besoin de générer de nouvelles adresses de réception vierges pour chaque transaction, ce qui permet d'éviter les interactions habituelles dans Bitcoin où le destinataire doit fournir une nouvelle adresse au payeur. C'est un peu l'équivalent du code de paiement réutilisable dans le cadre du BIP47.

Cette adresse est composée de deux clés publiques : $B_{\text{scan}}$ pour le scan et $B_{\text{spend}}$ pour la dépense, concaténées pour former l'adresse statique $B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$. Le destinataire publie cette adresse, permettant aux expéditeurs de dériver des adresses de paiement uniques sans interaction supplémentaire avec le destinataire. Pour gérer plusieurs sources de paiements distinctes, on peut ajouter un label à $B_{\text{spend}}$, créant ainsi plusieurs adresses statiques labellisées à partir de $B_1$, $B_2$, etc.). Cela permet de ségréguer les paiements tout en utilisant une seule adresse de base, réduisant ainsi la charge de travail pour le scan de la blockchain. Toutefois, toutes les adresses statiques d'une entité peuvent être facilement associées en raison de l'utilisation commune de $B_{\text{scan}}$.

> ► *Pour plus d'informations, voir la définition de **[SILENT PAYMENTS](./S.md#silent-payment)**.*

## AGORISME

Philosophie politique fondée par Samuel Edward Konkin III dans les années 1980. Elle est une extension du libertarianisme, mettant en avant une action directe pour s'extraire des jougs de l'autorité étatique par le biais de la contre-économie, une pratique économique qui se déroule en dehors des cadres régulés par le gouvernement. L'idéologie agoriste repose sur le jusnaturalisme, qui affirme que les droits naturels des individus sont supérieurs aux lois imposées par l'État. Cela inclut la primauté de la propriété privée, le respect de l'intégrité physique, et la liberté de contracter. Les agoristes rejettent toute forme de participation politique traditionnelle comme le vote, qu'ils considèrent comme une validation de l'autorité coercitive de l'État. Ils aspirent à une société où les échanges économiques et sociaux se déroulent librement dans un marché ouvert, appelé l'Agora, visant ainsi à une révolution pacifique pour éroder progressivement le pouvoir de l'État. Leur emblème est d’ailleurs « A3 », pour « Agora, Anarchie, Action ». Le principe de l'agorisme est décrit dans le *Manifeste néo-Libertarien* paru en 1980. Ce papier est établi sur le *Manifeste Libertarien* de Murray Rothbard, mais il va encore plus loin. Beaucoup de bitcoiners se réclament de l'agorisme et pensent que Bitcoin en est l'outil parfait.

## AJUSTEMENT DE LA DIFFICULTE

L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin. Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L’ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d’un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. La formule exécutée par les nœuds pour calculer la nouvelle cible est la suivante : 
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Où :
* $N$ : La nouvelle cible ;
* $A$ : L'ancienne cible des 2016 derniers blocs ;
* $T$ : Le temps total réel des 2016 derniers blocs en secondes ;
* $1,209,600$ : Le temps cible en secondes pour produire 2016 blocs avec un intervalle de 10 minutes entre chacun.

> ► *En français, on parle également parfois de « reciblage » pour évoquer l'ajustement. En anglais, on parle de « Difficulty Adjustment ».*

## ALGORITHME

Suite finie et non ambiguë d'instructions permettant de réaliser une tâche. Dans le cadre de l'informatique, il s'agit d'un processus écrit dans un langage de programmation qui indique à un ordinateur comment effectuer une mission.

## ALTCOIN

Désigne toute cryptomonnaie autre que le bitcoin (BTC). Le terme « altcoin » est la contraction de « alternative » et de « coin » (pièce alternative). Certains bitcoiners maximalistes parlent également de « shitcoins » pour désigner les altcoins.

## ANALYSE DE CHAINE

Pratique qui regroupe toutes les méthodes permettant de tracer les flux de bitcoins sur la blockchain. De façon générale, l’analyse de chaîne s’appuie sur l’observation de caractéristiques sur des échantillons de transactions antérieures. Elle consiste ensuite à repérer ces mêmes caractéristiques sur une transaction que l’on souhaite analyser, et à en déduire des interprétations vraisemblables. Cette méthode de résolution de problème à partir d’une approche pratique, pour trouver une solution suffisamment bonne, c’est ce que l’on appelle une heuristique. Pour vulgariser, l’analyse de chaîne se fait en deux grandes étapes : 
* Le repérage de caractéristiques connues ;
* La déduction d’hypothèses.

Un des objectifs de l’analyse de chaîne consiste à regrouper diverses activités sur Bitcoin en vue de déterminer l'unicité de l'utilisateur les ayant effectuées. Par la suite, il sera possible de tenter de rattacher ce faisceau d'activités à une identité réelle grâce à un point d'entrée. Il est important de comprendre que l'analyse de chaîne n'est pas une science exacte. Elle repose sur des heuristiques dérivées d'observations antérieures ou d’interprétations logiques. Ces règles permettent d'obtenir des résultats assez fiables, mais jamais d'une précision absolue. En d'autres termes, l'analyse de chaîne implique toujours une dimension de vraisemblabilité dans les conclusions émises. Par exemple, on pourra estimer avec plus ou moins de certitude que deux adresses appartiennent à une même entité, mais une certitude totale sera toujours hors de portée. Tout l’objectif de l'analyse de chaîne réside précisément dans l'agrégation de diverses heuristiques en vue de minimiser le risque d'erreur. Il s'agit en quelque sorte d'une accumulation de preuves qui nous permet de nous approcher davantage de la réalité. Ces fameuses heuristiques peuvent être regroupées en différentes catégories : 
* Les patterns de transaction (ou modèles de transaction) ;
* Les heuristiques internes à la transaction ;
* Les heuristiques externes à la transaction. 

Notons que les deux premières heuristiques sur Bitcoin ont été formulées par Satoshi Nakamoto lui-même. Il les expose dans la partie 10 du White Paper (livre blanc). Il est intéressant d’observer que ces deux heuristiques conservent toujours une prééminence dans l’analyse de chaîne aujourd’hui. Ce sont la CIOH (*Common Input Ownership Heuristic*) et la réutilisation d’adresse.

## ANCESTOR MINING

Autre nom parfois donné à CPFP (*Child-Pay-For-Parent*). Le minage des ancêtres est le principe selon lequel un mineur ne choisit pas une transaction uniquement sur la base de ses propres frais de transaction, mais prend aussi en compte les frais des transactions ascendantes.

> ► *Pour plus d'informations, voir la définition de [**CPFP (CHILD PAY FOR PARENT)**](./C.md#cpfp-child-pay-for-parent).*

## ANCHOR OUTPUTS

Proposition qui vise à améliorer la gestion des frais de transaction dans le cadre des canaux Lightning. À chaque changement d'état dans un canal Lightning, les parties prenantes créent et signent une nouvelle transaction d'engagement qui reflète la nouvelle répartition des fonds au sein du canal. Le problème de ce mécanisme réside dans la détermination des frais de transaction au moment de sa création. En effet, les frais de transaction sur le réseau Bitcoin sont sujets à de fortes fluctuations, tant à la hausse qu'à la baisse. Si les frais fixés pour la dernière transaction d'engagement sont insuffisants au moment de la fermeture unilatérale du canal, non seulement la transaction prendra un temps considérable à se confirmer, mais les mécanismes de verrouillage temporel (timelocks) pourraient également permettre un vol des fonds. Les anchor outputs permettent de réserver une petite partie des fonds dans une transaction d'engagement pour couvrir les frais futurs. En cas de congestion du réseau et d'augmentation des frais, les anchor outputs permettent de modifier les frais de transaction après la création de la transaction d'engagement, garantissant ainsi une fermeture suffisamment rapide du canal Lightning.

## ANCHORS.DAT

Fichier utilisé dans le client Bitcoin Core pour stocker les adresses IP des nœuds sortants auxquels un client était connecté avant d'être éteint. Anchors.dat est donc créé à chaque fois que le nœud est arrêté et supprimé lorsqu'il est relancé. Les nœuds dont les adresses IP sont contenues dans ce fichier sont utilisés pour aider à établir rapidement des connexions lors du redémarrage du nœud.

## ANCRAGE BILATÉRAL

Mécanisme qui permet d'établir une connexion entre le système principal de Bitcoin et une sidechain (ou une drivechain), c'est-à-dire une chaîne latérale. L'ancrage bilatéral assure une corrélation de valeur fixe entre les bitcoins sur la blockchain principale et les actifs correspondants sur la sidechain, permettant ainsi de déplacer des bitcoins entre les deux chaînes. Pour ce faire, les bitcoins sont temporairement verrouillés sur la blockchain principale et un montant équivalent d'actifs est émis sur la sidechain. Cela permet de profiter des avantages spécifiques de la sidechain, comme des transactions plus rapides ou des fonctionnalités de confidentialité améliorées, tout en maintenant la valeur des bitcoins utilisés. Lorsque les utilisateurs souhaitent revenir à la blockchain Bitcoin, le processus s'inverse : les actifs sur la sidechain sont détruits et les bitcoins correspondants sont déverrouillés. Il existe de nombreux mécanismes d'ancrages bilatéraux différents qui peuvent reposer sur :
* Un tiers de confiance unique ;
* Une fédération d'entités ;
* Les mineurs de la chaîne principale (drivechain).

> ► *En anglais, on parle d'un « two-way peg » ou « 2WP ».*

## ANONSETS (ANONYMITY SETS)

Les anonsets servent d'indicateurs pour évaluer le degré de confidentialité d'un UTXO particulier. Plus spécifiquement, ils mesurent le nombre d'UTXOs indistinguables au sein de l'ensemble qui inclut la pièce en étudiée. Puisqu'il faut disposer d'un groupe d'UTXOs identiques, les anonsets sont généralement calculés au sein d'un cycle de coinjoins. Ils permettent, le cas échéant, de juger de la qualité des coinjoins. Un anonset de grande taille signifie un niveau d'anonymat accru, car il devient difficile de distinguer un UTXO spécifique au sein de l'ensemble. Deux types d'anonsets existent :
* L'ensemble d'anonymat prospectif ;
* L'ensemble d'anonymat rétrospectif.

Le premier indique la taille du groupe parmi lequel se cache l'UTXO étudié en sortie, sachant l'UTXO en entrée. Cet indicateur permet de mesurer la résistance de la confidentialité de la pièce face à une analyse passé vers présent (entrée vers sortie). En anglais, le nom de cet indicateur est « *forward anonset* », ou « *forward-looking metrics* ».

![](assets/39.png)

Le second indique le nombre de sources possibles pour une pièce donnée, sachant l'UTXO en sortie. Cet indicateur permet de mesurer la résistance de la confidentialité de la pièce face à une analyse présent vers passé (sortie vers entrée). En anglais, le nom de cet indicateur est « *backward anonset* », ou « *backward-looking metrics* ».

![](assets/40.png)

> ► *En français, il est globalement admis d'utiliser le terme « anonset ». On pourrait toutefois le traduire par « ensemble d'anonymat » ou « potentiel d'anonymat ». En anglais et en français, on parle également parfois de « score » pour évoquer les anonsets (score prospectif et score rétrospectif). Pour plus d'informations, voir la définition [**COINJOIN**](./C.md#coinjoin).*

## ANTI MONEY LAUNDERING (AML)

Désigne l'ensemble des procédures, lois et régulations destinées à prévenir le blanchiment d'argent. Ces règles obligent les institutions financières comme les plateformes d'échange de bitcoins à surveiller activement les transactions de leurs clients, à effectuer des vérifications d'identité, à tenir des registres et à signaler les activités suspectes aux autorités.

## ANYPREVOUT (APO)

Nom donné au BIP118 qui propose d'ajouter deux nouveaux SigHash Flag modificateurs, nommés `SIGHASH_ANYPREVOUT` et `SIGHASH_ANYPREVOUTANYSCRIPT`. Le terme « *AnyPrevOut* » provient de la contraction de « *Any Previous Output* » que l'on pourrait traduire en français par « toute sortie précédente ».

> ► *Pour plus d'informations, voir la définition de **[SIGHASH_ANYPREVOUT](./S.md#sighash_anyprevout)**.*

## AOPP

Sigle de « *Address Ownership Proof Protocol* ». C'est un protocole controversé, conçu pour prouver automatiquement la propriété d'adresses Bitcoin. Ce mécanisme permet aux utilisateurs de démontrer qu'ils contrôlent une adresse spécifique, directement à travers leur logiciel de portefeuille compatible. Initialement, l'AOPP a été créé pour simplifier la vérification de possession d'adresses, une exigence légale pour les clients désirant transférer leurs bitcoins hors des plateformes d'échange dans certaines juridictions, telles que la Suisse.

Néanmoins, ce protocole a été l'objet de critiques importantes au sein de la communauté Bitcoin, car il pourrait établir un précédent où les utilisateurs devraient demander l'autorisation pour exercer leur droit de possession sur leurs propres fonds (self-custody). Face à ces critiques, de nombreux logiciels de portefeuille ont choisi de ne pas adopter ce protocole.

## API

Sigle de « *Application Programming Interface* ». Dans le contexte général de l'informatique, une API est un ensemble de règles et de spécifications que les logiciels peuvent suivre pour communiquer entre eux. Elles permettent aux développeurs d'accéder à des fonctionnalités ou à des données d'une application, d'un système d'exploitation ou d'un autre service pour leur propre logiciel.

> ► *En français, on peut le traduire par « interface de programmation d'applications » ou directement « interface de programmation ».*

## ARBITRAGE

Pratique consistant à exploiter les différences de prix du BTC (ou de tout autre actif) entre différentes plateformes d'échange pour réaliser un profit. L'arbitrage implique d'acheter du bitcoin sur une plateforme où le prix est relativement bas et de le vendre simultanément sur une autre plateforme où le prix est plus élevé. Les écarts de prix peuvent survenir en raison de différences dans la liquidité, la demande, les volumes de transaction et les délais de transfert entre les plateformes d'échange. L'arbitrage contribue à équilibrer les prix sur différentes plateformes.

## ARBRE DE MERKLE

Un Arbre de Merkle est un accumulateur cryptographique. C’est une méthode pour justifier l’appartenance d’une information donnée à un ensemble plus grand. C'est une structure de données qui facilite la vérification d’informations dans un format compact. Dans le système Bitcoin, les arbres de Merkle sont utilisés pour regrouper et condenser les transactions d'un bloc en un unique hachage, appelé la racine de Merkle (ou « *Root Hash* »). Chaque transaction est hachée, puis les hachages adjacents sont hachés ensemble de façon hiérarchique jusqu'à ce que la racine de Merkle soit obtenue.

![](assets/1.png)

Cette structure permet de vérifier rapidement si une transaction spécifique est incluse dans un bloc donné sans avoir à analyser l'ensemble des transactions. Par exemple, si je dispose seulement de la racine de Merkle et que je souhaite vérifier que la `TX 7` fait bien partie de l'arbre, j'aurai uniquement besoin des preuves suivantes :
* `TX 7` ;
* `HASH 8` ;
* `HASH 5-6` ;
* `HASH 1-2-3-4`.
Grâce à ces quelques informations, je suis en capacité de calculer les nœuds intermédiaires jusqu'à la racine de Merkle.

![](assets/2.png)

Les arbres de Merkle sont notamment utilisés pour les nœuds légers (dits « SPV ») qui ne conservent que les entêtes de blocs, mais pas les transactions. On retrouve également cette structure dans le protocole UTREEXO, un protocole permettant de condenser l'UTXO set des nœuds, et dans le MAST Taproot.

> ► *L'arbre de Merkle porte le nom de Ralph Merkle, un cryptographe qui a conçu cette structure en 1979. Un arbre de Merkle peut également être nommé « arbre de hachage ». En anglais, on dit « Merkle Tree » ou « Hash Tree ».*

## ARK

Nouveau protocole de seconde couche dévoilé par Burak en mai 2023. Comme le Lightning Network, Ark est un système se déployant par-dessus la chaîne principale de Bitcoin. Il permettrait de faire des paiements en bitcoins en dehors de la chaîne de manière rapide, anonyme et à bas frais. Par rapport à Lightning, Ark ne nécessite pas d’avoir des liquidités entrantes pour recevoir des paiements, ce qui permet d’améliorer considérablement l’expérience utilisateur. De plus, il procure une confidentialité se rapprochant des transactions coinjoins, alors que Lightning est un assez mauvais modèle pour protéger sa vie privée. Enfin, Ark pourrait également être non interactif si des covenants sont ajoutés à Bitcoin. Burak critique souvent la capacité de Lightning à passer à l’échelle en raison de sa dépendance à la chaîne principale et suggère qu'Ark pourrait théoriquement intégrer toute la population mondiale en self-custody. Même si Ark peut être vu comme un protocole concurrent au Lightning Network, les deux peuvent en réalité coexister. Ils pourraient même être plutôt complémentaires. Notons toutefois que pour le moment, Ark n’est qu’une simple idée. Burak n’a pas encore dévoilé le code de son invention.

## ASCII

Sigle de « *American Standard Code for Information Interchange* ». C'est un système de codage de caractères pour les ordinateurs. Le standard ASCII utilise 7 bits pour représenter 128 caractères différents : des lettres majuscules et minuscules de l'alphabet latin, des chiffres, des symboles de ponctuation, et des commandes de contrôle, comme le saut de ligne ou la tabulation.

## ASIC

Un ASIC est un composant électronique conçu pour exécuter une fonction spécifique avec une efficacité optimale. Dans le contexte du minage de Bitcoin, les ASIC sont des circuits intégrés spécialisés qui effectuent des opérations de hachage à haute vitesse et faible consommation d'énergie. Ils sont spécialisés dans l'exécution de la fonction de hachage `SHA256` utilisée dans le mécanisme de la preuve de travail. L'ASIC est initialement le nom de la puce. Par extension, l'acronyme « ASIC » vise souvent à désigner également la machine qui héberge cette puce. Ainsi, les ordinateurs spécialisés dans le minage de Bitcoin sont parfois appelés des « ASIC », ou bien des « mineurs ». Les ASIC ont progressivement remplacé les autres méthodes de minage, telles que l'utilisation de processeurs (CPU) et de cartes graphiques (GPU), en raison de leur efficacité énergétique supérieure et de leur taux de hachage bien plus élevé.

>*L'acronyme « ASIC » désigne en anglais « Application-Specific Integrated Circuit ». En français, ce terme peut être traduit par « Circuit intégré spécifique à une application ».*

## ASICBOOST

Méthode d'optimisation algorithmique inventée en 2016, conçue pour augmenter l'efficacité du minage de Bitcoin d'environ 20 % en réduisant la quantité de calculs nécessaires pour chaque tentative de hachage de l'entête. Cette technique exploite une particularité de la fonction de hachage SHA256, utilisée pour le minage, qui divise les données en blocs avant de les traiter. AsicBoost conserve l'un de ces blocs inchangé à travers plusieurs tentatives de hachage, ce qui permet au mineur de ne réaliser qu'une partie du travail pour ce bloc sur plusieurs tentatives. Ce partage de données permet une réutilisation des résultats de calculs précédents, ce qui diminue ainsi le nombre total de calculs nécessaires pour trouver un hachage valide.

AsicBoost peut être utilisé sous deux formes : Overt ASICBoost et Covert ASICBoost. La forme Overt AsicBoost est visible par tous, car elle implique d'utiliser le champ `nVersion` du bloc comme un nonce, et de ne pas modifier le vrai `Nonce`. La forme Covert cherche à masquer ces modifications en utilisant les arbres de Merkle. En revanche, cette seconde méthode n'est plus efficace depuis SegWit à cause du second arbre de Merkle qui multiplie le nombre de calculs nécessaires pour l'utiliser.

Pour résumer, AsicBoost permet de ne pas avoir à effectuer un vrai SHA256 complet pour toutes les tentatives de hachage, car une partie du résultat reste inchangée, ce qui permet d'accélérer le travail des mineurs.

## ASMAP

Outil inventé par Gleb Naumenko et utilisé par Bitcoin Core pour améliorer la sécurité et la topologie du réseau Bitcoin en diversifiant les connexions entre les nœuds. Il s'agit d'une carte d'adressage IP vers les numéros de systèmes autonomes (ASN), permettant une meilleure répartition des connexions sortantes en fonction de l'ASN plutôt que des préfixes IP. Cela aide à prévenir les attaques Eclipse (notamment l'attaque Erebus) en rendant plus difficile pour un attaquant de simuler plusieurs nœuds.

## ASSUME UTXO

Paramètre de configuration dans le client majoritaire Bitcoin Core qui permet à un nœud qui vient d'être initialisé (mais qui n'a pas encore fait l'IBD) de reporter la vérification des transactions et de l'UTXO set avant un snapshot donné. Le concept repose sur l'utilisation d'un UTXO set (liste de tous les UTXOs existants à un moment donné) fourni par Core et présumé exact, ce qui permet au nœud d'être synchronisé très rapidement sur la chaîne avec le plus de travail accumulé. Puisque le nœud saute la longue étape de l'IBD, il est très rapidement fonctionnel pour son utilisateur. Assume UTXO divise la synchronisation (IBD) en deux parties : 
* Tout d'abord, le nœud réalise le Header First Sync (vérification des en-têtes seulement) et il considère comme valide l'UTXO set qui lui est fourni par Core ;
* Puis, une fois qu'il est fonctionnel, le nœud va vérifier l'historique complet des blocs en arrière-plan, en actualisant un nouvel UTXO set qu'il aura vérifié lui-même. Si ce dernier ne correspond pas à l'UTXO set fourni par Core, il fournira un message d'erreur.

Assume UTXO permet donc d'accélérer la préparation d'un nouveau nœud Bitcoin en reportant le processus de vérification des transactions et de l'UTXO set grâce à un snapshot actualisé fourni dans Core.

## ASSUME VALID

Paramètre de configuration dans le client majoritaire Bitcoin Core qui permet à un nœud qui vient d'être initialisé (mais qui n'a pas encore fait l'IBD) de sauter la vérification des signatures pour toutes les transactions incluses dans les blocs antérieurs à un certain bloc donné. Ce fameux bloc est défini par l'empreinte de son en-tête, c'est-à-dire son hash. Le bloc choisi est renouvelé lors de chaque nouvelle version de Bitcoin Core. À son initialisation, si le nœud a activé ce paramètre, il va donc vérifier la chaîne d'en-têtes de blocs pour trouver la branche avec le plus de travail accumulé. Si le nœud détecte le hash fourni par Core dans la branche qu'il a retenue, il omettra la vérification des signatures pour les blocs antérieurs. Dans le cas contraire, le nœud procédera à une synchronisation traditionnelle (IBD) pour tout vérifier par lui-même.

L'objectif d'Assume Valid est d'accélérer le processus de synchronisation initiale d'un nœud sans compromettre la sécurité, en supposant que la majorité du réseau ait déjà validé ces transactions dans le passé. Le seul vrai compromis pour le nœud est qu'en cas de vol antérieur de bitcoins, il ne sera pas averti. Cependant, il peut toujours s'assurer de l'exactitude de la quantité de bitcoins émis. Les nœuds poursuivent la vérification des signatures de transactions postérieures au bloc Assume Valid. Cette approche repose sur l'hypothèse que si une transaction est acceptée par le réseau depuis assez longtemps sans contestation, il est improbable qu'elle soit frauduleuse.

## ATH (ALL-TIME HIGH)

Désigne le niveau le plus élevé jamais atteint par l'élément étudié. Souvent, l'ATH désigne le plus haut niveau de prix du bitcoin en comparaison avec une monnaie étatique sur une période donnée.

## ATLC

Sigle de « *Anchor Timelock Contracts* ». C'est un paiement conditionnel utilisé dans le cadre du protocole Ark pour fournir un calendrier de paiement atomique à un hub, grâce à des connecteurs permettant de former ce que l'on appelle un « txlock ». L'objectif d'un ATLC est sensiblement le même que celui d'un HTLC sur Lightning.

> ► *Pour plus d'informations, voir la définition de [**ARK**](./A.md#ark).*

## ATOMIC SWAP

Technologie permettant un échange de cryptomonnaies directement entre deux parties, sans besoin de confiance et sans nécessiter d'intermédiaire. Ces échanges sont dits « atomiques » car ils ne peuvent donner que deux résultats :
* Soit l'échange réussi et les deux participants se sont effectivement échangé leurs cryptomonnaies ;
* Soit l'échange échoue et les deux participants repartent avec leurs cryptomonnaies de départ.

Les Atomic Swaps peuvent s'effectuer soit avec une même cryptomonnaie, dans ce cas, on parle également de « *coinswap* », soit entre des cryptomonnaies différentes. Historiquement, ils s'appuyaient sur des « *Hash Time-Locked Contracts* » (HTLC), un système de verrouillage temporel qui garantit la complétude ou l'annulation totale de l'échange, préservant ainsi l'intégrité des fonds des parties impliquées. Cette méthode exigeait des protocoles capables de gérer à la fois les scripts et les timelocks. Toutefois, ces dernières années, la tendance s'est orientée vers l'utilisation des *Adaptor Signatures*. Cette seconde approche présente l'avantage de se passer de scripts, ce qui réduit ainsi les coûts opérationnels. Son autre atout majeur réside dans le fait qu'elle n'exige pas l'emploi d'un hachage identique pour les deux volets de la transaction, ce qui permet d'éviter de révéler un lien entre elles.

## ATTAQUE DES 51 POUR CENT

Scénario hypothétique sur le système Bitcoin où un acteur malveillant contrôle plus de 50 % de la puissance de calcul totale du minage (hashrate). Avec une telle dominance, l'attaquant peut manipuler le processus de consensus, permettant des actions malveillantes telles que la double dépense, où les mêmes bitcoins sont dépensés une première fois sur une chaîne finalement rendue désuète, puis une seconde fois sur la chaîne valide. Une autre finalité d'une attaque des 51 % est la censure des transactions. Cependant, réaliser une attaque des 51 % nécessite des ressources financières, humaines, énergétiques et techniques considérables, et rend l'acteur malveillant susceptible d'être découvert avant que l'attaque n'ait lieu. Bien que théoriquement possible, une attaque des 51 % sur Bitcoin est considérée comme très peu probable en raison de la décentralisation du minage et de la grande puissance de calcul actuellement déployée.

> ► *Cette attaque est également nommée « Attaque Goldfinger ».*

## AVG. ROUND DURATION

La durée moyenne de tour est un indicateur utilisé pour estimer le temps nécessaire à une pool de minage pour trouver un bloc, en fonction de la difficulté du réseau et du hashrate de la pool. Il est calculé en prenant le nombre de shares attendues pour trouver un bloc et en le divisant par le hashrate de la pool. Par exemple, si une pool de minage compte 200 mineurs, et que chacun génère en moyenne 4 shares par seconde, la puissance totale de calcul de la pool est de 800 shares par seconde :

```text
200 * 4 = 800
```

En supposant qu'il faille, en moyenne, produire 1 million de shares pour trouver un bloc valide, l'*Avg. Round Duration* de la pool sera de 1 250 secondes, soit environ 21 minutes :

```text
1 000 000 / 800 = 1 250
```

Concrètement, cela signifie qu'en moyenne, la pool de minage devrait trouver un bloc toutes les 21 minutes environ. Cet indicateur fluctue avec les variations du hashrate de la pool : une augmentation du hashrate réduit l'*Avg. Round Duration*, tandis qu'une diminution l'allonge. Il va également fluctuer à chaque évolution périodique de la cible de difficulté sur Bitcoin (tous les 2016 blocs). Cette mesure ne prend pas en compte les blocs trouvés par d'autres pools et se concentre uniquement sur la performance interne de la pool étudiée.

> ► *Pour plus d'informations, voir les définitions de **[SHARES](./S.md#shares)** et de **[LUCK](./L.md#luck)**.*
