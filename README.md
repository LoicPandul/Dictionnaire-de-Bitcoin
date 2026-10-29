[![Cover Image](./assets/images/cover.png)](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/blob/main/dictionnaire-de-bitcoin.pdf)

<p align="center">
  <img src="https://img.shields.io/badge/Nombre%20de%20d%C3%A9finitions-1536-1B3A4B?style=for-the-badge" alt="Nombre de définitions">
</p>

<p align="center">
  <a href="https://bitcoinbazar.fr/products/le-dictionnaire-de-bitcoin"><img src="https://img.shields.io/badge/Acheter%20sur%20Bitcoin%20Bazar-F7931A?style=for-the-badge&logo=bitcoin&logoColor=white" alt="Acheter sur Bitcoin Bazar"></a>
  <a href="https://amzn.to/4cxaOA8"><img src="https://img.shields.io/badge/Acheter%20sur%20Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white" alt="Acheter sur Amazon"></a>
</p>

<p align="center">
  <a href="https://x.com/Loic_Pandul"><img src="https://img.shields.io/badge/@Loic__Pandul-000000?style=flat&logo=x&logoColor=white" alt="X"></a>
  <a href="https://www.pandul.fr/"><img src="https://img.shields.io/badge/pandul.fr-000000?style=flat&logo=firefox&logoColor=white" alt="Site web"></a>
  <a href="mailto:info@pandul.fr"><img src="https://img.shields.io/badge/info@pandul.fr-D14836?style=flat&logo=mail.ru&logoColor=white" alt="Email"></a>
</p>


⚡ Lightning :

```
sats@pandul.fr
```

