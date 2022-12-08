# 高级装配

- Spring profile
- 条件化的 bean 声明
- 自动装配与歧义性
- bean 的作用域
- Spring表达式语言

## 环境与 profile

我们必须要有一种方法来配置 DataSource，使其在每种环境下都会选择最为合适的配置。

### 配置 profile bean

- 使用 `@Profile` 注解指定某个 bean 属于哪一个 profile。
- `@Profile` 注解指定某个 bean 属于哪一个 profile。`@Profile("dev")` 注解应用在了类级别上时。它会告诉 Spring 这个配置类中的 bean 只有在 dev profile 激活时才会创建。如果 dev profile 没有激活的话，那么带有 `@Bean` 注解的方法都会被忽略掉。

- 从 Spring 3.2 开始，可以在方法级别上使用 `@Profile` 注解，与 `@Bean` 注解一同使用。这样的话，就能将这两个 bean 的声明放到同一个配置类之中。
- 没有指定 profile 的 bean 始终都会被创建，与激活哪个 profile 没有关系。
- `<beans>` 元素中可以嵌套定义 `<beans>` 元素，这能够将所有的 profile bean 定义放到同一个 XML 文件中。

### 激活 profile

Spring 在确定哪个 profile 处于激活状态时，需要依赖两个独立的属性：`spring.profiles.active` 和 `spring.profiles.default`。profile 使用的都是复数形式。这意味着你可以同时激活多个 profile，这可以通过列出多个 profile 名称，并以逗号分隔来实现。

有多种方式来设置这两个属性：

- 作为 DispatcherServlet 的初始化参数。
- 作为 Web 应用的上下文参数。
- 作为 JNDI 条目。
- 作为环境变量。
- 作为 JVM 的系统属性。
- 在集成测试类上，使用 `@ActiveProfiles` 注解设置。

## 条件化的 bean

Spring 4 引入了一个新的 `@Conditional` 注解，它可以用到带有 `@Bean` 注解的方法上。如果给定的条件计算结果为 true，就会创建这个bean，否则的话，这个 bean 会被忽略。`@Conditional` 中给定了一个 Class，它指明了条件。`@Conditional` 将会通过 Condition 接口进行条件对比。

```java
public interface Condition {
  boolean matches(ConditionContext ctxt, AnnotatedTypeMetadata metadata);
}
```

matches() 方法会得到 ConditionContext 和 AnnotatedTypeMetadata 对象用来做出决策。

```java
public interface ConditionContext {
  BeanDefinitionRegistry getRegistry();
  ConfigurationListableBeanFactory getBeanFactory();
  Environment getEnvironment();
  ResourceLoader getResourceLoader();
  ClassLoader getClassLoader();
}
```

通过 ConditionContext，我们可以做到如下几点：

- 借助 getRegistry() 返回的 BeanDefinitionRegistry 检查 bean 定义。
- 借助 getBeanFactory() 返回的 ConfigurableListableBeanFactory 检查 bean 是否存在，甚至探查 bean 的属性。
- 借助 getEnvironment() 返回的 Environment 检查环境变量是否存在以及它的值是什么。
- 读取并探查 getResourceLoader() 返回的 ResourceLoader 所加载的资源。
- 借助 getClassLoader() 返回的 ClassLoader 加载并检查类是否存在。

```java
public interface AnnotatedTypeMetadata {
  boolean isAnnotated(String annotationType);
  Map<String, Object> getAnnotationAttributes(String annotationType);
  Map<String, Object> getAnnotationAttributes(String annotationType, boolean classValuesAsString);
  MultiValueMap<String, Object> getAllAnnotationAttributes(String annotationType);
  MultiValueMap<String, Object> getAllAnnotationAttributes(String annotationType, boolean classValuesAsString);
}
```

AnnotatedTypeMetadata 则能够让我们检查带有 `@Bean` 注解的方法上还有什么其他的注解。借助 isAnnotated() 方法，我们能够判断带有 `@Bean` 注解的方法是不是还有其他特定的注解。借助其他的那些方法，我们能够检查 `@Bean` 注解的方法上其他注解的属性。

`@Profile` 注解:

```java
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD})
@Documented
@Conditional({ProfileCondition.class})
public @interface Profile {
    String[] value();
}
```

