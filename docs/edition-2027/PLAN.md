# Édition 2027 — plan de travail

Branche : `feat/edition-2027`. Ce fichier est la mémoire du chantier : on le relit avant de reprendre, on coche au fil de l'eau, on note ici chaque décision.

**Chantier terminé le 2026-10-27, sauf les points `[!]` qui attendent une décision de Loïc.** Dossier de travail durable des sous-tâches : `~/.local/share/dico-2027/` (hors dépôt ; `/tmp` est vidé au redémarrage).

Légende : `[x]` fait · `[~]` en cours · `[ ]` à faire · `[!]` bloqué ou à trancher par Loïc

---

## Décisions d'architecture

Ces choix conditionnent tout le reste. Chacun est réversible, mais il faut le changer ici avant de le changer dans le code.

1. **Les slugs et les dossiers ne bougent pas.** Toute entrée, qu'elle soit technique, une entreprise, une personne ou un BIP, reste dans `definitions/fr/<lettre>/<slug>/`. Le site (`feat/site-dictionnaire`) continue de lire ce dossier.
2. **La partie du livre se déduit de la catégorie.** Pas de nouveau champ dans `metadata.yaml` : `templates/parts.yaml` range chaque catégorie dans une partie (`technique`, `ecosysteme`, `personnes`, `specifications`), avec son pictogramme et son nom en casse de phrase (`display`). Une catégorie n'appartient qu'à une partie.
3. **`templates/categories.yaml` garde son format** (liste `  - NOM` précédée de commentaires), parce que le site lit les commentaires comme description de catégorie.
4. **Version courte = fichier `courte.md`** à côté de `definition.md`, dans chaque dossier, pour toutes les parties. Une ou deux phrases, 45 mots au plus, sans liste, image, formule, lien ni gras. `scripts/validators/sync_checker.py` vérifie que chaque `definition.md` a sa `courte.md` et inversement.
5. **Les BIP, BOLT et bLIP sortent du dictionnaire technique.** Leur partie se construit depuis `specifications/fr/<bip|bolt|blip>.yaml` (numéro, titre, statut, type, résumé en français, lien, `related`). Quand une définition développée existe (catégories `BIP`, `BOLT`, `BLIP`), l'entrée YAML pointe vers son slug et l'édition complète imprime le texte développé sous le résumé. Les termes génériques (`bip`, `bolt`, `blip`, `nip`) restent dans le dictionnaire technique.
6. **Chronologie = `chronologie/fr/*.yaml`**, un fichier par année à partir de 2009 et `avant-2009.yaml`. Chaque événement : `date` (ISO), `title`, `text`, `related` (slugs), `sources` (au moins deux URL indépendantes).
7. **Deux éditions depuis la même source** (`templates/editions.yaml`) : `complete` (définitions développées, BIP et BOLT avec leur texte développé) et `essentiel` (poche : définitions courtes techniques et écosystème seulement, depuis le 27/10). Formats : complet broché couleur 7 × 10 po, poche noir et blanc 5 × 8 po, EPUB 3 ; plus de relié ni de tomes.
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
- [x] Générateur PDF multi-parties, un seul code pour le broché couleur et le poche (fin du remplacement de chaînes de l'ancien `pdf_hardcover_generator.py`, supprimé).
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
  - [x] README racine : structure du dépôt 2027, parties, versions courtes (chiffres à rafraîchir au dernier build).

## Phase 2 — Catégories et parties

- [x] Analyse des 1 408 entrées et nouvelle taxonomie : 55 catégories (technique 33, écosystème 12, personnes 6, spécifications 4), aucune au-dessus de 80. Détail et cas limites : `docs/edition-2027/taxonomie.md`, reclassement ligne à ligne : `docs/edition-2027/reclassement.tsv`.
- [x] Retouche de l'orchestrateur : catégorie ECASH (Cashu, Fedimint) créée dès 2027, Loïc les cite expressément.
- [x] Reclassement appliqué (697 métadonnées modifiées).
- [x] Pictogrammes des 56 catégories redessinés à la charte (section 7), y compris APPLICATION NOSTR.

## Phase 3 — Versions courtes

- [x] `courte.md` pour 100 % des entrées (1 408), voix de Loïc, 31,9 mots en moyenne, 45 au plus.
- [x] `python3 scripts/main.py check` : versions courtes conformes, mêmes termes que les versions développées.
- [x] 271 problèmes repérés pendant la rédaction des courtes, recopiés dans `docs/edition-2027/signalements.md` avec les écarts de spécifications (278 lignes), plus 4 signalés par les schémas : vérifiés un par un à la source (lots C1 à C9, journaux dans `~/.local/share/dico-2027/ed2027/corrections/`), corrigés quand le signalement était prouvé. Points laissés à Loïc : section « Questions ouvertes ».

## Phase 4 — Nouvelles parties

### Entreprises, applications et logiciels
- [x] Sortie du dictionnaire technique par reclassement (195 entrées, 12 catégories).
- [x] Logos et captures : gardés, crédités sous chaque image (champ `credit` de `assets:`) et exclus de la licence dans `LICENSE.md` (décision de Loïc du 27/10).

### Personnes
- [x] Limite éditoriale et liste (`docs/edition-2027/personnes-candidats.md`, 151 candidats, 144 retenues en 13 lots).
- [x] Reclassement des personnes présentes (`nakamoto-satoshi`, `finney-hal`, `bitcoin-jesus`).
- [x] 152 nouvelles fiches (lots P1 à P13), rédigées et vérifiées avec `dictionnaire-definition` (rapports `verification-P*.md`), avec leurs renvois. Retenue de l'orchestrateur : les fiches suivent l'usage public de la personne pour son nom ; la fiche de Mara van der Laan est écrite sans pronom genré en attendant le choix de Loïc.

### Chronologie
- [x] Collecte depuis le fil bitcointalk 5187275, chaque date recoupée par une seconde source.
- [x] Fusion dans `chronologie/fr/` (715 événements de 1976 à 2026), validation, commit ; écartés faute de recoupement : `docs/edition-2027/chronologie-ecartes.md`.

### BIP, BOLT, bLIP, NIP
- [x] `specifications/fr/bip.yaml` (214 BIP, dépôt `bitcoin/bips` au commit `100ba872`).
- [x] `specifications/fr/bolt.yaml` (13) et `specifications/fr/blip.yaml` (15).
- [x] ~~`specifications/fr/nip.yaml` (100 NIP)~~ : retiré le 27/10, Nostr n'étant pas Bitcoin.
- [x] 33 écarts entre des définitions de BIP, BOLT et bLIP et leurs spécifications (`docs/edition-2027/ecarts-specifications.md`) : vérifiés et corrigés avec la passe de corrections.

## Phase 5 — Termes manquants

- [x] Liste des termes : 30 quantiques, 24 concepts Nostr, 12 applications, 7 personnes (`docs/edition-2027/termes-quantique-nostr.md`).
- [x] Démonstration de la chaîne sur 5 termes quantiques (CRQC, Q-DAY, ALGORITHME DE GROVER, P2MR, SIGNATURE DE LAMPORT), avec 3 schémas.
- [x] Les 25 autres termes quantiques, les 24 concepts Nostr et les 11 applications Nostr, rédigés par `dictionnaire-definition`, vérifiés par verificator (rapports `verification-<lot>.md`), déposés et commités.
- [x] Repérage dans bitcoindev, Delving Bitcoin et Optech (`docs/edition-2027/termes-candidats.md`, 150 candidats).
- [x] Les 18 candidats de priorité A rédigés par `dictionnaire-definition` et vérifiés (lots K1 et K2).
- [x] `templates/fr/pending_terms.yaml` : les 132 candidats B et C, avec catégorie et raison.

## Phase 6 — Skills

- [x] `dictionnaire-redaction` : charte d'écriture (registre du dictionnaire, phrase d'attaque, version courte, typographie, anti-AI-slop du loicizer).
- [x] `dictionnaire-definition` : terme → doublons → recherche obligatoire (Bitcoin Core, BIP, Optech, bitcoindev, Delving) → rédaction courte et développée → verificator → métadonnées → `check`. Scripts `doublons.py`, `nouvelle_entree.py`, `renvois.py`.
- [x] `schemas-dictionnaire` : fork de `schemas` sur la charte officielle (`f5a3a13b`) : classes de rôle, version N&B par classe `nb`, exports `image-N.png` (couleur), `image-N-nb.pdf` (vectoriel) et `image-N-nb.png` (2 560 px), SVG source, légende = texte alternatif. Scripts `rendre.mjs` et `deposer.py`.
- [x] `verificator` : dossier de travail corrigé pour Linux (`$LOCALAPPDATA` vide donnait `/Temp`).
- [x] Démonstration sur 5 nouveaux termes, chaîne complète (voir phase 5).

