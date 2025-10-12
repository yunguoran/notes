# Web 应用程序

## 从 Django 入手

Django 是一个 **Web 框架**，即一套旨在帮助开发交互式网站的工具。

### 建立项目

建立项目时，首先需要以规范的方式对项目进行描述，再建立虚拟环境，以便在其中创建项目。

#### 虚拟环境

**虚拟环境**是系统的一个位置，可在其中安装包，并将之与其他的 Python 包隔离。环境处于活动状态时，环境名将包含在圆括号内。在这种情况下，你可以在环境中安装包，并使用已安装的包，在虚拟环境中安装的包仅在该环境处于活动状态才可用。

```shell
# 创建虚拟环境
python -m venv ll_env
# 激活虚拟环境：
    # Linux / macOS:
    cd ~/workspace/learning_log
    source ll_env/bin/activate
    # Windows PowerShell:
    cd D:\workspace\learning_log
    # 修改 PowerShell 的脚本执行策略，默认情况下 Windows 出于安全考虑，可能不允许运行 .ps1 脚本。
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\ll_env\Scripts\activate
# Windows Terminal 配置启动项自动激活虚拟环境
xxx\powershell.exe -NoExit -Command ".\ll_env\Scripts\activate"
# 终止虚拟环境（直接关闭运行虚拟环境的终端，虚拟环境也将不再处于活动状态）
deactivate
```

#### 安装 Django

```shell
# 在虚拟环境中安装 Django
pip install django
```

#### 在 Django 中创建项目

```shell
# 句点告诉 Django 不要再创建一个新的目录来包含项目，而是将项目文件直接创建在当前目录中。
django-admin startproject ${project_name} .
```

执行 `django-admin startproject learning_log .` 命令创建的目录结构如下所示：

```shell
learning_log/ # 原本的外层文件夹
├── manage.py
├── learning_log/ # Django 自动生成的同名内层包，用来存放项目代码
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

上述结构是 Django 官方推荐的结构，外层目录作为项目容器，内层目录作为项目的实际 Python 包。名字一样是常见现象。

- `__init__.py` 让 `learning_log/` 这个文件夹被 Python 当作一个包（Package）。
    - 通常是空的。
    - 只要有 `__init__.py`，你就能在 Python 里写 `import learning_log`。
- `asgi.py` 是 ASGI (Asynchronous Server Gateway Interface) 的入口。
    - 用于部署异步服务，比如 Daphne, Uvicorn, Hypercorn，通常用于支持 WebSocket、异步视图等。
    - Django 提供一个 `application` 对象，服务器启动时会去找它。
- `setting.py` 是项目的配置文件。
- `urls.py` 用来定义 URL 路由规则。
- `wsgi.py`是 WSGI (Web Server Gateway Interface) 的入口。
    - 用于部署同步服务，比如 Gunicorn, uWSGI, mod_wsgi (Apache)。
    - 也会提供一个 `application` 对象，服务器启动时会用它来处理请求。

不写 `.`，直接执行 `django-admin startproject learning_log`。那么结果会是：

```shell
learning_log/
└── learning_log/
    ├── manage.py
    └── learning_log/
        ├── __init__.py
        ├── settings.py
        ...
