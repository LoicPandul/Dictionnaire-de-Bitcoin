Clé cryptographique utilisée dans le Lightning Network pour permettre la punition d'un pair qui publie un ancien état de canal. Chaque transaction d'engagement contient une sortie `to_local` qui offre deux chemins de dépense :
* l'un soumis à un délai relatif (`OP_CHECKSEQUENCEVERIFY`) pour le propriétaire,
* l'autre immédiatement dépensable par la contrepartie si elle détient la clé de révocation correspondante.

La clé de révocation est construite de manière collaborative. Pour une transaction d'engagement donnée, Alice fournit un point d'engagement ($C_A$) et Bob fournit un point de base de révocation ($R_B$). La clé publique de révocation est calculée comme suit :

$$\text{Rev} = R_B \cdot \text{SHA256}(R_B \| C_A) + C_A \cdot \text{SHA256}(C_A \| R_B)$$

Ni Alice ni Bob ne peuvent dériver seuls la clé privée correspondante. Lorsque l'état du canal est mis à jour, Alice révèle le secret $c_A$ associé à son point d'engagement. Bob peut alors combiner $c_A$ avec son propre secret $r_B$ pour obtenir la clé privée de révocation et, le cas échéant, construire une transaction de pénalité.