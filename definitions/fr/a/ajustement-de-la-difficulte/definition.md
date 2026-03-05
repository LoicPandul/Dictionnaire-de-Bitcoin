L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin. Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L'ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d'un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. La formule exécutée par les nœuds pour calculer la nouvelle cible est la suivante :

$$N = A \cdot \left(\frac{T}{1\,209\,600}\right)$$

Où :
* $N$ : la nouvelle cible ;
* $A$ : l'ancienne cible ;
* $T$ : le temps écoulé entre le premier et le dernier bloc de la période en secondes ;
* $1\,209\,600$ : le temps cible en secondes pour 2016 blocs à 10 minutes d'intervalle ($2016 \times 600$).

En raison d'un bug off-by-one introduit par Satoshi Nakamoto, $T$ mesure en réalité la durée de 2015 intervalles de blocs, et non 2016. Le calcul compare en effet l'horodatage du premier bloc de la période (bloc $n$) à celui du dernier (bloc $n + 2015$), ce qui ne couvre que 2015 intervalles. Un calcul correct aurait comparé le dernier bloc de la période précédente (bloc $n - 1$) au dernier bloc de la période actuelle (bloc $n + 2015$), soit 2016 intervalles. Ce bug introduit un biais d'environ 0,05 % vers une difficulté légèrement trop élevée par rapport à ce qu'elle devrait être. Il est surtout à l'origine de la faisabilité de l'attaque *time warp*, car les périodes de retarget ne se chevauchent pas.

*En français, on parle également parfois de « reciblage » pour évoquer l'ajustement.*