Shareable identifier defined by NIP-19 that encodes in Bech32 the ID of a Nostr event along with optional hints: one or more relays where it can be found, the public key of its author, and its kind. It complements the `note` identifier, which contains only the 32 bytes of the event ID, so that a client receiving the link also knows where to look for the event.

This need comes from the architecture of Nostr: no central server holds all the events, and each one is found only on the relays that received it. Let's take an example. Alice sends Bob the `note` identifier of a post by Charlie. Bob's client asks the relays it is connected to for this event, but if none of them received it, it finds nothing. With an `nevent`, Alice passes him the same ID along with the address of one of Charlie's relays: Bob's client connects to it, requests the event by its ID, and gets it.

To carry this information, NIP-19 uses a TLV (type-length-value) structure: a series of entries, each of which starts with a type byte, then a length byte, followed by the value over the announced number of bytes. An `nevent` can contain 4 types of entries:

* type `0`, required: the 32 bytes of the event ID;
* type `1`, optional and repeatable: the URL of a relay where the event is likely to be found, in ASCII;
* type `2`, optional: the 32 bytes of the author's public key;
* type `3`, optional: the kind of the event, written as a 32-bit unsigned integer (big-endian).

The application concatenates these entries, then encodes the whole in Bech32 with the `nevent` prefix. A client that encounters a type it does not know should ignore it instead of rejecting the string, which leaves room for new types without breaking older software.

NIP-21 gives the following `nevent` as an example, which starts with `nevent1qqstna2yrezu5wghjvswqqculvvwxsrcvu7uc0f78gan4xqhvz49d9sp` and is 165 characters long. Once decoded, it yields 95 bytes: the ID `b9f5441e45ca39179320e0031cfb18e34078673dcc3d3e3a3b3a981760aa5696` and 2 relays, `wss://nostr-relay.untethr.me` and `wss://nostr-pub.wellorder.net`, with no author or kind. The indicated relay does not need to be trusted for the authenticity of the event: since the ID is the `SHA256` hash of the event and the event carries its author's signature, Bob's client verifies by itself that it received the right event, intact.

The author's public key serves as a fallback. If none of the indicated relays responds, a client that follows the outbox model can look for the event on the relays where the author declares they publish; NIP-10 describes the same use for the author's key placed in an `e` tag. In a text, an `nevent` is placed after the `nostr:` prefix of NIP-21 (`nostr:nevent1…`): this is how one note quotes another (NIP-27), and NIP-18 then asks to add a `q` tag that repeats the reference.

These hints come at a cost in length. A `note` identifier is 63 characters long; an `nevent` with 2 relays is 165, well beyond the 90 characters that BIP-0173 sets for a Bech32 string in Bitcoin. A Nostr decoder therefore cannot apply this limit, and since March 2026 NIP-19 recommends not exceeding 5,000 characters. The relays written into an `nevent` are also those the application knew at the time of sharing: if one of them shuts down or deletes the event, the hint is of no use.

The `nevent` has been part of NIP-19 since it was added to the NIP repository on December 16, 2022, from a proposal by fiatjaf opened on October 31, 2022. At that point it contained only the ID and relays. The author's public key was added as an option on March 15, 2023, then the kind on April 9, 2023.

*Not to be confused with the `note` identifier, which contains only the event ID, nor with the `naddr`, which designates an addressable event by its coordinate rather than by the ID of a specific version.*
