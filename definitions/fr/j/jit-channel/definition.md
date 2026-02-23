Canal Lightning ouvert à la volée par un fournisseur de services Lightning (LSP) au moment où un paiement entrant arrive pour un client qui ne dispose pas encore de canal. Le terme « JIT » (*just-in-time*) signifie que le canal n'est créé qu'au moment précis où il est nécessaire, et non en avance.

Le fonctionnement repose sur le protocole LSPS2 (bLIP-0052). Le client demande au LSP les paramètres de frais d'ouverture, puis obtient un identifiant SCID temporaire qu'il inclut dans son invoice Lightning comme indice de routage. Lorsqu'un payeur envoie le paiement, le LSP intercepte le HTLC, ouvre un canal à zéro confirmation vers le client et transfère le paiement en déduisant les frais d'ouverture du montant reçu. Le client réclame le paiement en révélant la préimage.

Deux modèles de confiance existent :
- dans le modèle par défaut, le LSP diffuse la transaction de financement avant de recevoir la préimage, ce qui laisse la possibilité au client vérifier sa validité ;
- dans le modèle alternatif, le client transmet la préimage immédiatement après l'engagement du HTLC.

Ce mécanisme ne doit pas être confondu avec le *JIT routing*, qui consiste à rééquilibrer des canaux existants.