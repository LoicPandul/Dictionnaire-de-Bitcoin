Closing of a Lightning channel carried out with the mutual agreement of both parties. It is the most advantageous closing method: the two channel partners jointly sign a closing transaction that redistributes the funds to their respective addresses, without a timelock.

Unlike a force close, where a unilateral commitment transaction is broadcast and imposes a timelock before the funds of the party who broadcast it become accessible, a cooperative close produces a simple transaction. Mining fees are therefore lower (since they can be adjusted to the current fee market), and the funds are available as soon as the transaction is confirmed.

![From the same 100,000-sat channel, the cooperative close signed by Alice and Bob releases both balances upon confirmation, whereas the force close broadcast by Alice locks her own share for 144 blocks.](../../../fr/c/cooperative-close/assets/image-1.png)
