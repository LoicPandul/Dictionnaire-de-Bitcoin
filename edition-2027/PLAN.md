# Édition 2027 — plan de travail

Branche : `feat/edition-2027`. Ce fichier est la mémoire du chantier : on le relit avant de reprendre, on coche au fil de l'eau, on note ici chaque décision.

**Phase en cours : 5 et 7 (termes quantiques et Nostr, visuels), en parallèle de la phase 4 (chronologie, personnes)**

Légende : `[x]` fait · `[~]` en cours · `[ ]` à faire · `[!]` bloqué ou à trancher par Loïc

---

## Décisions d'architecture

Ces choix conditionnent tout le reste. Chacun est réversible, mais il faut le changer ici avant de le changer dans le code.

1. **Les slugs et les dossiers ne bougent pas.** Toute entrée, qu'elle soit technique, une entreprise, une personne ou un BIP, reste dans `definitions/fr/<lettre>/<slug>/`. Le site (`feat/site-dictionnaire`) continue de lire ce dossier.
2. **La partie du livre se déduit de la catégorie.** Pas de nouveau champ dans `metadata.yaml` : `templates/parts.yaml` range chaque catégorie dans une partie (`technique`, `ecosysteme`, `personnes`, `specifications`), avec son pictogramme et son nom en casse de phrase (`display`). Une catégorie n'appartient qu'à une partie.
3. **`templates/categories.yaml` garde son format** (liste `  - NOM` précédée de commentaires), parce que le site lit les commentaires comme description de catégorie.
4. **Version courte = fichier `courte.md`** à côté de `definition.md`, dans chaque dossier, pour toutes les parties. Une ou deux phrases, 45 mots au plus, sans liste, image, formule, lien ni gras. `scripts/validators/sync_checker.py` vérifie que chaque `definition.md` a sa `courte.md` et inversement.
5. **Les BIP, BOLT, bLIP et NIP sortent du dictionnaire technique.** Leur partie se construit depuis `specifications/<bip|bolt|blip|nip>.yaml` (numéro, titre, statut, type, résumé en français, lien, `related`). Quand une définition développée existe (catégories `BIP`, `BOLT`, `BLIP`), l'entrée YAML pointe vers son slug et l'édition complète imprime le texte développé sous le résumé. Les termes génériques (`bip`, `bolt`, `blip`, `nip`) restent dans le dictionnaire technique.
6. **Chronologie = `chronologie/fr/*.yaml`**, un fichier par année à partir de 2009 et `avant-2009.yaml`. Chaque événement : `date` (ISO), `title`, `text`, `related` (slugs), `sources` (au moins deux URL indépendantes).
7. **Deux éditions depuis la même source** (`templates/editions.yaml`) : `complete` (définitions développées, BIP et BOLT avec leur texte développé) et `essentiel` (versions courtes partout, résumés seuls pour les spécifications). Formats : PDF broché 5,5 × 8,5 po, PDF relié 7 × 10 po, EPUB 3.
8. **Sorties de build dans `build/`** (ignoré par git). Les PDF 2026 à la racine du dépôt ne sont pas touchés : Loïc décide s'il les remplace à la sortie 2027.
9. **Outils de build locaux** dans `.tools/` (ignoré par git) : Tectonic 0.17 (moteur XeTeX autonome, sans sudo), epubcheck 5.4.0, et un environnement Python (`.tools/venv`). `xelatex` système reste prioritaire s'il existe. Avec Tectonic, le générateur lance une passe par processus (`--reruns 0`) jusqu'à stabilité du `.aux` : les recompilations internes de Tectonic gonflaient des lignes de plusieurs dizaines de points (936 pages au lieu de 694).
10. **Skills hors du dépôt** : `~/.claude/skills/dictionnaire-redaction`, `dictionnaire-definition`, `schemas-dictionnaire`. Rien de ces skills ne va dans ce dépôt public.
11. **Charte 2027** (`design/charte-2027.md`, branche `feat/couverture-2027`, commit `f5a3a13b`) : appliquée au PDF (Archivo en instances statiques, Atkinson Hyperlegible Mono, Fira Math, vedettes sans cartouche, catégorie en casse de phrase avec pictogramme de 3 mm, « Voir aussi »), aux schémas et aux pictogrammes. Polices copiées depuis le commit `46c954c2` de la même branche (fichiers identiques, aucun conflit à la fusion).