`@Profile` 本身也使用了 `@Conditional` 注解，并且引用 ProfileCondition 作为 Condition 实现。如下所示，ProfileCondition 实现了 Condition 接口，并且在做出决策的过程中，考虑到了 ConditionContext 和 AnnotatedType-Metadata 中的多个因素。

```java
class ProfileCondition implements Condition {

  @Override
  public boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata) {
    if (context.getEnvironment() != null) {
      MultiValueMap<String, Object> attrs = metadata.getAllAnnotationAttributes(Profile.class.getName());
      if (attrs != null) {
        for (Object value : attrs.get("value")) {
          if (context.getEnvironment().acceptsProfiles(((String[]) value))) {
            return true;
          }
        }
        return false;
      }
    }
    return true;
  }

}
```

## 处理自动装配的歧义性

自动装配具有歧义性时，Spring 会抛出 `NoUniqueBeanDefinitionException`。

### 标示首选的 bean

`@Primary` 能够与 `@Component` 组合用在组件扫描的 bean 上，也可以与 `@Bean` 组合用在 Java 配置的 bean 声明中。

### 限定自动装配的 bean

```java
@Autowired
@Qualifier("iceCream")
public void setDessert(Dessert dessert) {
  this.dessert = dessert;
}
```

创建自定义的限定符注解:

```java
@Target({ElementType.CONSTRUCTOR, ElementType.FIELD,
         ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Qualifier
public @interface Cold { }
```

## bean 的作用域

在默认情况下，Spring 应用上下文中所有 bean 都是作为以单例（singleton）的形式创建的。也就是说，不管给定的一个 bean 被注入到其他 bean 多少次，每次所注入的都是同一个实例。
有时候，可能会发现，你所使用的类是易变的（mutable），它们会保持一些状态，因此重用是不安全的。在这种情况下，将 class 声明为单例的 bean 就不是什么好主意了，因为对象会被污染，稍后重用的时候会出现意想不到的问题。

Spring 定义了多种作用域，可以基于这些作用域创建 bean，包括：

- 单例（Singleton）：在整个应用中，只创建 bean 的一个实例。
- 原型（Prototype）：每次注入或者通过 Spring 应用上下文获取的时候，都会创建一个新的 bean 实例。
- 会话（Session）：在 Web 应用中，为每个会话创建一个 bean 实例。
- 请求（Request）：在 Web 应用中，为每个请求创建一个 bean 实例。

如果选择其他的作用域，要使用 `@Scope` 注解，它可以与 `@Component` 或 `@Bean` 一起使用。

```java
@Bean
@Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)
public Notepad notepad() {
  return new Notepad();
}
```

### 使用会话和请求作用域

在典型的电子商务应用中，可能会有一个 bean 代表用户的购物车。如果购物车是单例的话，那么将会导致所有的用户都会向同一个购物车中添加商品。另一方面，如果购物车是原型作用域的，那么在应用中某一个地方往购物车中添加商品，在应用的另外一个地方可能就不可用了，因为在这里注入的是另外一个原型作用域的购物车。

```java
@Component
@Scope(value=WebApplicationContext.SCOPE_SESSION,
       proxyMode=ScopedProxyMode.INTERFACES)
public ShoppingCart cart() { ... }
```

```java
@Component
public class StoreService {
  @Autowired
  public void setShoppingCart(ShoppingCart shoppingCart) {
    this.shoppingCart = shoppingCart;
  }
}
```

