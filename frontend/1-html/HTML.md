# HTML 教程

## HTML 简介

浏览器访问网站，其实就是从服务器下载 HTML（HyperText Markup Language）代码，然后渲染出网页。

### 网页的基本概念

- 学习 HTML 语言，就是学习各种标签的用法。
    - HTML 标签名是大小不敏感。
    - 一些标签不是成对使用，而是只有开始标签，没有结束标签，比如 `<meta>` 标签，这种单独使用的标签，通常是因为标签本身就足够完成功能了，不需要标签之间的内容。

        ```html
        <meta charset="utf-8">
        ```

    - HTML 语言忽略缩进和换行。
- 所有元素可以分成两大类：块级元素（block）和行内元素（inline）。
    - 块级元素默认占据一个独立的区域，在网页上会自动另起一行，占据 100% 的宽度（`<p>`）。
    - 行内元素默认与其他元素在同一行，不产生换行（`<span>`）。
- 属性（attribute）是标签的额外信息，使用空格与标签名和其他属性分隔。
    - 属性值一般放在双引号里面。
    - 属性名大小写不敏感。

### 网页的基本标签

```html
<!-- 表示文档类型，告诉浏览器如何解析网页。简单声明 doctype 为 html 即可，浏览器就会按照 HTML5 的规则处理网页。 -->
<!DOCTYPE html>
<!-- 一个网页只能有一个 <html> 标签。 -->
<html lang="zh-CN">
  <!-- <head> 标签是一个容器标签，用于放置网页的元信息。它的内容不会出现在网页上，而是为网页  渲染提供额外信息。 -->
  <head>
    <!-- <meta> 标签用于设置或说明网页的元数据，必须放在 <head> 里面。一个 <meta> 标签就是一    项元数据，网页可以有多个 <meta>。<meta> 标签约定放在 <head> 内容的最前面。 -->
    <meta charset="utf-8"> <!-- 网页采用 UTF-8 格式编码 -->
    <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- 网页在手机端可以自动缩放 -->
    <!-- <title> 标签用于指定网页的标题，会显示在浏览器窗口的标题栏。 -->
    <title>Google Chrome</title>
  </head>
  <!-- <body> 标签是一个容器标签，用于放置网页的主体内容。浏览器显示的页面内容，都放置在它的内部。它是 <html> 的第二个子元素，紧跟在 <head> 后面。 -->
  <body></body>
</html>
```

- `<head>` 的子元素一般有下面七个：
    - `<meta>`：设置网页的元数据。
    - `<link>`：连接外部样式表。
    - `<title>`：设置网页标题。
    - `<style>`：放置内嵌的样式表。
    - `<script>`：引入脚本。
    - `<noscript>`：浏览器不支持脚本时，所要显示的内容。
    - `<base>`：设置网页内部相对 URL 的计算基准。
- `<meta>` 标签有五个属性：
    - `charset` 属性，用来指定网页的编码方式几乎总是应该采用 `UTF-8` 编码格式。
    - `name` 属性表示元数据的名字，`content` 属性表示元数据的值。它们合在一起使用，就可以为网页指定一项元数据。
    - `http-equiv` 属性用来补充 HTTP 回应的头信息字段，如果服务器发回的 HTTP 回应缺少某个字段，就可以用它补充（HTTP 相关）。
- 空格和换行
    - 标签内容的头部和尾部的空格，一律忽略不计。
    - 标签内容里面的多个连续空格（包含制表符 `\t`），会被浏览器合并成一个。
    - 浏览器还会将文本里面的换行符（`\n`）和回车符（`\r`），替换成空格。
    - HTML 源码里面的换行，不会产生换行效果。

## URL 简介