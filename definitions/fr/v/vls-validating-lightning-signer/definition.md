Sigle de « Validating Lightning Signer ». Bibliothèque open source en Rust qui sépare les clés privées d'un nœud Lightning du logiciel du nœud lui-même, en les déportant vers un dispositif de signature dédié. Avant chaque opération cryptographique, VLS applique un ensemble de plus de cinquante règles de validation pour vérifier que la transaction proposée est sûre.

Si le nœud est compromis ou tente une action malveillante, comme signer une *commitment transaction* révoquée ou fermer un canal vers une adresse non autorisée, VLS refuse la signature. Ce mécanisme protège les fonds même en cas de compromission totale du logiciel du nœud.

VLS propose des intégrations de référence pour CLN et LDK. En octobre 2026, le site du projet le présente comme prêt pour la production et audité ; sa version 0.14.0 date du 7 novembre 2025.
