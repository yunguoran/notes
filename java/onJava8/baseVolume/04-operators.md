# 操作符

几乎所有操作符都只能操作基本类型（Primitives）。唯一的例外是 `=`、`==` 和 `!=`，它们能操作所有对象。除此以外，String 类型支持 `+` 和 `+=`。

```java
int x = 1, y = 2, z = 3;
int a = x + y - 2/2 + z;
int b = x + (y - 2)/(2 + z);
System.out.println("a = " + a); // a = 5
System.out.println("b = " + b); // b = 1
```

`System.out.println()` 使用了操作符 `+`，这里 `+` 意味着**字符串连接**。此处 a 和 b 经历了从 int 到 string 的类型转换。

## 赋值

- 基本类型的赋值都是直接的。基本类型存储了实际的值，所以在为其赋值的时候，直接将一个地方的内容复制到了另一个地方。
- 当操作一个对象的时候，我们真正操作的是这个对象的引用。所以当一个对象赋值给另一个对象的时候，其实是将对象的引用从一个地方赋值到另一个地方。

    ```java
    class Tank {
        int level;
    }

    public class Test {
        public static void main(String[] args) {
            Tank t1 = new Tank();
            Tank t2 = new Tank();
            t1.level = 9;
            t2.level = 47;
            System.out.println("1: t1.level: " + t1.level + ", t2.level: " + t2.level); // 1: t1.level: 9, t2.level: 47
            t1 = t2;
            System.out.println("2: t1.level: " + t1.level + ", t2.level: " + t2.level); // 2: t1.level: 47, t2.level: 47
            t1.level = 27;
            System.out.println("3: t1.level: " + t1.level + ", t2.level: " + t2.level); // 3: t1.level: 27, t2.level: 27
        }
    }
    ```

## 算数操作符

- Float 类型能保证前 6 位一定是准确的。
- Double 类型能保证前 15 位一定是准确的。

通过创建 `Random` 对象时提供种子，可以在每次执行程序时都生成相同的随机数。

### 一元加减操作符

一元加号的作用是把较小的数值类型自动转换为 int 类型。

## 测试对象是否相等

```java
public class Test {
    public static void main(String[] args) {
        test(127);
        test(128);
    }

    static void show(String desc, Integer n1, Integer n2) {
        System.out.println(desc + ":");
        System.out.printf("%d==%d %b %b%n", n1, n2, n1 == n2, n1.equals(n2));
    }

    @SuppressWarnings("deprecation")
    public static void test(int value) {
        Integer i1 = value; // [1]
        Integer i2 = value;
        show("Automatic", i1, i2);
        // Old way, deprecated since Java 9:
        Integer r1 = new Integer(value); // [2]
        Integer r2 = new Integer(value);
        show("new Integer()", r1, r2);
        // Preferred since Java 9:
        Integer v1 = Integer.valueOf(value); // [3]
        Integer v2 = Integer.valueOf(value);
        show("Integer.valueOf()", v1, v2);
        // Primitives can't use equals():
        int x = value;  // [4]
        int y = value;
        // x.equals(y); // Doesn't compile
        System.out.println("Primitive int:");
        System.out.printf("%d==%d %b%n", x, y, x == y);
    }
}

/* output:
Automatic:
127==127 true true
new Integer():
127==127 false true
Integer.valueOf():
127==127 true true
Primitive int:
127==127 true
Automatic:
128==128 false true
new Integer():
128==128 false true
Integer.valueOf():
128==128 false true
Primitive int:
128==128 true
*/
```

- `System.out.printf()`：按照格式化字符串的规则输出内容。
    - `%d`：输出一个整数。
    - `%b`：输出布尔值。
    - `%n`：输出一个换行符（平台相关，Windows 是 `\r\n`，Linux/Unix 是 `\n`），因此要使用 `%n`，而不是写死 `\n`，这样跨平台更安全。
    - `%e`：以科学计数法显示结果。
    - `%x`：十六进制形式输出整数。
- `Integer i1 = value;` 其实是自动调用了 `Integer.valueOf()` 来完成自动装箱的。
    - 因此 [1] 和 [3] 的结果始终一致。
- `IntegerCache` 是 `java.lang.Integer` 内部用来复用 `Integer` 对象的一个缓存机制，目的是减少频繁创建/回收小整数对象的开销。因此在可能重复出现的小整数范围内，`Integer.valueOf(int)` 会返回缓存里的已有对象，而不是每次都 `new` 一个。
    - 缓存范围是 [-128, 127]。
    - `-XX:AutoBoxCacheMax=4096` 参数可以扩大缓存的上界。
- `float` / `double` 类型的**舍入误差**。
    - 有些十进制小数在二进制中是 无限循环小数（比如 0.1）。存储时只能截断或舍入，导致结果不精确。
    - 当一个非常大的数值减去一个相对较小的数值时，非常的大数值并不会发生明显变化。
