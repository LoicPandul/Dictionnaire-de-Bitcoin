Attaque par déni de service sur le Lightning Network qui consiste à bloquer la capacité de routage d'un ou plusieurs canaux de paiement pendant une durée prolongée, empêchant les nœuds honnêtes de router des paiements. L'attaquant s'envoie un paiement fictif à lui-même à travers une série de canaux intermédiaires, puis refuse de finaliser ou d'annuler le HTLC, ce qui immobilise les fonds des nœuds de routage sans frais pour l'attaquant.

L'attaque se décline en deux variantes :
* Le *liquidity jamming* (décrit dès 2015 sous le nom de « loop attack ») exploite l'effet de levier du routage multi-sauts : avec $x$ bitcoins, un attaquant peut verrouiller jusqu'à $20x$ bitcoins sur un chemin de 20 canaux.
* Le *slot jamming* exploite la limite de 483 HTLC simultanés par canal : en envoyant 483 micro-paiements, un attaquant sature les emplacements disponibles avec un capital minimal.

Plusieurs pistes de mitigation sont explorées : frais payés à l'avance (*upfront fees*) par l'expéditeur, système de réputation locale entre pairs, certificats de preuve de fonds (*stake certificates*) et jetons de réputation. Le bLIP-0004 propose un mécanisme d'approbation des HTLC (*HTLC endorsement*) comme première mesure concrète. Aucune solution définitive n'a encore fait consensus.
