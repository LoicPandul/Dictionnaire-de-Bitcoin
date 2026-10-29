# Traduction et synchro français / anglais

Le dictionnaire est écrit en français ; la version anglaise traduit tout le livre : les
définitions des quatre parties, les résumés des spécifications et la chronologie (périmètre fixé
dans `templates/languages.yaml`). Ce document explique comment une
traduction garde la trace de sa source, comment le script repère ce qui est à refaire, et ce
que fait un contributeur qui modifie l'une ou l'autre langue. La règle courte est aussi dans
[CONTRIBUTING.md](../CONTRIBUTING.md).

## La trace de la source

Les deux versions d'une entrée partagent le même UUID. La version traduite note dans son
`metadata.yaml` l'état de la source qu'elle traduit :

```yaml
uuid: "0cda73d6-8c4a-4d18-bd03-1d56a12154dd"   # le même que l'entrée française
title: "BEARER ASSET"
slug: "bearer-asset"
source_lang: "fr"                               # langue de la version d'origine
source_slug: "actif-au-porteur"                 # dossier de la source, pour s'y retrouver
source_hash: "4be1f0c29a7d3e85"                 # empreinte de la source à la dernière synchro
source_commit: "0589898a"                       # dernier commit de la source à ce moment
translation_hash: "93c0d1aa5e6b2f47"            # empreinte de la traduction à la dernière synchro
```

L'empreinte est un SHA-256 tronqué du titre, de `definition.md` et de `courte.md` (espaces de fin
de ligne ignorés). Elle ne dépend pas de git : elle survit aux rebases, aux fusions écrasées
(squash) et aux copies du dépôt. Le commit sert seulement d'indice pour afficher le `git diff`.

Tout ce qui ne se traduit pas reste dans la version d'origine : catégorie, renvois, images
déclarées. Une traduction n'a donc rien à mettre à jour quand on change une catégorie ou un
renvoi en français.

### Chronologie et résumés des spécifications

La chronologie (`chronologie/<langue>/<année>.yaml`) et les résumés des BIP, BOLT et bLIP
(`specifications/<langue>/<série>.yaml`) se traduisent élément par élément. Le fichier traduit ne
garde que le texte traduit ; dates, statuts, auteurs, renvois et sources restent dans le fichier
français. Chaque élément porte ses deux empreintes :

```yaml
# chronologie/en/2009.yaml
events:
  - date: "2009-01-03"                 # retrouve l'événement français du même jour
    title: "Genesis block mined"
    text: "Block 0 of Bitcoin is timestamped 18:15:05 UTC. …"
    source_hash: "9e246cbe1208d07d"     # empreinte du titre et du texte français
    translation_hash: "4e56977270504ed5"

# specifications/en/bolt.yaml
entries:
  - id: "BOLT-00"                       # retrouve le document français de même identifiant
    summary: "Entry document of the BOLT specifications. …"
    source_hash: "5d7cad98a596124f"
    translation_hash: "9573cd541faf17be"
```

Un événement se reconnaît à sa date dans son fichier ; deux événements du même jour se
distinguent par leur ordre (`2009-01-03`, puis `2009-01-03#2`). Le statut se calcule comme pour
une définition.

## Les statuts

`python3 scripts/main.py sync` compare chaque paire et lui donne un statut :

| Statut | Ce qui s'est passé | À faire |
|---|---|---|
| à jour | rien n'a changé depuis la dernière synchro | rien |
| manquante | l'entrée française n'a pas de traduction | traduire (si elle est dans le périmètre) |
| en retard | le français a changé, pas l'anglais | reporter la modification en anglais |
| à reporter | l'anglais a changé, pas le français | reporter la modification en français |
| conflit | les deux ont changé | fusionner à la main, puis marquer |
| à marquer | la traduction existe, la synchro n'a jamais été enregistrée | relire, puis marquer |
| absente de la langue d'origine | entrée écrite d'abord en anglais | la traduire en français |
| orpheline | l'entrée source a été supprimée | supprimer ou rattacher la traduction |
| exclue | l'entrée n'a pas de sens dans la langue cible (`exclude` dans `templates/languages.yaml`) | rien |
| en attente | la traduction attend une décision (`pending` dans `templates/languages.yaml`, par slug ou par catégorie) | rien, jusqu'à la décision |

Les statuts se lisent dans les deux sens : « en retard » signale une traduction anglaise à
mettre à jour, « à reporter » une modification anglaise que le français n'a pas encore.

## Les commandes

```bash
python3 scripts/main.py sync                      # tableau par partie : traduites, manquantes, en retard…
python3 scripts/main.py sync --list               # le détail, entrée par entrée (sauf les manquantes)
python3 scripts/main.py sync --list manquante     # les entrées à traduire
python3 scripts/main.py sync --list "en retard"   # un seul statut
python3 scripts/main.py sync --diff coinjoin      # ce qui a changé des deux côtés depuis la synchro
python3 scripts/main.py sync --new adresse-de-reception --title "RECEIVING ADDRESS"
python3 scripts/main.py sync --mark coinjoin      # enregistrer que la paire est à jour
python3 scripts/main.py sync --mark BIP-0032 2009-01-03   # un résumé, un événement de la chronologie
python3 scripts/main.py sync --strict             # échoue s'il reste du travail dans le périmètre
```

