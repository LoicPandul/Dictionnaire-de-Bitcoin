Cryptographic secret sharing scheme designed by Adi Shamir in 1979. It splits a secret into n distinct shares, such that a minimum of t shares is needed to reconstruct the original secret, while t-1 shares or fewer reveal no information about it. The (t, n) setting is defined when the shares are created.

![Shamir secret sharing with a threshold of 2 shares out of 4: two shares fix a single line that leads to the secret, while a single share leaves every line, and therefore every secret, possible.](./assets/image-1.png)

In the Bitcoin ecosystem, Shamir's secret sharing is used in several contexts. The Codex32 protocol, formalized in BIP-0093, relies on this scheme to allow the manual backup and reconstruction of seeds. It is also an option offered on Trezor hardware wallets. Threshold signature protocols such as FROST also rely on this mechanism during the distributed key generation phase.
