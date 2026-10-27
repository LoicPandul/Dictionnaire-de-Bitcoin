Identifier in the format of an email address (`name@domain`) that a Nostr user declares in their profile, and that a client checks by asking the domain which public key matches that name. Defined by NIP-05, it makes an account easier to recognize and find, but it identifies an account without verifying who is behind it.

The check relies on a file published by the domain. Let's take an example. Bob adds the field `"nip05": "bob@example.com"` to his profile, the kind `0` event that contains his name and description. When Alice's client displays this profile, it splits the identifier into 2 parts, `bob` and `example.com`, then sends an HTTPS request to `https://example.com/.well-known/nostr.json?name=bob`. The server replies with a JSON document that maps names to public keys:

```json
{
  "names": {
    "bob": "b0635d6a9851d3aed0cd6c495b282167acf761729078d975fc341b22650b07b9"
  }
}
```

If the key returned for `bob` is the one that signed the profile, Alice's client considers the identifier valid and can display it next to Bob's name. Otherwise, it does not display it. NIP-05 imposes a few formatting rules: the part before the `@` contains only lowercase letters, digits, and the characters `-`, `_`, and `.`; the key is written in lowercase hexadecimal, never as an `npub`; the server must not return any HTTP redirect, and the client must ignore them. The name is passed as a query parameter rather than in the path, which lets a domain serve a plain static file that lists several names. The identifier `_@example.com` is the root identifier, which clients can display as the bare domain `example.com`.

The same mechanism works in reverse, to find someone. Alice types `bob@example.com` into the search bar of her client. The client queries the domain's file, obtains Bob's key, fetches his profile, and checks that it does carry the same identifier. The domain's response may also contain, as a recommended option, a `relays` attribute that lists the relays where Bob's events can be found, which helps the client load his posts.

A valid NIP-05 identifier only proves that the domain associates this name with this key. It says nothing about the person: anyone who controls a domain can register any name there. NIP-05 has stated this since August 29, 2024: it exists to identify an account, to ease contact exchange and search, and not to verify its holder. The only exception concerns the domain itself: whoever owns a well-known domain (a company) or is attached to it (a project) can use the identifier as an attestation of that link with the organization that runs it.

The public key remains the true identity. NIP-05 asks clients to follow a key, never a NIP-05 address. If Alice follows Bob after finding his key through `bob@example.com`, her client keeps that key. If the domain later starts returning a different key for `bob`, the client does not replace the followed key: it only stops displaying the identifier, which has become invalid. With clients that respect this rule, the domain owner can therefore remove the identifier from an account, but cannot redirect its followers to another key.

The first version of NIP-05, published by fiatjaf on June 18, 2021, associated a profile with a domain name through a `TXT` DNS record placed under `_nostrkey.<domain>`. On December 30, 2021, fiatjaf replaced it with the current scheme: an email-style identifier and a JSON file at `/.well-known/nostr.json`. NIP-05 reached final status on November 22, 2022.

*It is also referred to by the name of its specification alone, "NIP-05". Not to be confused with an email address: the identifier only borrows its format, and the client simply makes an HTTPS request to the domain.*
