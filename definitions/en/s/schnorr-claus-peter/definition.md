German mathematician and cryptographer (1943-2025), professor at Goethe University Frankfurt, inventor of the signature that bears his name.

Born on August 4, 1943, in Völklingen, in Saarland, he became a professor of mathematics at Frankfurt in 1971. In the late 1980s, he devised an identification and signature scheme based on the discrete logarithm, now called the Schnorr signature. Goethe University Frankfurt noted in 2008 that the scheme had become a decisive component of the US Digital Signature Standard. His US patent 4,995,082, which describes the identification and signature method, was filed with a priority date of February 24, 1989 and granted on February 19, 1991.

`BIP-0340`, assigned on January 19, 2020 to Pieter Wuille, Jonas Nick, and Tim Ruffing, specifies 64-byte Schnorr signatures on the secp256k1 curve and compares them with ECDSA, which uses the same curve. It stresses their linearity: several participants can jointly produce a valid signature for the sum of their public keys, which is the basis for multisignatures such as MuSig2 and threshold signatures such as FROST. Taproot (`BIP-0341`) uses these signatures, 64 bytes by default (65 with an explicit sighash byte), and activated at block 709,632.

He is neither among the authors nor in the acknowledgments of these BIPs: his link to Bitcoin runs through the mathematical construction that bears his name.
