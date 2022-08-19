# 面向切面的 Spring

在软件开发中，散布于应用中多处的功能被称为横切关注点（crosscutting concern）。通常来讲，这些横切关注点从概念上是与应用的业务逻辑相分离的（但是往往会直接嵌入到应用的业务逻辑之中）。把这些横切关注点与业务逻辑相分离正是面向切面编程（AOP）所要解决的问题。

## 什么是面向切面编程

横切关注点可以被模块化为特殊的类，这些类被称为切面（aspect）。面向切面编程两个好处：

- 现在每个关注点都集中于一个地方，而不是分散到多处代码中。
- 服务模块更简洁，因为它们只包含主要关注点（或核心功能）的代码，而次要关注点的代码被转移到切面中了。

### 定义 AOP 术语

AOP 已经形成了自己的术语。描述切面的常用术语有通知（advice）、切点（pointcut）和连接点（join point）。

![AOP Terminology](/images/aopTerminology.jpg)

**通知（Advice）**

在 AOP 术语中，切面的工作被称为通知。通知定义了切面是什么以及何时使用。除了描述切面要完成的工作，通知还解决了何时执行这个工作的问题。Spring 切面可以应用 5 种类型的通知：

- 前置通知（Before）：在目标方法被调用之前调用通知功能。
- 后置通知（After）：在目标方法完成之后调用通知，此时不会关心方法的输出是什么。
- 返回通知（After-returning）：在目标方法成功执行之后调用通知。
- 异常通知（After-throwing）：在目标方法抛出异常后调用通知。
- 环绕通知（Around）：通知包裹了被通知的方法，在被通知的方法调用之前和调用之后执行自定义的行为。

**连接点（Join point）**

连接点是在应用执行过程中能够插入切面的一个点。这个点可以是调用方法时、抛出异常时、甚至修改一个字段时。切面代码可以利用这些点插入到应用的正常流程之中，并添加新的行为。

**切点（Pointcut）**

切点的定义会匹配通知所要织入的一个或多个连接点。我们通常使用明确的类和方法名称，或是利用正则表达式定义所匹配的类和方法名称来指定这些切点。有些 AOP 框架允许我们创建动态的切点，可以根据运行时的决策（比如方法的参数值）来决定是否应用通知。

**切面（Aspect）**

切面是通知和切点的结合。通知和切点共同定义了切面的全部内容 —— 它是什么，在何时和何处完成其功能。

**引入（Introduction）**

引入允许我们向现有的类添加新方法或属性。可以在无需修改这些现有的类的情况下，让它们具有新的行为和状态。

**织入（Weaving）**

织入是把切面应用到目标对象并创建新的代理对象的过程。切面在指定的连接点被织入到目标对象中。在目标对象的生命周期里有多个点可以进行织入:

- 编译期：切面在目标类编译时被织入。这种方式需要特殊的编译器。AspectJ 的织入编译器就是以这种方式织入切面的。
- 类加载期：切面在目标类加载到 JVM 时被织入。这种方式需要特殊的类加载器（ClassLoader），它可以在目标类被引入应用之前增强该目标类的字节码。AspectJ 5 的加载时织入（load-time weaving，LTW）就支持以这种方式织入切面。
- 运行期：切面在应用运行的某个时刻被织入。**一般情况下，在织入切面时，AOP 容器会为目标对象动态地创建一个代理对象。Spring AOP 就是以这种方式织入切面的**。

### Spring 对 AOP 的支持

Spring 提供了 4 种类型的 AOP 支持：

- 基于代理的经典 Spring AOP。
- 纯 POJO 切面。
- `@AspectJ` 注解驱动的切面。
- 注入式 AspectJ 切面（适用于 Spring 各版本）。

Spring AOP 构建在动态代理基础之上，因此 Spring 对 AOP 的支持局限于方法拦截。

**Spring 通知是 Java 编写的**

- Spring 所创建的通知都是用标准的 Java 类编写的。
- 虽然 AspectJ 现在支持基于注解的切面，但 AspectJ 最初是以 Java 语言扩展的方式实现的。

**Spring 在运行时通知对象**

通过在代理类中包裹切面，Spring 在运行期把切面织入到 Spring 管理的 bean 中。代理类封装了目标类，并拦截被通知方法的调用，再把调用转发给真正的目标 bean。当代理拦截到方法调用时， 在调用目标 bean 方法之前，会执行切面逻辑。

