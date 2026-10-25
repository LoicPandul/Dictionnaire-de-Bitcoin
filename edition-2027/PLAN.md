# Édition 2027 — plan de travail

Branche : `feat/edition-2027`. Ce fichier est la mémoire du chantier : on le relit avant de reprendre, on coche au fil de l'eau, on note ici chaque décision.

**Phase en cours : 0 (cadrage)**

Légende : `[x]` fait · `[~]` en cours · `[ ]` à faire · `[!]` bloqué (raison indiquée)

---

## Décisions d'architecture

Ces choix conditionnent tout le reste. Chacun est réversible, mais il faut le changer ici avant de le changer dans le code.

1. **Les slugs et les dossiers ne bougent pas.** Toute entrée, qu'elle soit technique, une entreprise, une personne ou un BIP, reste dans `definitions/fr/<lettre>/<slug>/`. Le site (`feat/site-dictionnaire`) continue de lire ce dossier sans rien casser.
2. **La partie du livre se déduit de la catégorie.** Pas de nouveau champ dans `metadata.yaml` : `templates/parts.yaml` range chaque catégorie dans une partie (`technique`, `ecosysteme`, `personnes`, `specifications`) et lui associe son pictogramme. Une catégorie n'appartient qu'à une partie.
3. **`templates/categories.yaml` garde son format** (liste `  - NOM` précédée de commentaires), parce que le site lit les commentaires comme description de catégorie.
4. **Version courte = fichier `courte.md`** à côté de `definition.md`, dans chaque dossier, pour toutes les parties. Une ou deux phrases, 45 mots au plus, sans liste, sans image, sans formule. `scripts/validators/sync_checker.py` vérifie que chaque `definition.md` a sa `courte.md` et inversement.
5. **Les BIP, BOLT, bLIP et NIP sortent du dictionnaire technique.** Leur partie se construit depuis `specifications/<bip|bolt|blip|nip>.yaml` (numéro, titre, statut, type, résumé en français, lien). Quand une définition développée existe déjà (catégories `BIP`, `BOLT`, `BLIP`), l'entrée YAML pointe vers son slug et le livre complet imprime le texte développé sous le résumé. Les termes génériques (`bip`, `bolt`, `blip`, `nip`) restent dans le dictionnaire technique.
6. **Chronologie = `chronologie/fr/*.yaml`**, un fichier par année à partir de 2009 et `avant-2009.yaml`. Chaque événement : `date` (ISO, précision jour quand elle est connue), `title`, `text`, `related` (slugs du dictionnaire), `sources` (au moins deux URL indépendantes).
7. **Deux éditions générées depuis la même source** : `complete` (toutes les parties, définitions développées) et `essentiel` (dictionnaire technique en version courte, plus les autres parties en version courte). Formats : PDF broché 5,5 × 8,5 po, PDF relié 7 × 10 po, EPUB 3.
8. **Sorties de build dans `build/`** (ignoré par git). Les PDF 2026 à la racine du dépôt ne sont pas touchés : Loïc décide s'il remplace ces fichiers au moment de la sortie 2027.
9. **Outils de build locaux** dans `.tools/` (ignoré par git) : Tectonic (moteur XeTeX autonome, sans sudo) et epubcheck. `scripts/config.py` les trouve tout seul ; `xelatex` système reste prioritaire s'il existe.
10. **Skills hors du dépôt** : `~/.claude/skills/dictionnaire-redaction`, `~/.claude/skills/dictionnaire-definition`, `~/.claude/skills/schemas-dictionnaire`. Rien de ces skills ne va dans ce dépôt public.

---

## Phase 0 — Cadrage

- [x] Inventaire : 1 408 définitions, 19 catégories, 52 définitions illustrées (54 PNG), générateurs PDF XeLaTeX, aucun EPUB.
- [x] Décisions d'architecture ci-dessus.
- [ ] Commit du plan.

## Phase 1 — Outils et ménage du dépôt

- [ ] Outils locaux dans `.tools/` (Tectonic, epubcheck) et détection dans `config.py`.
- [ ] `main.py` en ligne de commande non interactive (`python3 scripts/main.py build --edition complete --format pdf,epub`), le menu reste pour un lancement sans argument.
- [ ] Modèle de livre (`scripts/core/book.py`) : parties, catégories, éditions, renvois qui ne pointent que vers des entrées présentes dans l'édition.
- [ ] Générateur PDF multi-parties (intertitres de partie, dictionnaire technique, écosystème, personnes, chronologie, BIP, BOLT, bLIP, NIP).
- [ ] Générateur EPUB 3 (formules en MathML), validé par epubcheck.
- [ ] `sync_checker.py` : mêmes termes dans `definition.md` et `courte.md`, contraintes de la version courte.
- [ ] Ménage :
  - [ ] `Dictionary.load` supprime les dossiers vides au chargement (effet de bord destructif) : à retirer.
  - [ ] `metadata_validator` réécrit les `metadata.yaml` pendant la validation : séparer validation et correction.
  - [ ] `OUTPUT_INDEX` pointe vers `index.md` alors que le fichier suivi est `INDEX.md` : sur Linux, le build crée un doublon.
  - [ ] `pdf_hardcover_generator` remplace des chaînes dans le LaTeX produit : passer la géométrie en paramètre.
  - [ ] Police `Arial` codée en dur : repli sur Liberation Sans (métriques identiques) quand Arial manque.
  - [ ] Dossiers `assets/` qui contiennent des `definition.md` et `metadata.yaml` (slugs `*-assets`, faux positifs de recherche) : vérifier.
  - [ ] README et `scripts/README.md` à jour.

