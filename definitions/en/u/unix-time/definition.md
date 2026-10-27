Number of seconds elapsed since January 1, 1970 at midnight UTC (the Unix epoch). This system is used in Unix operating systems and their derivatives to mark time in a universal, standardized way. It allows clock synchronization and the management of events over time, independently of time zones.

In Bitcoin, it is used for the nodes' local clock, which is the reference used to check the validity of block timestamps. For a block to be accepted by a node, its timestamp must fall between the MTP (the median time past of the last 11 mined blocks) and the node's local time plus 2 hours:

```text
MTP < valid timestamp <= (local time + 2h)
```

Up to Bitcoin Core 26, local time was corrected by the network-adjusted time, a median of the times announced by peers. This adjusted time was removed from the consensus code in Bitcoin Core 27.0.

Unix time is also used to set timelocks, when they are based on real time rather than on a number of blocks.
