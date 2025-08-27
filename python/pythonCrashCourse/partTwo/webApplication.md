# Web 应用程序

## 从 Django 入手

Django 是一个 **Web 框架**，即一套旨在帮助开发交互式网站的工具。

### 建立项目

**虚拟环境**是系统的一个位置，可在其中安装包，并将之与其他的 Python 包隔离。环境处于活动状态时，环境名将包含在圆括号内。在这种情况下，你可以在环境中安装包，并使用已安装的包，在虚拟环境中安装的包仅在该环境处于活动状态才可用。

```shell
# 创建虚拟环境
python -m venv ll_env
# 激活虚拟环境：
    # Linux / macOS:
    cd /d/workspace/learning_log
    source ll_env/bin/activate
    # Windows PowerShell:
    cd D:\workspace\learning_log
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\ll_env\Scripts\activate
# 终止虚拟环境
deactivate
# 安装 Django
pip install django
# 创建项目：
    # 句点告诉 Django 不要再创建一个新的目录来包含项目，而是将项目文件直接创建在当前目录中。
    # 如果你不加这个点，Django 会创建一个形如 learning_log/learning_log/ 的嵌套结构。
    django-admin startproject learning_log .
# 创建数据库
python manage.py migrate
# 查看项目状态：端口默认是 8000
python manage.py runserver ${port}
```

### 创建应用程序

**Django 项目**由一系列应用程序组成，他们协同工作让项目成为一个整体。

```shell
# 创建一个应用
python manage.py startapp ${appname}
```

#### 定义模型

- [Django Model Fields Reference](https://docs.djangoproject.com/en/5.2/ref/models/fields/)。
- 存储少量文本如名称、标题、城市等，可以使用 **CharField**。定义 CharField 属性是必须告诉 Django 该在数据库中预留多少空间。
- `auto_now_add=True`：每当用户创建新主题时，Django 都会将这个属性自动设置为当前的日期和时间。
- Django 调用方法 `__str__()` 来显示模型的简单表示。

```python
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
```