## Phase 7 — Visuels

Objectif : environ un visuel toutes les 3 ou 4 définitions, là où il aide.

- [x] Plan des visuels (`docs/edition-2027/visuels/`) : 277 schémas (76 de priorité A), logos et captures.
- [x] Production des schémas avec `schemas-dictionnaire` : les 79 schémas de priorité A (3 démos et lots A1 à A8). Les priorités B (≈ 150) et C restent dans `plan-schemas.tsv` pour une suite.
- [x] Refaire au style 2027 les images de 2026 : les 48 schémas sont redessinés (lots A et R1 à R4), chacun vérifié à la source ; les passages faux repérés en dessinant sont corrigés (lots C9 à C11).
- [x] 6 images de tiers gardées (logos de Bitcoin Core, Bitcoin Knots, Bitcoin Cash et BSV, emblème « B » de Bitcoin, avatars PayNym) : chacune porte son crédit (titulaire, source, licence ou mention de marque), imprimé sous l'image dans le PDF et l'EPUB, lu par le site dans `metadata.yaml`, et listé dans `LICENSE.md`.

## Phase 8 — EPUB et Amazon KDP

- [x] EPUB validé par epubcheck (deux éditions).
- [x] Dossier `docs/edition-2027/kdp/` : métadonnées, description, mots-clés, catégories, prix conseillé, étapes Kindle et papier (Loïc publie lui-même).

