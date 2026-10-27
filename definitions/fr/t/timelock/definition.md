Primitive de contrat intelligent qui permet de définir une condition temporelle à remplir pour qu'une transaction puisse être ajoutée à un bloc. Il existe deux types de timelocks sur Bitcoin : 
* Le timelock absolu, qui spécifie un moment précis avant lequel la transaction ne peut être incluse dans un bloc ; 
* Le timelock relatif, qui définit un délai à partir de la confirmation de la sortie que la transaction dépense. 

Le timelock absolu peut être défini soit sous la forme d'une date exprimée en temps Unix, soit sous la forme d'un numéro de bloc. Le timelock relatif se compte soit en blocs, soit en tranches de 512 secondes. Enfin, le timelock peut s'appliquer soit à un output de transaction grâce à l'utilisation d'un opcode spécifique dans le script de verrouillage (`OP_CHECKLOCKTIMEVERIFY` ou `OP_CHECKSEQUENCEVERIFY`), soit à une transaction entière grâce à l'utilisation du champ `nLockTime`, soit à un input spécifique grâce à l'utilisation du champ `nSequence`.

![Les quatre timelocks de Bitcoin rangés en deux sur deux : absolu ou relatif, champ de la transaction ou opcode du script, avec nLockTime, nSequence, OP_CHECKLOCKTIMEVERIFY et OP_CHECKSEQUENCEVERIFY.](./assets/image-1.png)

*On parle également parfois d'un « locktime » pour évoquer un timelock.*
