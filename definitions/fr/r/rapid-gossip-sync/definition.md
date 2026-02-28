Protocole de synchronisation du graphe des canaux Lightning qui permet à un nœud de rattraper l'état du réseau en téléchargeant un instantané compact depuis un serveur, plutôt que de collecter les messages gossip un par un via le réseau pair-à-pair.

Un serveur RGS enregistre les annonces et mises à jour de canaux, puis calcule un delta par rapport à la dernière synchronisation du client. Le format omet les signatures et encode les données de manière incrémentale, ce qui réduit considérablement le volume transféré : un instantané complet du graphe occupe environ 3,3 Mo (1,5 Mo compressé), une synchronisation hebdomadaire environ 566 Ko, et une synchronisation quotidienne seulement 99 Ko compressés.

Développé dans le cadre de LDK, ce protocole cible les clients mobiles où la bande passante et le temps de synchronisation sont limités. Le calcul des routes reste côté client, ce qui préserve la vie privée de l'utilisateur.
