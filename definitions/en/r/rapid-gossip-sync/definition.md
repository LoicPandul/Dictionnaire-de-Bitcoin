Lightning channel graph synchronization protocol that lets a node catch up with the state of the network by downloading a compact snapshot from a server, rather than collecting gossip messages one by one over the peer-to-peer network.

A Rapid Gossip Sync (RGS) server records channel announcements and updates, then computes a delta relative to the client's last synchronization. The format omits signatures and encodes the data incrementally, which considerably reduces the volume transferred: a full snapshot of the graph takes about 3.3 MB (1.5 MB compressed), a weekly synchronization about 566 kB, and a daily synchronization only 99 kB compressed.

Developed as part of LDK, this protocol targets mobile clients, where bandwidth and synchronization time are limited. Route computation stays on the client side, which preserves the user's privacy.