```

这样会多一层目录，看起来更令人困惑。

#### 创建数据库

```shell
python manage.py migrate
```

命令 `python manage.py migrate` 的作用是把迁移文件中描述的数据库结构同步到真实的数据库。在使用 SQLite 的新项目中首次执行这个命令时，Django 将新建一个数据库。SQLite 是一种使用单个文件的数据库，是编写简单应用的理想选择。

#### 查看项目

```shell
# 端口默认是 8000
python manage.py runserver
# 也可以指定端口号
python manage.py runserver ${port}
```

Django 会启动一个名为 development server 的服务器。当你修改 Python 代码后，服务器会自动检测并重启，不用手动停止/重启。

### 创建应用程序

**Django 项目**由一系列应用程序组成，他们协同工作让项目成为一个整体。

```shell
python manage.py startapp ${appname}
```

`python manage.py startapp ${appname}` 命令用来创建一个新的 Django 应用。执行后会在当前目录下生成一个名为 `${appname}` 的文件夹，里面包含 Django 为你准备好的应用代码框架。

```shell
# 执行 python manage.py startapp learning_logs 会生成以下目录：
learning_logs/
├── __init__.py # 把 learning_logs 文件夹变成一个 Python 包
├── admin.py # 配置后台管理站点用
├── apps.py # 定义应用配置类
├── migrations/ # 存放数据库迁移文件
│   └── __init__.py
├── models.py # 定义数据库模型（表结构）
├── tests.py # 写单元测试
└── views.py # 写视图函数（处理请求、返回响应）
```

#### 定义模型

[Django Model Fields Reference](https://docs.djangoproject.com/en/5.2/ref/models/fields/)。

- 存储少量文本如名称、标题、城市等，可以使用 `CharField`。定义 `CharField` 属性时必须告诉 Django 该在数据库中预留多少空间。`max_length=200` 表示最大长度是 200 个字符。
    - 在 Python 中，一个中文字符通常也算作一个字符。
    - 这是因为 Python 的 `len()` 函数计数的是 Unicode 码点（Code Points）的数量，而不是底层的字节数。
- `auto_now_add=True`：每当用户创建新主题时，Django 都会将这个属性自动设置为当前的日期和时间。
- Django 调用方法 `__str__()` 来显示模型的简单表示。
- `TextField()` 类型的字段的长度不受限制。
- Meta 类中的 `verbose_name_plural` 属性指定 entry 的复数形式为 entries 而非 entrys。

    ```python
    from django.db import models
    from django.contrib.auth.models import User

    class Topic(models.Model):
        """A topic the user is learning about."""
        text = models.CharField(max_length=200)
        date_added = models.DateTimeField(auto_now_add=True)
        owner = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            """Return a string representation of the model."""
            return self.text

    class Entry(models.Model):
        """Something specific learned about a topic."""
        topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
        text = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = 'entries'

        def __str__(self):
            """Return a string representation of the model."""
            return f"{self.text[:50]}..."
    ```

#### 激活模型

要使用上述定义的模型，必须让 Django 将前述应用程序包含到项目中。修改项目中 `settings.py` 中的 `INSTALLED_APPS`，把自己的应用添加到这个列表中，注意要放在默认应用程序的前面，这样能够覆盖默认应用程序的行为。

```python
INSTALLED_APPS = [
    # 我的应用程序
    'learning_logs',
    # 默认添加的应用程序
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

接下来需要修改数据库，把数据库结构更新到最新状态：

```shell
# 根据在 models.py 里的改动，生成迁移文件（在 migrations/ 目录里）。
python manage.py makemigrations ${appname}
# 取迁移文件（你和 Django 自带 app 的），然后在数据库里执行相应的 SQL 操作，把数据库结构更新到最新状态。
python manage.py migrate
```

- `makemigrations`：写好施工蓝图（迁移文件）。
- `migrate`：拿着蓝图去真正施工（修改数据库）。

第一次建项目时（你还没写自己的模型）：

- 可以直接执行 `migrate`，因为 Django 内置的 app（auth、admin、sessions 等）已经带有迁移文件。
- 这一步会在数据库里创建用户表、会话表、权限表等。

当你写了自己的模型/改了模型时：

- 必须先 `makemigrations` 生成迁移文件，然后再 `migrate` 才能生效。
- 如果只执行 `migrate` 而没有 `makemigrations`，数据库不会知道你加了哪些表或字段。

#### 管理网站

##### 创建超级用户

```shell
python manage.py createsuperuser
```

##### 向管理网站注册模型

Django 自动在管理网站中添加了一些模型，如 User 和 Group，对于我们自己创建的模型，必须进行手工注册。

在 `admin.py` 中注册模型：

```python
from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

访问 <http://localhost:8000/admin/> 以添加 `Topic` 和 `Entry`。

#### Django shell

Django shell 是一个交互式终端会话，可以在其中以编程方式查看模型相关的数据。输入 `python manage.py shell` 以启动 Django shell。

```shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>

>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
...
1 Chess
2 Rock Climbing

>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2025, 9, 29, 15, 1, 9, 367810, tzinfo=datetime.timezone.utc)

