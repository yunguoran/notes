# Bast Practices

## Column to Row

| week | utmSourceType | payerNum | orderNum
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
