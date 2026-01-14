# 接口

## 抽象类和抽象方法

抽象方法是用 `abstract` 关键字修饰的方法，只有一个声明，没有方法体。

- 不能有方法体（没有 `{}`）。
- 必须被子类重写，除非子类也是抽象类。
- 不能用 `private`、`final`、`static` 修饰。

抽象类是使用 `abstract` 关键字修饰的类，可以包含抽象方法和普通方法。

- 不能被实例化。
- 可以有构造方法（用于子类初始化）。
- 可以有成员变量。
- 可以包含 0 个或多个抽象方法。
- 子类必须实现所有抽象方法，除非子类也是抽象类。

抽象类和抽象方法很有用，因为它们明确了类的抽象性，并告诉用户和编译器自己的预期用途，**抽象类还是有用的重构工具，它能让你轻松地在继承层次结构中向上移动通用方法。**

## 接口定义

接口使用 `interface` 关键字来定义。

- Java 8 中的接口允许默认方法和静态方法。
- 接口也可以包含字段，但这些字段是隐式的 `static` 和 `final`。
- 接口中的方法是 `public` 的，即使不显式声明。

接口和抽象类之间最显著的区别可能是两者的惯用方式。接口通常暗示“类的类型”或作为形容词来使用，例如 `Runnable` 或 `Serializable`。而抽象类通常是类层次结构的一部分，并且是“事物的类型”，例如 `String` 或 `Instrument`。

### 默认方法

当在接口内使用 `default` 关键字时，`default` 关键字所修饰的方法会创建一个方法体，如果实现了这个接口的类没有提供该方法的定义，就用这个方法体来代替。

可以添加默认方法的原因是它允许向现有接口中添加方法，而不会破坏已经在使用该接口的所有代码。

在 JDK 9 中接口里的 `default` 和 `static` 方法都是可以 `private` 的。

### 多重继承

Java 8 可以组合多个来源的实现，只要所有基类方法都有不同的名称和参数列表（方法签名），代码就能正常工作。发生冲突时必须重写冲突的方法（可以使用 `super` 关键字来选择一个实现）。

```java
// interfaces/Jim.java
import java.util.*;

interface Jim1 {
    default void jim() {
        System.out.println("Jim1::jim");
    }
}

interface Jim2 {
    default void jim() {
        System.out.println("Jim2::jim");
    }
}

public class sJim implements Jim1, Jim2 {
    @Override
    public void jim() {
        Jim2.super.jim();
    }

    public static void main(String[] args) {
        new Jim().jim();
    }
}
/* Output:
Jim2::jim
*/
```

### 接口中的静态方法

接口中的静态方法是属于接口本身的，只能通过“接口名.静态方法”的方式调用。

```java
// onjava/Operation.java
public interface Operation {
    void execute();

    static void runOps(Operation... ops) {
        for (Operation op : ops)
            op.execute();
    }

    static void show(String msg) {
        System.out.println(msg);
    }
}


// interfaces/MetalWork.java
class Heat implements Operation {
    @Override
    public void execute() {
        Operation.show("Heat");
    }
}

public class MetalWork {
    public static void main(String[] args) {
        Operation twist = new Operation() {
            public void execute() {
                Operation.show("Twist");
            }
        };
        Operation.runOps(
            new Heat(),                     // [1]
            new Operation() {               // [2]
                public void execute() {
                    Operation.show("Hammer");
                }
            },
            twist::execute,                 // [3]
            () -> Operation.show("Anneal")  // [4]
        );
    }
}
/* Output:
Heat
Hammer
Twist
Anneal
*/
```

`runOps` 是**模版方法**设计模式的一个例子。

此处创建 `Operation` 用了四种不同的方式:

- 常规类 `Heat`。
- 匿名类。
- 方法引用。
- Lambda 表达式。

## 抽象类与接口

