Développeur, connu sous le pseudonyme jb55, créateur de Damus, client Nostr pour iOS, et coauteur de NIP-57 avec Kieran, qui définit les zaps.

Le premier commit de Damus date du 2 avril 2022. William Casarin rédige NIP-25 (réactions) dans le dépôt des NIP le 30 juillet 2022 ; sa pull request est fusionnée le 1er août. En janvier 2023, il publie cln-nostr-zapper, un script pour Core Lightning qui écoute les paiements de factures et envoie un reçu de zap quand la facture contient une requête de zap. Le 13 février 2023, il ajoute au dépôt des NIP le fichier de NIP-57, qui portait alors les mentions d'auteur jb55 et kieran, retirées de tous les NIP en novembre 2023.

NIP-57 décrit comment un client Nostr demande une facture Lightning pour une note ou un profil, puis comment le nœud qui la reçoit publie un reçu signé : c'est le zap. Le texte note que Core Lightning, qu'il appelle CLN, enregistre automatiquement la description de la facture, et renvoie vers le script de Casarin comme implémentation de référence d'un serveur LNURL compatible avec les zaps (« zapper » dans la version initiale).

Damus intègre les zaps dès le début de 2023 : le premier commit sur le sujet date du 16 janvier. En juillet 2023, OpenSats compte Damus, attribué à jb55, parmi les projets Nostr qu'il soutient.
