# HTML 教程

## HTML 简介

浏览器访问网站，其实就是从服务器下载 HTML（HyperText Markup Language）代码，然后渲染出网页。

### 网页的基本概念

- 学习 HTML 语言，就是学习各种标签的用法。
    - HTML 标签名大小写不敏感。
    - 一些标签不是成对使用，而是只有开始标签，没有结束标签，比如 `<meta>` 标签。这种单独使用的标签，通常是因为标签本身就足够完成功能了，不需要标签之间的内容。

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
  <!-- <head> 标签是一个容器标签，用于放置网页的元信息。它的内容不会出现在网页上，而是为网页渲染提供额外信息。 -->
  <head>
    <!-- <meta> 标签用于设置或说明网页的元数据，必须放在 <head> 里面。一个 <meta> 标签就是一项元数据，网页可以有多个 <meta>。<meta> 标签约定放在 <head> 内容的最前面。 -->
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

![URL](/images/frontend/html/url.png)

- 主机（host）又称为域名（domain）。
- 有 18 个字符属于 URL 的保留字符，只能在给定的位置出现。网址的其他部分如果要使用这些保留字符，必须使用它们的转义形式。
    - URL 字符转义的方法是，在这些字符的十六进制 ASCII 码前面加上百分号（%）。
    - 空格的转义形式是 `%20`。
- `<base>` 标签指定网页内部的所有相对 URL 的计算基准。整张网页只能有一个 `<base>` 标签，而且只能放在 `<head>` 里面。它是单独使用的标签，没有闭合标签。

    ```html
    <head>
      <base href="https://www.example.com/files/" target="_blank">
    </head>
    ```

    - `<base>` 标签的 href 属性给出计算的基准网址，target 属性给出如何打开链接的说明。
    - 一旦设置了 `<base>`，就对整个网页都有效。如果要改变某个链接的行为，只能用绝对链接替代相对链接。这时锚点也是针对 `<base>` 计算的，而不是针对当前网页的 URL。

## 元素的属性

属性名不区分大小写。

全局属性（global attributes）是所有元素都可以使用的属性。

- `id` 属性是元素在网页内的唯一标识符。比如，网页可能包含多个 `<p>` 标签，`id` 属性可以指定每个 `<p>` 标签的唯一标识符。
    - `id` 属性的值必须是全局唯一的。`id` 属性的值不得包含空格。
    - `id` 属性的值还可以在最前面加上 `#`，放到 URL 中作为锚点。
- `title` 属性用来为元素添加附加说明。鼠标悬浮在元素上面时，会将 `title` 属性值作为浮动提示，显示出来。

    ```html
    <div title="版权说明">
        <p>本站内容使用创意共享许可证，可以自由使用。</p>
    </div>
    ```

- 网页通常使用鼠标操作，但是某些情况下，用户可能希望使用键盘，或者只有键盘可以用。因此，浏览器允许使用 Tab 键遍历网页元素。也就是说，只要不停按下 Tab 键，网页的焦点就会从一个元素转移到另一个元素，选定焦点元素以后，就可以进行下一步操作，比如按下回车键访问某个链接，或者直接在某个输入框输入文字。HTML 提供了 `tabindex` 属性以便在用户按下 Tab 键的时候，浏览器知道跳到哪一个元素。
    - `tabindex` 属性的值是一个整数，表示用户按下 Tab 键的时候，网页焦点转移的顺序。
    - 负整数：该元素可以获得焦点（比如使用 JS 的 `focus()` 方法），但不参与 Tab 键对网页元素的遍历。这个值通常是 `-1`。
    - `0`：该元素参与 Tab 键的遍历，顺序由浏览器指定，通常是按照其在网页里面出现的位置。
    - 正整数：网页元素按照从小到大的顺序参与 Tab 键的遍历。如果多个元素的 `tabindex` 属性相同，则按照在网页源码里面出现的顺序遍历。
- `accesskey` 属性指定网页元素获得焦点的快捷键，该属性的值必须是单个的可打印字符。
    - Chrome 浏览器在 Windows 系统和 Linux 系统的快捷键是 `Alt + 字符键`。
- `style` 属性用来指定当前元素的 CSS 样式。
- `hidden` 是一个布尔属性，表示当前的网页元素不再跟页面相关，因此浏览器不会渲染这个元素。
    - CSS 的可见性设置，高于 `hidden` 属性。如果 CSS 设为该元素可见，`hidden` 属性将无效。
