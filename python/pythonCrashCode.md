# Python Crash Code

## 第 1 章 起步

关闭 Python REPL 的两种方法：

- 按 **Ctrl** + **z**、再按回车键。
- 执行 `exit()`。

注意在 Python REPL 中不必使用 print() 即可打印，因为 Python REPL 是交互式的。

## 第 2 章 变量和简单的数据类型

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

## 第 3 章 列表简介

- 列表是有序集合。
- 要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。如：`bicycle[0]`。
- 索引从 `0` 开始。
- 通过将索引指定为 `-1` 以访问列表最后一个元素。这种约定也适用于其他负数索引。例如，索引 `-2` 返回倒数第二个元素。

### 修改、添加和删除元素

- 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
- 添加列表元素。
    - 使用 `append()` 方法在列表末尾添加元素： `motorcycles.append('ducati')`。
    - 使用 `insert()` 方法在列表的任何位置添加元素：`motorcycles.insert(0, 'ducati')`。这种操作将列表中既有的每个元素都右移一个位置。
- 删除列表元素。
    - 如果知道要删除的元素在列表中的位置，可使用 `del` 语句删除元素：`del motorcycles[0]`。删除后无法访问该元素。
    - 方法 `pop()` 删除列表末尾的元素，并让你能够接着使用它：`popped_motorcycle = motorcycles.pop()`。
    - 可以使用 `pop()` 来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引即可：`first_owned = motorcycles.pop(0)`。
    - 使用 `remove()` 可以根据值来删除元素，此时也可以接着使用它的值。
    - 方法 `remove()` 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。

### 组织列表

- 使用 `sort()` 对列表进行永久排序：`cars.sort(reverse=True)`。
- 使用 `sorted()` 对列表进行临时排序： `sorted(cars, reverse=True)`。
- 要反转列表元素的排列顺序，可使用方法 `reverse()`：`cars.reverse()`。
- 使用 `len()` 获取列表的长度。

## 第 4 章 操作列表

### 遍历整个列表

- 在代码 `for cat in cats` 后面，每个缩进的代码行都是循环的一部分，将针对列表中的每个值都执行一次。
- 在 for 循环后面，没有缩进的代码都只执行一次。

### 避免缩进错误

- Python 根据缩进来判断代码行与前一个代码行的关系。
- `for` 语句末尾的冒号告诉 Python，下一行是循环的第一行。

### 创建数值列表

- 可使用函数 `list()` 将 `range()` 的结果直接转换为列表。
- `range(1, 5)` 的类型是 `<class 'range'>`，左闭右开。
- `range(6)` 返回数 0 - 5。

### 列表解析

```python
squares = [value**3 for value in range(1, 11)]
print(squares)
```

### 列表切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 `range()` 一样，Python 在到达第二个索引之前的元素后停止。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 如果没有指定第一个索引，Python 将自动从列表开头开始
print(players[:3])
# 要让切片终止于列表末尾，也可使用类似的语法
print(players[2:])
# 输出名单上的最后三名队员
print(players[-3:])
# 可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取一个。
print(players[:3:2])
```

### 复制列表

创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（`[:]`）。

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
```

### 元组

Python 将不能修改的值称为**不可变**的 ，而不可变的列表被称为**元组**。

- 元组看起来很像列表，但使用**圆括号**而非中括号来标识。
- 严格地说，元组是由**逗号**标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号。
- 虽然不能修改元组的元素，但可以给存储元组的变量赋值。

### 设置代码格式

## 第 5 章 if 语句

### 条件测试

每条 `if` 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为**条件测试**。

- 要判断两个值是否不等，可结合使用惊叹号和等号（`!=`），其中的惊叹号表示**不**。
- 要判断特定的值是否已包含在列表中，可使用关键字 `in`。
- 要判断特定的值未包含在列表中可使用关键字 `not in`。
- 我们经常需要检查超过两个的情形，为此可使用 Python 提供的 `if-elif-else` 结构。
- 在 `if` 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True ，并在列表为空时返回 False。

## 第 6 章 字典

在 Python 中，**字典**是一系列键值对 。每个键都与一个值相关联，你可使用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值。

- 在 Python 中，字典用放在花括号（`{}`）中的一系列键值对表示。
- 要获取与键相关联的值，可依次指定字典名和放在方括号内的键。
    - 此时如果指定的键不存在就会报错。
    - 可以使用方法 `get()` 在指定的键不存在时返回一个默认值。
    - 使用方法 `get()` 时如果没有指定第二个参数且指定的键不存在，Python 将返回值 None 。
- 字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。
- 字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。
- 要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值。
- 对于字典中不再需要的信息，可使用 `del` 语句将相应的键值对彻底删除。使用 `del` 语句时，必须指定字典名和要删除的键。

### 遍历字典

- 字典的 `items()` 方法返回一个键值对列表。
- `keys()` 方法返回一个键列表。可以使用函数 `sorted()` 来获得按特定顺序排列的键列表的副本。
- `values()` 方法返回一个值列表。
- `set()` 可以剔除重复项，返回值是 `<class 'set'>`。
- 可使用一对花括号直接创建集合，并在其中用逗号分割元素。集合不会以特定的顺序存储元素。

```python
favorite_languages = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}

for name, language in favorite_language.items():
    print(f"name: {name}")
    print(f"language: {language}\n")

for name in favorite_languages.keys():
    print(name.title())

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
```

### 嵌套

如果函数调用 `print()` 中的字符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于除第一行外的其他各行，都在行首加上引号并缩进。这样，Python 将自动合并圆括号内的所有字符串。

```python
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
```
