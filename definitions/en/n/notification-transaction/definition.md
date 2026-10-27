Specific Bitcoin transaction used in the BIP-0047 protocol (reusable payment codes). The notification transaction is the first step needed to establish a payment link between two users through their respective payment codes.

In practice, when Alice wants to send payments to Bob using his payment code, she must first send him a notification transaction. This transaction contains, in an `OP_RETURN` output, Alice's payment code encrypted with a shared secret calculated with ECDH (Elliptic-Curve Diffie-Hellman). By monitoring his notification address, Bob can decrypt this information and discover Alice's payment code. He can then derive the corresponding addresses to identify Alice's future payments.

The notification transaction needs to be sent only once for each pair of users. Subsequent payments between Alice and Bob no longer require this step.
