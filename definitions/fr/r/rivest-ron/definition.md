Cryptographe américain, au MIT depuis 1974 et aujourd'hui professeur de l'Institut, Ron Rivest est l'un des trois inventeurs de RSA et l'auteur, avec Adi Shamir, de deux systèmes de micropaiement parus avant Bitcoin.

Reçu par la revue le 4 avril 1977, l'article de Rivest, Shamir et Leonard Adleman qui décrit RSA paraît en 1978 dans *Communications of the ACM*. Il présente une méthode où la clé qui chiffre est publique et celle qui déchiffre reste secrète, et où un message se signe avec la clé privée et se vérifie avec la clé publique. C'est l'idée de Clé publique et de Signature numérique sur laquelle repose Bitcoin, même si Bitcoin ne signe pas avec RSA : il utilise ECDSA, puis Schnorr, sur la courbe secp256k1.

En avril 1996, Rivest et Shamir présentent PayWord et MicroMint, deux systèmes pour payer de très petites sommes sur Internet en limitant les opérations à clé publique. PayWord repose sur des chaînes de valeurs obtenues par une Fonction de hachage : l'utilisateur signe la chaîne une seule fois, puis dévoile ses maillons un à un pour payer. MicroMint représente les pièces par des collisions de hachage. Le livre blanc de Bitcoin ne cite pas ces travaux : ils restent des systèmes de paiement électronique antérieurs.

Rivest reçoit avec Shamir et Adleman le prix Turing 2002 pour leur contribution à rendre la cryptographie à clé publique utilisable en pratique.
