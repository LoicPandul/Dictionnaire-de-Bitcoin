High-performance, high-security C library for digital signatures and other cryptographic primitives on the `secp256k1` elliptic curve. Since this curve has never been widely used outside Bitcoin (unlike the often preferred `secp256r1` curve), the library aims to be the most complete reference for its use. The development of libsecp256k1 has been primarily driven by Bitcoin's needs, and features intended for other applications may be less tested or verified. Proper use of the library requires particular care, to make sure it suits the specific goals of applications other than Bitcoin.

The libsecp256k1 library offers a variety of features, including:
* ECDSA-secp256k1 signing and verification, as well as cryptographic key generation;
* Additive and multiplicative operations on secret and public keys;
* Serialization and parsing of secret keys, public keys, and signatures;
* Constant-time, constant-memory-access signing and public key generation;
* And many other cryptographic primitives.
