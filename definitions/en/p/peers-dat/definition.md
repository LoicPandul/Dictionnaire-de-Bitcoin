File in which Bitcoin Core serializes the tables of the `addrman` module: the "new" table (addresses discovered but not yet tested) and the "tried" table (addresses the node has already connected to successfully). It contains the IP addresses of other nodes, port numbers, last-connection timestamps, and the bucketing key (`nKey`) that determines the placement of addresses in the buckets.

On first launch, the file does not exist and the tables are empty: the node queries the DNS seeds to obtain an initial list of peers. As connections are made, addresses are inserted into the tables and `peers.dat` is updated periodically. Addresses can also be added manually with the `-addnode` option or the `addnode` RPC command.

This file replaced `addr.dat` as of Bitcoin Core 0.7.0 (2012), when Pieter Wuille introduced `addrman` with its deterministic bucketing system.
