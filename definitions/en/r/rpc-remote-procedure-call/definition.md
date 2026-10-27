Computing protocol that lets a program execute a procedure on another, remote computer as if it were executed locally.

Specifically in Bitcoin, it is used to let applications interact with `bitcoind`. It can run commands on a Bitcoin node, such as sending transactions, managing wallets, or reading blockchain data. The security of this interaction is ensured by authentication through a `.cookie` file or credentials, so that only authorized clients can make RPC calls on the node.
