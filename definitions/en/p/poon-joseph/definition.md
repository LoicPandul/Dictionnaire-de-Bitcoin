Developer, coauthor with Thaddeus Dryja of the Lightning Network white paper and first to propose for Segregated Witness the `SIGHASH_NOINPUT` signature flag, already named in the white paper and ancestor of `SIGHASH_ANYPREVOUT`.

Draft 0.5 of "The Bitcoin Lightning Network", signed by Poon and Dryja, was online by February 28, 2015, and version 0.5.9.2, titled "The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments", is dated January 14, 2016. The text describes a network of payment channels: Alice can pay Dave through Bob and Carol without trusting them, thanks to contracts with decrementing timelocks, each of which can be enforced on-chain if a participant refuses to cooperate. It assumes a new sighash type that fixes transaction malleability.

On February 26, 2016, Poon wrote on bitcoin-dev, under the title "SIGHASH_NOINPUT in Segregated Witness", that a signature flag not covering the input's transaction ID or index would be useful to Lightning. It would let a third party in charge of monitoring a channel hold a single transaction valid for all earlier states, instead of receiving every signature one by one.

BIP-0118 takes up this flag, renamed `SIGHASH_ANYPREVOUT`, and credits Poon in its acknowledgments. The eltoo protocol depends on it.
