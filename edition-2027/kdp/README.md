# Publication Amazon KDP — édition 2027

Dossier de publication du *Dictionnaire de Bitcoin*, édition 2027, pour Kindle (ebook) et broché. Deux livres imprimés : le complet (broché en couleur premium) et le poche « essentiel » (broché en noir et blanc). Loïc publie lui-même : rien n'est envoyé à Amazon depuis ce dépôt.

Fiche des livres (titre, description, mots-clés, catégories, prix) : [fiche.md](fiche.md).

Les barèmes KDP cités ici ont été lus sur les pages d'aide de KDP le 27 octobre 2026 ; ces pages ne sont pas datées. **Le calculateur de redevances et l'onglet « Droits et tarification » de KDP font foi** : vérifier chaque prix dans l'interface avant de publier. Sources :

- coûts d'impression en euros : <https://kdp.amazon.com/fr_FR/help/topic/G201834340>
- redevances (60 % et 50 %) : <https://kdp.amazon.com/en_US/help/topic/G201834330>
- limites de pages, formats et marges intérieures : <https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6>

## 1. Fichiers à produire

```bash
python3 scripts/main.py check                                            # zéro erreur avant tout
python3 scripts/main.py build --edition complete --format pdf,epub
python3 scripts/main.py build --edition essentiel --format pdf,epub
```

| Fichier | Usage KDP |
|---|---|
| `build/complete/dictionnaire-de-bitcoin.pdf` | intérieur du broché complet (7 × 10 po, couleur premium, PDF CMJN, 730 pages) |
| `build/essentiel/dictionnaire-de-bitcoin.pdf` | intérieur du poche « essentiel » (5 × 8 po, noir et blanc, 302 pages) |
| `build/complete/dictionnaire-de-bitcoin.epub` | ebook Kindle du complet (rapport epubcheck à côté, 0 erreur) |
| `build/essentiel/dictionnaire-de-bitcoin.epub` | ebook Kindle de l'essentiel (rapport epubcheck à côté, 0 erreur) |
| couvertures | produites sur la branche `feat/couverture-2027` (`design/couverture/build.py`, voir `design/charte-2027.md`, section 4) : un PDF CMJN par broché avec le nombre de pages final, image 1 600 × 2 560 px par ebook |

Contrôles avant envoi :

- **Polices incorporées** : `pdffonts` doit afficher `emb yes` partout.
- **Nombre de pages** : `pdfinfo`. Complet : 730 pages ; la couleur premium accepte de 24 à 828 pages. Essentiel : 302 pages ; le noir et blanc sur papier blanc accepte de 24 à 828 pages. Un changement de contenu qui fait varier le nombre de pages change aussi le coût d'impression : refaire le tableau de la fiche.
- **Marge intérieure** : KDP exige au moins 22,3 mm de 701 à 828 pages et 15,9 mm de 301 à 500 pages. Le complet (730 pages) est réglé à 25,5 mm, au-dessus du minimum ; l'essentiel (302 pages) est dans la tranche 301 à 500 pages.
- **Épaisseur de la couverture** : la tranche se calcule avec le nombre de pages final du PDF intérieur ; relancer le script de couverture après le dernier build.
- **Ebooks** : poids des fichiers. Au-delà de quelques Mo, les frais de livraison de l'option 70 % pèsent sur chaque vente ; les schémas 2027 en PNG de 1 280 px peuvent faire grimper le poids. Si un EPUB dépasse 10 Mo, réduire les images de l'ebook (largeur 1 000 px, PNG en palette) avant l'envoi.
- **Kindle Previewer** (gratuit, Amazon) : ouvrir chaque EPUB et contrôler une page avec formules, une avec tableau, une avec schéma, la table des matières.

## 2. Ebooks Kindle

Deux ebooks, un par édition (complet et essentiel). Pour chacun :

1. Bibliothèque KDP → Créer → eBook Kindle.
2. Détails : reprendre [fiche.md](fiche.md) (langue français, titre, sous-titre, édition, auteur, description, mots-clés, catégories). « Numéro d'édition » : voir la fiche.
3. Droits de publication : « Je détiens les droits d'auteur ». Le texte est sous licence CC BY-NC-SA 4.0 et Loïc en est l'auteur : il peut le vendre lui-même. Les 6 logos de tiers du livre sont conservés : chacun porte un crédit sous l'image et est exclu de la licence dans `LICENSE.md` (voir PLAN.md, « Droits sur les logos et les captures d'écran »).
4. **KDP Select : ne pas s'inscrire.** Select exige l'exclusivité de l'ebook sur Amazon, alors que le PDF et l'EPUB sont gratuits sur GitHub.
5. Contenu : DRM non (cohérent avec la licence libre), fichier EPUB de l'édition, couverture 1 600 × 2 560 px. Lancer l'aperçu en ligne.
6. Tarification : voir la fiche (option 70 %, prix entre 2,69 € et 12,99 € pour la zone euro).
7. Publier. Délai de mise en ligne annoncé par KDP : jusqu'à 72 heures.

## 3. Broché complet

1. Créer → Livre broché, ou « Associer » à la fiche ebook pour partager titre et description.
2. ISBN : l'édition 2027 change de contenu en profondeur (nouvelles parties, nouvelle mise en page) : KDP demande un nouvel ISBN pour une nouvelle édition. Prendre l'ISBN gratuit KDP ou un ISBN propre (question ouverte dans la fiche), puis le reporter dans `templates/legal.yaml` (`isbn_paperback`) et relancer le build pour l'imprimer dans les pages légales.
3. Impression : **couleur premium**, papier blanc, format 7 × 10 po (17,78 × 25,4 cm), sans fond perdu. KDP classe ce format parmi les « grands » (au-delà de 6,12 × 9 po) : c'est le barème « grand » qui s'applique (voir la fiche). Couverture brillante (charte : la finition brillante garde mieux le magenta).
4. Intérieur : `build/complete/dictionnaire-de-bitcoin.pdf` (CMJN). Couverture : PDF CMJN du script de couverture.
5. Lancer le vérificateur en ligne, puis commander **une épreuve** avant de publier (la charte le demande : un aplat de Figue à 35 % de noir peut montrer des bandes sur presse numérique ; l'épreuve en couleur premium permet aussi de juger les schémas).
6. Tarification et distribution étendue : voir la fiche.

## 4. Poche « essentiel »

Même procédure que le broché complet, avec `build/essentiel/dictionnaire-de-bitcoin.pdf`, son propre ISBN (un ISBN par livre imprimé), son propre fichier de couverture et ces réglages d'impression : **noir et blanc**, papier blanc, format 5 × 8 po (12,7 × 20,32 cm, format « standard » de KDP), sans fond perdu.

## 5. Après publication

- Mettre à jour les liens d'achat du `README.md` et le badge de version.
- Remplacer, si Loïc le décide, les PDF de la racine du dépôt par les PDF 2027 et publier une *release* GitHub avec PDF et EPUB.
- Vérifier chaque fiche Amazon (aperçu « Feuilleter », catégories retenues, prix dans chaque marché).
