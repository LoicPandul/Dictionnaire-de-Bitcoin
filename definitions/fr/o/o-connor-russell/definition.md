Développeur chez Blockstream, créateur du langage Simplicity et proposant de la méthode d'activation Speedy Trial utilisée pour Taproot.

En octobre 2017, il présente à l'atelier PLAS de l'ACM l'article « Simplicity: A New Language for Blockchains », mis en ligne sur arXiv le 8 novembre. Simplicity est un langage typé, sans boucle ni récursion, dont la sémantique est formalisée dans l'assistant de preuve Coq. Il se veut une alternative à Bitcoin Script, avec un langage dont on peut démontrer le comportement et borner le coût de calcul avant l'exécution d'un contrat.

En mars 2021, la communauté cherche comment activer Taproot. Selon BIP-0343, O'Connor propose Speedy Trial, que David Harding expose sur la liste bitcoin-dev : les mineurs disposent d'environ 3 mois pour signaler leur accord, et l'activation échoue s'ils n'atteignent pas le seuil de 90 %. Les PR #21377 et #21686 intègrent la méthode et les paramètres de Taproot dans Bitcoin Core le 15 avril 2021, et Taproot s'active au bloc 709 632, en novembre 2021.

Simplicity est ensuite déployé sur la sidechain Liquid : il est activé sur son testnet le 9 octobre 2024, puis lancé sur son réseau principal le 31 juillet 2025.
