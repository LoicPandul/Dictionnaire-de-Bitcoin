# Écarts entre les définitions et les spécifications (BIP, BOLT, bLIP)

Relevés pendant l'écriture de `specifications/fr/*.yaml` ; chaque écart est vérifié et corrigé dans la passe de corrections (lots C1 à C8).

## bip-A

| BIP | La définition dit | Le BIP dit |
| --- | --- | --- |
| BIP-0010 | Statut « *Withdrawn* ». | `Status: Closed`. |
| BIP-0015 | « Quatre mécanismes » : FirstBits, DNS TXT, HTTPS, Namecoin. | 6 schémas : FirstBits, DNS TXT Records, Server Service, HTTPS Web Service, IP Transactions, Namecoin ID. |
| BIP-0021 | Norme « aujourd'hui largement adoptée », sans mention de remplacement. | `Status: Closed`, `Proposed-Replacement: 321` ; bandeau « Superseded by BIP 321 » en tête du texte. |
| BIP-0052 | « Cette proposition reste au stade de brouillon. » | `Status: Closed`. |
| BIP-0053 | « Fait partie du consensus cleanup proposé dans le BIP-0054. » | Document distinct, qui ne cite pas le BIP-0054 (et inversement) ; le BIP-0054 reprend la même règle des transactions de 64 octets. |
| BIP-0054 | « Proposition actuellement en brouillon. » | `Status: Complete`. |
| BIP-0062 | « Il a été retiré (*Withdrawn*). » | `Status: Closed`. |
| BIP-0074 | « Son statut officiel étant *Rejected*. » | `Status: Closed` (le `Comments-Summary: Unanimously Discourage for implementation` est bien présent). |
| BIP-0089 | « Proposition (brouillon). » | `Status: Deployed`. |
| BIP-0100 | Taille maximale ajustée « entre 1 et 32 Mo ». | Aucune borne de 32 Mo dans le texte actuel : `hardLimit` part de 1 000 000 octets et varie d'au plus 5 % par période de 2016 blocs, sur le vote du 1512e bloc. |
| BIP-0116 | « A été supplanté par Taproot (BIP-0341). » | `Status: Draft`, aucun en-tête `Proposed-Replacement`. |
| BIP-0117 | « A été supplanté par Taproot (BIP-0341). » | `Status: Draft`, aucun en-tête `Proposed-Replacement`. |
| BIP-0126 | Transactions dont les entrées ont des « types de scripts différents (P2PKH, P2SH, SegWit...) ». | Une HIT est une transaction dont les scripts des sorties dépensées « are not identical (e.g. a transaction spending outputs which were sent to more than one Bitcoin address) » : scripts différents, pas forcément de types différents. |
| BIP-0127 | « Actuellement au statut de brouillon » ; définit « un format de fichier basé sur Protocol Buffers ». | `Status: Complete` ; changelog 1.0.0 (2026-05-21) : « Advance to Complete », « Remove incomplete and unused protocol buffers part ». |

Source : dépôt bitcoin/bips, commit `100ba872c808946155b1eeb8c4568058f2eea0a7` (2026-10-24).

## bip-B

