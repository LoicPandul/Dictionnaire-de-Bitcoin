Développeur de Bitcoin, premier auteur de BIP-0068 et coauteur de BIP-0112 et BIP-0113, qui introduisent les verrous temporels relatifs.

Le 22 octobre 2014, il figure parmi les neuf auteurs de l'article « Enabling Blockchain Innovations with Pegged Sidechains », avec Adam Back, Matt Corallo, Luke Dashjr, Gregory Maxwell, Andrew Miller, Andrew Poelstra, Jorge Timón et Pieter Wuille, qui propose les sidechains à ancrage bilatéral.

Le numéro de BIP-0068 est attribué le 28 mai 2015. Cette proposition, qu'il rédige avec BtcDrak, Nicolas Dorier et kinoshitajona, donne au champ `nSequence` d'une entrée un sens relatif : la transaction reste invalide pendant un délai défini après la confirmation de la sortie qu'elle dépense. Le 10 août 2015, deux autres numéros sont attribués : BIP-0112, qu'il écrit avec BtcDrak et Eric Lombrozo, définit l'opcode OP_CHECKSEQUENCEVERIFY, et BIP-0113, avec Thomas Kerin, fait passer le calcul des verrous temporels à la médiane des 11 derniers blocs (*median time past*). Le 25 septembre 2015, il écrit dans Bitcoin Core le commit « BIP112: Implement CHECKSEQUENCEVERIFY ».

Les trois BIP forment un même *soft fork*. Bitcoin Core 0.12.1, publié le 15 avril 2016, le déploie par le mécanisme BIP-0009, avec un signalement des mineurs ouvert à partir du 1er mai 2016. Ces verrous relatifs servent notamment aux canaux de paiement bidirectionnels.

Dans des BIP datés d'août 2017, il propose avec Kalle Alm et BtcDrak deux modifications de *soft fork* restées au stade de brouillon : BIP-0098 sur les arbres de Merkle rapides et BIP-0117 sur l'exécution par appel terminal.
