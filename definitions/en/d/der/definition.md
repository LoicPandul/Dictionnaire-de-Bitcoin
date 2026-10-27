Acronym for *Distinguished Encoding Rules*. It is a strict subset of the ASN.1 encoding rules defined in the [ITU-T X.690, 2002](https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf) specification and is used to encode any type of data into a binary sequence. DER is mostly used in specific fields, such as cryptography, where data must be encoded in a standard and predictable way.

On Bitcoin, ECDSA signatures are encoded in DER format. They consist of two encoded numbers (`r`, `s`). The signature format consists of the following elements:

```text
0x30 | length |  0x02 | r-length | r | 0x02 | s-length | s
```

With:
* `0x30` (1 byte): identifier of a constructed structure;
* `length` (1 byte): length of the following data;
* `0x02` (1 byte): identifier of an `INTEGER` data type (whole number);
* `r-length` (1 byte): length of the following `r` value (usually 32 or 33 bytes);
* `r` (variable): the `r` value as a big-endian integer;
* `0x02` (1 byte): identifier of an `INTEGER` data type (whole number);
* `s-length` (1 byte): length of the following `s` value (usually 32 or 33 bytes);
* `s` (variable): the `s` value as a big-endian integer.

In a Bitcoin transaction, one byte is added at the end of a DER signature to indicate the SigHash type used.
