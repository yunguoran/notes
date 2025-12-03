# 初始化和清理

## 使用构造器保证初始化

- Java 中构造器的名字就是类的名字。
- 方法首字母小写的编程风格并不适用于构造器，因为构造器的名字必须与类的名字完全匹配。
- 构造器没有返回类型，并且也别无选择。但注意 `new` 表达式确实返回了新建对象的引用。

## 方法重载（Overload）

- **方法重载**是指不同参数类型的方法有相同的名字。
- 就算仅仅是参数顺序不同也足以区分两个方法，不过我们通常不会采用这种方式，因为它会产生难以维护的代码。

### 类型提升

- `byte` → `short` → `int` → `long` → `float` → `double`。
- `char` → `int` → `long` → `float` → `double`。
- 算术表达式中，`byte`/`short`/`char` 在运算时先被提升为 `int`。

方法重载解析优先级（常用记忆顺序）：

- 精确匹配（exact）
- 原始类型提升（widening）
- 装箱（boxing，例如 int → Integer）
- 可变参数（varargs）

编译时常量的 `int` 值如果在目标窄类型范围内，可以在赋值给变量时被允许窄化（例如 `byte b = 5;` 不需要强转）。但在方法重载解析时整数字面量被视为 `int`，优先匹配 `int` 参数；只有当没有 `int` 可用时，才使用提升规则。

注意：

- `char` 类型会直接提升到 `int` 类型。
    - `char` 代表的是字符，用于存储 Unicode 字符集中的字符值。其范围是从 `0` 到 `65535`（2^16-1，无符号），通常用于处理字符数据。
    - `short` 是一个有符号的整数类型，其范围是从 `-32768` 到 `32767`（2^15-1）。
    - 因为 `short` 无法全部包含 `char` 的范围，因此 `char` 类型会直接提升到 `int` 类型。
- 符号位的存在使得负数的表示有了特殊性，尤其是最小负数 `-32768`，它就是补码表示法中负零的替代。

## 无参构造器

- 如果你创建了一个没有构造器的类，编译器会自动为这个类添加一个无参构造器。
- 如果你已经定义了一个构造器，无论是否有参数，编译器都**不会**再帮你自动创建一个了。

## `this` 关键字

- 两个相同类型的对象 `a` 和 `b` 在调用相同的方法 `peel()` 时，编译器做了一些底层工作，`peel()` 方法中第一个参数隐密地传入了一个指向操作对象的引用，这是在内部实现的。
- `this` 关键字只能在非静态方法中使用。
- 如果你在一个类的方法里调用其他该类中的方法，不要使用 `this`，直接调用即可，`this` 自动地应用于其他方法上了。

### `this` 的使用场景

- 区分成员变量和局部变量

    ```java
    class Person {
        private String name;

        public Person(String name) {
            this.name = name; // 这里的 this.name 指的是类的成员变量
        }
    }
    ```

- 调用当前类的构造函数

    ```java
    class Person {
        private String name;
        private int age;

        public Person(String name) {
            this(name, 0);  // 调用另一个构造函数
        }

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    }
    ```

- 引用当前对象

    ```java
    public class Car {
        private String model;

        public void printModel() {
            System.out.println(this.model);  // 使用 this 引用当前对象的 model 字段
        }
    }
    ```

- 返回当前对象

    ```java
    public class Car {
        private String model;

        public Car setModel(String model) {
            this.model = model;
            return this;  // 返回当前对象
        }
    }
    ```

注意：

- 虽然可以用 `this` 调用另一个构造器，但不能同时调用两个。
- 构造器调用必须出现在方法的最开始部分。
- 编译器禁止在非构造器的普通方法里调用构造器。

### `static` 的含义

- `static` 方法中不会存在 `this`。
- 不能在静态方法内部调用非静态方法（反过来可以）。
- 一个类里的静态方法可以访问其他静态方法和静态字段。

## 清理：终结和垃圾回收

在 Java 中对象并不总是被垃圾回收。垃圾回收并不等同于 C++ 中的析构函数。

### `finalize()` 的作用

- 垃圾回收仅与内存有关。垃圾收集器存在的唯一原因就是回收程序里不再使用的内存。
- `finalize()` 的使用仅限于一种特殊的情况：对象以某种方式分配内存空间，而不是通过创建对象来分配。
    - 这主要通过**本地方法**来实现，它只可以在 Java 代码里调用 C 和 C++ 代码，但 C 和 C++ 可以调用其他语言的代码，因此实际上 Java 可以调用任何代码。
    - 在非 Java 代码里，可能会调用 C 的 `malloc()` 系列函数来分配存储空间，此时除非明确调用 `free()` 方法，此时该存储空间不会被释放，从而导致内存泄露。
    - `free()` 是一个 C 和 C++ 函数，所以需要在 `finalize()` 里通过本地方法来调用。