| BIP | La définition dit | Le BIP dit |
| --- | --- | --- |
| BIP-0148 | « Bien que ce BIP historique n'ait finalement pas été activé » | `Status: Deployed` dans l'en-tête du BIP. |
| BIP-0150 | Le BIP-0324 est « aujourd'hui implémenté en option dans Bitcoin Core ». | Bitcoin Core `doc/bips.md` : transport v2 pris en charge depuis v26.0 sans être actif par défaut, actif par défaut depuis v27.0. |
| BIP-0151 | Le BIP-0324 est « aujourd'hui implémenté en option dans Bitcoin Core ». | Bitcoin Core `doc/bips.md` : transport v2 pris en charge depuis v26.0 sans être actif par défaut, actif par défaut depuis v27.0. |
| BIP-0152 | « Adopté en novembre 2016 dans la version 0.13.0 de Bitcoin Core » | Bitcoin Core `doc/bips.md` : blocs compacts utilisés depuis v0.13.0 ; le tag `v0.13.0` date du 2016-08-22 (v0.13.1 : 2016-10-27). |
| BIP-0173 | Bech32 « permet de détecter et potentiellement de modifier automatiquement les fautes de frappe ». | Section « Error correction » : les implémentations « SHOULD NOT implement correction », au mieux elles signalent où se trouve l'erreur, sans proposer de correction. |
| BIP-0324 | Transport v2 « inclus en option (désactivé par défaut) dans la version 26.0 », activable avec `v2transport=1`. | Bitcoin Core `doc/bips.md` : pris en charge depuis v26.0 sans être actif par défaut, actif par défaut depuis v27.0 (tag du 2024-04-15). |
| BIP-0345 | « Proposé par James O'Beirne » | Auteurs : James O'Beirne et Greg Sanders. |
| BIP-0346 | « Proposé par Steven Roose » | Auteurs : Steven Roose et Brandon Black. |
| BIP-0352 | « Proposition d'amélioration de Josibake et Ruben Somsen » | Auteurs : josibake, Ruben Somsen et Sebastian Falbesoner. |
| BIP-0433 | « un script de 2 octets (`OP_1 0x4e73`) » | Le script est `OP_1 <0x4e73>` : c'est le programme témoin qui fait 2 octets (le script de sortie complet en fait 4). |
| BIP-0434 | Les nœuds annoncent leurs fonctionnalités « via un ensemble standardisé de messages de négociation ». | Le BIP définit un seul message, `feature`, envoyé entre `version` et `verack`. |

## ln


Sources clonées le 2026-10-25 :

- `lightning/bolts`, clone complet (historique nécessaire pour le BOLT 06), SHA `191462825ae341f0a27098765c075f01ca9bc6c2` (dernier commit du 2026-10-19).
- `lightning/blips`, clone `--depth 1`, SHA `ca04f374d03001ddbed60ff109da58bd9c390c9a` (dernier commit du 2026-07-17).

## Méthode pour les statuts BOLT

1. Les BOLT n'ont pas de champ de statut. La liste de référence est l'index de `00-introduction.md` (BOLT 1 à 12, sans le 6) recoupé avec les fichiers `NN-*.md` présents au SHA ci-dessus : 12 fichiers, tous listés dans l'index. Ils reçoivent `status: "Actif"`.
2. Pour trouver les numéros absents, `git log --all --name-only` liste tous les noms de fichiers qui ont existé dans le dépôt. Un seul numéro a disparu : `06-irc-announcements.md`. L'autre nom ancien, `01-messaging-crypto-and-init.md`, est l'ancien nom du BOLT 01 (même numéro, renommé), pas un document retiré.
3. Historique du BOLT 06, d'après les commits :
   - `1393561` (2016-11-14, Christian Decker) « Imported IRC routing announcements » ajoute le fichier ;
   - `76dfd37` (2016-11-15, Rusty Russell) l'inscrit dans l'index comme « BOLT #6: Interim Node and Channel Discovery » ;
   - `f91df05` (2017-10-02, Roman Zeyde) « Remove unused 06-irc-announcements.md file » supprime le fichier ;
   - `ca713c8` (2017-10-17, Rusty Russell) « Remove BOLT #6 from index, spelling list ».
   Le texte du fichier annonçait lui-même son remplacement par « a discovery mechanism that does not rely on a centralized server » ; ce rôle revient au BOLT 07 (« P2P Node and Channel Discovery », ajouté le 2016-11-21 par `2e93a41`). Le BOLT 06 n'a pas été fusionné dans un autre fichier : il a été abandonné, et le numéro n'a jamais été réattribué. Il reçoit `status: "Retiré"`, son titre est le premier titre du fichier historique, et son `url` pointe vers le fichier au commit parent de la suppression (`2aa9f971`).
