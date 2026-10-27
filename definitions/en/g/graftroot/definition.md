Bitcoin protocol improvement proposal formulated by Gregory Maxwell in February 2018. Graftroot extends the concept of Taproot by adding a mechanism for delegating spending conditions. With Taproot, a group of participants sharing an aggregated key can either spend directly with that key or reveal an alternative script contained in a Merkle tree. Graftroot also lets these participants delegate their ability to spend to arbitrary scripts by signing those scripts with their aggregated key.

The main benefit of this protocol is that there is no limit on the number of alternative spending conditions. Each delegation takes the form of a single Schnorr signature over the authorized script, with no extra cost proportional to the number of delegated scripts. In Taproot, adding branches to the Merkle tree increases the size of the spending proof, whereas Graftroot keeps the cost constant.

Graftroot was never formalized as a BIP and was not integrated into the Bitcoin protocol.
