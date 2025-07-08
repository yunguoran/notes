# 基础知识

## 第 1 章 起步

Windows 终端：

- `cd` 可以在文件系统中导航。
- `dir` 可以显示当前目录中的所有文件。
- `python hello_world.py` 可以从终端运行 Python 代码。

关闭 Python REPL 的两种方法：

- 按 **Ctrl** + **z**、再按回车键。
- 执行 `exit()`。

注意在 Python REPL（[Read–eval–print loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)）中不必使用 `print()` 即可打印，因为 Python REPL 是交互式的。

## 第 2 章 变量和简单的数据类型

- Python 变量名应当小写。
- 变量是可以赋给值的标签。

### 字符串

编程中的**空白**泛指任何非打印字符。

- `str.upper()` 全部大写。
- `str.lower()` 全部小写。
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

- `str.lstrip()` 会去除字符串开头的空白。
- `str.rstrip()` 会去除字符串末尾的空白。
- `str.strip()` 会同时去除字符串首尾的空白。

#### 在字符串中使用变量

- 要在字符串中插入变量的值，可在前引号前加上字母 `f`，再将要插入的变量放在花括号内。这样，当 Python 显示字符串时，将把每个变量都替换为其值（**f** 字符串）。
- **f** 字符串是 Python 3.6 引入的。

    ```python
    name = 'Albert Einstein'
    message = f'Hello {name}!'
    print(message)
    ```

### 数

#### 整数

Python 使用两个乘号（`**`）表示乘方运算。

#### 浮点数

- 将任意两个数相除时，结果总是浮点数。即便这两个数都是整数且能整除。
- 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数。

    ```python
    # 除法生成数字 8。
    print(int(16 / 2))
    print(16 // 2)
    print(format(16 / 2, '.0f'))
    ```

#### 数中的下划线（Python 3.6 及以后）

- 书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读。
- 打印此种数时，Python 不会打印其中的下划线。

    ```python
    universe_age = 14_000_000_000
    ```

#### 同时给多个变量赋值

- 可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。
- 这样做时，需要用逗号将变量名分开；对于要赋给变量的值，也需同样处理。

    ```python
    x, y, z = 0, 0, 0
    ```

#### Python 之禅

不要企图编写完美无缺的代码，而是要先编写行之有效的代码，再决定是对其做进一步改进，还是转而去编写新代码。

```python
import this
```

## 第 3 章 列表简介

- 在 Python 中，用方括号（`[]`）表示列表，并用逗号分隔其中的元素。
- 列表是有序集合，因此要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。如：`bicycle[0]`。
- 索引从 **0** 开始。
- 通过将索引指定为 **-1** 以访问列表最后一个元素。这种约定也适用于其他负数索引。例如，索引 **-2** 返回倒数第二个元素。

### 修改、添加和删除元素

- 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。如：`motorcycles[0] = 'ducati'`。
- 添加列表元素。
    - 使用 `append()` 方法在列表末尾添加元素。如：`motorcycles.append('ducati')`。
    - 使用 `insert()` 方法在列表的任何位置添加元素。如：`motorcycles.insert(0, 'ducati')`。这种操作将列表中既有的每个元素都右移一个位置。
- 删除列表元素。
    - 如果知道要删除的元素在列表中的位置，可使用 `del` 语句删除元素。如：`del motorcycles[0]`。删除后无法访问该元素。
    - 方法 `pop()` 删除列表末尾的元素，并让你能够接着使用它，如：`popped_motorcycle = motorcycles.pop()`。
    - 可以使用 `pop()` 来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引即可。如：`first_owned = motorcycles.pop(0)`。
    - 使用 `remove()` 可以根据值来删除元素，此时也可以接着使用它的值。
    - 方法 `remove()` 只删除第一个指定的值，如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。

### 组织列表

