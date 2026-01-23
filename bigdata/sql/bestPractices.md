# 最佳实践

## 列转行

| week | utmSourceType | payerNum | orderNum |
| ------ | ------ | ------ | ------ |
| 2022-09-19 | 公众号菜单 | 0 | 0 |
| 2022-09-19 | 其他 | 5 | 6 |
| 2022-09-19 | 微信广告 | 1 | 1 |
| 2022-09-26 | 公众号菜单 | 6 | 6 |
| 2022-09-26 | 其他 | 74 | 82 |
| 2022-09-26 | 微信广告 | 69 | 72 |
| 2022-10-03 | 公众号菜单 | 13 | 15 |
| 2022-10-03 | 其他 | 27 | 29 |
| 2022-10-03 | 微信广告 | 49 | 50 |
| 2022-10-10 | 公众号菜单 | 8 | 9 |
| 2022-10-10 | 其他 | 23 | 24 |
| 2022-10-10 | 微信广告 | 29 | 29 |

| num | utmSourceType | 2022-09-19 | 2022-09-26 | 2022-10-03 | 2022-10-10 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| payerNum | 微信广告 | 1 | 69 | 49 | 29 |
| payerNum | 公众号菜单 | 0 | 6 | 13 | 8 |
| payerNum | 其他 | 5 | 74 | 27 | 23 |
| orderNum | 微信广告 | 1 | 72 | 50 | 29 |
| orderNum | 公众号菜单 | 0 | 6 | 15 | 9 |
| orderNum | 其他 | 6 | 82 | 29 | 24 |

```sql
SELECT 'payerNum' AS num, *
FROM (
    SELECT week, utmSourceType, payerNum
    FROM tmpWeek
)
PIVOT (
    max(payerNum) FOR week IN ('2022-09-19', '2022-09-26', '2022-10-03', '2022-10-10')
)
UNION ALL
SELECT 'orderNum' AS num, *
FROM (
    SELECT week, utmSourceType, orderNum
    FROM tmpWeek
)
PIVOT (
    max(orderNum) FOR week IN ('2022-09-19', '2022-09-26', '2022-10-03', '2022-10-10')
);
```

```python
columns = ['payerNum', 'orderNum']
sqls = []

sql = """
SELECT '{column}' AS num, *
FROM (
    SELECT week, utmSourceType, {column}
    FROM tmpWeek
)
PIVOT (
    max({column}) FOR week IN ('2022-09-19', '2022-09-26', '2022-10-03', '2022-10-10')
)
"""

for column in columns:
    sqls.append(sql.format(column=column))

sql = 'UNION ALL'.join(sqls)
spark.sql(sql).show()
```

## [Divide the number field infinitely by fixed step](https://stackoverflow.com/questions/75066077/how-to-divide-the-number-field-infinitely-by-fixed-step-in-spark-sql)

```sql
SELECT
    intervalLeft,
    concat("[", intervalLeft, ", ", intervalLeft + 5, ")") AS numInterval,
    count(number) AS count
FROM (
    SELECT number, floor(number / 5 ) * 5 AS intervalLeft
    FROM example
)
GROUP BY intervalLeft
ORDER BY intervalLeft;
```

## [Convert two columns of dataFrame into orderedDict](https://stackoverflow.com/questions/75141364/how-to-convert-two-columns-of-dataframe-into-an-ordereddict-in-python)

```python
import pandas as pd

data = [
    ("2022-12-15", "2022-12-18"),
    ("2022-12-19", "2022-12-21"),
    ("2022-12-22", "2022-12-24"),
    ("2022-12-26", "2022-12-27"),
    ("2022-12-29", "2022-12-30"),
    ("2022-12-02", "2022-12-04"),
    ("2022-12-06", "2022-12-07"),
    ("2022-12-07", "2022-12-08"),
    ("2022-12-13", "2022-12-14"),
    ("2023-01-01", "2023-01-03"),
]

df = spark.createDataFrame(data).toDF(*('startDate', 'endDate')).toPandas()
dictTest = df.set_index('startDate')['endDate'].to_dict()

print(dictTest)

for k,v in dictTest.items():
    print(f'StartDate is {k} and corresponding endDate is {v}.')
```

