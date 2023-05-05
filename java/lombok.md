# Lombok

## Val

- use `val` as the type of a local variable declaration instead of actually writing the type.
- The local variable will be made `final`.
- This feature works on local variables and on foreach loops only, not on fields.
- The initializer expression is required.

Vanilla Java

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ValExample {
  public String example() {
    final ArrayList<String> example = new ArrayList<String>();
    example.add("Hello, World!");
    final String foo = example.get(0);
    return foo.toLowerCase();
  }

  public void example2() {
    final HashMap<Integer, String> map = new HashMap<Integer, String>();
    map.put(0, "zero");
    map.put(5, "five");
    for (final Map.Entry<Integer, String> entry : map.entrySet()) {
      System.out.printf("%d: %s\n", entry.getKey(), entry.getValue());
    }
  }
}
```

With Lombok

```java
import java.util.ArrayList;
import java.util.HashMap;
import lombok.val;

public class ValExample {
  public String example() {
    val example = new ArrayList<String>();
    example.add("Hello, World!");
    val foo = example.get(0);
    return foo.toLowerCase();
  }

  public void example2() {
    val map = new HashMap<Integer, String>();
    map.put(0, "zero");
    map.put(5, "five");
    for (val entry : map.entrySet()) {
      System.out.printf("%d: %s\n", entry.getKey(), entry.getValue());
    }
  }
}
```

Small print

- For compound types, the most common superclass is inferred, not any shared interfaces.
- In ambiguous cases, such as when the initializer expression is null, `java.lang.Object` is inferred.

## Var

`var` works exactly like `val`, except the local variable is not marked as `final`.

## @NonNull

- Use `@NonNull` on a record component, or a parameter of a method or constructor. This will cause to lombok generate a null-check statement for you.

Vanilla Java

```java
public class NonNullExample extends Something {
  private String name;

  public NonNullExample(Person person) {
    super("Hello");
    if (person == null) {
      throw new NullPointerException("person is marked non-null but is null");
    }
    this.name = person.getName();
  }
}
```

With Lombok

```java
import lombok.NonNull;

public class NonNullExample extends Something {
  private String name;

  public NonNullExample(@NonNull Person person) {
    super("Hello");
    this.name = person.getName();
  }
}
```

## @Cleanup

Use `@Cleanup` to ensure a given resource is automatically cleaned up before the code execution path exits your current scope.

Vanilla Java

```java

import java.io.*;

public class CleanupExample {
  public static void main(String[] args) throws IOException {
    InputStream in = new FileInputStream(args[0]);
    try {
      OutputStream out = new FileOutputStream(args[1]);
      try {
        byte[] b = new byte[10000];
        while (true) {
          int r = in.read(b);
          if (r == -1) break;
          out.write(b, 0, r);
        }
      } finally {
        if (out != null) {
          out.close();
        }
      }
    } finally {
      if (in != null) {
        in.close();
      }
    }
  }
}
```

With Lombok

```java
import lombok.Cleanup;
import java.io.*;

public class CleanupExample {
  public static void main(String[] args) throws IOException {
    @Cleanup InputStream in = new FileInputStream(args[0]);
    @Cleanup OutputStream out = new FileOutputStream(args[1]);
    byte[] b = new byte[10000];
    while (true) {
      int r = in.read(b);
      if (r == -1) break;
      out.write(b, 0, r);
    }
  }
}
```

## @Getter and @Setter

- You can annotate any field with `@Getter` and/or `@Setter`, to let lombok generate the default getter/setter automatically.
- You can always manually disable getter/setter generation for any field by using the special `AccessLevel.NONE` access level. This lets you override the behavior of a `@Getter`, `@Setter` or `@Data` annotation on a class.

Vanilla Java

```java
public class GetterSetterExample {

  private int age = 10;
  private String name;

  @Override public String toString() {
    return String.format("%s (age: %d)", name, age);
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  protected void setName(String name) {
    this.name = name;
  }
}
```

With Lombok

```java
import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;

public class GetterSetterExample {

  @Getter @Setter private int age = 10;
  @Setter(AccessLevel.PROTECTED) private String name;

  @Override public String toString() {
    return String.format("%s (age: %d)", name, age);
  }
}
```

## @ToString

Annotating a class with @ToString will cause lombok to generate an implementation of the toString() method.

Vanilla Java

```java
import java.util.Arrays;

public class ToStringExample {
  private static final int STATIC_VAR = 10;
  private String name;
  private Shape shape = new Square(5, 10);
  private String[] tags;
  private int id;

  public String getName() {
    return this.name;
  }

  public static class Square extends Shape {
    private final int width, height;

    public Square(int width, int height) {
      this.width = width;
      this.height = height;
    }

    @Override public String toString() {
      return "Square(super=" + super.toString() + ", width=" + this.width + ", height=" + this.height + ")";
    }
  }

  @Override public String toString() {
    return "ToStringExample(" + this.getName() + ", " + this.shape + ", " + Arrays.deepToString(this.tags) + ")";
  }
}
```

With Lombok

```java

import lombok.ToString;

@ToString
public class ToStringExample {
  private static final int STATIC_VAR = 10;
  private String name;
  private Shape shape = new Square(5, 10);
  private String[] tags;
  @ToString.Exclude private int id;

  public String getName() {
    return this.name;
  }

  @ToString(callSuper=true, includeFieldNames=true)
  public static class Square extends Shape {
    private final int width, height;

    public Square(int width, int height) {
      this.width = width;
      this.height = height;
    }
  }
}
```

## @NoArgsConstructor, @RequiredArgsConstructor and @AllArgsConstructor
