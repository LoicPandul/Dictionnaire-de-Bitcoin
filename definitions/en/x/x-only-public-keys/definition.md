Public key format on the secp256k1 elliptic curve in which only the $x$ coordinate of the point is kept, without the prefix byte that usually indicates the parity of the $y$ coordinate. This format reduces the size of a public key from 33 bytes (standard compressed key) to 32 bytes.

On an elliptic curve, each value of $x$ corresponds to exactly two points that are symmetric about the x-axis and differ only in the sign of their $y$ coordinate. To resolve this ambiguity without an extra byte, BIP-0340 (Schnorr signatures) imposes a convention: only the point whose $y$ coordinate is even is considered valid. The verifier can thus reconstruct the full point from the 32 bytes of $x$ alone.

This format is used systematically in Taproot (BIP-0341) and Tapscript (BIP-0342) for internal keys, output keys, and signature checks within SegWit v1 scripts. The saving of one byte per key, though modest in appearance, adds up across all the transactions of the network and helps reduce the size of witnesses.

The use of x-only keys, however, introduces a constraint for key aggregation protocols such as MuSig2: participants must make sure that the final aggregated key does produce a point with an even $y$ coordinate, which may require a step of negating the private key.
