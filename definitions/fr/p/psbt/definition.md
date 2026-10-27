Sigle de « *Partially Signed Bitcoin Transaction* ». C'est une spécification introduite avec le BIP-0174 pour standardiser la manière dont les transactions non finalisées sont construites dans les logiciels en rapport avec Bitcoin, comme les logiciels de portefeuille. Un PSBT encapsule une transaction dans laquelle les inputs peuvent ne pas être entièrement signés. Il inclut toutes les informations nécessaires pour qu'un participant puisse signer la transaction sans nécessiter des données supplémentaires. Ainsi, un PSBT peut se présenter sous 3 formes différentes :
* Une transaction entièrement construite, mais pas encore signée ;
* Une transaction partiellement signée, où certains inputs sont signés tandis que d'autres ne le sont pas encore ;
* Ou une transaction Bitcoin entièrement signée, qui pourra être convertie pour être prête pour la diffusion sur le réseau.

![Un même PSBT, créé par le logiciel, reçoit la signature d'Alice puis celle de Bob, puis est finalisé en une transaction diffusable.](./assets/image-1.png)

Le format PSBT facilite l'interopérabilité entre différents logiciels de portefeuille et périphériques de signature (hardware wallet). La version 0 des PSBT est définie dans le BIP-0174, et la version 2 dans le BIP-0370. Depuis Bitcoin Core 32.0, les RPC de PSBT créent par défaut des PSBT de version 2.

*La version 1 des PSBT n'existe pas. Étant donné que la version 0 était la première version, la seconde version était familièrement appelée version 2. Ava Chow, qui a rédigé le BIP-0370, a donc décidé de donner le numéro 2 à cette nouvelle version afin d'éviter toute confusion.*
