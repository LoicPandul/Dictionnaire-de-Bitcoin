Structure de données fournie dans le témoin d'une transaction P2TR lors d'une dépense par chemin de script (*script path spend*), telle que définie dans le BIP-0341. Le control block prouve qu'un script donné fait bien partie de l'arbre de scripts (MAST) qui a servi à construire la clé publique Taproot de la sortie.

Il se compose de trois éléments :
- un premier octet qui encode la version du script feuille (*leaf version*) et la parité de la clé publique de sortie ;
- la clé publique interne (*internal key*) sur 32 octets, qui est la clé avant application du tweak ;
- le chemin de Merkle, constitué de zéro à 128 hachages de 32 octets chacun, qui représente la suite des nœuds frères nécessaires pour recalculer la racine de l'arbre depuis la feuille révélée.

Lors de la validation, le nœud recalcule la racine de Merkle à partir du script feuille et du chemin fourni, puis vérifie que le tweak de la clé publique interne avec cette racine correspond bien à la clé publique de sortie inscrite dans le `scriptPubKey`. Ce mécanisme permet de prouver l'appartenance d'un script à l'arbre sans révéler les autres feuilles, ce qui préserve la confidentialité des chemins de dépense non utilisés.