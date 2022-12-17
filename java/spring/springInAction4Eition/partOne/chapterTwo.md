# 装配 Bean

在 Spring 中，对象无需自己查找或创建与其所关联的其他对象。相反，容器负责把需要相互协作的对象引用赋予各个对象。创建应用对象之间协作关系的行为通常称为装配（wiring），这也是依赖注入（DI）的本质。

## Spring 配置的可选方案

Spring 提供了三种主要的装配机制：

- 在 XML 中进行显式配置。
- 在 Java 中进行显式配置。
- 隐式的 bean 发现机制和自动装配。

尽可能使用自动配置的机制，显式配置越少越好。

## 自动化装配 bean

Spring 从两个角度来实现自动化装配：

- 组件扫描（component scanning）：Spring 会自动发现应用上下文中所创建的 bean。
- 自动装配（autowiring）：Spring 自动满足 bean 之间的依赖。

### 创建可被发现的 bean

`@Component` 注解表明该类会作为组件类，并告知 Spring 要为这个类创建 bean。组件扫描默认是不启用的。我们还需要显式配置一下 Spring，从而命令它去寻找带有 `@Component` 注解的类，并为其创建 bean。`@ComponentScan` 默认会扫描与配置类相同的包。因此 Spring 将会扫描这个包以及这个包下的所有子包，查找带有 `@Component` 注解的类。这样的话，就能发现带有 `@Component` 注解的类，并且会在 Spring 中自动为其创建一个 bean。

### 为组件扫描的 bean 命名

- `@Component("lonelyHeartsClub")`
- Spring 支持将 `@Named` 作为 `@Component` 注解的替代方案。

### 设置组件扫描的基础包

- `@ComponentScan("soundsystem")`
- `@ComponentScan(basePackages="soundsystem")`
- `@ComponentScan(basePackages={"soundsystem", "video"})`

在上面的例子中，所设置的基础包是以 String 类型表示的。这种方法是类型不安全（not type-safe）的。如果重构代码的话，那么所指定的基础包可能就会出现错误了。除了将包设置为简单的 String 类型之外，`@ComponentScan` 还提供了另外一种方法，那就是将其指定为包中所包含的类或接口：

- `@ComponentScan(basePackageClasses={CDPlayer.class, DVDPlayer.class})`

basePackages 属性被替换成了 basePackageClasses。同时不再使用 String 类型的名称来指定包，而是为 basePackageClasses 属性所设置的数组中包含了类。这些类所在的包将会作为组件扫描的基础包。

### 通过为 bean 添加注解实现自动装配

- `@Autowired` 注解可以用在类的任何方法上，包括构造器。
- 不管是构造器、Setter 方法还是其他的方法，Spring 都会尝试满足方法参数上所声明的依赖。假如有且只有一个 bean 匹配依赖需求的话，那么这个 bean 将会被装配进来。如果没有匹配的 bean，那么在应用上下文创建的时候，Spring 会抛出 一个异常。为了避免异常的出现，你可以将 @Autowired 的 required 属性设置为 false：`@Autowired(required=false)`，但需警惕空指针异常。
- 如果有多个 bean 都能满足依赖关系的话，Spring 将会抛出一个异常，表明没有明确指定要选择哪个 bean 进行自动装配。

## 通过 Java 代码装配 bean

在你想要将第三方库中的组件装配到你的应用中，在这种情况下，是没有办法在它的类上添加 `@Component` 和 `@Autowired` 注解的，因此就不能使用自动化装配的方案了。此时需要通过 JavaConfig 显式配置 Spring。在进行显式配置时，JavaConfig 是更好的方案， 因为它更为强大、类型安全并且对重构友好。因为它就是 Java 代码， 就像应用程序中的其他 Java 代码一样。

### 创建配置类

创建 JavaConfig 类的关键在于为其添加 `@Configuration` 注解，`@Configuration` 注解表明这个类是一个配置类，该类应该包含在 Spring 应用上下文中如何创建 bean 的细节。

### 声明简单的 bean

要在 JavaConfig 中声明 bean，我们需要编写一个方法，这个方法会创建所需类型的实例，然后给这个方法添加 `@Bean` 注解。`@Bean` 注解会告诉 Spring 这个方法将会返回一个对象，该对象要注册为 Spring 应用上下文中的 bean。方法体中包含了最终产生 bean 实例的逻辑。

### 借助 JavaConfig 实现注入

