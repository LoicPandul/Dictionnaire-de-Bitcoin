L'Heure Unix ou Temps Unix représente le nombre de secondes écoulées depuis le 1er janvier 1970 à minuit UTC (Époque Unix). Ce système est utilisé dans les systèmes d'exploitation Unix et dérivés pour marquer le temps de manière universelle et standardisée. Il permet la synchronisation des horloges et la gestion des événements dans le temps, indépendamment des fuseaux horaires.

Dans le cadre de Bitcoin, on l'utilise pour l'horloge locale des nœuds, qui sert de référence pour vérifier la validité des horodatages des blocs. En effet, pour qu'un bloc soit accepté par un nœud, son horodatage doit se situer entre le MTP (temps médian des 11 derniers blocs minés) et l'heure locale du nœud plus 2 heures :

```text
MTP < Horodatage valide <= (heure locale + 2h)
```

Jusqu'à Bitcoin Core 26, l'heure locale était corrigée par le *network-adjusted time*, une médiane des temps annoncés par les pairs. Ce temps ajusté a été retiré du code de consensus dans Bitcoin Core 27.0.

On utilise également l'Heure Unix pour établir des *timelocks*, lorsque ceux-ci se basent sur l'heure réelle, et non pas sur un nombre de blocs.