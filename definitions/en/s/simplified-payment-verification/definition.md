Method that lets light clients verify Bitcoin transactions without downloading the entire blockchain. A node that uses SPV downloads only the block headers, which are much lighter than full blocks. When it needs to verify a transaction, the SPV node asks full nodes for a Merkle proof to confirm that the transaction is included in a specific block. This approach is efficient for devices with limited resources, such as smartphones, but it implies a dependence on full nodes, which can reduce security and increase the trust required.

*The acronym “SPV” is often used to refer to this method.*
