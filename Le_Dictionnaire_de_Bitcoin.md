# Le Dicitonnaire de Bitcoin 2024





# A
**ADRESSE DE RÉCEPTION -**

Information utilisée pour recevoir des bitcoins. Une adresse est construite en hachant une clé publique, à l'aide de SHA256 et de RIMPEMD160, et en ajoutant des métadonnées à ce condensat. Les clés publiques utilisées pour construire une adresse de réception font partie du portefeuille de l'utilisateur et sont donc dérivées depuis sa graine.

Les adresses SegWit sont composées des informations suivantes : 
* Un HRP pour désigner « bitcoin » : bc ; 
* Un séparateur : 1 ; 
* La version de SegWit utilisée : q ou p ; 
* La charge utile : le condensat de la clé publique ; 
* La somme de contrôle : un code BCH.

Une adresse de réception peut être représentée sous la forme d'une chaîne de caractères alphanumériques ou sous la forme d'un QR code. Chaque adresse peut être utilisée plusieurs fois, mais c'est une pratique très déconseillée. En effet, dans le but de maintenir un certain niveau de confidentialité, il est conseillé de n'utiliser chaque adresse Bitcoin qu'une seule fois. Il faut en générer une nouvelle pour tout paiement entrant vers son portefeuille.

Une adresse est encodée en Bech32 pour les adresses SegWit V0, en Bech32m pour les adresses SegWit V1, et en Base58check pour les adresses Legacy.

D'un point de vue technique, une adresse ne permet pas réellement de recevoir des bitcoins, mais plutôt de bloquer des bitcoins à l'aide d'un script, en mettant des contraintes sur leur dépense.

**AJUSTEMENT DE LA DIFFICULTÉ (OU RECIBLAGE) -**

L'ajustement de la difficulté est un processus périodique qui redéfinit la cible de difficulté pour le mécanisme de la preuve de travail (le minage) sur Bitcoin.

Cet évènement intervient tous les 2016 blocs (environ toutes les deux semaines). Il vient augmenter ou baisser le facteur de difficulté (également nommé la cible de difficulté), en fonction de la rapidité à laquelle les 2016 derniers blocs ont été trouvés. L’ajustement vise à conserver un taux de production de blocs stable et prévisible, à une fréquence d’un bloc toutes les 10 minutes, malgré les variations de la puissance de calcul déployée par les mineurs. La modification de la difficulté lors de l'ajustement est limitée à un facteur 4. Le calcul qu'effectuent les nœuds pour calculer la nouvelle cible est le suivant : *N = A * (T / 1 209 600)*. Où :
* N : La nouvelle cible ;
* A : L'ancienne cible des 2016 derniers blocs ;
* T : Le temps total réel des 2016 derniers blocs en secondes ;
* 1 209 600 : Correspond au temps cible, en secondes, pour produire 2016 blocs avec un intervalle de 10 minutes entre chacun.
> *En français, on parle parfois également de « reciblage » pour évoquer l'ajustement. En anglais, on parle de « Difficulty Adjustment ».*

**ARBRE DE MERKLE -**
Un Arbre de Merkle est un accumulateur cryptographique. C’est une méthode pour justifier l’appartenance d’une information donnée à un ensemble plus grand. C'est une structure de données qui facilite la vérification d’informations dans un format compact.

Dans le système Bitcoin, les arbres de Merkle sont utilisés pour regrouper et condenser les transactions d'un bloc en un unique hachage, appelé la racine de Merkle (ou « Top Hash »). Chaque transaction est hachée, puis les hachages adjacents sont hachés ensemble de façon hiérarchique jusqu'à ce que la racine de Merkle soit obtenue.





