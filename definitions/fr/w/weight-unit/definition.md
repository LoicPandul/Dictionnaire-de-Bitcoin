Unité de mesure introduite par SegWit (BIP-0141) pour quantifier l'espace qu'une transaction ou un bloc occupe par rapport à la limite maximale autorisée. Chaque *weight unit* (WU) représente 1/4 000 000e de la capacité maximale d'un bloc. Cette unité remplace la mesure en octets bruts qui était utilisée avant SegWit, et permet d'appliquer une pondération différenciée selon la nature des données dans une transaction.

Le calcul du poids d'une transaction repose sur une distinction entre les données *non-witness* (version, inputs, outputs, *locktime*) et les données *witness* (signatures, clés publiques et autres éléments de preuve ajoutés par SegWit). La formule est la suivante :

$$\text{poids} = \text{taille sans witness} \times 4 + \text{taille du witness} \times 1$$

Autrement dit, chaque octet de données *non-witness* compte pour 4 WU, tandis que chaque octet de données *witness* ne compte que pour 1 WU. Pour une transaction *legacy* (sans SegWit), il n'y a pas de données *witness*, donc le poids est simplement 4 fois la taille en octets. Par exemple, une transaction *legacy* P2PKH classique de 226 octets pèse $226 \times 4 = 904$ WU.

Pour une transaction SegWit équivalente (P2WPKH, 1 input, 2 outputs), la taille totale est d'environ 222 octets, dont environ 110 octets de *witness* (signature et clé publique). Le poids est alors :

$$112 \times 4 + 110 \times 1 = 448 + 110 = 558 \text{ WU}$$

Cela représente une réduction d'environ 38 % par rapport à la transaction *legacy* équivalente, ce qui permet d'inclure davantage de transactions dans un bloc.

La limite de bloc est fixée à 4 000 000 WU. Si un bloc ne contient que des transactions *legacy*, cette limite est équivalente à l'ancienne limite de 1 000 000 d'octets ($1\,000\,000 \times 4 = 4\,000\,000$), ce qui assure la rétrocompatibilité avec les nœuds non mis à jour. En pratique, avec une majorité de transactions SegWit, les blocs atteignent environ 2 à 3 Mo en taille réelle. Le maximum théorique approche 4 Mo, mais uniquement dans le cas pathologique d'un bloc rempli presque exclusivement de données *witness*.

Pour convertir un poids en octets virtuels (*vbytes*), il suffit de diviser par 4 : $\text{vbytes} = \text{poids} / 4$. Les frais de transaction sont généralement exprimés en sat/vB (satoshis par *vbyte*).