Unique 32-byte identifier assigned to each asset issued via the Taproot Assets protocol. The asset ID is produced by hashing five concatenated elements with SHA-256: the outpoint of the genesis transaction (the one that creates the asset), a tag chosen by the issuer (for example, the hash of a brand name), the hash of the metadata associated with the asset (links, images, documents), the index of the output containing the Taproot Assets commitment in the genesis transaction, and the type of the asset (normal or collectible).

```
asset_id=sha256(genesis_outpoint‖asset_tag‖asset_meta_hash‖output_index‖asset_type)
```

Since it depends on the genesis outpoint, the asset ID is globally unique: two distinct issuances will always produce different identifiers. It serves as a key to look up an asset in a Universe, verify its provenance, and distinguish the different types of assets committed in the same Sparse Merkle Sum Tree.