![springAspect](/images/springAspect.jpg)

直到应用需要被代理的 bean 时，Spring 才创建代理对象。如果使用的是 ApplicationContext 的话，在 ApplicationContext 从 BeanFactory 中加载所有 bean 的时候，Spring 才会创建被代理的对象。因为 Spring 运行时才创建代理对象，所以我们不需要特殊的编译器来织入 Spring AOP 的切面。

**Spring 只支持方法级别的连接点**

因为 Spring 基于动态代理，所以 Spring 只支持方法连接点。除了方法切点，AspectJ 和 JBoss 还提供了字段和构造器接入点。Spring 缺少对字段连接点的支持，无法让我们创建细粒度的通知，例如拦截对象字段的修改。而且它不支持构造器连接点，我们就无法在 bean 创建时应用通知。

## 通过切点来选择连接点

使用 AspectJ 的切点表达式语言来定义切点。
|AspectJ 指示器 | 描 述 |
| ------ | ------ |
| arg() | 限制连接点匹配参数为指定类型的执行方法 |
| @args() | 限制连接点匹配参数由指定注解标注的执行方法 |
| execution() | 用于匹配是连接点的执行方法 |
| this() | 限制连接点匹配 AOP 代理的 bean 引用为指定类型的类 |
| target | 限制连接点匹配目标对象为指定类型的类 |
| @target() | 限制连接点匹配特定的执行对象，这些对象对应的类要具有指定类型的注解 |
| within() | 限制连接点匹配指定的类型 |
| @within() | 限制连接点匹配指定注解所标注的类型（当使用Spring AOP时，方法定义在由指定的注解所标注的类里） |
| @annotation | 限定匹配带有指定注解的连接点 |

在 Spring 中尝试使用 AspectJ 其他指示器时，将会抛出 IllegalArgumentException 异常。只有 execution 指示器是实际执行匹配的，而其他的指示器都是用来限制匹配的。这说明 execution 指示器是我们在编写切点定义时最主要使用的指示器。在此基础上，我们使用其他指示器来限制所匹配的切点。

### 编写切点

为了阐述 Spring 中的切面，我们定义一个 Performance 接口：

```java
package concert;

public interface Performance {
  public void perform();
}
```

下图展现了一个切点表达式，这个表达式能够设置当 perform() 方法执行时触发通知的调用。

![pointcutExpression](/images/pointcutExpression.jpg)

使用 execution() 指示器选择 Performance 的 perform() 方法。方法表达式以 "*" 号开始，表明了我们不关心方法返回值的类型。然后，我们指定了全限定类名和方法名。对于方法参数列表，我们使用两个点号（..）表明切点要选择任意的 perform() 方法，无论该方法的入参是什么。现在假设我们需要配置的切点仅匹配 concert 包。在此场景下，可以使用 within() 指示器来限制匹配，如下图所示：

![pointcutExpressionWithIn](/images/pointcutExpressionWthIn.jpg)

我们使用了 "&&" 操作符把 execution() 和 within() 指示器连接在一起形成与（and）关系（切点必须匹配所有的指示器）。类似地，我们可以使用 "||" 操作符来标识或（or）关系，而使用 "!" 操作符来标识非（not）操作。因为 "&" 在 XML 中有特殊含义，所以在 Spring 的 XML 配置里面描述切点时，我们可以使用 and 来代替 "&&"。同样，or 和 not 可以分别用来代替 "||" 和 "!"。

### 在切点中选择 bean

Spring 还引入了一个新的 bean() 指示器，它允许我们在切点表达式中使用 bean 的 ID 来标识 bean。bean() 使用 bean ID 或 bean 名称作为参数来限制切点只匹配特定的 bean。
例如，考虑如下的切点：

```java
execution(*concert.Performance.perform()) and bean('woodstock')
```

在这里，我们希望在执行 Performance 的 perform() 方法时应用通知，但限定 bean 的 ID 为 woodstock。
在某些场景下，限定切点为指定的 bean 或许很有意义，但我们还可以使用非操作为除了特定 ID 以外的其他 bean 应用通知：

```java
execution(* concert.Performance.perform()) and !bean('woodstock')
```

在此场景下，切面的通知会被编织到所有 ID 不为 woodstock 的 bean 中。

## 使用注解创建切面

使用注解来创建切面是 AspectJ 5 所引入的关键特性。

### 定义切面