- 无论垃圾收集还是终结操作都不保证一定会发生。如果 JVM 没有面临内存耗尽的情况，它可能不会浪费时间去执行垃圾收集来恢复内存。

### 垃圾回收器（Garbage Collector）的工作原理

#### 可达性分析（Reachability Analysis）

垃圾回收器（GC）判断哪些对象是“活着”的时候，不是去遍历所有对象找引用它们的东西，而是从一组称为 GC Roots 的根集合出发，沿着引用链把能到达的对象全部标记为存活；没有被标记到的对象就是垃圾，可以被回收。

- GC Roots 是一组特殊的“起点对象”（或引用），GC 以它们为根去做可达性分析。
- 任何从 GC Roots 出发、通过一系列引用能到达的对象，都被认为是“可达的/存活的”。
- 常见的 GC Roots。
    - 栈帧（Stack Frame）中正在使用的局部变量与方法参数。
    - 所有的活动线程（Thread）。
    - 静态变量（Static Fields）。
    - 类对象（java.lang.Class）。
    - JNI（Java Native Interface）/本地（Native）代码中持有的全局引用。

#### 垃圾收集算法

停止-复制（stop-and-copy）算法：

- 这需要先暂停程序的运行，然后将所有存活的对象从当前堆复制到另一个堆，没有复制的就是需要被垃圾回收的。另外，当对象被复制到新堆时，它们是一个挨着一个，因此十分紧凑。
- 当对象从一处复制到另一处，所有指向它的引用都必须修正。位于栈或静态存储区的引用可以直接被修正，但可能还有其他指向这些对象的引用，它们在遍历的过程中才能被找到（可以想象成一个表格，将旧地址映射到新地址）。

这种所谓的“复制回收器”效率低下主要因为两个原因：

- 其一是需要有两个堆，然后在这两个独立的堆之间来回复制内存，这比实际需要多了一倍内存。某些 JVM 解决这个问题的方式是，按需要将堆划分成较大的块，复制动作发生在块之间。
- 其二在于复制过程本身。一旦程序进入稳定状态之后，可能只会产生少量垃圾，甚至没有。尽管如此，复制回收器仍然会将所有内存从一处复制到另一处，这是一种浪费。为了避免这种状况，一些 JVM 检测到没有新垃圾产生后，会切换到不同的垃圾收集算法（即“自适应”）。这种模式称为标记-清除，Sun 公司早期版本的 JVM 一直使用这种算法。对一般用途，“标记-清除”算法相当慢，但是垃圾很少甚至不产生垃圾时，它的速度就很快了。

标记-清除（mark-and-sweep）算法：

它所依据的思路仍然是从栈和静态存储区出发，遍历所有的引用，找出所有存活的对象。但每当找到一个存活对象，就给该对象设置一个标志————此时尚未开始回收。只有在标记过程完成后才会进行清除。在清除过程中，没有标记的对象被释放，但不会发生复制。此时剩下的堆空间是不连续的，垃圾回收器要是希望得到连续空间，就需要重新排列对象。

严格的“停止-复制”需要将每个存活对象都从旧堆复制到新堆，然后才能释放旧堆，这意味着需要大量内存。有了块之后，垃圾回收通常可以将对象直接复制到废弃的块里。每个块都有一个代数（Generation Count）来跟踪它是否还活着。通常，只压缩上次垃圾回收以来创建的块。如果块在某处被引用，它的代数就会增加。这种方式可以很方便的处理正常情况下的大量短期临时对象。垃圾回收器会周期性地进行全面清理————不过大的对象不会被仍然不会被复制（只是增加它们的代数），包含小对象的块会被复制和压缩。

## 成员初始化

- 对于方法的局部变量，如果没有初始化，会得到一个编译时错误。
- 对于类的基本类型字段，Java 会自动给于默认值。
    - char 类型的默认值是 `\u0000`。
        - `\u` 本身不是一种进制，而是一个在 Java 等编程语言中用于引入 Unicode 转义序列的前缀。
        - 在 Java 中，`\u` 后面必须紧跟着 4 位十六进制数字。

## 构造器初始化

在类中变量定义的顺序决定了它们初始化的顺序。即使变量定义散布在方法定义之间，它们仍会在任何方法（包括构造器）被调用之前得到初始化。

