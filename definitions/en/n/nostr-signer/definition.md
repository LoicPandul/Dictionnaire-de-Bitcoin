Software or device that holds a Nostr user's private key and signs their events at the request of clients, without ever handing the key over to them. It also answers encryption and decryption requests that require this key. The client (see NOSTR CLIENT) prepares the event, the signer signs it, and the client publishes it.

The purpose of a signer is to limit the places where the key exists. NIP-46 lays out the principle: a private key should be exposed to as few systems as possible (applications, operating systems, devices), since each one widens the attack surface. Without a signer, Alice pastes her `nsec` into every client she tries, and it takes only one malicious client for her to lose her identity. With a signer, the key stays in one place and clients only see the signatures (see NOSTR EVENT SIGNATURE).

Three NIPs describe how a client talks to its signer, depending on where the signer runs.

* NIP-07, for a web page: a browser or an extension exposes a `window.nostr` object. It offers `getPublicKey()` and `signEvent(event)`, and optionally `nip04.encrypt` and `nip04.decrypt` (NIP-04, deprecated) as well as `nip44.encrypt` and `nip44.decrypt` (see NIP-44 ENCRYPTION). The site checks that the object exists, then calls it. The nos2x extension, by fiatjaf, implements it for Chromium browsers.
* NIP-55, for Android: the signer is an application on the same phone. The client sends it a request through an Android intent, and the user approves in the signer; for permissions the user has chosen to remember, a request through a Content Resolver, to the signer's Content Provider, succeeds in the background without opening the application. A web client can also call it through a `nostrsigner:` URL. Amber is one example.
* NIP-46, for a remote signer: the client and the signer exchange events encrypted through relays (see NOSTR BUNKER). This is the route NIP-55 recommends for web applications, since approval windows are less frequent there.

Let's take an example with NIP-07. Alice opens a web client and clicks “Publish”. The client builds a kind `1` event with her text, date, and tags, without `id`, `pubkey`, or `sig`, and calls `window.nostr.signEvent`. The extension displays the request; Alice approves; the extension computes the ID, adds the public key and the signature, and returns the complete event. The client then sends it to the relays.

The signer protects only the key, not the user's decisions. It signs what Alice approves, and a permission granted too broadly makes it sign without her knowing. Permissions are therefore set per method and per kind: both NIP-46 and NIP-55 let the client ask, for example, for the signing of reactions or notes, and a signer like Amber can then allow reactions without confirmation and ask for approval for each note. A compromised signer exposes the key itself, like any software that holds it (see ncryptsec for backing it up encrypted).

NIP-07 was published by fiatjaf on May 6, 2022. NIP-55 was proposed by greenart7c3, the author of Amber, on November 8, 2023 under number 100, then renumbered 55 on June 5, 2024. NIP-46 entered the NIPs repository on February 20, 2023.

*A Nostr signer should not be confused with the client, which builds the events and publishes them but does not hold the key.*
