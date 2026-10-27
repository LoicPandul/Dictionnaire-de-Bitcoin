In the RGB protocol, the set of data exchanged between parties, subject to client-side validation. There are two main categories of consignments:
* `Contract Consignment`: provided by the issuer (the contract's issuer), it includes the initialization information such as the schema, the genesis, the interface, and the interface implementation.
* `Transfer Consignment`: provided by the paying party (the payer). It contains the whole history of state transitions leading to the terminal consignment (that is, the final state received by the recipient).

These consignments are not recorded publicly in the blockchain; they are exchanged directly between the parties concerned over the communication channel of their choice.
