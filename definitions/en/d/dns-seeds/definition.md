Initial connection points for new Bitcoin nodes joining the network. These seeds, which are in fact specific DNS servers, have their addresses permanently built into the Bitcoin Core code. When a new node starts, it contacts these servers to get a random list of IP addresses of Bitcoin nodes that are presumably active. The new node can then establish connections with the nodes on this list to get the information it needs for its initial block download (IBD) and to synchronize to the chain with the most accumulated work. As of October 2026, here is the list of Bitcoin Core's mainnet DNS seeds and the people responsible for maintaining them (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* dnsseed.bluematt.me: Matt Corallo;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS seeds are the second means, in order of priority, for a Bitcoin node to establish connections. The first means is to use the `peers.dat` file that the node itself created. This file is naturally empty for a new node, unless the user has modified it manually.

*Note that DNS seeds should not be confused with "seed nodes," which are the third way of establishing connections.*
