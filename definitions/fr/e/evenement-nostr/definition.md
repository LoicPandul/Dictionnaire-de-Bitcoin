Unité fondamentale de données dans le protocole Nostr. Toute information transmise sur le réseau Nostr (publication de texte, mise à jour de profil, réaction, message chiffré, reçu de zap...) prend la forme d'un événement. Un événement est un objet JSON contenant sept champs :
* `id` : un identifiant unique obtenu par hachage SHA-256 du contenu sérialisé,
* `pubkey` : la clé publique de l'auteur,
* `created_at` : l'horodatage Unix,
* `kind` : le type d'événement identifié par un entier,
* `tags` : les métadonnées structurées permettant de mentionner des utilisateurs, référencer d'autres événements ou ajouter des hashtags,
* `content` : le contenu textuel,
* `sig` : la signature Schnorr sur secp256k1.

Le champ `kind` détermine la nature de l'événement : kind 0 pour les métadonnées de profil, kind 1 pour les notes textuelles, kind 4 pour les messages directs chiffrés, kind 7 pour les réactions ou kind 9735 pour les reçus de zap. Les relais vérifient la signature avant d'accepter un événement, ce qui garantit l'authenticité et l'intégrité des données.