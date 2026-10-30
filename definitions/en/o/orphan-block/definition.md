Block received by a node that has not yet acquired its parent block, that is, the previous one in the chain, in the theoretical sense of the term. Older versions of Bitcoin Core kept it aside while waiting for the parent; since version 0.10, which downloads headers first, the node rejects this block (`prev-blk-not-found`).

However, in common usage, the expression “orphan block” often refers to a block without a child: a valid block that is not retained in the main chain of Bitcoin. It occurs when two miners find a valid block at the same chain height within a short time and broadcast it on the network. Nodes eventually choose a single block to include in the chain, following the principle of the chain with the most accumulated work, which makes the other one “orphaned”.

![The two meanings of “orphan block”: in the strict sense, a node that knows the chain up to block 144 receives block 146 without knowing its parent 145 and first requests the missing header; in common usage, after a fork at height 145, the chain keeps 145-B and then 146, and 145-A is left without a child, called orphaned or stale.](../../../fr/o/orphelin/assets/image-1.png)

*Personally, I prefer to use the term “orphan block” for a block without a parent and the term “stale block” for a block that has no child. I find this more logical and understandable, although most bitcoiners do not follow this usage.*
