In the context of the RGB protocol, a set of client-side data used to prove the inclusion of a unique commitment in a transaction. An RGB anchor consists of the following elements:
* The Bitcoin transaction ID (txid) of the witness transaction;
* The proof of the Multi Protocol Commitment (MPC), including the depth, the cofactor, and the Merkle proof;
* The Extra Transaction Proof (ETP), which provides the additional data needed to validate a Tapret commitment (not required for Opret).

An anchor thus establishes a verifiable link between a specific Bitcoin transaction and private data validated by the RGB protocol. It guarantees that this data is indeed included in the blockchain, without its exact content being publicly exposed.