```java
class Window {
    Window(int marker) {
        System.out.println("Window(" + marker + ")");
    }
}

class House {
    Window w1 = new Window(1); // Before constructor

    House() {
        // Show that we're in the constructor:
        System.out.println("House()");
        w3 = new Window(33); // Reinitialize w3
    }

    Window w2 = new Window(2); // After constructor

    void f() {
        System.out.println("f()");
    }

    Window w3 = new Window(3); // At end
}

public class OrderOfInitialization {
    public static void main(String[] args) {
        House h = new House();
        h.f(); // Shows that construction is done
    }
}
```

Output:

```text
Window(1)
Window(2)
Window(3)
House()
Window(33)
f()
```

### 静态数据的初始化

无论创建了多少对象，静态数据都只占用一份存储空间。`static` 关键字不能应用于局部变量，而仅适用于字段（成员变量）。如果一个字段是静态的基本类型，你没有初始化它，那么它就会获得基本类型的标准初始值。如果它是对象引用，那么它的默认初值就是 `null`。

```java
class Bowl {

    Bowl(int marker) {
        System.out.println("Bowl(" + marker + ")");
    }

    void f1(int marker) {
        System.out.println("f1(" + marker + ")");
    }
}

class Table {

    static Bowl bowl1 = new Bowl(1);

    Table() {
        System.out.println("Table()");
        bowl2.f1(1);
    }

    void f2(int marker) {
        System.out.println("f2(" + marker + ")");
    }

    static Bowl bowl2 = new Bowl(2);
}

class Cupboard {

    Bowl bowl3 = new Bowl(3);
    static Bowl bowl4 = new Bowl(4);

    Cupboard() {
        System.out.println("Cupboard()");
        bowl4.f1(2);
    }

    void f3(int marker) {
        System.out.println("f3(" + marker + ")");
    }

    static Bowl bowl5 = new Bowl(5);
}

public class StaticInitialization {

    public static void main(String[] args) {
        System.out.println("main creating new Cupboard()");
        new Cupboard();
        System.out.println("main creating new Cupboard()");
        new Cupboard();
        table.f2(1);
        cupboard.f3(1);
    }

    static Table table = new Table();
    static Cupboard cupboard = new Cupboard();
}
```

Output:

```text
Bowl(1)
Bowl(2)
Table()
f1(1)
Bowl(4)
Bowl(5)
Bowl(3)
Cupboard()
f1(2)
main creating new Cupboard()
Bowl(3)
Cupboard()
f1(2)
main creating new Cupboard()
Bowl(3)
Cupboard()
f1(2)
f2(1)
f3(1)
```

初始化的顺序是从静态字段开始（如果它们还没有被先前的对象创建触发初始化的话），然后是非静态字段。

创建对象的过程如下，假设有个名为 `Dog` 的类：

- 尽管没有显式使用 `static` 关键字，但构造器实际上也是静态方法。因此，第一次创建类型为 `Dog` 的对象时，或第一次访问 Dog 类的静态方法或静态字段时，Java 解释器会搜索类路径来定位 `Dog.class` 文件。
- 当 `Dog.class` 被加载后，它的所有静态初始化工作都会执行。因此，静态初始化只在 Class 对象首次加载时发生一次。
- 当使用 `new Dog()` 创建对象时，首先会在堆上为 `Dog` 对象分配足够的存储空间。
- 这块存储空间首先会被清空，然后会将 `Dog` 对象中的所有基本类型数据设置为其默认值，引用被设置为 `null`。
- 执行所有出现在字段定义处的初始化操作。
- 执行构造器。

### 显式的静态初始化

Java 允许在一个类里将多个静态初始化语句放在一个**静态块**里。静态块里的代码只执行一次：第一次创建该类的对象时，或第一次访问该类的静态成员时（即使从未创建该类的对象）。

```java
class Cup {

    Cup(int marker) {
        System.out.println("Cup(" + marker + ")");
    }

    void f(int marker) {
        System.out.println("f(" + marker + ")");
    }
}

class Cups {

    static Cup cup1;
    static Cup cup2;

    static {
        cup1 = new Cup(1);
        cup2 = new Cup(2);
    }

    Cups() {
        System.out.println("Cups()");
    }
}

public class ExplicitStatic {
    public static void main(String[] args) {
        System.out.println("Inside main()");
        // Cups.cup1.f(99);                  // [1]
    }
    // static Cups cups1 = new Cups();  // [2]
    // static Cups cups2 = new Cups();  // [2]
}
/* Output:
Inside main()
Cup(1)
Cup(2)
f(99)
*/
```

### 非静态实例初始化

实例初始化子句在构造器之前执行，此语法对于支持**匿名内部类**的初始化是必需的。

