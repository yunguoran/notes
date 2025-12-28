# 多态

## 向上转型

获取对象引用并将其当作基类类型的引用，称为**向上转型**。

```java
// polymorphism/music/Note.java
package music;

public enum Note {
    MIDDLE_C, C_SHARP, B_FLAT; // Etc.
}

// polymorphism/music/Instrument.java
package music;

class Instrument {
    public void play(Note n) {
        System.out.println("Instrument.play()");
    }
}

// polymorphism/music/Wind.java
package music;

// Wind objects are instruments
// because they have the same interface:
public class Wind extends Instrument {
    // Redefine interface method:
    @Override
    public void play(Note n) {
        System.out.println("Wind.play() " + n);
    }
}

// polymorphism/music/Music.java
package music;

public class Music {
    public static void tune(Instrument i) {
        i.play(Note.MIDDLE_C);
    }

    public static void main(String[] args) {
        Wind flute = new Wind();
        tune(flute); // Upcasting
    }
}
/* Output:
Wind.play() MIDDLE_C
*/
```

## 难点

### 方法调用绑定

将一个方法调用和一个方法体关联起来的动作称为**绑定**。在程序运行之前执行绑定（如果存在编译器和连接器的话，由他们来实现），称为**前期绑定**，在面向过程语言中默认就是前期绑定的。在 C 语言中只有一种方法调用，那就是前期绑定。

**后期绑定**也称为动态绑定或运行时绑定，这意味着绑定发生在运行时并基于对象的类型。在 Java 中，所有方法绑定都是后期绑定，除非方法是 `static` 或 `final` 的（`private` 方法隐式为 `final`）。

### 产生正确热行为

一旦知道了 Java 中所有的方法绑定都是后期绑定，并以多态的方式发生，你就可以编写只与基类打交道的代码了，并且知道所有的子类都可以使用这个相同的代码来正确工作。

### 可扩展性

```java
// polymorphism/music3/Music3.java
package music3;

import music.Note;

class Instrument {
    void play(Note n) {
        System.out.println("Instrument.play() " + n);
    }

    String what() {
        return "Instrument";
    }

    void adjust() {
        System.out.println("Adjusting Instrument");
    }
}

class Wind extends Instrument {
    @Override
    void play(Note n) {
        System.out.println("Wind.play() " + n);
    }

    @Override
    String what() {
        return "Wind";
    }

    @Override
    void adjust() {
        System.out.println("Adjusting Wind");
    }
}

class Percussion extends Instrument {
    @Override
    void play(Note n) {
        System.out.println("Percussion.play() " + n);
    }

    @Override
    String what() {
        return "Percussion";
    }

    @Override
    void adjust() {
        System.out.println("Adjusting Percussion");
    }
}

class Stringed extends Instrument {
    @Override
    void play(Note n) {
        System.out.println("Stringed.play() " + n);
    }

    @Override
    String what() {
        return "Stringed";
    }

    @Override
    void adjust() {
        System.out.println("Adjusting Stringed");
    }
}

class Brass extends Wind {
    @Override
    void play(Note n) {
        System.out.println("Brass.play() " + n);
    }

    @Override
    void adjust() {
        System.out.println("Adjusting Brass");
    }
}

class Woodwind extends Wind {
    @Override
    void play(Note n) {
        System.out.println("Woodwind.play() " + n);
    }

    @Override
    String what() {
        return "Woodwind";
    }
}

public class Music3 {
    // Doesn't care about type, so new types
    // added to the system still work right:
    public static void tune(Instrument i) {
        // ...
        i.play(Note.MIDDLE_C);
    }

    public static void tuneAll(Instrument[] e) {
        for (Instrument i : e)
            tune(i);
    }

    public static void main(String[] args) {
        // Upcasting during addition to the array:
        Instrument[] orchestra = {
            new Wind(),
            new Percussion(),
            new Stringed(),
            new Brass(),
            new Woodwind()
        };
        tuneAll(orchestra);
    }
}
/* Output:
Wind.play() MIDDLE_C
Percussion.play() MIDDLE_C
Stringed.play() MIDDLE_C
Brass.play() MIDDLE_C
Woodwind.play() MIDDLE_C
*/
```

