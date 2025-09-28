# 控制流

## 迭代语句

- `Math.random()` 生成一个范围为 `[0, 1)` 的 `double` 值。
- `while` 和 `do while` 的唯一区别是 `do-while` 中的语句至少会执行一次。
- `Character.isLowerCase()` 方法可以判断一个字符是否是小写字母。

### 逗号操作符

`for` 循环中的 `,` 是**逗号操作符**而不是逗号分隔符，这是 Java 中唯一用到逗号操作符的地方。

```java
public class CommaOperator {
    public static void main(String[] args) {
        for (int i = 1, j = i + 10; i < 5; i++, j = i * 2) {
            System.out.println("i = " + i + " j = " + j);
        }
    }
}
```

上述 `for` 语句的 `int` 参数定义包括 i 和 j，在初始化部分可以定义**同一个类型**的任意数量的变量。

## `for-in` 语法

String 类有一个方法 `toCharArray()`，返回值类型为 `char` 数组。

```java
public class ForInString {
    public static void main(String[] args) {
        for (char c : "An African Swallow".toCharArray())
            System.out.print(c + " ");
    }
}
```

## `return`

`return` 关键字有两种用途：

- 它可以指定一个方法的返回值（没有返回值返回的就是 `void`）。
- 还会导致当前方法的退出，并且返回这个值。

如果在一个返回了 `void` 的方法中没有 `return`，那么该方法的结尾处会有一个隐含的 `return`，所以方法里并不一定会有一个 `return` 语句。但是如果你的方法声明了它将返回一个非 void 的值，那就必须确保每一条代码路径都会返回一个值。

## `break` 和 `continue`

- `break` 会直接退出循环，不再执行循环里的剩余部分。
- `continue` 则会停止执行当前的迭代，然后退回循环开始位置执行下一次迭代。
- 有一种无限循环的形式：`for(;;)`，在编译器看来，它与 `while(true)` 无异。使用哪种完全取决于你的编程习惯。

## 臭名昭著的 `goto`

- 标签是以冒号结尾的标识符。
- `break` 和 `continue` 关键字通常只中断当前循环，但若搭配标签一起使用，它们就会中断并跳转到标签所在的地方开始执行。

```java
public class LabeledFor {
    public static void main(String[] args) {
        int i = 0;
        outer:
        // Can't have statements here
        for (; true; ) { // infinite loop
            inner:
            // Can't have statements here
            for (; i < 10; i++) {
                System.out.println("i = " + i);
                if (i == 2) {
                    System.out.println("continue");
                    continue;
                }
                if (i == 3) {
                    System.out.println("break");
                    i++; // Otherwise i never
                    // gets incremented.
                    break;
                }
                if (i == 7) {
                    System.out.println("continue outer");
                    i++; // Otherwise i never
                    // gets incremented.
                    continue outer;
                }
                if (i == 8) {
                    System.out.println("break outer");
                    break outer;
                }
                for (int k = 0; k < 5; k++) {
                    if (k == 3) {
                        System.out.println("continue inner");
                        continue inner;
                    }
                }
            }
        }
        // Can't break or continue to labels here
    }
}
```

上述代码中 `break` 中断了 `for` 循环，而 `for` 循环在执行到末尾之前，它的递增表达式不会执行。

- 普通的 `continue` 会跳到最内层循环的起始处，并继续执行。
- 带标签的 `continue` 会跳到对应标签的位置，并重新进入这个标签后面的循环。
- 普通的 `break` 会跳出循环的底部，也就是跳出当前循环。
- 带标签的 `break` 会跳出标签所指的循环。

在 Java 中使用标签的唯一理由是用到了嵌套循环，而且你需要使用 `break` 或 `continue` 来跳出多层的循环。

## `switch`

`switch` 选择器不但可以使用整数值（包括 `char` 类型），还添加了使用字符串的能力。

### `System.exit()`

```java
System.exit(int status);
```

status 是一个整型参数，称为 退出状态码：

- 0 表示正常退出（success）。
- 非 0 表示异常退出（error）。
    - 比如 1、-1、2 等通常用来区分不同类型的错误。
    - 具体含义需要你自己在程序或文档中定义。

语句效果：

- JVM 会先执行所有已注册的 shutdown hooks（如果有的话）。
- 然后会调用 `finalize()` 的对象不会再被执行。
- 最后强制终止整个进程，JVM 退出。
