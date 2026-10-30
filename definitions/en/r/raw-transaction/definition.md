Constructed and signed Bitcoin transaction, in its binary form. A raw transaction (raw TX) is the final representation of a transaction, just before it is broadcast on the network. This transaction contains all the information needed for its inclusion in a block:
* The version;
* The marker and the flag (for SegWit transactions);
* The inputs;
* The outputs;
* The witness (for SegWit transactions);
* The locktime.

![Fields of a raw transaction in their serialization order, from the first to the last byte: only the version, the inputs, the outputs, and the locktime go into the double SHA-256 that gives the TXID.](../../../fr/r/raw-transaction/assets/image-1.png)

What is called a “raw transaction” is the raw data that is passed twice through the `SHA256` hash function to generate the transaction's `txid`. For SegWit transactions, only the original serialization (without the marker, the flag, and the witness) is used to compute the `txid`. This data is then used in the block's Merkle tree to integrate the transaction into the blockchain.

*This concept is also sometimes called “serialized transaction.”*
