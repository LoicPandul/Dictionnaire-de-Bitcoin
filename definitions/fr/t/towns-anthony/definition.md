Développeur de Bitcoin Core, connu sous le surnom aj, coauteur de plusieurs BIP sur Taproot, ANYPREVOUT et signet. Son premier commit dans le dépôt de Bitcoin Core date du 23 août 2016.

Le 19 janvier 2020, les BIP-0341 et BIP-0342, qui définissent les règles de dépense et la validation des scripts de Taproot, sont assignés à Pieter Wuille, Jonas Nick et à lui. Taproot s'active au bloc 709 632, le 14 novembre 2021. Il est aussi coauteur de BIP-0118, qui propose le drapeau de signature `SIGHASH_ANYPREVOUT`: le BIP est rédigé par Christian Decker (son en-tête le date du 28 février 2017) et reçoit son numéro en mai 2018 ; Anthony Towns y est ajouté ensuite comme coauteur. Le BIP reste au statut brouillon en 2026.

Avec Karl-Johan Alm, il rédige BIP-0325, qui décrit signet, un réseau de test où les blocs sont signés en plus de la preuve de travail. Le BIP est daté du 20 mars 2019 et reçoit son numéro le 4 novembre 2019.

En septembre 2022, il annonce sur la liste de diffusion bitcoin-dev Bitcoin Inquisition, un fork de Bitcoin Core qui refuse le réseau principal et testnet (seuls signet et regtest sont acceptés) et qui applique des règles de *soft fork* issues de propositions bien spécifiées. Le dépôt est créé le 15 mai 2022 et la première version, `inq-v23.0`, est publiée par lui le 13 décembre 2022. Il y a fusionné toutes les PR, ce qui fait de lui son mainteneur. Le but est d'évaluer en conditions réelles des propositions de *soft fork*, et de pouvoir comparer des approches concurrentes comme `OP_CHECKTEMPLATEVERIFY` et `SIGHASH_ANYPREVOUT`, avant tout déploiement sur le réseau principal.

Il est également l'auteur de BIP-0434 (négociation de fonctionnalités entre pairs), assigné le 14 janvier 2026.
