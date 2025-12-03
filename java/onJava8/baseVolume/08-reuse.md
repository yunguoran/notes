# 复用

在新类中创建现有类的对象。这称为**组合**（Composition），因为新类由现有类的对象组合而成。

## 组合语法

将对象引用放在新类中即可为组合。

- 每个非基本类型的对象都有一个 `toString()` 方法。
- 注解 `@Override` 用在 `toString()` 方法上，来让编译器确保我们实现了正确的重写。`@Override` 是可选的，但它有助于验证有没有拼写错误。

初始化引用的四种方式如下：

- 在定义对象时进行显式初始化。这意味着它们将始终在调用构造器之前被初始化。
- 使用实例初始化块初始化。
- 在该类的构造器中进行初始化。
- 在对象实际使用之前。这通常称为延迟初始化（Lazy Initialization）。在对象创建成本高昂且不需要每次都创建的情况下，它可以减少开销。

```java
// reuse/Bath.java
class Soap {
    private String s;

    Soap() {
        System.out.println("Soap()");
        s = "Constructed";
    }

    @Override
    public String toString() {
        return s;
    }
}

public class Bath {
    private String // Initializing at point of definition:
            s1 = "Happy",
            s2 = "Happy",
            s3, s4;
    private Soap castile;
    private int i;
    private float toy;

    public Bath() {
        System.out.println("Inside Bath()");
        s3 = "Joy";
        toy = 3.14f;
        castile = new Soap();
    }

    // Instance initialization:
    {
        i = 47;
    }

    @Override
    public String toString() {
        if (s4 == null) // Delayed initialization:
            s4 = "Joy";
        return
                "s1 = " + s1 + "\n" +
                        "s2 = " + s2 + "\n" +
                        "s3 = " + s3 + "\n" +
                        "s4 = " + s4 + "\n" +
                        "i = " + i + "\n" +
                        "toy = " + toy + "\n" +
                        "castile = " + castile;
    }

    public static void main(String[] args) {
        Bath b = new Bath();
        System.out.println(b);
    }
}
```

上述代码执行流程如下：

- 程序开始执行 `main()`，`new Bath()` 创建了一个 `Bath` 对象，于是开始进入对象初始化流程。
- JVM 会先为这个 `Bath` 实例分配内存，并给每个成员变量赋上默认值。
    - `s1`：`null`。
    - `s2`：`null`。
    - `s3`：`null`。
    - `s4`：`null`。
    - `castile`：`null`。
    - `i`：`0`。
    - `toy`：`0.0`。
- 执行字段的显式初始化语句：Java 会按照它们在类中出现的顺序依次执行这些赋值语句（无论写在哪一行）。
    - `s1 = "Happy"`。
    - `s2 = "Happy"`。
- 执行实例初始化块。
    - `i = 47`。
- 执行构造方法 `Bath()`。
    - 打印 `Inside Bath()`。
    - `s3 = "Joy"`。
    - `toy = 3.14f`。
    - 进入 `Soap` 类的构造函数。
- 执行 `Soap` 构造方法。
    - 打印 `Soap()`。
    - 把 `Soap` 对象的字段 `s` 设为 `"Constructed"`。
    - 这时 `Bath` 的字段 `castile` 指向了这个 `Soap` 实例。
- 构造方法执行完毕，返回到 `main()`。
    - `s1`：`"Happy"`。
    - `s2`：`"Happy"`。
    - `s3`：`"Joy"`。
    - `s4`：`null`。
    - `castile`：`Soap` 对象（其 `s` = `"Constructed"`）。
    - `i`：`47`。
    - `toy`：`3.14`。
- 调用 `System.out.println(b);` 会触发 `b.toString()`。
    - 因为 `s4` 目前是 `null`，于是执行：`s4 = "Joy"`。
    - 然后字符串拼接时，`castile` 会被自动调用 `Soap.toString()`，返回 `"Constructed"`。
- 拼出完整字符串，输出如下：

    ```java
    Inside Bath()
    Soap()
    s1 = Happy
    s2 = Happy
    s3 = Joy
    s4 = Joy
    i = 47
    toy = 3.14
    castile = Constructed
    ```

## 继承语法

```java
// reuse/Detergent.java
class Cleanser {
    private String s = "Cleanser";

    public void append(String a) {
        s += a;
    }

    public void dilute() {
        append(" dilute()");
    }

    public void apply() {
        append(" apply()");
    }

    public void scrub() {
        append(" scrub()");
    }

    @Override
    public String toString() {
        return s;
    }

    public static void main(String[] args) {
        Cleanser x = new Cleanser();
        x.dilute();
        x.apply();
        x.scrub();
        System.out.println(x);
    }
}

public class Detergent extends Cleanser {
    // Change a method:
    @Override
    public void scrub() {
        append(" Detergent.scrub()");
        super.scrub(); // Call base-class version
    }

    // Add methods to the interface:
    public void foam() {
        append(" foam()");
    }

    // Test the new class:
    public static void main(String[] args) {
        Detergent x = new Detergent();
        x.dilute();
        x.apply();
        x.scrub();
        x.foam();
        System.out.println(x);
        System.out.println("Testing base class:");
        Cleanser.main(args);
    }
}
/*
运行 Detergent.main() 时输出为:
Cleanser dilute() apply() Detergent.scrub() scrub() foam()
Testing base class:
Cleanser dilute() apply() scrub()

运行 Cleanser.main() 时输出为:
Cleanser dilute() apply() scrub()
*/
```

- `+=` 操作符是为处理字符串对象而重载的操作符之一。
- `Detergent` 和 `Cleanser` 类各有一个 `main()` 方法。
    - 可以为每个类都创建一个 `main()` 来进行测试，测试完也无需删掉，以供后续测试。
    - 即使一个程序中有很多类，唯一运行的 `main()` 也只会是在命令行中调用的那个。
