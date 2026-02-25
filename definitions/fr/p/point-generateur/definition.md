Point fixe sur une courbe elliptique qui sert de base pour toutes les opérations de cryptographie à clé publique. Dans Bitcoin, le point générateur `G` est un paramètre standard de la courbe secp256k1 défini de manière déterministe. Tous les utilisateurs de Bitcoin partagent le même point générateur `G`. C'est un paramètre public et universel de la courbe secp256k1. Ses coordonnées sont :

```
x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
```

Le point générateur est à la base de la dérivation des clés publiques : une clé privée `k` (un nombre entier) est associé à une clé publique `K` par multiplication scalaire sur la courbe elliptique : `K = k * G`. Cette opération est facile à calculer dans un sens, mais pratiquement impossible à inverser (problème du logarithme discret sur courbes elliptiques).