---

## Phase 0 — Cadrage

- [x] Inventaire : 1 408 définitions, 19 catégories, 52 définitions illustrées (54 PNG), générateurs PDF XeLaTeX, aucun EPUB.
- [x] Décisions d'architecture ci-dessus.

## Phase 1 — Outils et ménage du dépôt

- [x] Outils locaux dans `.tools/` et détection dans `config.py`.
- [x] `main.py` en ligne de commande (`check`, `fix`, `build`, `index`, `stats`, `info`) ; le menu reste pour un lancement sans argument.
- [x] Modèle de livre (`scripts/core/book.py`) : parties, éditions, renvois limités aux entrées présentes dans l'édition.
- [x] Générateur PDF multi-parties, broché et relié dans le même code (fin du remplacement de chaînes de l'ancien `pdf_hardcover_generator.py`, supprimé).
- [x] Générateur EPUB 3 (formules en MathML, légendes, `toc.ncx`) : epubcheck 0 erreur, 0 avertissement sur les deux éditions.
- [x] `sync_checker.py` et `content_validator.py` (spécifications, chronologie).
- [x] Ménage :
  - [x] `Dictionary.load` ne supprime plus les dossiers vides au chargement.
  - [x] `metadata_validator` ne réécrit plus rien pendant la validation (`fix` à part).
  - [x] `OUTPUT_INDEX` pointe vers `INDEX.md` (plus de doublon `index.md` sous Linux).
  - [x] Le badge du README se met à jour (la regex ne correspondait plus au badge).
  - [x] Les images avec texte alternatif s'impriment enfin dans le PDF (l'ancienne regex n'acceptait que `![]()`, le PDF 2026 imprimait « !Coinjoin à cinq… » à la place de l'image).
  - [x] Les URL ne mangent plus la ponctuation ni `\end{quote}` (erreur de compilation que le `nonstopmode` masquait).
  - [x] Polices 2026 retirées (Fira Code, CMU Serif) ; Archivo et Atkinson Hyperlegible Mono ajoutées.
  - [x] README des scripts à jour.
  - [ ] README racine : structure du dépôt et lien vers les nouvelles parties (à faire en fin de chantier).

## Phase 2 — Catégories et parties

- [x] Analyse des 1 408 entrées et nouvelle taxonomie : 55 catégories (technique 33, écosystème 12, personnes 6, spécifications 4), aucune au-dessus de 80. Détail et cas limites : `edition-2027/taxonomie.md`, reclassement ligne à ligne : `edition-2027/reclassement.tsv`.
- [x] Retouche de l'orchestrateur : catégorie ECASH (Cashu, Fedimint) créée dès 2027, Loïc les cite expressément.
- [x] Reclassement appliqué (697 métadonnées modifiées).
- [~] Pictogrammes des 55 catégories au style de la charte (section 7) : redessin en cours. Les 36 pictogrammes provisoires (Lucide) seront remplacés.

## Phase 3 — Versions courtes

- [x] `courte.md` pour 100 % des entrées (1 408), voix de Loïc, 31,9 mots en moyenne, 45 au plus.
- [x] `python3 scripts/main.py check` : versions courtes conformes, mêmes termes que les versions développées.
- [ ] 271 problèmes repérés dans les définitions développées pendant la rédaction (`/tmp/ed2027/courtes/lot-*-signalements.md`, à recopier dans `edition-2027/signalements.md`) : passe de corrections vérifiées à lancer.

## Phase 4 — Nouvelles parties

### Entreprises, applications et logiciels
- [x] Sortie du dictionnaire technique par reclassement (195 entrées, 12 catégories).
- [!] Logos et captures : voir « Droits sur les logos et les captures ».

