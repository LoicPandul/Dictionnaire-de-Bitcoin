Champ de 4 octets présent dans l'en-tête de chaque bloc Bitcoin, qui encode la cible de difficulté sous une forme compacte : le premier octet indique le nombre d'octets de la cible complète (l'exposant), et les trois octets suivants constituent la mantisse (les chiffres significatifs de la cible). La formule de décodage est : $cible = mantisse \times 256^{(exposant - 3)}$.

![Le champ nBits du bloc de genèse, 0x1d00ffff : un octet d’exposant (0x1d = 29) et trois octets de mantisse (0x00ffff), qui donnent la cible = mantisse × 256^(exposant − 3).](./assets/image-1.png)

Un hash de bloc doit être inférieur ou égal à la valeur cible encodée dans `nBits` pour que le bloc soit considéré comme valide. Ce champ est recalculé tous les 2 016 blocs lors de l'ajustement de la difficulté, afin de maintenir un intervalle moyen d'environ 10 minutes entre chaque bloc.