| 对比维度 | 抽象类（Abstract Class） | 接口（Interface） |
|--------|------------------------|-------------------|
| 本质 | 类 | 行为规范 / 能力 |
| 是否可实例化 | 否 | 否 |
| 继承 / 实现方式 | `extends`（单继承） | `implements`（可多实现） |
| 是否支持多继承 | 否 | 是（多实现） |
| 方法类型 | 抽象方法 + 普通方法 | 抽象方法（Java 8+ 支持 `default` / `static`） |
| 方法访问修饰符 | 任意 | 默认 `public` |
| 成员变量 | 任意成员变量 | `public static final` 常量 |
| 构造方法 | 可以有 | 不可以有 |
| 状态（字段） | 可以保存状态 | 不能保存状态 |
| 设计侧重点 | 代码复用、模板设计 | 规范约束、解耦 |
| 典型使用场景 | 父类模板、公共逻辑 | 能力定义、跨模块接口 |
| 关键字 | `abstract class` | `interface` |
| 与类关系 | is-a（是什么） | can-do（能做什么） |

## 完全解耦

```java
// interfaces/Applicator.java
import java.util.*;

class Processor {
    public String name() {
        return getClass().getSimpleName();
    }

    public Object process(Object input) {
        return input;
    }
}

class Upcase extends Processor {
    @Override // Covariant return:
    public String process(Object input) {
        return ((String) input).toUpperCase();
    }
}

class Downcase extends Processor {
    @Override
    public String process(Object input) {
        return ((String) input).toLowerCase();
    }
}

class Splitter extends Processor {
    @Override
    public String process(Object input) {
        // split() divides a String into pieces:
        return Arrays.toString(((String) input).split(" "));
    }
}

public class Applicator {
    public static void apply(Processor p, Object s) {
        System.out.println("Using Processor " + p.name());
        System.out.println(p.process(s));
    }

    public static void main(String[] args) {
        String s =
            "We are such stuff as dreams are made on";
        apply(new Upcase(), s);
        apply(new Downcase(), s);
        apply(new Splitter(), s);
    }
}
/* Output:
Using Processor Upcase
WE ARE SUCH STUFF AS DREAMS ARE MADE ON
Using Processor Downcase
we are such stuff as dreams are made on
Using Processor Splitter
[We, are, such, stuff, as, dreams, are, made, on]
*/
```

`Applicator.apply()` 方法接收任何类型的 `Processor`，将其应用到一个 Object 并打印结果。可以创建这样一个方法，它根据传递的参数对象来表现出不同的行为，这就是**策略**设计模式。

