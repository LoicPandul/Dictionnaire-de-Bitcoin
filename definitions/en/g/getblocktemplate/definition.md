Communication protocol between a Bitcoin node and mining software, defined in BIP-0022 and BIP-0023. It was introduced in 2012 to replace the `getwork` protocol, whose limitations were becoming a problem as the network's computing power grew.

Unlike `getwork`, which gave the miner a block header ready to hash, `getblocktemplate` sends a complete block template. The miner receives the list of transactions to include, the block parameters, and the consensus rules to follow. This approach lets the miner build the candidate block itself and choose which transactions go into it.

This change lets whoever builds the block select the transactions, instead of leaving that choice to the pool operator alone, provided the pool passes this template on to its miners. Between a pool and its miners, the Stratum protocol later replaced `getwork`, but `getblocktemplate` remains the RPC method through which Bitcoin Core provides a block template.
