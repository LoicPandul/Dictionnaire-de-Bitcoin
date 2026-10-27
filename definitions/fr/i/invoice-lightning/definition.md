Requête de paiement Lightning générée par le destinataire, qui contient toutes les informations nécessaires pour réaliser la transaction.

Une invoice Lightning contient la destination du paiement sous la forme de la clé publique du nœud destinataire, mais également un préfixe `ln`, le montant, un temps avant expiration, le hachage du secret utilisé dans le cadre des HTLCs, ainsi que d'autres métadonnées, pour certaines optionnelles, comme des options relatives au routage. Ces invoices sont définies par la norme BOLT-11. Une fois payée, une invoice Lightning ne peut plus être réutilisée.

![Anatomie d'une facture BOLT-11 : la partie lisible porte le préfixe ln et le montant facultatif ; après le séparateur 1, la partie données range l'horodatage, le hachage du secret, l'expiration et la clé publique du destinataire, facultatives, puis la signature.](./assets/image-1.png)
