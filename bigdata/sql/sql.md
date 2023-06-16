# SQL

[Reference](https://spark.apache.org/docs/latest/sql-ref.html)

## Summaries

- 对日期字段进行 ORDER BY，null 值将会排在正常日期之前。
- max() 和 min() 可以用在 Boolean 类型的字段上，因为 true 可以强转为 Integer 类型的 1，false 为 0。
- Date 和 Timestamp 类型的字段在与对应的 String 类型的字段进行比较时，Spark 会自动提升 String 类型为对应的 Date 或 Timestamp 类型。
- Spark SQL 中使用 DISTINCT 和 GROUP BY 对数据进行去重时，所做的操作完全一致，因为物理计划是一致的。
