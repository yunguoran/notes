# CSS 文本样式

用于设置文本样式的属性通常分为两类：

- 字体样式。
- 文本布局样式。

## 字体

### 颜色（`color` 属性）

`color` 属性设置元素中前景内容的颜色，通常是文本。但也包含使用 `text-decoration` 属性生成的上划线和下划线。

`color` 属性接受任何 [CSS 颜色单位](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units#color)。

### 字体族（`font-family` 属性）

`font-family` 属性可以为文本设置不同的字体，值为一个字体或者字体列表。浏览器只有在访问网站的机器上可用字体时才会应用该字体，如果没有，浏览器就会启用回退机制。
