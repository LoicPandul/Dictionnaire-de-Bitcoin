Référence unique à une sortie de transaction (*output*). Il est constitué de deux éléments :
* `txid` : l'identifiant de la transaction qui a créé l'output ;
* `vout` : l'index de l'output dans la transaction.

La combinaison de ces deux éléments permet d'identifier précisément un output de transaction. Par exemple, si une transaction a un `txid` de `abc...123` et que l'index de l'output est `0`, l'outpoint sera noté :

![L'outpoint `a1b2c3d4…f9e0:1` placé dans l'entrée d'une nouvelle transaction désigne, par son txid, la transaction précédente, puis, par son index vout, la sortie 1 de cette transaction.](./assets/image-1.png)

```text
abc...123:0
```

L'outpoint est utilisé dans les inputs (`vin`) d'une nouvelle transaction pour indiquer quel UTXO est dépensé.

*Le terme « outpoint » désigne une simple référence, qui peut pointer vers un output déjà dépensé. Un UTXO est un output non dépensé, l'outpoint n'est donc pas un synonyme de « UTXO ».*
