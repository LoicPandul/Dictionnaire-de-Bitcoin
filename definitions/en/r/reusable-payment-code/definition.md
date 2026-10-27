Static identifier defined in BIP-0047, generated from a Bitcoin wallet, that makes it possible to initiate a notification transaction and derive unique addresses. This avoids address reuse, which leads to a loss of privacy, without having to manually derive and send a new blank address for each payment. In BIP-0047, reusable payment codes are built as follows:
* Byte 0 is the version;
* Byte 1 is a bit field that allows adding information for specific uses;
* Byte 2 indicates the parity of the `y` of the public key;
* From byte 3 to byte 34 is the `x` value of the public key;
* From byte 35 to byte 66 is the chain code associated with the public key;
* From byte 67 to byte 79 is zero padding.

A version byte (`0x47`) is generally added at the start of the payment code and a checksum at the end, then the whole is encoded in Base58Check. Building a payment code is thus quite close to building an extended key. Here, for example, is my former BIP-0047 payment code in Base58Check:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

In the PayNym implementation of BIP-0047, payment codes can also be expressed as identifiers associated with the image of a robot. Here is my former one, for example:

```text
+throbbingpond8B1
```

In 2026, payment codes with the PayNym implementation are available in Sparrow Wallet on desktop and in Ashigaru on mobile (a fork of Samourai Wallet, whose servers were seized by US authorities in April 2024).