```java
package concert;

import org.aspect.lang.annotation.AfterReturning;
import org.aspect.lang.annotation.AfterThrowing;
import org.aspect.lang.annotation.Aspect;
import org.aspect.lang.annotation.Before;

@Aspect
public class Audience {

  @Before("execution(** concert.Performance.perform(..))")
  public void silenceCellPhones() {
    System.out.println("Silencing cell phones");
  }

  @Before("execution(** concert.Performance.perform(..))")
  public void takeSeats() {
    System.out.println("Taking seats");
  }

  @AfterReturning("execution(** concert.Performance.perform(..))")
  public void applause() {
    System.out.println("CLAP CLAP CLAP!!!");
  }

  @AfterThrowing("execution(** concert.Performance.perform(..))")
  public void demandRefund() {
    System.out.println("Demanding a refund");
  }
}
```

Audience 类使用 `@AspectJ` 注解进行了标注，该注解表明 Audience 是一个切面。AspectJ 提供了五个注解来定义通知:

| 注解 | 通知 |
| ------ | ------ |
| @After | 通知方法会在目标方法返回或抛出异常后调用 |
| @AfterReturning | 通知方法会在目标方法返回后调用 |
| @AfterThrowing | 通知方法会在目标方法抛出异常后调用 |
| @Around | 通知方法会将目标方法封装起来 |
| @Before | 通知方法会在目标方法调用之前执行 |

相同的切点表达式我们重复了四遍，这样的重复让人感觉有些不对劲。如果我们只定义这个切点一次，然后每次需要的时候引用它，那么这会是一个很好的方案。`@Pointcut` 注解能够在一个 `@AspectJ` 切面内定义可重用的切点。

```java
package concert;

import org.aspect.lang.annotation.AfterReturning;
import org.aspect.lang.annotation.AfterThrowing;
import org.aspect.lang.annotation.Aspect;
import org.aspect.lang.annotation.Before;
import org.aspect.lang.annotation.Pointcut;

@Aspect
public class Audience {

  @Pointcut("execution(** concert.Performance.perform(..))")
  public void performance() { }

  @Before("performance()")
  public void silenceCellPhones() {
    System.out.println("Silencing cell phones");
  }

  @Before("performance()")
  public void takeSeats() {
    System.out.println("Taking seats");
  }

  @AfterReturning("performance()")
  public void applause() {
    System.out.println("CLAP CLAP CLAP!!!");
  }

  @AfterThrowing("performance()")
  public void demandRefund() {
    System.out.println("Demanding a refund");
  }
}
```

performance() 方法的实际内容并不重要，在这里它实际上应该是空的。其实该方法本身只是一个标识，供 `@Pointcut` 注解依附。

Audience 只是一个 Java 类，只不过它通过注解表明会作为切面使用而已。像其他的 Java 类一样，它可以装配为 Spring 中的 bean：

```java
@Bean
public Audience audience() {
  return new Audience();
}
```

**如果你就此止步的话，Audience 只会是 Spring 容器中的一个 bean。即便使用了 `@AspectJ` 注解，但它并不会被视为切面，这些注解不会解析，也不会创建将其转换为切面的代理。**

如果你使用 JavaConfig 的话，可以在配置类的类级别上通过使用 `@EnableAspectJAutoProxy` 注解启用自动代理功能。

```java
package concert;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Component;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
@EnableAspectJAutoProxy
@Component
public class ConcertConfig {

  @Bean
  public Audience audience() {
    return new Audience();
  }
}
```

假如你在 Spring 中要使用 XML 来装配 bean 的话，那么需要使用 Spring aop 命名空间中的 `<aop:aspectj-autoproxy>` 元素。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:context="http://www.springframework.org/schema/context"
  xmlns:context="http://www.springframework.org/schema/aop" <!-- 声明 Spring 的 aop 命名空间 -->
  xsi:schemaLocation="
    http://www.springframework.org/schema/aop
    http://www.springframework.org/schema/aop/spring-aop.xsd
    http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd" >

  <context:component-scan base-package="context" />

  <aop:aspectj-autoproxy /> <!-- 启用 AspectJ 自动代理 -->

  <bean class="concert.Audience" /> <!-- 声明 Audience bean -->