- 使用 `sort()` 对列表进行永久排序。
    - `cars.sort()` 按字母顺序排列。
    - `cars.sort(reverse=True)` 按字母顺序相反的顺序排列。
- 使用 `sorted()` 对列表进行临时排序，使用之后原列表的排列顺序并没有变。
    - `sorted(cars)`
    - `sorted(cars, reverse=True)`
- 要反转列表元素的排列顺序，可使用方法 `reverse()`。如：`cars.reverse()`。
    - `reverse()` 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。
    - `reverse()` 永久修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用 `reverse()` 即可。
- 使用 `len()` 获取列表的长度。

## 第 4 章 操作列表

### 遍历整个列表

- 在代码 `for cat in cats` 后面，每个缩进的代码行都是循环的一部分，将针对列表中的每个值都执行一次。
- 在 for 循环后面，没有缩进的代码都只执行一次。

### 避免缩进错误

- Python 根据缩进来判断代码行与前一个代码行的关系。
- `for` 语句末尾的冒号告诉 Python，下一行是循环的第一行。
- `for magician in magicians:` 这一行就已经将 `magician` 这个变量与 `magicians[0]` 关联起来了。因此下方代码不会报错，且 `magician` 的值在循环结束之后依然是 `magicians[-1]`，即 `magicians` 列表中最后的那个元素值。

    ```python
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!")

    # Alice, that was a great trick!
    # David, that was a great trick!
    # Carolina, that was a great trick!
    # I can't wait to see your next trick, Carolina!
    ```

### 创建数值列表

- `range(1, 5)` 的类型是 `<class 'range'>`，左闭右开。
- `range(6)` 返回数 0 - 5。
- 可使用函数 `list()` 将 `range()` 的结果直接转换为列表。

    ```python
    for value in range(1, 5):
        print(value)

    # 1
    # 2
    # 3
    # 4

    # 指定步长
    for value in range(2, 11, 2):
        print(value)

    # 2
    # 4
    # 6
    # 8
    # 10
    ```

#### 列表解析

```python
squares = [value**3 for value in range(1, 11)]
print(squares)
```

### 使用列表的一部分

#### 列表切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 `range()` 一样，Python 在到达第二个索引**之前**的元素后停止。

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 如果没有指定第一个索引，Python 将自动从列表开头开始。
print(players[:3])
# 要让切片终止于列表末尾，也可使用类似的语法。
print(players[2:])
# 输出名单上的最后三名队员。
print(players[-3:])
# 可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取一个。
print(players[:3:2])
```

#### 复制列表

- 创建一个包含整个列表的切片（即副本），方法是同时省略起始索引和终止索引（`[:]`）。
- 如果直接赋值，而不是将 `my_foods` 的副本（`my_foods[:]`）赋给 `friend_foods`，实际的行为将是 `friend_foods` 和 `my_foods` 指向同一个列表。

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
```

### 元组

Python 将不能修改的值称为**不可变**的 ，而不可变的列表被称为**元组**。

- 元组看起来很像列表，但使用**圆括号**而非中括号来标识。
- 严格地说，元组是由**逗号**标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号。
- 虽然不能修改元组的元素，但可以给存储元组的变量赋值。

## 第 5 章 if 语句

### 条件测试

每条 `if` 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为**条件测试**。

- 要判断两个值是否不等，可结合使用惊叹号和等号（`!=`），其中的惊叹号表示**不**。
- 要判断特定的值是否已包含在列表中，可使用关键字 `in`。
- 要判断特定的值未包含在列表中可使用关键字 `not in`。
- 我们经常需要检查超过两个的情形，为此可使用 Python 提供的 `if-elif-else` 结构。
    - `elif` 代码块可以有多个。
    - `else` 代码块可以省略。
- 在 `if` 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True ，并在列表为空时返回 False。

    ```python
    requested_toppings = []

    if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")
    ```

## 第 6 章 字典

在 Python 中，**字典**是一系列键值对 。每个键都与一个值相关联，你可使用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值。

