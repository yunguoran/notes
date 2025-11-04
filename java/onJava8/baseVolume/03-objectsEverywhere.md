# 万物皆对象

## 对象操纵

```java
String s = "asdf";
String s = new String("asdf");
```

- `String s = "asdf";`：
    - "asdf" 这个字面量会被放入字符串常量池。
    - 如果常量池中已经存在 "asdf"，则 s1 会直接指向那个已有的对象；如果没有，就会在常量池中新建一个，然后让 s1 指向它。
    - 优点是节省内存，提高效率。
- `String s = new String("asdf");`
    - `new` 关键字 总是在**堆**上创建一个新对象，即使常量池中已经有 "asdf"。
    - JVM 先在常量池里确认 "asdf" 是否存在（如果不存在，就先放进去）。
    - 在堆内存中再创建一个新的 String 对象，并把内容复制一份。
    - 所以此处 s2 指向的是一个堆里的新对象，而不是常量池里的对象。

## 数据存储

- **寄存器**（Registers）是最快的存储区域，位于 CPU 内部。然而，寄存器的数量十分有限，所以寄存器根据需求进行分配。我们对其没有直接的控制权，也无法在自己的程序里找到寄存器存在的踪迹。
- **栈**（Stack）存在于常规内存 RAM 区域中，可通过**栈指针**获得处理器的直接支持。栈指针下移分配内存，上移释放内存。这是一种仅次于寄存器的非常快速有效的分配存储方式。创建程序时，Java 系统必须知道栈内保存的所有项的生命周期。这种约束限制了程序的灵活性。**对象引用保存在栈内存上**。
- **堆**（Heap）这是一种通用的内存池（也在 RAM 区域），**所有 Java 对象都存在于堆上**。与栈内存不同，编译器不需要知道对象必须在堆内存上停留多长时间。因此，用堆内存保存数据更具灵活性。创建一个对象时，只需用 `new` 命令实例化对象即可，当执行代码时，会自动在堆中进行内存分配。这种灵活性是有代价的：分配和清理堆内存要比栈内存需要更多的时间（如果可以用 Java 在栈内存上创建对象，就像在 C++ 中那样的话）。随着时间的推移，Java 的堆内存分配机制现在已经非常快，因此这不是一个值得关心的问题了。
- **常量存储**（Constant Storage）常量值通常直接放在程序代码中，因为它们永远不会改变。如需严格保护，可考虑将它们置于只读存储器 ROM 中，一个例子是**字符串常量池**：所有文字字符串和字符串值常量表达式都会自动被自动放置到这个特殊的存储空间中。
- **非 RAM 存储**（Non-RAM storage）数据完全存在于程序之外，在程序未运行以及脱离程序控制后依然存在。这些存储的方式都是将对象转存于另一个介质中，并在需要时恢复成常规的、基于 RAM 的对象。Java 为轻量级持久化提供了支持。而诸如 JDBC 和 Hibernate 这些类库为使用数据库存储和检索对象信息提供了更复杂的支持。两个主要的例子：
    - 序列化对象：对象被转换为字节流，通常被发送到另一台机器；
    - 持久化对象：对象被放置在磁盘或数据库上，即使程序终止，数据依然存在。

## 基本类型

`new` 关键字是在堆上创建对象，这就意味着哪怕是创建一些简单的变量也不会很高效。因此**基本类型的值直接存在栈上。**

Java 有 8 种基本类型（此处注意 `char` 在语义上被归为字符类型，但实际存储的是无符号整数，范围 `0~65535`）：

<!-- markdownlint-disable -->
<table border="1" cellspacing="0" cellpadding="6">
  <thead>
    <tr>
      <th>分类</th>
      <th>基本类型</th>
      <th>初始值</th>
      <th>占用空间大小</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>布尔</td>
      <td>boolean</td>
      <td>false</td>
      <td>-</td>
    </tr>
    <tr>
      <td>字符</td>
      <td>char</td>
      <td>\u0000 (null)</td>
      <td>16bit</td>
    </tr>
    <tr>
      <td rowspan="4">整数</td>
      <td>byte</td>
      <td>(byte) 0</td>
      <td>8bit</td>
    </tr>
    <tr>
      <td>short</td>
      <td>(short) 0</td>
      <td>16bit</td>
    </tr>
    <tr>
      <td>int</td>
      <td>0</td>
      <td>32bit</td>
    </tr>
    <tr>
      <td>long</td>
      <td>0L</td>
      <td>64bit</td>
    </tr>
    <tr>
      <td rowspan="2">浮点数</td>
      <td>float</td>
      <td>0.0f</td>
      <td>32bit</td>
    </tr>
    <tr>
      <td>double</td>
      <td>0.0d</td>
      <td>64bit</td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-enable -->

当一个类的字段是基本类型时，即使你没有初始化这些字段，它们也会拥有默认值。局部变量没有默认值。

基本类型有自己对应的包装类型，如果你希望在堆内存里表示基本类型的数据，就需要用到它们的包装类。

```java
char c = 'x';
Character ch = new Character(c);
Character ch = new Character('x');

// 基本类型自动转换成包装类型（自动装箱）
Character ch = 'x';

// 包装类型转化为基本类型（自动拆箱）
char c = ch;
```

Java 对部分包装类做了**对象缓存**，为了节省内存。

- `Integer.valueOf(int)` 会缓存 [-128, 127] 范围的整数。
- 这意味着虽然包装类在堆里，但有时候会被缓存池复用。

    ```java
    Integer x = Integer.valueOf(127);
    Integer y = Integer.valueOf(127);
    System.out.println(x == y); // true (指向缓存池同一个对象)

    Integer m = Integer.valueOf(128);
    Integer n = Integer.valueOf(128);
    System.out.println(m == n); // false (堆上不同对象)
    ```

### 高精度数值

在 Java 中有两种类型的数据可用于高精度的计算，它们是 `BigInteger` 和 `BigDecimal`。

- `BigInteger` 支持任意精度的整数。可用于精确表示任意大小的整数值，同时在运算过程中不会丢失精度。
- `BigDecimal` 支持任意精度的定点数字。例如：可用它进行精确的货币计算。

## 注释

- 单行注释：`//`
- 多行注释：`/* */`

## 方法、参数以及返回值

- 方法名和参数列表统称为方法签名（Signature），签名是方法的唯一标识。
- 当返回类型为 `void` 时， `return` 关键字仅用于退出方法，因此在方法结束处的 `return` 可被省略。我们可以随时从方法中返回。

    ```java
    // 该方法计算并返回了保存指定字符串所需的字节数。
    // 字符串的每一个 char 的长度是 16bit 也就是 2 个字节。
    int storage(String s) {
        return s.length() * 2
    }
    ```

## 编写 Java 程序

每个独立的程序应该包含一个 `main()` 方法作为程序运行的入口。

```java
public static void main(String[] args) {
}
```

- 关键字 `public` 表示方法可以被外界访问到。
- `main()` 方法的参数是一个 字符串（String）数组。 参数 `args` 并没有在当前的程序中使用到，但是 Java 编译器强制要求必须要有，这是因为它们被用于接收从命令行输入的参数。
- Java 的包名是全小写的。

打印系统属性：

```java
public class ShowProperties {
    public static void main(String[] args) {
        System.getProperties().list(System.out);
        System.out.println(System.getProperty("user.name"));
        System.out.println(System.getProperty("java.library.path"));
    }
}
```
