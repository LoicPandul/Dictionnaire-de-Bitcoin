UTXO management strategy that consists of selecting a transaction's inputs so as to eliminate or minimize the need to create a change output. The goal is to match the sum of the inputs as closely as possible to the payment amount plus the transaction fees.

The main benefit of this approach is privacy. A change output is often identifiable by chain analysis tools and gives away information for tracing funds over time. By eliminating it, the information available to an outside observer is reduced, no information is revealed in the future through the common-input-ownership heuristic (CIOH), and chain analysis can also be misled.

Some wallets implement this strategy automatically in their coin selection algorithm.
