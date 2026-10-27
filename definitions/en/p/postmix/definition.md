Account that gathers the UTXOs that have taken part in at least one coinjoin cycle in the Whirlpool protocol. The postmix represents mixed funds whose link to their origin has been broken through the coinjoin process.

UTXOs in the postmix account benefit from anonsets that grow with each additional coinjoin cycle. The more remixes a UTXO takes part in (which are free in Whirlpool), the more its prospective and retrospective anonymity set grows, which strengthens its privacy.

Using postmix UTXOs requires particular care so as not to degrade the privacy gained. Merging postmix UTXOs with each other or with unmixed UTXOs can restore traceable links. Spends from the postmix are best made with privacy-preserving techniques such as Stonewall or Stonewall x2.
