Développeur de logiciels Bitcoin, créateur de Sparrow Wallet et auteur de BIP-0329, le format d'export des étiquettes d'un portefeuille.

Il publie la première version de Sparrow sur GitHub le 12 avril 2020. Ce premier jalon (v0.5) est un simple éditeur de transactions, sans portefeuille, qui charge des fichiers PSBT, lit une transaction en hexadécimal et en détaille le contenu. En septembre 2020, Sparrow est présenté comme un portefeuille de bureau qui gère les adresses simples et multisignatures, les PSBT, les portefeuilles matériels et la sélection des pièces.

Le 24 août 2022, Craig Raw soumet à la liste bitcoin-dev un projet de BIP pour standardiser l'export des étiquettes que l'utilisateur attache à ses adresses et à ses transactions. Face à SLIP-0015, le format de stockage chiffré des étiquettes de SatoshiLabs (Trezor), il explique les différences entre les deux. Sparrow importe et exporte ce format depuis la version 1.7.2, publiée en février 2023, qui ajoute aussi la prise en charge de Taproot avec Bitcoin Core.

En 2026, il obtient les numéros de deux autres BIP, tous deux à l'état de brouillon : BIP-0392, qui définit les descripteurs `sp()` pour les *silent payments* (6 février), et BIP-0393, qui ajoute des annotations aux descripteurs de script de sortie, par exemple la hauteur de bloc à partir de laquelle chercher les fonds d'un portefeuille (17 mars).
