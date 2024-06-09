## HASH160

Fonction cryptographique utilisée sur Bitcoin notamment pour générer des adresses de réception Legacy et SegWit v0. Elle combine deux fonctions de hachage qui s'exécute successivement sur l'input : d'abord SHA256, puis RIPEMD160. La sortie de cette fonction est donc de 160 bits.
$$\text{HASH-160}(x) = \text{RIPEMD-160}(\text{SHA-256}(x))$$

