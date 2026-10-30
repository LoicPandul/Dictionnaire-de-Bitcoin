In the derivation of hierarchical deterministic wallets, derivation branch used to generate addresses that the wallet does not have to share with third parties, in practice change addresses. Each account, as defined at depth 3, has two keychains at depth 4: an external keychain and an internal keychain (also called “change”). The internal keychain is derived with an index of `/1/`.

![At depth 4, each account splits into two keychains: the internal keychain, with index 1 (path m/84'/0'/0'/1), produces the change addresses.](../../../fr/c/chaine-interne/assets/image-1.png)
