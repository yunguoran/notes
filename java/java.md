# Java

## Concatenate Two Arrays

[Concatenate Two Arrays in Java](https://www.baeldung.com/java-concatenate-arrays).

## Stream

### Peek()

- [Java 8 Streams peek() API](https://www.baeldung.com/java-streams-peek-api).
- This method exists mainly to support debugging, where you want to see the elements as they flow past a certain point in a pipeline.
- `peek()` can be useful in another scenario: when we want to alter the inner state of an element.

```java
Stream<User> userStream = Stream.of(new User("Alice"), new User("Bob"), new User("Chuck"));
userStream.peek(u -> u.setName(u.getName().toLowerCase()))
  .forEach(System.out::println);
```

Alternatively, we could have used map(), but `peek()` is more convenient since we don't want to replace the element.

## Javadoc

- [Introduction to Javadoc](https://www.baeldung.com/javadoc#3-javadoc-at-field-level).
- [Javadoc: @see and @link](https://www.baeldung.com/javadoc-see-vs-link).
- [javadoc](https://docs.oracle.com/en/java/javase/11/tools/javadoc.html).

## Try catch

- [Try with Resources](https://www.baeldung.com/java-try-with-resources).
- [The try-with-resources Statement](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html).

## Libraries

- [Array.sort() in Java8](https://www.geeksforgeeks.org/dual-pivot-quicksort/).
- [Apache Commons Lang 3](https://www.baeldung.com/java-commons-lang-3).

## Cron Expression

### Preface

[What is Cron?](https://en.wikipedia.org/wiki/Cron)

计划任务，是任务在约定的时间执行已经计划好的工作。在 Linux 中，我们经常用到 cron 服务器来完成这项工作。cron 服务器可以根据配置文件约定的时间来执行特定的任务。

Cron 表达式是一个字符串，字符串以 5 或 6 个空格隔开，分为 6 或 7 个域，每一个域代表一个含义，Cron 有如下两种语法格式：

- Seconds Minutes Hours DayOfMonth Month DayOfWeek Year
- Seconds Minutes Hours DayOfMonth Month DayOfWeek

### Cron 表达式的结构

Cron 表达式是一个具有时间含义的字符串，字符串以 5 个空格隔开，分为 6 个域，格式为 x x x x x x。其中 x 是一个域的占位符。单个域有多个取值时，使用半角逗号 `,` 隔开取值。每个域可以是确定的取值，也可以是具有逻辑意义的特殊字符。

### 域取值

下表为Cron表达式中六个域能够取的值以及支持的特殊字符。

| 域 | 是否必需 | 取值范围 | 特殊字符 |
| ------ | ------ | ------ | ------ |
| 秒 Seconds | 是 | [0, 59] | * , - / |
| 分钟 Minutes | 是 | [0, 59] |* , - / |
| 小时 Hours | 是 | [0, 23] | * , - / |
| 日期 DayOfMonth | 是 | [1, 31] |* , - / ? L W |
| 月份 Month | 是 | [1, 12] 或 [JAN, DEC] | * , - / |
| 星期 DayOfWeek | 是 | [1, 7] 或 [MON, SUN]。若使用 [1, 7] 表达方式，1 代表星期一，7 代表星期日。 |* , - / ? L # |
| 年 Year | 否 | 1970+ | - * / |

### 特殊字符

每一个域都使用数字，但还可以出现如下特殊字符，它们的含义是：

- `*`：表示匹配该域的任意值。假如在 Minutes 域使用 `*`, 即表示每分钟都会触发事件。
- `?`：只能用在 DayOfMonth 和 DayOfWeek 两个域。它也匹配域的任意值，但实际不会。因为 DayOfMonth 和 DayOfWeek 会相互影响。例如想在每月的 20 日触发调度，不管 20 日到底是星期几，则只能使用如下写法： `13 13 15 20 * ?,` 其中最后一位只能用 `？`，而不能使用 `*`，如果使用 `*` 表示不管星期几都会触发，实际上并不是这样。
- `-`：表示范围。例如在 Minutes 域使用 `5-20`，表示从 5 分到 20 分钟每分钟触发一次
- `/`：表示起始时间开始触发，然后每隔固定时间触发一次。例如在 Minutes 域使用 `5/20`，则意味着 5 分钟触发一次，而 25，45 等分别触发一次.
- `,`：表示列出枚举值。例如在 Minutes 域使用 `5,20`，则意味着在 5 和 20 分每分钟触发一次。
- `L`：表示最后，只能出现在 DayOfWeek 和 DayOfMonth 域。如果在 DayOfWeek 域使用 `5L`，意味着在最后的一个星期四触发。
- `W`：表示有效工作日(周一到周五)，只能出现在 DayOfMonth 域，系统将在离指定日期的最近的有效工作日触发事件。例如在 DayOfMonth 使用 `5W`，如果 5 日是星期六，则将在最近的工作日：星期五，即 4 日触发。如果 5 日是星期天，则在 6 日(周一)触发；如果 5 日在星期一到星期五中的一天，则就在 5 日触发。另外一点，W 的最近寻找不会跨过月份。
- `LW`：这两个字符可以连用，表示在某个月最后一个工作日，即最后一个星期五。
- `#`：用于确定每个月第几个星期几，只能出现在 DayOfMonth 域。例如 `4#2`，表示某月的第二个星期三。

### 常用例子

- `0 0 2 1 * ? *` 表示在每月的 1 日的凌晨 2 点执行
- `0 15 10 ? * MON-FRI` 表示周一到周五每天上午 10 点 15 执行
- `0 15 10 ? 6L 2002-2006` 表示 2002-2006 年的每个月的最后一个星期五上午 10 点 15 执行
- `0 0 10,14,16 * * ?` 每天上午 10 点、下午 2 点、4 点执行
- `0 0/30 9-17 * * ?` 朝九晚五工作时间内每半小时执行一次
- `0 0 12 ? * WED` 表示每个星期三中午 12 点执行
- `0 0 12 * * ?` 每天中午 12 点执行
- `0 15 10 ? * *` 每天上午 10 点 15 执行
- `0 15 10 * * ?` 每天上午 10 点 15 执行
- `0 15 10 * * ? *` 每天上午10 点 15 执行
- `0 15 10 * * ? 2005` 2005 年的每天上午 10 点 15 执行
- `0 * 14 * * ?` 在每天下午 2 点到下午 2 点 59 期间的每 1 分钟执行一次
- `0 0/5 14 * * ?` 在每天下午 2 点到下午 2 点 55 期间的每 5 分钟执行一次
- `0 0/5 14,18 * * ?` 在每天下午 2 点到 2 点 55 期间和下午 6 点到 6 点 55 期间的每 5 分钟执行一次
- `0 0-5 14 * * ?` 在每天下午 2 点到下午 2 点 5 分期间的每 1 分钟执行一次
- `0 10,44 14 ? 3 WED` 每年三月的星期三的下午 2 点 10 和 2 点 44 执行
- `0 15 10 ? * MON-FRI` 周一至周五的上午 10 点 15 执行
- `0 15 10 15 * ?` 每月 15 日上午 10 点 15 执行
- `0 15 10 L * ?` 每月最后一日的上午 10 点 15 执行
- `0 15 10 ? * 6L` 每月的最后一个星期五上午 10 点 15 执行
- `0 15 10 ? * 6L 2002-2005` 2002 年至 2005 年的每月的最后一个星期五上午 10 点 15 执行
- `0 15 10 ? * 6#3` 每月的第三个星期五上午 10 点 15 执行

note：

- 有些子表达式能包含一些范围或列表。例如：子表达式（天（星期））可以为 `MON-FRI`，`MON，WED，FRI`，`MON-WED,SAT`。
- `*` 字符代表所有可能的值。因此，`*` 在子表达式（月）里表示每个月的含义，`*` 在子表达式（天（星期））表示星期的每一天。
- `/` 字符用来指定数值的增量。例如：在子表达式（分钟）里的 `0/15` 表示从第 0 分钟开始，每 15 分钟在子表达式（分钟）里的 `3/20` 表示从第 3 分钟开始，每 20 分钟（它和 `3，23，43`）的含义一样
- `？` 字符仅被用于天（月）和天（星期）两个子表达式，表示不指定值。当 2 个子表达式其中之一被指定了值以后，为了避免冲突，需要将另一个子表达式的值设为`？`。
- `L` 字符仅被用于天（月）和天（星期）两个子表达式，它是单词 `last` 的缩写。但是它在两个子表达式里的含义是不同的： 在天（月）子表达式中，`L` 表示一个月的最后一天，在天（星期）自表达式中，`L` 表示一个星期的最后一天，也就是 `SAT` 如果在 `L` 前有具体的内容，它就具有其他的含义了。例如：`6L` 表示这个月的倒数第 ６ 天，`FRIL` 表示这个月的最一个星期五 注意在使用 `L` 参数时，不要指定列表或范围，因为这会导致问题。
