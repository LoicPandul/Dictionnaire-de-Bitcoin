In the context of Bitcoin, attack in which a transaction valid on one blockchain is maliciously reproduced on another blockchain that shares the same transaction history. In other words, a transaction broadcast on one chain can be replicated on another without the consent of the sender of the first transaction.

Let's take the example of a hypothetical Bitcoin hard fork named "BitcoinBis". If Alice pays in bitcoin to buy a baguette from a baker on the real Bitcoin blockchain, the same baker could replay this legitimate transaction on BitcoinBis to receive the same amount of cryptocurrency on that fork, without any action from Alice.

This type of attack can only occur when the blockchain splits into 2 independent chains that persist over time. Typically, this happens with a hard fork. For a replay attack to be possible, the 2 blockchains must share a common history, and the duplicated transaction must spend as inputs UTXOs created by earlier transactions that took place before the two chains split, or by earlier transactions that were themselves already replayed in a previous replay attack.

More generally, in computing, a replay attack consists of intercepting and reusing valid data to fool a system by repeating the original transmission. This can sometimes lead to identity spoofing on a network.

*A replay attack on a Bitcoin transaction is sometimes simply called a "transaction replay".*