</beans>
```

不管是使用 JavaConfig 还是 XML，AspectJ 自动代理都会为使用 `@Aspect` 注解的 bean 创建一个代理，这个代理会围绕着所有该切面的切点所匹配的 bean。在这种情况下，将会为 Concert bean 创建一个代理，Audience 类中的通知方法将会在 perform() 调用前后执行。

Spring 的 AspectJ 自动代理仅仅使用 `@AspectJ` 作为创建切面的指导，切面依然是基于代理的。在本质上，它依然是 Spring 基于代理的切面。这一点非常重要，因为这意味着尽管使用的是 `@AspectJ` 注解，但我们仍然限于代理方法的调用。如果想利用 AspectJ 的所有能力，我们必须在运行时使用 AspectJ 并且不依赖 Spring 来创建基于代理的切面。

### 创建环绕通知

环绕通知是最为强大的通知类型。它能够让你所编写的逻辑将被通知的目标方法完全包装起来。实际上就像在一个通知方法中同时编写前置通知和后置通知。这次我们使用一个环绕通知来代替之前多个不同的前置通知和后置通知。

```java
package concert;

import org.aspect.lang.annotation.ProceedingJoinPoint;
import org.aspect.lang.annotation.Around;
import org.aspect.lang.annotation.Aspect;
import org.aspect.lang.annotation.Pointcut;

@Aspect
public class Audience {

  @Pointcut("execution(** concert.Performance.perform(..))")
  public void performce() { }

  @Around("performance()")
  public void watchPerformance(ProceedingJoinPoint jp) {
    try {
      System.out.println("Silencing cell phones");
      System.out.println("Taking seats");
      jp.proceed();
      System.out.println("CLAP CLAP CLAP!!!");
    } catch (Throwable e) {
      System.out.println("Demanding a refund");
    }
  }
}
```

`@Around` 注解表明 watchPerformance() 方法会作为 performance() 切点的环绕通知。这个通知所达到的效果与之前的前置通知和后置通知是一样的。但是，现在它们位于同一个方法中，不像之前那样分散在四个不同的通知方法里面。

新的通知方法接受 ProceedingJoinPoint 作为参数。这个对象是必须要有的，因为要在通知中通过它来调用被通知的方法。通知方法中可以做任何的事情，当要将控制权交给被通知的方法时，它需要调用 ProceedingJoinPoint 的 proceed() 方法。

需要注意的是，别忘记调用 proceed() 方法。如果不调这个方法的话，那么你的通知实际上会阻塞对被通知方法的调用。有可能这就是你想要的效果，但更多的情况是你希望在某个点上执行被通知的方法。

你可以不调用 proceed() 方法，从而阻塞对被通知方法的访问，与之类似，你也可以在通知中对它进行多次调用。要这样做的一个场景就是实现重试逻辑，也就是在被通知方法失败后，进行重复尝试。

### 处理通知中的参数

如果切面所通知的方法确实有参数该怎么办呢？切面能访问和使用传递给被通知方法的参数吗？

```java
package soundsystem;

import java.util.HashMap;
import java.util.Map;
import org.aspect.lang.annotation.Aspect;
import org.aspect.lang.annotation.Before;
import org.aspect.lang.annotation.Pointcut;

@Aspect
public class TrackCounter {

  private Map<Integer, Integer> trackCounts = new HashMap<>();

  @Pointcut("execution(* soundsystem.CompactDisc.playTrack(int) && args(trackNumber)")
  public void trackPlayed(int trackNumber) { }

  @Before("trackPlayed(trackNumber)")
  public void countTrack(int trackNumber) {
    int currentCount = getPlayCount(trackNumber);
    trackCounts.put(trackNumber, currentCount + 1);
  }

  public int getPlayCount(int trackNumber) {
    return trackCounts.containsKey(trackNumber) ? trackCounts.get(trackNumber) : 0;
  }
}
```

这个切面使用 `@Pointcut` 注解定义命名的切点，并使用 `@Before` 将一个方法声明为前置通知。这里的不同点在于切点还声明了要提供给通知方法的参数。

![pointcut parameter](/images/pointcutParameter.jpg)

切点表达式中的 `args(trackNumber)` 限定符表明传递给 playTrack() 方法的 int 类型参数也会传递到通知中去。参数的名称 trackNumber 也与切点方法签名中的参数相匹配。这个参数会传递到通知方法中，这个通知方法是通过 `@Before` 注解和命名切点 trackPlayed(trackNumber) 定义的。切点定义中的参数与切点方法中的参数名称是一样的，这样就完成了从命名切点到通知方法的参数转移。

### 通过注解引入新功能

利用被称为**引入**的 AOP 概念，切面可以为 Spring bean 添加新方法。当引入接口的方法被调用时，代理会把此调用委托给实现了新接口的某个其他对象。实际上，一个 bean 的实现被拆分到了多个类中。

Encoreable 接口：

```java
package concert;

