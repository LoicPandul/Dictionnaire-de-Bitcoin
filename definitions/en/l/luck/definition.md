Metric used in mining pools to measure a pool's performance against its theoretical expectations. As the name suggests, it assesses how lucky the pool is at finding blocks. Luck is calculated by comparing the number of shares theoretically needed to find a valid block, based on Bitcoin's current difficulty, with the actual number of shares produced to find that block. A number of shares lower than expected indicates good luck, while a higher number indicates bad luck.

By relating Bitcoin's difficulty to the number of shares the pool produces each second and the difficulty of each share, the pool can calculate the number of shares theoretically needed to find a valid block. For example, suppose that, in theory, a pool needs 100,000 shares to find a block. If the pool actually produces 200,000 before finding a block, its luck is 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Conversely, if this pool found a valid block after producing only 50,000 shares, its luck is 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Luck can only be updated after the pool discovers a block, which makes it a static metric that is refreshed periodically.
