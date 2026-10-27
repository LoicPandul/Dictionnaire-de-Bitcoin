First block of the Bitcoin system. It marks the concrete launch of Bitcoin. The genesis block was created by Bitcoin's anonymous founder, Satoshi Nakamoto, on January 3, 2009. Its hash is:

```text
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

This block contains only one coinbase transaction, which generates 50 bitcoin as a reward for the miner (in this case, Satoshi Nakamoto himself). The block includes a message embedded in the coinbase transaction:

```text
The Times 03/Jan/2009 Chancellor on brink of second bailout for banks
```

This quote refers to an article in the newspaper *The Times*. The message is read as a criticism of the traditional financial system and its excesses, which partly motivated the creation of Bitcoin as a monetary alternative.

Because it is the very first block of the Bitcoin blockchain, the genesis block has a field for the hash of the previous block, but that field is filled with zeros, since there is no previous block. Also, the 50 bitcoin generated as a reward in this block cannot be spent at the protocol level.
