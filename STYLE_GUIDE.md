# Charte éditoriale Dictionnaire de Bitcoin

Guide de style a destination des contributeurs.

## 1. Typographie generale

| Element            | Convention                                                         |
| ------------------ | ------------------------------------------------------------------ |
| Apostrophe         | Droite (U+0027)                                                    |
| Guillemets         | Toujours français `« texte »` avec espaces insécables              |
| Espaces insecables | Avant `:`, `;`, `!`, `?`, et à l'intérieur des guillemets français |

## 2. Mise en forme du texte

### Gras

Le gras (`**texte**`) est **interdit** dans le corps des définitions (`definition.md`).

### Italique

L'italique (`*texte*`) est utilise pour :
- **Termes anglais** employés dans le texte français : *seed*, *wallet*, *output*, *hash*, *pool*, *self-custody*
- **Noms de protocoles ou concepts en anglais** : *Silent Payments*, *Atomic Swap*, *adaptor signature*
- **Note en bas de définition** (bloc entier en italique) : `*Texte de la note.*`

L'italique n'est **pas** utilisé pour :
- Les noms propres de logiciels ou entreprises : Bitcoin Core, Samourai Wallet, ACINQ
- Les sigles et acronymes : UTXO, PSBT, HTLC, BIP
- Les termes déjà en code inline

### Code inline

Le code inline est utilisé pour :
- Les opcodes : `OP_CHECKSIG`, `OP_RETURN`
- Les fonctions de hachage : `SHA256`, `RIPEMD160`, `HASH160`
- Les paramètres de configuration : `maxmempool`, `mempoolexpiry`, `datacarriersize`
- Les valeurs hexadécimales et les préfixes : `0x50`, `bc1q`, `bc1p`
- Les noms de fichiers : `peers.dat`, `chainstate`
- Les commandes : `getblocktemplate`
- Les algorithmes d'encodage : `Bech32`, `Bech32m`, `Base58check`

Le code inline n'est **pas** utilise pour les noms de protocoles, de standards ou de concepts.

## 3. Références aux standards

### BIP (Bitcoin Improvement Proposals)

Format obligatoire : `BIP-NNNN` (tiret + exactement 4 chiffres, avec zéros de remplissage).

### BOLT (Basis of Lightning Technology)

Format obligatoire : `BOLT-NN` (tiret + 2 chiffres avec zéro de remplissage).

## 4. Mathématiques (LaTeX)

Les formules mathématiques utilisent la syntaxe LaTeX encadrée par des `$` (inline) ou `$$` (bloc).

## 5. Structure d'une définition

Chaque définition se compose de :

1. **`metadata.yaml`** : métadonnées (uuid, title, slug, category, cross_references, etc.)
2. **`definition.md`** : corps de la définition en texte continu

### Corps de la définition

- Le texte est rédigé en paragraphes continus (pas de titre markdown `#` dans le corps)
- Les listes a puces sont autorisées
- Les images sont référencées avec `![](./assets/image.png)` et placées dans un sous-dossier `assets/` du dossier de la définition
- Une note optionnelle en italique peut apparaitre en fin de définition

### Titre dans metadata.yaml

- Toujours en MAJUSCULES : `title: "ADAPTOR SIGNATURE"`
- Le slug est en minuscules avec tirets : `slug: "adaptor-signature"`