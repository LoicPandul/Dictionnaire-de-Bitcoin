Cryptographic function used for various applications on Bitcoin. It consists of applying the SHA256 function twice to the input data. The message is passed through SHA256 a first time, and the result of that operation is used as the input for a second pass through SHA256. The output of this function is therefore 256 bits.
$$HASH256(x)\ =\ SHA256(SHA256(x))$$