4. Hors champ, faute de numéro : `bolt-simple-taproot.md` (« Extension BOLT XX: Simple Taproot Channels ») et `proposals/route-blinding.md`.

## Conventions des deux YAML

- Clé `definition` absente quand le dossier `definitions/fr/b/<slug>/` n'existe pas (formats.md : « slug d'une entrée développée s'il y en a une ») : BOLT-06 et bLIP-0042.
- bLIP : `title`, `status` et `created` recopiés tels quels depuis l'en-tête du fichier ; `authors` = noms sans e-mail.

## Points à signaler (hors définitions)

- bLIP-0025 : l'en-tête dit `Status: Draft`, le tableau du README du dépôt dit « Active ». Le YAML garde `Draft` (consigne « tel quel »).
- bLIP-0039 (`Status: Draft`) n'apparaît pas dans le tableau du README du dépôt.
- bLIP-0017 : l'en-tête écrit « Anton Kumaigorodski », le README « Anton Kumaigorodskiy ». Le YAML suit l'en-tête.
- bLIP-0004 : `experiment_end` vaut `1767225600`, soit le 2026-01-01 à 00:00 UTC ; l'expérience est donc terminée, mais le statut reste `Active`.
- bLIP-0042 (Bolt 12 Contacts) n'a pas de définition dans le dictionnaire : candidate pour la phase 5.
- Les `metadata.yaml` des définitions titrent « BLIP-0025 » (majuscules), alors que la charte écrit `bLIP-0025`.

## Écarts entre définitions et spécifications

| Document | La définition dit | La spec dit |
|---|---|---|
| bLIP-0011 | « suivi d'un deux-points et de deux espaces (`: `) » : le code inline ne contient qu'une espace. | « a colon and two spaces (`:  `) », exemple `Alfred:  payment for the bubblegum you owed me`. |
| bLIP-0039 | Le *route blinding* a été « initialement conçu pour BOLT-12 ». | « Blinded paths have been included in the BOLT 4 specification » ; BOLT 12 les utilise nativement. Le mécanisme appartient au BOLT 04. |
| BOLT-02 | Le cycle de vie du canal (ouverture v1 et v2, HTLC, RBF, *quiescence*, fermeture) ne mentionne pas le *splicing*. | Section « Channel Splicing » (feature 62/63) fusionnée le 2026-03-23 (commit `a377265`, PR #1160). Omission. |
| BOLT-12 | « Elle introduit trois concepts » : *offers*, *invoice requests*, invoices. | Le document définit aussi les *invoice errors* et, depuis le 2026-07-27, les *payer proofs* (préfixe `lnp`, commit `e20a924`, PR #1346), ainsi qu'un flux inverse où le commerçant publie un `invoice_request` (« ATM or refund »). Omission. |
| BOLT-09 | Les fonctionnalités sont annoncées dans `init`, `node_announcement` et `channel_announcement`. | La colonne Context couvre aussi les factures BOLT-11 (`9`) et le champ `allowed_features` des chemins aveuglés (`B`). Omission mineure. |
| BOLT-10 | Le nœud interroge « des serveurs DNS autoritaires (*seed nodes*) ». | La spec nomme ces serveurs *DNS Seed* (des serveurs DNS, pas des nœuds Lightning) et leur donne un second rôle, *Assisted Node Location* (retrouver l'adresse actuelle d'un pair connu), absent de la définition. |
| BOLT-04 | Couvre le routage en oignon, le *route blinding* et les erreurs chiffrées. | Le document contient aussi une section « Onion Messages » (messages en oignon), utilisée par BOLT-12. Omission mineure. |
| bLIP-0050 | Schémas communs utilisés « par toutes les spécifications LSPS de niveau supérieur (LSPS1 à LSPS5) ». | Le dépôt bLIP ne contient que LSPS1, LSPS2 et LSPS5 (bLIP-0051, 0052, 0055) ; aucune bLIP LSPS3 ni LSPS4. Formulation à préciser. |
