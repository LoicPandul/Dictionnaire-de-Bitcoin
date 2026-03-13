Variante de fonction de hachage utilisée dans le protocole Bitcoin (notamment dans Taproot) pour garantir la séparation des domaines. Une fonction de hachage taguée prend un tag (une chaîne de caractères UTF-8) et des données en entrée, et calcule le hachage comme suit :
$$
TaggedHash(tag,\ data) = SHA256(SHA256(tag)\ \Vert\ SHA256(tag)\ \Vert\ data)
$$

Le fait de préfixer les données par le double hachage du tag garantit que des hachages calculés dans des contextes différents ne peuvent pas entrer en collision. Par exemple, un hachage calculé avec le tag `TapLeaf` ne pourra jamais être identique à un hachage calculé avec le tag `TapBranch`, même si les données sont les mêmes.

Ce mécanisme est introduit par le BIP-0340 et utilisé dans l'ensemble des BIPs liés à Taproot (BIP-0341 et BIP-0342). Chaque étape de la construction et de la dépense d'une sortie P2TR utilise un tag distinct : `TapLeaf` pour les feuilles de l'arbre de scripts, `TapBranch` pour les branches, `TapTweak` pour le calcul du tweak, et `TapSighash` pour la création du hash de signature. Le BIP-0340 utilise aussi des tags pour les signatures de Schnorr : `BIP0340/challenge`, `BIP0340/aux` et `BIP0340/nonce`.