## 低版本 Hive 生成日期序列

```sql
SELECT date_add('2026-01-01', pos) AS `date`
FROM (
    SELECT posexplode(split(space(datediff('2026-12-31', '2026-01-01')), ' ')) AS (pos, val)
) AS t;
```

## 日期维表生成 SQL

```sql
SELECT
    `date`,
    date_id,
    date_name,
    CASE
        WHEN `date` = '2026-12-30' THEN '2026W53'
        WHEN `date` = '2026-12-31' THEN '2026W53'
        ELSE concat('2026W', week_id)
    END AS week_id,
    ten_id,
    month_id,
    season_id,
    half_id,
    year_id,
    week_day,
    row_number() OVER (PARTITION BY ten_id ORDER BY `date`) AS ten_day,
    month_day,
    season_day,
    half_day,
    year_day,
    week,
    cast(substr(ten_id, 6, 8) AS INT) AS ten,
    month,
    season,
    half_year,
    CASE
        WHEN week_day IN (1, 2, 3, 4, 5) AND `date` NOT IN (
            '2026-01-01', '2026-01-02', -- 元旦
            '2026-02-16', '2026-02-17', '2026-02-18', '2026-02-19', '2026-02-20', '2026-02-23', -- 春节
            '2026-04-06', -- 清明节
            '2026-05-01', '2026-05-04', '2026-05-05', -- 劳动节
            '2026-06-19', -- 端午节
            '2026-09-25', -- 中秋节
            '2026-10-01', '2026-10-02', '2026-10-05', '2026-10-06', '2026-10-07' -- 国庆节
            ) THEN '是'
        WHEN is_exchange = '是' THEN '是'
        ELSE '否'
    END AS is_workday,
    is_national,
    is_labour,
    is_spring,
    is_exchange
FROM (
    SELECT
        row_number() OVER (ORDER BY `date`) AS num,
        `date`,
        date_format(`date`, 'yyyyMMdd') AS date_id,
        concat(year(`date`), '年', date_format(`date`, 'MM'), '月', date_format(`date`, 'dd'), '日') AS date_name,
        CASE
            WHEN weekofyear(`date`) < 10 THEN concat('0', weekofyear(`date`))
            ELSE string(weekofyear(`date`))
        END AS week_id,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-01-10' THEN '2026T01'
            WHEN `date` BETWEEN '2026-01-11' AND '2026-01-20' THEN '2026T02'
            WHEN `date` BETWEEN '2026-01-21' AND '2026-01-31' THEN '2026T03'
            WHEN `date` BETWEEN '2026-02-01' AND '2026-02-10' THEN '2026T04'
            WHEN `date` BETWEEN '2026-02-11' AND '2026-02-20' THEN '2026T05'
            WHEN `date` BETWEEN '2026-02-21' AND '2026-02-28' THEN '2026T06'
            WHEN `date` BETWEEN '2026-03-01' AND '2026-03-10' THEN '2026T07'
            WHEN `date` BETWEEN '2026-03-11' AND '2026-03-20' THEN '2026T08'
            WHEN `date` BETWEEN '2026-03-21' AND '2026-03-31' THEN '2026T09'
            WHEN `date` BETWEEN '2026-04-01' AND '2026-04-10' THEN '2026T10'
            WHEN `date` BETWEEN '2026-04-11' AND '2026-04-20' THEN '2026T11'
            WHEN `date` BETWEEN '2026-04-21' AND '2026-04-30' THEN '2026T12'
            WHEN `date` BETWEEN '2026-05-01' AND '2026-05-10' THEN '2026T13'
            WHEN `date` BETWEEN '2026-05-11' AND '2026-05-20' THEN '2026T14'
            WHEN `date` BETWEEN '2026-05-21' AND '2026-05-31' THEN '2026T15'
            WHEN `date` BETWEEN '2026-06-01' AND '2026-06-10' THEN '2026T16'
            WHEN `date` BETWEEN '2026-06-11' AND '2026-06-20' THEN '2026T17'
            WHEN `date` BETWEEN '2026-06-21' AND '2026-06-30' THEN '2026T18'
            WHEN `date` BETWEEN '2026-07-01' AND '2026-07-10' THEN '2026T19'
            WHEN `date` BETWEEN '2026-07-11' AND '2026-07-20' THEN '2026T20'
            WHEN `date` BETWEEN '2026-07-21' AND '2026-07-31' THEN '2026T21'
            WHEN `date` BETWEEN '2026-08-01' AND '2026-08-10' THEN '2026T22'
            WHEN `date` BETWEEN '2026-08-11' AND '2026-08-20' THEN '2026T23'
            WHEN `date` BETWEEN '2026-08-21' AND '2026-08-31' THEN '2026T24'
            WHEN `date` BETWEEN '2026-09-01' AND '2026-09-10' THEN '2026T25'
            WHEN `date` BETWEEN '2026-09-11' AND '2026-09-20' THEN '2026T26'
            WHEN `date` BETWEEN '2026-09-21' AND '2026-09-30' THEN '2026T27'
            WHEN `date` BETWEEN '2026-10-01' AND '2026-10-10' THEN '2026T28'
            WHEN `date` BETWEEN '2026-10-11' AND '2026-10-20' THEN '2026T29'
            WHEN `date` BETWEEN '2026-10-21' AND '2026-10-31' THEN '2026T30'
            WHEN `date` BETWEEN '2026-11-01' AND '2026-11-10' THEN '2026T31'
            WHEN `date` BETWEEN '2026-11-11' AND '2026-11-20' THEN '2026T32'
            WHEN `date` BETWEEN '2026-11-21' AND '2026-11-30' THEN '2026T33'
            WHEN `date` BETWEEN '2026-12-01' AND '2026-12-10' THEN '2026T34'
            WHEN `date` BETWEEN '2026-12-11' AND '2026-12-20' THEN '2026T35'
            WHEN `date` BETWEEN '2026-12-21' AND '2026-12-31' THEN '2026T36'
        END AS ten_id,
        date_format(`date`, 'yyyyMM') AS month_id,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-03-31' THEN '2026Q1'
            WHEN `date` BETWEEN '2026-04-01' AND '2026-06-30' THEN '2026Q2'
            WHEN `date` BETWEEN '2026-07-01' AND '2026-09-30' THEN '2026Q3'
            WHEN `date` BETWEEN '2026-10-01' AND '2026-12-31' THEN '2026Q4'
        END AS season_id,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-06-30' THEN '2026H1'
            WHEN `date` BETWEEN '2026-07-01' AND '2026-12-31' THEN '2026H2'
        END AS half_id,
        year(`date`) AS year_id,
        dayOfWeek(date_add(`date`, -1)) AS week_day,
        dayOfMonth(`date`) AS month_day,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-03-31' THEN datediff(`date`, '2026-01-01') + 1
            WHEN `date` BETWEEN '2026-04-01' AND '2026-06-30' THEN datediff(`date`, '2026-04-01') + 1
            WHEN `date` BETWEEN '2026-07-01' AND '2026-09-30' THEN datediff(`date`, '2026-07-01') + 1
            WHEN `date` BETWEEN '2026-10-01' AND '2026-12-31' THEN datediff(`date`, '2026-10-01') + 1
        END AS season_day,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-06-30' THEN datediff(`date`, '2026-01-01') + 1
            WHEN `date` BETWEEN '2026-07-01' AND '2026-12-31' THEN datediff(`date`, '2026-07-01') + 1
        END AS half_day,
        row_number() OVER (ORDER BY `date`) AS year_day,
        CASE
            WHEN `date` = '2026-12-30' THEN '53'
            WHEN `date` = '2026-12-31' THEN '53'
            ELSE weekofyear(`date`)
        END AS week,
        month(`date`) AS month,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-03-31' THEN 1
            WHEN `date` BETWEEN '2026-04-01' AND '2026-06-30' THEN 2
            WHEN `date` BETWEEN '2026-07-01' AND '2026-09-30' THEN 3
            WHEN `date` BETWEEN '2026-10-01' AND '2026-12-31' THEN 4
        END AS season,
        CASE
            WHEN `date` BETWEEN '2026-01-01' AND '2026-06-30' THEN 1
            WHEN `date` BETWEEN '2026-07-01' AND '2026-12-31' THEN 2
        END AS half_year,
        if(`date` BETWEEN '2026-10-01' AND '2026-10-07', '是', '否') AS is_national,
        if(`date` BETWEEN '2026-05-01' AND '2026-05-05', '是', '否') AS is_labour,
        if(`date` BETWEEN '2026-02-15' AND '2026-02-23', '是', '否') AS is_spring,
        CASE
            WHEN `date` IN (
                '2026-01-04', -- 元旦调休
                '2026-02-14', '2026-02-28', -- 春节调休
                -- '2026-04-07', -- 清明节调休
                '2026-05-09', -- 劳动节调休
                -- '2026-09-14', -- 中秋节调休
                '2026-09-20', '2026-10-10' -- 国庆节调休
            ) THEN '是'
            ELSE '否'
        END AS is_exchange
    FROM (
        SELECT date_add('2026-01-01', pos) AS `date`
        FROM (
            SELECT posexplode(split(space(datediff('2026-12-31', '2026-01-01')), ' ')) AS (pos, val)
        ) AS t
    ) AS t
) AS t
ORDER BY `date`;
```

