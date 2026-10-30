Technique proposed by René Pickhardt in 2019 that lets a Lightning routing node rebalance its channels on the fly to forward a payment that would otherwise have been rejected for lack of sufficient liquidity on the outgoing channel. The term “JIT” (just-in-time) indicates that rebalancing is triggered at the precise moment the incoming HTLC arrives, not preventively.

In practice, when an intermediate node receives an HTLC to forward but lacks funds on the outgoing channel, it briefly suspends the relay and makes a circular payment through its other channels to move the necessary liquidity. The node uses its local knowledge of the network to quickly compute low-cost rebalancing cycles. If rebalancing succeeds and the fees incurred are lower than the routing fees earned, the operation is profitable.

JIT routing requires no protocol change: it is local behavior that each routing node can adopt independently.

This mechanism should not be confused with JIT channels, which refer to the on-the-fly opening of a channel by an LSP.
