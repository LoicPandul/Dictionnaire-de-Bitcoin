Cryptographic function used on Bitcoin notably to generate Legacy and SegWit v0 receiving addresses. It combines two hash functions run successively on the input: first SHA256, then RIPEMD160. The output of this function is therefore 160 bits.
$$HASH160(x)\ =\ RIPEMD160(SHA256(x))$$
