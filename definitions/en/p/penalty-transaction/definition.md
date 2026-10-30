Bitcoin transaction used on the Lightning Network to punish a peer that has published an old, revoked commitment transaction on the blockchain. It lets the wronged party recover all of the channel's funds, including the attacker's share.

The mechanism relies on revocation keys. When a channel state is updated, each party hands the other the secret of the old state (`per_commitment_secret`), from which the other party derives the revocation key that allows spending all of the funds if that state were ever published. If a node tries to cheat by broadcasting an old commitment, its peer has a delay in which to detect the fraud and build the penalty transaction using this revocation key. That delay is guaranteed by an `OP_CHECKSEQUENCEVERIFY` timelock on the cheater's output.

![Alice publishes a revoked commitment: her output stays locked for `to_self_delay` blocks by `OP_CHECKSEQUENCEVERIFY`, and Bob claims it before the delay ends with a penalty transaction signed by the revocation private key.](./assets/image-1.png)

Watchtowers are third-party services that monitor the blockchain around the clock to detect such frauds and broadcast penalty transactions on behalf of offline nodes.
