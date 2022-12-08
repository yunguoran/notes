# Spring 之旅

在诞生之初，创建 Spring 的主要目的是用来替代更加重量级的企业级 Java 技术，尤其是 EJB。

## 简化 Java 开发

Spring 最早由 Rod Johnson 创建，目的是为了解决企业级应用开发的复杂性。任何 Java 应用都能在简单性、可测试性和松耦合等方面从 Spring 中获益。Spring 的目标是致力于全方位的简化 Java 开发。

Spring 采取了以下 4 种关键策略去降低 Java 开发的复杂性：

- 基于 POJO 的轻量级和最小侵入性编程。
- 通过依赖注入和面向接口实现松耦合。
- 基于切面和惯例进行声明式编程。
- 通过切面和模板减少样板式代码。

### 激发 POJO 的潜能

Spring 竭力避免因自身的 API 而弄乱你的应用代码。Spring 不会强迫你实现 Spring 规范的接口或继承 Spring 规范的类，相反，在基于 Spring 构建的应用中，它的类通常没有任何痕迹表明你使用了 Spring。

### 依赖注入

依赖注入这个词已经演变成一项复杂的编程技巧或设计模式理念。在项目中应用 DI，你的代码会变得异常简单并且更容易理解和测试。

任何一个有实际意义的应用都会由两个或者更多的类组成，这些类相互之间进行协作来完成特定的业务逻辑。按照传统的做法，每个对象负责管理与自己相互协作的对象（即它所依赖的对象）的引用，这将会导致高度耦合和难以测试的代码。

耦合具有两面性。一方面，紧密耦合的代码难以测试、难以复用、难以理解，并且典型地表现出 “打地鼠” 式的 bug 特性（修复一个 bug，将会出现一个或者更多新的 bug）。另一方面，一定程度的耦合又是必须的 —— 完全没有耦合的代码什么也做不了。DI 所带来的最大收益是松耦合。

创建应用组件之间协作的行为通常称为装配（wiring）。

Spring 通过应用上下文（Application Context）装载 bean 的定义并把它们组装起来。Spring 应用上下文全权负责对象的创建和组装。Spring 自带了多种应用上下文的实现，它们之间主要的区别仅仅在于如何加载配置。

### 应用切面

DI 能够让相互协作的软件组件保持松散耦合，而面向切面编程（aspect-oriented programming，AOP）允许你把遍布应用各处的功能分离出来形成可重用的组件。面向切面编程往往被定义为促使软件系统实现关注点的分离一项技术。在整个系统内，关注点（例如日志和安全）的调用经常散布到各个模块中，而这些关注点并不是模块的核心业务。AOP 能够使这些服务模块化，并以声明的方式将它们应用到它们需要影响的组件中去。

### 使用模板消除样式代码

Spring 旨在通过模板封装来消除样板式代码。Spring 的 JdbcTemplate 使得执行数据库操作时，避免传统的 JDBC 样板代码成为了可能。

## 容纳你的 Bean

在基于 Spring 的应用中，你的应用对象生存于 Spring 容器（container） 中。Spring 容器负责创建对象，装配它们，配置它们并管理它们的整个生命周期，从生存到死亡。

### 使用应用上下文

使用 `FileSystemXmlApplicationContext` 和使用 `ClassPathXmlApplicationContext` 的区别在于：`FileSystemXmlApplicationContext` 在指定的文件系统路径下查找 xml 文件；而 `ClassPathXmlApplicationContext` 是在所有的类路径（包含 JAR 文件）下查找 xml 文件。

### bean 的生命周期

![Bean 的生命周期](/images/springBeanLifeCycle.jpg)

## 俯瞰 Spring 风景线

### Spring 模块

![Spring 模块](/images/springFrameworkModule.jpg)

Spring Boot 以 Spring 的视角致力于简化 Spring 本身。
