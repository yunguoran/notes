# 实现隐藏（访问控制）

Python `range()` 函数的 Java 版本。

```java
public class Range {
    // Produce sequence [start..end) incrementing by step
    public static int[] range(int start, int end, int step) {
        if (step == 0)
            throw new IllegalArgumentException("Step cannot be zero");
        int sz = Math.max(0, step >= 0 ? (end - start + step - 1) / step : (end - start + step + 1) / step);
        int[] result = new int[sz];
        for (int i = 0; i < sz; i++)
            result[i] = start + (i * step);
        return result;
    }  // Produce a sequence [start..end)

    public static int[] range(int start, int end) {
        return range(start, end, 1);
    }

    // Produce a sequence [0..n)
    public static int[] range(int n) {
        return range(0, n);
    }
}
```

## `import` 和 `import static`

- `import` 让你在代码中使用某个类时，不用写完整的包名。
- `import static` 让你在代码中直接使用类的静态成员（变量或方法），而不用写类名。

```java
// import
import java.util.ArrayList;

public class Demo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>(); // ✅ 直接用类名
    }
}

// import static 导入静态方法
import static java.lang.Math.*;  // 导入 Math 类的所有静态方法

public class Demo {
    public static void main(String[] args) {
        double r = sqrt(9);    // ✅ 不用写 Math.sqrt
        double a = pow(2, 3);  // ✅ 不用写 Math.pow
    }
}

// import static 导入静态常量
import static java.lang.System.out;

public class Demo {
    public static void main(String[] args) {
        out.println("Hello"); // ✅ 不用写 System.out
    }
}
```

## 访问权限修饰符

### `public`

```java
// hiding/dessert/Cookie.java
package hiding.dessert;

public class Cookie {
    public Cookie() {
        System.out.println("Cookie constructor");
    }

    void bite() {
        System.out.println("bite");
    }
}

// hiding/Dinner.java
import hiding.dessert.Cookie;

public class Dinner {
    public static void main(String[] args) {
        Cookie x = new Cookie();
        // x.bite(); // Can't access
    }
}
/* Output:
Cookie constructor
*/
```

Cookie.java 生成的类文件必须置于名为 `dessert` 的子目录中，该子目录位于 `hiding` 目录下，`hiding` 目录必须位于 CLASSPATH 指定的路径之一里。

### `private`

```java
class Sundae {
    private Sundae() {
    }

    static Sundae makeASundae() {
        return new Sundae();
    }
}

public class IceCream {
    public static void main(String[] args) {
        //- Sundae x = new Sundae();
        Sundae x = Sundae.makeASundae();
    }
}
```

- 上述例子可以控制对象的创建方式，并防止特定的构造器被调用。
- 除非必须要公开底层实现，否则就将字段设为 `private`。
- 仅仅因为一个对象的引用在类中是 `private` 的，并不意味着其他对象不能拥有对同一个对象的 `public` 引用。
    - `private` 限定的是引用，不是对象本身。
    - 同一个对象可以有多个引用，这些引用可以有不同的访问权限。

### `protected`

```java
// hiding/ChocolateChip.java
import hiding.dessert.Cookie;

public class ChocolateChip extends Cookie {
    public ChocolateChip() {
        System.out.println("ChocolateChip constructor");
    }

    public void chomp() {
        //- bite(); // Can't access bite
    }

    public static void main(String[] args) {
        ChocolateChip x = new ChocolateChip();
        x.chomp();
    }
}
/* Output:
Cookie constructor
ChocolateChip constructor
*/

// hiding/cookie2/Cookie.java
package hiding.cookie2;

public class Cookie {
  public Cookie() {
    System.out.println("Cookie constructor");
  }
  protected void bite() {
    System.out.println("bite");
  }
}

// hiding/ChocolateChip2.java
import hiding.cookie2.Cookie;

public class ChocolateChip2 extends Cookie {
    public ChocolateChip2() {
        System.out.println("ChocolateChip2 constructor");
    }

    public void chomp() {
        bite();
    } // Protected method

    public static void main(String[] args) {
        ChocolateChip2 x = new ChocolateChip2();
        x.chomp();
    }
}
/* Output:
Cookie constructor
ChocolateChip2 constructor
bite
*/
```

- 上述代码中的 `ChocolateChip` 类中的 `chomp()` 方法无法访问 `hiding/dessert/Cookie.java` 中 `Cookie` 类的 `bite()` 方法，这是因为此处的 `bite()` 只有包访问权限，且在另一个包中，因此 `chomp()` 无法调用它。
- 上述代码中的 `ChocolateChip2()` 类中的 `chomp()` 方法可以访问 `hiding/cookie2/Cookie.java` 中 `Cookie` 类的 `bite()` 方法，这是因为此处的 `bite()` 有 `protected` 权限，任何继承自 `hiding/cookie2/Cookie.java` 中 `Cookie` 类的子类都可以访问该 `Cookie` 类的 `bite()` 方法。

### 包访问权限和 public 构造器

```java
// hiding/packageaccess/PublicConstructor.java
package hiding.packageaccess;

class PublicConstructor {
  public PublicConstructor() {}
}
```

在包访问权限类中，可以给它一个 `public` 构造器，编译器此时不会报错，但是手动编译此文件时，会看到一个编译器错误消息。

## 接口和实现

将数据和方法包装在类中，并与实现隐藏相结合，称为**封装**（Encapsulation）。

## 类的访问权限

- 每个编译单元（单个文件）都只能有一个 `public` 类，否则会产生编译时错误。
- `public` 类的名称必须与包含编译单元的文件名完全匹配，包括大小写。
- 除内部类外的任何类都不能使用 `private` 和 `protected` 关键字修饰。

```java
// hiding/Lunch.java
class Soup1 {
    private Soup1() {
    }

    public static Soup1 makeSoup() {
        return new Soup1();
    }
}

class Soup2 {
    private Soup2() {
    }

    private static Soup2 ps1 = new Soup2();

    public static Soup2 access() {
        return ps1;
    }

    public void f() {
    }
}

// Only one public class allowed per file:
public class Lunch {
    void testPrivate() {
        // Can't do this! Private constructor:
        //- Soup1 soup = new Soup1();
    }

    void testStatic() {
        Soup1 soup = Soup1.makeSoup();
    }

    void testSingleton() {
        Soup2.access().f();
    }
}
```

## JDK 9 新特性：模块

在 JDK 9 之前，Java 程序会依赖整个 Java 库。这意味着即使最简单的程序也带有大量未使用过的库代码。还有另一个更重要的问题是。尽管包访问似乎提供了有效的隐藏，该类不能在包外使用，但还是可以使用反射来规避这个限制。

JDK 9 最终引入了模块（Module）解决了这两个问题。JDK 9 的 Jigsaw 项目将 JDK 库拆分为 100 多个平台模块。现在使用库组件时，你会仅仅获得该组件的模块及其依赖项，不会有不使用的模块。

```shell
# 显示所有可用的模块
java --list-modules

# 查看模块的具体内容
java --describe-module java.base
```

输出如下：

```text
java.base@11
java.compiler@11
...
```

`@11` 表示正在使用的 JDK 版本，当引用模块时该信息不需要包括在内。