```java
// interfaces/filters/Waveform.java
package filters;

public class Waveform {
    private static long counter;
    private final long id = counter++;

    @Override
    public String toString() {
        return "Waveform " + id;
    }
}

// interfaces/filters/Filter.java
package filters;

public class Filter {
    public String name() {
        return getClass().getSimpleName();
    }

    public Waveform process(Waveform input) {
        return input;
    }
}

// interfaces/filters/LowPass.java
package filters;

public class LowPass extends Filter {
    double cutoff;

    public LowPass(double cutoff) {
        this.cutoff = cutoff;
    }

    @Override
    public Waveform process(Waveform input) {
        return input; // Dummy processing
    }
}

// interfaces/filters/HighPass.java
package filters;

public class HighPass extends Filter {
    double cutoff;

    public HighPass(double cutoff) {
        this.cutoff = cutoff;
    }

    @Override
    public Waveform process(Waveform input) {
        return input;
    }
}

// interfaces/filters/BandPass.java
package filters;

public class BandPass extends Filter {
    double lowCutoff, highCutoff;

    public BandPass(double lowCut, double highCut) {
        lowCutoff = lowCut;
        highCutoff = highCut;
    }

    @Override
    public Waveform process(Waveform input) {
        return input;
    }
}

// interfaces/interfaceprocessor/Processor.java
package interfaceprocessor;

public interface Processor {
    default String name() {
        return getClass().getSimpleName();
    }

    Object process(Object input);
}

// interfaces/interfaceprocessor/Applicator.java
package interfaceprocessor;

public class Applicator {
    public static void apply(Processor p, Object s) {
        System.out.println("Using Processor " + p.name());
        System.out.println(p.process(s));
    }
}

// interfaces/interfaceprocessor/StringProcessor.java
package interfaceprocessor;

import java.util.*;

interface StringProcessor extends Processor {
    @Override
    String process(Object input);        // [1]

    String S =                           // [2]
        "If she weighs the same as a duck, " +
            "she's made of wood";

    static void main(String[] args) {    // [3]
        Applicator.apply(new Upcase(), S);
        Applicator.apply(new Downcase(), S);
        Applicator.apply(new Splitter(), S);
    }
}

class Upcase implements StringProcessor {
    @Override // Covariant return:
    public String process(Object input) {
        return ((String) input).toUpperCase();
    }
}

class Downcase implements StringProcessor {
    @Override
    public String process(Object input) {
        return ((String) input).toLowerCase();
    }
}

class Splitter implements StringProcessor {
    @Override
    public String process(Object input) {
        return Arrays.toString(((String) input).split(" "));
    }
}
/* Output:
Using Processor Upcase
IF SHE WEIGHS THE SAME AS A DUCK, SHE'S MADE OF WOOD
Using Processor Downcase
if she weighs the same as a duck, she's made of wood
Using Processor Splitter
[If, she, weighs, the, same, as, a, duck,, she's, made,
of, wood]
*/

```

`StringProcessor` 类是复用代码的第一种方法，调用者可以编写符合这个接口的类。

- [1] 处的声明是不必要的，删除它编译器也不会提示错误。但是它能指出方法的返回值从 `Object` 协变为 `String`。
- [2] 处字段 `s` 自动是 `static` 和 `final` 的，因为它是在接口内定义的。
- [3] 处甚至可以在接口内定义一个 `main()` 方法。

在多数情况下类是无法修改的，此时可以使用**适配器**设计模式。在适配器里编写代码来通过已有的接口生成需要的接口。

- 此时 `FilterAdapter` 构造器通过 `Filter` 接口来生成一个需要的 `Processor` 接口的对象。
- `FilterAdapter` 中使用了委托。
- 协变允许我们从 `process()` 里产生一个 `Waveform`，而不仅仅是一个 `Object`。

```java
// interfaces/interfaceprocessor/FilterProcessor.java
package interfaceprocessor;

import filters.*;

class FilterAdapter implements Processor {
    Filter filter;

    FilterAdapter(Filter filter) {
        this.filter = filter;
    }

    @Override
    public String name() {
        return filter.name();
    }

    @Override
    public Waveform process(Object input) {
        return filter.process((Waveform) input);
    }
}

public class FilterProcessor {
    public static void main(String[] args) {
        Waveform w = new Waveform();
        Applicator.apply(new FilterAdapter(new LowPass(1.0)), w);
        Applicator.apply(new FilterAdapter(new HighPass(2.0)), w);
        Applicator.apply(new FilterAdapter(new BandPass(3.0, 4.0)), w);
    }
}
/* Output:
Using Processor LowPass
Waveform 0
Using Processor HighPass
Waveform 0
Using Processor BandPass
Waveform 0
*/
```

## 组合多个接口