`--mark`, `--diff` et `--new` acceptent le slug français, le slug anglais ou l'UUID ; `--mark`
accepte aussi l'identifiant d'un résumé (`BIP-0032`) ou la date d'un événement (`2009-01-03`).

Le livre anglais se génère comme le français, dans `build/en/<édition>/` :

```bash
python3 scripts/main.py build --lang en                       # complet et poche, PDF et EPUB
python3 scripts/main.py build --lang en --edition essentiel --format epub
```

Il ne contient que les entrées traduites. Titres et introductions des parties, noms des
catégories et titres des éditions viennent de `templates/en/book.yaml` ; note de l'auteur,
remerciements et mentions légales de `templates/en/`.

`python3 scripts/main.py check` valide aussi la structure des traductions (métadonnées, version
courte, markdown, images) et affiche une ligne d'état. Une traduction en retard ou manquante ne
fait pas échouer `check` : le français doit pouvoir avancer sans attendre l'anglais. `sync
--strict` sert à vérifier qu'une branche ne laisse rien derrière elle.

## Ce que fait un contributeur

**Je modifie une définition française.**

1. Je modifie `definitions/fr/…`.
2. Si l'entrée a une traduction, `sync` la montre « en retard ». Deux possibilités :
   - je reporte la modification en anglais dans la même pull request, puis
     `sync --mark <slug>` ;
   - ou je laisse la traduction en retard et je le signale dans la pull request. Le statut reste
     visible jusqu'à ce que quelqu'un la mette à jour.
3. Je ne lance jamais `--mark` sur une traduction que je n'ai pas relue : l'empreinte
   affirmerait qu'elle est à jour.

**Je modifie une définition anglaise.**

1. Je modifie `definitions/en/…`.
2. `sync` la montre « à reporter ». Si la modification touche au fond (un fait, un chiffre, une
   explication), je la reporte en français dans la même pull request, ou j'ouvre une issue qui
   la décrit. Si elle ne touche qu'à l'anglais (tournure, coquille), le français n'a rien à
   changer.
3. `sync --mark <slug>` une fois les deux versions d'accord.

**Je modifie la chronologie ou un résumé de spécification.** Même règle que pour une définition :
je reporte la modification dans `chronologie/en/` ou `specifications/en/` (même date, même
identifiant), puis `sync --mark <date ou identifiant>`. Un nouvel événement ou un nouveau document
s'ajoute aussi dans le fichier anglais, à la même place.

**J'ajoute une entrée.** Je la crée en français (voir le README) ; la traduction viendra
ensuite et `sync` la compte comme manquante. Une entrée peut aussi naître en anglais : son
`metadata.yaml` porte alors catégorie et renvois, sans `source_lang`, et `sync` signale qu'elle
manque en français.

**Je supprime ou je fusionne une entrée.** Je supprime aussi sa traduction, dans la même pull
request : une traduction orpheline fait échouer `check`.

**Je traduis une entrée.**

1. `python3 scripts/main.py sync --new <slug-fr> --title "TITRE ANGLAIS"` crée le dossier et son
   `metadata.yaml`.
2. J'écris `definition.md` et `courte.md` en suivant les conventions ci-dessous.
3. `python3 scripts/main.py check`, puis `sync --mark <slug>`.

## Conventions de la version anglaise

- **Terminologie** : celle de Bitcoin Core, des BIP et de Bitcoin Optech. Le
  [glossaire](./glossaire-fr-en.md) fixe les équivalences ; un terme qui n'y est pas se vérifie
  dans ces sources avant d'être employé.
- **Titre et slug** : titre en MAJUSCULES, mêmes formats qu'en français (`RBF - REPLACE-BY-FEE`) ;
  slug tiré du titre anglais, un nombre initial écrit en toutes lettres
  (`fifty-one-percent-attack`). Le dossier de lettre est la première lettre du slug.
- **Registre** : celui du dictionnaire français (phrase d'attaque sans sujet, voix impersonnelle,
  Alice et Bob), en anglais technique naturel, orthographe américaine. Pas de tiret cadratin ni
  demi-cadratin, pas de gras, guillemets droits doubles, séparateur de milliers en virgule.
- **Italique** : il marquait en français les termes anglais (*wallet*, *output*) ; en anglais,
  ces termes s'écrivent en romain. L'italique reste pour la note finale et les mots étrangers.
- **Note finale** : elle se réécrit pour un lecteur anglophone (synonymes, confusions
  fréquentes) ; ce qui ne servait qu'au lecteur français (« en anglais, on dit… ») disparaît.
- **Images** : la traduction réutilise l'image française avec un chemin relatif
  (`![Alt text in English.](../../../fr/c/coinjoin/assets/image-1.png)`) et traduit le texte
  alternatif. Un schéma redessiné en anglais va dans `assets/` du dossier anglais.
- **Version courte** : mêmes règles qu'en français (une ou deux phrases, 45 mots au plus, sans
  liste, lien, image, formule, gras ni titre).
