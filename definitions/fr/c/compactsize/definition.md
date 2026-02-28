Format d'encodage d'entiers non signés à longueur variable utilisé dans le protocole Bitcoin pour indiquer le nombre d'éléments ou la taille de certains champs dans les transactions et les messages réseau. Le CompactSize permet d'économiser de l'espace en utilisant moins d'octets pour les petites valeurs. L'encodage fonctionne comme suit :
* les valeurs de 0 à 252 sont encodées sur un seul octet ;
* les valeurs de 253 à 65 535 sont précédées de l'octet `0xfd` et encodées sur 2 octets en little-endian ;
* les valeurs de 65 536 à 4 294 967 295 sont précédées de `0xfe` et encodées sur 4 octets ;
* les valeurs supérieures sont précédées de `0xff` et encodées sur 8 octets.

Le CompactSize est utilisé par exemple pour indiquer le nombre de transactions dans un bloc, le nombre d'entrées ou de sorties dans une transaction, ou encore la longueur d'un script.
