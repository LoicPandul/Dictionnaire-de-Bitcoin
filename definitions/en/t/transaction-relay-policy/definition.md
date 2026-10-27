Subset of relay policy that gathers all the rules a Bitcoin node applies specifically to the handling and retransmission of transactions on the peer-to-peer network. Transaction relay policy notably includes mempool policy and, by extension, the standardness rules.

These rules determine whether a transaction received from a peer will be accepted, stored in the mempool, and then relayed to the other nodes of the network. They go beyond the format of individual transactions (covered by the standardness rules) and also include considerations related to network management.

Like all policy rules, transaction relay policy is configured locally by each node and can vary from one node to another. It differs from relay policy in the broad sense, which also covers aspects unrelated to transactions, such as the handling of blocks or the management of connections with peers.
