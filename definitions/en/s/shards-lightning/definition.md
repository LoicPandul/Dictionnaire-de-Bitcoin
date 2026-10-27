In multi-path payments (MPP) or atomic multi-path payments (AMP), a shard is a fraction of an overall payment. Each shard is a part of the total payment that is routed separately along a different route on Lightning.

In MPP, all shards share the same secret, whereas in AMP, each shard has a unique partial secret. The recipient collects the shards to reconstitute and finalize the complete payment. This mechanism works around the liquidity limits of a single channel.
