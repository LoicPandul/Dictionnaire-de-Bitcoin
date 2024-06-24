## SCRIPTWITNESS

Élément dans les entrées de transactions SegWit qui contient les signatures et les clés publiques nécessaires pour déverrouiller les bitcoins envoyés dans la transaction. Semblable au `ScriptSig` des transactions Legacy, le `ScriptWitness` n'est toutefois pas placé au même endroit. En effet, c'est cette partie, que l'on appelle le « témoin » (« witness » en anglais), qui est déplacée dans une base de données séparée afin de résoudre le problème de la malléabilité des transactions. Chaque input SegWit possède son propre `ScriptWitness`, et tous les `ScriptWitness` forment ensemble le champ `Witness` de la transaction.

► ***NOTE :** Attention de ne pas confondre le ScriptWitness avec le WitnessScript. Tandis que le ScriptWitness contient les données de témoin de tout input SegWit, le WitnessScript définit les conditions de dépense d'un UTXO P2WSH ou P2SH-P2WSH et constitue un script à part entière, à la manière du redeemScript pour une sortie P2SH.*

