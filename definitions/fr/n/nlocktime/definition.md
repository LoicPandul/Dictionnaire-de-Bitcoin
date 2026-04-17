Champ de 4 octets intégré dans chaque transaction Bitcoin, qui spécifie soit une hauteur de bloc absolue (si sa valeur est inférieure à 500 000 000), soit un timestamp Unix absolu (si sa valeur est supérieure ou égale à 500 000 000). La transaction n'est considérée comme finale (donc incluable dans un bloc) qu'une fois cette valeur strictement dépassée par la hauteur du bloc candidat (pour le mode hauteur) ou par le MTP, la médiane des 11 blocs précédents (pour le mode temps). C'est donc un timelock absolu, par opposition aux timelocks relatifs du champ `nSequence`, qui agit au niveau de la transaction entière.

Le `nLockTime` n'est appliqué que si au moins un input de la transaction a un `nSequence` différent de la valeur `0xFFFFFFFF`. Si tous les inputs ont `nSequence = 0xFFFFFFFF`, le champ est totalement ignoré. C'est pourquoi les wallets utilisant le `nLockTime` positionnent typiquement `nSequence = 0xFFFFFFFE`.

`OP_CHECKLOCKTIMEVERIFY` complète ce mécanisme en permettant d'imposer un verrouillage temporel depuis un `scriptPubKey`. L'opcode vérifie 4 conditions :
* la valeur en haut de la pile et le `nLockTime` de la transaction sont du même type (hauteur de bloc ou timestamp),
* la valeur en haut de la pile n'est pas négative,
* la valeur en haut de la pile est inférieure ou égale au `nLockTime` de la transaction,
* le `nSequence` de l'input en cours d'évaluation n'est pas `0xFFFFFFFF`.

CLTV ne vérifie donc jamais directement le temps ou la hauteur : il délègue cette vérification en forçant la transaction de dépense à déclarer un `nLockTime` inférieur ou égal à la valeur voulue par le script.