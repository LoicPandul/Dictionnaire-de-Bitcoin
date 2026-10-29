Open-source library written in Rust for handling Bitcoin protocol data structures and messages. It can serialize and deserialize transactions, blocks, and network messages, manage private keys, addresses, and BIP-0032 derivation, and work with PSBTs.

Rust Bitcoin is not designed for consensus validation: known and unknown discrepancies exist with the reference implementation, Bitcoin Core, which makes it unsuitable for a full node. It instead targets developers building wallets, explorers, analysis tools, or any software that interacts with the Bitcoin network without fully validating it.

The project, released under the CC0 license (public domain), comes with companion crates such as `bitcoin_hashes`, `secp256k1`, or `miniscript`, and works in a `no-std` environment for embedded systems.