```java
// interfaces/Adventure.java
interface CanFight {
    void fight();
}

interface CanSwim {
    void swim();
}

interface CanFly {
    void fly();
}

class ActionCharacter {
    public void fight() {
        System.out.println("ActionCharacter.fight()");
    }
}

class Hero extends ActionCharacter implements CanFight, CanSwim, CanFly {
    @Override
    public void swim() {
        System.out.println("Hero.swim()");
    }

    @Override
    public void fly() {
        System.out.println("Hero.fly()");
    }
}

public class Adventure {
    public static void t(CanFight x) {
        x.fight();
    }

    public static void u(CanSwim x) {
        x.swim();
    }

    public static void v(CanFly x) {
        x.fly();
    }

    public static void w(ActionCharacter x) {
        x.fight();
    }

    public static void main(String[] args) {
        Hero h = new Hero();
        t(h); // Treat it as a CanFight
        u(h); // Treat it as a CanSwim
        v(h); // Treat it as a CanFly
        w(h); // Treat it as an ActionCharacter
    }
}
/* Output:
ActionCharacter.fight()
Hero.swim()
Hero.fly()
ActionCharacter.fight()
*/
```

只能将 `extends` 用于单个类，但是在构建新接口时，`extends` 可以关联多个父接口，接口名称使用逗号分隔。

## 适配接口

```java
// interfaces/RandomStrings.java
import java.nio.*;
import java.util.*;

public class RandomStrings implements Readable {
    private static Random rand = new Random(47);
    private static final char[] CAPITALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
    private static final char[] LOWERS = "abcdefghijklmnopqrstuvwxyz".toCharArray();
    private static final char[] VOWELS = "aeiou".toCharArray();
    private int count;

    public RandomStrings(int count) {
        this.count = count;
    }

    @Override
    public int read(CharBuffer cb) {
        if (count-- == 0)
            return -1; // Indicates end of input
        cb.append(CAPITALS[rand.nextInt(CAPITALS.length)]);
        for (int i = 0; i < 4; i++) {
            cb.append(VOWELS[rand.nextInt(VOWELS.length)]);
            cb.append(LOWERS[rand.nextInt(LOWERS.length)]);
        }
        cb.append(" ");
        return 10; // Number of characters appended
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(new RandomStrings(10));
        while (s.hasNext())
            System.out.println(s.next());
    }
}
/* Output:
Yazeruyac
Fowenucor
Goeazimom
Raeuuacio
Nuoadesiw
Hageaikux
Ruqicibui
Numasetih
Kuuuuozog
Waqizeyoy
*/
```

`RandomStrings` 实现了 `Readable` 接口，让 `RandomStrings` 伪装成一个“输入源”，被 `Scanner` 当作输入流读取，每次读出一个随机生成的字符串。

- 只要实现了 `Readable`，就能作为 `Scanner` 的数据源。
- `while (s.hasNext())` 中 `hasNext()` 方法说的是 `Scanner` 试图从输入源读数据。
    - `Scanner` 内部调用 `source.read(charBuffer);`。
    - `source` 就是 `RandomStrings` 对象。
- `count` 初始是 `10`。
    - 每调用一次 `read()` 执行 `count--`，当 `count == 0` 时返回 `-1`，`-1` 是 `Readable` 的 EOF 标志。

    ```java
    cb.append(CAPITALS[rand.nextInt(CAPITALS.length)]);
    for (int i = 0; i < 4; i++) {
        cb.append(VOWELS[rand.nextInt(VOWELS.length)]);
        cb.append(LOWERS[rand.nextInt(LOWERS.length)]);
    }
    cb.append(" ");
    ```

- 上述代码拼出来的结构是：1 个大写字母 + (元音 + 小写字母) × 4 + 空格（`" "`）。
    - 最后的 `" "` 很关键，`Scanner` 默认用空白符分词，没有空格 `next()` 就读不出来。
- `return 10;` 表示这次向 `CharBuffer` 写入了多少字符。
    - `Scanner` 用它判断是否成功读取，是否继续读取。
    - 这个值要大于等于 `0`，代表有数据；`-1` 代表结束。
- `Scanner` 使用正则 `\p{javaWhitespace}+` 作为默认分隔符。
    - 每次 `next()` 读取一个 `token`。
    - 所以 `"Yazeruyac "` 变成了 `Yazeruyac`。

任何类都可以实现接口，这就意味着把接口作为参数的方法可以让任何类都适应它。

