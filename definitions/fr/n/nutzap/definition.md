Paiement Nostr défini par NIP-61 : un jeton Cashu verrouillé pour son destinataire, publié dans un événement Nostr qui sert lui-même de reçu. Il joue le rôle du ZAP, mais le paiement se fait en monnaie électronique Cashu et non en Lightning.

Le jeton est un jeton de CASHU, émis par un *mint*. Le verrou est celui de P2PK : en l'absence de condition supplémentaire (clés additionnelles, date d'expiration), seule la clé privée associée à une clé publique donnée peut dépenser la preuve.

Pour recevoir des nutzaps, le destinataire publie un événement de kind `10019`. Il y indique par des tags `relay` les relais où il lira les paiements, par des tags `mint` les mints dont il accepte les jetons, et par un tag `pubkey` la clé P2PK sur laquelle verrouiller. Cette clé ne doit pas être sa clé Nostr principale : elle correspond à une clé privée gardée, chiffrée, dans son portefeuille Cashu de NIP-60, un portefeuille dont l'état est stocké sur des relais pour le suivre d'une application à l'autre.

Prenons un exemple. Alice aime une note de Bob et veut lui envoyer 1 sat.

* Son client lit le kind `10019` de Bob et y trouve ses mints.
* Alice crée un jeton de 1 sat chez l'un de ces mints, ou échange des jetons qu'elle détient déjà chez lui, verrouillé sur la clé P2PK de Bob. Le client ajoute le préfixe `02` à cette clé, pour la compatibilité entre Nostr et Cashu.
* Elle publie un événement de kind `9321` sur les relais de Bob. Ses tags `proof` contiennent les preuves, chacune accompagnée de sa preuve DLEQ, `u` donne l'URL du mint, `unit` l'unité (`sat` par défaut), `e` la note concernée et `p` la clé Nostr de Bob. Le `content` peut porter un commentaire.
* Le client de Bob lit les kinds `9321` qui le citent et échange les jetons dans un portefeuille NIP-60, un portefeuille Lightning ou un autre. Il publie en retour, de préférence, un événement de kind `7376`, qui note que le nutzap est réclamé.

Contrairement au zap, le destinataire n'émet aucune facture Lightning et aucun serveur LNURL n'intervient de son côté : le zap de NIP-57 passe par une requête LNURL-pay et par un reçu que ce serveur publie. Le nutzap tient entièrement dans l'événement `9321`, dont les preuves sont à la fois le paiement et le reçu.

Tout observateur peut donc contrôler l'authenticité d'un nutzap sans interroger personne, mais seul le mint dit si le jeton est déjà dépensé : il contrôle que le destinataire a bien publié un kind `10019` qui liste ce mint, que le jeton est verrouillé sur la clé annoncée, que le tag `u` correspond à l'un de ses mints et que la preuve DLEQ est valide. Ces contrôles se font hors ligne, à condition de connaître les clés du mint et le kind `10019`.

Le système a ses pièges. L'expéditeur doit se limiter aux mints que le destinataire a listés : un jeton émis ailleurs peut ne jamais être vu ou dépensé, et NIP-61 prévient qu'il risque de brûler son argent. Le destinataire devrait lui aussi choisir des mints qui gèrent P2PK (NUT-11), faute de quoi il recevrait des nutzaps que n'importe qui peut dépenser, et les preuves DLEQ (NUT-12), qui permettent la vérification hors ligne.

NIP-61 est ajouté au dépôt des NIP le 25 octobre 2024, avec NIP-60, dans un commit de Pablo Fernandez, et porte aujourd'hui le statut `draft`.

*NIP-61 emploie aussi l'expression « Cashu zap ».*
