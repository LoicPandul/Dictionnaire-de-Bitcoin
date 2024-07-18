## GAP LIMIT

Paramètre utilisé dans les logiciels de portefeuille Bitcoin pour déterminer le nombre maximal d'adresses consécutives non utilisées à générer avant de cesser la recherche de transactions supplémentaires. L'ajustement de ce paramètre est souvent nécessaire lors de la récupération d'un portefeuille pour garantir que toutes les transactions soient bien trouvées. Un Gap Limit insuffisant pourrait entraîner l'oubli de certaines transactions si des adresses étaient ignorées lors des phases de dérivation. Augmenter le Gap Limit permet au portefeuille de rechercher plus loin dans la séquence d'adresses, afin de récupérer toutes les transactions associées. 

En effet, une seule `xpub` peut théoriquement dériver plus de 4 milliards d'adresses de réception (adresses internes et externes). Toutefois, les logiciels de portefeuille ne peuvent pas toutes les dériver et vérifier leur utilisation sans engendrer un coût opérationnel énorme. Ainsi, ils procèdent par ordre d'index, car c'est normalement dans cet ordre que tous les logiciels de portefeuille génèrent les adresses. Le logiciel enregistre chaque adresse utilisée avant de passer à la suivante, et il cesse sa recherche lorsqu'il rencontre un nombre d'adresses consécutivement vides. Ce nombre, c'est ce que l'on appelle le Gap Limit. 

Si, par exemple, le Gap Limit est fixé à `20`, et que l'adresse `m/84'/0'/0'/0/15/` est vide, le portefeuille dérivera les adresses jusqu'à `m/84'/0'/0'/0/34/`. Si cette plage d'adresses reste inutilisée, la recherche s'arrête là. Par conséquent, une transaction utilisant l'adresse `m/84'/0'/0'/0/40/` ne serait pas détectée dans cet exemple.

## GENÈSE (BLOC)

Le bloc de Genèse (en anglais « *Genesis block* ») est le premier bloc du système Bitcoin. Il incarne le lancement concret de Bitcoin. Le bloc de Genèse a été créé par le fondateur anonyme de Bitcoin, Satoshi Nakamoto, le 3 janvier 2009. Son hachage est :