### Personnes
- [~] Limite éditoriale et liste (`edition-2027/personnes-candidats.md`, tâche relancée après la limite d'usage).
- [x] Reclassement des personnes présentes (`nakamoto-satoshi`, `finney-hal`, `bitcoin-jesus`).
- [ ] Nouvelles fiches, rédigées et vérifiées avec `dictionnaire-definition`.

### Chronologie
- [~] Collecte depuis le fil bitcointalk 5187275, chaque date recoupée par une seconde source (4 lots relancés après la limite d'usage ; `avant-2009`, `2009` et `2021` déjà prêts en brouillon).
- [ ] Fusion dans `chronologie/fr/`, validation, commit.

### BIP, BOLT, bLIP, NIP
- [x] `specifications/bip.yaml` (214 BIP, dépôt `bitcoin/bips` au commit `100ba872`).
- [x] `specifications/bolt.yaml` (13) et `specifications/blip.yaml` (15).
- [x] `specifications/nip.yaml` (100 NIP, `related` vers les entrées techniques existantes).
- [ ] 33 écarts entre des définitions de BIP, BOLT et bLIP et leurs spécifications (`/tmp/ed2027/specs/*-ecarts.md`) : à corriger avec la passe de corrections.

## Phase 5 — Termes manquants

- [x] Liste des termes : 30 quantiques, 24 concepts Nostr, 12 applications, 7 personnes (`edition-2027/termes-quantique-nostr.md`).
- [~] Démonstration de la chaîne sur 5 termes quantiques (CRQC, Q-DAY, ALGORITHME DE GROVER, P2MR, SIGNATURE DE LAMPORT).
- [ ] Les autres termes quantiques et Nostr, rédigés par `dictionnaire-definition`, vérifiés par verificator.
- [~] Repérage dans bitcoindev, Delving Bitcoin et Optech (`edition-2027/termes-candidats.md`, tâche relancée).
- [ ] `templates/pending_terms.yaml` alimenté avec ce qui n'est pas rédigé.

## Phase 6 — Skills

- [x] `dictionnaire-redaction` : charte d'écriture (registre du dictionnaire, phrase d'attaque, version courte, typographie, anti-AI-slop du loicizer).
- [x] `dictionnaire-definition` : terme → doublons → recherche obligatoire (Bitcoin Core, BIP, Optech, bitcoindev, Delving) → rédaction courte et développée → verificator → métadonnées → `check`. Scripts `doublons.py`, `nouvelle_entree.py`, `renvois.py`.
- [x] `schemas-dictionnaire` : fork de `schemas` sur la charte officielle (`f5a3a13b`) : classes de rôle, version N&B par classe `nb`, exports `image-N.png` (couleur), `image-N-nb.pdf` (vectoriel) et `image-N-nb.png` (2 560 px), SVG source, légende = texte alternatif. Scripts `rendre.mjs` et `deposer.py`.
- [x] `verificator` : dossier de travail corrigé pour Linux (`$LOCALAPPDATA` vide donnait `/Temp`).
- [~] Démonstration sur 5 nouveaux termes, chaîne complète (voir phase 5).

## Phase 7 — Visuels

Objectif : environ un visuel toutes les 3 ou 4 définitions, là où il aide.

- [~] Plan des visuels (`edition-2027/visuels/`) : schémas par priorité, logos et captures.
- [ ] Production des schémas avec `schemas-dictionnaire`, par lots, en commençant par la priorité A.
- [ ] Refaire au style 2027 les 54 images de 2026 (noir et blanc, Arial).
- [!] Logos et captures : attendent la décision sur les droits.

## Phase 8 — EPUB et Amazon KDP

- [x] EPUB validé par epubcheck (deux éditions).
- [ ] Dossier `edition-2027/kdp/` : métadonnées, description, mots-clés, catégories, prix conseillé, étapes Kindle et papier.

## Phase 9 — Ce que le site devra suivre

- [ ] Note de compatibilité (section ci-dessous) à transmettre au worker de `feat/site-dictionnaire` en fin de chantier.

---

## Budget de pages (à trancher sur pièces)

Premier build complet à la charte, sans chronologie, sans nouvelles fiches de personnes ni nouveaux termes : **broché 694 pages, relié 566 pages**. KDP limite le relié à 550 pages et le broché à 828 (marge intérieure portée automatiquement à 22,5 mm au-delà de 700 pages). La charte prévoit deux options si le relié dépasse 540 pages : passer le relié en 9 / 11,5 pt (environ −5 %) ou le publier en deux volumes. L'édition `essentiel` reste loin de ces limites.

## Limite éditoriale : qui entre dans le dictionnaire des personnes

À compléter avec le résultat de la tâche « Liste des personnes » (critères proposés : travail cité par le livre blanc ou brique directe de Bitcoin ; rôle documenté dans le développement de Bitcoin, de Lightning ou d'une surcouche ; penseur fondateur invoqué par le discours Bitcoin, école autrichienne et cypherpunks ; acteur central d'un événement de la chronologie. Exclus : influenceurs, investisseurs, responsables politiques, fondateurs d'autres cryptomonnaies sans rôle dans Bitcoin).

## Droits sur les logos et les captures d'écran

Le livre est vendu, et son texte est sous licence CC BY-NC-SA 4.0. Deux régimes différents s'appliquent aux images de tiers :

- **Logos** : ce sont des marques, souvent des œuvres protégées. Les citer par leur nom est libre (usage nominatif) ; reproduire le logo dans un livre vendu demande en pratique l'accord du titulaire ou des conditions d'usage qui le permettent (kit presse, charte de marque). Beaucoup de kits presse autorisent l'usage éditorial mais interdisent la modification et l'usage commercial : une lecture au cas par cas est nécessaire.
- **Captures d'écran** : l'interface d'un logiciel est une œuvre. Un logiciel libre (licence MIT, GPL…) couvre son code ; la reproduction de son interface dans un livre est en général tolérée et défendable au titre de la citation, mais pas garantie. Un logiciel propriétaire demande l'accord de l'éditeur.
- **Incompatibilité de licence** : une image de tiers ne peut pas être placée sous CC BY-NC-SA par le dictionnaire. Chaque image de tiers doit porter sa mention de source et être exclue explicitement de la licence du livre (mention dans les pages légales et dans `LICENSE.md`).
- **Recommandation** : pas de logos de tiers dans le livre imprimé sans autorisation écrite ; captures limitées aux logiciels libres, faites par Loïc lui-même, créditées, et listées dans une page « Crédits des images ». Le plan des visuels note la source et les conditions trouvées pour chaque candidat (`edition-2027/visuels/plan-logos-captures.tsv`).

## Compatibilité avec le site

Le site (`feat/site-dictionnaire`) lit `definitions/fr` avec un parseur YAML minimal. Ce qui change pour lui :

- **Nouveau fichier `courte.md`** dans chaque dossier : version courte, un paragraphe. Utilisable pour les descriptions, les aperçus et les cartes de survol (aujourd'hui calculées depuis `definition.md`).
- **Catégories** : 55 au lieu de 19, mêmes commentaires de description dans `templates/categories.yaml`. Nouveau `templates/parts.yaml` : partie de chaque catégorie, pictogramme et nom en casse de phrase (`display`). Le site peut séparer les entrées par partie (technique, écosystème, personnes, spécifications) sans nouveau champ dans `metadata.yaml`.
- **Pictogrammes** : `assets/pictograms/<slug>.svg` en `currentColor` (charte, section 7), un par catégorie.
- **Images** : en plus de `image-N.png` (couleur, à afficher), un schéma 2027 a `image-N-nb.pdf`, `image-N-nb.png` (livre imprimé, à ignorer) et `image-N.svg` (source). Seul `image-N.png` est déclaré dans `assets:` de `metadata.yaml`. Le texte alternatif sert aussi de légende.
- **Nouvelles sources** : `specifications/*.yaml` (BIP, BOLT, bLIP, NIP) et `chronologie/fr/*.yaml`, pour des pages dédiées si le site le souhaite.
- **Slugs inchangés**, aucune URL ne casse. Les nouvelles entrées (quantique, Nostr, personnes) ajoutent des slugs.

## Questions ouvertes pour Loïc

- Budget de pages du relié (voir plus haut).
- Logos et captures dans le livre vendu (voir plus haut).
- Le titre de l'édition `essentiel` et son ISBN éventuel (aujourd'hui : même titre, sous-titre « L'essentiel en définitions courtes », sans ISBN).

## Journal

- 2026-10-25 : démarrage, inventaire, décisions d'architecture. Taxonomie, spécifications, versions courtes, scripts, EPUB, skills. Limite d'usage de l'API vers 13 h 20 : quatre tâches relancées en reprise. Charte officielle reçue (`f5a3a13b`) : skill de schémas mis en conformité, mise en page du livre refaite à la charte, bogue de Tectonic contourné.