>>> t.entry_set.all()
<QuerySet [
    <Entry: The opening is the first part of the game, roughly...>,
    <Entry: In the opening phase of the game, it is important ...>
]>
```

- `Topic.objects.all()` 获取模型 `Topic` 的所有实例，返回一个 `QuerySet`。
    - `QuerySet` 实现了 `__iter__()` 方法，该方法返回一个迭代器对象。
    - 除了 `__iter__()`，还要实现 `__next__()` 方法。该方法每次返回一个元素，没有元素时抛出 `StopIteration`。
    - 因此 `QuerySet` 可以像列表一样进行遍历。
- 知道对象的 ID 后就可以使用方法 `Topic.objects.get()` 获取该对象并查看其属性。
- 通过外键关系获取数据，可使用相关模型的小写名称、下划线和单词 `set`：`t.entries().all()`。

每次修改模型后，都需要重启 Django shell，这样才能看到修改之后的结果。

在 Django shell 中访问数据时编写的代码其实是查询，详细的查询文档见 [Making queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/)。

### 创建页面

使用 Django 创建页面的过程分为三个阶段：定义 URL 模式、编写视图和编写模板。

- URL 模式描述了 URL 是如何设计的，让 Django 知道如何将浏览器请求与网站 URL 匹配，以确定返回哪个页面。
- 每个 URL 都被映射到特定的视图——视图函数获取并处理页面所需的数据。
- 视图函数通常使用模板来渲染页面，而模板定义页面的总体结构。

#### 映射 URL

```python
# learning_log/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]
```

`path('', include('learning_logs.urls'))` 这行代码将会包含 `learning_logs` 这个应用所有的 URL，因此在 `learning_logs` 文件夹下新建一个 `urls.py` 即可管理该应用下的所有 URL。

```python
# learning_logs/urls.py
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
```

`app_name = 'learning_logs'` 的作用是给这个应用定义一个命名空间（Namespace）。命名空间的作用是当项目中有多个应用时，可以用 `app_name:url_name` 的方式来引用具体的 URL，避免不同应用的 URL 名字冲突。

```python
<a href="{% url 'learning_logs:topics' %}">查看所有主题</a>
```

#### 编写视图

视图函数接受请求中的信息，准备好生成页面所需的数据，再将这些数据发送给浏览器。

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
```

- `context = {'topics': topics}` 定义了一个将发送给模板的**上下文**。上下文是一个字典，其中的键是将在模板中用来访问数据的名称，而值是要发送给模板的数据。
- `new_topic = form.save(commit=False)` 让 Django 创建一个新的 `topic` 对象，并赋值给 `new_topic` 但不保存到数据库中。
- `form = EntryForm(instance=entry, data=request.POST)` 中的 `instance=entry` 实参让 Django 创建一个表单，并使用既有条目对象中的信息填充它。用户将看到既有的数据，并且能够编辑。

#### 编写模板

模板定义页面的外观，而每当页面被请求时，Django 将填入相关的数据。模板让你能够访问视图提供的任何数据。

**模板继承**是指创建网站时，一些通用元素几乎会在所有页面中出现。在这种情况下可以编写一个包含通用元素的父模板，并让每个页面都继承这个模板，而不必在每个页面中重复定义这些通用元素。

```html
<!-- learning_logs\templates\learning_logs\base.html -->
<!-- 加载 django-bootstrap5 中的模板标签集。 -->
{% load bootstrap5 %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- 设置视口宽度等于设备宽度以让页面适配手机屏幕、初始缩放比例为 1 以及不自动压缩页面。 -->
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Learning Log</title>
  <!-- 在渲染 HTML 时会生成一条 <link> 标签，引入 Bootstrap 的 CSS 文件。 -->
  {% bootstrap_css %}
  <!-- 在渲染 HTML 时会生成一条 <script > 标签，引入 Bootstrap 相关的 JavaScript 脚本。 -->
  {% bootstrap_javascript %}
</head>
<body>
  <nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">
    <a class="navbar-brand" href="{% url 'learning_logs:index' %}">Learning Log</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarCollapse"
      aria-controls="navbarCollapse"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="{% url 'learning_logs:topics' %}">Topics</a>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        {% if user.is_authenticated %}
          <li class="nav-item">
            <span class="navbar-text">Hello, {{ user.username }}.</span>
          </li>
          <li class="nav-item">
            <form class="form-inline" action="{% url 'users:logout' %}" method='post'>
              {% csrf_token %}
              <button class="btn btn-outline-secondary" name='submit'>Log out</button>
            </form>
          </li>
        {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'users:register' %} ">Register</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'users:login' %}">Log in</a>
          </li>
        {% endif %}
      </ul>
    </div>
  </nav>
  <main role="main" class="container">
    <div class=""pb-2 mb-2 border-bottom>
      {% block page_header %}{% endblock page_header %}
    </div>
    <div>
      {% block content %}{% endblock content %}
    </div>
  </main>
</body>
</html>
```

