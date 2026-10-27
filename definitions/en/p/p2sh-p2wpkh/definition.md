Acronym for *Pay to Script Hash - Pay to Witness Public Key Hash*. Standard script template used to set spending conditions on a UTXO, also known as "Nested SegWit".

P2SH-P2WPKH was introduced with the implementation of SegWit in August 2017. This script is a P2WPKH wrapped inside a P2SH. It locks bitcoin based on the hash of a public key. The difference from a regular P2WPKH is that the script is here wrapped in the `redeemScript` of a regular P2SH.

This script was created at the launch of SegWit to ease its adoption. It makes it possible to use this new standard even with services or wallets not yet natively compatible with SegWit. It is a kind of transition script toward the new standard. Today, it is therefore no longer very relevant to use this type of wrapped SegWit script, since most wallets have implemented native SegWit. P2SH-P2WPKH addresses are written using the `Base58Check` encoding and always begin with `3`, like any P2SH address.

*`P2SH-P2WPKH` is also sometimes called `P2WPKH-nested-in-P2SH`.*