- `lang` 属性的值，必须符合 [BCP47](https://www.rfc-editor.org/bcp/bcp47.txt) 的标准。
- `translate` 属性只用于文本元素，用来指示翻译软件是否翻译该文本。属性值为 `yes` 或 `no`。
- `contenteditable` 属性允许用户修改内容，属性值为枚举类型的 `true` 或 `false`。
- 浏览器一般会自带拼写检查功能，编辑内容时，拼错的单词下面会显示红色的波浪线。`spellcheck` 属性表示是否打开拼写检查。属性值为枚举类型的 `true` 或 `false`。该属性只在编辑时生效，因此必须和 `contenteditable` 属性连用，对于不可编辑的元素，`spellcheck` 属性无效。

## 字符编码

服务器向浏览器发送 HTML 网页文件时，会通过 HTTP 头信息，声明网页的编码方式。

- 字符的数字表示法
    - 每个字符有一个 Unicode 号码，称为码点（code point）。
    - 字符的码点表示法是 `&#N` 或者 `&#xN`（N 代表码点）。比如，字符 a 可以写成 `&#97` 或者 `&#x61`，字符`中`可以写成 `&#20013` 或者 `&#x4e2d`。
    - HTML 标签本身不能使用码点表示，否则浏览器会认为这是所要显示的文本内容。
- 字符的实体表示法
    - 为了能够快速输入，HTML 为一些特殊字符，规定了容易记忆的名字，允许通过名字来表示它们，这称为实体表示法（entity）。
    - 实体的写法是 `&name`。例如空格可以写为：`&nbsp`。

## 语义结构

### `<header>`

- `<header>` 既可以表示整个网页的头部，也可以表示一篇文章或者一个区块的头部。
- 一个页面可能包含多个 `<header>`，但 `<header>` 里面不能包含另一个 `<header>` 或 `<footer>`。

### `<footer>`

- `<footer>` 标签表示网页、文章或章节的尾部。如果用于整张网页的尾部，就称为“页尾”，通常包含版权信息或者其他相关信息。
- `<footer>` 不能嵌套，即内部不能放置另一个 `<footer>`，也不能放置 `<header>`。

### `<main>`

- `<main>` 标签表示页面的主体内容，一个页面只能有一个 `<main>`。
- `<main>` 是顶层标签，不能放置在 `<header>`、`<footer>`、`<article>`、`<aside>`、`<nav>` 等标签之中。

### `<article>`

- `<article>` 通常用来表示一篇文章或者一个论坛帖子，它可以有自己的标题 `<h1>` 到 `<h6>`。
- 一个网页可以包含一个或多个 `<article>`。

### `<aside>`

- `<aside>` 标签用来放置与网页或文章主要内容间接相关的部分。
- 网页级别的 `<aside>`，可以用来放置侧边栏，但不一定就在页面的侧边；文章级别的 `<aside>`，可以用来放置补充信息、评论或注释。

### `<section>`

- `<section>` 标签表示一个含有主题的独立部分，通常用在文档里面表示一个章节，比如 `<article>` 可以包含多个 `<section>`。
- `<section>` 总是多个一起使用，一个页面不能只有一个 `<section>`。

### `<nav>`

- `<nav>` 标签用于放置页面或文档的导航信息。
- `<nav>` 往往放置在 `<header>` 里面，不适合放入 `<footer>`。

### `<hgroup>`

- 如果主标题包含多级标题（比如带有副标题），那么可以使用 `<hgroup>` 标签，将多级标题放在其中。
- `<hgroup>` 只能包含 `<h1>`~`<h6>`，不能包含其他标签。

## 文本标签

### `<div>`

- `<div>` 是块级元素。
- 带有语义的块级标签始终应该优先使用，当且仅当没有其他语义元素合适时才可以使用 `<div>`。

### `<p>`

`<p>` 标签是一个块级元素，代表文章的一个段落（paragraph）。

### `<span>`

- `<span>` 是一个无语义的的行内标签。
- 它通常用作 CSS 样式的钩子，如果需要对某些行内内容指定样式，就可以把它们放置在 `<span>` 内。

### `<br>`，`<wbr>`

- `<br>` 让网页产生一个换行效果。该标签是单独使用的，没有闭合标签。
- 块级元素的间隔不要使用 `<br>` 来产生，而要使用 CSS 指定。
- `<wbr>` 标签表示一个可选的断行。如果一行的宽度足够，则不断行；如果宽度不够需要断行，就在 `<wbr>`的位置的断行。它是为了防止浏览器在一个很长的单词中间，不正确地断行或者不断行，所以事先标明可以断行的位置。

### `<hr>`

- `<hr>` 用来在一篇文章中分隔两个不同的主题，浏览器会将其渲染为一根水平线。该标签是单独使用的，没有闭合标签。
- 该标签是历史遗留下来的，尽量避免使用。主题之间的分隔可以使用 `<section>`，如果想要水平线的效果，可以使用 CSS。

### `<pre>`

- `<pre>` 是一个块级元素，表示保留原来的格式（preformatted），即浏览器会保留该标签内部原始的换行和空格。浏览器默认以等宽字体显示标签内容。
- HTML 标签在 `<pre>` 里面还是起作用的。`<pre>` 只保留空格和换行，不会保留 HTML 标签。

### `<strong>`

`<strong>` 是一个行内元素，表示它包含的内容具有很强的重要性，需要引起注意。浏览器会以粗体显示内容。

### `<em>`

`<em>` 是一个行内标签，表示强调（emphasize），浏览器会以斜体显示它包含的内容。

### `<sub>`，`<sup>`，`<var>`

- `<sub>` 标签将内容变为下标，`<sup>` 标签将内容变为上标。它们都是行内元素。
- `<var>` 标签表示代码或数学公式的变量。

### `<u>`，`<s>`

- `<u>` 标签是一个行内元素，表示对内容提供某种注释，提醒用户这里可能有问题，基本上只用来表示拼写错误。浏览器默认以下划线渲染内容。
- `<u>` 会产生下划线，由于链接也默认带有下划线，万一确有必要使用，最好使用 CSS 改变 `<u>` 的默认样式。
- `<s>` 标签是一个行内元素，为内容加上删除线。

### `<blockquote>`，`<cite>`，`<q>`

```html
<blockquote cite="https://quote.example.com">
  <p>天才就是 1% 的天赋和99%的汗水。</p>
</blockquote>
<cite>-- 爱迪生</cite>

<p>
  莎士比亚的《哈姆雷特》有一句著名的台词：
  <q cite="https://quote.example.com">活着还是死亡，这是一个问题。</q>
</p>
```

- `<blockquote>` 是一个块级标签，表示引用他人的话。浏览器会在样式上，与正常文本区别显示。
- `<blockquote>` 标签有一个 `cite` 属性，它的值是一个网址，表示引言来源，不会显示在网页上。
- `<cite>` 标签表示引言出处或者作者，浏览器默认使用斜体显示这部分内容。
- `<cite>` 不一定跟 `<blockquote>` 一起使用。如果文章中提到资料来源，也可以单独使用。
- `<q>` 是一个行内标签，也表示引用。
- 浏览器默认会斜体显示 `<q>` 的内容，并且会自动添加半角的双引号。

### `<code>`

- `<code>` 标签是一个行内元素，表示标签内容是计算机代码，浏览器默认会以等宽字体显示。
- 如果要表示多行代码，`<code>` 标签必须放在 `<pre>` 内部。`<code>` 本身仅表示一行代码。

### `<kbd>`，`<samp>`

- `<kbd>` 标签是一个行内元素，原意是用户从键盘输入的内容，现在扩展到各种输入，包括语音输入。浏览器默认以等宽字体显示标签内容。
- `<kbd>` 可以嵌套，方便指定样式。
- `<samp>` 标签是一个行内元素，表示计算机程序输出内容的一个例子。浏览器默认以等宽字体显示。

### `<mark>`

```html
<blockquote>
床前明月光，疑是地上霜。<mark>举头望明月，低头思故乡。</mark>
</blockquote>
```

- `<mark>` 是一个行内标签，表示突出显示的内容。Chrome 浏览器默认会以亮黄色背景，显示该标签的内容。
- `<mark>` 很适合在引用的内容（`<q>` 或 `<blockquote>`）中，标记出需要关注的句子。

### `<small>`

`<small>` 是一个行内标签，浏览器会将它包含的内容以小一号的字号显示，不需要使用 CSS 样式。

### `<time>`，`<data>`

```html
<p>运动会预定<time datetime="2015-06-10">下周三</time>举行。</p>
<p>音乐会在<time datetime="20:00">晚上八点</time>开始。</p>
<p>本次马拉松比赛第一名是<data value="39">张三</data></p>。
```

- `<time>` 是一个行内标签，为跟时间相关的内容提供机器可读的格式。
- 上面代码中 `<time>` 表示下周三的具体日期。这方便搜索引擎抓取，或者下一步的其他处理。
- `<data>` 标签与 `<time>` 类似，也是提供机器可读的内容，但是用于非时间的场合。

### `<address>`

```html
<footer>
  <address>
    文章的相关问题请联系<a href="mailto:zhangsan@example.com">张三McClure</a>。
  </address>
</footer>
```

- `<address>` 标签是一个块级元素，表示某人或某个组织的联系方式。
    - 如果是文章里提到的地址（比如提到搬家前的地址），而不是联系信息，不要使用 `<address>` 标签。
    - `<address>` 的内容不得有非联系信息，比如发布日期。
    - `<address>` 不能嵌套。
    - 通常 `<address>` 会放在 `<footer>` 里面。

### `<abbr>`

`<abbr>` 标签是一个行内元素，表示标签内容是一个缩写。它的 `title` 属性给出缩写的完整形式，或者缩写的描述。

### `<ins>`，`<del>`

- `<ins>` 标签是一个行内元素，表示原始文档添加（insert）的内容。`<del>` 表示删除（delete）的内容。它们通常用于展示文档的删改。
- 浏览器默认为 `<del>` 标签的内容加上删除线，为 `<ins>` 标签的内容加上下划线。
- 这两个标签都有以下属性。
    - `cite`：该属性的值是一个 URL，表示该网址可以解释本次删改。
    - `datetime`：表示删改发生的时间。

### `<dfn>`

```html
<p>
  <dfn><abbr title="acquired immune deficiency syndrome">AIDS</abbr></dfn>的全称是获得性免疫缺陷综合征。
</p>
```

`<dfn>` 是一个行内元素，表示标签内容是一个术语（definition），本段或本句包含它的定义。

### `<ruby>`

```html
<ruby>
    汉<rp>(</rp><rt>han</rt><rp>)</rp>
    字<rp>(</rp><rt>zi</rt><rp>)</rp>
</ruby>
```

- `<ruby>` 标签是一个行内元素，也是一个容器标签。
- `<ruby>` 标签表示文字的语音注释，主要用于东亚文字，比如汉语拼音和日语的片假名。它默认将语音注释，以小字体显示在文字的上方。
    - `<rp>` 标签是为不支持语音注释的浏览器提供一个兼容方案。对于那些支持语音注释的浏览器，该标签的内容不显示。
    - `<rp>` 标签一般用于放置圆括号，如果遇到不支持的浏览器，就会将语音注释显示在括号里面。
    - `<rt>` 标签用于放置语音注释。

### `<bdo>`，`<bdi>`

- `<bdo>` 标签是一个行内元素，表示文字方向与网页主体内容的方向不一致。
- `<bdo>` 标签里面的文字，会以相反的方向渲染。
- `<bdo>` 的 `dir` 属性，指定具体的文字方向。它有两个值，`ltr` 表示从左到右，`rtl` 表示从右到左。
- `<bdi>` 标签用于不确定文字方向的情况，由浏览器自己决定。

## 列表标签

- `<ol>` 标签是一个有序列表容器（ordered list），会在内部的列表项前面产生数字编号。
- `<ol>` 标签内部可以嵌套 `<ol>` 标签或 `<ul>` 标签，形成多级列表。
- `<ol>` 标签有以下属性。
    - `reversed` 属性产生倒序的数字列表。
    - `start` 属性的值是一个整数，表示数字列表的起始编号。
    - `type` 属性指定数字编号的样式。目前，浏览器支持以下样式。
        - `a`：小写字母
        - `A`：大写字母
        - `i`：小写罗马数字
        - `I`：大写罗马数字
        - `1`：整数（默认值）
    - 即使编号是字母，`start` 属性也依然使用整数。
- `<ul>` 标签是一个无序列表容器（unordered list），会在内部的列表项前面产生实心小圆点，作为列表符号。
- `<ul>` 标签内部可以嵌套 `<ul>` 或 `<ol>`，形成多级列表。
- `<li>` 表示列表项，用在 `<ol>` 或 `<ul>` 容器之中。
    - 有序列表 `<ol>` 之中，`<li>` 有一个 `value` 属性，定义当前列表项的编号，后面列表项会从这个值开始编号。
- `<dl>` 标签是一个块级元素，表示一组术语的列表（description list）。
    - 术语名（description term）由 `<dt>` 标签定义。
    - 术语解释（description detail）由 `<dd>` 标签定义。`<dl>` 常用来定义词汇表。
    - 多个术语（`<dt>`）对应一个解释（`<dd>`），或者多个解释（`<dd>`）对应一个术语（`<dt>`），都是合法的。
