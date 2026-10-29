American cryptographer, at MIT since 1974 and now an Institute Professor, Ron Rivest is one of the three inventors of RSA and, with Adi Shamir, the author of two micropayment systems that predate Bitcoin.

Received by the journal on April 4, 1977, the article by Rivest, Shamir, and Leonard Adleman that describes RSA appeared in 1978 in *Communications of the ACM*. It presents a method in which the key that encrypts is public and the one that decrypts stays secret, and in which a message is signed with the private key and verified with the public key. This is the idea of public key and digital signature on which Bitcoin rests, even though Bitcoin does not sign with RSA: it uses ECDSA, then Schnorr, on the secp256k1 curve.

In April 1996, Rivest and Shamir presented PayWord and MicroMint, two systems for paying very small amounts over the Internet while limiting public-key operations. PayWord relies on chains of values obtained with a hash function: the user signs the chain once, then reveals its links one by one to pay. MicroMint represents coins as hash collisions. The Bitcoin white paper does not cite this work: these remain earlier electronic payment systems.

Rivest received the 2002 Turing Award with Shamir and Adleman for their contribution to making public-key cryptography usable in practice.
