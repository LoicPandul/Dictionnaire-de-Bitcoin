Secondary wallet designed to provide plausible deniability under physical coercion. When a user is forced to unlock their signing device under threat (a scenario known as the "$5 wrench attack"), the user enters a special PIN known as the "duress PIN" that opens a wallet holding a reduced amount. The attacker cannot determine whether another wallet exists on the device.

The duress wallet is derived from a seed or a derivation path distinct from the main wallet's. Its interface and behavior are identical, which makes the two impossible to tell apart. On some signing devices such as the Coldcard, this feature relies on a dedicated PIN; on other devices, the BIP-0039 passphrase plays a similar role by giving access to an entirely different wallet depending on the passphrase entered.

The principle assumes keeping a credible balance in the duress wallet so that the decoy is convincing.
