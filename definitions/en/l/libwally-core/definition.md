Open-source cryptography and utility library developed by Blockstream, designed to make it easier to integrate Bitcoin functions into applications. It provides low-level primitives for key management, transaction construction, address encoding, and PSBT operations.

Libwally-core is written in C to be portable and fast, with bindings available for Python, Java, JavaScript, and other languages. It relies on `libsecp256k1` for cryptographic operations on the elliptic curve.

It is notably used as a core dependency of Core Lightning (CLN) for all wallet and transaction operations. Other projects, such as Blockstream's Green Wallet, use it as well.
