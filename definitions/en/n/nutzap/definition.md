Nostr payment defined by NIP-61: a Cashu token locked to its recipient, published in a Nostr event that itself serves as a receipt. It plays the role of the ZAP, but the payment is made in Cashu ecash and not over Lightning.

The token is a Cashu token, issued by a mint. The lock is the P2PK one: absent any additional condition (extra keys, expiration date), only the private key associated with a given public key can spend the proof.

To receive nutzaps, the recipient publishes a kind `10019` event. In it, they indicate with `relay` tags the relays where they will read payments, with `mint` tags the mints whose tokens they accept, and with a `pubkey` tag the P2PK key to lock to. This key must not be their main Nostr key: it corresponds to a private key kept, encrypted, in their NIP-60 Cashu wallet, a wallet whose state is stored on relays so that it follows them from one application to another.

Let's take an example. Alice likes a note by Bob and wants to send him 1 sat.

* Her client reads Bob's kind `10019` and finds his mints there.
* Alice creates a 1-sat token at one of these mints, or swaps tokens she already holds there, locked to Bob's P2PK key. The client adds the prefix `02` to this key, for compatibility between Nostr and Cashu.
* She publishes a kind `9321` event on Bob's relays. Its `proof` tags contain the proofs, each accompanied by its DLEQ proof, `u` gives the mint's URL, `unit` the unit (`sat` by default), `e` the note concerned, and `p` Bob's Nostr key. The `content` can carry a comment.
* Bob's client reads the kind `9321` events that mention him and swaps the tokens into a NIP-60 wallet, a Lightning wallet, or another. It preferably publishes in return a kind `7376` event, which records that the nutzap has been redeemed.

Unlike the zap, the recipient issues no Lightning invoice and no LNURL server is involved on their side: the NIP-57 zap goes through an LNURL-pay request and through a receipt that this server publishes. The nutzap fits entirely in the `9321` event, whose proofs are both the payment and the receipt.

Any observer can therefore check the authenticity of a nutzap without asking anyone, but only the mint says whether the token has already been spent. The observer checks that the recipient did publish a kind `10019` event that lists this mint, that the token is locked to the announced key, that the `u` tag matches one of the recipient's mints, and that the DLEQ proof is valid. These checks can be done offline, provided the mint's keys and the kind `10019` event are known.

The system has its pitfalls. The sender must stick to the mints that the recipient has listed: a token issued elsewhere may never be seen or spent, and NIP-61 warns that the sender risks burning their money. The recipient should likewise choose mints that support P2PK (NUT-11), otherwise they would receive nutzaps that anyone can spend, and DLEQ proofs (NUT-12), which allow offline verification.

NIP-61 was added to the NIP repository on October 25, 2024, along with NIP-60, in a commit by Pablo Fernandez, and has the status `draft`.

*NIP-61 also uses the expression "Cashu zap".*
