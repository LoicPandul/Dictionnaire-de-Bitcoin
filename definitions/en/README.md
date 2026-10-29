# Bitcoin Dictionary: English version

This folder holds the English translation of the *Dictionnaire de Bitcoin* by Loïc Morel. The
dictionary is written in French first (`definitions/fr/`); this folder holds the English version
of its four parts (technical dictionary; companies, applications, and software; people;
specifications). The timeline and the specification summaries are translated in
`chronologie/en/` and `specifications/en/`.

Each entry is a folder named after its English slug, filed under its first letter:

* `definition.md`: the full definition;
* `courte.md`: the short version, one or two sentences (the file keeps its French name so that
  both languages share the same tooling);
* `metadata.yaml`: the shared UUID, the English title and slug, and the fingerprint of the French
  version this translation was made from (`source_*` fields).

Category, cross-references and images live in the French entry and apply to both languages.
Diagrams are reused from the French entry until they are redrawn in English.

To see which translations are missing or outdated, run `python3 scripts/main.py sync`. To build
the English books (PDF and EPUB, in `build/en/`), run `python3 scripts/main.py build --lang en`. Before
editing an entry that exists in both languages, read [CONTRIBUTING.md](../../CONTRIBUTING.md#contributing-to-the-bitcoin-dictionary).

Licensed under [CC BY-NC-SA 4.0](../../LICENSE.md).
