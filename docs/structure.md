# Structure du dépôt

Ce document décrit le rangement du dépôt depuis l'arrivée de la version anglaise : où vit chaque
type de fichier, et pourquoi. La synchronisation entre le français et l'anglais a son propre
document : [traduction.md](./traduction.md).

## Principes

1. **Une langue est un sous-dossier, au plus près du contenu.** `definitions/fr/` et
   `definitions/en/`, `chronologie/fr/` et `chronologie/en/`, `specifications/fr/` et
   `specifications/en/`. Pas de second dépôt ni de copie de l'arborescence par langue : une même
   pull request peut corriger les deux versions d'une entrée, le script de synchro compare les
   deux dossiers, et tout ce qui ne se traduit pas reste commun.
2. **Une entrée a la même forme dans toutes les langues.** Un dossier par entrée, avec
   `metadata.yaml`, `definition.md`, `courte.md` et, s'il y a lieu, `assets/`. Les noms de fichiers
   sont des identifiants, pas de la prose : `courte.md` garde son nom en anglais. Les validateurs,
   les générateurs et le site lisent ainsi les deux langues avec le même code.
3. **Ce qui ne se traduit pas n'est écrit qu'une fois.** L'UUID relie les versions d'une entrée.
   La catégorie, les renvois et les images déclarées vivent dans la version d'origine (le
   français aujourd'hui) et valent pour toutes les langues. La traduction ne porte que son titre,
   son slug et la trace de sa source.
4. **Le slug suit la langue.** `definitions/fr/a/adresse-de-reception/` et
   `definitions/en/r/receiving-address/` : chaque URL du site se lit dans sa langue. Un slug publié
   ne change plus, en français comme en anglais.
5. **La configuration commune et les textes traduits sont séparés.** `templates/` garde ce qui
   décrit le livre quelle que soit la langue (catégories, parties, éditions, langues) ;
   `templates/fr/` et `templates/en/` gardent les textes du livre (note de l'auteur, mentions
   légales, remerciements).
6. **La racine montre ce qu'un lecteur cherche.** README, PDF, index, licences, guide de
   contribution. Le reste est rangé dans un dossier qui dit ce qu'il contient : `docs/` pour la
   documentation des contributeurs et les dossiers de travail des éditions, `assets/` pour les
   fichiers binaires communs, `scripts/` pour l'outillage.
7. **Les chemins publics restent stables.** Les PDF restent à la racine et les slugs français ne
   bougent pas : des liens extérieurs (boutique, réseaux, site) pointent vers eux.

## Arbre cible

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
├── chronologie/fr/                 # Chronologie, un fichier par année (en/ plus tard)
├── specifications/fr/              # BIP, BOLT et bLIP : numéro, titre, statut, résumé
│
├── templates/                      # Configuration du livre, commune aux langues
│   ├── categories.yaml             # Catégories et leur description
│   ├── parts.yaml                  # Parties du livre et catégories de chaque partie
│   ├── editions.yaml               # Éditions générées (complète en couleur, essentiel en poche)
│   ├── languages.yaml              # Langues et périmètre de chaque traduction
│   └── fr/                         # Textes du livre en français
│       ├── introduction.md         # Note de l'auteur
│       ├── contributors.md         # Contributeurs et remerciements
│       ├── legal.yaml              # Mentions légales
│       ├── excluded_words.yaml     # Mots exclus des statistiques
│       └── pending_terms.yaml      # Termes en attente de définition
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

## Chaque dossier et sa raison

| Dossier | Contenu | Pourquoi ici |
|---|---|---|
| `definitions/<langue>/<lettre>/<slug>/` | une entrée par dossier | La lettre découpe 1 600 dossiers en 26 listes lisibles sur GitHub. Le site et les scripts lisent déjà `definitions/fr`. |
| `chronologie/<langue>/` | un fichier YAML par année | Le texte des événements se traduit ; les dates, liens et sources sont identiques d'une langue à l'autre. |
| `specifications/<langue>/` | `bip.yaml`, `bolt.yaml`, `blip.yaml` | Le résumé de chaque spécification est en français : il se traduit comme une définition. Ranger ces fichiers par langue évite un `bip.en.yaml` isolé à côté de `bip.yaml`. |
| `templates/` | `categories.yaml`, `parts.yaml`, `editions.yaml`, `languages.yaml` | Les catégories sont des identifiants (`PROTOCOLE`) que toutes les langues partagent ; les éditions et les parties décrivent le livre, pas sa langue. Le site lit les commentaires de `categories.yaml` : ce fichier ne bouge pas. |
| `templates/<langue>/` | note de l'auteur, mentions légales, remerciements, mots exclus, termes en attente | Textes à traduire : un dossier par langue, comme les définitions. |
| `assets/` | images du README, pictogrammes, polices, couverture du broché | Tous les fichiers binaires communs au même endroit ; `fonts/` à la racine n'en était qu'un cas particulier. |
| `docs/` | documentation des contributeurs, dossiers de travail des éditions | La racine reste lisible ; un nouveau contributeur trouve toute la documentation au même endroit. `docs/edition-2027/` garde la mémoire du chantier 2027 sans encombrer la racine. |
| `scripts/` | outillage Python | Inchangé. `scripts/migrations/` reçoit les scripts de rangement à usage unique, gardés pour mémoire. |
| `build/` | PDF, EPUB et sources LaTeX générés | Ignoré par git. Le livre anglais sortira dans `build/en/<édition>/` quand le générateur saura le construire. |
| racine | README, PDF, `INDEX.md`, `stats.md`, licences, `CONTRIBUTING.md` | Ce qu'un lecteur ou un contributeur ouvre en premier. GitHub affiche `CONTRIBUTING.md` à l'ouverture d'une pull request. |

