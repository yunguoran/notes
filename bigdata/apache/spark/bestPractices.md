# Bast Practices

- 尽可能的将数据过滤条件下推到数据源（条件下推，filter pushdown，又叫谓词下推，predicate pushdown）以及排除不需要的字段（列裁剪，column pruning），即只拉取必需的数据做计算，而不是全部取出来再过滤，以减少网络 IO 和序列化、反序列化消耗。
- 大表 join 小表时尽量广播小表，对于直接从 MongoDB 拉取数据的场景，即把小表作为查询条件下推到大表查询中。
- 使用 MongoSamplePartitioner 拉取数据时需合理设置 pipeline：
    - 其在规划分区时，只会使用 pipeline 中的第一个 stage，如果第一个 stage 中的 `$match` 没有合理利用索引，会导致大量文档扫描；如果 `$match` 分散在多个 stage 可能会导致分区不均匀。
    - `isDeleted: false` 过滤可放在第二个 stage，因为其很有可能没有索引，而且 `isDeleted: true` 一般为少数，放在第一个 stage 会导致规划分区时就把大部分文档扫了一遍。
    - 所有表会有 `{ accountId: 1, _id: 1 }` 索引，使用 `accountId` 可高效过滤文档。
- 拼接 MongoDB pipeline 时，推荐使用 `org.bson.Document`，它与 `org.bson.BsonDocument` 的区别在于：
    - `BsonDocument` 更偏向底层，对类型太过严格，它实现的是 `Map<String, BsonValue>` 接口，需要所有的类型都显示转化成 `BsonValue`，业务代码会变得复杂。
    - `Document` 对类型的要求宽泛一些，它实现的是 `Map<String, Object>` 接口，不限制类型，写起来更容易，需要注意的是如果使用了 MongoDB 不支持的类型会在运行时报错。
    - `Document` 与 spring 的 `Criteria` 转化更容易，方便 Spark 与 Spring 的业务共用拼接条件逻辑。
- 合理使用 mapPartition、foreachPartition 减少遍历开销。
- 小数据量实时计算时可调整 `spark.sql.shuffle.partitions` 减少 task 数量，以降低调度开销、提高处理速度。
- 重复使用的数据要缓存，避免从数据源反复拉取。
