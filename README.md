# Dictionnaire de Bitcoin
Tout le vocabulaire technique de Bitcoin et de son environnement.

## Description du projet
Cet ouvrage recense tous les termes techniques en rapport avec Bitcoin ou son environnement, ainsi que les définitions correspondantes. Rédigé par Loïc Morel, de Pandul, il est accessible gratuitement en version numérique sur GitHub, ou sous format PDF sur le site [https://www.pandul.fr/](https://www.pandul.fr/). Ce livre sera également vendu imprimé et broché sur Amazon à partir de fin 2024.

Je gagne une petite marge sur chaque exemplaire physique vendu via Amazon. Si vous trouvez ce projet utile, ou plus généralement, si vous appréciez mon travail de production de contenus pédagogiques, vous pouvez commander votre propre livre *Dictionnaire de Bitcoin* afin de me soutenir.

La première édition de l'ouvrage est prévue pour 2024. Si le projet intéresse et suscite de l'engagement, je publierai chaque année une nouvelle version actualisée du *Dictionnaire de Bitcoin*. Ces mises à jour comprendront les modifications proposées par la communauté de contributeurs et les termes nouvellement apparus au cours de l'année écoulée.

Pour ceux qui ne désirent pas acheter le livre sur Amazon mais souhaitent néanmoins soutenir le projet, il est possible de faire un don sur [+throbbingpond8B1](https://paynym.is/+throbbingpond8B1) (BIP47) ou à [loic@sats.pandul.fr](https://www.pandul.fr/) (adresse LN).

## Lire le *Dictionnaire de Bitcoin*
Vous pouvez découvrir gratuitement la version en ligne du *Dictionnaire de Bitcoin* dans le dossier [dictionnaire](./dictionnaire). Les définitions sont classées par ordre alphabétique et chaque fichier markdown correspond à une lettre.

Pour faciliter la navigation et vous aider à trouver rapidement les définitions, j'ai créé un sommaire détaillé de tous les termes inclus dans le *Dictionnaire de Bitcoin*. Chaque entrée du sommaire est liée à sa définition spécifique, ce qui vous permet d'accéder directement à l'information recherchée.

[Accéder au sommaire](./INDEX.md)

Une version PDF est également disponible au téléchargement à la racine de ce dépôt ou sur https://www.pandul.fr/. La branche `main` correspond à la version intermédiaire de travail, sur laquelle les Pull Request sont fusionnées progressivement. Vous pourrez retrouver une version imprimée et brochée du *Dictionnaire de Bitcoin* sur Amazon à partir de la fin de l'année 2024.

Sur ce dépôt, vous trouverez le dictionnaire décliné en trois formats différents, chacun contenant les mêmes définitions, afin de répondre aux préférences de chacun, que vous souhaitiez intégrer le dictionnaire à un site web ou simplement le télécharger pour un usage personnel. Les formats proposés sont les suivants :
- [Un fichier markdown unique rassemblant l'ensemble des définitions](/autres_formats/dictionnaire_complet/dictionnaire_complet.md) ;
- [Un dossier contenant un fichier markdown séparé pour chaque définition](/autres_formats/definitions_individuelles) ;
- [Un dossier de travail « dictionnaire » organisé de manière à regrouper les définitions dans des fichiers markdown par lettre de l'alphabet](/dictionnaire).

## Demandes de modification et contributions
*Dictionnaire de Bitcoin* est un projet ouvert. Vous êtes libre de proposer tout type de modification ou de correction, ce qui inclut notamment :
* La suggestion de nouveaux termes à ajouter (avec ou sans définition) ;
* La correction d'une définition qui vous semble erronée ou imprécise ;
* La correction d'une faute d'orthographe ou d'une coquille ;
* Toute autre suggestion de modification.

Pour contribuer, voici la marche à suivre : 
1. Créez votre fork du projet ;
2. Créez une nouvelle branche établie sur la branche `edit` ; 
3. Rédigez vos suggestions de modification directement sur votre branche ;
4. Proposez une Pull Request pour fusionner votre branche face à la branche `edit` du dépôt source.

Sur ce dépôt, vous trouverez le dictionnaire décliné en trois formats différents, chacun contenant les mêmes définitions, afin de répondre aux préférences de chacun. Les formats proposés sont les suivants :
- [Un fichier markdown unique rassemblant l'ensemble des définitions](/autres_formats/dictionnaire_complet/dictionnaire_complet.md) ;
- [Un dossier contenant un fichier markdown séparé pour chaque définition](/autres_formats/definitions_individuelles) ;
- [Un dossier de travail `/dictionnaire` organisé de manière à regrouper les définitions dans des fichiers markdown par lettre de l'alphabet](/dictionnaire).

**Les contributions doivent se faire uniquement sur le dossier de travail [/dictionnaire](/dictionnaire).** Un script python permet de mettre à jour automatiquement les autres formats.

Si vous ne vous sentez pas à l'aise avec l'utilisation de Git, ou si vous avez en tête une modification mineure à apporter (telle que l'ajout d'un terme ou la correction d'une petite erreur d'orthographe), vous pouvez également créer une issue sur GitHub plutôt qu'une PR.

Pour les changements d'envergure, comme la réalisation d'une traduction de l'ouvrage, je vous invite à me contacter directement. Mes coordonnées sont disponibles sur [https://www.pandul.fr/](https://www.pandul.fr/).

En contribuant, **votre pseudo GitHub sera mentionné tant dans la version en ligne que dans la version imprimée du dictionnaire**. Si vous préférez ne pas être cité, ou si vous souhaitez apparaître sous un autre nom que votre pseudo GitHub, veuillez le préciser explicitement dans votre issue ou votre PR.

Mon objectif pour ce projet de dictionnaire est de publier une nouvelle édition toutes les N années. Ainsi, les modifications apportées au document principal ne se refléteront pas immédiatement dans la version imprimée disponible sur Amazon.

Si vous le souhaitez, vous pouvez joindre un schéma à votre définition pour faciliter la compréhension. Vous pouvez envoyer un schéma brouillon que je reprendrai en l'adaptant à la charte graphique du projet.

## Termes acceptés dans le Dictionnaire
L'intégration d'un nouveau terme dans le *Dictionnaire de Bitcoin* nécessite simplement qu'il soit pertinent pour Bitcoin ou son écosystème. Utilisez votre discernement pour juger de l'utilité potentielle du terme pour ceux qui étudient ou utilisent Bitcoin et son environnement. 

L'ambition de ce dictionnaire est de couvrir le champ lexical de Bitcoin avec la plus grande exhaustivité possible, dans le même esprit que les dictionnaires professionnels d'autres domaines. Ainsi, même les termes d'intérêt limité doivent être considérés.

Un terme est accepté si la réponse à la question suivante est affirmative : **« _Un débutant qui étudie Bitcoin pourrait-il croiser ce terme durant ses recherches et désirer en comprendre la signification ?_ »**

Tous les termes techniques, logiciels, algorithmes et protocoles sont acceptés s'ils se rapportent, de manière directe ou indirecte, à Bitcoin ou à un protocole s'appuyant sur Bitcoin (comme Lightning, RGB, Liquid, Ark...).

Les termes généraux liés à l'informatique et à la cryptographie sont uniquement inclus s'ils sont susceptibles d'être rencontrés et nécessaires à la compréhension de Bitcoin. L'objectif est d'offrir un dictionnaire complet sans pour autant devenir un dictionnaire informatique généraliste.

Quant aux noms d'entreprises et de marques, j'accepte de les ajouter uniquement si elles ont eu un rôle historique dans l'évolution technique de Bitcoin. Il faut également qu'elles soient connues à l'échelle internationale. La préférence est donnée à l'intégration des logiciels et des protocoles développés par ces entreprises, plutôt qu'aux entreprises en elles-mêmes. Les propositions d'ajout de définition contre rémunération ne sont pas acceptées. 

En ce qui concerne les individus, seules les contributions historiquement significatives à Bitcoin justifient une mention. Plutôt que de nommer directement une personne, il est préférable de référencer le logiciel ou le protocole sur lequel elle a travaillé, en la mentionnant dans la définition correspondante.

On ne parle évidemment pas de shitcoins dans ce dictionnaire, sauf si le shitcoin en question fait partie de l'histoire de Bitcoin (par exemple, les forks de Bitcoin).

Il n'y a pas de limite de taille pour les définitions. Je préfère avoir une définition exhaustive, même si elle doit être longue, plutôt qu'une définition courte et imprécise.

## Licence et réutilisation
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
**Crédit:**
Cette définition est extraite du « Dictionnaire de Bitcoin », un ouvrage libre rédigé par Loïc Morel (Pandul) disponible sur GitHub : https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/tree/main

Cet ouvrage est sous licence CC BY-NC-SA 4.0 [Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International][cc-by-nc-sa-fr].

This work is licensed under a CC BY-NC-SA 4.0
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
[cc-by-nc-sa-fr]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr
