Script situé dans la partie sortie (output) d'une transaction Bitcoin qui définit les conditions sous lesquelles l'UTXO associé peut être dépensé. Ce script permet donc de sécuriser des bitcoins. Dans sa forme la plus courante, le `scriptPubKey` contient une condition qui exige que la prochaine transaction fournisse une preuve de possession de la clé privée correspondant à une adresse Bitcoin spécifiée. C'est souvent réalisé par un script qui demande une signature correspondant à la clé publique associée à l'adresse utilisée pour sécuriser ces fonds. Lorsqu'une transaction tente d'utiliser cet UTXO en entrée (input), elle doit fournir un `scriptSig` qui, exécuté d'abord puis suivi du `scriptPubKey` sur la même pile, satisfait les conditions posées et produit un script valide. Pour une sortie SegWit native, le `scriptSig` doit être vide : les données de déverrouillage se trouvent alors dans le témoin (*witness*). 

![Le scriptPubKey P2PKH verrouille la sortie 0 de la transaction 1 ; l'entrée 0 de la transaction 2 la dépense et fournit le scriptSig qui le satisfait.](./assets/image-1.png)

Par exemple, voici un `scriptPubKey` P2PKH classique :

```text
OP_DUP
OP_HASH160
OP_PUSHBYTES_20
<hash de la clé publique>
OP_EQUALVERIFY
OP_CHECKSIG
```

Le `scriptSig` correspondant serait :

```text
<signature> <clé publique>
```

*Pour nommer ce script, on parle également parfois d'un « locking script » ou « script de verrouillage » en français.*
