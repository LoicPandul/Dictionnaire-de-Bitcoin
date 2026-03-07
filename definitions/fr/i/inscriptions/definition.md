Dans le cadre de la théorie des Ordinals, les inscriptions sont des contenus arbitraires gravés sur des sats, transformant ces derniers en artefacts numériques natifs de Bitcoin. Les inscriptions sont effectuées via des transactions qui exposent le contenu de l'information dans le script d'un input Taproot de cette manière :

```text
OP_FALSE
OP_IF
  OP_PUSH "ord"
  OP_PUSH 1
  OP_PUSH "<content type>"
  OP_PUSH 0
  OP_PUSH "<la data ici>"
OP_ENDIF
```

Ces artefacts numériques, comme des NFTs, peuvent être échangés et conservés.
