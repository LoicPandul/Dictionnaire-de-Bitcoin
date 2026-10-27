Indicators used to assess the degree of privacy of a particular UTXO. More precisely, they measure the number of indistinguishable UTXOs within the set that includes the coin under study. Since a group of identical UTXOs is needed, anonsets are generally calculated within a series of coinjoins. Where relevant, they make it possible to judge the quality of coinjoins. A large anonset means a higher level of anonymity, because it becomes difficult to single out a specific UTXO within the set. Two types of anonsets exist:
* The forward anonymity set;
* The backward anonymity set.

The first (forward anonset, also called forward-looking metrics) indicates the size of the group among which the output UTXO under study is hidden, given the input UTXO. This indicator measures how well the coin's privacy withstands a past-to-present analysis (input to output).

![Computing the forward anonset of a UTXO over three successive coinjoins: 4 + 4 + 5 = 13 indistinguishable UTXOs.](../../../fr/a/anonsets-anonymity-sets/assets/image-1.png)

The second (backward anonset, also called backward-looking metrics) indicates the number of possible sources for a given coin, given the output UTXO. This indicator measures how well the coin's privacy withstands a present-to-past analysis (output to input).

![Backward anonset: going back from the UTXO under study into the past, each stage of earlier coinjoins brings new Tx0 outputs, the possible sources of the coin, down to the genesis coinjoin.](../../../fr/a/anonsets-anonymity-sets/assets/image-2.png)

*Anonsets are also sometimes called "scores" (forward score and backward score).*
