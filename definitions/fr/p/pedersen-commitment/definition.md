Un Pedersen commitment est un type d'engagement cryptographique présentant la propriété d'être homomorphique vis-à-vis de l'opération d'addition. Cela signifie qu'il est possible de valider la somme de deux engagements sans dévoiler les valeurs individuelles.

Formellement, si :
$$
C_1\ =\ commit(m_1,\ r_1) \quad C_2\ =\ commit(m_2,\ r_2)
$$

alors :
$$
C_3\ =\ C_1 \cdot C_2\ =\ commit(m_1\ +\ m_2,\ r_1\ +\ r_2)
$$

Cette propriété devient utile, par exemple, pour dissimuler les montants de *tokens* échangés dans des systèmes de cryptomonnaies, comme par exemple RGB, tout en pouvant vérifier les totaux.