Protocole de communication entre un nœud Bitcoin et un logiciel de minage, défini dans le BIP-0022 et le BIP-0023. Il a été introduit en 2012 pour remplacer le protocole `getwork`, dont les limitations devenaient problématiques avec la croissance de la puissance de calcul du réseau.

Contrairement à `getwork`, qui fournissait au mineur un en-tête de bloc prêt à hacher, `getblocktemplate` transmet un modèle complet de bloc (*block template*). Le mineur reçoit la liste des transactions à inclure, les paramètres du bloc et les règles de consensus à respecter. Cette approche lui permet de construire lui-même le bloc candidat et de choisir quelles transactions y intégrer.

Ce changement a réduit le pouvoir des opérateurs de pools de minage sur la sélection des transactions, ce qui a décentralisé une partie du processus de construction des blocs. `getblocktemplate` a ensuite été largement remplacé par le protocole Stratum, puis par Stratum V2.
