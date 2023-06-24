# 流

- **声明式编程**是一种编程风格，我们说明想要完成什么（what），而不是指明怎么做（how）。
- 内部迭代产生的代码不仅可读性更好，而且更容易利用多处理器。

## Java 8 对流的支持

### 流的创建

- 使用 `Stream.of()`，可以轻松地将一组条目变成一个流。
- 每个 Collection 都可以使用 `stream()` 方法来生成一个流。
- `boxed()` 流操作会自动将基本类型转换为其对应的包装器类型。
- `Stream.generate()` 可以接受任何的 `Supplier<T>`，并生成一个由 T 类型的对象组成的流。
- `Stream.iterate()` 从一个种子开始（第一个参数），然后将其传给第二个参数所引用的方法。其结果被添加到这个流上，并且保存下来作为下一次 `iterate()` 调用的第一个参数。
- Java 8 在 java.util.regex.Pattern 中增加了一个新的方法 `splitAsStream()`，它接受一个字符串序列，并根据我们传入的公式将其分割为一个流。

### 中间操作

- `peek()` 接受的是一个遵循 Consumer() 函数式接口的函数。
- `filter()` 过滤操作只保留符合特定条件的元素。
- `concat()` 会按照参数的顺序将两个流组合到一起。

### Optional 类型

- 空流是通过 `Stream.<String>empty()` 创建的。如果只使用了 `Stream.empty()` 而没有任何上下文信息，那么 Java 不知道它应该是什么类型的，而这种语法解决了该问题。
- 当接收到 Optional 对象时，应首先调用 `isPresent()` 检查其中是否包含元素。如果存在，再使用 `get()` 获取。
- 对于普通的流 `filter()` 而言，如果 Predicate 返回 false，它会将元素从流中删除。但是对于 Optional.filter() 而言，如果 Predicate 返回 false，它不会删除元素，但是会将其转化为 empty。
- Optional.map() 会应用一个函数，但是在 Optional 的情况下，只有当 Optional 不为 empty 时，它才会应用这个映射函数。
- 和 map() 类似，flatMap 会获得非 empty 的 Optional 中的对象，并将其交给映射函数中。它们唯一的区别是 flatMap() 不会将结果包在Optional 当中。

### 终结操作

- `forEach(Consumer)` 被明确设计为可以任何顺序操作元素，这只有在引入 parallel() 操作时才有意义。
- `forEachOrdered(Consumer)` 这个版本确保 forEach 对元素的操作顺序是原始的流的顺序。
- 假设想把我们最终的条目放到一个 TreeSet 中，由此使他们总是有序的。在 Collectors 中没有特定的 `toTreeSet()` 方法，但是可以使用`Collectors.toCollection`，并将任何类型的 Collection 的构造器引用传给它。
