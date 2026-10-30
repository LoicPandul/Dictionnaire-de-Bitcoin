# Fiches Nostr retirées (décision de Loïc du 30/10/2026)

Nostr n'est pas Bitcoin : les 44 fiches des catégories « Nostr » et « Application Nostr », plus l'outil NDK, sont retirées en français et en anglais avec `git rm`, avec leurs schémas, leurs renvois entrants, leurs catégories, leurs pictogrammes et leurs lignes d'index. La chronologie et les spécifications n'en citaient aucune.

Les mentions de Nostr dans les fiches de produits Bitcoin (Alby, Alby Hub, BitBanana, Coinos, Joinstr, LNbits, Umbrel) restent : elles décrivent ces produits.

Pour repêcher une fiche : `git checkout 4905dc0f -- definitions/fr/<lettre>/<slug> definitions/en/<lettre>/<slug-en>`, puis remettre la catégorie dans `templates/categories.yaml` et `templates/parts.yaml`.

| Slug FR | Titre | Catégorie | Slug EN |
|---|---|---|---|
| amber | AMBER | APPLICATION NOSTR |  |
| amethyst | AMETHYST | APPLICATION NOSTR |  |
| blossom | BLOSSOM | NOSTR | blossom |
| bunker-nostr | BUNKER NOSTR | NOSTR | nostr-bunker |
| chiffrement-nip-44 | CHIFFREMENT NIP-44 | NOSTR | nip-44-encryption |
| client-nostr | CLIENT NOSTR | NOSTR | nostr-client |
| contenu-long-nostr | CONTENU LONG NOSTR | NOSTR | nostr-long-form-content |
| coracle | CORACLE | APPLICATION NOSTR |  |
| damus | DAMUS | APPLICATION NOSTR |  |
| dvm-data-vending-machine | DVM - DATA VENDING MACHINE | NOSTR | dvm-data-vending-machine |
| evenement-adressable | ÉVÉNEMENT ADRESSABLE | NOSTR | addressable-event |
| evenement-nostr | ÉVÉNEMENT NOSTR | NOSTR | nostr-event |
| evenement-remplacable | ÉVÉNEMENT REMPLAÇABLE | NOSTR | replaceable-event |
| gift-wrap | GIFT WRAP | NOSTR | gift-wrap |
| gossip-client-nostr | CLIENT GOSSIP | APPLICATION NOSTR |  |
| identifiant-nip-05 | IDENTIFIANT NIP-05 | NOSTR | nip-05-identifier |
| kind-nostr | KIND NOSTR | NOSTR | nostr-kind |
| message-prive-nostr | MESSAGE PRIVÉ NOSTR | NOSTR | nostr-private-direct-message |
| modele-outbox | MODÈLE OUTBOX | NOSTR | outbox-model |
| mostro | MOSTRO | NOSTR | mostro |
| naddr | NADDR | NOSTR | naddr |
| ncryptsec | NCRYPTSEC | NOSTR | ncryptsec |
| ndk-nostr-development-kit | NDK - NOSTR DEVELOPMENT KIT | OUTIL DE DÉVELOPPEMENT |  |
| nevent | NEVENT | NOSTR | nevent |
| nip | NIP | NOSTR | nip |
| nos2x | NOS2X | APPLICATION NOSTR |  |
| nostr | NOSTR | NOSTR | nostr |
| nostrudel | NOSTRUDEL | APPLICATION NOSTR |  |
| note-nostr | NOTE NOSTR | NOSTR | nostr-text-note |
| nprofile | NPROFILE | NOSTR | nprofile |
| npub | NPUB | NOSTR | npub |
| nsec | NSEC | NOSTR | nsec |
| nsec-app | NSEC.APP | APPLICATION NOSTR |  |
| nutzap | NUTZAP | NOSTR | nutzap |
| nwc-nostr-wallet-connect | NWC - NOSTR WALLET CONNECT | NOSTR | nwc-nostr-wallet-connect |
| preuve-de-travail-nostr | PREUVE DE TRAVAIL NOSTR | NOSTR | nostr-proof-of-work |
| primal | PRIMAL | APPLICATION NOSTR |  |
| relais-nostr | RELAIS NOSTR | NOSTR | nostr-relay |
| signataire-nostr | SIGNATAIRE NOSTR | NOSTR | nostr-signer |
| signature-d-evenement-nostr | SIGNATURE D'ÉVÉNEMENT NOSTR | NOSTR | nostr-event-signature |
| tag-nostr | TAG NOSTR | NOSTR | nostr-tag |
| web-of-trust | WEB OF TRUST | NOSTR | web-of-trust |
| white-noise | WHITE NOISE | APPLICATION NOSTR |  |
| zap | ZAP | NOSTR | zap |
