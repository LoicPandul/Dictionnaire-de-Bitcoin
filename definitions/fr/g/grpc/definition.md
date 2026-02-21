Framework d'appels de procédures distantes (*Remote Procedure Call*) développé par Google. gRPC utilise le format Protocol Buffers pour sérialiser les données et le protocole HTTP/2 pour le transport, offrant des communications performantes et typées entre un client et un serveur.

Dans l'écosystème Lightning, gRPC est l'interface principale utilisée par LND pour exposer ses fonctionnalités. Les outils comme LNCLI interagissent avec le nœud Lightning via des appels gRPC pour gérer les canaux, envoyer des paiements, consulter les balances ou configurer le routage.
