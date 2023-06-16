# Apache Spark

## Join Strategy

- [Join Strategies](https://faun.pub/primer-on-spark-join-strategy-134e7340f7a6)
- Join strategies execution sequence

    ![joinStrategies](/images/joinStrategies.png)

## Hints

- [Partitioning Hints](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-hints.html#partitioning-hints)
- [Join Hints](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-hints.html#join-hints)

## Performance Tuning

- [Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html#performance-tuning)
- When there are few columns, you can try to cache intermediate results to prevent **BroadcastNestedLoopJoin**