## UTF-8 编码下四字节的 Unicode 字符

Unicode 的字符空间被划分为 17 个平面，每个平面包含 $2^{16}$ (65,536) 个码点（Code Points）。

- 基本多语言平面 (BMP - Basic Multilingual Plane)。
    - 这是第 0 号平面（Plane 0），码点范围从 `U+0000` 到 `U+FFFF`。
    - 涵盖了世界上绝大多数现代文字（汉字、英文、藏文等）以及最常用的标点符号。
    - 在 UTF-8 编码下通常占用 **1 到 3 个字节**。
- 增补平面 (Supplementary Planes)：这是第 1 到 16 号平面，码点范围从 `U+10000` 到 `U+10FFFF`。
    - 第 1 平面包含绝大多数现代 Emoji 表情（如🥰，码点为 `U+1F970`）。
    - 在 UTF-8 中必须使用 **4 个字节**。
    - 许多旧的正则引擎将这些字符视为两个代理对（Surrogate Pairs），如果只搜索单字符属性（如 `\p{So}`），引擎可能只会识别到代理对的一部分从而匹配失败。

Hive 元数据库 (Metastore) 的编码限制。

- Hive 的元数据（表名、分区名、字段备注等）存储在外部关系型数据库中（通常是 MySQL），
- 很多 MySQL 默认设置的 `utf8` 字符集实际上只支持最多 3 字节的字符。
- 当含有 🥰 的数据进入分区字段或触发某些元数据操作时，由于 MySQL 无法存储 4 字节字符，会导致数据库报错（如 `Incorrect string value`），从而让整个 Hive 任务失败。

```sql
-- 匹配 Unicode 基本多语言平面内的字符。
SELECT *
FROM your_table
WHERE your_column RLIKE '[\x{0000}-\x{FFFF}]';

-- 匹配 Unicode 增补平面内的字符。
SELECT *
FROM your_table
WHERE your_column RLIKE '[\\x{10000}-\\x{10FFFF}]';

-- 提取第一个 Unicode 增补平面内的字符。
SELECT regexp_extract(your_column, '([\\x{10000}-\\x{10FFFF}])', 1)
FROM your_table
WHERE your_column RLIKE '[\\x{10000}-\\x{10FFFF}]';

-- 提取全部Unicode 增补平面内的字符。
SELECT regexp_extract_all(your_column, '([\\x{10000}-\\x{10FFFF}])', 1)
FROM your_table
WHERE your_column RLIKE '[\\x{10000}-\\x{10FFFF}]';

-- 去掉 Unicode 增补平面内的字符。
SELECT regexp_replace(your_column, '[\\x{10000}-\\x{10FFFF}]', '') AS cleaned_column
FROM your_table;
```