## Ce qui change

| Ancien chemin | Nouveau chemin | Raison |
|---|---|---|
| `specifications/*.yaml` | `specifications/fr/*.yaml` | résumés en français, à traduire |
| `templates/introduction.md`, `contributors.md`, `legal.yaml`, `excluded_words.yaml`, `pending_terms.yaml` | `templates/fr/` | textes en français ; `templates/` ne garde que la configuration commune |
| `STYLE_GUIDE.md` | `docs/charte-editoriale.md` | documentation des contributeurs, propre au français (l'anglais aura la sienne) |
| `edition-2027/` | `docs/edition-2027/` | dossier de travail, pas un contenu du livre |
| `fonts/` | `assets/fonts/` | fichiers binaires communs |

Ce qui ne bouge pas, volontairement :

- `definitions/fr/` et ses slugs : le site construit ses URL depuis ces dossiers.
- `chronologie/fr/` : déjà rangée par langue.
- Les PDF, `INDEX.md` et `stats.md` à la racine : liens extérieurs et badge du README.
- Les noms de fichiers d'une entrée (`courte.md` compris) : identifiants partagés par les
  scripts, le site et les deux langues. Les renommer coûterait 1 600 déplacements sans rien
  apporter au lecteur.

## La migration

Ce rangement a été appliqué le 27 octobre 2026, en un commit
(`refactor(repo): move to the bilingual layout`), par `scripts/migrations/structure_bilingue.py`,
une fois fusionnées les branches qui modifiaient les mêmes fichiers (`feat/edition-2027`,
`feat/schemas-2027`). Le script reste dans le dépôt pour mémoire : il déplace avec `git mv`,
réécrit les chemins cités dans les fichiers suivis, remplace l'arbre du README par celui de ce
document et lance `python3 scripts/main.py check`. Relancé, il ne change rien.

Hors du dépôt, deux outils citent encore les anciens chemins et sont à mettre à jour :
le skill `dictionnaire-definition` (`templates/pending_terms.yaml`, dans `scripts/doublons.py`)
et le skill `dictionnaire-redaction` (mentions de `STYLE_GUIDE.md` et de `specifications/`).
Le site (`site/`, branche `feat/site-dictionnaire`) a été écrit avant la migration. À sa
prochaine fusion, trois chemins sont à suivre :

- `site/lib/edition.mjs` : les séries de spécifications se lisent dans `specifications/fr/`
  (et `specifications/<langue>/` pour une traduction), plus dans `specifications/` ;
- `site/build.mjs` : `edition-2027/reclassement.tsv` devient `docs/edition-2027/reclassement.tsv` ;
- `site/README.md` : les polices viennent de `assets/fonts/`.

Le reste de ce qu'il lit ne bouge pas (`definitions/`, `chronologie/fr/`, `templates/*.yaml`,
`assets/pictograms/`).

## Plus tard

Ces étapes viendront avec le livre anglais, pas avant :

- `templates/en/` : note de l'auteur, mentions légales et remerciements en anglais, et les noms
  affichés des parties et des catégories (`parts.yaml` garde les identifiants communs).
- `specifications/en/`, `chronologie/en/` : résumés et événements traduits, suivis par le même
  mécanisme que les définitions.
- `README.en.md` et un index anglais, générés comme `INDEX.md`.
- Schémas en anglais : les traductions réutilisent aujourd'hui les images françaises
  (`../../../fr/<lettre>/<slug>/assets/…`) ; un schéma redessiné en anglais ira dans le dossier
  `assets/` de l'entrée anglaise.
- `python3 scripts/main.py build --lang en` et les sorties dans `build/<langue>/<édition>/`.
