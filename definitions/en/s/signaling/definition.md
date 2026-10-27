Mechanism by which miners indicate their support for, or readiness for, a soft fork proposal on Bitcoin. Signaling is done by setting a specific bit in the `nVersion` field of the header of the blocks they mine, following the process defined by BIP-0009 (and its successors such as BIP-0008).

Each bit of the version field can be associated with a distinct soft fork proposal. When a miner sets the corresponding bit, it signals that it has updated its software and is ready to enforce the new rules.
