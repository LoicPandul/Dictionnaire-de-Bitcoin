Structured expression that fully describes an output script (`scriptPubKey`) and provides all the information needed to track transactions to or from a particular script. Output script descriptors, or simply descriptors, make key management in HD wallets easier through a standard description of the structure and the address types used.

The main value of descriptors lies in their ability to encapsulate all the information essential to restoring a wallet in a single string (in addition to the mnemonic phrase). By backing up a descriptor along with the corresponding mnemonic phrases, it is possible to restore not only the private keys but also the precise structure of the wallet and the associated script parameters. Indeed, recovering a wallet requires knowing not only the initial seed but also the specific indexes used to derive child key pairs, as well as the `xpub` of each cosigner in a multisig wallet. In the past, this information was presumed to be implicitly known to everyone. However, with the diversification of scripts and the emergence of more complex setups, this information may become hard to extrapolate, turning this data into private information that is hard to brute-force. Using descriptors greatly simplifies the process: it is enough to know the mnemonic phrase or phrases and the corresponding descriptor to restore everything reliably and securely.

A descriptor is made up of several elements:
* Script functions such as `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (multisignature), and `sortedmulti` (multisignature with sorted keys);
* Derivation paths, for example `[d34db33f/44h/0h/0h]`, which indicates a derived path and a specific master fingerprint;
* Keys in various formats, such as hexadecimal public keys or extended public keys (`xpub`);
* A checksum, preceded by a hash sign, to verify the integrity of the descriptor.

For example, a descriptor for a P2WPKH wallet might look like:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

In this descriptor, the `wpkh` function indicates a Pay-to-Witness-Public-Key-Hash script type. It is followed by the derivation path, which contains:
* `cdeab12f`: the fingerprint of the master key;
* `84h`: meaning that a BIP-0084 purpose is used, intended for SegWit v0 addresses;
* `0h`: indicating the BTC coin type on mainnet;
* `0h`: referring to the specific account number used in the wallet.

The descriptor also includes the extended public key used in this wallet:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Next, the notation `/<0;1>/*` specifies that the descriptor can generate addresses from the external keychain (`0`) and the internal keychain (`1`), with a wildcard (`*`) allowing the sequential derivation of multiple addresses in a configurable way, similar to managing a "gap limit" in conventional wallet software.

Finally, `#jy0l7nr4` represents the checksum used to verify the integrity of the descriptor.
