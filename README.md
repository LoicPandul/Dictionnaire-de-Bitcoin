[![Cover Image](./img/cover.png)](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/blob/main/Dictionnaire%20de%20Bitcoin.pdf)
<p align="center">
  <img src="https://img.shields.io/badge/Nombre%20de%20définitions-777-black" alt="Nombre de définitions">
</p>

<p align="center">
  <a href="https://x.com/Loic_Pandul">
    <img src="https://img.shields.io/twitter/follow/Loic_Pandul?style=social" alt="Suivez-moi sur X">
  </a>
  <a href="https://www.pandul.fr/">
    <img src="https://img.shields.io/badge/Site%20web-Visitez%20mon%20site-brightgreen?style=social&logo=internet-explorer" alt="Visitez mon site">
  </a>
</p>

## Table des matières
- [Description du projet 📝](#description-du-projet-)
- [Lire le *Dictionnaire de Bitcoin* 📖](#lire-le-dictionnaire-de-bitcoin-)
- [Demandes de modification et contributions ✍️](#demandes-de-modification-et-contributions-%EF%B8%8F)
- [Termes acceptés dans le *Dictionnaire de Bitcoin* ✅](#termes-acceptés-dans-le-dictionnaire-de-bitcoin-)
- [Structure du dépôt 🗂️](#structure-du-dépôt-%EF%B8%8F)
- [Licence et réutilisation 📜](#licence-et-réutilisation-)

## Description du projet 📝

Cet ouvrage recense tous les termes techniques en rapport avec Bitcoin ou son environnement, ainsi que les définitions correspondantes. Rédigé par Loïc Morel, de Pandul, il est accessible gratuitement en version numérique sur ce dépôt GitHub. Ce livre sera également vendu imprimé sur Amazon à partir de fin 2024.

Je gagne une petite marge sur chaque exemplaire physique vendu via Amazon. Si vous trouvez ce projet utile, ou plus généralement, si vous appréciez mon travail de production de contenus pédagogiques, vous pouvez commander votre propre livre *Dictionnaire de Bitcoin* afin de me soutenir.

La première édition de l'ouvrage est prévue pour 2024. Si le projet intéresse et suscite de l'engagement, je publierai de nouvelles versions actualisées du *Dictionnaire de Bitcoin*. Ces mises à jour comprendront les modifications proposées par la communauté de contributeurs et les termes nouvellement apparus.

Si vous souhaitez soutenir ce projet, vous pouvez aussi le partager sur les réseaux sociaux ou me faire un don LN sur pandul@sats.rs. Merci ! :)

## Lire le *Dictionnaire de Bitcoin* 📖

Vous pouvez découvrir gratuitement [la version PDF du *Dictionnaire de Bitcoin*](/Dictionnaire%20de%20Bitcoin.pdf) à la racine de ce dépôt ou [dans les Releases](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/releases). C'est la manière la plus simple de lire et de rechercher des définitions.

&nbsp;
<p align="center">
  <img src="./img/README%20GIF.gif" alt="Présentation GIF" width="70%">
</p>
&nbsp;

Pour les liseuses, il y a une version en .epub que [vous pouvez télécharger à la racine](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/blob/main/Dictionnaire_de_Bitcoin.epub).

Vous pouvez également découvrir la version en markdown du *Dictionnaire de Bitcoin* dans le dossier [dictionnaire](./dictionnaire). Les définitions sont classées par ordre alphabétique et chaque fichier markdown correspond à une lettre.

Pour faciliter la navigation et vous aider à trouver rapidement les définitions, j'ai créé un sommaire détaillé de tous les termes inclus dans le *Dictionnaire de Bitcoin*. Chaque entrée du sommaire est liée à sa définition spécifique, ce qui vous permet d'accéder directement à l'information recherchée.

<p align="center">
  <a href="./INDEX.md">
    <img src="https://img.shields.io/badge/Accéder%20au%20sommaire-Cliquez%20ici-black" alt="Accéder au sommaire">
  </a>
</p>

La branche `main` correspond à la version intermédiaire de travail, sur laquelle les PR sont fusionnées progressivement.

Sur ce dépôt, vous trouverez le dictionnaire décliné en trois formats différents, chacun contenant les mêmes définitions, afin de répondre aux préférences de chacun, que vous souhaitiez intégrer le dictionnaire à un site web ou simplement le télécharger pour un usage personnel. Les formats proposés sont les suivants :
- [Un fichier markdown unique rassemblant l'ensemble des définitions](/autres_formats/dictionnaire_complet/dictionnaire_complet.md) ;
- [Un dossier contenant un fichier markdown séparé pour chaque définition](/autres_formats/definitions_individuelles) ;
- [Un dossier de travail `/dictionnaire` organisé de manière à regrouper les définitions dans des fichiers markdown par lettre de l'alphabet](/dictionnaire).

## Demandes de modification et contributions ✍️

*Dictionnaire de Bitcoin* est un projet ouvert. Vous êtes libre de proposer tout type de modification ou de correction, ce qui inclut notamment :
* La suggestion de nouveaux termes à ajouter (avec ou sans définition) ;
* La correction d'une définition qui vous semble erronée ou imprécise ;
* La correction d'une faute d'orthographe ou d'une coquille ;
* Toute autre suggestion de modification.

Pour contribuer, voici la marche à suivre : 
1. Créez votre fork du projet ;
2. Créez une nouvelle branche établie sur la branche `main` ; 
3. Rédigez vos suggestions de modification directement sur votre branche ;
4. Proposez une Pull Request pour fusionner votre branche face à la branche `main` du dépôt source.

Sur ce dépôt, vous trouverez le dictionnaire décliné en trois formats différents, chacun contenant les mêmes définitions, afin de répondre aux préférences de chacun. Les formats proposés sont les suivants :
- [Un fichier markdown unique rassemblant l'ensemble des définitions](/autres_formats/dictionnaire_complet/dictionnaire_complet.md) ;
- [Un dossier contenant un fichier markdown séparé pour chaque définition](/autres_formats/definitions_individuelles) ;
- [Un dossier de travail `/dictionnaire` organisé de manière à regrouper les définitions dans des fichiers markdown par lettre de l'alphabet](/dictionnaire).

**Les contributions doivent se faire uniquement sur le dossier de travail [/dictionnaire](/dictionnaire).** Un script python permet de mettre à jour automatiquement les autres formats.

Si vous ne vous sentez pas à l'aise avec l'utilisation de Git, ou si vous avez en tête une modification mineure à apporter (telle que l'ajout d'un terme ou la correction d'une petite erreur d'orthographe), vous pouvez également créer une issue sur GitHub plutôt qu'une PR.

Dans le fichier [Termes en attente.md](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/blob/main/Termes%20en%20attente.md), vous trouverez tous les termes auxquels j'ai déjà pensé, mais que je n'ai pas encore eu le temps de définir (c'est un peu ma mempool à moi !). Si vous souhaitez contribuer, vous pouvez piocher dans cette liste de mots pour écrire les définitions que vous connaissez. Si vous souhaitez demander l'ajout d'un nouveau terme, avant de me contacter ou d'ouvrir une issue, je vous remercie de bien vouloir vérifier qu'il ne se trouve pas dans cette liste d'attente.

Pour les changements d'envergure, comme la réalisation d'une traduction de l'ouvrage, je vous invite à me contacter directement à info@pandul.fr ou sur [mon Twitter](https://x.com/Loic_Pandul).

En contribuant, **votre pseudo GitHub sera mentionné tant dans la version en ligne que dans la version imprimée du dictionnaire**. Si vous préférez ne pas être cité, ou si vous souhaitez apparaître sous un autre nom que votre pseudo GitHub, veuillez le préciser explicitement dans votre issue ou votre PR.

Mon objectif pour ce projet de dictionnaire est de publier une nouvelle édition toutes les N années. Ainsi, les modifications apportées au document principal ne se refléteront pas immédiatement dans la version imprimée disponible sur Amazon.

Si vous le souhaitez, vous pouvez joindre un schéma à votre définition pour faciliter la compréhension. Vous pouvez envoyer un schéma brouillon que je reprendrai en l'adaptant à la charte graphique du projet.

## Termes acceptés dans le *Dictionnaire de Bitcoin* ✅

L'intégration d'un nouveau terme dans le *Dictionnaire de Bitcoin* nécessite simplement qu'il soit en lien avec Bitcoin ou son écosystème. L'ambition de ce dictionnaire est de couvrir le champ lexical de Bitcoin avec la plus grande exhaustivité possible, dans le même esprit que les dictionnaires professionnels d'autres domaines. Ainsi, même les termes d'intérêt limité doivent être considérés, car la qualité d'un dictionnaire ne repose pas sur la sélection et la synthèse des informations, comme ça peut être le cas pour un livre classique, mais plutôt sur l'étendue des termes qu'il couvre.

Un terme est accepté si la réponse à la question suivante est affirmative : **« _Un débutant qui étudie Bitcoin pourrait-il croiser ce terme durant ses recherches et désirer en comprendre la signification ?_ »**

Tous les termes techniques, logiciels, algorithmes et protocoles sont acceptés s'ils se rapportent, de manière directe ou indirecte, à Bitcoin ou à un protocole s'appuyant sur Bitcoin (comme Lightning, RGB, Liquid, Ark...).

Les termes généraux liés à l'informatique et à la cryptographie sont uniquement inclus s'ils sont susceptibles d'être rencontrés et nécessaires à la compréhension de Bitcoin. L'objectif est d'offrir un dictionnaire complet, sans pour autant devenir un dictionnaire informatique généraliste.

Quant aux noms d'entreprises et de marques, j'accepte de les ajouter uniquement si elles ont eu un rôle historique dans l'évolution technique de Bitcoin. Il faut également qu'elles soient connues à l'échelle internationale. La préférence est donnée à l'intégration des logiciels et des protocoles développés par ces entreprises, plutôt qu'aux entreprises en elles-mêmes. Les propositions d'ajout de définition contre rémunération ne sont pas acceptées. 

En ce qui concerne les individus, seules les contributions historiquement significatives à Bitcoin justifient une mention (Satoshi Nakamoto, Hal Finney...). Plutôt que de nommer directement une personne, il est préférable de référencer le logiciel ou le protocole sur lequel elle a travaillé, en la mentionnant dans la définition correspondante.

On ne parle évidemment pas de shitcoins dans ce dictionnaire, sauf si le shitcoin en question fait partie de l'histoire de Bitcoin (par exemple, les forks de Bitcoin).

Il n'y a pas de limite de taille pour les définitions. Je préfère avoir une définition exhaustive, même si elle doit être longue, plutôt qu'une définition courte et imprécise.

## Structure du dépôt 🗂️

```plaintext 
Dictionnaire-de-Bitcoin/
├── .gitignore
├── Dictionnaire de Bitcoin.pdf
├── INDEX.md
├── LICENCE_FR.md
├── LICENSE_ENG.md
├── README.md
├── Termes en attente.md
├── stats.md
├── img/
├── dictionnaire/
│   ├── A.md
│   ├── B.md
│   ├── C.md
│   ├── ...
│   └── Z.md
├── autres_formats/
│   ├── dictionnaire_complet/
│   │   └── dictionnaire_complet.md
│   └── definitions_individuelles/
│       ├── definition_1.md
│       ├── definition_2.md
│       ├── definition_3.md
│       ├── ...
│       └── definition_N.md
└── scripts/
    ├── PDF/
    │   ├── contributeurs_paragraphe.md
    │   ├── cover_back.png
    │   ├── cover_front.png
    │   ├── dictionnaire_MD_for_PDF.md
    │   └── pdf.py
    ├── execute_all_scripts.py
    ├── generate_dictionary_files.py
    ├── md_for_pdf.py
    ├── puces_et_citations.py
    ├── stats.py
    ├── termes_manquants.py
    └── update_index.py
```

## Licence et réutilisation 📜

**Shield:** [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

**Crédit:**
Cette définition est extraite du « Dictionnaire de Bitcoin », un ouvrage libre rédigé par Loïc Morel (Pandul) disponible sur GitHub : https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/tree/main

Cet ouvrage est sous licence CC BY-NC-SA 4.0 [Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International][cc-by-nc-sa-fr].

This work is licensed under a CC BY-NC-SA 4.0
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

<div align="center">
  <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img src="https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png" alt="CC BY-NC-SA 4.0">
  </a>
</div>

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
[cc-by-nc-sa-fr]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr


[![Cover Image](./img/Logo-Pandul-NOIR.png)](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/blob/main/Dictionnaire%20de%20Bitcoin.pdf)


