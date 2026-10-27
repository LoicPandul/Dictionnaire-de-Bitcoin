Acronym for *Exclusive Or*, an operation that is a fundamental function of Boolean logic. It takes two Boolean operands, each being $true$ or $false$, and produces a $true$ output only when the two operands differ. In other words, the output of the XOR operation is $true$ if exactly one (but not both) of the operands is $true$. For example, the XOR of $1$ and $0$ gives $1$. It is written:
$$
1 \oplus 0 = 1
$$

Likewise, the XOR operation can be applied to longer sequences of bits. For example:
$$
10110 \oplus 01110 = 11000
$$

Each bit of the sequence is compared with its counterpart and the XOR operation is applied. Here is the truth table of the XOR operation:

| $A$ | $B$ | $A \oplus B$ |
|:---:|:---:|:------------:|
| $0$ | $0$ |      $0$     |
| $0$ | $1$ |      $1$     |
| $1$ | $0$ |      $1$     |
| $1$ | $1$ |      $0$     |

The XOR operation is used in many areas of computing, notably in cryptography, for useful properties such as:
* Commutativity: the order of the operands does not affect the result. For two given variables $D$ and $E$: $D \oplus E = E \oplus D$;
* Associativity: the grouping of the operands does not affect the result. For three given variables $A$, $B$, and $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
* It has an identity element $0$: an operand XORed with $0$ is always equal to the operand. For a given variable $A$: $A \oplus 0 = A$;
* Each element is its own inverse. For a given variable $A$: $A \oplus A = 0$.

In Bitcoin, the XOR operation is used in many places. For example, XOR is used extensively in the SHA256 function, itself widely used in the Bitcoin protocol. Some protocols, such as Coldcard's SeedXOR, also use this primitive for other applications. It is also found in BIP-0047, to encrypt the reusable payment code when it is transmitted.

In the more general field of cryptography, XOR can be used as is as a symmetric encryption algorithm. This algorithm is called the "one-time pad" or the "Vernam cipher," after its inventor. Although useless in practice because of the key length, this algorithm is one of the only encryption algorithms recognized as unconditionally secure.
