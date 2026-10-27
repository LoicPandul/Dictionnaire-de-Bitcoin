Individual node within the Spark Entity (SE), participating in the threshold signing protocol that secures off-chain transfers in Spark. Each SO holds a fragment of the SE's key share, without ever possessing the complete key alone. The SOs together (or a threshold of them) cooperate via the FROST protocol to co-sign transactions and refresh key shares during ownership transfers.

SOs also play a watchtower role: they monitor the Bitcoin blockchain to detect possible fraudulent exit attempts by former owners.

If an SO is unavailable, transfers may be temporarily blocked, but users keep the ability to exit unilaterally to the base layer. At the launch of Spark, two operators (Lightspark and Flashnet) make up the SE, with the aim of expanding the number of operators across diverse jurisdictions to spread the risk.
