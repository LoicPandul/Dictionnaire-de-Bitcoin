Element of a Bitcoin transaction that determines the destination of the funds sent. A transaction can include several outputs, each uniquely identified by the combination of the transaction identifier (`txid`) and an index called `vout`. This index, which starts at `0`, marks the position of the output in the transaction's sequence of outputs. Thus, the first output is designated by `"vout": 0`, the second by `"vout": 1`, and so on.

Each `vout` mainly encapsulates two pieces of information:
* the value, expressed in bitcoin, which represents the amount sent;
* a locking script (`scriptPubKey`) that stipulates the conditions required for the funds to be spent again in a later transaction.

The combination of the `txid` and the `vout` of a specific UTXO forms what is called an outpoint, for example:

* txid:

```
4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
```

* vout:

```
0
```

* outpoint:

```
4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```