```java
class Mug {
    Mug(int marker) {
        System.out.println("Mug(" + marker + ")");
    }
}

public class Mugs {
    Mug mug1;
    Mug mug2;

    {                                         // [1]
        mug1 = new Mug(1);
        mug2 = new Mug(2);
        System.out.println("mug1 & mug2 initialized");
    }

    Mugs() {
        System.out.println("Mugs()");
    }

    Mugs(int i) {
        System.out.println("Mugs(int)");
    }

    public static void main(String[] args) {
        System.out.println("Inside main()");
        new Mugs();
        System.out.println("new Mugs() completed");
        new Mugs(1);
        System.out.println("new Mugs(1) completed");
    }
}
/* Output:
Inside main()
Mug(1)
Mug(2)
mug1 & mug2 initialized
Mugs()
new Mugs() completed
Mug(1)
Mug(2)
mug1 & mug2 initialized
Mugs(int)
new Mugs(1) completed
*/
```

## 数组初始化

数组是一个对象序列或基本类型序列，其中含有的元素类型相同。数组通过方括号**索引操作符**（Indexing Operator）来定义和使用。下面两种定义都合法：

```java
int[] a1;
int a1[];
```

编译器不允许指定数组的大小。定义数组之后我们所拥有的知识对数组的引用（已经为该引用分配了足够的存储空间），但并没有为数组对象本身分配任何空间。只有在初始化数组时，才会为数组对象分配存储空间。

```java
int[] a1 = {1, 2, 3, 4, 5}
```

上述代码会在定义数组时使用一组花括号括起来的值来进行初始化。这种情况下，编译器负责存储的分配（相当于使用 `new`）。此种初始化表达式只能在创建数组的地方出现。

下方的代码将会把 `a1` 这个数组赋值给 `a2`，但其实真正所做的只是复制了一个引用。这里的 `a1` 和 `a2` 只是同一个数组的不同别名，因此任意一个数组所做的更改都可以在另一个数组中看到。

```java
public class ArraysOfPrimitives {
    public static void main(String[] args) {
        int[] a1 = {1, 2, 3, 4, 5};
        int[] a2;
        a2 = a1;
        for (int i = 0; i < a2.length; i++)
            a2[i] += 1;
        for (int i = 0; i < a1.length; i++)
            System.out.println("a1[" + i + "] = " + a1[i]);
    }
}
/* Output:
a1[0] = 2
a1[1] = 3
a1[2] = 4
a1[3] = 5
a1[4] = 6
*/
```

### 可变参数列表

- 如果没有为自己的类定义 `toString()` 方法，默认的行为就是打印类名和对象的地址。
- 省略号可以用来定义一个可变参数列表。编译器会自动将其转换为一个 `Object` 类型的数组。
- 可以将 `0` 个参数传递给可变参数列表。

```java
static void printArray(Object... args) {
    for (Object obj : args)
        System.out.print(obj + " ");
    System.out.println();
}
```

### 枚举类型

- 枚举类型的实例是常量，所以都是大写的，如果一个名字中有多个单词，它们之间用下划线分隔。
- 创建 `enum` 时，编译器会自动添加一个 `toString()` 方法，来方便的显示 `enum` 实例的名字。
- 静态的 `values()` 方法，按照声明顺序生成一个 `enum` 常量值的数组。
- `ordinal()` 方法输出特定枚举常量的声明顺序。
- `switch` 语句中可以直接使用枚举类型。

```java
// Spiciness.java
public enum Spiciness {
  NOT, MILD, MEDIUM, HOT, FLAMING
}

// EnumOrder.java
public class EnumOrder {
    public static void main(String[] args) {
        for (Spiciness s : Spiciness.values())
            System.out.println(s + ", ordinal " + s.ordinal());
    }
}
/* Output:
NOT, ordinal 0
MILD, ordinal 1
MEDIUM, ordinal 2
HOT, ordinal 3
FLAMING, ordinal 4
*/
```

### JDK 11 新特性：局部变量类型推断（Type Inference）

```java
class Plumbus {
}

public class TypeInference {
    void method() {
        // Explicit type:
        String hello1 = "Hello";
        // Type inference:
        var hello = "Hello!";
        // Works for user-defined types:
        Plumbus pb1 = new Plumbus();
        var pb2 = new Plumbus();
    }

    // Also works for static methods:
    static void staticMethod() {
        var hello = "Hello!";
        var pb2 = new Plumbus();
    }
}

class NoInference {
    String field1 = "Field initialization";
    // var field2 = "Can't do this";
    // void method() {
    //   var noInitializer; // No inference data
    //   var aNull = null;  // No inference data
    // }
    // var inferReturnType() {
    //   return "Can't infer return type";
    // }
}
```
