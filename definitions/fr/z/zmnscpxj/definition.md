Développeur pseudonyme, contributeur de Core Lightning, auteur de CLBOSS et coauteur de la proposition swap-in-potentiam. Il signe ZmnSCPxj et son identité n'est pas publique.

Dans Core Lightning, l'implémentation Lightning développée par Blockstream, il écrit multifundchannel. Cette commande ouvre plusieurs canaux vers des pairs différents dans une seule transaction de financement, ce qui économise des frais on-chain. Il ouvre la *pull request* correspondante en juin 2020 et la commande est livrée dans la version 0.9.1, le 15 septembre 2020.

Le 1er octobre 2020, il crée le dépôt de CLBOSS, un gestionnaire automatique pour les nœuds de routage Core Lightning. Le programme exécute régulièrement des modules qui ouvrent des canaux vers des nœuds utiles quand les frais on-chain sont bas, achètent de la capacité entrante par des swaps, rééquilibrent les canaux et ajustent les frais de relais. En 2025, la propriété du dépôt passe à Ken Sedgwick, qui en assure la maintenance.

Le 3 janvier 2023, il publie sur la liste lightning-dev, avec Jesse Posner, « Swap-in-Potentiam: Moving Onchain Funds "Instantly" To Lightning ». Le problème visé : un utilisateur qui reçoit des bitcoins on-chain doit attendre plusieurs confirmations avant de les mettre dans un canal, sauf à faire confiance à un canal sans confirmation. Dans leur proposition, l'utilisateur et un fournisseur de liquidité détiennent ensemble les fonds sur une adresse réutilisable. L'utilisateur peut les déplacer vers un canal avec l'aide du fournisseur, ou les récupérer seul après un délai si le fournisseur disparaît. Une variante, swaproot, est utilisée dans le portefeuille Phoenix.

Son travail touche Core Lightning, le Lightning Network, le financement de canaux et le swap-in-potentiam.
