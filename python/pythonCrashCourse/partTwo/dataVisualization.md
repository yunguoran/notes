# 数据可视化

**数据可视化**指的是通过可视化表示来探索数据。它与数据分析紧密相关，而**数据分析**指的是使用代码来探索数据集的规律和关联。

## 生成数据

Matplotlib 是一个数学绘图库。

```shell
python -m pip install --user matplotlib
```

### 折线图

```python
import matplotlib.pyplot as plt

# 打印可用的内置样式。
print(plt.style.available)

# 使用内置样式。
plt.style.use('seaborn-v0_8-colorblind')

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# fig 接收的是 matplotlib.figure.Figure 对象，表示整个图形窗口。
# ax 接收的是 matplotlib.axes.axes 对象，表示子图。如果只创建一个子图，它是单一的 Axes 对象，如果创建多个子图，它是一个包含多个 Axes 对象的二维数组。
fig, ax = plt.subplots()

# linewidth 参数决定了绘制线条的粗细。
ax.plot(input_values, squares, linewidth=3)

# 设置图表和每条轴线的标题以及文字的大小。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度的字号为 14
ax.tick_params(axis='both', labelsize=14)

plt.show()
```

### 散点图

```python
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-colorblind')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()

# 使用参数 s 设置绘制图形时使用的点的尺寸。
# 使用参数 c 设置绘制图形时使用的点的颜色。
#   - 可以直接使用颜色名，如 'red', 'blue', 'green'。
#   - 也可使用 RGB 颜色模式：ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0))。
#   - 值越接近 0，指定的颜色越深；越接近 1，颜色越浅。
ax.scatter(x_values, y_values, s=10, c='red')

ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

# which 参数有三个值：major：主刻度、minor：次刻度、both：同时修改主刻度和次刻度。
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()
```

#### 在散点图中使用[颜色映射](https://matplotlib.org/stable/gallery/color/colormap_reference.html#colormap-reference)

**颜色映射**是一系列颜色，从起始颜色渐变到结束颜色。

```python
# 打印所有的颜色映射。
from matplotlib import colormaps
print(list(colormaps))
```

```python
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-colorblind')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.turbo)

ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

# 第一个参数是文件名、第二个参数指定将图表多余空白区域裁剪掉。
#   - bbox：即边界框（Bounding Box），在计算机视觉和图像处理中，用于表示目标物体在图像中的位置和大小的矩形框。
plt.savefig('plot.png', bbox_inches='tight')
```

#### 随机漫步

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

plt.style.use('seaborn-v0_8-colorblind')

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()
    # figsize 参数指定生成的图形的尺寸，dpi 参数指定分辨率
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=200)

    # edgecolors='none' 会删掉每个点周围的轮廓
    ax.scatter(rw.x_values, rw.y_values, s=1, c=range(rw.num_points), cmap=plt.cm.turbo, edgecolors='none')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

### 使用 Plotly 模拟掷骰子

需要创建在浏览器上显示的图表时，**Plotly** 生成的图表将自动缩放以适合观看者的屏幕，且生成的图表是交互式的。

```shell
python -m pip install --user plotly
```

```python
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    # 列表的 count 方法，可以计数特定数字的个数。
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个 D6 和一个 D10 50000 次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
```

## 下载数据

打印表头及其位置。

```python
import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # next() 是内置函数，用于获取迭代器的下一个值。
    header_row = next(reader)

# enumerate(iterable, start=0) 可以获取每个元素的索引及其值。
for index, column_header in enumerate(header_row):
    print(index, column_header)
```

绘制温度图表。

```python
import csv
from datetime import datetime

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-colorblind')

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

fig, ax = plt.subplots()
# 绘制倾斜的日期标签，以免其批次重复。
fig.autofmt_xdate()
# 实参 alpha 指定颜色的透明度。alpha 值为 0 表示完全透明，为 1（默认设置）表示完全不透明。
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
# 向 fill_between() 传递一个 x 值系列（dates），以及两个 y 值系列（highs 和 lows）。实参 facecolor 指定填充区域的颜色。
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('2018 年每日最高温度', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('温度（F）', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

### 模块 datetime

- 变量名 vs `print()` 是调用了不同的方法。
    - `first_date` 调用的底层方法是 `first_date.__repr__()`。
    - `print(first_date)` 调用的底层方法是 `first_date.__str__()`。
- `from datetime import datetime` 中的第二个 `datetime` 其实是类名，设计的时候并未遵循类名首字母大写的规范。
    - `strptime()`：p 是 parse，意为从字符串中解析时间。
    - `strftime()`：f 是 format，意为时间对象格式化为字符串。
    - [Format Codes](https://docs.python.org/3/library/datetime.html#format-codes)。

```python
>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
>>> first_date
datetime.datetime(2018, 7, 1, 0, 0)
>>> print(first_date)
2018-07-01 00:00:00
```

### 全球地震散点图

美化 JOSN 数据。

```python
import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    print(type(all_eq_data))

readable_file = 'data/readable_file.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
```

打印 Plotly Express 的所有渐变。

```python
import plotly.express as px

for key, value in px.colors.named_colorscales():
    print(key)
    print(value)
```

全球地震散点图。

```python
import json
import pandas as pd
import plotly.express as px

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
title = all_eq_data['metadata']['title']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags),
    columns=['lons', 'lats', 'titles', 'mags']
)
data.head()

fig = px.scatter(
    data,
    x='lons',
    y='lats',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=title,
    size='mags',
    size_max=10,
    color='mags',
    color_continuous_scale='Viridis',
    hover_name='titles'
)
fig.write_html('global_earthquakes.html')
fig.show()
```

## 使用 API

Web API 是网站的一部分，用于与使用具体 URL 请求特定信息的程序交互。这种请求称为 **API 调用**。

```shell
python -m pip install --user requests
```

### 使用 Web API

```python
import requests

from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'GitHub 上最受欢迎的 Python 项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
```

### Hacker News API

```python
from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': int(response_dict.get('descendants', 0))
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```
