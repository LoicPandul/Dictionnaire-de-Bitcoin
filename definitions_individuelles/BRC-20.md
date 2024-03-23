## BRC-20

BRC-20 définit un ensemble de règles et de méthodes à respecter pour permettre une interaction avec des jetons non natifs sur Bitcoin. Il s'appuie sur les inscriptions du protocole Ordinals afin de définir des fonctions interprétées en dehors de la chaine. Ce standard a été créé par le développeur Domo, au début du mois de mars 2023. Selon son créateur, ce standard n'est qu'une expérimentation. Cela n'a pas empêché la machine spéculative de prendre le dessus durant les mois d'avril et de mai 2023. Des milliers d'investisseurs se sont emparés de ce standard, en achetant massivement les jetons BRC-20, créant au passage une hausse soudaine et historique des frais de transaction sur Bitcoin. Les jetons BRC-20 sont dénués d'existence concrète sur Bitcoin. Ils sont off-chain. Ce protocole utilise simplement Bitcoin, à travers le protocole Ordinals, pour stocker et horodater des fonctions permettant la gestion des jetons BRC-20. Ces fonctions sont encodées dans un format texte JSON, puis elles sont diffusées sous forme d’inscription Ordinals sur Bitcoin. Il en existe trois :
* `deploy`, qui permet de créer un nouveau jeton BRC-20 et de définir ses conditions d'utilisation ;
* `mint`, qui permet de réclamer des jetons BRC-20 spécifiques. Cela représente leur émission ;
* `transfer`, qui permet de transférer des jetons BRC-20 entre plusieurs utilisateurs.

Pour exécuter ce protocole, il faut que des personnes maintiennent des serveurs qui recensent l'intégralité des fonctions. Le standard BRC-20 est alors une utilisation très peu optimisée de Bitcoin par rapport à un protocole tel que RGB.

