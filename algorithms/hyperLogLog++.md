# HyperLogLog++

## Preface

- How to estimate the number of unique values (aka cardinality) within a very large dataset?
- This question is called [Count-distinct problem](https://en.wikipedia.org/wiki/Count-distinct_problem) in Computer Science or Cardinality Estimation Problem in Applied Mathematics.
- [HyperLogLog](https://towardsdatascience.com/hyperloglog-a-simple-but-powerful-algorithm-for-data-scientists-aed50fe47869).

## Flajolet-Martin Algorithm

[Paper Link](https://www.sciencedirect.com/science/article/pii/0022000085900418).

![Flajolet-Martin Algorithm](/images/Flajolet-MartinAlgorithm.png)

## LogLog

[Paper Link](https://link.springer.com/chapter/10.1007/978-3-540-39658-1_55).

![LogLog Algorithm](/images/logLogAlgorithm.png)

## SuperLogLog

To be more specific, when collecting the values from the buckets, we can retain the 70 percent smallest values and discarding the rest for averaging. By doing so, the accuracy is improved from 1.3/√m to 1.05/√m.

![SuperLogLog Algorithm](/images/superLogLogAlgorithm.png)

## HyperLogLog

[Harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean).

![Harmonic mean](/images/harmonicMean.png)

[Paper Link](https://dmtcs.episciences.org/3545/pdf).

![HyperLogLog](/images/hyperLogLogAlgorithm.png)

## HyperLogLog++

[Paper Link](https://research.google/pubs/pub40671/).
