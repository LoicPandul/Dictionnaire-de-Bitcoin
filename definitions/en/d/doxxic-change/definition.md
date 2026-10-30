Change output from a Tx0 transaction in the Whirlpool protocol, which poses a risk to the user's privacy. Doxxic change is the portion of bitcoin that cannot be included in the chosen coinjoin pool and that returns to the wallet as change.

This change is called “doxxic” (a portmanteau of “toxic” and “doxx,” meaning to expose someone's identity) because it keeps a direct link to the Tx0, and therefore potentially to the user's identity or history. If this change is spent carelessly, for example by merging it with postmix UTXOs, it can compromise the privacy gained during the coinjoin cycles.

To limit this risk, doxxic change can be spent separately (for example on gift cards, through donations, or on Lightning), used in a new Tx0, or consolidated via atomic swaps on Monero.
