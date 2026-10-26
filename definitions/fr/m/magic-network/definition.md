Constantes utilisées dans le protocole Bitcoin pour identifier le réseau spécifique (mainnet, testnet, regtest...) d'un message échangé entre des nœuds. Ces valeurs sont inscrites au début de chaque message pour faciliter leur identification dans le flux de données. Les Magic Network sont conçus pour être rarement présents dans des données de communication ordinaires. En effet, ces 4 octets sont peu fréquents dans l'ASCII, sont invalides en UTF-8 et génèrent un très grand entier de 32 bits, peu importe le format de stockage des données. Les Magic Network sont (en format *little-endian*) :

Mainnet :
```text
f9beb4d9
```

Testnet3 :
```text
0b110907
```

Testnet4 :
```text
1c163f28
```

Signet (réseau public par défaut) :
```text
0a03cf40
```

Regtest :
```text
fabfb5da
```

Sur un signet personnalisé, la valeur est dérivée du défi (*challenge*) du réseau, ce qui donne à chaque signet son propre identifiant.

*Ces 4 octets sont parfois également nommés « Magic Number », « Magic Bytes » ou encore « Start String ».*