Intermediate account in the Whirlpool protocol that holds the UTXOs resulting from the Tx0 while they wait for their first coinjoin cycle. The premix is a transitional state: UTXOs stay there until they are selected to take part in a coinjoin transaction.

Each UTXO in the premix account holds exactly the nominal amount of the chosen pool (for example 0.01 BTC for the 0.01 pool), plus the mining fees needed for the first coinjoin cycle. These UTXOs are considered unmixed, because they are still directly traceable to the Tx0 that created them. They have not yet benefited from the link breaking that coinjoin provides.

Once a premix UTXO is selected for a coinjoin cycle and the transaction is confirmed, it moves to the postmix account.
