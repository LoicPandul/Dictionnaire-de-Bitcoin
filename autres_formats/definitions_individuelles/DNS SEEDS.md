## DNS SEEDS

Points de connexion initiaux pour les nouveaux nœuds Bitcoin qui rejoignent le réseau. Ces seeds, qui sont en fait des serveurs DNS spécifiques, ont leur adresse intégrée de façon permanente dans le code de Bitcoin Core. Lorsqu'un nouveau nœud se lance, il contacte ces serveurs pour obtenir une liste aléatoire d'adresses IP de nœuds Bitcoin à priori actifs. Le nouveau nœud pourra ainsi établir des connexions avec les nœuds de cette liste afin d'obtenir les informations pour faire son IBD et se synchroniser sur la chaîne avec le plus de travail accumulé. En 2023, voici la liste des DNS seeds de Bitcoin Core et les personnes responsables de leur maintenance (bitcoin/src/kernel/chainparams.cpp) :
* seed.bitcoin.sipa.be : Pieter Wuille ;
* dnsseed.bluematt.me : Matt Corallo ;
* dnsseed.bitcoin.dashjr.org : Luke Dashjr ;
* seed.bitcoinstats.com : Christian Decker ;
* seed.bitcoin.jonasschnelli.ch : Jonas Schnelli ;
* seed.btc.petertodd.net : Peter Todd ;
* seed.bitcoin.sprovoost.nl : Sjors Provoost ;
* dnsseed.emzy.de : Stephan Oeste ;
* seed.bitcoin.wiz.biz : Jason Maurice.

Les DNS seeds représentent le second moyen, par ordre de priorité, pour un nœud de Bitcoin d'établir des connexions. Le premier moyen consiste à utiliser le fichier peers.dat que le nœud a lui-même créé. Ce fichier est naturellement vide dans le cas d'un nouveau nœud, à moins que l'utilisateur l'ai modifié manuellement.

> ► *Attention, les DNS seeds ne doivent pas être confondus avec les « seed nodes », qui sont eux la troisième manière d'établir des connexions. Pour plus d'informations, voir la définition de [**SEED NODES**](/dictionnaire/S.md#seed-nodes).*

