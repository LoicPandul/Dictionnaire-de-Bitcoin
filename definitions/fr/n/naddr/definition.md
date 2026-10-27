Identifiant partageable défini par NIP-19 qui désigne un événement adressable par sa coordonnée, c'est-à-dire son kind, la clé publique de son auteur et la valeur de son tag `d`, avec des relais facultatifs où le trouver. Comme il ne contient l'identifiant d'aucune version précise, le lien mène à la dernière version que le relais interrogé a reçue de l'article ou de la liste qu'il désigne.

Ce format répond à une particularité des événements adressables (kinds `30000` à `39999`). Pour chaque combinaison d'un kind, d'une clé publique et d'une valeur de tag `d`, NIP-01 demande aux relais de conserver la dernière version, et les autorise à jeter les précédentes. Chaque modification produit pourtant un nouvel événement, avec un nouvel identifiant. Un NEVENT, qui pointe vers un identifiant, mènerait donc vers une version que les relais ont pu effacer. Le `naddr` pointe vers la coordonnée, qui ne change pas d'une version à l'autre.

Le `naddr` reprend la structure TLV du NEVENT, avec des types dont le sens change :

* type `0` : la valeur du tag `d`, en texte, ou une chaîne vide pour désigner un événement remplaçable ordinaire, dont l'adresse ne comporte que le kind et l'auteur ;
* type `1`, facultatif et répétable : l'URL d'un relais où trouver l'événement ;
* type `2` : les 32 octets de la clé publique de l'auteur ;
* type `3` : le kind, en entier non signé de 32 bits (*big-endian*).

Contrairement au `nevent`, l'auteur et le kind sont ici obligatoires, puisqu'ils font partie de l'adresse elle-même.

Prenons un exemple. Alice publie sur Nostr un article, un événement de kind `30023` (NIP-23) dont le tag `d` vaut `guide-multisig`. Elle partage son `naddr`. Bob l'ouvre : son client le décode, se connecte au relais indiqué et demande l'événement de kind `30023`, dont l'auteur est la clé d'Alice et dont le tag `d` vaut `guide-multisig`. Le relais lui renvoie la version qu'il garde. Une semaine plus tard, Alice corrige une erreur : son client publie un nouvel événement avec le même tag `d`, qui remplace l'ancien sur les relais. Le lien déjà diffusé reste valable et affiche désormais l'article corrigé. NIP-21 donne en exemple un `naddr` de 123 caractères (69 octets une fois décodé) qui désigne de la même façon un article de kind `30023` : son tag `d` vaut `18ff5416`, et il indique le relais `wss://fiatjaf.com`.

À l'intérieur des événements, la même coordonnée s'écrit dans un tag `a`, sous la forme `<kind>:<clé publique en hexadécimal>:<valeur du tag d>`, par exemple `30023:<clé d'Alice>:guide-multisig`. Le `naddr` en est la forme destinée aux humains : NIP-23 prévoit de lier un article avec un `naddr` et un tag `a`, et NIP-21 propose de placer un `nostr:naddr1…` dans une balise `<link rel="alternate">` de la page web qui publie le même article en HTML.

Cette stabilité a sa contrepartie. Celui qui partage un `naddr` ne fige pas ce qu'il partage : l'auteur peut réécrire l'article, et le lecteur verra la version en vigueur au moment où il ouvre le lien, pas celle que l'expéditeur avait lue. Pour désigner une version précise, il faut un `nevent`, à condition qu'un relais la conserve encore.

Le `naddr` arrive dans NIP-19 le 3 février 2023, avec NIP-23 et ses articles longs, sous le nom `nref`, pour désigner ce qu'on appelait alors un événement « remplaçable paramétré » (*parameterized replaceable event*, NIP-33). Le 5 février 2023, il devient `nitem`, puis le kind y est ajouté le lendemain, et le 13 février 2023 il prend le nom `naddr`, en même temps que le tag de référence passe de `i` à `a`.

*À ne pas confondre avec le NEVENT, qui désigne une version précise d'un événement par son identifiant.*
