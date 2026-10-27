Variant of a hash function used in the Bitcoin protocol (notably in Taproot) to ensure domain separation. A tagged hash function takes a tag (a UTF-8 string) and data as input, and computes the hash as follows:
$$
TaggedHash(tag,\ data) = SHA256(SHA256(tag)\ \Vert\ SHA256(tag)\ \Vert\ data)
$$

Prefixing the data with two copies of the tag's hash, `SHA256(tag)`, ensures that hashes computed in different contexts cannot collide. For example, a hash computed with the tag `TapLeaf` can never be identical to a hash computed with the tag `TapBranch`, even if the data is the same.

This mechanism was introduced by BIP-0340 and is used across the BIPs related to Taproot (BIP-0341 and BIP-0342). Each step in the construction and spending of a P2TR output uses a distinct tag: `TapLeaf` for the leaves of the script tree, `TapBranch` for the branches, `TapTweak` for the tweak computation, and `TapSighash` for creating the signature hash. BIP-0340 also uses tags for Schnorr signatures: `BIP0340/challenge`, `BIP0340/aux`, and `BIP0340/nonce`.
