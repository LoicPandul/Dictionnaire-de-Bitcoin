Integer from 0 to 65535, placed in the `kind` field of a Nostr event, that indicates the nature of that event. A kind tells clients how to read the rest of the event: kind `0` carries the user's profile, kind `1` a short note, kind `3` their follow list, kind `9735` a zap receipt. Depending on the range it falls in, it also tells relays how to store the event.

The meaning of the other fields depends on the kind. For a kind `0`, the `content` field contains a JSON object with the user's name, description, and image; for a kind `1`, it contains the text of the note; for a kind `3`, it is unused and the list lives in the tags. The same tag can thus change meaning from one kind to another: NIP-01 cites the `r` tag, which does not mean the same thing in a note and in a relay list (kind `10002`). Each NIP can define new kinds that have no meaning elsewhere yet: NIP-01 defines kind `0`, NIP-10 now describes kind `1`, which was present from the first NIP-01, NIP-02 describes kind `3`, and NIP-57 kinds `9734` (zap request) and `9735` (zap receipt).

NIP-01 divides kinds into 4 categories according to their range, which indicate how a relay keeps them:

* regular (`1`, `2`, `4` to `44`, `1000` to `9999`): relays are expected to store all of them;
* replaceable (`0`, `3`, `10000` to `19999`): for the same author and the same kind, the relay must keep the most recent version and may discard the earlier ones (see REPLACEABLE EVENT);
* ephemeral (`20000` to `29999`): relays forward them to current subscribers and are not expected to store them;
* addressable (`30000` to `39999`): the relay must keep the latest version for each combination of author, kind, and `d` tag value (see ADDRESSABLE EVENT).

The ranges `45` to `999` and `40000` to `65535` fall under none of these conventions. NIP-01 also states that these are conventions, and that relay implementations may deviate from them.

Let's take an example. Alice updates the description of her profile: her client publishes a new kind `0` event. Since this kind is replaceable, relays keep Alice's new profile and may discard the old one. The same day, she publishes 2 kind `1` notes, which relays are expected to keep, both of them. When her client authenticates to a relay under NIP-42, it signs a kind `22242` event, from the ephemeral range; NIP-42 specifies that the relay verifies it but must not forward it to any client. Finally, the kind is used in queries: a client that wants only notes and their reposts (kind `6`, NIP-18) asks the relay with the filter `{"kinds": [1, 6]}`.

No authority formally assigns kinds. The NIPs repository keeps a de facto index, but nobody is obliged to follow it. The README of the NIPs repository holds a table of known kinds, stating that it is not exhaustive, and points to a machine-readable registry (`registry-of-kinds`) or to any alternative registry in the same format. Nothing therefore prevents 2 applications from using the same number for different purposes; the table and the NIPs exist to avoid that.

In NIP-01 as merged in May 2022 into the NIPs repository (the text had existed since November 2020 in the main Nostr repository), there were only 3 base kinds: `0` (`set_metadata`), `1` (`text_note`), and `2` (`recommend_server`, which recommended a relay), the latter having since left NIP-01 (in August 2023) and then the repository table, where it appeared as deprecated. The ranges from 10000 on come from NIP-16, proposed by Semisol in May 2022 for replaceable and ephemeral events, and from NIP-33, added in January 2023 for parameterized replaceable events (now addressable). The 2 documents were merged into NIP-01 on August 13, 2023.

*An event of kind `1` is also written `kind:1`.*
