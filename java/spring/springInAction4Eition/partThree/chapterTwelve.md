# 使用 NoSQL 数据库

- 为 MongoDB 和 Neo4j 编写 Repository；
- 为多种数据存储形式持久化数据；
- 组合使用 Spring 和 Redis。

## 使用 MongoDB 持久化文档数据

Spring Data MongoDB 提供了三种方式在 Spring 应用中使用 MongoDB：

- 通过注解实现对象-文档映射；
- 使用 MongoTemplate 实现基于模板的数据库访问；
- 自动化的运行时 Repository 生成功能。

### 启用 MongoDB

TODO

### 为模型添加注解，实现 MongoDB 持久化

将 Java 类型映射为 MongoDB 文档的注解：

| 注解 | 描述 |
| ------ | ------ |
| @Document | 标示映射到 MongoDB 文档上的领域对象 |
| @Id | 标示某个域为ID域 |
| @DbRef | 标示某个域要引用其他的文档，这个文档有可能位于另外一个数据库中 |
| @Field | 为文档域指定自定义的元数据 |
| @Version | 标示某个属性用作版本域 |

- Order 类添加了 `@Document` 注解，这样它就能够借助 MongoTemplate 或自动生成的 Repository 进行持久化；
- 其 id 属性上使用了 `@Id` 注解，用来指定它作为文档的 ID；
- 除非将属性设置为瞬时态（transient）的，否则 Java 对象中所有的域都会持久化为文档中的域；
- 如果我们不使用 `@Field` 注解进行设置的话，那么文档域中的名字将会与对应的 Java 属性相同。

### 使用 MongoTemplate 访问 MongoDB

- count()；
- save()；
- findById()；
- Query 对象和 Criteria 对象；
- remove()；

### 编写 MongoDB Repository

`@Query` 注解可以为 Repository 方法指定自定义的查询，接受一个 JSON 查询。
`@Query` 中给定的 JSON 将会与所有的 Order 文档进行匹配，并返回匹配的文档。需要注意的是，type 属性映射成了 “?0”，这表明 type 属性应该与查询方法的第零个参数相等。如果有多个参数的话，它们可以通过 “?1”、“?2” 等方式进行引用。

## 使用 Neo4j 操作图数据

TODO

## 使用 Redis 操作 key-value 数据

TODO