- 因为 StoreService 是一个单例的 bean，会在 Spring 应用上下文加载的时候创建。当它创建的时候，Spring 会试图将 ShoppingCart bean 注入到 setShoppingCart() 方法中。但是 ShoppingCart bean 是会话作用域的，此时并不存在。直到某个用户进入系统，创建了会话之后，才会出现 ShoppingCart 实例。
- 系统中将会有多个 ShoppingCart 实例：每个用户一个。我们并不想让 Spring 注入某个固定的 ShoppingCart 实例到 StoreService 中。我们希望的是当 StoreService 处理购物车功能时，它所使用的 ShoppingCart 实例恰好是当前会话所对应的那一个。Spring 并不会将实际的 ShoppingCart bean 注入到 StoreService 中， Spring 会注入一个到 ShoppingCart bean 的代理。这个代理会暴露与 ShoppingCart 相同的方法，所以 StoreService 会认为它就是一个购物车。但是，当 StoreService 调用 ShoppingCart 的方法时，代理会对其进行懒解析并将调用委托给会话作用域内真正的 ShoppingCart bean。
- proxyMode 属性被设置成了 `ScopedProxyMode.INTERFACES`，这表明这个代理要实现 ShoppingCart 接口，并将调用委托给实现 bean。
- 如果 ShoppingCart 是接口而不是类的话，这是可以的（也是最为理想的代理模式）。但如果 ShoppingCart 是一个具体的类的话，Spring 就没有办法创建基于接口的代理了。此时，它必须使用 CGLib 来生成基于类的代理。所以，如果 bean 类型是具体类的话，我们必须要将 proxyMode 属性设置为 `ScopedProxyMode.TARGET_CLASS`，以此来表明要以生成目标类扩展的方式创建代理。

## 运行时值注入

有的时候，我们可能会希望避免硬编码值，而是想让这些值在运行时再确定。为了实现这些功能，Spring提供了两种在运行时求值的方式：

- 属性占位符（Property placeholder）。
- Spring 表达式语言（SpEL）。

### 注入外部的值

```java
package com.soundsystem;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;

@Configuration
@PropertySource("classpath:/com/soundsystem/app.properties")
public class ExpressiveConfig {

  @Autowired
  Environment env;

  @Bean
  public BlankDisc disc() {
    return new BlankDisc(
      env.getProperty("disc.title"),
      env.getProperty("disc.artist")
    );
  }
}
```

`@PropertySource` 引用了类路径中一个名为 app.properties 的文件。它大致会如下所示：

```text
disc.title=Sgt. Peppers Lonely Hearts Club
disc.artist=The Beatles
```

getProperty() 方法有四个重载的变种形式：

- String getProperty(String key)
- String getProperty(String key, String defaultValue)
- T getProperty(String key, Class<T> type)
- T getProperty(String key, Class<T> type, T defaultValue)

如果你在使用 getProperty() 方法的时候没有指定默认值，并且这个属性没有定义的话，获取到的值是 null。如果你希望这个属性必须要定义，那么可以使用 getRequiredProperty() 方法。如果想将属性解析为类的话，可以使用 getPropertyAsClass() 方法。

Environment 还提供了一些方法来检查哪些 profile 处于激活状态：

- String[] getActiveProfiles()：返回激活 profile 名称的数组。
- String[] getDefaultProfiles()：返回默认 profile 名称的数组。
- boolean acceptsProfiles(String... profiles)：如果 environment 支持给定 profile 的话，就返回 true。

Spring 装配中，占位符的形式为使用 ${ ... } 包装的属性名称。使用 `@Value` 注解:

```java
public BlankDisc(
  @Value("${disc.title}") String title,
  @Value("${disc.artist}") String artist) {
    this.title = title;
    this.artist = artist;
}
```

为了使用占位符，我们必须要配置一个 PropertySourcesPlaceholderConfigurer bean。

### 使用 Spring 表达式语言进行装配

[SpEL](http://itmyhome.com/spring/expressions.html) 拥有很多特性，包括：

- 使用 bean 的 ID 来引用 bean。
- 调用方法和访问对象的属性。
- 对值进行算术、关系和逻辑运算。
- 正则表达式匹配。
- 集合操作。

- SpEL 表达式要放到 `#{ ... }` 之中。
- 如果要在 SpEL 中访问类作用域的方法和常量的话，要依赖 `T()` 这个运算符：`T(java.lang.Math).PI`。
- SpEL 通过 `matches` 运算符支持表达式中的模式匹配：`#{admin.email matches '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.com'}`。
- SpEL 还提供了查询运算符 `.?[]`，它会用来对集合进行过滤，得到集合的一个子集：`#{jukebox.songs.?[artist eq 'Aerosmith']}`。
- SpEL 还提供了另外两个查询运算符：`.^[]` 和 `.$[]`，它们分别用来在集合中查询第一个匹配项和最后一个匹配项：`#{jukebox.songs.^[artist eq 'Aerosmith']}`。
- SpEL 还提供了投影运算符 `.![]`：`#{jukebox.songs.![title]}`。
