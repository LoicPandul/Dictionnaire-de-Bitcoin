## STAMPS

Protocole qui permet d'intégrer des données d'image formatées directement sur la blockchain Bitcoin via des transactions multisignatures brutes (P2MS). Il encode le contenu binaire d'une image en base 64 et l'ajoute dans les clés d’un « bare multisig » 1/3. Une clé est réelle et sert à dépenser les fonds, tandis que les deux autres sont des fausses clés (on ne connait pas la clé privée associée) qui stockent les données. En utilisant encodant les données directement sous forme de clés publiques plutôt qu'en utilisant des sorties `OP_RETURN`, les images stockées avec le protocole Stamps sont particulièrement intensives en terme de charge de travail pour les neouds. Cette méthode crée notamment de multiples UTXOs, ce qui augmente la taille de l'UTXO set et pose des problèmes pour les nœuds complets.

► ***NOTE :** Pour plus d'informations, voir les définitions d'**[UTREEXO](/dictionnaire/U.md#utreexo)** et d'**[UTXO SET](/dictionnaire/U.md#utxo-set)**.*

