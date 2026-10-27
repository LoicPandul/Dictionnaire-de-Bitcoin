Indicator used to assess the privacy level of a Bitcoin transaction. The Boltzmann score is based on the number of possible interpretations of a transaction, that is, the number of plausible combinations between its inputs and outputs.

The principle is inspired by the statistical physics of Ludwig Boltzmann: the more possible combinations (microstates) a transaction admits, the higher its entropy, and the harder it is to analyze. The score is generally expressed in bits of entropy. A transaction with a score of 0 bits has only one possible interpretation (each input is clearly linked to an output). Conversely, a well-built coinjoin can reach a high score, because the multiple inputs and outputs of identical amounts generate a very large number of possible combinations.

This score lets users objectively assess the privacy effectiveness of a coinjoin, or of any transaction.
