Data structure provided in the witness of a P2TR transaction during a script path spend, as defined in BIP-0341. The control block proves that a given script is indeed part of the script tree (MAST) that was used to build the output's Taproot public key.

It consists of three elements:
* a first byte that encodes the leaf version and the parity of the output public key;
* the 32-byte internal key, which is the key before the tweak is applied;
* the Merkle path, made up of zero to 128 hashes of 32 bytes each, which represents the sequence of sibling nodes needed to recompute the root of the tree from the revealed leaf.

During validation, the node recomputes the Merkle root from the leaf script and the supplied path, then verifies that tweaking the internal key with this root yields the output public key recorded in the `scriptPubKey`. This mechanism proves that a script belongs to the tree without revealing the other leaves, which preserves the privacy of the unused spending paths.
