Requête de paiement Lightning générée par le destinataire, qui contient toutes les informations nécessaires pour réaliser la transaction.

Une invoice Lightning contient un préfixe `ln`, le hachage du secret utilisé dans le cadre des HTLCs, ainsi que d'autres métadonnées, dont certaines sont facultatives : le montant, un temps avant expiration (3 600 secondes par défaut), la clé publique du nœud destinataire, que le payeur peut aussi retrouver à partir de la signature, ou des options relatives au routage. Ces invoices sont définies par la norme BOLT-11.

![Anatomie d'une facture BOLT-11 : la partie lisible porte le préfixe ln et le montant facultatif ; après le séparateur 1, la partie données range l'horodatage, le hachage du secret, l'expiration et la clé publique du destinataire, facultatives, puis la signature.](./assets/image-1.png)