## 接口中的字段

接口中的任何字段都自动是 `public`、`static` 和 `final` 的。

### 初始化接口中的字段

```java
// interfaces/RandVals.java
import java.util.*;

public interface RandVals {
    Random RAND = new Random(47);
    int RANDOM_INT = RAND.nextInt(10);
    long RANDOM_LONG = RAND.nextLong() * 10;
    float RANDOM_FLOAT = RAND.nextLong() * 10;
    double RANDOM_DOUBLE = RAND.nextDouble() * 10;
}
```

接口中的字段可以用非常量表达式初始化。

- 这些字段都是静态的，所以它们会在类第一次加载时被初始化，首次访问该接口的任何字段都会出发这个加载。
- 这些字段不是接口的一部分，这些值存储在该接口的静态存储区中。

## 嵌套接口

```java
// interfaces/nesting/NestingInterfaces.java
package nesting;

class A {
    interface B {
        void f();
    }
    public interface C {
        void f();
    }
    private interface D {
        void f();
    }

    public class BImp implements B {
        @Override
        public void f() {
        }
    }

    private class BImp2 implements B {
        @Override
        public void f() {
        }
    }

    class CImp implements C {
        @Override
        public void f() {
        }
    }

    private class CImp2 implements C {
        @Override
        public void f() {
        }
    }

    private class DImp implements D {
        @Override
        public void f() {
        }
    }

    public class DImp2 implements D {
        @Override
        public void f() {
        }
    }

    private D dRef;

    public D getD() {
        return new DImp2();
    }

    public void receiveD(D d) {
        dRef = d;
        dRef.f();
    }
}

interface E {
    interface G {
        void f();
    }

    // Redundant "public":
    public interface H {
        void f();
    }

    void g();
    // Cannot be private within an interface:
    //- private interface I {}
}

public class NestingInterfaces {
    public class BImp implements A.B {
        @Override
        public void f() {
        }
    }

    class CImp implements A.C {
        @Override
        public void f() {
        }
    }

    // Cannot implement a private interface except
    // within that interface's defining class:
    //- class DImp implements A.D {
    //-  public void f() {}
    //- }
    class EImp implements E {
        @Override
        public void g() {
        }
    }

    class EGImp implements E.G {
        @Override
        public void f() {
        }
    }

    class EImp2 implements E {
        @Override
        public void g() {
        }

        class EG implements E.G {
            @Override
            public void f() {
            }
        }
    }

    public static void main(String[] args) {
        A a = new A();
        // 看不到 A.D：
        //- A.D ad = a.getD();
        // 类型不匹配 + 不可见：
        //- A.DImp2 di2 = a.getD();
        // 无法访问方法：
        //- a.getD().f();
        // 只有 A 自己能操作自己：
        A a2 = new A();
        a2.receiveD(a.getD());
    }
}
```

这段代码主要想说明了 4 件事：

- 接口可以嵌套在类里，接口和类一样，也受访问控制影响。
    - 接口 `A.B`，修饰符默认包级，同包能看到。实现 `A.B` 的 `BImp` 和 `BImp2` 都合法，因为 `B` 对 `A` 内部可见。
    - 接口 `A.C`，修饰符 `public`，任何地方都能看到。实现 `A.C` 的 `CImp` 和 `CImp2` 都合法，因为 `public` 接口谁都能实现。
    - 接口 `A.D`，修饰符 `private`，仅 `A` 内部能看到。实现 `A.D` 的 `DImp` 和 `DImp2` 都合法，因为实现发生在 `A` 内部，`private` 接口只能在定义它的类里被实现。
- 接口也可以嵌套在接口里。
    - 接口中的接口默认就是 `public static`，任何修饰都是多余的。
    - 接口中不允许定义任何 `private` 接口。
