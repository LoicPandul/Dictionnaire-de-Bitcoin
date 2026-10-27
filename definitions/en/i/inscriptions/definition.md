Arbitrary content engraved on sats in Ordinals theory, turning them into digital artifacts native to Bitcoin. Inscriptions are made through transactions that expose the content in a Taproot script revealed by a script path spend, as follows:

```text
OP_FALSE
OP_IF
  OP_PUSH "ord"
  OP_PUSH 1
  OP_PUSH "<content type>"
  OP_PUSH 0
  OP_PUSH "<data goes here>"
OP_ENDIF
```

These digital artifacts, like NFTs, can be traded and held.
