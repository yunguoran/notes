# Data Analysis

## Model

RFM

- recency 用户的最近消费时间
- frequency 消费频次
- monetary 消费金额

## Statistical Measure

### Percentile

Quantile 是分位数，划分份数可以是任意等份，Percentile 是百分位数，划分份数为 100 等份。百分位数是分位数的特例。中位数是百分位数的特例，即 `median(col) = percentile(col, 0.5)`。

Percentile 用于精确计算分位数。注意：不要再超大数据集上使用，极易 OOM。

```sql
-- 计算单个分位数
SELECT percentile(col, p);
-- 同时计算多个分位数（返回一个数组）
SELECT percentile(col, array(p1, p2, p3, ...));
```

- 对数据进行全局升序排序。
- 根据公式 `pos = (n − 1) * p + 1` 计算精确位置（n 为**数据总数**、p 为**分位点**，取值范围 [0.0, 1.0]）。
- 如果 pos 是整数，直接取该位置的值。
- 如果是小数，则找出它左右两个最近的整数位置，对应的值用**线性插值**计算。
    - 线性插值在两个已知点 (x1​, y1​) 和 (x2​, y2​) 之间画一条直线。
    - 直线方程就是一元一次函数：y = kx + b
    - k 为斜率：即 (y2 - y1) / (x2 - x1)
    - b 为截距：即 x = 0 时的 y 值。

approx_percentile 用于近似计算分位数，通过牺牲少量精度换取巨大的性能提升。

```sql
-- 计算单个分位数
SELECT approx_percentile(col, p [, accuracy]);
-- 同时计算多个分位数
SELECT approx_percentile(col, array(p1, p2, p3, ...) [, accuracy]);
```

- 在每个分区内构建一个数据“摘要”，记录数据的分布特征。
- 将这些摘要合并，而不是合并所有原始数据。
- 从合并后的摘要中估算出分位数值。
- `accuracy` 默认值为 10000，相对误差约为 ±0.0001（0.01%）。

注意 percentile 和 approx_percentile 不仅可以计算百分位数，其他分位数也可以计算，完全取决于你传入的 p 值，例如：p = 0.5 计算的值同时是：

- 第 2 二分位数。
- 第 5 十分位数。
- 第 50 百分位数。
- 第 500 千分位数。

p = 0.001 计算的是第 1 千分位数。

### 本福特系数

```python
# 本福特系数，单日汇总：
def theil_t_index(income):
    # 确保所有收入都是正数
    income = np.array(income)
    if any(income <= 0):
        raise ValueError("所有收入必须是正数")
    # 计算总收入
    total_income = np.sum(income)
    # 计算收入份额
    income_share = income / total_income
    # 计算每个人的收入与平均收入的比率
    ratio = income_share / (1 / len(income))
    # 计算Theil的T指数
    theil_t = np.sum(income_share * np.log(ratio))
    return theil_t
```

### 基尼系数

```python
# 基尼系数基尼系数（Gini coefficient），单日汇总:
def gini_coefficient(income):
    # 首先对收入进行排序
    income = np.sort(income)
    # 计算累积人口和累积收入
    n = income.size
    cumulative_population = np.linspace(1/n, 1, n)
    cumulative_income = np.cumsum(income) / income.sum()
    # 计算洛伦兹曲线下的面积和对角线下的面积（即完全平等情况下的面积）
    # 洛伦兹曲线下的面积可以通过累积收入的平均值减去0.5/n（因为是从1/n开始的）计算
    lorenz_curve_area = cumulative_income.mean() - 0.5 / n
    # 因为完全平等线下的面积是0.5，所以基尼系数为1减去2倍的洛伦兹曲线面积
    gini = 1 - 2 * lorenz_curve_area
    return gini
```

### ADF 指数

```python
# ADF 指数（Python adfuller），单日汇总：
from statsmodels.tsa.stattools import adfuller
```

### 变异系数（波动系数）

```sql
SELECT stddev_pop(col) / avg(col);
```

### Pandas 生成日期序列

```python
import pandas as pd

start_date = '2024-02-01'
end_date = '2024-07-31'

date_range = pd.date_range(start=start_date, end=end_date)
print([date for date in date_range.strftime('%Y-%m-%d')])
```
