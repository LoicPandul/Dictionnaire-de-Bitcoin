Metric used in chain analysis, derived from Shannon entropy and invented by LaurentMT. It measures analysts' lack of knowledge about the exact configuration of a Bitcoin transaction. In other words, the higher a transaction's entropy, the harder it becomes for analysts to identify the movements of bitcoin between inputs and outputs.

In practice, entropy reveals whether, from an outside observer's point of view, a transaction has multiple possible interpretations, based solely on the amounts of the inputs and outputs, without taking other external or internal patterns and heuristics into account. High entropy therefore means better privacy for the transaction.

Entropy is defined as the binary logarithm of the number of possible combinations. Here is the formula used, with $E$ the transaction's entropy and $C$ the number of possible interpretations:
$$
E = \log_2(C)
$$

Taking into account the values of the UTXOs involved in the transaction, the number of interpretations $C$ represents the number of ways the inputs can be associated with the outputs. In other words, it determines how many interpretations a transaction can give rise to from the point of view of an outside observer analyzing it.
