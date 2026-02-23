bLIP qui définit LSPS1, une API standardisée permettant aux portefeuilles Lightning d'acheter des canaux de paiement auprès de fournisseurs de services Lightning (LSP). Le processus se déroule en trois étapes :
- le client interroge les options disponibles du LSP via `lsps1.get_info`,
- il crée une commande avec les paramètres souhaités (capacité, durée, répartition des soldes) via `lsps1.create_order`,
- puis il règle via une facture BOLT-11, une offre BOLT-12 ou un paiement on-chain.

Le LSP ouvre ensuite le canal demandé. La spécification supporte les canaux publics et privés, les canaux à zéro confirmation, et prévoit un remboursement automatique en cas d'échec de l'ouverture. LSPS1 repose sur la couche de transport LSPS0 du bLIP-0050.