## Phase 9 — Ce que le site devra suivre

- [x] Note de compatibilité à jour (section ci-dessous), prête à transmettre au worker de `feat/site-dictionnaire`.

---

## Budget de pages

Retour de Loïc du 27/10 : deux livres imprimés, plus de relié ni de tomes ; le complet sous 750 pages pour garder une marge. Limites lues sur l'aide KDP (https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6) : couleur premium, papier blanc, 24 à 828 pages jusqu'à 8 × 10 po ; couleur standard, 72 à 600 pages.

Build du 2026-10-27 (1 536 entrées : 1 060 techniques, 208 écosystème, 48 personnes, 220 spécifications ; 160 événements ; plus de NIP) :

| Livre | Format | Impression | Pages | EPUB (epubcheck) |
|---|---|---|---|---|
| complete | 7 × 10 po, Archivo 9/11,5 pt, une colonne, schémas couleur vectoriels (252) | couleur premium | 736 | 0 erreur |
| essentiel (poche) | 5 × 8 po, 9/11,5 pt, définitions courtes techniques et écosystème seulement | noir et blanc | 302 | 0 erreur |

Après fusion de `feat/schemas-2027` (140 nouveaux schémas) le complet passait à 790 pages en 9,5/12 pt ; corps ramené à 9/11,5 pt (broché de la charte) et schémas limités à 80 % de la ligne et 90 mm de haut : 736 pages. Coût d'impression du complet en couleur premium, grand format : 0,75 € + 0,0715 € par page, soit environ 53,40 € par exemplaire (détail et prix dans `docs/edition-2027/kdp/fiche.md`). Passer sous 600 pages permettrait la couleur standard, moins chère.

## Limite éditoriale : qui entre dans le dictionnaire des personnes