上述所有这些新类都可以与旧的未修改过的 `tune()` 方法一起正常工作。即使 `tune()` 在一个单独的文件中并且有新方法被添加到 `Instrument` 的接口里，`tune()` 仍然可以正常工作，**甚至不重新编译也可以。**

`tune()` 方法完全不了解周围发生的任何代码变更，但它仍然可以正常工作。这正是多态应该提供的。更改代码不会对程序不该受到影响的部分造成破坏。换句话说，多态是程序员“将变化的事物与不变的事物分离”的一项重要技术。

### 陷阱：“重写” `private` 方法

```java
// polymorphism/PrivateOverride.java
public class PrivateOverride {
    private void f() {
        System.out.println("private f()");
    }

    public static void main(String[] args) {
        PrivateOverride po = new Derived();
        po.f();
    }
}

class Derived extends PrivateOverride {
    public void f() {
        System.out.println("public f()");
    }
}
/* Output:
private f()
*/
```

这段代码中 `Derived` 的 `f()` 永远不会被调用。`Derived` 中的 `f()` 不是重写，而是一个全新的方法。方法是否动态绑定，取决于是否可被重写，`private` 方法不能被重写（Override），因此此处是静态绑定。多态只对“可重写的方法”生效，因此 `private` 方法天生排除在多态机制之外。

```java
// polymorphism/PrivateOverride2.java
public class PrivateOverride2 {
    private void f() {
        System.out.println("private f()");
    }

    public static void main(String[] args) {
        PrivateOverride2 po = new Derived2();
        po.f();
    }
}

class Derived2 extends PrivateOverride2 {
    @Override
    public void f() {
        System.out.println("public f()");
    }
}
```

如果使用了 `@override` 注解，那么这个问题就会被检测出来。编译器会提示如下错误信息：

```text
Method does not override method from its superclass
```

### 陷阱：字段与静态方法

只有普通的方法调用可以是多态的，如果直接访问一个字段则该访问会在编译时解析。

```java
// polymorphism/FieldAccess.java
class Super {
    public int field = 0;

    public int getField() {
        return field;
    }
}

class Sub extends Super {
    public int field = 1;

    @Override
    public int getField() {
        return field;
    }

    public int getSuperField() {
        return super.field;
    }
}

public class FieldAccess {
    public static void main(String[] args) {
        Super sup = new Sub(); // Upcast
        System.out.println("sup.field = " + sup.field + ", sup.getField() = " + sup.getField());
        Sub sub = new Sub();
        System.out.println(
            "sub.field = " + sub.field
            + ", sub.getField() = " + sub.getField()
            + ", sub.getSuperField() = " + sub.getSuperField()
        );
    }
}
/* Output:
sup.field = 0, sup.getField() = 1
sub.field = 1, sub.getField() = 1, sub.getSuperField() = 0
*/
```

当 `Sub` 对象向上转型为 `Super` 引用时，任何字段访问都会被编译器解析，因此不是多态的。在此示例中，`Super.field` 和 `Sub.field` 被分配了不同的存储空间。因此，`Sub` 实际上包含两个被称为 `field` 的字段：它自己的字段和它从 `Super` 继承的字段。然而，当你在 `Sub` 中引用 `field` 的时，`Super` 版本并不是默认的那个。要获得 `Super` 的 `field`，必须明确地说 `super.field`。

尽管这看起来令人困惑，但在实践中几乎不会遇到这种情况。一方面我们通常会将所有字段设为 `private`，因此不会直接访问它们，而只会作为调用方法的副作用。另一方面，我们一般不会为基类字段和子类字段指定相同的名称，因为这会造成混淆。

如果一个方法是静态的，那它的行为就不会是多态的：

