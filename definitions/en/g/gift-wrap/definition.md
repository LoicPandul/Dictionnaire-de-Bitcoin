NIP-59 technique that wraps a Nostr event in several layers of encryption, so that a relay learns neither its author nor its content. The visible event is signed by a throwaway key. NIP-59 does not define any messaging: it provides the wrapping, which NIP-17 uses for private messages (see NOSTR PRIVATE DIRECT MESSAGE).

The process relies on 3 nested objects, each with its own role.

* The rumor is an ordinary event with its signature removed. It carries the content. Because it is unsigned, nobody can prove it came from its author if it leaks: relays and clients reject it, which gives some plausible deniability.
* The seal is an event of kind `13` whose `content` field holds the rumor, encrypted with NIP-44 (see NIP-44 ENCRYPTION) for the recipient. The author's real key signs it, and it carries no recipient tag. It reveals who signs, but not what is said or to whom.
* The gift wrap is an event of kind `1059` whose `content` holds the encrypted seal, this time encrypted with a random key pair created for this one message. This throwaway key signs it. Its tags contain what is needed to route it: the recipient's `p` tag, or a proof of work (NIP-13).

Let's take an example. Alice wants to send Bob an event of kind `1` that says “Are you coming to the party tonight?”. Her client creates the event without signing it, encrypts it for Bob in a seal that she signs, then encrypts that seal with a random key in a `1059` wrapper carrying a `p` tag pointing to Bob. It sends only this gift wrap to Bob's relays and deletes the other events. Bob decrypts the gift wrap with his private key and the gift wrap's public key, which yields the seal; he decrypts the seal with his private key and the seal's public key, which yields the rumor. A relay, for its part, sees only an unknown key sending opaque text to Bob.

Dates require particular care. The canonical date is the rumor's; the others should be randomized and set in the past, because some relays do not serve events dated in the future. When a rumor is addressed to several people, one gift wrap is made per recipient, and the author can also address one to themselves to keep an encrypted copy.

NIP-59 provides an ephemeral variant, of kind `21059`, which has the same structure but which relays must not store. It suits real-time uses, such as a chat room or a game, whereas kind `1059` suits asynchronous exchanges such as NIP-17 messages.

The wrapping has a price. Because every gift wrap carries a fresh key, relays can no longer filter spam by key reputation, and mass-sending gift wraps becomes a way to saturate a relay. NIP-59 suggests that relays require NIP-42 authentication and that clients add a proof of work (NIP-13); relays may also refuse to store these events, judging them of little public use. The recipient's `p` tag remains readable: NIP-59 therefore asks relays to serve `1059` events only to the recipient, after authentication. Relays should delete a `1059` event whose `p` tag points to the key that signs a NIP-09 deletion or a NIP-62 request to vanish (the latter, still a draft, only targets the relays it names).

Jon Staab proposed NIP-59 on August 11, 2023. In its first form, the recipient's `p` tag was mandatory and only that key remained public; on January 9, 2024, the tag became recommended and the NIP stated that it does not define any messaging. The NIP entered the NIPs repository on January 29, 2024.

*Gift wrap should not be confused with the seal, the intermediate layer that the author signs.*
