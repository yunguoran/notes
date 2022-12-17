# SQL

## Elementary Knowledge

[SQL Reference](https://spark.apache.org/docs/latest/sql-ref.html)

## Summaries

- 对日期字段进行 ORDER BY，null 值将会排在正常日期之前。
- max() 和 min() 可以用在 boolean 类型的字段上，因为 true 可以强转为 integer 类型的 1，false 为 0。
- date 和 timestamp 类型的字段在与对应的 string 类型的字段进行比较时，spark 会自动提升 string 类型为对应的 date 或 timestamp 类型。
