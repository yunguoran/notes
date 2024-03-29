# Regex

## 入门

- 正则表达式的两种用途：搜索和替换。
- 相等（equality）测试本质上也是搜索操作。
- 正则表达式是一些用来匹配和处理文本的字符串。

## 匹配单个字符

- [Rich Text vs. Plain Text: What's the Difference?](https://www.indeed.com/career-advice/career-development/rich-text-vs-plain-text)
- 绝大多数正则表达式的实现都提供了一种能够获得所有匹配结果结果的机制，比如说，在 JavaScript 里，可选的 g（global）标志将返回一个包含所有匹配结果的数组。
- `.` 可以匹配任意单个字符、字母、数字，甚至是 `.` 字符本身。
- 用术语**模式**（pattern）表示实际的正则表达式。
- `.` 字符在正则表达式中有特殊的含义。如果模式里需要一个 `.`，就要想办法老告诉正则表达式你需要的是 `.` 字符本身而不是它在正则表达式里的特殊含义。为此需要在 `.` 前面加上一个 `\` 来对它进行转义。
- `\` 是一个**元字符**（metacharacter），表示这个字符有特殊含义，代表的不是字符本身。因此 `.` 表示匹配任意单个字符，`\.` 表示匹配 `.` 字符本身。如果需要搜索 `\` 本身，就必须对 `\` 字符进行转义。即 `\\`。
- 注意 `.` 未必可以匹配所有字符，在大多数的正则表达式实现里，`.` 不能匹配换行符（\n）。

```regex
c.t
sales.
.a.
.a..
.a.\.
.a.\.xls
```

## 匹配一组字符

- 使用 `[` 和 `]` 来定义一个字符集合。在使用 `[` 和 `]` 定义的字符集合里，出现在 `[` 和 `]` 之间的所有字符都是该集合的组成部分，必须匹配其中某个成员。
- 可以用 `-`（hyphen）来定义字符区间。
- 字符区间的首、尾字符可以是 ASCII 字符表里的任意字符。
- `-` 只有出现在 `[` 和 `]` 之间的时候才是元字符。在字符集合以外的地方，`-` 只是一个普通字符，只能与 `-` 本身相匹配。因此 `-` 不需要被转义。
- 使用 `^` 来排除某个字符集合。`^` 的效果将作用于给定字符集合里的所有字符或字符区间，而不是仅限于紧跟在 `^` 字符后面的那一个字符或字符区间。

```regex
[ns]a.\.xls
[Rr]eg[Ee]x
[ns]a[0-9]\.xls
#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]
[ns]a[^0-9]\.xls
```

## 使用元字符

### 匹配特定字符

- `\d` 匹配任何一个数字字符（等价于 `[0-9]` ）。
- `\D` 匹配任何一个非数字字符（等价于 `[^0-9]` ）。
- `\w` 匹配任何一个字母数字字符或下划线字符（等价于 `[a-zA-Z0-9_]` ）。
- `\W` 匹配任何一个非字母数字字符或非下划线字符（等价于 `[^a-zA-Z0-9_]` ）。
- `\s` 匹配任何一个空白字符（等价于 `[\f\n\r\t\v]` ）。
- `\S` 匹配任何一个非空白字符（等价于 `[^\f\n\r\t\v]` ）。

`\r\n` 匹配一个回车和换行的组合，Windows 把这个组合用作文本行的结束标记。因此，搜索 `\r\n` 将匹配两个连续的行尾标记，这正是两条记录的空白行。

`\s` 不包含退格符 `[\b]`，`\S` 也没有排除 `[\b]`。

```regex
myArray\[[0-9]\]
\r\n\r\n
myArray\[\d\]
\w\d\w\d\w\d
```

### 匹配十六进制或八进制数值

- 十六进制的值要用前缀 `\x` 来给出。
- 八进制的值要用前缀 `\0` 来给出。

### 使用 POSIX 字符类

[A Guide to POSIX](https://www.baeldung.com/linux/posix).

| 字符类 | 说明 |
| ------ | ------ |
| [:alnum:] | 任何一个字母或数字（等价于 [a-zA-Z0-9] ） |
| [:alpha:] | 任何一个字母（等价于 [a-zA-Z] ） |
| [:blank:] | 空格或制表符（等价于 [\t ] ） |
| [:cntrl:] | [ASCII](https://en.wikipedia.org/wiki/ASCII) 控制字符（ASCII 0 到 31，再加上 ASCII 127） |
| [:digit:] | 任何一个数字（等价于 [0-9]） |
| [:graph:] | 和 [:print:] 一样，但不包括空格 |
| [:lower:] | 任何一个小写字母（等价于 [a-z]） |
| [:print:] | 任何一个可打印字符 |
| [:punct:] | 既不属于 [:alnum:]，也不属于 [:cntrl:] 的任何一个字符 |
| [:space:] | 任何一个空白字符，包括空格（等价于 [\f\n\r\t\v ]） |
| [:upper:] | 任何一个大写字母，等价于 [A-Z] |
| [:xdigit:] | 十六进制数字（等价于 [a-fA-F0-9]） |

- JavaScript 不支持在正则表达式里使用 POSIX 字符类；
- POSIX 字符类必须出现在 `[:` 和 `:]` 之间。

## 重复匹配

- `+` 匹配某个字符或字符集合的一次或多次出现；
- `*` 匹配某个字符或字符集合的零次或多次出现；
- `?` 匹配某个字符或字符集合的零次或一次出现。
- 想要设置具体的匹配次数，把数字写在 `{` 和 `}` 之间即可。
- `{}` 语法还可以用来为重复匹配次数设定一个区间范围，即 `{2,4}` 这样的形式。
- 不指定最大匹配次数，`{3,}` 表示至少重复 3 次。

```regex
\w+@\w+.\w+
[\w.]+@[\w.]+\.\w+
\w+[\w.]*@[\w.]+\.\w+
https?:\/\/[\w.\/]+
[\r]?\n[\r]?\n
#[A-Fa-f0-9]{6}
\d{1,2}[-\/]\d{1,2}[-\/]\d{2,4}
\d+: \$\d{3,}\.\d{2}
```

注意：

- 当在字符集合里使用元字符的时候，像 `.` 和 `+` 这样的元字符将被解释为普通字符，不需要被转义；
- 在需要匹配 `/` 字符本身的时候，最好总是是用它的转义序列。

### 防止过度匹配

```regex
<[Bb]>.*<\/[Bb]>
<[Bb]>.*?<\/[Bb]>
```

- `*` 和 `+` 都是贪婪型的元字符，其匹配行为是多多益善而不是适可而止；
- 懒惰型版本的量词会匹配尽可能少的字符，而非尽可能多的去匹配，懒惰型量词的写法是在贪婪型量词后面加上一个 `?`。

## 位置匹配

- `\b` 指定单词边界，用来匹配一个单词的开头或结尾；
- `\b` 匹配的是一个位置，而不是任何实际的字符。因此 `\bcat\b` 匹配到的字符串的长度是 3 个字符，而不是 5 个。
- `\B` 匹配非单词边界。
- `^` 代表字符串开头，`$` 代表字符串结尾。

注意：有些元字符拥有多种用途，比如 `^`。只有当它出现在字符集合里且紧跟在左方括号后面时，它才表示排除该字符集合。如果出现在字符集合之外并位于模式的开头，`^` 将匹配字符串的起始位置。

### 多行模式

许多正则表达式都支持使用一些特殊的元字符去改变另一些元字符的行为，`(?m)` 就是其中之一，它可用于启用多行模式。多行模式迫使正则表达式引擎将换行符视为字符串分隔符，这样一来 `^` 既可以匹配字符串开头，也可以匹配换行符之后的起始位置，即新行。在使用时 `(?m)` 必须出现在整个模式的最前面。

```regex
\bcat\b
\B-\B
</?xml.*\?>
^\s*<\?xml.*\?>
</[Hh][Tt][Mm][Ll]>\s*$
(?m)^\s*\/\/.*$
```

## 子表达式

划分子表达式的目的是为了将其视为单一的实体来使用。子表达式必须出现在 `(` 和 `)` 之间。

```regex
($nbsp;){2,}
(\d{1,3}\.){3}\d{1,3}
(19|20)\d{2}
<!-- 注意这里只能反向先匹配大的，再匹配小的。不然会出现只匹配到前两位数的情况 -->
(((25[0-5])|(2[0-4]\d)|(1\d{2})(\d{1,2}))\.){3}(((25[0-5])|(2[0-4]\d)|(1\d{2})(\d{1,2})))
```

## 反向引用（Backreference）

- 反向引用指的是这些实体引用的是先前的子表达式。
- 反向引用只能用来引用括号里的子表达式。
- 大多数实现中 `(\0)` 可以用来代表整个正则表达式。
- `.` 通常无法匹配换行符。

### 替换

```regex
<!-- 这里 \1 匹配到的内容与第一个分组匹配的内容是一样的 -->
[ ]+(\w+)[ ]+\1
<[hH]([1-6])>.*?<\/[hH]\1>
```

### 大小写转换

| 元字符 | 说明 |
| ------ | ------ |
| \E | 结束 \L 或 \U 转换 |
| \l | 把下一个字符转换为小写 |
| \L | 把 \L 到 \E 之间的字符全部转换为小写 |
| \u | 把下一个字符转换为大写 |
| \U | 把 \U 到 \E 之间的字符全部转换为大+写 |
