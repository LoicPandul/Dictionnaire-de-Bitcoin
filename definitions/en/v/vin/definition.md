Element of a Bitcoin transaction that specifies the source of the funds used to satisfy the outputs. Each `vin` refers to an unspent output (UTXO) of a previous transaction. A transaction can contain several inputs, each identified by a combination of the `txid` (the identifier of the originating transaction) and the `vout` (the index of the output in that transaction).

Each `vin` includes the following information:
* `txid`: the identifier of the previous transaction containing the output used here as an input;
* `vout`: the index of the output in the previous transaction;
* `scriptSig` or `scriptWitness`: an unlocking script that provides the data needed to satisfy the conditions set by the `scriptPubKey` of the previous transaction whose funds are being spent, generally by providing a cryptographic signature;
* `nSequence`: a field used to indicate how this input is timelocked, as well as other options such as RBF.
