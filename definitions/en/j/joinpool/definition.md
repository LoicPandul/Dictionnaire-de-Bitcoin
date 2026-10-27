Type of layer 2 payment system based on shared ownership of one or more UTXOs, with no need for trust. When funds leave a pool in this type of system, it must be impossible to determine on-chain which user made the spend.

The fundamental principle of a joinpool-type system is therefore UTXO sharing to improve how Bitcoin scales: rather than each participant owning one or more individual UTXOs, a single UTXO represents the funds of the whole group. Each member retains the ability to unilaterally withdraw their funds at any time, either through pre-signed transactions or through mechanisms proposed at the protocol level such as covenants. Without covenants, the interactivity required among participants grows significantly, because any change to the pool's state requires the signatures of all members.

The Ark protocol can be considered a concrete implementation of the joinpool concept, in which an Ark Service Provider acts as coordinator and liquidity provider for the pool's participants.

This type of system is sometimes also called a "coinpool" or "payment pool".
