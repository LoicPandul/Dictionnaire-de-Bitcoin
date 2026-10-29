Developer and researcher, coauthor with Joseph Poon of the Lightning Network white paper, and author of Discreet Log Contracts and of the Utreexo accumulator. He goes by the first name Tadge.

Draft 0.5 of "The Bitcoin Lightning Network," authored by Poon and Dryja, was online by February 28, 2015, and version 0.5.9.2, titled "The Bitcoin Lightning Network: Scalable Off-Chain Instant Payments," is dated January 14, 2016. The text proposes linking payment channels into a network: Alice can pay Dave through Bob and Carol without trusting them, thanks to contracts with decrementing timelocks, enforced on-chain if a participant refuses to cooperate or cheats.

In 2017, Dryja worked at the MIT Digital Currency Initiative on lit, Lightning node software. There he described Discreet Log Contracts (DLCs), which he presented at Scaling Bitcoin at Stanford in November 2017. An oracle publishes a key point and a nonce point in advance, then later signs the value of an event (a price, the weather). That signature, added to the winner's private key, gives the winner the private key that unlocks their payout, and on-chain, the contract looks like an ordinary multisig output.

On June 3, 2019, he filed the paper "Utreexo: A dynamic hash-based accumulator optimized for the Bitcoin UTXO set" on ePrint as sole author. A node no longer stores the full UTXO set, but a hash-based accumulator whose size grows logarithmically, and each transaction carries the inclusion proof for its inputs.

In 2025, he coauthored with Calvin Kim and Davidson Souza three BIP drafts on Utreexo, numbered 181 to 183, including BIP-0181 for the accumulator.
