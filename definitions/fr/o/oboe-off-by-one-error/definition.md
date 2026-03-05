Erreur de logique où une boucle itère une fois de trop ou de moins, souvent due à une mauvaise utilisation des opérateurs de comparaison ou de mauvais indices dans la gestion des structures de données. Deux instances notables de ce bug existent dans Bitcoin.

La plus conséquente se trouve dans le calcul de l'ajustement de la difficulté. L'algorithme mesure le temps écoulé durant une période de 2016 blocs en comparant l'horodatage du premier bloc de la période à celui du dernier, puis compare cette durée au temps cible de $1\,209\,600$ secondes ($2016 \times 600$). Le problème est que la différence entre le premier et le dernier bloc d'une période ne couvre que 2015 intervalles de blocs, et non 2016 :

$$T = t_{2015} - t_0$$

Les intervalles comptés sont :

$$\underbrace{[t_0 \to t_1]}_{1},\ \underbrace{[t_1 \to t_2]}_{2},\ \ldots,\ \underbrace{[t_{2014} \to t_{2015}]}_{2015}$$

Soit 2015 intervalles. Pour en obtenir 2016, il aurait fallu utiliser le dernier bloc de la période précédente comme point de départ :

$$T_{\text{correct}} = t_{2015} - t_{-1}$$

Où $t_{-1}$ désigne l'horodatage du dernier bloc de la période précédente (bloc $n - 1$ pour une période qui commence au bloc $n$). L'algorithme compare donc 2015 intervalles réels au temps théorique de 2016 intervalles. Ce décalage introduit un biais d'environ $\frac{1}{2016} \approx 0{,}05\,\%$ vers une difficulté légèrement surestimée.

Ce bug a surtout pour conséquence que les périodes de retarget ne se chevauchent pas : l'horodatage du dernier bloc d'une période n'entre pas dans le calcul de la période suivante. Cette discontinuité rend possible l'attaque *time warp*, où un attaquant majoritaire manipule l'horodatage du dernier bloc d'une période sans que cela n'affecte le calcul de la période suivante. Corriger réellement ce bug nécessiterait un hard fork, mais les attaques *time warp* peuvent être empêchées via un simple soft fork en ajoutant des contraintes sur les horodatages.

La seconde instance de bug *off-by-one* dans Bitcoin est le *dummy element* dans `OP_CHECKMULTISIG`, où l'opcode consomme un élément de pile supplémentaire par erreur. Ce bug a été corrigé dans les faits par le BIP-0147 (*NULLDUMMY*), qui impose que cet élément soit une valeur nulle.