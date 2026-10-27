Transaction Bitcoin utilisée sur le Lightning Network pour punir un pair qui a publié une ancienne transaction d'engagement révoquée sur la blockchain. Elle permet à la partie lésée de récupérer la totalité des fonds du canal, y compris la part de l'attaquant.

Le mécanisme repose sur les clés de révocation. Lorsqu'un état du canal est mis à jour, chaque partie remet à l'autre le secret de l'ancien état (`per_commitment_secret`), dont l'autre partie dérive la clé de révocation qui permet de dépenser l'intégralité des fonds si cet état venait à être publié. Si un nœud tente de tricher en diffusant un vieil engagement, son pair dispose d'un délai pour détecter la fraude et construire la transaction de pénalité à l'aide de cette clé de révocation. Ce délai est garanti par un timelock `OP_CHECKSEQUENCEVERIFY` sur la sortie du tricheur.

![Alice publie un engagement révoqué : sa sortie reste bloquée `to_self_delay` blocs par `OP_CHECKSEQUENCEVERIFY`, et Bob la reprend avant la fin du délai avec une transaction de pénalité signée par la clé privée de révocation.](./assets/image-1.png)

Les *watchtowers* sont des services tiers qui surveillent la blockchain en permanence pour détecter ces fraudes et diffuser les transactions de pénalité au nom des nœuds hors ligne.
