Identifiant unique de 32 octets attribué à chaque actif émis via le protocole Taproot Assets. L'*asset ID* est produit en hachant avec SHA-256 trois éléments concaténés : l'outpoint de la transaction de genèse (celle qui crée l'actif), un tag choisi par l'émetteur (par exemple le hash d'un nom de marque), et des métadonnées associées à l'actif (liens, images, documents).

`asset_id = sha256(genesis_outpoint || asset_tag || asset_meta)`

Puisqu'il dépend de l'outpoint de genèse, l'*asset ID* est unique à l'échelle mondiale : deux émissions distinctes produiront toujours des identifiants différents. Il sert de clé pour retrouver un actif dans un *Universe*, vérifier sa provenance et distinguer les différents types d'actifs engagés dans un même *Sparse Merkle Sum Tree*.