Format defined by NIP-49 that encrypts a Nostr private key with a password and encodes the result in Bech32 with the `ncryptsec` prefix. It is used to back up the key or move it from one piece of software to another without exposing it in plaintext, as an `nsec` does, which anyone can use as soon as they read it.

The encryption takes place in 2 steps. First, an encryption key must be derived from the password. A password makes a poor key: its bits are not uniformly random, and it can be guessed much faster than a real key. NIP-49 therefore runs it through scrypt, a key derivation function that is deliberately slow and memory-hungry, with a salt of 16 random bytes and a cost parameter chosen by the user or the software, `LOG_N`, which gives scrypt's cost parameter N as a power of 2 (a value of 18 corresponds to N = 262,144). The result is a symmetric key of 32 bytes, which the software must wipe from memory after use. This key then encrypts the 32 bytes of the private key with XChaCha20-Poly1305, an authenticated encryption algorithm, and a nonce of 24 random bytes.

Let's take an example. Alice wants to move from one Nostr client to another. Her first client asks her for a password, normalizes it to Unicode NFKC so that it yields the same bytes when she retypes it on another computer or in another client, then derives the key with `LOG_N` equal to 16. It encrypts her private key and assembles 91 bytes in this order:

* 1 byte of version, `0x02`;
* 1 byte for `LOG_N`;
* the 16 bytes of the salt;
* the 24 bytes of the nonce;
* 1 byte that indicates whether the key has ever been handled insecurely: `0x00` if it has been stored or copied in plaintext, `0x01` if it has not, to the software's knowledge, `0x02` if the software does not track this information;
* the 48 encrypted bytes, that is the private key and an authentication tag of 16 bytes.

Encoded in Bech32, these 91 bytes give a string of 162 characters that starts with `ncryptsec1`. Alice pastes it into her new client and retypes her password. The client reads the salt and `LOG_N` from the string, recomputes the symmetric key, then decrypts. The authentication tag guarantees the result: with a wrong password or a tampered string, the recomputed tag no longer matches and decryption fails instead of producing a wrong key. The security byte is also covered by this tag, because it serves as associated data for the encryption. NIP-49 gives a test vector: the string `ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p`, decrypted with the password `nostr`, returns the private key `3501454135014541350145413501453fefb02227e449e57cf4d3a3ce05378683`. Since the salt and the nonce are drawn at random, encrypting the same key twice with the same password gives 2 different strings.

The `LOG_N` parameter sets the resistance to brute force. According to the table in NIP-49, a value of 16 requires 64 MiB of memory and about 100 milliseconds on a fast computer, a value of 20 requires 1 GiB and about 2 seconds, and a value of 22 climbs to 4 GiB. Each step doubles the work, for the legitimate user as well as for an attacker who tries passwords one by one.

The protection of an `ncryptsec` is only as good as its password. Anyone who obtains the string can test passwords offline, with no limit on attempts: scrypt slows down each try, but a short or common password eventually falls. For this reason, NIP-49 advises against publishing these encrypted keys on Nostr, because cracking a key becomes easier when an attacker can collect many of them.

Mike Dilger, author of the Gossip client, opened the proposal that became NIP-49 on December 30, 2022; it describes Gossip's key export and import, and it joined the NIP repository on January 29, 2024. On February 16, 2024, a change incompatible with the previous version made NFKC normalization of the password mandatory.

*Not to be confused with the `nsec`, which encodes the same private key in plaintext: an `nsec` is enough to control the account, whereas an `ncryptsec` also requires the password.*
