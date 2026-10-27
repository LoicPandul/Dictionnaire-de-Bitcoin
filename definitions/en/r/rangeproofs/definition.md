Type of zero-knowledge proof used in Confidential Transactions to demonstrate that a committed amount lies within a valid range, without revealing its exact value. Rangeproofs prevent a user from creating negative or excessively large amounts that would allow units of money to be fraudulently generated, while preserving the privacy of the transaction.

In the first implementations of Confidential Transactions on Liquid, rangeproofs relied on Borromean ring signatures. This mechanism is meant to be replaced by Bulletproofs++, which produce more compact proofs that are more efficient to verify.