À compléter avec le résultat de la tâche « Liste des personnes » (critères proposés : travail cité par le livre blanc ou brique directe de Bitcoin ; rôle documenté dans le développement de Bitcoin, de Lightning ou d'une surcouche ; penseur fondateur invoqué par le discours Bitcoin, école autrichienne et cypherpunks ; acteur central d'un événement de la chronologie. Exclus : influenceurs, investisseurs, responsables politiques, fondateurs d'autres cryptomonnaies sans rôle dans Bitcoin).

## Droits sur les logos et les captures d'écran

Le livre est vendu, et son texte est sous licence CC BY-NC-SA 4.0. Deux régimes différents s'appliquent aux images de tiers :

- **Logos** : ce sont des marques, souvent des œuvres protégées. Les citer par leur nom est libre (usage nominatif) ; reproduire le logo dans un livre vendu demande en pratique l'accord du titulaire ou des conditions d'usage qui le permettent (kit presse, charte de marque). Beaucoup de kits presse autorisent l'usage éditorial mais interdisent la modification et l'usage commercial : une lecture au cas par cas est nécessaire.
- **Captures d'écran** : l'interface d'un logiciel est une œuvre. Un logiciel libre (licence MIT, GPL…) couvre son code ; la reproduction de son interface dans un livre est en général tolérée et défendable au titre de la citation, mais pas garantie. Un logiciel propriétaire demande l'accord de l'éditeur.
- **Incompatibilité de licence** : une image de tiers ne peut pas être placée sous CC BY-NC-SA par le dictionnaire. Chaque image de tiers doit porter sa mention de source et être exclue explicitement de la licence du livre (mention dans les pages légales et dans `LICENSE.md`).
- **Décision de Loïc (27/10)** : les logos et images de tiers restent, avec un crédit correct sur chaque image dans le PDF, l'EPUB, le livre papier et le dépôt. Recommandation d'origine, gardée pour mémoire : pas de logos de tiers dans le livre imprimé sans autorisation écrite ; captures limitées aux logiciels libres, faites par Loïc lui-même, créditées, et listées dans une page « Crédits des images ». Le plan des visuels note la source et les conditions trouvées pour chaque candidat (`docs/edition-2027/visuels/plan-logos-captures.tsv`).

## Compatibilité avec le site

Le site (`feat/site-dictionnaire`) lit `definitions/fr` avec un parseur YAML minimal. Ce qui change pour lui :

- **Nouveau fichier `courte.md`** dans chaque dossier : version courte, un paragraphe. Utilisable pour les descriptions, les aperçus et les cartes de survol (aujourd'hui calculées depuis `definition.md`).
- **Catégories** : 55 au lieu de 19, mêmes commentaires de description dans `templates/categories.yaml`. Nouveau `templates/parts.yaml` : partie de chaque catégorie, pictogramme et nom en casse de phrase (`display`). Le site peut séparer les entrées par partie (technique, écosystème, personnes, spécifications) sans nouveau champ dans `metadata.yaml`.
- **Pictogrammes** : `assets/pictograms/<slug>.svg` en `currentColor` (charte, section 7), un par catégorie.
- **Images** : en plus de `image-N.png` (couleur, à afficher), un schéma 2027 a `image-N-nb.pdf`, `image-N-nb.png` (livre imprimé, à ignorer) et `image-N.svg` (source). Seul `image-N.png` est déclaré dans `assets:` de `metadata.yaml`. Le texte alternatif sert aussi de légende.
- **Nouvelles sources** : `specifications/fr/*.yaml` (BIP, BOLT, bLIP ; les NIP sont retirés) et `chronologie/fr/*.yaml`, pour des pages dédiées si le site le souhaite.
- **Slugs inchangés**, aucune URL ne casse, même quand le slug porte une faute (`op-2drop-0xd6`, `canal-de-paiment`, `dlp-discreet-log-probleme`) : le titre est corrigé, le slug reste. Les nouvelles entrées (quantique, Nostr, applications Nostr, termes Optech, personnes) ajoutent des slugs.

## Questions ouvertes pour Loïc

- Fiche de Mara van der Laan : pronom à choisir (aujourd'hui sans pronom).
- Points « à trancher » des lots de corrections et de fiches : listés dans les journaux `~/.local/share/dico-2027/ed2027/corrections/C*-journal.md` et les rapports `verification-*.md` (dates à source unique, positions éditoriales comme BIP-0148).
- Le titre du poche `essentiel` et son ISBN (aujourd'hui : même titre, sous-titre « L'essentiel en définitions courtes », sans ISBN) ; nouvel ISBN du complet en 7 × 10 po.
- Notions de Nostr (catégories « Nostr » et « Application Nostr ») : les NIP sont retirés, mais ces fiches restent ; à garder ou à retirer ?
- Fiches et événements retirés à repêcher éventuellement : `docs/edition-2027/personnes-retirees.md`, `docs/edition-2027/chronologie-retiree.md`.

## Journal

- 2026-10-25 : démarrage, inventaire, décisions d'architecture. Taxonomie, spécifications, versions courtes, scripts, EPUB, skills. Limite d'usage de l'API vers 13 h 20 : quatre tâches relancées en reprise. Charte officielle reçue (`f5a3a13b`) : skill de schémas mis en conformité, mise en page du livre refaite à la charte, bogue de Tectonic contourné.
- 2026-10-26 : `/tmp` vidé au redémarrage ; travail des sous-tâches recopié dans `~/.local/share/dico-2027/`. Corrections C1 à C9 commitées, schémas A1 à A3, termes Nostr et quantiques.
- 2026-10-27 : deux limites d'usage, tâches relancées. Schémas A4 à A8 et R1 à R4, 152 fiches de personnes, 18 termes candidats, corrections C10 et C11, `pending_terms.yaml`. Charte passée au baobab sur `feat/couverture-2027` (`8ea661ec`) : section 6 des schémas inchangée, copie du skill mise à jour.
- 2026-10-27 (retour de Loïc) : NIP retirés ; personnes de 155 à 48 et chronologie de 696 à 160 événements (listes dans `docs/edition-2027/`) ; note de l'auteur et introductions réécrites ; mise en page couleur à la charte ; un broché couleur 7 × 10 po de 730 pages et un poche « essentiel » de 302 pages ; relié et tomes supprimés ; logos de tiers crédités.
- 2026-10-27 (fusion) : `feat/schemas-2027` (PDF couleur vectoriels des 112 schémas, 140 nouveaux) et `feat/english-2027` (`definitions/en/`, synchro FR/EN) fusionnées ; aucune traduction orpheline ; complet 736 pages, poche 302 pages.