- 在 JavaConfig 中装配 bean 的最简单方式就是引用创建 bean 的方法。
- 通过调用方法来引用 bean 的方式有点令人困惑。其实还有一种理解起来更为简单的方式：

```java
@Bean
public CDPlayer cdPlayer(CompactDisc compactDisc) {
  return new CDPlayer(compactDisc);
}
```

在这里，cdPlayer() 方法请求一个 CompactDisc 作为参数。当 Spring 调用 cdPlayer() 创建 CDPlayer bean 的时候，它会自动装配一个 CompactDisc 到配置方法之中。然后，方法体就可以按照合适的方式来使用它。借助这种技术，cdPlayer() 方法也能够将 CompactDisc 注入到 CDPlayer 的构造器中，而且不用明确引用 CompactDisc 的 `@Bean` 方法。其实不管 CompactDisc 是采用什么方式创建出来的，Spring 都会将其传入到配置方法中，并用来创建 CDPlayer bean。

带有 `@Bean` 注解的方法可以采用任何必要的 Java 功能来产生 bean 实例。

## 通过 XML 装配 bean

### 创建 XML 配置规范

创建 XML 配置文件创建和管理 Spring XML 配置文件的一种简便方式是使用 [Spring Tool Suite](https://spring.io/tools/sts) 。在 Spring Tool Suite 的菜单中， 选择 File>New>Spring Bean Configuration File，能够创建 Spring XML 配置文件，并且可以选择可用的配置命名空间。

### 声明一个简单的 <bean>

```xml
<bean class="soundsystem.SgtPeppers" />
```

因为没有明确给定 ID，所以这个 bean 将会根据全限定类名来进行命名。在本例中，bean 的 ID 将会是 “soundsystem.SgtPeppers#0”。其中，“#0” 是一个计数的形式，用来区分相同类型的其他 bean。如果你声明了另外一个 SgtPeppers，并且没有明确进行标识，那么它自动得到的 ID 将会是 “soundsystem.SgtPeppers#1”。
尽管自动化的 bean 命名方式非常方便，但如果你要稍后引用它的话，那自动产生的名字就没有多大的用处了。因此，通常来讲更好的办法是借助 id 属性，为每个 bean 设置一个你自己选择的名字：

```xml
<bean id="compactDisc" class="soundsystem.SgtPeppers" />
```

第一件需要注意的事情就是你不再需要直接负责创建 SgtPeppers 的实例，在基于 JavaConfig 的配置中，我们是需要这样做的。当 Spring 发现这个元素时，它将会调用 SgtPeppers 的默认构造器来创建bean。在 JavaConfig 配置方式中，你可以通过任何可以想象到的方法来创建 bean 实例。

### 借助构造器注入初始化 bean

在 Spring XML 配置中，只有一种声明 bean 的方式：使用 <bean> 元素并指定 class 属性。Spring 会从这里获取必要的信息来创建 bean。
但是，在 XML 中声明 DI 时，会有多种可选的配置方案和风格。具体到构造器注入，有两种基本的配置方案可供选择：

- <constructor-arg> 元素
- 使用 Spring 3.0 所引入的 c- 命名空间

```xml
<bean id="cdPlayer" class="soundsystem.CDPlayer">
  <constructor-arg ref="compactDisc">
</bean>
```

要使用 `c-` 命名空间的话，必须要在 XML 的顶部声明其模式。在 `c-` 命名空间和模式声明之后，我们就可以使用它来声明构造器参数了。

```xml
<bean id="cdPlayer" class="soundsystem.CDPlayer" c:cd-ref="compactDisc" />
```

![c-namespace](/images/c-namespace.jpg)

使用参数在整个参数列表中的位置信息:

```xml
<bean id="cdPlayer" class="soundsystem.CDPlayer" c:_0-ref="compactDisc" />
```

我将参数的名称替换成了 0，也就是参数的索引。因为在 XML 中不允许数字作为属性的第一个字符，因此必须要添加一个下划线作为前缀。只有一个构造器参数时无需标示参数。

将字面量注入到构造器中：使用 value 属性，通过该属性表明给定的值要以字面量的形式注入到构造器之中。

```xml
<bean id="compactDisc" class="soundsystem.BlankDisc">
    <constructor-arg value="Sgt. Pepper's Lonely Hearts Club Band" />
    <constructor-arg value="The Beatles" />
</bean>
```

### 设置属性

对强依赖使用构造器注入，而对可选性的依赖使用属性注入。
