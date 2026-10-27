Développeur, cofondateur de SatoshiLabs, l'entreprise à l'origine du portefeuille matériel Trezor, et auteur de plusieurs BIP sur la dérivation des clés.

En 2013, il coécrit avec Marek Palatinus, Aaron Voisine et Sean Bowe le BIP-0039, qui décrit comment encoder une entropie en une liste de mots, la phrase mnémonique, puis en dériver la graine. Le 24 avril 2014, il reçoit avec Marek Palatinus ceux du BIP-0043, qui réserve un champ `purpose` dans le chemin de dérivation, et du BIP-0044, qui organise les comptes et les chaînes d'adresses d'un portefeuille déterministe. Le 29 décembre 2017, il obtient seul le numéro du BIP-0084, qui applique ce schéma aux comptes P2WPKH (adresses SegWit natives).

Dans Bitcoin Core, il compte 16 commits entre juillet 2015 et avril 2022, dont l'option `uacomment` qui ajoute des commentaires à la chaîne *user agent* du nœud, comme le prévoit le BIP-0014.

Les quatre BIP ont le statut Deployed à la date du 24 octobre 2026. Les portefeuilles et les matériels qui les suivent peuvent restaurer les mêmes clés depuis les mêmes mots, à condition d'utiliser la même phrase secrète et le même chemin de dérivation.
