Proposal written by Nils Schneider and Matt Corallo, based on BIP-0020 by Luke Dashjr, which itself came from another document by Nils Schneider. BIP-0021 defines how receiving addresses should be encoded in Uniform Resource Identifiers (URIs) to make payments easier. For example, a Bitcoin URI following BIP-0021 that requests 0.1 BTC under the label “Pandul” would look like this:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
``` 

This standardization improves the user experience of Bitcoin transactions by making it possible to click a link or scan a QR code to launch a payment with its parameters already filled in. BIP-0021 has `Closed` status: BIP-0321, which replaces it, takes up the same URI scheme.
