Le *Dictionnaire de Bitcoin* définit, en français, le vocabulaire de Bitcoin et de son écosystème. Je l'ai écrit pour que le lecteur qui croise un terme inconnu, dans un article, dans un BIP ou dans l'interface d'un logiciel, trouve une explication exacte qu'il peut suivre sans prérequis, et qu'il puisse remonter de définition en définition jusqu'à tout comprendre.

# POURQUOI CE DICTIONNAIRE

Bitcoin a son propre vocabulaire, et il s'élargit à chaque proposition d'amélioration, à chaque logiciel et à chaque protocole construit par-dessus. Les documents techniques emploient ces mots sans les expliquer, le plus souvent en anglais, alors que le lecteur qui débute ne les connaît pas encore. Ce livre rassemble ces termes au même endroit et donne pour chacun une définition complète, rédigée en français, que l'on peut lire sans ouvrir dix autres pages avant.

# CONTENU DU LIVRE

Le livre se compose des parties suivantes, dans cet ordre :
* Le dictionnaire technique : les termes de Bitcoin et des protocoles qui s'appuient sur lui, classés par ordre alphabétique, chacun avec une définition développée ;
* Entreprises, applications et logiciels : les entreprises, associations, logiciels, portefeuilles, matériels et services qui forment l'écosystème. Les mécanismes qu'ils mettent en œuvre sont définis dans le dictionnaire technique ;
* Personnes : les figures historiques de Bitcoin et du mouvement cypherpunk, ainsi que les personnalités principales de l'écosystème ;
* Chronologie : les événements majeurs de Bitcoin, du mouvement cypherpunk et de la cryptographie utile à Bitcoin, dans l'ordre où ils se sont produits. Chaque date est recoupée par au moins 2 sources ;
* BIP, puis BOLT et bLIP : les propositions d'amélioration de Bitcoin (BIP) et les documents du Lightning Network (BOLT et bLIP). Chaque entrée donne un résumé et un statut, et la définition développée vient sous le résumé lorsqu'elle existe.

# GUIDE DE LECTURE

Chaque entrée du dictionnaire technique suit le même format :
* Titre : le terme défini ;
* Catégorie : le domaine concerné (Cryptographie, Réseau, Portefeuille, etc.), accompagné de son pictogramme ;
* Terme anglais : l'équivalent anglais, précédé de « EN ». Lorsque le terme défini est lui-même anglais, c'est l'équivalent français qui apparaît, précédé de « FR » ;
* Définition : l'explication du concept ;
* Voir aussi : les termes associés à cette définition.

La première phrase de la définition dit ce qu'est le terme. Les paragraphes suivants expliquent comment il fonctionne, ce qu'il implique et d'où il vient, chacun s'appuyant sur le précédent. Une note en italique, en fin d'entrée, signale au besoin les synonymes ou les confusions fréquentes.

Les entrées des autres parties se lisent de la même façon. Une fiche de personne ou d'entreprise commence par le rôle de celle ou de celui qu'elle décrit. Une entrée de BIP, de BOLT ou de bLIP donne son identifiant, son statut, son titre d'origine en anglais et son résumé. Un événement de la chronologie porte sa date, un titre court et un court texte.

Pour une lecture efficace, suivez les termes de « Voir aussi » : ils relient les notions entre elles, et vous progressez ainsi de définition en définition.

# PRINCIPES DE RÉDACTION

Publier un dictionnaire implique de choisir les termes qu'il contient. J'en retiens un dès qu'il a un lien avec Bitcoin ou son écosystème, car l'ambition de ce livre est de couvrir le vocabulaire de Bitcoin de la façon la plus exhaustive possible, dans l'esprit des dictionnaires professionnels d'autres disciplines. Concrètement, la question est la suivante : « *Un débutant qui étudie Bitcoin pourrait-il croiser ce terme au cours de ses recherches et souhaiter en comprendre la signification ?* »

Si la réponse est oui, le terme entre, qu'il s'agisse d'une notion technique, d'un logiciel, d'un algorithme ou d'un protocole lié à Bitcoin, directement ou non, y compris les protocoles qui s'appuient sur lui (Lightning, RGB, Liquid, Ark, etc.). Les termes plus généraux d'informatique ou de cryptographie n'entrent que s'ils peuvent se rencontrer et si Bitcoin ne se comprend pas sans eux. Nostr, protocole distinct de Bitcoin, n'y figure pas.

Je ne me suis imposé aucune limite de longueur pour les définitions. Je préfère une définition longue et exacte à une définition courte et floue. Je vérifie les faits à la source (BIP, code de Bitcoin Core, documentation des projets), et je date ceux qui peuvent changer. Le dictionnaire décrit : il ne recommande aucun produit.

Pour les noms propres, la ligne est la suivante :
* Une personne a sa propre entrée lorsqu'elle compte parmi les figures historiques de Bitcoin ou du mouvement cypherpunk (Satoshi Nakamoto, Hal Finney ou Wei Dai, par exemple), ou parmi les personnalités principales de l'écosystème. Les autres sont citées, quand c'est utile, dans la définition de leur contribution ;
* Une organisation (entreprise, marque, projet, association) a sa propre entrée lorsque je la considère comme majeure, et la même règle s'applique aux logiciels et aux matériels. L'écosystème est difficile à découper, puisque les concepts sont portés par des logiciels, eux-mêmes associés à des entités, et connaître ces entités aide à comprendre l'ensemble ;
* La chronologie se limite aux événements majeurs. Un événement dont la date n'a pas pu être recoupée par 2 sources n'y figure pas.

# CONTRIBUTION

*Dictionnaire de Bitcoin* est un projet ouvert. Vous pouvez proposer :
* un nouveau terme, avec ou sans définition ;
* la correction d'une définition qui vous semble erronée ou imprécise ;
* la correction d'une faute d'orthographe ou d'une coquille ;
* toute autre modification.

Pour cela, ouvrez une pull request ou une issue sur le dépôt GitHub du projet (https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/). Le fichier README du dépôt détaille la marche à suivre, et la charte éditoriale fixe les conventions de rédaction. Les contributeurs sont cités dans le livre, sous leur pseudo GitHub sauf demande contraire.

Le texte est publié sous licence CC BY-NC-SA 4.0. Le dépôt contient la version la plus récente de l'ouvrage.

# AVERTISSEMENT

Ce dictionnaire a une vocation purement informative et pédagogique. Les informations qu'il contient ne constituent en aucun cas des conseils financiers, juridiques ou d'investissement, et je décline toute responsabilité quant à l'usage qui pourrait en être fait.

Bitcoin évolue vite, et malgré le soin apporté à la rédaction, certaines informations peuvent devenir obsolètes. Vérifiez-les auprès des sources officielles et de la documentation technique, et consultez la version en ligne la plus récente.
