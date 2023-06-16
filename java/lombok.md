# Lombok

## @NonNull

Use `@NonNull` on a record component, or a parameter of a method or constructor. This will cause to Lombok generate a null-check statement for you.

```java
// With Lombok
import lombok.NonNull;

public class NonNullExample extends Something {

  private String name;

  public NonNullExample(@NonNull Person person) {
    super("Hello");
    this.name = person.getName();
  }
}

// Vanilla Java
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

## @Getter and @Setter

- You can annotate any field with `@Getter` and/or `@Setter` to let Lombok generate the default getter/setter automatically.
- You can also put a `@Getter` and/or `@Setter` annotation on a class. In that case, it's as if you annotate all the non-static fields in that class with the annotation.
- You can always manually disable getter/setter generation for any field by using the special `AccessLevel.NONE` access level. This lets you override the behavior of a `@Getter`, `@Setter` or `@Data` annotation on a class.

```java
// With Lombok
import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;

public class GetterSetterExample {

    @Setter
    @Getter
    private int age = 10;
    @Setter(AccessLevel.PROTECTED)
    private String name;

    @Override
    public String toString() {
        return String.format("%s (age: %d)", name, age);
    }
}

// Vanilla Java
public class GetterSetterExample {

    private int age = 10;
    private String name;

