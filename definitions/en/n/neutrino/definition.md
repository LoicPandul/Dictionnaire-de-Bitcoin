Bitcoin light client written in Go and developed by Lightning Labs. Designed for mobile applications using the Lightning Network, Neutrino implements the compact block filters protocol defined in BIP-0157 and BIP-0158 to synchronize the blockchain while minimizing bandwidth and storage.

Neutrino downloads only block headers and compact filter headers. Filters and full blocks are fetched on demand when a match is detected against the watched scripts. It offers rescan features to scan the blockchain for relevant transactions, as well as a `GetUtxo` function to check the existence and spend status of an output.

Neutrino is notably used as a backend by LND for light setups that do not need a full Bitcoin Core node. The term "Neutrino" is sometimes loosely used to refer to the BIP-0157/0158 protocol itself, when it names only this specific client library.