- 即使一个类只有包访问权限，也可以访问它的 `public main()` 方法（`Cleanser.main()`）。
- `Detergent` 通过 `extends` 关键字继承了 `Cleanser`，所以它的接口就自动获得了这些方法，即使并没有在 `Detergent` 中显式定义。
- `super` 关键字用来指代当前类继承的基类。`super.scrub()` 调用了基类版本的 `scrub()` 方法。
- 当创建子类对象时，它里面包含了一个基类的子对象（Subobject），这个子对象与直接通过基类创建的对象是一样的。
- Java 会自动在子类构造器中插入对基类构造器的调用。

## 委托

```java
// reuse/SpaceShipControls.java
public class SpaceShipControls {
    void up(int velocity) {
    }

    void down(int velocity) {
    }

    void left(int velocity) {
    }

    void right(int velocity) {
    }

    void forward(int velocity) {
    }

    void back(int velocity) {
    }

    void turboBoost() {
    }
}

// reuse/SpaceShipDelegation.java
public class SpaceShipDelegation {
    private String name;
    private SpaceShipControls controls = new SpaceShipControls();

    public SpaceShipDelegation(String name) {
        this.name = name;
    }

    // Delegated methods:
    public void back(int velocity) {
        controls.back(velocity);
    }

    public void down(int velocity) {
        controls.down(velocity);
    }

    public void forward(int velocity) {
        controls.forward(velocity);
    }

    public void left(int velocity) {
        controls.left(velocity);
    }

    public void right(int velocity) {
        controls.right(velocity);
    }

    public void turboBoost() {
        controls.turboBoost();
    }

    public void up(int velocity) {
        controls.up(velocity);
    }

    public static void main(String[] args) {
        SpaceShipDelegation protector = new SpaceShipDelegation("NSEA Protector");
        protector.forward(100);
    }
}
```

委托是指当前对象将某项工作交给另一个对象来完成，在 Java 中通常是通过组合实现的。

- 可以选择性暴露功能，而不像继承需要暴露全部父类接口。
- 常用于包装（Wrapper）、代理（Proxy）、适配器（Adapter）、装饰器（Decorator）等设计模式。

## `final` 关键字

### `final` 数据

在 Java 中，常量必须是基本类型，并用 `final` 关键字表示，在定义常量时必须提供一个值。常量有两种类型：

- 一个永远不会改变的**编译时常量**。此时计算可以在编译时进行，这节省了一些运行时开销。
- 在运行时初始化的值，而你不希望它被更改。

一个即是 `static` 又是 `final` 的字段只会分配一块不能改变的存储空间。

对于基本类型，`final` 使其值恒定不变，但对于对象引用，`final` 使其**引用**恒定不变。一旦引用被初始化为一个对象，它就永远不能被更改为指向另一个对象了。但是对象本身是可以修改的。

对 `final` 字段赋值的地方只能发生在两个地方：

- 字段定义处使用表达式进行赋值。
- 在构造器中。

这保证了 `final` 字段在使用前总是被初始化。

可以通过在参数列表中进行声明来创建 `final` 参数。这意味着：

- 对于引用来说，在方法内部不能更改参数引用指向的内容。
- 对于基本类型来说，可以读取这个参数，但不能修改它。

### `final` 方法

创建 `final` 方法的唯一目的是为了明确防止子类重写（Override）该方法。

- 类中任何 `private` 方法都是隐式的 `final`。
- 重写只有在方法是基类接口的一部分时才会发生（如果一个方法是 `private` 的，它就不是基类接口的一部分，即使在子类中创建了具有相同名称的 `public`、`protected` 或包访问权限的方法，它与基类中这个相同名称的方法也没有任何联系）。

### `final` 类

将整个类定义为 `final` 时，就阻止了该类的所有继承。

- `final` 类的字段可以是 `final`，也可以不是，根据个人选择而定。无论类是否定义为 `final`，相同的规则都适用于字段的 `final` 定义。
- 由于 `final` 类禁止继承，它的所有方法都是隐式 `final` 的，因此无法重写它们。

## 初始化及类的加载

每个类的编译代码都存在于自己的单独文件中，只有在需要它的代码的时候才会加载该文件。一般可以认为“类的代码在第一次使用时才加载”。这通常是在构造该类的第一个对象时，但在访问静态字段或静态方法时也会触发加载。尽管没有显式指定 `static` 关键字，但构造器也是一个静态方法，所以准确地说，当一个类的任何静态成员被访问时，都会触发它的加载。

静态初始化也发生在初次使用之时。所有静态对象和静态代码块都在加载时按文本顺序（在类定义中编写它们的顺序）初始化，静态成员只初始化一次。

```java
// reuse/Beetle.java
class Insect {
    private int i = 9;
    protected int j;

    Insect() {
        System.out.println("i = " + i + ", j = " + j);
        j = 39;
    }

    private static int x1 = printInit("static Insect.x1 initialized");

    static int printInit(String s) {
        System.out.println(s);
        return 47;
    }
}

public class Beetle extends Insect {
    private int k = printInit("Beetle.k initialized");

    public Beetle() {
        System.out.println("k = " + k);
        System.out.println("j = " + j);
    }

    private static int x2 = printInit("static Beetle.x2 initialized");

    public static void main(String[] args) {
        System.out.println("Beetle constructor");
        Beetle b = new Beetle();
    }
}
/* Output:
static Insect.x1 initialized
static Beetle.x2 initialized
Beetle constructor
i = 9, j = 0
Beetle.k initialized
k = 47
j = 39
*/
```
