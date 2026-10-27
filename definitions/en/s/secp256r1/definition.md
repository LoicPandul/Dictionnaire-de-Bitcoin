Name given to an elliptic curve defined by the NIST standard for public-key cryptography. It uses a 256-bit prime field and an elliptic curve equation $y^2 = x^3 + ax + b$ with the constants:

```text
a=-3
```

and

```text
b=41058363725152142129326129780047268409114441015993725554835256314039467401291
```

The `secp256r1` curve is widely used in many protocols, but it is not used in Bitcoin. Satoshi Nakamoto opted for the `secp256k1` curve, which was little known in 2009. The precise reason for this choice is unknown, but it may have been to minimize the risk of backdoors. The parameters of the $k1$ curve are indeed much simpler than those of the $r1$ curve, in particular the constant $b$.

*This curve is sometimes also called "P-256".*
