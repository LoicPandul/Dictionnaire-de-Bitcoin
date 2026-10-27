Identifiant partageable défini par NIP-19 qui encode en Bech32 l'identifiant d'un événement Nostr accompagné d'indices facultatifs : un ou plusieurs relais où le trouver, la clé publique de son auteur et son kind. Il complète l'identifiant `note`, qui ne contient que les 32 octets de l'identifiant de l'événement, pour qu'un client qui reçoit le lien sache aussi où aller chercher l'événement.

Ce besoin vient de l'architecture de Nostr : aucun serveur central ne détient tous les événements, chacun ne se trouve que sur les relais qui l'ont reçu. Prenons un exemple. Alice envoie à Bob l'identifiant `note` d'une publication de Charlie. Le client de Bob demande cet événement aux relais auxquels il est connecté, mais si aucun d'eux ne l'a reçu, il ne trouve rien. Avec un `nevent`, Alice lui transmet le même identifiant accompagné de l'adresse d'un relais de Charlie : le client de Bob s'y connecte, demande l'événement par son identifiant et l'obtient.

Pour transporter ces informations, NIP-19 utilise une structure TLV (*type-length-value*) : une suite d'entrées dont chacune commence par un octet de type, puis un octet de longueur, suivis de la valeur sur le nombre d'octets annoncé. Un `nevent` peut contenir 4 types d'entrées :

* type `0`, obligatoire : les 32 octets de l'identifiant de l'événement ;
* type `1`, facultatif et répétable : l'URL d'un relais où l'événement a des chances de se trouver, en ASCII ;
* type `2`, facultatif : les 32 octets de la clé publique de l'auteur ;
* type `3`, facultatif : le kind de l'événement, écrit en entier non signé de 32 bits (*big-endian*).

L'application concatène ces entrées, puis encode le tout en Bech32 avec le préfixe `nevent`. Un client qui rencontre un type qu'il ne connaît pas devrait l'ignorer au lieu de rejeter la chaîne, ce qui laisse la place à de nouveaux types sans casser les anciens logiciels.

NIP-21 donne en exemple le `nevent` suivant, qui commence par `nevent1qqstna2yrezu5wghjvswqqculvvwxsrcvu7uc0f78gan4xqhvz49d9sp` et compte 165 caractères. Une fois décodé, il livre 95 octets : l'identifiant `b9f5441e45ca39179320e0031cfb18e34078673dcc3d3e3a3b3a981760aa5696` et 2 relais, `wss://nostr-relay.untethr.me` et `wss://nostr-pub.wellorder.net`, sans auteur ni kind. Le relais indiqué n'a pas besoin d'être digne de confiance pour l'authenticité de l'événement : comme l'identifiant est le haché `SHA256` de l'événement et que l'événement porte la signature de son auteur, le client de Bob vérifie lui-même qu'il a bien reçu le bon événement, intact.

La clé publique de l'auteur sert de solution de repli. Si aucun relais indiqué ne répond, un client qui suit le modèle outbox peut chercher l'événement sur les relais où l'auteur déclare publier ; NIP-10 décrit le même usage pour la clé de l'auteur placée dans un tag `e`. Dans un texte, un `nevent` se place après le préfixe `nostr:` de NIP-21 (`nostr:nevent1…`) : c'est ainsi qu'une note en cite une autre (NIP-27), et NIP-18 demande alors d'ajouter un tag `q` qui reprend la référence.

Ces indices ont un coût en longueur. Un identifiant `note` fait 63 caractères ; un `nevent` avec 2 relais en fait 165, bien au-delà des 90 caractères que BIP-0173 fixe pour une chaîne Bech32 dans Bitcoin. Un décodeur Nostr ne peut donc pas appliquer cette limite, et NIP-19 recommande depuis mars 2026 de ne pas dépasser 5 000 caractères. Les relais inscrits dans un `nevent` sont aussi ceux que l'application connaissait au moment du partage : si l'un d'eux ferme ou efface l'événement, l'indice ne sert plus.

Le `nevent` figure dans NIP-19 dès son ajout au dépôt des NIP, le 16 décembre 2022, à partir d'une proposition de fiatjaf ouverte le 31 octobre 2022. Il ne contient alors que l'identifiant et des relais. La clé publique de l'auteur s'y ajoute en option le 15 mars 2023, puis le kind le 9 avril 2023.

*À ne pas confondre avec l'identifiant `note`, qui ne contient que l'identifiant de l'événement, ni avec le NADDR, qui désigne un événement adressable par sa coordonnée plutôt que par l'identifiant d'une version précise.*