```java
// polymorphism/StaticPolymorphism.java
class StaticSuper {
    public static String staticGet() {
        return "Base staticGet()";
    }

    public String dynamicGet() {
        return "Base dynamicGet()";
    }
}

class StaticSub extends StaticSuper {
    public static String staticGet() {
        return "Derived staticGet()";
    }

    @Override
    public String dynamicGet() {
        return "Derived dynamicGet()";
    }
}

public class StaticPolymorphism {
    public static void main(String[] args) {
        StaticSuper sup = new StaticSub(); // Upcast
        System.out.println(StaticSuper.staticGet());
        System.out.println(sup.dynamicGet());
    }
}
/* Output:
Base staticGet()
Derived dynamicGet()
*/
```

静态方法与类相关联，而不是与单个对象相关联。

## 构造器和多态

```java
// polymorphism/Sandwich.java
class Meal {
    Meal() {
        System.out.println("Meal()");
    }
}

class Bread {
    Bread() {
        System.out.println("Bread()");
    }
}

class Cheese {
    Cheese() {
        System.out.println("Cheese()");
    }
}

class Lettuce {
    Lettuce() {
        System.out.println("Lettuce()");
    }
}

class Lunch extends Meal {
    Lunch() {
        System.out.println("Lunch()");
    }
}

class PortableLunch extends Lunch {
    PortableLunch() {
        System.out.println("PortableLunch()");
    }
}

public class Sandwich extends PortableLunch {
    private Bread b = new Bread();
    private Cheese c = new Cheese();
    private Lettuce l = new Lettuce();

    public Sandwich() {
        System.out.println("Sandwich()");
    }

    public static void main(String[] args) {
        new Sandwich();
    }
}
/* Output:
Meal()
Lunch()
PortableLunch()
Bread()
Cheese()
Lettuce()
Sandwich()
*/
```

复杂对象的构造器调用顺序：

- 递归地寻找基类的构造器，一直到构造层次结构的根。
- 按声明的顺序来初始化根类的成员。
- 执行根类的构造方法。
- 然后是下一个子类，以此类推（指按先声明的顺序来初始化类成员，然后再执行构造方法），直到最底层的子类。

### 构造器内部的多态方法行为

原则：永远不要在构造器中调用可被重写的方法。

```java
// polymorphism/PolyConstructors.java
class Glyph {
    void draw() {
        System.out.println("Glyph.draw()");
    }

    Glyph() {
        System.out.println("Glyph() before draw()");
        draw();
        System.out.println("Glyph() after draw()");
    }
}

class RoundGlyph extends Glyph {
    private int radius = 1;

    RoundGlyph(int r) {
        radius = r;
        System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
    }

    @Override
    void draw() {
        System.out.println("RoundGlyph.draw(), radius = " + radius);
    }
}

public class PolyConstructors {
    public static void main(String[] args) {
        new RoundGlyph(5);
    }
}
/* Output:
Glyph() before draw()
RoundGlyph.draw(), radius = 0
Glyph() after draw()
RoundGlyph.RoundGlyph(), radius = 5
*/
```

本例的初始化过程：

- `new RoundGlyph(5)` 开始，此处 `Glyph` 类没有实例变量，因此直接执行其构造器。
- 控制台打印 `Glyph() before draw()`。
- 在父类构造器执行期间，子类对象尚未完成初始化，但多态已经生效。此处构造器属于父类，但 `this` 永远指向正在创建的那个对象，而不是当前类。因此此处会调用子类的 `draw()` 方法，此时子类字段尚未初始化，因此控制台打印 `RoundGlyph.draw(), radius = 0`。
- 控制台打印 `Glyph() after draw()`。
- 执行子类字段初始化，此时 `radius = 1`。
- 执行子类构造器，此时 `radius = 5`，控制台打印 `RoundGlyph.RoundGlyph(), radius = 5`。

## 协变返回类型

**协变返回类型**表示子类中重写方法的返回值可以是基类方法返回值的**子类型**。
