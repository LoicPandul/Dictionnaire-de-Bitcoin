Version of Miniscript for Tapscript. Tapscript differs from the original version of Script in a few notable ways. For example, the opcodes `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` are disabled in it (BIP-0342), so the Miniscript fragment `multi`, which uses them, is replaced by `multi_a`, built with `OP_CHECKSIG` and `OP_CHECKSIGADD`. MiniTapscript thus provides Tapscript support in Miniscript, as described in BIP-0379. Its reference implementation has been available in Bitcoin Core since version 26.0.

*This term is sometimes disputed, as some bitcoiners prefer "TapMiniscript".*
