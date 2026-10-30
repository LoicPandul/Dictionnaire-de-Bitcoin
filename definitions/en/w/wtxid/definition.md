Extension of the traditional TXID that includes the witness data introduced with SegWit. While the TXID is a hash of the transaction data excluding the witness, the WTXID is the `SHA256d` of all of the transaction data, witness included. WTXIDs are stored in a second Merkle tree whose root is placed in the coinbase transaction. This separation eliminates the malleability of the transaction's TXID.

![The two Merkle trees of a SegWit block: the TXID root goes into the header, and the WTXID root is committed to in an OP_RETURN output of the coinbase transaction.](./assets/image-1.png)
