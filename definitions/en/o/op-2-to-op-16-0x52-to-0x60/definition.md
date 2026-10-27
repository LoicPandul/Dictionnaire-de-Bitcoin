The opcodes from `OP_2` through `OP_16` push the respective numeric values from 2 to 16 onto the stack. They are used to simplify scripts by allowing small numeric values to be inserted. This type of opcode is notably used in multisig scripts. Here is an example of a `scriptPubKey` for a 2-of-3 multisig:

```text
OP_2
<Public key A>
<Public key B>
<Public key C>
OP_3
OP_CHECKMULTISIG
```

All of these opcodes are sometimes also named `OP_PUSHNUM_N`.
