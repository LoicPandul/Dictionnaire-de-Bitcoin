Développeur de Bitcoin, coauteur des spécifications de SegWit et auteur d'une proposition de MAST, connu sous le pseudonyme jl2012.

Le 21 décembre 2015, le BIP-0141, qui définit SegWit, reçoit son numéro avec trois auteurs : Eric Lombrozo, Johnson Lau et Pieter Wuille. Le 3 janvier 2016, Johnson Lau et Pieter Wuille obtiennent celui du BIP-0143, qui décrit la signature des transactions pour les programmes témoin de version 0.

Le 2 avril 2016, il propose seul le BIP-0114, qui introduit le MAST : un arbre de Merkle dont chaque feuille est une branche de script, de sorte qu'une dépense ne révèle que la branche exécutée. La proposition est ensuite fermée (statut Closed). Le BIP-0341 de Taproot cite ce travail parmi ses antécédents et remercie Johnson Lau pour ses constructions de branches de Merkle.

En 2016 également, il écrit le BIP-0147, qui impose que l'élément factice consommé en plus par `OP_CHECKMULTISIG` soit un tableau d'octets vide, faute de quoi le script échoue : cet élément n'était pas inspecté et offrait une prise à la malléabilité. Son code NULLDUMMY entre dans Bitcoin Core par un commit du 31 août 2016, et la règle est déployée avec SegWit, par les mêmes paramètres BIP9. Il cosigne aussi, avec Pieter Wuille, le BIP-0146 sur la malléabilité de l'encodage des signatures, resté au statut Closed.
