Metric used to estimate the time a mining pool needs to find a block, based on the network difficulty and the pool's hashrate. It is calculated by taking the number of shares expected to find a block and dividing it by the pool's hashrate. For example, if a mining pool has 200 miners, and each generates an average of 4 shares per second, the pool's total computing power is 800 shares per second:

```text
200 * 4 = 800
```

Assuming that, on average, 1 million shares must be produced to find a valid block, the pool's average round duration will be 1,250 seconds, or about 21 minutes:

```text
1,000,000 / 800 = 1,250
```

In practice, this means that on average the mining pool should find a block about every 21 minutes. This metric fluctuates with changes in the pool's hashrate: an increase in hashrate reduces the average round duration, while a decrease lengthens it. It also fluctuates with each periodic change in the Bitcoin difficulty target (every 2,016 blocks). This measure does not take into account blocks found by other pools and focuses solely on the internal performance of the pool being studied.