    @Override
    public String toString() {
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

## @NoArgsConstructor

- Lombok `@NoArgsConstructor` will generate a no arguments/default constructor, by default generated constructor will be public.

    ```java
    // With Lombok
    @NoArgsConstructor
    public class NoArgsDemo1 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class NoArgsDemo1 {

        private Long id;
        private String username;
        public NoArgsDemo1() {}
    }
    ```

- You will get a compiler error if class has any non initialized `final` fields. You need to set attribute value `force=true` if you have any non initialized `final` fields and all non initialized `final` fields set to their default values within generated constructor. `static` fields are not initialized within generated constructor for `@NoArgsConstructor`.

    ```java
    // With Lombok
    @NoArgsConstructor(force = true)
    public class NoArgsDemo2 {

        private final Long id;
        private final String username;
        private final double minSalary;
        private final int defaultRole = 1;
        private static boolean status;
    }

    // Vanilla Java
    public class NoArgsDemo2 {

        private final Long id;
        private final String username;
        private final double minSalary;
        private final int defaultRole = 1;
        private static boolean status;

        public NoArgsDemo2() {
            this.id = null;
            this.username = null;
            this.minSalary = 0.0;
        }
    }
    ```

- Like `@AllArgsConstructor` generates check for the non-null fields (fields declared as `@NonNull`), no check is generated for `@NoArgsConstructor`.

    ```java
    // With Lombok
    @NoArgsConstructor
    public class NoArgsDemo3 {

        private Long id;
        @NonNull
        private String username;
    }

    // Vanilla Java
    public class NoArgsDemo3 {

        private Long id;
        @NonNull
        private String username;

        public NoArgsDemo3() {}
    }
    ```

- Lombok generates a `public` no-args constructor by default for the `@NoArgsConstructor`. To generate `private` no-args constructor declare `@NoArgsConstructor(access = AccessLevel.PRIVATE)`. `access` attribute of `@NoArgsConstructor` allows you to change the access modifier of the generated constructor.

    ```java
    // With Lombok
    public class NoArgsDemo4 {

        private Long id;
        private String username;

        private NoArgsDemo4() {}
    }

    // Vanilla Java
    @NoArgsConstructor(access = AccessLevel.PRIVATE)
    public class NoArgsDemo4 {

        private Long id;
        private String username;
    }
    ```

- `@NoArgsConstructor(staticName = "getInstance")` generates a `static` factory method named with **getInstance**, `staticName` attribute of `@NoArgsConstructor` allows us to generates a private no-args constructors and an additional `static` factory method that wraps around the `private` constructor is generated.

    ```java
    // With Lombok
    @NoArgsConstructor(staticName = "getInstance")
    public class NoArgsDemo5 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class NoArgsDemo5 {

        private Long id;
        private String username;

        private NoArgsDemo5() {}

        public static NoArgsDemo5 getInstance() {
            return new NoArgsDemo5();
        }
    }
    ```

- Sometimes you may want to define annotations on top of constructor, for example when you are working with Spring framework or some other third part java libraries, you may need to declare annotations on top of constructor . `onConstructor` attribute of `@AllArgsConstructor` allows us to put annotations on generated all-args constructor.

    ```java
    // Syntax: @NoArgsConstructor(onConstructor_={@AnnotationsGoHere})
    // With Lombok
    @NoArgsConstructor(onConstructor_= @Deprecated )
    public class NoArgsDemo6 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class NoArgsDemo6 {

        private Long id;
        private String username;

        @Deprecated
        public NoArgsDemo6() {}
    }
    ```

## @RequiredArgsConstructor

- Generates a constructor with required arguments. Required arguments are uninitialized `final` fields and fields with constraints such as `@NonNull`. Default access modifier is `public`.

    ```java
    // With Lombok
    @RequiredArgsConstructor
    public class RequiredArgsDemo1 {

        private Long id;
        @NonNull
        private String username;
        @NonNull
        private String email;
        private final boolean status;
    }

    // Vanilla Java
    public class RequiredArgsDemo1 {

        private Long id;
        @NonNull
        private String username;
        @NonNull
        private String email;
        private final boolean status;

        public RequiredArgsDemo1(@NonNull final String username, @NonNull final String email, final boolean status) {
            if (username == null) {
                throw new NullPointerException("username is marked non-null but is null");
            }
            if (email == null) {
                throw new NullPointerException("email is marked non-null but is null");
            }
            this.username = username;
            this.email = email;
            this.status = status;
        }
    }
    ```

- Lombok `@RequiredArgsConstructor` will not generate any argument for following fields:

    - Non-final fields.
    - Initialized `final` fields.
    - `static` fields.
    - Initialized non-null fields.

    ```java
    // With Lombok
    @RequiredArgsConstructor
    public class RequiredArgsDemo2 {

        private Long id;
        @NonNull
        private String username = "anonymous";
        private final int defaultRole = 1;
        private static double minSalary = 10000.00;
    }

    // Vanilla Java
    public class RequiredArgsDemo2 {

        private Long id;
        @NonNull
        private String username = "anonymous";
        private final int defaultRole = 1;
        private static double minSalary = 10000.0;

        public RequiredArgsDemo2() {}
    }
    ```

- Lombok generates a `public` constructor by default for the `@RequiredArgsConstructor`. To generate `private` constructor declare `@RequiredArgsConstructor(access = AccessLevel.PRIVATE)`. `access` attribute of `@RequiredArgsConstructor` allows you to change the access modifier of the generated constructor.

    ```java
    // With Lombok
    @RequiredArgsConstructor(access = AccessLevel.PRIVATE)
    public class RequiredArgsDemo3 {

        private Long id;
        @NonNull
        private String username;
    }

    // Vanilla Java
    public class RequiredArgsDemo3 {

        private Long id;
        @NonNull
        private String username;

        private RequiredArgsDemo3(@NonNull final String username) {
            if (username == null) {
                throw new NullPointerException("username is marked non-null but is null");
            }
            this.username = username;
        }
    }
    ```

- If we would like to create instance using a `static` factory method, `staticName` attribute of `@RequiredArgsConstructor` allows us to generates a private constructor with one argument for each uninitialized final, non-null fields and an additional `static` factory method that wraps around the `private` constructor is generated. Let’s have a look into following example.

    ```java
    // With Lombok
    @RequiredArgsConstructor(staticName = "getInstance")
    public class RequiredArgsDemo4 {

        private Long id;
        @NonNull
        private String username;
        @NonNull
        private String email;
        private final boolean status;

    }

    // Vanilla Java
    public class RequiredArgsDemo4 {

        private Long id;
        @NonNull
        private String username;
        @NonNull
        private String email;
        private final boolean status;

        private RequiredArgsDemo4(@NonNull final String username, @NonNull final String email, final boolean status) {
            if (username == null) {
                throw new NullPointerException("username is marked non-null but is null");
            }
            if (email == null) {
                throw new NullPointerException("email is marked non-null but is null");
            }
            this.username = username;
            this.email = email;
            this.status = status;
        }

        public static RequiredArgsDemo4 getInstance(
            @NonNull final String username,
            @NonNull final String email,
            final boolean status
        ) {
            return new RequiredArgsDemo4(username, email, status);
        }
    }
    ```

- Sometimes you may want to define annotations on top of constructor, for example when you are working with Spring framework or some other third party java libraries, you may need to declare annotations on top of constructor. `onConstructor` attribute of `@RequiredArgsConstructor` allows us to put annotations on generated required-args constructor.

    ```java
    // Syntax: @NoArgsConstructor(onConstructor_={@AnnotationsGohere})
    // With Lombok
    @RequiredArgsConstructor(onConstructor_=@ConstructorProperties({"username"}))
    public class RequiredArgsDemo5 {

        private Long id;
        @NonNull
        private String username;
    }

    // Vanilla Java
    public class RequiredArgsDemo5 {

        private Long id;
        @NonNull
        private String username;

        @ConstructorProperties({"username"})
        public RequiredArgsDemo5(@NonNull final String username) {
            if (username == null) {
                throw new NullPointerException("username is marked non-null but is null");
            }
            this.username = username;
        }
    }
    ```

## @AllArgsConstructor

- Lombok `@AllArgsConstructor` generates a constructor with one parameter for each field in your class, by default generated constructor will be `public`.

    ```java
    // With Lombok
    @AllArgsConstructor
    public class AllArgsDemo1 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class AllArgsDemo1 {

        private Long id;
        private String username;

        public AllArgsDemo1(final Long id, final String username) {
            this.id = id;
            this.username = username;
        }
    }
    ```

- The fields marked with `@NonNull` in your class result in null check on those parameter within generated all-args constructor.

    ```java
    // With Lombok
    @AllArgsConstructor
    public class AllArgsDemo2 {

        private Long id;
        @NonNull
        private String username;
    }

    // Vanilla Java
    public class AllArgsDemo2 {

        private Long id;
        @NonNull
        private String username;

        public AllArgsDemo2(final Long id, @NonNull final String username) {
            if (username == null) {
                throw new NullPointerException("username is marked non-null but is null");
            }
            this.id = id;
            this.username = username;
        }
    }
    ```

- Lombok never generates constructor argument for the `static` fields for `@AllArgsConstructor`.
- For `@AllArgsConstructor` Lombok never generates constructor argument for the `final` fields if they are initialized with value, otherwise an argument will be generated.

    ```java
    // With Lombok
    @AllArgsConstructor
    public class AllArgsDemo3 {

        private Long id;
        private static boolean defaultStatus;
        private final double minSalary = 10000.00;
        private final int defaultRole;
    }

    // Vanilla Java
    public class AllArgsDemo3 {

        private Long id;
        private static boolean defaultStatus;
        private final double minSalary = 10000.00;
        private final int defaultRole;

        public AllArgsDemo3(final Long id, final int defaultRole) {
            this.id = id;
            this.defaultRole = defaultRole;
        }
    }
    ```

- Lombok generates a public all-args constructor by default for the `@AllArgsConstructor`. To generate `private` all-args constructor define `@AllArgsConstructor(access = AccessLevel.PRIVATE)`. `access` attribute of `@AllArgsConstructor` allows you to change the access modifier of the generated constructor.

    ```java
    // With Lombok
    @AllArgsConstructor(access = AccessLevel.PRIVATE)
    public class AllArgsDemo4 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class AllArgsDemo4 {

        private Long id;
        private String username;

        private AllArgsDemo4(final Long id, final String username) {
            this.id = id;
            this.username = username;
        }
    }
    ```

- If we would like to create instance using a `static` factory method, `staticName` attribute of `@AllArgsConstructor` allows us to generates a private all-args constructors and an additional `static` factory method that wraps around the `private` constructor is generated.

    ```java
    // With Lombok
    @AllArgsConstructor(staticName = "getInstance")
    public class AllArgsDemo5 {

        private Long id;
        private String username;

    }

    // Vanilla Java
    public class AllArgsDemo5 {

        private Long id;
        private String username;

        private AllArgsDemo5(final Long id, final String username) {
            this.id = id;
            this.username = username;
        }

        public static AllArgsDemo5 getInstance(final Long id, final String username) {
            return new AllArgsDemo5(id, username);
        }
    }
    ```

- Sometimes you may want to define annotations on top of constructor, for example when you are working with Spring framework or some other third part java libraries, you may need to declare annotations on top of constructor . `onConstructor` attribute of `@AllArgsConstructor` allows us to put annotations on generated all-args constructor.

    ```java
    // Syntax: @AllArgsConstructor(onConstructor_={@AnnotationsGoHere})
    // With Lombok
    @AllArgsConstructor(onConstructor_=@ConstructorProperties({"id", "username"}))
    public class AllArgsDemo6 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class AllArgsDemo6 {

        private Long id;
        private String username;

        @ConstructorProperties({"id", "username"})
        public AllArgsDemo6(final Long id, final String username) {
            this.id = id;
            this.username = username;
        }
    }
    ```

## @Data

- Lombok Data annotation (`@Data`) Generates getters for all fields, a useful toString method, and hashCode and equals implementations that check all non-transient fields. Will also generate setters for all non-final fields, as well as a constructor. A `@Data` annotations Equivalent to  combination of `@Getter` `@Setter` `@RequiredArgsConstructor` `@ToString` `@EqualsAndHashCode`.

    ```java
    // Use other annotation
    @Setter
    @Getter
    @RequiredArgsConstructor
    @ToString
    @EqualsAndHashCode
    public class User1 {

        private Long id;
        private String username;
    }

    // Use @Data annotation
    @Data
    public class User2 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class User1 {

        private Long id;
        private String username;

        public Long getId() {
            return this.id;
        }

        public String getUsername() {
            return this.username;
        }

        public void setId(final Long id) {
            this.id = id;
        }

        public void setUsername(final String username) {
            this.username = username;
        }

        public User1() {}

        @Override
        public String toString() {
            return "User1(id=" + this.getId() + ", username=" + this.getUsername() + ")";
        }

        @Override
        public boolean equals(final Object o) {
            if (o == this)
                return true;
            if (!(o instanceof User1))
                return false;
            final User1 other = (User1) o;
            if (!other.canEqual((Object) this))
                return false;
            final Object this$id = this.getId();
            final Object other$id = other.getId();
            if (this$id == null ? other$id != null : !this$id.equals(other$id))
                return false;
            final Object this$username = this.getUsername();
            final Object other$username = other.getUsername();
            if (this$username == null ? other$username != null : !this$username.equals(other$username))
                return false;
            return true;
        }

        protected boolean canEqual(final Object other) {
            return other instanceof User1;
        }

        @Override
        public int hashCode() {
            final int PRIME = 59;
            int result = 1;
            final Object $id = this.getId();
            result = result * PRIME + ($id == null ? 43 : $id.hashCode());
            final Object $username = this.getUsername();
            result = result * PRIME + ($username == null ? 43 : $username.hashCode());
            return result;
        }
    }
    ```

- `@Data` generates all the boilerplate that is normally associated with simple POJOs and beans:
    - getter methods for all fields.
    - setter methods for all non-final fields.
    - appropriate `toString()`.
    - appropriate `equals()` and `hashCode()` implementations that involve the fields of the class.
    - a constructor that initializes all final fields.
    - all non-final fields with no initializer that have been marked with `@NonNull`, in order to ensure the field is never null.
- If you specify a staticConstructor name, then the generated constructor will be private, a static factory method is created to that other classes can use to create instances.

    ```java
    // With Lombok
    @Data(staticConstructor = "create")
    public class User3 {

        private Long id;
        private String username;
    }

    // Vanilla Java
    public class User3 {

        private Long id;
        private String username;

    private User3() {}

    public static User3 create() {
        return new User3();
    }

        // Rest of code same as delomboked User3.java
    }
    ```

- `@Data` annotation alone not provide support for ignoring fields from generating getters/setters or toString or equals and hashCode methods. Following example demonstrates how to exclude fields when you are using `@Data` annotation.

    ```java
    @Data
    public class User4 {

        @Setter(value = AccessLevel.NONE)
        private Long id;
        @Getter(value = AccessLevel.NONE)
        private String username;

        @ToString.Exclude
        private boolean active;

        @EqualsAndHashCode.Exclude
        @ToString.Exclude
        private int role;
    }
    ```

- If you use `@Data` annotation alone, public required-args constructor is generated. If you are using `@Data` and `@Builder` annotations together, all-args constructor (Package access level) is generated. In case initializing objects is responsible for third party libraries like Spring Framework, most of the cases they look for no-args constructor.Following example demonstrates how you can generate all-args and no-args constructor when you are using `@Data` and `@Builder` together.

    ```java
    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor(access = AccessLevel.PACKAGE)
    public class User5 {

        private Long id;
        private String username;
    }
    ```

## @Builder

- When we annotate a class with `@Builder`, Lombok produces complex builder APIs for your class.

    ```java
    // With Lombok
    @Getter
    @Builder
    public class LombokBuilderDemo1 {

        private Long id;
        private String name;
    }

    // Vanilla Java
    public class LombokBuilderDemo1 {

        private Long id;
        private String name;

        LombokBuilderDemo1(final Long id, final String name) {
            this.id = id;
            this.name = name;
        }


        public static class LombokBuilderDemo1Builder {

            private Long id;
            private String name;

            LombokBuilderDemo1Builder() {}

            public LombokBuilderDemo1.LombokBuilderDemo1Builder id(final Long id) {
                this.id = id;
                return this;
            }

            public LombokBuilderDemo1.LombokBuilderDemo1Builder name(final String name) {
                this.name = name;
                return this;
            }

            public LombokBuilderDemo1 build() {
                return new LombokBuilderDemo1(this.id, this.name);
            }

            @Override
            public String toString() {
                return "LombokBuilderDemo1.LombokBuilderDemo1Builder(id=" + this.id + ", name=" + this.name + ")";
            }
        }

        public static LombokBuilderDemo1.LombokBuilderDemo1Builder builder() {
            return new LombokBuilderDemo1.LombokBuilderDemo1Builder();
        }

    // Getters omitted
    }
    ```

- In the above example `LombokBuilderDemo1Builder` is the builder class and which is used to create instance for your class. If we wants to change the name of builder class, have to declare annotation like `@Builder(builderClassName = "Builder")`.
    - To change `build()` name use buildMethodName attribute like `@Builder(buildMethodName = "create")`.
    - To Change `builder()` name use builderMethodName attribute like `@Builder(builderMethodName = "user")`.
- If not all the fields are required to instantiate your class, if only few of them required then declare `@Builder` annotation at constructor level which is having required arguments.

    ```java
    // With Lombok
    @Getter
    public class LombokBuilderDemo2 {

        private Long id;
        private String name;
        private boolean status;
        private int role;

        @Builder()
        public LombokBuilderDemo2(Long id, int role) {
            this.id = id;
            this.role = role;
        }
    }

    // Vanilla Java
    public class LombokBuilderDemo2 {

        private Long id;
        private String name;
        private boolean status;
        private int role;

        public LombokBuilderDemo2(Long id, int role) {
            this.id = id;
            this.role = role;
        }


        public static class LombokBuilderDemo2Builder {

            private Long id;
            private int role;

            LombokBuilderDemo2Builder() {}

            public LombokBuilderDemo2.LombokBuilderDemo2Builder id(final Long id) {
                this.id = id;
                return this;
            }

            public LombokBuilderDemo2.LombokBuilderDemo2Builder role(final int role) {
                this.role = role;
                return this;
            }

            public LombokBuilderDemo2 build() {
                return new LombokBuilderDemo2(this.id, this.role);
            }

            @Override
            public String toString() {
                return "LombokBuilderDemo2.LombokBuilderDemo2Builder(id=" + this.id + ", role=" + this.role + ")";
            }
        }

        public static LombokBuilderDemo2.LombokBuilderDemo2Builder builder() {
            return new LombokBuilderDemo2.LombokBuilderDemo2Builder();
        }

    // Getters omitted
    }
    ```

- If your class already have a method to create instance, you can make it as builder by declaring `@Builder` on that method.

    ```java
    public class LombokBuilderDemo3 {

        private Long id;
        private String name;
        private boolean status;
        private int role;

        public LombokBuilderDemo3(Long id, String name, int role, boolean status) {
            this.id = id;
            this.name = name;
        }

        public static LombokBuilderDemo3 createInstance(Long id, String name) {
            // create instance with default role and status
            return new LombokBuilderDemo3(id, name, 1, false);
        }


        public static class MyBuilder {

            private Long id;
            private String name;

            MyBuilder() {}

            public LombokBuilderDemo3.MyBuilder id(final Long id) {
                this.id = id;
                return this;
            }

            public LombokBuilderDemo3.MyBuilder name(final String name) {
                this.name = name;
                return this;
            }

            public LombokBuilderDemo3 build() {
                return LombokBuilderDemo3.createInstance(this.id, this.name);
            }

            @Override
            public String toString() {
                return "LombokBuilderDemo3.MyBuilder(id=" + this.id + ", name=" + this.name + ")";
            }
        }

        public static LombokBuilderDemo3.MyBuilder builder() {
            return new LombokBuilderDemo3.MyBuilder();
        }

    // Getters omitted
    }
    ```

## @SneakyThrows

`@SneakyThrows` can be used to sneakily throw checked exceptions without actually declaring this in your method's throws clause.

```java
// With Lombok
import lombok.SneakyThrows;

public class SneakyThrowsExample implements Runnable {

    @SneakyThrows(UnsupportedEncodingException.class)
    public String utf8ToString(byte[] bytes) {
        return new String(bytes, "UTF-8");
    }

    @SneakyThrows
    public void run() {
        throw new Throwable();
    }
}

// Vanilla Java
import lombok.Lombok;

public class SneakyThrowsExample implements Runnable {
  public String utf8ToString(byte[] bytes) {
    try {
      return new String(bytes, "UTF-8");
    } catch (UnsupportedEncodingException e) {
      throw Lombok.sneakyThrow(e);
    }
  }

  public void run() {
    try {
      throw new Throwable();
    } catch (Throwable t) {
      throw Lombok.sneakyThrow(t);
    }
  }
}
```

## Val

- use `val` as the type of a local variable declaration instead of actually writing the type.
- The local variable will be made `final`.
- This feature works on local variables and on foreach loops only, not on fields.
- The initializer expression is required.

```java
// Vanilla Java
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

```java
// With Lombok
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

## @Cleanup

Use `@Cleanup` to ensure a given resource is automatically cleaned up before the code execution path exits your current scope.

```java
// Vanilla Java
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

// With Lombok
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

## @ToString

Annotating a class with `@ToString` will cause Lombok to generate an implementation of the toString() method.

```java
// Vanilla Java
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

// With Lombok
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
