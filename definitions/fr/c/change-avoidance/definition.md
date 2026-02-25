Stratégie de gestion des UTXOs qui consiste à sélectionner les entrées d'une transaction de manière à éliminer ou minimiser le besoin de créer un output de change. L'objectif est de faire correspondre au plus près la somme des inputs avec le montant du paiement et les frais de transaction.

L'intérêt principal de cette approche est la confidentialité. Un output de change est souvent identifiable par les outils d'analyse de chaîne et constitue une information pour tracer des fonds dans le temps. En l'éliminant, on réduit les informations disponibles pour un observateur extérieur, on s'empêche de révéler des informations dans le futur via la CIOH, et on peut également induire en erreur l'analyse de chaîne.

Certains portefeuilles implémentent cette stratégie automatiquement dans leur algorithme de sélection de pièces.
