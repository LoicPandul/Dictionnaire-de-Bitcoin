Mathématicien et cryptographe, cofondateur de Certicom et à qui l'on attribue la proposition de l'algorithme de signature ECDSA. Né en 1947, professeur à l'université de Waterloo (Ontario), il s'intéresse à la cryptographie sur les courbes elliptiques après une conférence de Victor Miller à CRYPTO '85, et cofonde la même année, avec Gord Agnew et Ron Mullin, l'entreprise qui deviendra Certicom (nom adopté en 1995).

En 1992, il propose, en réponse à l'appel à commentaires du NIST sur son premier projet de standard de signature numérique, de transposer l'algorithme à une courbe elliptique : c'est l'origine d'ECDSA. L'algorithme est ensuite normalisé : ANSI X9.62, puis IEEE 1363 et FIPS 186-2 du NIST (2000).

Le lien avec Bitcoin passe par ces deux héritages. Certicom Research publie les paramètres de courbes SEC 2, dont `secp256k1` dans sa version 2.0 du 27 janvier 2010, à laquelle renvoient BIP-0032 et BIP-0340. Bitcoin signe ses transactions avec ECDSA sur cette courbe, ce que BIP-0340 décrit comme l'usage traditionnel, avant que Taproot (2021) n'ajoute les signatures de Schnorr sur la même courbe. Vanstone n'a pas participé à Bitcoin : son nom s'attache à l'algorithme qui sert à signer les transactions.

Il meurt le 2 mars 2014.
