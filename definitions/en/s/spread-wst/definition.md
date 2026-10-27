In Whirlpool Stat Tool, the statistics tool for Whirlpool, the Samourai Wallet coinjoin, the spread is an indicator that measures how evenly the mixing process has worked from the point of view of a given coin. Two spreads are distinguished: the forward spread and the backward spread.

The forward spread is calculated as the ratio between the coin's forward anonset and the total number of coins created after the coin's Tx0. For example, if the pool holds 100 coins and the coin has an anonset of 70, the coin's forward spread is 70%.

The backward spread, for its part, is the ratio between the coin's backward anonset and the total number of Tx0s created before the coin's last mix. So, if the coin's backward anonset is 95 and there were 100 Tx0s before the last mix, the coin's backward spread is 95%.

These two indicators make it possible to evaluate how effectively the coin has been mixed relative to the potential the pool offers. A low forward spread, such as 5%, indicates a large margin for improvement through additional mixes. Conversely, a high forward spread, such as 97%, means that little additional anonset can be gained from further coinjoins.

*Samourai Wallet ceased operations on April 24, 2024, with the arrest of its founders and the seizure of its servers: these indicators now apply only to mixes carried out before that date.*
