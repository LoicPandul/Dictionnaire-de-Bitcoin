Subset of transaction relay policy that gathers all the rules a Bitcoin node applies to determine which unconfirmed transactions it accepts into its mempool. Mempool policy includes the standardness rules, but extends beyond them by covering rules that take into account the context of the mempool as a whole, not only the format of individual transactions.

For example, the rules on the minimum relay fee rate (`minrelaytxfee`), the maximum mempool size (`maxmempool`), or the transaction replacement rules (RBF) fall under mempool policy. These rules are configured locally by each node and can vary from one node to another.

Mempool policy differs from standardness rules in that the latter concern only the format of a transaction taken in isolation, whereas mempool policy takes into account contextual factors such as mempool congestion, relationships between transactions, or the fee thresholds set by the node operator.
