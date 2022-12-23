# 通过 Spring 和 JDBC 征服数据库

本章内容：

- 定义 Spring 对数据访问的支持
- 配置数据库资源
- 使用 Spring 的 JDBC 模版

## Spring 的数据访问哲学

服务对象通过接口来访问 Repository 的好处：

- 它使得服务对象易于测试，因为它们不再与特定的数据访问实现绑定在一起。
- 数据访问层是以持久化技术无关的方式来进行访问的。持久化方式的选择独立于 Repository，同时只有数据访问相关的方法才通过接口进行暴露。这可以实现灵活的设计，并且切换持久化框架对应用程序其他部分所带来的影响最小。

### 了解 Spring 的数据访问异常体系

Spring 认为触发异常的很多问题是不能在 catch 代码块中修复的。Spring 使用了非检查型异常，而不是强制开发人员编写 catch 代码块（里面经常是空的）。这把是否要捕获异常的权力留给了开发人员。

### 数据访问模板化

Spring 将数据访问过程中固定的和可变的部分明确划分为两个不同的类：模板（template）和回调（callback）。

## 配置数据源

Spring 提供了在 Spring 上下文中配置数据源 bean 的多种方式，包括：

- 通过 JDBC 驱动程序定义的数据源；
- 通过 JNDI 查找的数据源；
- 连接池的数据源。

### 使用 JNDI 数据源

配置通过 JNDI 获取数据源。JNDI 的好处在于数据源完全可以在应用程序之外进行管理，这样应用程序只需在访问数据库的时候查找数据源就可以了。

### 使用数据源连接池

数据源连接池：

- [Apache Commons DBCP](http://jakarta.apache.org/commons/dbcp)
- [c3p0](http://sourceforge.net/projects/c3p0/)
- [BoneCP](http://jolbox.com/)

| 池配置属性 | 所指定的内容 |
| ------ | ------ |
| initialSize | 池启动时创建的连接数量 |
| maxActive | 同一时间可从池中分配的最多连接数。如果设置为 0，表示无限制 |
| maxIdle | 池里不会被释放的最多空闲连接数。如果设置为 0，表示无限制 |
| maxOpenPreparedStatements | 在同一时间能够从语句池中分配的预处理语句（prepared statement）的最大数量。如果设置为 0，表示无限制 |
| maxWait | 在抛出异常之前，池等待连接回收的最大时间（当没有可用连接时）。如果设置为 -1，表示无限等待 |
| minEvictableIdleTimeMillis | 连接在池中保持空闲而不被回收的最大时间 |
| minIdle | 在不创建新连接的情况下，池中保持空闲的最小连接数 |
| poolPreparedStatements | 是否对预处理语句（prepared statement）进行池管理（布尔值） |

### 基于 JDBC 驱动的数据源

在 Spring 中，通过 JDBC 驱动定义数据源是最简单的配置方式。Spring 提供了三个这样的数据源类（均位于 org.springframework.jdbc.datasource 包中）供选择：

- DriverManagerDataSource：在每个连接请求时都会返回一个新建的连接。与 DBCP 的 BasicDataSource 不同， 由 DriverManagerDataSource 提供的连接并没有进行池化管理；
- SimpleDriverDataSource：与 DriverManagerDataSource 的工作方式类似，但是它直接使用 JDBC 驱动，来解决在特定环境下的类加载问题，这样的环境包括 OSGi 容器；
- SingleConnectionDataSource：在每个连接请求时都会返回同一个的连接。尽管 SingleConnectionDataSource 不是严格意义上的连接池数据源，但是你可以将其视为只有一个连接的池。

### 使用嵌入式的数据源

嵌入式数据库作为应用的一部分运行，而不是应用连接的独立数据库服务器。尽管在生产环境的设置中，它并没有太大的用处，但是对于开发和测试来讲，嵌入式数据库都是很好的可选方案。这是因为每次重启应用或运行测试的时候，都能够重新填充测试数据。

### 使用 profile 选择数据源

通过使用 profile 功能，会在运行时选择数据源，这取决于哪一个 profile 处于激活状态。

## 在 Spring 中使用 JDBC

使用 JDBC 能够更好地对数据访问的性能进行调优。JDBC 允许你使用数据库的所有特性，而这是其他框架不鼓励甚至禁止的。

### 应对失控的 JDBC 代码

样板代码是非常重要的。清理资源和处理错误确保了数据访问的健壮性。如果没有它们的话，就不会发现错误而且资源也会处于打开的状态，这将会导致意外的代码和资源泄露。我们不仅需要这些代码，而且还要保证它是正确的。基于这样的原因，我们才需要框架来保证这些代码只写一次而且是正确的。

### 使用 JDBC 模板

Spring 的 JDBC 框架承担了资源管理和异常处理的工作，从而简化了 JDBC 代码，让我们只需编写从数据库读写数据的必需代码。
