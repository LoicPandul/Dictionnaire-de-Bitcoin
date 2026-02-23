Technique proposée par René Pickhardt en 2019 qui permet à un nœud de routage Lightning de rééquilibrer ses canaux à la volée pour transmettre un paiement qui aurait autrement été refusé faute de liquidité suffisante sur le canal sortant. Le terme « JIT » (*just-in-time*) indique que le rééquilibrage est déclenché au moment précis où le HTLC entrant arrive, et non de manière préventive.

Concrètement, lorsqu'un nœud intermédiaire reçoit un HTLC à transmettre mais manque de fonds sur le canal de sortie, il suspend brièvement le relais et effectue un paiement circulaire à travers ses autres canaux pour déplacer la liquidité nécessaire. Le nœud exploite sa connaissance locale du réseau pour calculer rapidement des cycles de rééquilibrage peu coûteux. Si le rééquilibrage réussit et que les frais engagés sont inférieurs aux frais de routage perçus, l'opération est rentable.

Le *JIT routing* ne nécessite aucune modification de protocole : il s'agit d'un comportement local que chaque nœud de routage peut adopter indépendamment.

Ce mécanisme ne doit pas être confondu avec les *JIT channels*, qui désignent l'ouverture à la volée d'un canal par un LSP.