- `==` 和 `equals()` 方法。
    - 基本类型：`==` 操作符比较值，不存在 `equals()` 方法。
    - 基本类型的包装类型：`==` 操作符比较引用（可能受缓存池影响），`equals()` 方法比较值。
    - 对象类型：`==` 操作符比较引用，**`equals()` 的默认行为也是比较引用，但大多数标准库会重写 `equals()` 方法来比较对象的内容**。因此自己新建的类必须重写 `equals()` 方法才能比较内容。

## 逻辑操作符

将 `int` 作为布尔处理不是合法的 Java 写法：即 `&&`、`||` 和 `!` 不能用于 int 类型。

## 字面量

Java 里有一套约定来区分不同进制的字面量：

- 二进制（Binary）以 `0b` 或 `0B` 开头。
- 八进制（Octal）以 `0` 开头。
- 十进制（Decimal）
    - `int` 类型直接写。
    - `long` 类型后面加大写的 L（小写 l 也可以，但容易与 1 混淆）。
    - `float` 类型后面加 `F` 或 `f`。
    - `double` 类型后面加 `D` 或 `d`。
- 十六进制 (Hex)：以 `0x` 或 `0X` 开头。

在 Long 型和 Integer 型中调用其静态的 `toBinaryString()` 方法即可。若将较小的类型传递给 `Integer.toBinaryString`() 时，类型将自动转换为 int。

### 八进制和二进制互相转化

1 个八进制位 = 3 个二进制位（8=2^3）。

- 八进制转化为二进制可以把每一位八进制数直接换成对应的 3 位二进制数。
    - 0237 = 0b10011111
    - 0236 = 0b10011110
- 二进制转化为八进制可以从右往左，每 3 位二进制转成一个八进制。
    - 0b1101 = 015
    - 如果二进制位数不是 3 的倍数，可以在左边补零。

### 十六进制和二进制互相转化

1 个十六进制位 = 4 个二进制位（16=2^4）。

- 十六进制转化为二进制可以把每一位十六进制数直接换成对应的 4 位二进制数。
    - 0x2F = 0b00101111
    - 0xA3 = 0b10100011
- 二进制转化为十六进制可以从右往左，每 4 位二进制转成一个十六进制。
    - 0b11010110 = 0xD6
    - 如果二进制位数不是 4 的倍数，可以在左边补零。0b101（0101）= 0x05。

### 字面量里的下划线

可以在数字字面量里面使用下划线，这样更容易阅读，真正计算和打印的时候不会输出或计算下划线。

## 按位操作符

按位操作符用来操作整数基本数据类型中的单个二进制位（bit）。按位操作符会对两个整数中对应的二进制位执行布尔代数运算，并生成一个结果。

- `&`
- `|`
- `^`：按位“异或”操作符。含义是：相同为 0，不同为 1。
- `~`

注意：

- `&=`、`|=` 和 `^=` 都是合法的操作符。
- 布尔类型不能执行按位“非”（大概是为了避免与逻辑操作符`!`混淆）。
- 对于布尔类型，按位操作符和逻辑操作符具有相同的效果，但他们不会“短路”。

## 移位操作符

移位操作符也操纵二进制位，他们只能用来处理基本类型里的**整数类型**。

- 左移位操作符 `<<` 会将其左边的操作数向左移动，移动的位数在操作符右侧指定（低位补 `0`）。
- “有符号”右移位操作符 `>>` 则按照操作符右侧指定的位数将操作符左侧的操作数向右移动。
    - 如果符号为正，则在高位插入 `0`；
    - 如果符号为负，则在高位插入 `1`。
- “无符号”右移位操作符（`>>>`），使用了“零扩展”（zero extension）：无论符号正负，都在高位插入 `0`。

注意：

- 如果对 `char`、`byte` 或者 `short` 类型的数值进行移位运算，在移位操作前它们会被转换为 `int` 类型。
- 对于 `int` 类型，右端的可移位数中只会用到低 `5` 位。
- 对于 `long` 类型，右端的可移位数中只会用到低 `6` 位。
- 移位操作符可以和等号组合使用（`<<=`、`>>=` 或 `>>>=`）。
    - 对 `byte` 或者 `short` 值进行无符号右移位运算，得到的可能不是正确的结果。它们会被提升为 `int` 类型，进行右移操作，然后在被赋值回原来的变量时被截断，这时得到结果是 `-1`。

## 类型转换操作符

- Java 将 `float` 或 `double` 转型为整型值时，总是对该数值执行截尾。
- 如果相对结果进行舍入，就需要使用 `java.lang.Math()` 中的 `round()` 方法。
- 对于 `boolean` 类型，我们只能赋予它 `true` 和 `false` 值，并测试它是真还是假，但不能将 `boolean` 值相加，或对 `boolean` 值执行其他任何运算。
