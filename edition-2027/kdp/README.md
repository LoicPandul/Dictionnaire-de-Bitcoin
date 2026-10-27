# Publication Amazon KDP — édition 2027

Dossier de publication du *Dictionnaire de Bitcoin*, édition 2027, pour Kindle (ebook), broché et relié. Loïc publie lui-même : rien n'est envoyé à Amazon depuis ce dépôt.

Fiche du livre (titre, description, mots-clés, catégories, prix) : [fiche.md](fiche.md).

Les barèmes KDP cités ici ont été lus sur les pages d'aide de KDP le 25 octobre 2026 ; ces pages ne sont pas datées et se contredisent parfois (relié). **Le calculateur de redevances et l'onglet « Droits et tarification » de KDP font foi** : vérifier chaque prix dans l'interface avant de publier.

## 1. Fichiers à produire

```bash
python3 scripts/main.py check                                   # zéro erreur avant tout
python3 scripts/main.py build --edition complete --format pdf,pdf-relie,epub
```

| Fichier | Usage KDP |
|---|---|
| `build/complete/dictionnaire-de-bitcoin.pdf` | intérieur du broché (5,5 × 8,5 po, noir et blanc) |
| `build/complete/dictionnaire-de-bitcoin-relie.pdf` | intérieur du relié (7 × 10 po) |
| `build/complete/dictionnaire-de-bitcoin.epub` | ebook Kindle (rapport epubcheck à côté, 0 erreur attendu) |
| couvertures | produites sur la branche `feat/couverture-2027` (`design/couverture/build.py`, voir `design/charte-2027.md`, section 4) : PDF CMJN du broché et du relié avec le nombre de pages final, image 1 600 × 2 560 px pour Kindle |

Contrôles avant envoi :

- **Polices incorporées** : `pdffonts` doit afficher `emb yes` partout (c'est le cas au premier build 2027 : Archivo, Atkinson Hyperlegible Mono, Fira Math).
- **Nombre de pages** : `pdfinfo`. Broché : 828 pages au plus ; au-delà de 700, le générateur porte seul la marge intérieure à 22,5 mm (règle KDP : 22,3 mm de 701 à 828 pages). Relié : **550 pages au plus**. Au premier build (sans chronologie ni nouveaux termes), le relié complet fait 566 pages : voir « Budget de pages » dans `edition-2027/PLAN.md`.
- **Épaisseur de la couverture** : la tranche se calcule avec le nombre de pages final du PDF intérieur ; relancer le script de couverture après le dernier build.
- **Ebook** : poids du fichier. Au-delà de quelques Mo, les frais de livraison de l'option 70 % pèsent sur chaque vente ; les schémas 2027 en PNG de 1 280 px peuvent faire grimper le poids. Si l'EPUB dépasse 10 Mo, réduire les images de l'ebook (largeur 1 000 px, PNG en palette) avant l'envoi.
- **Kindle Previewer** (gratuit, Amazon) : ouvrir l'EPUB et contrôler une page avec formules, une avec tableau, une avec schéma, la table des matières.

## 2. Ebook Kindle

1. Bibliothèque KDP → Créer → eBook Kindle.
2. Détails : reprendre [fiche.md](fiche.md) (langue français, titre, sous-titre, édition, auteur, description, mots-clés, catégories). « Numéro d'édition » : voir la fiche.
3. Droits de publication : « Je détiens les droits d'auteur ». Le texte est sous licence CC BY-NC-SA 4.0 et Loïc en est l'auteur : il peut le vendre lui-même. Les images de tiers éventuelles (logos, captures) doivent avoir leur accord écrit (voir PLAN.md, « Droits sur les logos et les captures »).
4. **KDP Select : ne pas s'inscrire.** Select exige l'exclusivité de l'ebook sur Amazon, alors que le PDF et l'EPUB sont gratuits sur GitHub.
5. Contenu : DRM non (cohérent avec la licence libre), fichier `dictionnaire-de-bitcoin.epub`, couverture 1 600 × 2 560 px. Lancer l'aperçu en ligne.
6. Tarification : voir la fiche (option 70 %, prix entre 2,69 € et 12,99 € pour la zone euro).
7. Publier. Délai de mise en ligne annoncé par KDP : jusqu'à 72 heures.

## 3. Broché

1. Créer → Livre broché, ou « Associer » à la fiche ebook pour partager titre et description.
2. ISBN : l'édition 2027 change de contenu en profondeur (nouvelles parties, nouvelle mise en page) : KDP demande un nouvel ISBN pour une nouvelle édition. Prendre l'ISBN gratuit KDP ou un ISBN propre (question ouverte dans la fiche), puis le reporter dans `templates/legal.yaml` (`isbn_paperback`) et relancer le build pour l'imprimer dans les pages légales.
3. Impression : noir et blanc, papier blanc, format 5,5 × 8,5 po (13,97 × 21,59 cm), sans fond perdu, couverture brillante (charte : la finition brillante garde mieux le magenta).
4. Intérieur : `dictionnaire-de-bitcoin.pdf`. Couverture : PDF CMJN du script de couverture.
5. Lancer le vérificateur en ligne, puis commander **une épreuve** avant de publier (la charte le demande : un aplat de Figue à 35 % de noir peut montrer des bandes sur presse numérique).
6. Tarification et distribution étendue : voir la fiche.

## 4. Relié

Même procédure que le broché, avec `dictionnaire-de-bitcoin-relie.pdf`, le format 7 × 10 po (17,78 × 25,4 cm), l'ISBN relié (`isbn_hardcover`) et la couverture reliée. Le relié n'est possible que si l'intérieur tient en 550 pages : trancher d'abord le budget de pages (corps 9 / 11,5 pt, ou deux volumes).

## 5. Après publication

- Mettre à jour les liens d'achat du `README.md` et le badge de version.
- Remplacer, si Loïc le décide, les PDF de la racine du dépôt par les PDF 2027 et publier une *release* GitHub avec PDF et EPUB.
- Vérifier la fiche Amazon (aperçu « Feuilleter », catégories retenues, prix dans chaque marché).
