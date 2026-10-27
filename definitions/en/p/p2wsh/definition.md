Acronym for *Pay to Witness Script Hash*. Standard script template used to set spending conditions on a UTXO. P2WSH was introduced with the implementation of SegWit in August 2017.

This script is similar to P2SH (*Pay to Script Hash*), since it also locks bitcoin based on the hash of a script. The difference lies in how signatures and scripts are included in the transaction. To spend bitcoin on this type of script, the recipient must provide the original script, called the `witnessScript` (the equivalent of the `redeemScript`), along with the required signatures. This mechanism makes it possible to implement more sophisticated spending conditions, such as multisigs.

With P2WSH, the signature script information (the `scriptWitness`, the equivalent of the `scriptSig`) is moved out of the traditional structure of the transaction into a separate section called the `Witness`. This move is a feature of the SegWit (*Segregated Witness*) upgrade that prevents signature-related malleability. P2WSH transactions are generally cheaper in fees than Legacy transactions, because the witness portion costs less.

P2WSH addresses are written using the `Bech32` encoding, with a checksum in the form of a BCH code. These addresses always begin with `bc1q`. P2WSH is a SegWit version 0 output.
