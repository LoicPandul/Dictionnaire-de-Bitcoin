In computing, the essential data carried in a larger data packet. For example, in a SegWit v0 address on Bitcoin, the payload is the hash of the public key (P2WPKH) or of the script (P2WSH), without the various metadata (the HRP, the separator, the SegWit version, and the checksum). The P2WPKH address `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` breaks down as follows:
* `bc`: the human-readable part (HRP);
* `1`: the separator;
* `q`: the SegWit version. Here, it is version 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa`: the payload, here the hash of the public key;
* `ys50gj`: the checksum.