- 类中嵌套接口可以有不同访问级别（外部类 `NestingInterfaces` 中的的实现）。
    - 实现 `A.B` 的 `BImp` 合法，因为 `NestingInterfaces` 和 `A` 在同一个包（同一个文件）。
    - 实现 `A.C` 的 `CImp` 合法，因为 `public` 接口谁都能实现。
    - 不能实现 `A.D`，因为 `private` 接口只对 `A` 可见。
    - 实现接口里的接口完全没问题，因为嵌套在接口中的接口默认 `public`。
- 能拿到对象不等于能用它。
    - 此处外部看不到接口，无法调用接口方法，只有 `A` 自己能操作它。
    - 外部不能声明 `A.D` 类型。
    - 不能调用 `f()`。
    - 不能实现 `D`。
    - 但可以执行 `a2.receiveD(a.getD());`，这就是类型对外不可见，但可传递。自己消费自己。

## 接口和工厂

```java
// interfaces/Factories.java
interface Service {
    void method1();
    void method2();
}

interface ServiceFactory {
    Service getService();
}

class Service1 implements Service {
    Service1() {
    } // Package access

    @Override
    public void method1() {
        System.out.println("Service1 method1");
    }

    @Override
    public void method2() {
        System.out.println("Service1 method2");
    }
}

class Service1Factory implements ServiceFactory {
    @Override
    public Service getService() {
        return new Service1();
    }
}

class Service2 implements Service {
    Service2() {
    } // Package access

    @Override
    public void method1() {
        System.out.println("Service2 method1");
    }

    @Override
    public void method2() {
        System.out.println("Service2 method2");
    }
}

class Service2Factory implements ServiceFactory {
    @Override
    public Service getService() {
        return new Service2();
    }
}

public class Factories {
    public static void serviceConsumer(ServiceFactory fact) {
        Service s = fact.getService();
        s.method1();
        s.method2();
    }

    public static void main(String[] args) {
        serviceConsumer(new Service1Factory());
        // Services are completely interchangeable:
        serviceConsumer(new Service2Factory());
    }
}
/* Output:
Service1 method1
Service1 method2
Service2 method1
Service2 method2
*/
```

工厂方法设计模式。

- 不是直接调用构造器，而是在工厂对象上调用创建方法，它可以产生接口实现。理论上，代码与接口实现完全隔离，从而可以透明地将一种实现替换为另一种实现。
- 如果没有工厂方法，代码必须在某处指定创建 `Service` 的确切类型，以调用相应的构造器。
- 添加中间层的一个常见原因是创建框架。

## 新特性

### JDK9：接口的 `private` 方法

JDK9 中可以有 `private` 方法，仅供接口内的方法进行调用。此时 `fd()` 方法不再需要 `default` 关键字，`private` 之后自动就是 `default` 的了。

```java
// interfaces/PrivateInterfaceMethods.java
interface Old {
    default void fd() {
        System.out.println("Old::fd()");
    }

    static void fs() {
        System.out.println("Old::fs()");
    }

    default void f() {
        fd();
    }

    static void g() {
        fs();
    }
}

class ImplOld implements Old {}

interface JDK9 {
    private void fd() { // Automatically default
        System.out.println("JDK9::fd()");
    }

    private static void fs() {
        System.out.println("JDK9::fs()");
    }

    default void f() {
        fd();
    }

    static void g() {
        fs();
    }
}

class ImplJDK9 implements JDK9 {}

public class PrivateInterfaceMethods {
    public static void main(String[] args) {
        new ImplOld().f();
        Old.g();
        new ImplJDK9().f();
        JDK9.g();
    }
}
/* Output:
Old::fd()
Old::fs()
JDK9::fd()
JDK9::fs()
*/
```

### JDK17：密封类和密封接口

JDK17 最终引入了密封类和密封接口，因此基类或接口可以限制自己能派生出哪些类。下方代码中如果尝试继承未在 `permits` 子句中列出的子类，比如 `D3`，则编译器会产生错误。