## Phase 2 — Catégories et parties

- [ ] Analyse des 1 408 entrées : catégories trop chargées, surcouches noyées dans `COUCHE SUPÉRIEURE`, logiciels et entreprises éparpillés dans `PORTEFEUILLE`, `MINAGE`, `LIGHTNING NETWORK`, `CONFIDENTIALITÉ`, `RÉSEAU`.
- [ ] Nouvelle taxonomie dans `templates/categories.yaml` et `templates/parts.yaml`.
- [ ] Reclassement des 1 408 entrées (script, un seul commit).
- [ ] Pictogrammes des nouvelles catégories (SVG et PDF dans `assets/pictograms/`). À reprendre si la charte 2027 change le style.

## Phase 3 — Versions courtes

- [ ] `courte.md` pour 100 % des entrées, rédigée à partir de la définition actuelle, voix de Loïc, règles anti-AI-slop.
- [ ] Relecture croisée : la version courte ne dit rien que la version développée ne dit pas.
- [ ] `sync_checker.py` passe.

## Phase 4 — Nouvelles parties

### Entreprises, applications et logiciels
- [ ] Sortie du dictionnaire technique par reclassement (phase 2).
- [ ] Logos : voir phase 7 et la question des droits.

### Personnes
- [ ] Limite éditoriale (ci-dessous) validée.
- [ ] Reclassement des personnes déjà présentes (`nakamoto-satoshi`, `finney-hal`, `bitcoin-jesus`…).
- [ ] Nouvelles fiches, vérifiées.

### Chronologie
- [ ] Collecte depuis le fil bitcointalk 5187275, chaque date recoupée par une seconde source indépendante.
- [ ] Préhistoire (1976 à 2008) : cryptographie à clé publique, cypherpunks, monnaies électroniques.
- [ ] 2009 à aujourd'hui, année par année.

### BIP, BOLT, bLIP, NIP
- [ ] `specifications/bip.yaml` depuis le dépôt `bitcoin/bips`.
- [ ] `specifications/bolt.yaml` et `specifications/blip.yaml` depuis `lightning/bolts` et `lightning/blips`.
- [ ] `specifications/nip.yaml` depuis `nostr-protocol/nips`.

## Phase 5 — Termes manquants

- [ ] Informatique quantique utile à Bitcoin (CRQC, Shor, Grover, Q-day, signatures post-quantiques, BIP-0360…), vérifiés par verificator.
- [ ] Nostr et son écosystème, vérifiés par verificator.
- [ ] Repérage dans bitcoindev et Delving Bitcoin : liste candidate, puis rédaction des termes retenus.
- [ ] `templates/pending_terms.yaml` alimenté avec ce qui n'est pas rédigé.

## Phase 6 — Skills

- [ ] `dictionnaire-redaction` : charte d'écriture (STYLE_GUIDE, loicizer, anti-AI-slop), formats `definition.md`, `courte.md`, `metadata.yaml`.
- [ ] `dictionnaire-definition` : un terme en entrée → recherche (code de Bitcoin Core, BIP, Optech, bitcoindev, Delving) → rédaction courte et développée → verificator → métadonnées validées par les scripts du dépôt.
- [ ] `schemas-dictionnaire` : fork de `schemas` avec le design system 2027. [!] Attend `design/charte-2027.md` (branche `feat/couverture-2027`).
- [ ] Démonstration sur 5 nouveaux termes, chaîne complète.

## Phase 7 — Visuels

Objectif : environ un visuel toutes les 3 ou 4 définitions, là où il aide (schéma technique, logo, capture d'écran).

- [ ] Plan des visuels : pour chaque entrée candidate, le type de visuel et ce qu'il doit montrer (ne dépend pas de la charte).
- [!] Production des schémas avec `schemas-dictionnaire` : attend la charte 2027.
- [ ] Logos et captures : attend la décision sur les droits (ci-dessous).

## Phase 8 — EPUB et Amazon KDP

- [ ] EPUB validé par epubcheck.
- [ ] Dossier `edition-2027/kdp/` : métadonnées, description, mots-clés, catégories, prix conseillé, étapes Kindle et papier. Loïc publie lui-même.

## Phase 9 — Ce que le site devra suivre

À transmettre au worker de `feat/site-dictionnaire` :

- [ ] Note de compatibilité (section ci-dessous) à jour en fin de chantier.

---

## Limite éditoriale : qui entre dans le dictionnaire des personnes

À compléter en phase 4.

## Droits sur les logos et les captures d'écran

À compléter en phase 7.

## Compatibilité avec le site

À compléter au fil des phases.

## Questions ouvertes pour Loïc

Aucune pour l'instant.

## Journal

- 2026-10-25 : démarrage, inventaire, décisions d'architecture.
