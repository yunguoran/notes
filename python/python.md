# Python

## 起步

关闭 Python REPL 的两种方法：

- 按 **Ctrl** + **z**、再按回车键。
- 执行 `exit()`。

## 变量和简单的数据类型

变量是可以赋给值的标签。

### 字符串

- `str.title()` 会将字符串中每个单词的首字母转换为大写，其余字母转换为小写。
- `str.capitalize()` 只会将字符串的第一个字符大写，其余字符转换为小写。
- 将字符串中的每个单词的首字母大写，同时保留其余字母的大小写：

    ```python
    def capitalize_first_letter_of_each_word(text):
        return ' '.join(word[0].upper() + word[1:] for word in text.split())

    text = "hello world"
    capitalized_text = capitalize_first_letter_of_each_word(text)
    print(capitalized_text)

    ```

- `str.strip() 会同时去除字符串首尾的空白`。
- `str.rstrip() 会去除字符串末尾的空白`。
- `str.lstrip() 会去除字符串开头的空白`。

#### 在字符串中使用变量

- 要在字符串中插入变量的值，可在前引号前加上字母 `f`，再将要插入的变量放在花括号内。这样，当 Python 显示字符串时，将把每个变量都替换为其值（**f** 字符串）。
- **f** 字符串是 Python 3.6 引入的。

### 数

#### 整数

Python 使用两个乘号（`*`）表示乘方运算。

#### 浮点数

- 将任意两个数相除时，结果总是浮点数。即便这两个数都是整数且能整除。
- 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数。

#### 数中的下划线（Python 3.6 及以后）

- 书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读。
- 打印此种数时，Python 不会打印其中的下划线。

#### 同时给多个变量赋值

```python
x, y, z = 0, 0, 0
```

- 可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。
- 这样做时，需要用逗号将变量名分开；对于要赋给变量的值，也需同样处理。

#### Python 之禅

```python
import this
```