public interface Encoreable {
  void performEncore();
}
```

我们需要有一种方式将这个接口应用到 Performance 实现中。我们现在假设你能够访问 Performance 的所有实现，并对其进行修改，让它们都实现 Encoreable 接口。但是，从设计的角度来看，这并不是最好的做法，并不是所有的 Performance 都是具有 Encoreable 特性的。另外一方面，有可能无法修改所有的 Performance 实现，当使用第三方实现并且没有源码的时候更是如此。但借助于 AOP 的引入功能，我们可以不必在设计上妥协或者侵入性地改变现有的实现。

```java
package concert;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.DeclareParents;

@Aspect
public class EncoreableIntroducer {

  @DeclareParents(value="concert.Performance+", defaultImpl=DefaultEncoreable.class)
  public static Encoreable encoreable;
}
```

EncoreableIntroducer 是一个切面。它通过 `@DeclareParents` 注解，将 Encoreable 接口引入到 Performance bean 中。

`@DeclareParents` 注解由三部分组成：

- `value` 属性指定了哪种类型的 bean 要引入该接口。在本例中是所有实现 Performance 的类型。（标记符后面的加号表示是 Performance 的所有子类型，而不是 Performance 本身。）
- `defaultImpl` 属性指定了为引入功能提供实现的类。在这里我们指定的是 DefaultEncoreable 提供实现。
- `@DeclareParents` 注解所标注的静态属性指明了要引入了接口。在这里我们所引入的是 Encoreable 接口。

## 在 XML 中声明切面

基于 Java 的配置要优于基于 XML 的配置。但是如果你需要声明切面，但是又不能为通知类添加注解的时候，那么就必须转向 XML 配置了。

| AOP 配置元素 | 用途 |
| ------ | ------ |
| <aop:advisor> | 定义 AOP 通知器 |
| <aop:after> | 定义 AOP 后置通知（不管被通知的方法是否执行成功） |
| <aop:after-returning> | 定义 AOP 返回通知 |
| <aop:after-throwing> | 定义 AOP 异常通知 |
| <aop:around> | 定义 AOP 环绕通知 |
| <aop:aspect> | 定义一个切面 |
| <aop:aspectj-autoproxy> | 启用 @AspectJ 注解驱动的切面 |
| <aop:before> | 定义一个 AOP 前置通知 |
| <aop:config> | 顶层的 AOP 配置元素。大多数的元素必须包含在元素内 |
| <aop:declare-parents> | 以透明的方式为被通知的对象引入额外的接口 |
| <aop:pointcut> | 定义一个切点 |

```java
package concert;

public class Audience {

  public void silenceCellPhones() {
    System.out.println("Silencing cell phones");
  }

  public void takeSeats() {
    System.out.println("Taking seats");
  }

  public void applause() {
    System.out.println("CLAP CLAP CLAP!!!");
  }

  public void demandRefund() {
    System.out.println("Demanding a refund");
  }
}
```

### 声明前置和后置通知

```xml
<aop:config>
  <aop:aspect ref="audience">

    <aop:before
      pointcut="execution(** concert.Performance.perform(..))"
      method="silenceCellPhones" />

    <aop:before
      pointcut="execution(** concert.Performance.perform(..))"
      method="takeSeats" />

    <aop:after-returning
      pointcut="execution(** concert.Performance.perform(..))"
      method="applause" />

    <aop:after-throwing
      pointcut="execution(** concert.Performance.perform(..))"
      method="demandRefund" />

  </aop:aspect>
</aop:config>
```

大多数的 AOP 配置元素必须在 `<aop:config>` 元素的上下文内使用。这条规则有几种例外场景，但是把 bean 声明为一个切面时，我们总是从 `<aop:config>` 元素开始配置的。

所有通知元素中的 pointcut 属性的值都是一样的，这是因为所有的通知都要应用到相同的切点上。在基于 AspectJ 注解的通知中，当发现这种类型的重复时，我们使用 `@Pointcut` 注解消除了这些重复的内容。而在基于 XML 的切面声明中，我们需要使用元素。如下的 XML 展现了如何将通用的切点表达式抽取到一个切点声明中，这样这个声明就能在所有的通知元素中使用了。

```xml
<aop:config>
  <aop:aspect ref="audience">
    <aop:pointcut
      id="performance"
      expressions="execution(** concert.Performance.perform(..))" />

    <aop:before
      pointcut-ref="performance"
      method="silenceCellPhones" />

    <aop:before
      pointcut-ref="performance"
      method="takeSeats" />

    <aop:after-returning
      pointcut-ref="performance"
      method="applause" />

    <aop:after-throwing
      pointcut-ref="performance"
      method="demandRefund" />

  </aop:aspect>
