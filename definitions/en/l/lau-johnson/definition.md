Bitcoin developer, coauthor of the SegWit specifications and author of a MAST proposal, known under the pseudonym jl2012.

On December 21, 2015, BIP-0141, which defines SegWit, was assigned its number with three authors: Eric Lombrozo, Johnson Lau, and Pieter Wuille. On January 3, 2016, Johnson Lau and Pieter Wuille obtained the number for BIP-0143, which describes transaction signing for witness programs of version 0.

On April 2, 2016, he proposed alone BIP-0114, which introduces MAST: a Merkle tree in which each leaf is a script branch, so that a spend reveals only the branch that is executed. The proposal was later closed (Closed status). The Taproot BIP-0341 cites this work among its antecedents and thanks Johnson Lau for his Merkle branch constructions.

Also in 2016, he wrote BIP-0147, which requires the dummy element additionally consumed by `OP_CHECKMULTISIG` to be an empty byte array, otherwise the script fails: this element was not inspected and offered a handle for malleability. His NULLDUMMY code entered Bitcoin Core through a commit of August 31, 2016, and the rule was deployed with SegWit, using the same BIP9 parameters. He also co-signed, with Pieter Wuille, BIP-0146 on the malleability of signature encoding, which remained in Closed status.
