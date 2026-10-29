Electrum server implementation written in C++ by Calin Culianu, initially for Bitcoin Cash, and released under the GPLv3 license. Fulcrum indexes every transaction of the Bitcoin blockchain from a full node and answers queries from wallets compatible with the Electrum protocol.

Designed as a high-performance replacement for ElectrumX, Fulcrum uses a RocksDB database and takes advantage of the multithreaded, asynchronous programming of C++20 to deliver fast response times, even under heavy load. It requires a Bitcoin Core (or Bitcoin Knots) node configured with `txindex=1` and without pruning.

The initial synchronization of the index with the blockchain takes far longer than with Electrs, and its index took up about 133 GB for Bitcoin in August 2023, according to the project's README. In return, it is much faster in use, whereas Electrs is slower but stands out for its lightness.
