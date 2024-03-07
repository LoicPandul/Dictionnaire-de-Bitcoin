## GENÈSE (BLOC)

Le bloc de genèse Bitcoin, également connu sous le nom de bloc Genesis ou bloc #0, est le premier bloc du système Bitcoin. Il incarne le lancement concret de Bitcoin. Le bloc de genèse a été créé par le fondateur anonyme de Bitcoin, Satoshi Nakamoto, le 3 janvier 2009. Son hash est [`000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f`](https://mempool.space/fr/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f). Ce bloc contient seulement une transaction coinbase qui génère 50 bitcoins en récompense pour le mineur (dans ce cas, Satoshi Nakamoto lui-même). Il est particulièrement significatif en raison de son message incorporé dans la transaction coinbase : `The Times 03/Jan/2009 Chancellor on brink of second bailout for banks`. Cette citation est une référence à un article du journal *The Times*. Le message est interprété comme une critique du système financier traditionnel et de ses dérives, ce qui a en partie motivé la création de Bitcoin en tant qu'alternative. Puisqu’il incarne le tout premier bloc de la blockchain Bitcoin, le bloc de genèse ne possède évidemment pas de champ contenant le hachage du bloc antérieur (car il n'y en pas). Par ailleurs, les 50 bitcoins générés en récompense dans ce bloc ne sont pas dépensables au niveau protocolaire.

## GETWORK

Ancien protocole de minage pour Bitcoin créé en 2010 par m0mchil. Getwork permettait aux mineurs de recevoir des données de travail de la part d'un nœud complet. Il était établi sur des requêtes RPC permettant d'obtenir des en-têtes de blocs à travailler pour trouver une preuve de travail valide. Getwork était optimisé pour le minage par GPU. Ce fut le premier logiciel open source conçu pour optimiser la communication entre les nœuds et les mineurs à une époque ou quelques acteurs gardait ces logiciels privés. Getwork a été progressivement remplacé par Stratum, plus efficace, notamment pour les ASIC, et moins gourmand en bande passante.

## GIT

Système de contrôle de version distribué conçu pour gérer tout type de projet logiciel avec efficacité. Il permet aux développeurs de suivre les modifications apportées au code source d'un projet au fil du temps, de revenir à des états antérieurs, de gérer des branches et de fusionner des modifications. Git facilite la collaboration entre les développeurs en permettant à plusieurs personnes de travailler sur le même projet simultanément, sans risque de conflit dans les fichiers. Chaque développeur travaille localement et peut ensuite synchroniser ses modifications avec le dépôt central. Créé en 2005 par Linus Torvalds, Git est devenu de fait le standard pour le contrôle de version dans l'industrie du logiciel. Les développements des implémentations de nœud Bitcoin, dont Bitcoin Core, sont gérées avec Git.

## GO (GOLANG)

Langage de programmation développé par Google, connu pour sa simplicité et son efficacité. Go est particulièrement adapté pour les applications cloud, les services web, et les systèmes distribués, grâce à sa gestion native de la concurrence et son modèle de programmation facile à comprendre.

## GOLDFINGER (ATTAQUE)

Voir la définition de **ATTAQUE DES 51%**.

## GOSSIP

Dans le cadre de Lightning, c'est un protocole de communication entre les nœuds pour partager les informations sur l'état actuel et la topologie du réseau. Le protocole de gossip permet aux nœuds de connaître l'état des canaux de paiement et des autres nœuds, facilitant le routage des transactions à travers le réseau sans nécessiter de connexions directes entre tous les nœuds. Le gossip assure une diffusion fiable et cohérente des données à tous le monde, malgré la nature dynamique du réseau.

## GRAINE (SEED)

Dans le cadre spécifique d'un portefeuille déterministe hiérarchique Bitcoin, une graine (ou « seed » en anglais) est une information de 512 bits issue d'un aléa. Elle permet de générer de manière déterministe et hiérarchique un ensemble de clés privées, et leurs clés publiques correspondantes, pour un portefeuille Bitcoin. La graine (seed) est souvent confondue avec la phrase de récupération en elle-même. Pourtant, c'est une information différente. La graine est obtenue en appliquant la fonction `PBKDF2` sur la phrase mnémonique et sur l’éventuelle passphrase. La graine a été inventée avec le BIP32 qui définit les bases du portefeuille déterministe hiérarchique. Dans ce standard, la graine mesurait 128 bits. Cela permet de dériver toutes les clés d'un portefeuille depuis une information unique, contrairement aux portefeuilles JBOK (Just a Bunch Of Keys) qui nécessitent de réaliser de nouvelles sauvegardes pour toute clé générée. Le BIP39 est par la suite venu proposer un encodage de cette graine, afin de simplifier sa lecture par l'humain. Cet encodage se fait sous la forme d'une phrase, que l'on nomme généralement phrase mnémonique ou phrase de récupération. Ce standard permet d'éviter les erreurs au niveau de la sauvegarde de la graine, notamment grâce à l'utilisation d'une somme de contrôle.

## GROS-BOUTISTE

Voir la définition de **BIG-ENDIAN**.

## GUI

Acronyme de « Graphical user interface », ou « interface graphique utilisateur » en français. C'est une forme d'interface utilisateur qui permet d'interagir avec des logiciels à travers des éléments visuels interactifs (boutons, icônes, images, fenêtres...) et qui privilégie l'utilisation de dispositifs de pointage (la souris) plutôt que de commandes textuelles comme avec la CLI.

## GUISETTINGS.INI.BAK

Fichier dans Bitcoin Core utilisé pour stocker une sauvegarde des paramètres de l'interface graphique (GUI). Cette sauvegarde est créée lors de l'utilisation de l'option `-resetguisettings`, qui réinitialise les paramètres de la GUI à leurs valeurs par défaut. Ce fichier permet à l'utilisateur de restaurer ses configurations précédentes si nécessaire.
