Acronym for *Validating Lightning Signer*. Open-source Rust library that separates a Lightning node's private keys from the node software itself, moving them to a dedicated signing device. Before each cryptographic operation, VLS applies a set of more than fifty validation rules to check that the proposed transaction is safe.

If the node is compromised or attempts a malicious action, such as signing a revoked commitment transaction or closing a channel to an unauthorized address, VLS refuses to sign. This mechanism protects funds even if the node software is fully compromised.

VLS offers reference integrations for CLN and LDK. As of October 2026, the project website describes it as production-ready and audited; its version 0.14.0 dates from November 7, 2025.
