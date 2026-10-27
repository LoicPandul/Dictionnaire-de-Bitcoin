Format défini par NIP-49 qui chiffre une clé privée Nostr avec un mot de passe et encode le résultat en Bech32 avec le préfixe `ncryptsec`. Il sert à sauvegarder la clé ou à la transférer d'un logiciel à un autre sans l'exposer en clair, comme le fait une `nsec`, que n'importe qui peut utiliser dès qu'il la lit.

Le chiffrement se déroule en 2 temps. Il faut d'abord tirer du mot de passe une clé de chiffrement. Un mot de passe fait une mauvaise clé : ses bits ne sont pas répartis au hasard, et il se devine bien plus vite qu'une vraie clé. NIP-49 le passe donc dans scrypt, une fonction de dérivation volontairement lente et gourmande en mémoire, avec un sel de 16 octets aléatoires et un paramètre de coût choisi par l'utilisateur ou le logiciel, `LOG_N`, qui donne le paramètre de coût N de scrypt sous forme de puissance de 2 (une valeur de 18 correspond à N = 262 144). Le résultat est une clé symétrique de 32 octets, que le logiciel doit effacer de sa mémoire après usage. Cette clé chiffre ensuite les 32 octets de la clé privée avec XChaCha20-Poly1305, un algorithme de chiffrement authentifié, et un nonce de 24 octets aléatoires.

Prenons un exemple. Alice veut passer d'un client Nostr à un autre. Son premier client lui demande un mot de passe, le normalise au format Unicode NFKC, pour qu'il donne les mêmes octets quand elle le retapera sur un autre ordinateur ou dans un autre client, puis le dérive avec `LOG_N` égal à 16. Il chiffre sa clé privée et assemble 91 octets dans cet ordre :

* 1 octet de version, `0x02` ;
* 1 octet pour `LOG_N` ;
* les 16 octets du sel ;
* les 24 octets du nonce ;
* 1 octet qui indique si la clé a déjà été manipulée sans protection : `0x00` si elle a déjà été stockée ou copiée en clair, `0x01` si ce n'est pas le cas à la connaissance du logiciel, `0x02` s'il ne suit pas cette information ;
* les 48 octets chiffrés, soit la clé privée et une étiquette d'authentification de 16 octets.

Encodés en Bech32, ces 91 octets donnent une chaîne de 162 caractères qui commence par `ncryptsec1`. Alice la colle dans son nouveau client et retape son mot de passe. Le client lit dans la chaîne le sel et `LOG_N`, recalcule la clé symétrique, puis déchiffre. L'étiquette d'authentification garantit le résultat : avec un mauvais mot de passe ou une chaîne altérée, l'étiquette recalculée ne correspond plus et le déchiffrement échoue au lieu de produire une fausse clé. L'octet de sécurité est lui aussi couvert par cette étiquette, car il sert de donnée associée au chiffrement. NIP-49 donne un vecteur de test : la chaîne `ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p`, déchiffrée avec le mot de passe `nostr`, rend la clé privée `3501454135014541350145413501453fefb02227e449e57cf4d3a3ce05378683`. Comme le sel et le nonce sont tirés au hasard, chiffrer 2 fois la même clé avec le même mot de passe donne 2 chaînes différentes.

Le paramètre `LOG_N` règle la résistance à la force brute. Selon le tableau de NIP-49, une valeur de 16 demande 64 Mio de mémoire et environ 100 millisecondes sur un ordinateur rapide, une valeur de 20 demande 1 Gio et environ 2 secondes, et une valeur de 22 monte à 4 Gio. Chaque cran double le travail, pour l'utilisateur légitime comme pour un attaquant qui essaie des mots de passe un par un.

La protection d'une `ncryptsec` ne vaut que celle de son mot de passe. Quiconque obtient la chaîne peut tester des mots de passe hors ligne, sans limite de tentatives : scrypt ralentit chaque essai, mais un mot de passe court ou courant finit par tomber. Pour cette raison, NIP-49 déconseille de publier ces clés chiffrées sur Nostr, car casser une clé devient plus facile quand un attaquant peut en amasser beaucoup.

Mike Dilger, auteur du client Gossip, ouvre le 30 décembre 2022 la proposition qui devient NIP-49 ; elle décrit l'export et l'import de clé de Gossip et rejoint le dépôt des NIP le 29 janvier 2024. Le 16 février 2024, une modification incompatible avec la version précédente impose la normalisation NFKC du mot de passe.

*À ne pas confondre avec la `nsec`, qui encode la même clé privée en clair : une `nsec` suffit pour contrôler le compte, alors qu'une `ncryptsec` exige aussi le mot de passe.*
