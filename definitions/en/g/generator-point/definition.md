Fixed point on an elliptic curve that serves as the base for all public-key cryptography operations. In Bitcoin, the generator point `G` is a standard parameter of the secp256k1 curve, defined deterministically. All Bitcoin users share the same generator point `G`. It is a public, universal parameter of the secp256k1 curve. Its coordinates are:

```
x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
```

The generator point is the basis of public key derivation: a private key `k` (an integer) is associated with a public key `K` by scalar multiplication on the elliptic curve: `K = k * G`. This operation is easy to compute in one direction but practically impossible to reverse (the elliptic curve discrete logarithm problem).
