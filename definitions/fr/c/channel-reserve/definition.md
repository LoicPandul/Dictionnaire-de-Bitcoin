Montant minimal que chaque partie d'un canal Lightning doit conserver de son côté et ne peut pas dépenser. Cette réserve garantit que chaque participant a toujours quelque chose à perdre en cas de tentative de fraude, ce qui rend les transactions de pénalité économiquement dissuasives.

Lors de l'ouverture d'un canal, chaque nœud impose à son pair une channel reserve, généralement fixée à 1 % de la capacité du canal (avec un plancher de 546 satoshis, correspondant au dust limit). Par exemple, dans un canal de 1 000 000 sats, chaque partie doit maintenir au moins 10 000 sats de son côté. Ce seuil est défini dans le champ `channel_reserve_satoshis` lors de la négociation du canal (BOLT-02).

La channel reserve réduit légèrement la capacité effectivement utilisable d'un canal. Elle est asymétrique dans le cas du dual funding, où chaque côté peut imposer un montant différent.
