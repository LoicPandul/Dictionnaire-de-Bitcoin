bLIP that defines LSPS1, a standardized API that lets Lightning wallets buy payment channels from Lightning service providers (LSPs). The process takes place in three steps:
* the client queries the LSP's available options through `lsps1.get_info`,
* it creates an order with the desired parameters (capacity, duration, balance split) through `lsps1.create_order`,
* then it pays through a BOLT-11 invoice, a BOLT-12 offer, or an on-chain payment.

The LSP then opens the requested channel. The specification supports public and private channels and zero-confirmation channels, and provides for an automatic refund if the opening fails. LSPS1 relies on the LSPS0 transport layer of bLIP-0050.