[**模板标签**](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/)（`{% %}`）用于生成要在页面中显示的信息。

- `{% url 'learning_logs:index' %}` 生成一个 URL，该 URL 与在 `learning_logs/urls.py` 中定义的名为 `index` 的 URL 模式匹配。
    - 其中 `learning_logs` 是命名空间，该命名空间来自于 `learning_logs/urls.py` 中 `app_name` 变量的值。
    - `index` 是该命名空间中一个名称独特的 URL 模式。
- `{% block page_header %}{% endblock page_header %}` 用来定义模板块。
    - `{% block page_header %}`：定义了一个可以被子模板覆盖（Override）的区域。
    - `{% endblock page_header %}`：标记这个块的结束。
    - `page_header` 是块的名字。

```html
<!-- learning_logs\templates\learning_logs\index.html -->
{% extends "learning_logs/base.html" %}

{% block page_header %}
  <div class="jumbotron">
    <h1 class="display-3">Track your learning.</h1>
    <p class="lead">Make your own learning log, and keep a list of the topics you're learning about. Whenever you learn
      something new about a topic, make an entry summarizing what you've learned.</p>
    </p>
    <a class="btn btn-lg btn-primary" href="{% url 'users:register' %}" role="button">Register &raquo</a>
  </div>
{% endblock page_header %}
```

- `{% extends 'learning_logs/base.html' %}` 声明这个模板继承自 `base.html`。
- `{% block page_header %} ... {% endblock page_header %}` 中包裹的内容将会填充到父模板中的 `page_header` 区域。

```html
<!-- learning_logs\templates\learning_logs\topics.html -->
{% extends "learning_logs/base.html" %}

{% block page_header %}
  <h2>Topics</h2>
{% endblock page_header %}

{% block content %}
  <ul>
    {% for topic in topics %}
      <li>
        <h3>
          <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
        </h3>
      </li>
    {% empty %}
      <li><h3>No topics available.</h3></li>
    {% endfor %}
  </ul>
  <h3><a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a></h3>
{% endblock content %}
```

- Python 使用缩进来指出哪些代码是 `for` 循环的组成部分，而在模板中，每个 `for` 循环都必须使用 `{% endfor %}` 标签来显式地指出其结束位置。
- 要在模板中打印变量，需要将变量名用双花括号括起来（`{{ topic }}`）。
- `{% empty %}` 告诉 Django 在列表 `topics` 为空时该做什么事情。

```html
<!-- learning_logs\templates\learning_logs\topic.html -->
{% extends 'learning_logs/base.html' %}

{% block page_header %}
  <h3>{{ topic }}</h3>
{% endblock page_header %}

{% block content %}
<p>
  <a href="{% url 'learning_logs:new_entry' topic.id %}">Add a new entry</a>
</p>
<ul>
  {% for entry in entries %}
  <div class="card mb-3">
    <h4 class="card-header">
      {{ entry.date_added|date:"M d, Y H:i" }}
      <small>
        <a href="{% url 'learning_logs:edit_entry' entry.id %}">edit entry</a>
      </small>
    </h4>
    <div class="card-body">
      {{ entry.text|linebreaks }}
  </div>
  {% empty %}
    <p>There are no entries for this topic yet.</p>
  {% endfor %}
</ul>
{% endblock content %}
```

- `|` 被称为[**模板过滤器**](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/)，即对模板变量进行格式化的函数。
- 过滤器 `linebreaks` 会把换行符转换成 `<p>` 或 `<br>`，确保多行文本在 HTML 中正确显示。

