Dans le logiciel Whirlpool Stat Tool, outil de statistiques de Whirlpool, le coinjoin de Samourai Wallet, le spread est un indicateur permettant de mesurer l'homogénéité du processus de mixage du point de vue d'une pièce donnée. On différenciera 2 spreads : le prospectif et le rétrospectif.

Le spread prospectif est calculé en tant que ratio entre l'anonset prospectif de la pièce et le nombre total de pièces créées après la Tx0 de cette pièce. Par exemple, si dans la pool il y a 100 pièces et que la pièce a un anonset de 70, le spread prospectif de la pièce est alors de 70 %. 

Le spread rétrospectif, quant à lui, est le ratio entre l'anonset rétrospectif de la pièce et le nombre total de Tx0 créées avant le dernier mix de la pièce. Ainsi, si l'anonset rétrospectif de la pièce est de 95 et qu'il y a eu 100 Tx0 avant le dernier mix, alors le spread rétrospectif de la pièce est de 95 %.

Ces deux indicateurs permettent d'évaluer l'efficacité du mixage de la pièce par rapport au potentiel offert par la pool. Un spread prospectif faible, comme 5 % par exemple, indique une importante marge d'amélioration possible par des mixages supplémentaires. Inversement, un spread prospectif élevé, comme par exemple 97 %, signifie que peu d'anonset supplémentaire peut être gagné avec des coinjoins supplémentaires.

*Samourai Wallet a cessé ses activités le 24 avril 2024, avec l'arrestation de ses fondateurs et la saisie de ses serveurs : ces indicateurs ne s'appliquent plus qu'aux mixages réalisés avant cette date.*