Introduit le format d'adresse bech32 pour les adresses SegWit V0. Ce format d'adresse est caractérisé par le préfixe `bc1q`. Le format bech32 offre plusieurs avantages : 
* Il demande moins d'espace dans les codes QR ;
* Il est plus facilement interprétable par les humains ;
* Il dispose d'une somme de contrôle qui détecte toute erreur portant sur 4 caractères au plus (le BIP déconseille de corriger automatiquement les fautes de frappe, au mieux d'indiquer où se trouve l'erreur).
Ces caractéristiques facilitent l'utilisation des adresses de réception tout en minimisant les risques d'erreurs.
