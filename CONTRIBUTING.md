# Contribuer au *Dictionnaire de Bitcoin*

*English version below.*

Toutes les contributions sont bienvenues : nouveau terme, correction d'une définition, coquille,
traduction. Le README explique comment [ajouter ou modifier une définition](./README.md#demandes-de-modification-et-contributions) ;
la [charte éditoriale](./STYLE_GUIDE.md) fixe les conventions de rédaction.

Avant d'ouvrir une pull request :

```bash
python3 scripts/main.py check
```

## Garder le français et l'anglais synchronisés

Le dictionnaire existe en français (`definitions/fr/`, langue d'origine) et en anglais
(`definitions/en/`, le dictionnaire technique pour l'instant). Chaque fichier anglais garde
l'empreinte de la version française qu'il traduit ; `python3 scripts/main.py sync` liste les
traductions manquantes, en retard ou à reporter. Le détail est dans
[docs/traduction.md](./docs/traduction.md).

- **Vous modifiez le français** : si l'entrée a une traduction, reportez la modification en
  anglais dans la même pull request puis lancez `python3 scripts/main.py sync --mark <slug>`.
  Si vous ne pouvez pas, dites-le dans la pull request : la traduction restera signalée « en
  retard » jusqu'à sa mise à jour.
- **Vous modifiez l'anglais** : si la modification touche au fond (fait, chiffre, explication),
  reportez-la en français dans la même pull request, ou décrivez-la dans une issue. Une
  correction de langue anglaise seule n'a rien à reporter. Lancez ensuite `sync --mark <slug>`.
- **Vous supprimez une entrée** : supprimez aussi sa traduction.
- **Ne marquez jamais** une traduction que vous n'avez pas relue : `--mark` affirme qu'elle est à
  jour.

---

# Contributing to the *Bitcoin Dictionary*

Contributions of every kind are welcome: a new term, a fix to a definition, a typo, a
translation. The dictionary is written in French first; the English version currently covers
the technical dictionary (`definitions/en/`).

Run this before opening a pull request:

```bash
python3 scripts/main.py check
```

## Keeping French and English in sync

Each English entry records the fingerprint of the French version it translates.
`python3 scripts/main.py sync` lists translations that are missing, outdated, or ahead of the
French. Details (in French): [docs/traduction.md](./docs/traduction.md).

- **You edit the French**: if the entry has a translation, update the English in the same pull
  request, then run `python3 scripts/main.py sync --mark <slug>`. If you can't, say so in the
  pull request: the translation stays flagged as outdated until someone updates it.
- **You edit the English**: if the change affects substance (a fact, a number, an explanation),
  port it to the French in the same pull request, or describe it in an issue. A pure English
  wording fix has nothing to port. Then run `sync --mark <slug>`.
- **You delete an entry**: delete its translation too.
- **Never mark** a translation you haven't reviewed: `--mark` records that it is up to date.

English entries follow the French dictionary's conventions, in natural technical English with
Bitcoin Core and BIP terminology; the [glossary](./docs/glossaire-fr-en.md) fixes the standard
terms.