</aop:config>
```

`<aop:pointcut>` 元素所定义的切点可以被同一个 `<aop:aspect>` 元素之内的所有通知元素引用。如果想让定义的切点能够在多个切面使用，我们可以把 `<aop:pointcut>` 元素放在 `<aop:config>` 元素的范围内。

### 声明环绕通知

```java
package concert;

import org.aspectj.lang.ProceedingJoinPoint;

public class Audience {

  public void watchPerformance(ProceedingJoinPoint jp) {
    try {
      System.out.println("Silencing cell phones");
      System.out.println("Taking seats");
      jp.proceed();
      System.out.println("CLAP CLAP CLAP!!!");
    } catch (Throwable e) {
      System.out.println("Demanding a refund");
    }
  }
}
```

```xml
<aop:config>
  <aop:aspect ref="audience">
    <aop:pointcut
      id="performance"
      expression="execution(** concert.Performance.perform(..))" />

    <aop:around
      pointcut-ref="performance"
      method="watchPerformance" />

  </aop:aspect>
</aop:config>
```

### 为通知传递参数

```java
package soundsystem;

import java.util.HashMap;
import java.util.Map;

public class TrackCounter {

  private Map<Integer, Integer> trackCounts = new HashMap<>();

  public void trackPlayed(int trackNumber) { }

  public void countTrack(int trackNumber) {
    int currentCount = getPlayCount(trackNumber);
    trackCounts.put(trackNumber, currentCount + 1);
  }

  public int getPlayCount(int trackNumber) {
    return trackCounts.containsKey(trackNumber) ? trackCounts.get(trackNumber) : 0;
  }
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:aop="http://www.springframework.org/schema/aop"
  xmlns:util="http://www.springframework.org/schema/util"
  xsi:schemaLocation="
    http://www.springframework.org/schema/aop
    http://www.springframework.org/schema/aop/spring-aop.xsd
    http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd" >

  <bean id="trackCounter" class="soundsystem.TrackCounter" />

  <bean id="cd" class="soundsystem.BlackDisc" >
    <property name="title" value="Sgt. Pepper's Lonelt Hearts Club Band" />
    <property name="artist" value="The Beatles" />
    <property name="tracks" >
      <list>
        <value>Sgt. Pepper's Lonely Hearts Club Band</value>
        <value>Lucy in the Sky with Diamonds</value>
        <value>Getting Better</value>
        <value>Fixing a Hole</value>
        <!-- ...other tracks omitted for brevity... -->
      </list>
    </property>
  </bean>

  <aop:config>
    <aop:aspect ref="trackCounter">
      <aop:pointcut
        id="trackPlayed"
        expression="execution(* soundsystem.CompactDisc.playTrack(int)) and args(trackNumber)" />

      <aop:before pointcut-ref="trackPlayed" method="countTrack" />
    </aop:aspect>
  </aop:config>

</beans>
```

### 通过切面引入新的功能

```xml
<aop:aspect>
  <aop:delate-parents
    types-matching="concert.Performance+"
    implement-interface="concert.Encoreable"
    default-impl="concert.DefaultEncoreable" />
</aop:aspect>
```

这里有两种方式标识所引入接口的实现。在本例中，我们使用 `default-impl` 属性用全限定类名来显式指定 Encoreable 的实现。或者，我们还可以使用 `delegate-ref` 属性来标识。

```xml
<aop:aspect>
  <aop:delate-parents
    types-matching="concert.Performance+"
    implement-interface="concert.Encoreable"
    delegate-ref="encoreableDelegate" />
</aop:aspect>
```

使用 `default-impl` 来直接标识委托和间接使用 `delegate-ref` 的区别在于后者是 Spring bean，它本身可以被注入、通知或使用其他的 Spring 配置。

### 注入 AspectJ 切面

AspectJ 切面根本不需要 Spring 就可以织入到我们的应用中。
