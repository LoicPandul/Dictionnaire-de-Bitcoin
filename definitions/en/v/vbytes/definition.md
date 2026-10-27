Unit of measurement used to evaluate the size of a Bitcoin transaction while accounting for the weighting introduced by SegWit. A vbyte (virtual byte) represents a normalized unit of weight: 4 weight units (WU) correspond to 1 vbyte. This measure allows a fair comparison between SegWit and legacy transactions.

Before SegWit, the size of a transaction was measured in raw bytes. With SegWit, witness data benefits from a discount: each witness byte counts for 1 WU, against 4 WU for other data. Computing in vbytes smooths out this difference. For example, a transaction with a total weight of 600 WU is 150 vbytes.

Transaction fees are calculated in satoshis per vbyte (sat/vB). Using vbytes lets wallets estimate fees correctly whatever the structure of the transaction. A Bitcoin block can contain at most 4 million WU, equivalent to 1 million vbytes.
