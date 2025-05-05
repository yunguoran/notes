# 数据可视化

Matplotlib 是一个数学绘图库。

```shell
python -m pip install --user matplotlib
```

```python
import matplotlib
import matplotlib.pyplot as plt

print(plt.style.available)
print(matplotlib.matplotlib_fname())
plt.savefig('plot.png', bbox_inches='tight')

import os

# 获取当前脚本文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
```
