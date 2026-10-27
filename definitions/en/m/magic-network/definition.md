Constants used in the Bitcoin protocol to identify the specific network (mainnet, testnet, regtest...) of a message exchanged between nodes. These values are written at the start of each message to make it easier to pick messages out of the data stream. Magic network values are designed to rarely appear in ordinary communication data. These 4 bytes are uncommon in ASCII, are invalid in UTF-8, and produce a very large 32-bit integer, whatever the data storage format. The magic network values are (in little-endian format):

Mainnet:
```text
f9beb4d9
```

Testnet3:
```text
0b110907
```

Testnet4:
```text
1c163f28
```

Signet (default public network):
```text
0a03cf40
```

Regtest:
```text
fabfb5da
```

On a custom signet, the value is derived from the network's challenge, which gives each signet its own identifier.

*These 4 bytes are sometimes also called "magic number", "magic bytes", or "start string".*