```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Ce bloc contient seulement une transaction coinbase qui génère 50 bitcoins en récompense pour le mineur (dans ce cas, Satoshi Nakamoto lui-même). Ce bloc inclut un message incorporé dans la transaction coinbase :

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

Cette citation est une référence à un article du journal *The Times*. Le message est interprété comme une critique du système financier traditionnel et de ses dérives, ce qui a en partie motivé la création de Bitcoin en tant qu'alternative monétaire.

Puisqu’il incarne le tout premier bloc de la blockchain Bitcoin, le bloc de Genèse ne possède évidemment pas de champ contenant le hachage du bloc antérieur (car il n'y en pas). Par ailleurs, les 50 bitcoins générés en récompense dans ce bloc ne sont pas dépensables au niveau protocolaire.

## GETWORK

Ancien protocole de minage pour Bitcoin créé en 2010 par m0mchil. Getwork permettait aux mineurs de recevoir des données de travail de la part d'un nœud complet. Il était établi sur des requêtes RPC permettant d'obtenir des entêtes de blocs sur lesquels travailler pour trouver une preuve de travail valide. Getwork était optimisé pour le minage par GPU. Ce fut le premier logiciel open source conçu pour optimiser la communication entre les nœuds et les mineurs à une époque où quelques acteurs gardaient ces logiciels privés. Getwork a été progressivement remplacé par Stratum, plus efficace, notamment pour les ASICs, et moins gourmand en bande passante.

## GIT

Système de contrôle de version distribué conçu pour gérer tout type de projet logiciel avec efficacité. Il permet aux développeurs de suivre les modifications apportées au code source d'un projet au fil du temps, de revenir à des états antérieurs, de gérer des branches et de fusionner des modifications. Git facilite la collaboration entre les développeurs en permettant à plusieurs personnes de travailler sur le même projet simultanément, sans risque de conflit dans les fichiers. Chaque développeur travaille localement et peut ensuite synchroniser ses modifications avec le dépôt central. Créé en 2005 par Linus Torvalds, Git est devenu de fait le standard pour le contrôle de version dans l'industrie du logiciel. Les développements des implémentations de nœud Bitcoin, dont Bitcoin Core, sont gérées avec Git.

![](assets/47.png)

## GITHUB

Plateforme de gestion et d'hébergement de code source qui facilite la collaboration entre développeurs. Comme son nom l'indique, GitHub est établi sur le système de contrôle de version Git. Cette plateforme permet donc de suivre les changements de code, de gérer les versions et d'encourager la collaboration grâce à des outils comme les pull requests et les issues. GitHub est devenu un outil incontournable pour les développeurs, notamment dans la communauté Bitcoin où la majorité des projets, y compris Bitcoin Core, l'implémentation principale du protocole, y sont hébergés. En 2018, Microsoft a acquis GitHub pour 7,5 milliards de dollars.

![](assets/46.png)

## GITLAB

Plateforme de gestion et d'hébergement de code source qui facilite la collaboration entre développeurs. GitLab est la principale alternative à GitHub. La plateforme est assez similaire, mais elle offre également la possibilité d'être autohébergée. Comme son nom l'indique, GitLab est établi sur le système de contrôle de version Git. Cette plateforme permet donc de suivre les changements de code, de gérer les versions et d'encourager la collaboration grâce à des outils comme les pull requests et les issues. Certains projets liés à Bitcoin comme Samourai Wallet, Whirlpool ou encore RoninDojo utilisent GitLab.

## GNPA (PRNG)

Sigle de « Générateur de nombre pseudo-aléatoire ». Les GNPA sont une catégorie d'algorithmes utilisés pour générer des séquences de nombres approximativement aléatoires, à partir d'un état initial appelé graine (seed). En cryptographie, le GNPA est utilisé pour produire des clés, des vecteurs d'initialisation et d'autres éléments nécessitants de l'aléatoire. Un bon GNPA doit avoir des propriétés telles que l'uniformité des sorties, l'imprévisibilité et la résistance aux attaques prédictives. Contrairement aux générateurs de nombres véritablement aléatoires, les GNPA sont déterministes et reproduisibles. Sur Bitcoin, les GNPA peuvent être utilisés sur les logiciels de gestion de portefeuille ou les hardware wallets, afin de générer la phrase de récupération qui est à la base des portefeuilles déterministes et hiérarchiques.

## GNU

Projet initié en 1983 par Richard Stallman pour créer un système d'exploitation libre, compatible avec Unix. Le projet a développé de nombreux logiciels libres qui peuvent être utilisés comme un système d'exploitation ou en complément d'un autre système d'exploitation. GNU est à la base du mouvement du logiciel libre, largement repris dans la communauté Bitcoin. Combiné avec le noyau Linux, il forme les systèmes d'exploitation GNU/Linux.

> ► *Le nom de « GNU » est un acronyme récursif signifiant « GNU's Not Unix », que l'on peut traduire en français « GNU n'est pas Unix ».*

## GOLDFINGER (ATTAQUE)

Scénario hypothétique sur le système Bitcoin où un acteur malveillant contrôle plus de 50 % de la puissance de calcul totale du minage (*hashrate*). Avec une telle dominance, l'attaquant peut manipuler le processus de consensus, permettant des actions malveillantes telles que la double dépense, où les mêmes bitcoins sont dépensés une première fois sur une chaîne finalement rendue désuète, puis une seconde fois sur la chaîne valide. Une autre finalité d'une attaque Goldfinger est la censure des transactions. Cependant, réaliser une attaque de ce type nécessite des ressources financières, humaines, énergétiques et techniques considérables, et rend l'acteur malveillant susceptible d'être découvert avant que l'attaque n'ait lieu. Bien que théoriquement possible, une attaque Goldfinger sur Bitcoin est considérée comme très peu probable en raison de la décentralisation du minage et de la grande puissance de calcul actuellement déployée.

> ► *Cette attaque est également nommée « Attaque des 51 % ».*

## GOSSIP

Dans le cadre de Lightning, le gossip est un protocole de communication entre les nœuds pour partager les informations sur l'état actuel et la topologie du réseau. Le protocole de gossip permet aux nœuds de connaître l'état dynamique des canaux de paiement et des autres nœuds, afin de faciliter le routage des transactions à travers le réseau sans nécessiter de connexions directes entre tous les nœuds.

> ► *En français, on pourrait traduire « gossip protocol » par « protocole de bavardage ».*

## GPL

Sigle de « *GNU General Public License* ». C'est une série de licences de logiciel libre initialement créée par la Free Software Foundation. Elle garantit aux utilisateurs la liberté d'utiliser, de modifier et de distribuer le logiciel. La GPL exige toutefois que tout logiciel dérivé ou modifié soit également distribué sous la même licence, ce qui permet d'assurer que les libertés initiales sont préservées dans toutes les versions du logiciel. La GPL est souvent utilisée pour les projets open source et on la retrouve parfois sur certains projets liés à Bitcoin. Toutefois, la licence initiale du client Bitcoin de Satoshi Nakamoto était une MIT X11. C'est d'ailleurs toujours le cas pour Bitcoin Core.

## GRAINE (SEED)

Dans le cadre spécifique d'un portefeuille déterministe hiérarchique Bitcoin, une graine (ou « seed » en anglais) est une information de 512 bits issue d'un aléa. Elle permet de générer de manière déterministe et hiérarchique un ensemble de clés privées, et leurs clés publiques correspondantes, pour un portefeuille Bitcoin. La graine est souvent confondue avec la phrase de récupération en elle-même. Pourtant, c'est une information différente. La graine est obtenue en appliquant la fonction `PBKDF2` sur la phrase mnémonique et sur l’éventuelle passphrase.

La graine a été inventée avec le BIP32 qui définit les bases du portefeuille déterministe hiérarchique. Dans ce standard, la graine mesurait 128 bits. Cela permet de dériver toutes les clés d'un portefeuille depuis une information unique, contrairement aux portefeuilles JBOK (*Just a Bunch Of Keys*) qui nécessitent de réaliser de nouvelles sauvegardes pour toute clé générée. Le BIP39 est par la suite venu proposer un encodage de cette graine, afin de simplifier sa lecture par l'humain. Cet encodage se fait sous la forme d'une phrase, que l'on nomme généralement phrase mnémonique ou phrase de récupération. Ce standard permet d'éviter les erreurs au niveau de la sauvegarde de la graine, notamment grâce à l'utilisation d'une somme de contrôle.

De manière plus générale, en cryptographie, une graine est un morceau de données aléatoires utilisé comme point de départ pour générer des clés cryptographiques, des chiffrements ou des séquences pseudo-aléatoires. La qualité et la sécurité de nombreux processus cryptographiques dépendent de la nature aléatoire et de la confidentialité de la graine.

> ► *La traduction anglaise de « graine » est « seed ». En français, beaucoup utilisent directement le mot anglais pour désigner la graine.*

## GREEN ADDRESS

Ancien logiciel de portefeuille Bitcoin racheté en juillet 2016 par Blockstream pour créer le logiciel actuel Green Wallet.

## GREEN ADDRESSES

Vieille proposition d'adresse Bitcoin dont les transactions qui y sont envoyées sont pré-approuvées par un tiers de confiance. Ce concept permet aux parties recevant des fonds via cette adresse de les considérer comme immédiatement fiables, sans attendre qu'elle soit incluse dans un bloc. Cela repose sur la confiance accordée au service qui contrôle la green address, car il garantit que les fonds envoyés n'ont pas été et ne seront pas double dépensés. Ce type de service était autrefois utilisé pour accélérer les transactions (zero-conf), mais il n'est plus utilisé de nos jours.

## GREEN WALLET

Logiciel de portefeuille Bitcoin disponible sur PC, Android et IOS développé par Blockstream depuis l'acquisition du logiciel Green Address en 2016. Il intègre plusieurs fonctionnalités comme une protection multisignatures avec une authentification à deux facteurs. Il est également compatible avec la plupart des hardware wallets. C'est un logiciel simple à prendre en main qui peut être utilisé par des débutants.

## GROS-BOUTISTE

Format de stockage de données dans les systèmes informatiques où les octets les plus significatifs (les « gros bouts ») sont placés en premier dans l'ordre des adresses. Cela signifie que dans une séquence avec plusieurs octets, l'octet ayant le plus grand poids (par exemple, les chiffres les plus à gauche en hexadécimale) est stocké en premier.

> ► *En anglais, on le traduit par « big-endian ».*

## GUI

Acronyme de « *Graphical User Interface* », ou « interface graphique utilisateur » en français. C'est une forme d'interface utilisateur qui permet d'interagir avec des logiciels à travers des éléments visuels interactifs (boutons, icônes, images, fenêtres...) et qui privilégie l'utilisation de dispositifs de pointage (la souris) plutôt que de commandes textuelles comme avec la CLI.

## GUISETTINGS.INI.BAK

Fichier dans Bitcoin Core utilisé pour stocker une sauvegarde des paramètres de l'interface graphique (GUI). Cette sauvegarde est créée lors de l'utilisation de l'option `-resetguisettings`, qui réinitialise les paramètres de la GUI à leurs valeurs par défaut. Ce fichier permet à l'utilisateur de restaurer ses configurations précédentes si nécessaire.
