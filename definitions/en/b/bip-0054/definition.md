Proposal (status `Complete` in the BIP repository in 2026) for a set of fixes to vulnerabilities in the consensus rules of Bitcoin, known as “Consensus Cleanup”. BIP-0054 does the following:
* it fixes the time warp attack by imposing constraints on block timestamps at the boundaries of difficulty adjustment periods;
* it limits block validation time by capping the number of signature operations per transaction;
* it invalidates 64-byte transactions to fix the weaknesses of the Merkle tree;
* and it requires the `nLockTime` field to be used in coinbase transactions, which removes the need for BIP-0030 validation.

This soft fork aims to reduce the attack surface of the protocol by cleanly fixing known, documented historical bugs, without changing its basic operation.
