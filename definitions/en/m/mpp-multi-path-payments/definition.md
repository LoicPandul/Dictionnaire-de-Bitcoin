Generic term for all payment techniques on Lightning that split a transaction into several smaller parts and route them along different routes. In other words, each payment shard takes a different path of nodes. This works around the liquidity limits of a single channel in the route.

![Alice splits a 90,000 sat payment into three 30,000 sat shards that take three different routes at the same time and come together at Bob, to whom the total is announced.](../../../fr/m/mpp-multi-path-payments/assets/image-1.png)

Multi-path payments also offer slight privacy benefits, because it becomes harder for an observer to link each payment shard to the whole transaction. However, in the basic version, all the shards share the same secret for the HTLCs, which can make the transaction traceable if an observer is present on several routes. Moreover, because the secret is the same for all the shards of the payment, the payment is not atomic in the strict sense. The specifications require the recipient to reveal the preimage only after receiving all the shards, but nothing cryptographically forces it to: a dishonest recipient could claim only part of the payment. These drawbacks are fixed by Atomic Multi-Path Payments.

*The same method is sometimes called “Multi-Part Payment”.*
