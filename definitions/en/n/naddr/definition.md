Shareable identifier defined by NIP-19 that designates an addressable event by its coordinate, that is, its kind, the public key of its author, and the value of its `d` tag, with optional relays where it can be found. Because it contains the identifier of no specific version, the link leads to the latest version that the queried relay has received of the article or list it designates.

This format addresses a particularity of addressable events (kinds `30000` to `39999`). For each combination of a kind, a public key, and a `d` tag value, NIP-01 asks relays to keep the latest version, and allows them to discard earlier ones. Yet each modification produces a new event, with a new identifier. An NEVENT, which points to an identifier, would therefore lead to a version that relays may have deleted. The `naddr` points to the coordinate, which does not change from one version to the next.

The `naddr` reuses the TLV structure of the NEVENT, with types whose meaning changes:

* type `0`: the value of the `d` tag, as text, or an empty string to designate an ordinary replaceable event, whose address consists only of the kind and the author;
* type `1`, optional and repeatable: the URL of a relay where the event can be found;
* type `2`: the 32 bytes of the author's public key;
* type `3`: the kind, as a 32-bit unsigned integer (big-endian).

Unlike the `nevent`, the author and the kind are mandatory here, since they are part of the address itself.

Let's take an example. Alice publishes an article on Nostr, an event of kind `30023` (NIP-23) whose `d` tag is `guide-multisig`. She shares her `naddr`. Bob opens it: his client decodes it, connects to the indicated relay, and requests the event of kind `30023` whose author is Alice's key and whose `d` tag is `guide-multisig`. The relay sends back the version it holds. A week later, Alice fixes an error: her client publishes a new event with the same `d` tag, which replaces the old one on relays. The link already shared remains valid and now displays the corrected article. NIP-21 gives as an example a 123-character `naddr` (69 bytes once decoded) that designates a kind `30023` article in the same way: its `d` tag is `18ff5416`, and it indicates the relay `wss://fiatjaf.com`.

Inside events, the same coordinate is written in an `a` tag, in the form `<kind>:<public key in hexadecimal>:<d tag value>`, for example `30023:<Alice's key>:guide-multisig`. The `naddr` is its human-facing form: NIP-23 provides for linking to an article with both an `naddr` and an `a` tag, and NIP-21 suggests placing a `nostr:naddr1…` in a `<link rel="alternate">` tag of the web page that publishes the same article in HTML.

This stability has a downside. Whoever shares an `naddr` does not freeze what is being shared: the author can rewrite the article, and the reader will see the version in effect when the link is opened, not the one the sender had read. To designate a specific version, an `nevent` is needed, provided a relay still holds it.

The `naddr` arrived in NIP-19 on February 3, 2023, along with NIP-23 and its long-form articles, under the name `nref`, to designate what was then called a “parameterized replaceable event” (NIP-33). On February 5, 2023, it became `nitem`, then the kind was added the next day, and on February 13, 2023 it took the name `naddr`, at the same time as the reference tag changed from `i` to `a`.

*Not to be confused with the NEVENT, which designates a specific version of an event by its identifier.*
