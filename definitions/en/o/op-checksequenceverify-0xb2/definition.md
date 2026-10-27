Makes the transaction invalid if any one of these characteristics is observed:
* The stack is empty;
* The value at the top of the stack is less than `0`;
* The disable flag of the value at the top of the stack is not set, and any of the following holds: the transaction version is less than `2`; the disable flag of the input's `nSequence` field is set; the timelock type is not the same for the `nSequence` field and the value at the top of the stack (real time or number of blocks); the value at the top of the stack is greater than the value of the input's `nSequence` field.

If one or more of these characteristics is observed, the script containing the `OP_CHECKSEQUENCEVERIFY` cannot be satisfied. If all of the conditions are valid, `OP_CHECKSEQUENCEVERIFY` acts as an `OP_NOP`, that is, it does nothing to the script. It is as if it disappeared. `OP_CHECKSEQUENCEVERIFY` therefore imposes a relative time constraint on spending the UTXO secured by the script that contains it. It can do so either as real time or as a number of blocks. To do this, it restricts the possible values of the `nSequence` field of the input that spends it, and that `nSequence` field in turn restricts when the transaction that includes this input can be included in a block.

*This opcode is a replacement for `OP_NOP`. It was placed on `OP_NOP3`. It is often referred to by its acronym, "CSV". Note that `OP_CSV` must not be confused with the `nSequence` field of a transaction. The former uses the latter, but their natures and actions are different.*