- 在 Python 中，字典用放在花括号（`{}`）中的一系列键值对表示。
- 要获取与键相关联的值，可依次指定字典名和放在方括号内的键。

    ```python
    alien_0 = {'color': 'green'}
    print(alien_0['color'])
    ```

    - 此时如果指定的键不存在就会报错。

        ```python
        alien_0 = {'color': 'green', 'speed': 'slow'}
        print(alien_0['points'])

        # Traceback (most recent call last):
        # File "D:\workspace\pythonWork\main.py", line 2, in <module>
        #     print(alien_0['points'])
        #         ~~~~~~~^^^^^^^^^^
        # KeyError: 'points'
        ```

    - 可以使用方法 `get()` 在指定的键不存在时返回一个默认值。

        ```python
        alien_0 = {'color': 'green', 'speed': 'slow'}
        point_value = alien_0.get('points', 'No point value assigned.')
        print(point_value)

        # No point value assigned.
        ```

    - 使用方法 `get()` 时如果没有指定第二个参数且指定的键不存在，Python 将返回值 None 。
- 字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。

    ```python
    alien_0 = {'color': 'green', 'points': '5'}
    print(alien_0)

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    # {'color': 'green', 'points': '5'}
    # {'color': 'green', 'points': '5', 'x_position': 0, 'y_position': 25}
    ```

- 字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。
- 要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值。

    ```python
    alien_0 = {'color': 'green'}
    print(f"The alien is {alien_0['color']}.")

    alien_0['color'] = 'yellow'
    print(f"The alien is now {alien_0['color']}.")

    # The alien is green.
    # The alien is now yellow.
    ```

- 对于字典中不再需要的信息，可使用 `del` 语句将相应的键值对彻底删除。使用 `del` 语句时，必须指定字典名和要删除的键。删除掉的键值对会永远消失。

    ```python
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)

    del alien_0['points']
    print(alien_0)

    # {'color': 'green', 'points': 5}
    # {'color': 'green'}
    ```

### 遍历字典

- 字典的 `items()` 方法返回一个键值对列表。
- `keys()` 方法返回一个键列表。
    - 可以使用函数 `sorted()` 来获得按特定顺序排列的键列表的副本。
    - 遍历字典时，会默认遍历所有的键，因此 `for name in favorite_languages.keys()` 中的 `.keys()` 可以省略。
- `values()` 方法返回一个值列表。
- `set()` 可以剔除重复项，返回值是 `<class 'set'>`。

    ```python
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }

    for name, language in favorite_languages.items():
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

    # name: jen
    # language: python

    # name: sarah
    # language: c

    # name: edward
    # language: ruby

    # name: phil
    # language: python

    # Jen
    # Sarah
    # Edward
    # Phil
    # Edward, thank you for taking the poll.
    # Jen, thank you for taking the poll.
    # Phil, thank you for taking the poll.
    # Sarah, thank you for taking the poll.
    # Python
    # C
    # Ruby
    # Python
    # Ruby
    # C
    # Python
    ```

- 可使用一对花括号直接创建**集合**，并在其中用**逗号**分割元素。集合不会以特定的顺序存储元素。

    ```python
    languages = {'python', 'ruby', 'python', 'c'}
    print(languages)

    # {'python', 'c', 'ruby'} 注意此处每次输出的结果很可能是不一样的
    ```

### 嵌套

如果函数调用 `print()` 中的字符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于除第一行外的其他各行，都在行首加上引号并缩进。这样，Python 将自动合并圆括号内的所有字符串。

```python
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
```

## 第 7 章 用户输入和 while 循环

### 用户输入

- 函数 `input()` 让程序暂停运行，等待用户输入一些文本。
- `input()` 接受一个字符串参数：要向用户显示的提示。
- 运算符 `+=` 在字符串末尾附加一个字符串。
- 函数 `int()` 将字符串转为数值类型。
- 求模运算符（`%`）将两个数相除并返回余数。