```java
// interfaces/Sealed.java
// {NewFeature} Since JDK 17
sealed class Base permits D1, D2 {}

final class D1 extends Base {}

final class D2 extends Base {}
// Illegal:
// final class D3 extends Base {}
```

还可以密封接口和抽象类：

```java
// interfaces/SealedInterface.java
// {NewFeature} Since JDK 17
sealed interface Ifc permits Imp1, Imp2 {}
final class Imp1 implements Ifc {}
final class Imp2 implements Ifc {}

sealed abstract class AC permits X {}
final class X extends AC {}
```

如果所有的子类都定义在同一个文件中，则不需要 `permits` 子句：

```java
// interfaces/SameFile.java
// {NewFeature} Since JDK 17
sealed class Shape {}
final class Circle extends Shape {}
final class Triangle extends Shape {}
```

`permits` 子句允许我们在单独的文件中定义子类：

```java
// interfaces/SealedPets.java
// {NewFeature} Since JDK 17
sealed class Pet permits Dog, Cat {}

// interfaces/SealedDog.java
final class Dog extends Pet {}

// interfaces/SealedCat.java
final class Cat extends Pet {}
```

`sealed` 类的子类只能通过下面的某个修饰符来定义：

- `final`：不允许有进一步的子类。
- `sealed`：允许有一组密封子类。
- `non-sealed`：允许未知的子类来继承它。

`sealed` 的子类保持了对层级结构的严格控制：

```java
// interfaces/SealedSubclasses.java
// {NewFeature} Since JDK 17
sealed class Bottom permits Level1 {}
sealed class Level1 extends Bottom permits Level2 {}
sealed class Level2 extends Level1 permits Level3 {}
final class Level3 extends Level2 {}
```

注意，一个 `sealed` 类必须至少有一个子类。

一个 `sealed` 的基类无法阻止 `non-sealed` 的子类的使用，因此可以随时放开限制：

```java
// interfaces/NonSealed.java
// {NewFeature} Since JDK 17
sealed class Super permits Sub1, Sub2 {}
final class Sub1 extends Super {}
non-sealed class Sub2 extends Super {}
class Any1 extends Sub2 {}
class Any2 extends Sub2 {}
```

`Sub2` 允许任意数量的子类，因此它似乎放开了对可以创建的类型的控制。但是，我们还是严格限制了 `sealed` 类 `Super` 的直接子类。也就是说，`Super` 仍然只能有直接子类 `Sub1` 和 `Sub2`。

JDK16 的 `record` 也可以用作接口的密封实现。因为 `record` 是隐式的 `final`，所以它们不需要在前面加 `final` 关键字。

```java
// interfaces/SealedRecords.java
// {NewFeature} Since JDK 17
sealed interface Employee permits CLevel, Programmer {}
record CLevel(String type) implements Employee {}
record Programmer(String experience) implements Employee {}
```

编译器会阻止我们从密封层次结构中向下转型为非法类型：

```java
// interfaces/CheckedDowncast.java
// {NewFeature} Since JDK 17
sealed interface II permits JJ {}
final class JJ implements II {}
class Something {}

public class CheckedDowncast {
  public void f() {
    II i = new JJ();
    JJ j = (JJ)i;
    // Something s = (Something)i;
    // error: incompatible types: II cannot
    // be converted to Something
  }
}
```

可以在运行时使用 `getPermittedSubclasses()` 方法来发现允许的子类：

```java
// interfaces/PermittedSubclasses.java
// {NewFeature} Since JDK 17
sealed class Color permits Red, Green, Blue {}
final class Red extends Color {}
final class Green extends Color {}
final class Blue extends Color {}

public class PermittedSubclasses {
  public static void main(String[] args) {
    for(var p: Color.class.getPermittedSubclasses())
      System.out.println(p.getSimpleName());
  }
}
/* Output:
Red
Green
Blue
*/
```
