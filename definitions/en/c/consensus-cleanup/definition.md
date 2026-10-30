Soft fork proposal (BIP-0054) bundling several fixes for old vulnerabilities in Bitcoin's consensus rules. Rather than deploying one soft fork per bug, the Consensus Cleanup groups them to share the fixed cost of a consensus change. The proposal, championed by Antoine Poinsot and Matt Corallo, targets four distinct problems.

First, the time warp attack: by manipulating timestamps at the boundaries of difficulty adjustment periods, a majority attacker can artificially and unfairly lower the difficulty to its minimum within a few periods. The fix requires the first block of a period to have a timestamp at most 2 hours before that of the previous block, and the last block to have a timestamp at least equal to that of the first (no period of negative duration).

Second, block validation time: specifically crafted blocks can take more than an hour to validate on modest hardware. A limit of 2,500 potentially executed signature operations per transaction reduces the worst case by a factor of 40.

Third, the Merkle tree weakness: a 64-byte transaction can be mistaken for an intermediate node of the tree, making it possible to forge inclusion proofs. These transactions are made invalid.

Fourth, the duplication of coinbase transactions: some blocks that predate BIP-0034 contain a valid height commitment for a future block, which could create duplicates starting at block 1,983,702. Requiring an `nLockTime` equal to the height minus one in coinbases permanently removes the need for BIP-0030 validation. In October 2026, BIP-0054 has the status “Complete” in the BIP repository, but Bitcoin Core contains no activation deployment for this soft fork.
