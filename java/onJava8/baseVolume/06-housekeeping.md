# 初始化和清理

## 区分重载方法

你可以根据参数列表中的参数顺序来区分不同的方法，但这会生成难以维护的代码。

## this 关键字

- 两个相同类型的对象 a 和 b 在调用相同的方法 peel() 时，编译器做了一些底层工作，peel() 方法中第一个参数隐密地传入了一个指向操作对象的引用，这是在内部实现的。
- 如果你在一个类的方法里调用其他该类中的方法，不要使用 this，直接调用即可，this 自动地应用于其他方法上了。

## 在构造器中调用构造器

在一个构造器中，当你给 this 一个参数列表时，它通过最直接的方式显式地调用匹配参数列表的构造器。

## static 的含义

static 方法中不会存在 this。

## 垃圾回收器

- 只要程序没有濒临内存用完的那一刻，对象占用的空间就总也得不到释放。如果程序执行结束，而垃圾回收器一直没有释放你创建的任何对象的内存，则当程序退出时，那些资源会全部交还给操作系统。这个策略是恰当的，因为垃圾回收本身也有开销，要是不使用它，那就不用支付这部分开销了。
- 使用垃圾回收的唯一原因就是为了回收程序不再使用的内存。

## 垃圾回收器如何工作

停止-复制（stop-and-copy）：

- 这需要先暂停程序的运行（不属于后台回收模式），然后将所有存活的对象从当前堆复制到另一个堆，没有复制的就是需要被垃圾回收的。另外，当对象被复制到新堆时，它们是一个挨着一个紧凑排列，然后就可以按照前面描述的那样简单、直接地分配新空间了。
- 当对象从一处复制到另一处，所有指向它的引用都必须修正。位于栈或静态存储区的引用可以直接被修正，但可能还有其他指向这些对象的引用，它们在遍历的过程中才能被找到（可以想象成一个表格，将旧地址映射到新地址）。

这种所谓的“复制回收器”效率低下主要因为两个原因：

- 其一得有两个堆，然后在这两个分离的堆之间来回折腾，得维护比实际需要多一倍的空间。某些 Java 虚拟机对此问题的处理方式是，按需从堆中分配几块较大的内存，复制动作发生在这些大块内存之间。
- 其二在于复制本身。一旦程序进入稳定状态之后，可能只会产生少量垃圾，甚至没有垃圾。尽管如此，复制回收器仍然会将所有内存从一处复制到另一处，这很浪费。为了避免这种状况，一些 Java 虚拟机会进行检查：要是没有新垃圾产生，就会转换到另一种模式（即“自适应”）。这种模式称为标记-清扫（mark-and-sweep），Sun 公司早期版本的 Java 虚拟机一直使用这种技术。对一般用途而言，“标记-清扫”方式速度相当慢，但是当你知道程序只会产生少量垃圾甚至不产生垃圾时，它的速度就很快了

“标记-清扫”所依据的思路仍然是从栈和静态存储区出发，遍历所有的引用，找出所有存活的对象。但是，每当找到一个存活对象，就给对象设一个标记，并不回收它。只有当标记过程完成后，清理动作才开始。在清理过程中，没有标记的对象将被释放，不会发生任何复制动作。“标记-清扫”后剩下的堆空间是不连续的，垃圾回收器要是希望得到连续空间的话，就需要重新整理剩下的对象。

## 初始化的顺序

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

## 静态数据的初始化

无论创建多少个对象，静态数据都只占用一份存储区域。`static` 关键字不能应用于局部变量，所以只能作用于属性（字段、域）。如果一个字段是静态的基本类型，你没有初始化它，那么它就会获得基本类型的标准初值。如果它是对象引用，那么它的默认初值就是 `null`。

如果在定义时进行初始化，那么静态变量看起来就跟非静态变量一样。

```java
// housekeeping/StaticInitialization.java
// Specifying initial values in a class definition

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

初始化的顺序先是静态对象（如果它们之前没有被初始化的话），然后是非静态对象。

创建对象的过程，假设有个名为 Dog 的类：

- 即使没有显式地使用 `static` 关键字，构造器实际上也是静态方法。所以，当首次创建 `Dog` 类型的对象或是首次访问 Dog 类的静态方法或属性时，Java 解释器必须在类路径中查找，以定位 Dog.class。
- 当加载完 Dog.class 后，有关静态初始化的所有动作都会执行。因此，静态初始化只会在首次加载 Class 对象时初始化一次。
- 当用 `new Dog()` 创建对象时，首先会在堆上为 Dog 对象分配足够的存储空间。
- 分配的存储空间首先会被清零，即会将 Dog 对象中的所有基本类型数据设置为默认值（数字会被置为 0，布尔型和字符型也相同），引用被置为 `null`。
- 执行所有出现在字段定义处的初始化动作。
- 执行构造器。