## Table des matières
- [Description du projet](#description-du-projet)
- [Lire le *Dictionnaire de Bitcoin*](#lire-le-dictionnaire-de-bitcoin)
- [Demandes de modification et contributions](#demandes-de-modification-et-contributions)
- [Termes acceptés dans le *Dictionnaire de Bitcoin*](#termes-acceptés-dans-le-dictionnaire-de-bitcoin)
- [Version anglaise](#version-anglaise)
- [Structure du dépôt](#structure-du-dépôt)
- [Scripts et génération](#scripts-et-génération)
- [Licence et réutilisation](#licence-et-réutilisation)

## Description du projet

Cet ouvrage recense tous les termes techniques en rapport avec Bitcoin ou son environnement, ainsi que les définitions correspondantes. Rédigé par Loïc Morel, de pandul.fr, il est accessible gratuitement en version numérique sur ce dépôt GitHub. Ce livre est également vendu imprimé sur [Amazon](https://amzn.to/4cxaOA8) et [Bitcoin Bazar](https://bitcoinbazar.fr/products/le-dictionnaire-de-bitcoin).

Je gagne une petite marge sur chaque exemplaire physique vendu. Si vous trouvez ce projet utile, ou plus généralement, si vous appréciez mon travail de production de contenus pédagogiques, vous pouvez commander votre propre livre *Dictionnaire de Bitcoin* afin de me soutenir.

Si vous souhaitez soutenir ce projet, vous pouvez aussi le partager sur les réseaux sociaux ou me faire un don LN sur sats@pandul.fr. Merci !

## Lire le *Dictionnaire de Bitcoin*

Vous pouvez découvrir gratuitement [la version PDF du *Dictionnaire de Bitcoin*](/dictionnaire-de-bitcoin.pdf) à la racine de ce dépôt ou [dans les Releases](https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/releases). C'est la manière la plus simple de lire et de rechercher des définitions. Vous pouvez également parcourir les définitions directement sur GitHub dans le dossier [definitions/fr/](./definitions/fr/). Chaque définition est dans son propre dossier, classé alphabétiquement.

Pour faciliter la navigation et vous aider à trouver rapidement les définitions, consultez l'[INDEX.md](./INDEX.md) qui liste toutes les entrées avec des liens directs.

<p align="center">
  <a href="./INDEX.md">
    <img src="https://img.shields.io/badge/Acc%C3%A9der%20au%20sommaire-Cliquez%20ici-1B3A4B?style=for-the-badge" alt="Accéder au sommaire">
  </a>
</p>

## Demandes de modification et contributions

*Dictionnaire de Bitcoin* est un projet ouvert. Vous êtes libre de proposer tout type de modification ou de correction, ce qui inclut notamment :
* La suggestion de nouveaux termes à ajouter (avec ou sans définition) ;
* La correction d'une définition qui vous semble erronée ou imprécise ;
* La correction d'une faute d'orthographe ou d'une coquille ;
* Toute autre suggestion de modification.

### Comment contribuer

1. Créez votre fork du projet ;
2. Créez une nouvelle branche établie sur la branche `main` ;
3. Consultez la [charte éditoriale](./docs/charte-editoriale.md) pour respecter les conventions de rédaction ;
4. Rédigez vos suggestions de modification dans le dossier `definitions/fr/` ;
5. Faites une Pull Request pour fusionner votre branche face à la branche `main` du dépôt source.

### Ajouter une nouvelle définition

Pour ajouter une nouvelle définition :

- Créez un dossier dans `definitions/fr/{lettre}/{slug-de-la-definition}/`
- Créez un fichier `metadata.yaml` avec les métadonnées :

```yaml
uuid: "générez-un-uuid-v4-unique"
title: "TITRE EN MAJUSCULES"
slug: "titre-en-minuscules" # identique au nom de dossier
category: "CATÉGORIE" # une catégorie de templates/categories.yaml
english_term: "ENGLISH TERM"  # optionnel
french_term: "FRENCH TERM"  # optionnel
cross_references:
  - "UUID du terme connexe"
  - "UUID du terme connexe"
version: "1"
```

- Créez un fichier `definition.md` avec le corps de la définition (la version développée)
- Créez un fichier `courte.md` avec la version courte : une ou deux phrases, 45 mots au plus, pour comprendre le terme en un coup d'œil
- Si votre définition inclut des images, créez un dossier `assets/` et référencez-les avec `![Texte alternatif](./assets/image.png)` ; le texte alternatif sert aussi de légende dans le livre

La catégorie décide de la partie du livre où l'entrée apparaît (dictionnaire technique, entreprises et logiciels, personnes, spécifications) : voir `templates/parts.yaml`. Avant de proposer votre modification, lancez `python3 scripts/main.py check`.

### Modifier une définition existante

Naviguez vers `definitions/fr/{lettre}/{slug}/` et modifiez le fichier `definition.md`. Si l'entrée existe aussi en anglais dans `definitions/en/`, reportez-y la modification ou signalez-la dans la PR (voir [CONTRIBUTING.md](./CONTRIBUTING.md)).

Si vous ne vous sentez pas à l'aise avec l'utilisation de Git, ou si vous avez en tête une modification mineure, vous pouvez également créer une issue sur GitHub plutôt qu'une PR.

Dans le fichier [pending_terms.yaml](./templates/pending_terms.yaml), vous trouverez tous les termes auxquels j'ai déjà pensé, mais que je n'ai pas encore eu le temps de définir. Si vous souhaitez contribuer, vous pouvez piocher dans cette liste.

Pour les changements d'envergure, comme la réalisation d'une traduction de l'ouvrage, je vous invite à me contacter directement à info@pandul.fr ou sur [mon Twitter](https://x.com/Loic_Pandul).

En contribuant, **votre pseudo GitHub sera mentionné tant dans la version en ligne que dans la version imprimée du Dictionnaire**. Si vous préférez ne pas être cité, ou si vous souhaitez apparaître sous un autre nom que votre pseudo GitHub, veuillez le préciser explicitement dans votre issue ou votre PR. À défaut, je prends le pseudo GitHub.

## Termes acceptés dans le *Dictionnaire de Bitcoin*

L'intégration d'un nouveau terme dans le *Dictionnaire de Bitcoin* nécessite simplement qu'il soit en lien avec Bitcoin ou son écosystème. L'ambition de ce dictionnaire est de couvrir le champ lexical de Bitcoin avec la plus grande exhaustivité possible, dans le même esprit que les dictionnaires professionnels d'autres domaines.

Un terme est accepté si la réponse à la question suivante est affirmative : **« _Un débutant qui étudie Bitcoin pourrait-il croiser ce terme durant ses recherches et désirer en comprendre la signification ?_ »**

Tous les termes techniques, logiciels, algorithmes et protocoles sont acceptés s'ils se rapportent, de manière directe ou indirecte, à Bitcoin ou à un protocole s'appuyant sur Bitcoin (comme Lightning, RGB, Liquid, Ark...).

Les termes généraux liés à l'informatique et à la cryptographie sont uniquement inclus s'ils sont susceptibles d'être rencontrés et nécessaires à la compréhension de Bitcoin.

Il n'y a pas de limite de taille pour les définitions. Je préfère avoir une définition exhaustive, même si elle doit être longue, plutôt qu'une définition courte et imprécise.

## Version anglaise

Le livre existe aussi en anglais, sous le titre *Bitcoin Dictionary* : définitions dans [definitions/en/](./definitions/en/), chronologie dans `chronologie/en/`, résumés des spécifications dans `specifications/en/`, textes du livre dans `templates/en/`. `python3 scripts/main.py build --lang en` le génère dans `build/en/`. Chaque texte anglais garde l'empreinte de la version française qu'il traduit, et `python3 scripts/main.py sync` signale les traductions manquantes, en retard ou à reporter en français. Si vous modifiez une définition qui existe dans les deux langues, suivez la règle de [CONTRIBUTING.md](./CONTRIBUTING.md) ; le détail est dans [docs/traduction.md](./docs/traduction.md).

*The whole dictionary is translated into English as the* Bitcoin Dictionary *([definitions/en/](./definitions/en/), `chronologie/en/`, `specifications/en/`); build it with `python3 scripts/main.py build --lang en`. See [CONTRIBUTING.md](./CONTRIBUTING.md#contributing-to-the-bitcoin-dictionary) to keep French and English in sync.*

## Structure du dépôt

Le rangement du dépôt et ses raisons sont décrits dans [docs/structure.md](./docs/structure.md).

<!-- arbre:debut -->
```plaintext
Dictionnaire-de-Bitcoin/
├── definitions/                    # Entrées du dictionnaire, une langue par dossier
│   ├── fr/                         # Langue d'origine
│   │   └── a/adresse-de-reception/
│   │       ├── metadata.yaml       # UUID, titre, catégorie, renvois, images
│   │       ├── definition.md       # Version développée
│   │       ├── courte.md           # Version courte (une ou deux phrases)
│   │       └── assets/             # Images de l'entrée
│   └── en/                         # Traduction anglaise
│       └── r/receiving-address/
│           ├── metadata.yaml       # UUID, titre, slug, trace de la source (source_*)
│           ├── definition.md
│           └── courte.md
│
├── chronologie/
│   ├── fr/                         # Chronologie, un fichier par année
│   └── en/                         # Titres et textes traduits (dates, renvois, sources : fr/)
├── specifications/
│   ├── fr/                         # BIP, BOLT et bLIP : numéro, titre, statut, résumé
│   └── en/                         # Résumés traduits
│
├── templates/                      # Configuration du livre, commune aux langues
│   ├── categories.yaml             # Catégories et leur description
│   ├── parts.yaml                  # Parties du livre et catégories de chaque partie
│   ├── editions.yaml               # Éditions générées (complète en couleur, essentiel en poche)
│   ├── languages.yaml              # Langues et périmètre de chaque traduction
│   ├── fr/                         # Textes du livre en français
│   │   ├── introduction.md         # Note de l'auteur
│   │   ├── contributors.md         # Contributeurs et remerciements
│   │   ├── legal.yaml              # Mentions légales
│   │   ├── excluded_words.yaml     # Mots exclus des statistiques
│   │   └── pending_terms.yaml      # Termes en attente de définition
│   └── en/                         # Textes du livre anglais
│       ├── book.yaml               # Titres des parties et des éditions, noms des catégories
│       ├── introduction.md
│       ├── contributors.md
│       └── legal.yaml              # Ce qui diffère du français (ISBN)
│
├── assets/
│   ├── images/                     # Images du README
│   ├── pictograms/                 # Pictogrammes des catégories (SVG/PDF)
│   ├── fonts/                      # Polices du livre (Archivo, Atkinson Hyperlegible Mono)
│   └── cover-paperback.pdf         # Couverture du livre broché
│
├── docs/
│   ├── structure.md                # Ce rangement et ses raisons
│   ├── traduction.md               # Synchro français / anglais
│   ├── glossaire-fr-en.md          # Terminologie de la traduction anglaise
│   ├── charte-editoriale.md        # Charte éditoriale (français)
│   └── edition-2027/               # Dossier de travail de l'édition 2027
│
├── scripts/                        # Validation, synchro et génération (PDF, EPUB, index, stats)
│   └── migrations/                 # Scripts de rangement à usage unique
│
├── build/                          # Sorties de build (ignoré par git)
├── dictionnaire-de-bitcoin.pdf     # Version PDF
├── INDEX.md                        # Index des définitions
├── stats.md                        # Statistiques
├── CONTRIBUTING.md                 # Contribuer, et garder le français et l'anglais synchronisés
├── README.md
├── LICENCE_FR.md
└── LICENSE.md
```
<!-- arbre:fin -->

## Scripts et génération

Voir le [README dédié](./scripts/README.md) dans le dossier `scripts/`.

## Licence et réutilisation

**Shield:**
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

**Crédit:**

```md
Cette définition est extraite du « Dictionnaire de Bitcoin », un ouvrage rédigé par Loïc Morel (pandul.fr) disponible sur GitHub : https://github.com/LoicPandul/Dictionnaire-de-Bitcoin/
```

Cet ouvrage est sous licence CC BY-NC-SA 4.0 [Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International][cc-by-nc-sa-fr].

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