```html
<!-- learning_logs\templates\learning_logs\new_topic.html -->
{% extends "learning_logs/base.html" %}

{% block content %}
  <p>Add a new topic:</p>
  <form action="{% url 'learning_logs:new_topic' %}" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button name="submit">Add Topic</button>
  </form>
{% endblock content %}
```

- `{% csrf_token %}` 来防止攻击者利用表单来获得对服务器未经授权的访问（跨站请求伪造）。
- `{{ form.as_p }}` 让 Django 自动创建显示表单所需的全部字段。修饰符 `as_p` 让 Django 以段落格式渲染所有表单元素。

## 用户账户

### 让用户输入数据

#### 添加新主题

让用户输入并提交信息的页面都是表单。在 Django 中创建表单最简单的方式是使用 [ModelForm](https://docs.djangoproject.com/en/5.2/topics/forms/modelforms/)，它可以根据先前定义的模型中的信息自动创建表单。

```python
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
```

- `TopicForm` 继承自 `forms.ModelForm`，表示它是一个基于模型的表单。
- `Meta` 内部类是 Django 约定的写法，用来配置表单和模型的对应关系。
    - `model = Topic`：告诉 Django，这个表单是基于 `Topic` 模型生成的。
    - `fields = ['text']`：只显示模型中的 `text` 字段（忽略其它字段，比如 `date_added`）。
    - `labels = {'text': ''}`：设置表单字段的显示标签为空字符串（默认标签会是 `Text`）。
- `widgets = {'text': forms.Textarea(attrs={'cols': 80})}`：将默认的单行 `<input>` 改为多行 `<textarea>`，并设置宽度为 `80` 列。

### 创建用户账户

#### 登录页面

Django 提供了一个默认的视图 login。

```python
# users\urls.py
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
```

`path('', include('django.contrib.auth.urls'))` 包含了 Django 定义的一些默认的身份验证 URL。登录页面的 URL 模式与 URL `http://localhost:8000/users/login` 匹配。

默认的身份验证视图在文件夹 registration 中查找模板，因此我们需要在 `users\templates\` 路径下创建这个文件夹。

```html
<!-- users\templates\registration\login.html -->
{% extends "learning_logs/base.html" %}
{% load bootstrap5 %}

{% block page_header %}
  <h2>Log in to your account.</h2>
{% endblock page_header %}

{% block content %}
  <form method="post" action="{% url 'users:login' %}" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
      <button type="submit" class="btn btn-primary">Log in</button>
    {% endbuttons %}
    <input type="hidden" name="next" value="{% url 'learning_logs:index' %}">
  </form>
{% endblock content %}
```

在 Django 身份验证系统中，每个模板都可使用变量 user，这个变量有一个 `is_authenticated` 属性用来表示用户是否已经登录。

#### 注册页面

Django 有一个 `UserCreationForm` 表单，可以用作新用户注册。

```python
# users\views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
```

#### 让用户拥有自己的数据

如果你确实想要一个全新的数据库可以执行 `python manage.py flush`，这样会重建数据库的结构。超级用户以及所有的数据都将丢失。

## 设置样式并部署

[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) 库是一个前端工具包，用于为 web 应用程序设置样式。[django-bootstrap5](https://django-bootstrap5.readthedocs.io/en/latest/) 是 Django 和 Bootstrap 之间的桥梁，可以让我们在 Django 模板里更方便地使用 Bootstrap5 样式来渲染表单、按钮、分页等组件，
无需手动写大量 HTML + CSS。。

### 设置项目的样式

```shell
# 在虚拟环境中安装 django-bootstrap5
pip install django-bootstrap5
```

在 `settings.py` 的 `INSTALLED_APPS` 中添加 `bootstrap5`。

```python
INSTALLED_APPS = [
    # My apps
    'learning_logs',
    'users',
    # Third-party apps
    'bootstrap5',
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### 使用 Bootstrap

```html
<!-- 加载 django-bootstrap5 中的模板标签集。 -->
{% load bootstrap5 %}
```

### 部署

#### 创建文件 requirements.txt

命令 `freeze` 让 `pip` 将项目中当前安装的所有包的名称都写入文件 `requirements.txt`。

```shell
pip freeze > requirements.txt
```