```python
name = input("Please enter your name: ")
print(f"\Hello, {name}!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\Hello, {name}!")
```

### while 循环

- 在任何 Python 循环中都可使用 `break` 语句。
- 要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用 `continue` 语句。

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

## 第 8 章 函数

- **文档字符串**（docstring）描述了函数是做什么的。文档字符串用三引号括起，Python 使用它们来生成有关程序中函数的文档。
- 形参（parameter）、实参（argument）。

```python
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")

greet_user()
```

### 传递实参

- 位置实参：实参的顺序与形参的顺序相同。
- 关键字实参：每个实参都由变量名和值组成，此时无须考虑函数调用中的实参顺序。
- 使用列表和字典。
- 编写函数时，可给每个形参指定默认值。
    - 在调用函数中给形参提供了实参时，Python 将使用指定的实参值；否则，将使用形参的默认值。
    - 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让 Python 依然能够正确地解读位置实参。

```python
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='willie')
```

### 返回值

- Python 将非空字符串解读为 `True`。
- 给形参一个空的默认值时，可以将此实参变为可选的。
- `None`（表示变量没有值），条件测试中，`None` 相当于 `False`。

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
musician = build_person('jimi', 'hendrix')
print(musician)
```

### 传递列表

- 每个函数都只应负责一项具体的工作。
- 为了禁止函数修改列表，可以向函数传递列表的副本。这样函数所作的任何修改都只影响副本，而原件丝毫不受影响。
- 让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。

```python
function_name(list_name[:])
```

### 传递任意数量的实参

有时候，预先不知道函数需要接受多少个实参。形参名 `*toppings` 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个元组中。Python 将实参封装到一个元组中，即便函数只收到一个值。

```python
def make_pizza(*toppings):
    """概述要制作的比萨。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

- `*args` 收集任意数量的位置实参。
- `**kwargs` 收集任意数量的关键字实参。`kwargs` 是字典类型。

```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# {'location': 'princeton', 'field': 'physics','first_name': 'albert', 'last_name': 'einstein'}
```

### 将函数存储在模块中

**模块**是扩展名为 `.py` 的文件，包含要导入到程序中的代码。

- 导入整个模块
    - `import module_name`
    - `module_name.function_name()`
- 导入特定函数
    - `from module_name import function_name`
    - `from module_name import function_0, function_1, function_2`
    - `function_name()`
- 使用 `as` 给函数指定别名
    - `from module_name import function_name as fn`
- 使用 `as` 给模块指定别名
    - `import module_name as mn`
- 导入模块中的所有函数（**要么只导入需要使用的函数，要么导入整个模块并使用句点表示法，此方法不推荐。**）
    - `from module_name import *`

### 函数编写指南

- 应给函数指定描述性名称，且只在其中使用小写字母和下划线。
- 每个函数都应包含简要地阐述其功能的注释。
- 给形参指定默认值时，等号两边不要有空格。
- 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开。
- 所有 `import` 语句都应放在文件开头。唯一例外的情形是，在文件开头使用了注释来描述整个程序。

## 第 9 章 类

- 在 Python 中，首字母大写的名称指的是**类**。
    - 类中的函数称为**方法**。
    - 可通过实例访问的变量称为**属性**。
- `__init__()` 是 Python 中类的构造方法，其第一个参数必须是 `self`，这是一个指向实例本身的引用。
- 创建实例时没有 Java 中的 `new` 关键字。
- `if __name__ == '__main__':` 的意思是：“如果这个文件被直接运行，而不是被导入，那么执行以下代码块”。
- 当这个文件被其他 Python 文件导入时，`__name__` 变量的值是这个文件的模块名。

```python
class Dog:
    """模拟小狗。"""

    def __init__(self, name, age):
        """初始化属性 name 和 age。"""
        self.name = name
        self.age = age

    def sit(self):
        """蹲下。"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """打滚。"""
        print(f"{self.name} rolled over.")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
```

### 继承

- 创建子类时，父类必须包含在当前文件中，且位于子类前面。
- 定义子类时，必须在圆括号内指定父类的名称：`class ElectricCar(Car):`。
- `super()` 是一个特殊函数，能够调用父类的方法：`super().__init__(make, model, year)`。

```python
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的特殊之处。"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动汽车没有邮箱。"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### Python 标准库

Python 标准库是一组模块，我们安装的 Python 都包含它。

模块 `random`。

- `randint()` 将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数。
- `choice()` 将一个列表或元组作为参数，并随机返回其中的一个元素。

### 类编码风格

- 类名应采用**驼峰命名法**，即将类名中的每个单词的首字母都大写，而不使用下划线。
- 实例名和模块名都采用小写格式，并在单词之间加上下划线。
- 对于每个类，都应紧跟在类定义后面包含一个文档字符串。
- 每个模块也都应包含一个文档字符串。
- 在**类**中，可使用**一个空行**来分隔方法；而在**模块**中，可使用**两个空行**来分隔类。
- 先编写导入标准库模块的 `import` 语句，再添加一个空行，然后编写导入你自己编写的模块的 `import` 语句。

## 第 10 章 文件和异常

### 从文件中读取数据

- 要以任何方式使用文件，那怕仅仅是打印其内容，都得先**打开**文件，才能访问它。函数 `open()` 接受一个参数：要打开的文件的路径。

    ```python
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
    print(contents)
    ```

- 关键字 `with` 在不再需要访问文件后将其关闭。
- `read()` 函数将读取这个文件的全部内容。
- `read()` 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。
- 显示文件路径时，Windows 系统使用反斜杠（`\`）而不是斜杠（`/`），但在代码中依然可以使用斜杠。
- 要逐行读取，可对文件对象使用 `for` 循环。

    ```python
    file_name = 'pi_digits.txt'

    with open(file_name) as file_object:
        for line in file_object:
            print(line.rstrip())
    ```

- 创建一个包含文件各行内容的列表。

    ```python
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line.rstrip())
    ```

- 读取文本文件时，Python 将其中的所有文本都解读为字符串。如果读取的是数，并要将其作为数值使用，就必须使用函数 `int()` 将其转换为整数或使用函数 `float()` 将其转换为浮点数。
- `replace()` 将字符串中的特定单词都替换为另一个单词，不止替换第一个，会替换所有的。

```python
message = 'I really like dogs and dogs.'
message = message.replace('dog', 'cat')
print(message)
```

### 写入文件

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

- `open` 方法的第一个实参是要打开的文件的路径。第二个实参（`'w'`）告诉 Python，要以写入模式打开这个文件。打开文件时，可指定读取模式（`'r'`）、写入模式（`'w'`）、附加模式 （`'a'`）或读写模式（`'r+'`）。如果省略了模式实参，Python 将以默认的只读模式打开文件。
- 以写入模式（`'w'`）打开文件时，如果指定的文件已经存在，Python 将在返回文件对象前清空该文件的内容。
- Python 只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 `str()` 将其转换为字符串格式。
- 函数 `write()` 不会在写入的文本末尾添加换行符。

### 异常

try-except-else 代码块：

- 依赖 `try` 代码块成功执行的代码都应放到 `else` 代码块中。
- 在系统的默认编码与要读取文件使用的编码不一致时，需要给 `open` 方法指定参数 `encoding`：`with open(filename, encoding='utf-8') as f:`。
- Python 有一个 `pass` 语句，可用于让 Python 在代码块中什么都不要做。

```python
def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

### 存储数据

- 函数 `json.dump()` 接受两个实参：要存储的数据，以及可用于存储数据的文件对象。
- 使用 `json.load()` 将数据读取到内存中。

```python
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
```
