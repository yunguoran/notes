# HTML（HyperText Markup Language）

本文档摘自[网道的 HTML 教程](https://wangdoc.com/html/)，省略了其中很多不言自明的简单知识，同时也对一些疑难的地方增加了详细说明，并修改了其中多处笔误。

## 简介

- 浏览器访问网站，其实就是从服务器下载 HTML 代码，然后渲染出网页。
- 浏览器右键菜单的 View page source（Ctrl + U），可以展示当前网页的 HTML 源码。

### 网页的基本概念

- 学习 HTML 语言，就是学习各种标签的用法。
    - HTML 标签名大小写不敏感。
    - 一些标签不是成对使用，而是只有开始标签，没有结束标签，比如 `<meta>` 标签。这种单独使用的标签，通常是因为标签本身就足够完成功能了，不需要标签之间的内容。

        ```html
        <meta charset="utf-8">
        ```

    - HTML 语言忽略缩进和换行。
- 所有元素可以分成两大类：块级元素（Block）和行内元素（Inline）。
    - 块级元素默认占据一个独立的区域，在网页上会自动另起一行，占据 100% 的宽度（`<p>`）。
        - `width: auto`：宽度默认撑满父容器。
        - `height: auto`：高度由内容决定，如果没有内容，那么高度就是 `0`。
        - 可以自由设置 `width`、`height` 属性。
    - 行内元素默认与其他元素在同一行，不产生换行（`<span>`）。
        - 默认宽度为内容的宽度。
        - 默认高度为内容的行高，通常由 `font-size` 和 `line-height` 决定。
- 属性（Attribute）是标签的额外信息，使用空格与标签名和其他属性分隔。
    - 属性值一般放在双引号里面。
    - 属性名大小写不敏感。

### 网页的基本标签

```html
<!-- 表示文档类型，告诉浏览器如何解析网页。简单声明 DOCTYPE 为 html 即可，浏览器就会按照 HTML5 的规则处理网页。 -->
<!-- 为了区别于普通的标签，因此大写。 -->
<!DOCTYPE html>
<!-- 一个网页只能有一个 <html> 标签，zh-CN 代表中国大陆。 -->
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
    - `http-equiv` 属性用来补充 HTTP 回应的头信息字段，如果服务器发回的 HTTP 回应缺少某个字段，就可以用它补充。
        - 此处牵扯到 HTTP 的高级用法，后续再补充。
        - `http-equiv` 和 `content` 属性是连用的。
- `<title>` 标签用于指定网页的标题，会显示在浏览器窗口的标题栏。
    - 该标签对于网页在搜索引擎的排序有很大影响，所以应当精心安排。
- `<body>` 标签是一个容器标签，用于放置网页的主体内容。浏览器显示的页面内容，都放置在它的内部。
- 空格和换行
    - 标签内容的头部和尾部的空格，一律忽略不计。
    - 标签内容里面的多个连续空格（包含制表符 `\t`），会被浏览器合并成一个。
    - 浏览器还会将文本里面的换行符（`\n`）和回车符（`\r`），替换成空格。
    - HTML 源码里面的换行，不会产生换行效果。

### 注释

HTML 没有专门的单行注释，只有使用 `<!-- -->` 包裹起来的通用注释，既可用于单行，也可用于多行。

```html
<!-- 这是一个注释 -->
<!--
  <p>hello world</p>
  <p>hello world</p>
-->
```

## URL（Uniform Resource Locator）简介

![URL](/images/frontend/html/url.png)

- `Scheme`（协议）：不包括后面的分隔符（://）。
- `Host`（主机）：此处的主机以域名形式展示，也可以是 IP 地址，使用 IP 地址时不会经 DNS 解析。
- `Port`（端口）：16 bit，因此范围为 0-65535，用以区分同一台主机上的不同服务。
- `Path to the file`（文件路径）：此处文件的概念是广义的，对于 Unix 和 Linux 来讲，一切皆文件，因此 URL 的规范文档保留了这种术语。
- `Parameters`（参数）。
- `Anchor`（锚点）：可以直接定位文档至锚点处。

### URL 字符

有 18 个字符属于 URL 的保留字符，只能在给定的位置出现。网址的其他部分如果要使用这些保留字符，必须使用它们的转义形式。

- URL 字符转义的方法是，在这些字符的十六进制 ASCII 码前面加上百分号（%）。
- URL 的合法字符，其实也可以采用这种转义方法，但是不建议使用。
- 空格的转义形式是 `%20`。

保留字符转义形式如下：

- `!`：%21
- `#`：%23
- `$`：%24
- `&`：%26
- `'`：%27
- `(`：%28
- `)`：%29
- `*`：%2A
- `+`：%2B
- `,`：%2C
- `/`：%2F
- `:`：%3A
- `;`：%3B
- `=`：%3D
- `?`：%3F
- `@`：%40
- `[`：%5B
- `]`：%5D

### `<base>` 标签

`<base>` 标签指定网页内部的所有相对 URL 的计算基准。整张网页只能有一个 `<base>` 标签，而且只能放在 `<head>` 里面。它是单独使用的标签，没有闭合标签。

```html
<head>
    <base href="https://www.example.com/files/" target="_blank">
</head>
```

- `<base>` 标签的 `href` 属性给出计算的基准网址，`target` 属性给出如何打开链接的说明。
- 一旦设置了 `<base>`，就对整个网页都有效。如果要改变某个链接的行为，只能用绝对链接替代相对链接。这时锚点也是针对 `<base>` 计算的，而不是针对当前网页的 URL。

## 元素的属性

- 属性名不区分大小写。
- 布尔属性只要添加了属性名，就表示打开该属性，没有就是关闭。
    - HTML 只会判断这个属性是否存在，`<input type="text" required="false">` 中 `required` 的值依然是 true，只有删除这个属性才表示 false。

### 全局属性

全局属性（Global Attributes）是所有元素都可以使用的属性，不过有些属性对某些元素可能不产生意义。

- `id` 属性是元素在网页内的唯一标识符。比如：网页可能包含多个 `<p>` 标签，`id` 属性可以指定每个 `<p>` 标签的唯一标识符。
    - `id` 属性的值必须是全局唯一的。`id` 属性的值不得包含空格。
    - `id` 属性的值还可以在最前面加上 `#`，放到 URL 中作为锚点。
- `class` 属性用于给元素分配一个或多个类名，多个类名之间用空格分割。
- `title` 属性用来为元素添加附加说明。鼠标悬浮在元素上面时，会将 `title` 属性值作为浮动提示显示出来。
    - 注意和 `<title>` 标签进行区分。

    ```html
    <div title="版权说明">
        <p>本站内容使用创意共享许可证，可以自由使用。</p>
    </div>
    ```

- 网页通常使用鼠标操作，但是某些情况下，用户可能希望使用键盘，或者只有键盘可以用。因此，浏览器允许使用 Tab 键遍历网页元素。也就是说，只要不停按下 Tab 键，网页的焦点就会从一个元素转移到另一个元素，选定焦点元素以后，就可以进行下一步操作，比如按下回车键访问某个链接，或者直接在某个输入框输入文字。HTML 提供了 `tabindex` 属性以便在用户按下 Tab 键的时候，浏览器知道跳到哪一个元素。
    - `tabindex` 属性的值是一个整数，表示用户按下 Tab 键的时候，网页焦点转移的顺序。
        - 负整数：该元素可以获得焦点（比如使用 JavaScript 的 `focus()` 方法），但不参与 Tab 键对网页元素的遍历。这个值通常是 `-1`。
        - `0`：该元素参与 Tab 键的遍历，顺序由浏览器指定，通常是按照其在网页里面出现的顺序。
        - 正整数：网页元素按照从小到大的顺序参与 Tab 键的遍历。如果多个元素的 `tabindex` 属性相同，则按照在网页源码里面出现的顺序遍历。
    - `<input>`、`<textarea>`、`<button>`、`<select>`、`<a href="...">`、`<iframe>` 这些元素默认拥有焦点。
- `accesskey` 属性指定网页元素获得焦点的快捷键，该属性的值必须是单个的可打印字符。
    - Chrome 浏览器在 Windows 系统和 Linux 系统的快捷键是 `Alt + 字符键`。
    - 如果跟操作系统或浏览器级别的快捷键有冲突，将不会生效。
- `style` 属性用来指定当前元素的 CSS 样式。
- `hidden` 是一个布尔属性，表示当前的网页元素不再跟页面相关，因此浏览器不会渲染这个元素。
    - CSS 的可见性设置，高于 `hidden` 属性。如果 CSS 设为该元素可见，`hidden` 属性将无效。
- `lang` 属性的值，必须符合 [BCP47](https://www.rfc-editor.org/bcp/bcp47.txt) 的标准。
- `dir` 属性表示文字的阅读方向，有三个可能的值。
    - `ltr`：从左到右阅读，比如：英语。
    - `rtl`：从右到左阅读，比如：阿拉伯语、波斯语、希伯来语。
    - `auto`：浏览器根据内容的解析结果，自行决定。
- `translate` 属性只用于文本元素，用来指示翻译软件是否翻译该文本。属性值为 `yes` 或 `no`。
- `contenteditable` 属性允许用户修改内容，属性值为**枚举**类型的 `true` 或 `false`。
- 浏览器一般会自带拼写检查功能，编辑内容时，拼错的单词下面会显示红色的波浪线。`spellcheck` 属性表示是否打开拼写检查。属性值为枚举类型的 `true` 或 `false`。该属性只在编辑时生效，因此必须和 `contenteditable` 属性连用，对于不可编辑的元素，`spellcheck` 属性无效。
- `data-` 是自定义属性，如果没有其他属性或元素合适放置数据，就可以放在 `data-` 属性。
    - `data-` 属性只能通过 CSS 或 JavaScript 利用。

        ```css
        /* HTML 代码如下
        <div data-role="mobile">
        Mobile only content
        </div>
        */
        div[data-role="mobile"] {
            display:none;
        }

        /* HTML 代码如下
        <div class="test" data-content="This is the div content">test</div>​
        */
        .test {
            display: inline-block;
        }
        .test:after {
            content: attr(data-content);
        }
        ```

- 事件处理属性，用来响应用户的动作。这些属性的值都是 JavaScript 代码。
    - onClick
    - onFocus
    - onInput
    - ...

## 字符编码

服务器向浏览器发送 HTML 网页文件时，会通过 HTTP 头信息，声明网页的编码方式。

```http
Content-Type: text/html; charset=UTF-8
```

- 字符的数字表示法
    - 每个字符有一个 Unicode 号码，称为码点（Code Point）。
    - 字符的码点表示法是 `&#N`（十进制）或者 `&#xN`（十六进制）其中 N 代表码点。比如，字符 *a* 可以写成 `&#97` 或者 `&#x61`，字符**中**可以写成 `&#20013` 或者 `&#x4e2d`。
    - HTML 标签本身不能使用码点表示，否则浏览器会认为这是所要显示的文本内容。
- 字符的实体表示法
    - 为了能够快速输入，HTML 为一些特殊字符，规定了容易记忆的名字，允许通过名字来表示它们，这称为实体表示法（Entity）。
    - 实体的写法是 `&name`。例如：空格可以写为 `&nbsp`。
        - `<`：`&lt`
        - `>`：`&gt`
        - `"`：`&quot`
        - `'`：`&apos`
        - `&`：`&amp`
        - `©`：`&copy`
        - `#`：`&num`
        - `§`：`&sect`
        - `¥`：`&yen`
        - `$`：`&dollar`
        - `£`：`&pound`
        - `¢`：`&cent`
        - `%`：`&percnt`
        - `*`：`&ast`
        - `@`：`&commat`
        - `^`：`&Hat`
        - `±`：`&plusmn`
        - `>>`：`&raquo`

## 语义结构

HTML 标签的一个重要作用就是声明网页元素的性质，使得用户只看标签，就能了解这个元素的意义，阅读 HTML 源码就能了解网页的大致结构。这被称为 HTML 的语义原则。

### 常用标签

- `<header>`
    - `<header>` 既可以表示整个网页的头部，也可以表示一篇文章或者一个区块的头部。
    - 一个页面可能包含多个 `<header>`，但 `<header>` 里面不能包含另一个 `<header>` 或 `<footer>`。
- `<footer>`
    - `<footer>` 标签表示网页、文章或章节的尾部。如果用于整张网页的尾部，就称为“页尾”，通常包含版权信息或者其他相关信息。
    - `<footer>` 不能嵌套，即内部不能放置另一个 `<footer>`，也不能放置 `<header>`。
- `<main>`
    - `<main>` 标签表示页面的主体内容，一个页面只能有一个 `<main>`。
    - `<main>` 是顶层标签，不能放置在 `<header>`、`<footer>`、`<article>`、`<aside>`、`<nav>` 等标签之中。
- `<article>`
    - `<article>` 通常用来表示一篇文章或者一个论坛帖子，它可以有自己的标题 `<h1>` 到 `<h6>`。
    - 一个网页可以包含一个或多个 `<article>`。
- `<aside>`
    - `<aside>` 标签用来放置与网页或文章主要内容间接相关的部分。
    - 网页级别的 `<aside>`，可以用来放置侧边栏，但不一定就在页面的侧边；文章级别的 `<aside>`，可以用来放置补充信息、评论或注释。
- `<section>`
    - `<section>` 标签表示一个含有主题的独立部分，通常用在文档里面表示一个章节，比如 `<article>` 可以包含多个 `<section>`。
    - `<section>` 总是多个一起使用，一个页面不能只有一个 `<section>`。
- `<nav>`
    - `<nav>` 标签用于放置页面或文档的导航信息。
    - `<nav>` 往往放置在 `<header>` 里面，不适合放入 `<footer>`。
- `<hgroup>`
    - 如果主标题包含多级标题（比如带有副标题），那么可以使用 `<hgroup>` 标签，将多级标题放在其中。
    - `<hgroup>` 只能包含 `<h1>`~`<h6>`，不能包含其他标签。

## 文本标签

- `<div>`
    - `<div>`（Division）是块级元素，中文可以翻译为划分或者分区。
    - 带有语义的块级标签始终应该优先使用，当且仅当没有其他语义元素合适时才可以使用 `<div>`。
- `<p>`
    - `<p>` 标签是一个块级元素，代表文章的一个段落（Paragraph），不仅是文本，任何想以段落显示的内容，比如图片和表单项，都可以放进 `<p>`元素。
- `<span>`
    - `<span>` 是一个无语义的的行内标签。
    - 它通常用作 CSS 样式的钩子，如果需要对某些行内内容指定样式，就可以把它们放置在 `<span>` 内。
- `<br>`，`<wbr>`
    - `<br>` 让网页产生一个换行效果。该标签是单独使用的，没有闭合标签。
    - 块级元素的间隔不要使用 `<br>` 来产生，而要使用 CSS 指定。
    - `<wbr>` 标签表示一个可选的断行。如果一行的宽度足够，则不断行；如果宽度不够需要断行，就在 `<wbr>`的位置的断行。它是为了防止浏览器在一个很长的单词中间，不正确地断行或者不断行，所以事先标明可以断行的位置。
- `<hr>`
    - `<hr>` 用来在一篇文章中分隔两个不同的主题，浏览器会将其渲染为一根水平线。该标签是单独使用的，没有闭合标签。
    - 该标签是历史遗留下来的，尽量避免使用。主题之间的分隔可以使用 `<section>`，如果想要水平线的效果，可以使用 CSS。
- `<pre>`
    - `<pre>` 是一个块级元素，表示保留原来的格式，即浏览器会保留该标签内部原始的换行和空格。浏览器默认以等宽字体显示标签内容。
    - HTML 标签在 `<pre>` 里面还是起作用的。`<pre>` 只原样保留空格和换行，不会原样保留 HTML 标签。
        - `<pre><strong>hello world</strong></pre>`：`<pre>` 标签的内容会加粗显示。
- `<strong>`
    - `<strong>` 是一个行内元素，表示它包含的内容具有很强的重要性，需要引起注意。浏览器会以粗体显示内容。
    - `<b>` 也表示它包含的内容需要引起注意，浏览器会加粗显示，但没有语义，因此总是应该使用 `<strong>` 标签。
- `<em>`
    - `<em>` 是一个行内标签，表示强调（Emphasize），浏览器会以斜体显示它包含的内容。但总是应该使用 CSS 指定样式，而不是使用 `<em>` 标签。
    - `<i>` 语义弱于 `<em>`，因此更加不会使用它。
- `<sub>`，`<sup>`，`<var>`
    - `<sub>` 标签将内容变为下标，`<sup>` 标签将内容变为上标。它们都是行内元素。
    - `<var>` 标签表示代码或数学公式的变量。
- `<u>`，`<s>`
    - `<u>` 标签是一个行内元素，表示对内容提供某种注释，提醒用户这里可能有问题，基本上只用来表示拼写错误。浏览器默认以下划线渲染内容。
    - `<u>` 会产生下划线，由于链接也默认带有下划线，万一确有必要使用，最好使用 CSS 改变 `<u>` 的默认样式。
    - `<s>` 标签是一个行内元素，为内容加上删除线。
- `<blockquote>`，`<cite>`，`<q>`
    - `<blockquote>` 是一个块级标签，表示引用他人的话。浏览器会在样式上，与正常文本区别显示。
    - `<blockquote>` 标签有一个 `cite` 属性，它的值是一个网址，表示引言来源，不会显示在网页上。
    - `<cite>` 标签表示引言出处或者作者，浏览器默认使用斜体显示这部分内容。
    - `<cite>` 不一定跟 `<blockquote>` 一起使用。如果文章中提到资料来源，也可以单独使用。
    - `<q>` 是一个行内标签，也表示引用。浏览器默认会斜体显示 `<q>` 的内容，并且会自动添加半角的双引号。

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

- `<code>`
    - `<code>` 标签是一个行内元素，表示标签内容是计算机代码，浏览器默认会以等宽字体显示。
    - 如果要表示多行代码，`<code>` 标签必须放在 `<pre>` 内部。`<code>` 本身仅表示一行代码。

        ```html
        <pre>
          <code>
            let a = 1;
            console.log(a);
          </code>
        </pre>
        ```

- `<kbd>`，`<samp>`
    - `<kbd>` 标签是一个行内元素，原意是用户从键盘输入的内容，现在扩展到各种输入，包括语音输入。浏览器默认以等宽字体显示标签内容。
    - `<kbd>` 可以嵌套，方便指定样式。
    - `<samp>` 标签是一个行内元素，表示计算机程序输出内容的一个例子。浏览器默认以等宽字体显示。
- `<mark>`
    - `<mark>` 是一个行内标签，表示突出显示的内容。Chrome 浏览器默认会以亮黄色背景，显示该标签的内容。
    - `<mark>` 很适合在引用的内容（`<q>` 或 `<blockquote>`）中，标记出需要关注的句子。

        ```html
        <blockquote>床前明月光，疑是地上霜。<mark>举头望明月，低头思故乡。</mark></blockquote>
        ```

- `<small>`
    - `<small>` 是一个行内标签，浏览器会将它包含的内容以小一号的字号显示，不需要使用 CSS 样式。
- `<time>`，`<data>`
    - `<time>` 是一个行内标签，为跟时间相关的内容提供机器可读的格式。
    - 上面代码中 `<time>` 表示下周三的具体日期。这方便搜索引擎抓取，或者下一步的其他处理。
    - `<data>` 标签与 `<time>` 类似，也提供机器可读的内容，但是用于非时间的场合。

        ```html
        <p>运动会预定<time datetime="2015-06-10">下周三</time>举行。</p>
        <p>音乐会在<time datetime="20:00">晚上八点</time>开始。</p>
        <p>本次马拉松比赛第一名是<data value="39">张三</data></p>。
        ```

- `<address>`
    - `<address>` 标签是一个块级元素，表示某人或某个组织的联系方式。
    - 如果是文章里提到的地址（比如提到搬家前的地址），而不是联系信息，不要使用 `<address>` 标签。
    - `<address>` 的内容不得有非联系信息，比如发布日期。
    - `<address>` 不能嵌套。
    - 通常 `<address>` 会放在 `<footer>` 里面。

        ```html
        <footer>
          <address>
            文章的相关问题请联系<a href="mailto:zhangsan@example.com">张三McClure</a>。
          </address>
        </footer>
        ```

- `<abbr>`
    - `<abbr>` 标签是一个行内元素，表示标签内容是一个缩写。它的 `title` 属性给出缩写的完整形式，或者缩写的描述。
- `<ins>`，`<del>`
    - `<ins>` 标签是一个行内元素，表示原始文档添加（Insert）的内容。`<del>` 表示删除（delete）的内容。它们通常用于展示文档的删改。
    - 浏览器默认为 `<del>` 标签的内容加上删除线，为 `<ins>` 标签的内容加上下划线。
    - 这两个标签都有以下属性。
        - `cite`：该属性的值是一个 URL，表示该网址可以解释本次删改。
        - `datetime`：表示删改发生的时间。

- `<dfn>`
    - `<dfn>` 是一个行内元素，表示标签内容是一个术语（Definition），本段或本句包含它的定义。

        ```html
        <p><dfn><abbr title="acquired immune deficiency syndrome">AIDS</abbr></dfn>的全称是获得性免疫缺陷综合征。</p>
        ```

- `<ruby>`
    - `<ruby>` 标签是一个行内元素，也是一个容器标签。
    - `<ruby>` 标签表示文字的语音注释，主要用于东亚文字，比如汉语拼音和日语的片假名。它默认将语音注释，以小字体显示在文字的上方。
        - `<rp>` 标签是为不支持语音注释的浏览器提供一个兼容方案。对于那些支持语音注释的浏览器，该标签的内容不显示。
        - `<rp>` 标签一般用于放置圆括号，如果遇到不支持的浏览器，就会将语音注释显示在括号里面。
        - `<rt>` 标签用于放置语音注释。

            ```html
            <ruby>
              汉<rp>(</rp><rt>han</rt><rp>)</rp>
              字<rp>(</rp><rt>zi</rt><rp>)</rp>
            </ruby>
            ```

- `<bdo>`，`<bdi>`
    - `<bdo>` 标签是一个行内元素，表示文字方向与网页主体内容的方向不一致。
    - `<bdo>` 标签里面的文字，会以相反的方向渲染。
    - `<bdo>` 的 `dir` 属性，指定具体的文字方向。它有两个值，`ltr` 表示从左到右，`rtl` 表示从右到左。
    - `<bdi>` 标签用于不确定文字方向的情况，由浏览器自己决定。

## 列表标签

- `<ol>` 标签是一个有序列表容器（Ordered List），会在内部的列表项前面产生数字编号。
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

        ```html
        <ol>
            <li>列表项 A</li>
            <li>列表项 B
                <ol>
                    <li>列表项 B1</li>
                    <li>列表项 B2</li>
                    <li>列表项 B3</li>
                </ol>
            </li>
            <li>列表项 C</li>
        </ol>
        ```

- `<ul>` 标签是一个无序列表容器（Unordered List），会在内部的列表项前面产生实心小圆点作为列表符号。它的语义化版本是 `<menu>`。
- `<ul>` 标签内部可以嵌套 `<ul>` 或 `<ol>`，形成多级列表。
- `<li>` 表示列表项，用在 `<ol>` 或 `<ul>` 容器之中。
    - 有序列表 `<ol>` 之中，`<li>` 有一个 `value` 属性，定义当前列表项的编号，后面列表项会从这个值开始编号。

        ```html
        <ol>
            <li>列表项 A</li>
            <li value="4">列表项 B</li>
            <li>列表项 C</li>
        </ol>
        ```

- `<dl>` 标签是一个块级元素，表示一组术语的列表（Description List）。
    - 术语名（Description Term）由 `<dt>` 标签定义。
    - 术语解释（Description Detail）由 `<dd>` 标签定义。`<dl>` 常用来定义词汇表。
    - 多个术语（`<dt>`）对应一个解释（`<dd>`），或者多个解释（`<dd>`）对应一个术语（`<dt>`），都是合法的。

    ```html
    <dl>
        <dt>CPU</dt>
        <dd>中央处理器</dd>

        <dt>Memory</dt>
        <dd>内存</dd>

        <dt>Hard Disk</dt>
        <dd>硬盘</dd>
    </dl>
    ```

## 图像标签

### `<img>`

- `<img>` 标签用于插入图片。它是单独使用的，没有闭合标签。
    - 如果 没有 `<base>` 标签，相对路径会基于当前 HTML 文档所在的位置来解析。
    - 如果 定义了 `<base href="...">`，相对路径会基于 `<base>` 定义的 URL 来解析。
    - `<img>` 默认是一个行内元素，与前后的文字处在同一行。
    - `<img>` 可以放在 `<a>` 标签内部，使得图片变成一个可以点击的链接。
- `alt` 属性用来设定图片的文字说明。图片不显示时（比如下载失败，或用户关闭图片加载），图片的位置上会显示该文本。
- 图片默认以原始大小插入网页，`width` 属性和 `height` 属性可以指定图片显示时的宽度和高度，单位是像素。
- `width` 属性和 `height` 属性只设置了一个，另一个没有设置时，浏览器会根据图片的原始大小，自动设置对应比例的图片宽度或高度。
- `<img>` 导致的图片加载的 HTTP 请求，默认会带有 Referer 的头信息。`referrerpolicy` 属性对这个行为进行设置。
- 有时图片和网页属于不同的网站，网页加载图片就会导致跨域请求，对方服务器可能要求跨域认证。`crossorigin` 属性用来告诉浏览器，是否采用跨域的形式下载图片，默认是不采用。
    - `anonymous`：跨域请求不带有用户凭证（通常是 Cookie）。
    - `use-credentials`：跨域请求带有用户凭证。
- `loading` 指定浏览器对图片的加载行为。
    - `auto`：浏览器默认行为，等同于不使用 `loading` 属性。
    - `lazy`：启用懒加载。
    - `eager`：立即加载资源，无论它在页面上的哪个位置。
    - 由于行内图片的懒加载，可能会导致页面布局重排，所以使用这个属性的时候，最好指定图片的高和宽。

        ```html
        <img src="image.png" loading="lazy" alt="…" width="200" height="200">
        ```

### `<figure>`, `<figcaption>`

- `<figure>` 标签可以理解为一个图像区块，将图像和相关信息封装在一起。`<figcaption>` 是它的可选子元素，表示图像的文本描述，通常用于放置标题，可以出现多个。
- 除了图像，`<figure>` 还可以封装引言、代码、诗歌等等。它等于是一个将主体内容与附加信息，封装在一起的语义容器。

    ```html
    <figure>
        <img src="../images\aopTerminology.jpg">
        <figcaption>示例图片</figcaption>
    </figure>
    ```

### 响应式设计

- `srcset` 属性
    - `srcset` 属性用来指定多张图像，适应不同像素密度的屏幕。它的值是一个逗号分隔的字符串，每个部分都是一张图像的 URL，后面接一个空格，然后是像素密度的描述符。
    - **像素密度描述符格式**是像素密度倍数 + 字母 `x`，1x 表示单倍像素密度。
    - 如果 `srcset` 属性都不满足条件，那么就加载 `src` 属性指定的默认图像。

        ```html
        <img srcset="foo-320w.jpg, foo-480w.jpg 1.5x, foo-640w.jpg 2x" src="foo-640w.jpg">
        ```

- `sizes` 属性
    - 像素密度的适配，只适合显示区域一样大小的图像。如果希望不同尺寸的屏幕，显示不同大小的图像，`srcset` 属性就不够用了，必须搭配`sizes` 属性。
    - **宽度描述符**就是图像原始的宽度，加上字符 `w`。
    - 下面代码中，`sizes` 属性给出了三种屏幕条件，以及对应的图像显示宽度。宽度不超过 440 像素的设备，图像显示宽度为 100%；宽度 441 像素到 900 像素的设备，图像显示宽度为 33%；宽度 900 像素以上的设备，图像显示宽度为 254px。

        ```html
        <img
            srcset="
                foo-160.jpg 160w,
                foo-320.jpg 320w,
                foo-640.jpg 640w,
                foo-1280.jpg 1280w
            "
            sizes="
                (max-width: 440px) 100vw,
                (max-width: 900px) 33vw,
                254px
            "
            src="foo-1280.jpg"
        >
        ```

    - 假定当前设备的屏幕宽度是 `480px` ，浏览器从 `sizes` 属性查询得到，图片的显示宽度是 33vw（即 33%），等于 160px。`srcset` 属性里面，正好有宽度等于 160px 的图片，于是加载 foo-160.jpg。

### `<picture>`

- `<img>` 标签的 `srcset` 属性和 `sizes` 属性分别解决了像素密度和屏幕大小的适配，但如果要同时适配不同像素密度、不同大小的屏幕，就要用到 `<picture>` 标签。
- `<picture>` 是一个容器标签，内部使用 `<source>` 和 `<img>` ，指定不同情况下加载的图像。

    ```html
    <picture>
        <source media="(max-width: 500px)" srcset="cat-vertical.jpg">
        <source media="(min-width: 501px)" srcset="cat-horizontal.jpg">
        <img src="cat.jpg" alt="cat">
    </picture>

    <picture>
        <source
            media="(min-width: 990px)"
            srcset="homepage-person@desktop.png, homepage-person@desktop-2x.png 2x"
        >
        <source
            media="(min-width: 750px)"
            srcset="homepage-person@tablet.png, homepage-person@tablet-2x.png 2x"
        >
        <img
            srcset="homepage-person@mobile.png,homepage-person@mobile-2x.png 2x"
            alt="Shopify Merchant, Corrine Anestopoulos"
        >
    </picture>
    ```

- 除了响应式图像，`<picture>` 标签还可以用来选择不同格式的图像。

    ```html
    <picture>
        <source type="image/svg+xml" srcset="logo.xml">
        <source type="image/webp" srcset="logo.webp">
        <img src="logo.png" alt="ACME Corp">
    </picture>
    ```

- `<source>` 标签的 `type` 属性给出图像的 [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types) 类型。

## `<a>`

`<a>` 标签代表一个可以跳转的链接,内部不仅可以放置文字，也可以放置其他元素，比如段落、图像、多媒体等等。

### `<a>` 标签的属性

- `href` 属性给出链接指向的网址（可以带锚点）。
- `hreflang` 属性给出链接指向的网址所使用的语言，纯粹是提示性的，主要供搜索引擎使用。
    - 如果某个资源有多种语言的不同版本，可以将 `hreflang` 设为 `x-default`，表示哪一个链接是默认版本。

        ```html
        <a href="https://example.com" hreflang="x-default">English</a>
        <a href="https://example.com/de" hreflang="de">German</a>
        ```

- `title` 属性给出链接的说明信息，鼠标悬停在链接上方时，浏览器会将这个属性的值，以提示块的形式显示出来。
- `target` 属性指定如何展示打开的链接。
    - `_self`：当前窗口打开，这是默认值。
    - `_blank`：新窗口打开。
    - `_parent`：在父级框架中打开链接。
    - `_top`：在最顶层窗口中打开链接，清除所有框架。
- `rel` 属性说明链接与当前页面的关系。
    - `noreferrer`：告诉浏览器打开链接时，不要将当前网址作为 HTTP 头信息的 Referer 字段发送出去，这样可以隐藏点击的来源。
    - `noopener`：告诉浏览器打开链接时，不让链接窗口通过 JavaScript 的 `window.opener` 属性引用原始窗口，这样就提高了安全性。
    - `alternate`：当前文档的另一种形式，比如翻译。
    - `author`：作者链接。
    - `bookmark`：用作书签的永久地址。
    - `external`：当前文档的外部参考文档。
    - `help`：帮助链接。
    - `license`：许可证链接。
    - `next`：系列文档的下一篇。
    - `nofollow`：告诉搜索引擎忽略该链接，主要用于用户提交的内容，防止有人企图通过添加链接，提高该链接的搜索排名。
    - `prev`：系列文档的上一篇。
    - `search`：文档的搜索链接。
    - `tag`：文档的标签链接。
- `referrerpolicy` 属性用于精确设定点击链接时，浏览器发送 HTTP 头信息的 Referer 字段的行为。
    - `no-referrer`：不发送 Referer 字段。
    - `no-referrer-when-downgrade`
    - `origin`：只发送源信息（协议+域名+端口）。
    - `origin-when-cross-origin`
    - `unsafe-url`
    - `same-origin`：示同源时才发送 Referer 字段。
    - `strict-origin`
    - `strict-origin-when-cross-origin`
- `ping` 属性指定一个网址，用户点击的时候，会向该网址发出一个 POST 请求，通常用于跟踪用户的行为。
    - `ping` 属性只对链接有效，对其他的交互行为无效。
    - 这个请求的 HTTP 标头，包含了 `ping-from` 属性（点击行为发生的页面）和 `ping-to` 属性（`href` 属性所指向的页面）。

        ```html
        <a href="http://localhost:3000/other" ping="http://localhost:3000/log">Go to Other Page</a>
        ```

        ```http
        headers: {
            'ping-from': 'http://localhost:3000/',
            'ping-to': 'http://localhost:3000/other'
            'content-type': 'text/ping'
            // ...other headers
        },
        ```

- `type` 属性给出链接 URL 的 MIME 类型，比如到底是网页，还是图像或文件，也是纯粹提示性的属性，没有实际功能。

    ```html
    <a href="smile.jpg" type="image/jpeg">示例图片</a>
    ```

- `download` 属性表明当前链接用于下载，而不是跳转到另一个 URL。
    - `download` 属性只在链接与网址同源时，才会生效。即链接应该与网址属于同一个网站。
    - 如果 `download` 属性设置了值，那么这个值就是下载的文件名。
    - 如果链接点击后，服务器的 HTTP 回应的头信息设置了 `Content-Disposition` 字段，并且该字段的值与 `download` 属性不一致，那么该字段优先，下载时将显示其设置的文件名。

### 邮件链接

- 链接也可以指向一个邮件地址，使用 `mailto` 协议。用户点击后，浏览器会打开本机默认的邮件程序，让用户向指定的地址发送邮件。
- 除了邮箱，邮件协议还允许指定其他几个邮件要素。
    - `subject`：主题
    - `cc`：抄送
    - `bcc`：密送
    - `body`：邮件内容

        ```html
        <a href="mailto:foo@bar.com?cc=test@test.com&subject=The%20subject&body=The%20body">发送邮件</a>
        ```

### 电话链接

如果是手机浏览的页面，还可以使用 `tel` 协议，创建电话链接。用户点击该链接，会唤起电话，可以进行拨号。

```js
<a href="tel:13312345678">13312345678</a>
```

## `<link>`

`<link>` 标签主要用于将当前网页与相关的外部资源联系起来，通常放在 `<head>` 元素里面。最常见的用途就是加载 CSS 样式表。

```html
<link rel="stylesheet" type="text/css" href="theme.css">

<link href="default.css" rel="stylesheet" title="Default Style">
<link href="fancy.css" rel="alternate stylesheet" title="Fancy">
<link href="basic.css" rel="alternate stylesheet" title="Basic">
```

`<link>` 还可以加载网站的 favicon 图标文件。

```html
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="favicon114.png">
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="favicon72.png">
```

`<link>` 也用于提供文档的相关链接，比如下面是给出文档的 RSS Feed 地址。

```html
<link rel="alternate" type="application/atom+xml" href="/blog/news/atom">
```

### `<link>` 的属性

- `href` 属性表示 `<link>` 标签所链接的资源。
- `rel` 属性表示外部资源与当前文档之间的关系，是 `<link>` 标签的必需属性，可以视为对 `href` 属性所链接资源的说明。
    - `alternate`：文档的另一种表现形式的链接，比如打印版。
    - `author`：文档作者的链接。
    - `dns-prefetch`：要求浏览器提前执行指定网址的 DNS 查询。
    - `help`：帮助文档的链接。
    - `icon`：加载文档的图标文件。
    - `license`：许可证链接。
    - `next`：系列文档下一篇的链接。
    - `pingback`：接收当前文档 pingback 请求的网址。
    - `preconnect`：要求浏览器提前与给定服务器建立 HTTP 连接。
    - `prefetch`：要求浏览器提前下载并缓存指定资源，供下一个页面使用。它的优先级较低，浏览器可以不下载。
    - `preload`：要求浏览器提前下载并缓存指定资源，当前页面稍后就会用到。它的优先级较高，浏览器必须立即下载。
    - `prerender`：要求浏览器提前渲染指定链接。这样的话，用户稍后打开该链接，就会立刻显示，感觉非常快。
    - `prev`：表示当前文档是系列文档的一篇，这里给出上一篇文档的链接。
    - `search`：提供当前网页的搜索链接。
    - `stylesheet`：加载一张样式表。
- `hreflang` 属性用来表示 `href` 属性链接资源的所用语言，通常指当前页面的其他语言版本。
    - 如果一个页面有多个语言的版本，`hreflang` 属性可以设为 `x-default`，表示哪一个页面是默认版本。

        ```html
        <link href="https://example.com" rel="alternate" hreflang="x-default" />
        <link href="https://example.com/de" rel="alternate" hreflang="de" />
        ```

### 资源的预加载

某些情况下，你需要浏览器预加载某些资源，也就是先把资源缓存下来，等到使用的时候，就不用再从网上下载了，立即就能使用。预处理指令可以做到这一点。

- `<link rel="preload">`
    - `<link rel="preload">` 告诉浏览器尽快下载并缓存资源。
        - 且允许指定预加载资源的类型，
        - 且允许 `onload` 事件的回调函数。

            ```html
            <link rel="preload" href="style.css" as="style">
            <link rel="preload" href="main.js" as="script">
            ```

    - `as` 属性指定加载资源的类型（如果不指定 `as` 属性，或者它的值是浏览器不认识的，那么浏览器会以较低的优先级下载这个资源）。
        - `script`
        - `style`
        - `image`
        - `media`
        - `document`
    - `type` 属性用于进一步明确 MIME 类型。
        - `<link rel="preload" href="sintel-short.mp4" as="video" type="video/mp4">`
    - 下方的写法资源预下载后立刻执行，这是因为 `onload` 指定的回调函数会在脚本下载完成后执行，立即插入页面。
        - `<link rel="preload" as="style" href="async_style.css" onload="this.rel='stylesheet'">`
- `<link rel="prefetch">`
    - 如果后续的页面需要某个资源，并且希望预加载该资源，以便加速页面渲染。该指令不是强制性的，优先级较低，浏览器不一定会执行。
    - 这意味着，浏览器可以不下载该资源，比如连接速度很慢时。
    - `<link rel="prefetch" href="https://www.example.com/">`
- `<link rel="preconnect">`
    - `<link rel="preconnect">` 要求浏览器提前与某个域名建立 TCP 连接。当你知道很快就会请求该域名时，这会很有帮助。
    - `<link rel="preconnect" href="https://www.example.com/">`
- `<link rel="dns-prefetch">`
    - `<link rel="dns-prefetch">` 要求浏览器提前执行某个域名的 DNS 解析。
    - `<link rel="dns-prefetch" href="//example.com/">`
- `<link rel="prerender">`
    - `<link rel="prerender">` 要求浏览器加载某个网页，并且提前渲染它。
    - `<link rel="prerender" href="http://example.com/">`

### `media` 属性

`media` 属性给出外部资源生效的媒介条件。

```html
<link rel="preload" as="image" href="map.png" media="(max-width: 600px)">
<link rel="preload" as="script" href="map.js" media="(min-width: 601px)">
```

上面代码中，如果屏幕宽度在 600 像素以下，则只加载第一个资源，否则就加载第二个资源。

## `<script>`，`<noscript>`

`<script>` 用于加载脚本代码，目前主要是加载 JavaScript 代码。

```html
<script type="text/javascript" src="javascript.js"></script>
```

- `type` 属性
    - `type` 属性给出脚本的类型，默认是 JavaScript 代码，所以可省略。
    - `type` 属性也可以设成 `module`，表示这是一个 ES6 模块，不是传统脚本。
    - 对于那些不支持 ES6 模块的浏览器，可以设置 `nomodule` 属性。支持 ES6 模块的浏览器，会不加载指定的脚本。这个属性通常与`type="module"` 配合使用，作为老式浏览器的回退方案。

        ```html
        <script type="module" src="main.js"></script>
        <script nomodule src="fallback.js"></script>
        ```

- `async`：该属性指定 JavaScript 代码为异步执行，不是造成阻塞效果，JavaScript 代码默认是同步执行。
- `defer`：该属性指定 JavaScript 代码不是立即执行，而是页面解析完成后执行。
- `crossorigin`：如果采用这个属性，就会采用跨域的方式加载外部脚本，即 HTTP 请求的头信息会加上 `origin` 字段。
- `integrity`：给出外部脚本的哈希值，防止脚本被篡改。只有哈希值相符的外部脚本，才会执行。
- `nonce`：一个密码随机数，由服务器在 HTTP 头信息里面给出，每次加载脚本都不一样。它相当于给出了内嵌脚本的白名单，只有在白名单内的脚本才能执行。
- `referrerpolicy`：HTTP 请求的 Referer 字段的处理方法。

`<noscript>` 标签用于浏览器不支持或关闭 JavaScript 时，所要显示的内容。用户关闭 JavaScript 可能是为了节省带宽，以延长手机电池寿命，或者为了防止追踪，保护隐私。

```html
<noscript>
  您的浏览器不能执行 JavaScript 语言，页面无法正常显示。
</noscript>
```

## 多媒体标签

### `<video>`

`<video>` 标签是一个块级元素，用于放置视频。如果浏览器支持加载的视频格式，就会显示一个播放器，否则显示 `<video>` 内部的子元素。

```html
<video src="example.mp4" controls>
  <p>你的浏览器不支持 HTML5 视频，请下载<a href="example.mp4">视频文件</a>。</p>
</video>
```

`<video>` 有以下属性。

- `src`：视频文件的网址。
- `controls`：播放器是否显示控制栏。该属性是布尔属性，不用赋值，只要写上属性名，就表示打开。如果不想使用浏览器默认的播放器，而想使用自定义播放器，就不要使用该属性。
- `width`：视频播放器的宽度，单位像素。
- `height`：视频播放器的高度，单位像素。
- `autoplay`：视频是否自动播放，该属性为布尔属性。
- `loop`：视频是否循环播放，该属性为布尔属性。
- `muted`：是否默认静音，该属性为布尔属性。
- `poster`：视频播放器的封面图片的 URL。
- `preload`：视频播放之前，是否缓冲视频文件。这个属性仅适合没有设置 `autoplay` 的情况。它有三个值，分别是 `none`（不缓冲）、`metadata`（仅仅缓冲视频文件的元数据）、`auto`（可以缓冲整个文件）。
- `playsinline`：iPhone 的 Safari 浏览器播放视频时，会自动全屏，该属性可以禁止这种行为。该属性为布尔属性。
- `crossorigin`：是否采用跨域的方式加载视频。它可以取两个值，分别是 `anonymous`（跨域请求时，不发送用户凭证，主要是 Cookie `use-credentials`（跨域时发送用户凭证）。
- `currentTime`：指定当前播放位置（双精度浮点数，单位为秒）。如果尚未开始播放，则会从这个属性指定的位置开始播放。
- `duration`：该属性只读，指示时间轴上的持续播放时间（总长度），值为双精度浮点数（单位为秒）。如果是流媒体，没有已知的结束时间，属性值为 `+Infinity`。

    ```html
    <video width="400" height="400" autoplay loop muted poster="poster.png"></video>
    ```

HTML 标准没有规定浏览器需要支持哪些视频格式，完全由浏览器厂商自己决定。为了避免浏览器不支持视频格式，可以使用 `<source>` 标签，放置同一个视频的多种格式。

```html
<video controls>
  <source src="example.mp4" type="video/mp4">
  <source src="example.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频，请下载<a href="example.mp4">视频文件</a>。</p>
</video>
```

### `<audio>`

`<audio>` 标签是一个块级元素，用于放置音频。

```html
<audio controls>
  <source src="foo.mp3" type="audio/mp3">
  <source src="foo.ogg" type="audio/ogg">
  <p>你的浏览器不支持 HTML5 音频，请直接下载<a href="foo.mp3">音频文件</a>。</p>
</audio>
```

其他属性与 `<video>` 标签类似。

### `<track>`

`<track>` 标签用于指定视频的字幕，格式是 WebVTT（.vtt文件），放置在 `<video>` 标签内部。它是一个单独使用的标签，没有结束标签。

```html
<video controls src="sample.mp4">
   <track label="英文" kind="subtitles" src="subtitles_en.vtt" srclang="en">
   <track label="中文" kind="subtitles" src="subtitles_cn.vtt" srclang="cn" default>
</video>
```

`<track>` 标签有以下属性：

- `label`：播放器显示的字幕名称，供用户选择。
- `kind`：字幕的类型，默认是 `subtitles`，表示将原始声音成翻译外国文字，比如英文视频提供中文字幕。另一个常见的值是 `captions`，表示原始声音的文字描述，通常是视频原始使用的语言，比如英文视频提供英文字幕。
- `src`：vtt 字幕文件的网址。
- `srclang`：字幕的语言，必须是有效的语言代码。
- `default`：是否默认打开，布尔属性。

### `<source>`

`<source>` 标签用于 `<picture>`、`<video>`、`<audio>` 的内部，用于指定一项外部资源。单标签是单独使用的，没有结束标签。

有如下属性：

- `type`：指定外部资源的 MIME 类型。
- `src`：指定源文件，用于 `<video>` 和 `<audio>` 。
- `srcset`：指定不同条件下加载的图像文件，用于 `<picture>`。
- `media`：指定媒体查询表达式，用于 `<picture>`。
- `sizes`：指定不同设备的显示大小，用于 `<picture>`，必须跟 `srcset` 搭配使用。

### `<embed>`

`<embed>` 标签用于嵌入外部内容，这个外部内容通常由浏览器插件负责控制。由于浏览器的默认插件都不一致，很可能不是所有浏览器的用户都能访问这部分内容，建议谨慎使用。

```html
<embed
    type="video/webm"
    src="/media/examples/flower.mp4"
    width="250"
    height="200"
>
```

`<embed>` 标签具有如下的通用属性：

- `height`：显示高度，单位为像素，不允许百分比。
- `width`：显示宽度，单位为像素，不允许百分比。
- `src`：嵌入的资源的 URL。
- `type`：嵌入资源的 MIME 类型。

QuickTime 插件播放 MOV 视频文件。

```html
<embed type="video/quicktime" src="movie.mov" width="640" height="480">
```

启动 Flash 插件。

```html
<embed
    src="whoosh.swf"
    quality="medium"
    bgcolor="#ffffff"
    width="550"
    height="400"
    name="whoosh"
    align="middle"
    allowScriptAccess="sameDomain"
    allowFullScreen="false"
    type="application/x-shockwave-flash"
    pluginspage="http://www.macromedia.com/go/getflashplayer"
>
```

## `<object>`，`<param>`

`<object>` 标签作用跟 `<embed>` 相似，也是插入外部资源，由浏览器插件处理。它可以视为 `<embed>` 的替代品，有标准化行为，只限于插入少数几种通用资源，没有历史遗留问题，因此更推荐使用。

插入 PDF 文件：

```html
<object
    type="application/pdf"
    data="/media/examples/In-CC0.pdf"
    width="250"
    height="200">
</object>
```

`<object>` 具有如下的通用属性。

- `data`：嵌入的资源的 URL。
- `form`：当前网页中相关联表单的 `id` 属性（如果有的话）。
- `height`：资源的显示高度，单位为像素，不能使用百分比。
- `width`：资源的显示宽度，单位为像素，不能使用百分比。
- `type`：资源的 MIME 类型。
- `typemustmatch`：布尔属性，表示 `data` 属性与 `type` 属性是否必须匹配。

`<object>` 标签是一个容器元素，内部可以使用 `<param>` 标签，给出插件所需要的运行参数。

```html
<object data="movie.swf" type="application/x-shockwave-flash">
  <param name="foo" value="bar">
</object>
```

## `<iframe>` 标签

`<iframe>` 标签用于在网页里面嵌入其他网页。

```html
<iframe
    src="https://www.baidu.com"
    width="100%" height="500"
    frameborder="0"
    allowfullscreen sandbox
>
  <p><a href="https://www.baidu.com">点击打开嵌入页面</a></p>
</iframe>
```

`<iframe>` 的属性如下：

- `allowfullscreen`：允许嵌入的网页全屏显示，需要全屏 API 的支持，请参考相关的 JavaScript 教程。
- `frameborder`：是否绘制边框，0 为不绘制，1 为绘制（默认值）。建议尽量少用这个属性，而是在 CSS 里面设置样式。
- `src`：嵌入的网页的 URL。
- `width`：显示区域的宽度。
- `height`：显示区域的高度。
- `sandbox`：设置嵌入的网页的权限，详见下文。
- `importance`：浏览器下载嵌入的网页的优先级，可以设置三个值。`high` 表示高优先级，`low` 表示低优先级，`auto` 表示由浏览器自行决定。
- `name`：内嵌窗口的名称，可以用于 `<a>`、`<form>`、`<base>`的 `target` 属性。
- `referrerpolicy`：请求嵌入网页时，HTTP 请求的 Referer 字段的设置。

### `sandbox` 属性

如果嵌入的网页是其他网站的页面，你不了解对方会执行什么操作，因此就存在安全风险。为了限制 `<iframe>` 的风险，HTML 提供了 `sandbox` 属性，允许设置嵌入的网页的权限，等同于提供了一个隔离层，即“沙箱”。

`sandbox` 可以当作布尔属性使用，只要写上这个属性表示打开所有限制，可以设置具体的值，如下：

- `allow-forms`：允许提交表单。
- `allow-modals`：允许提示框，即允许执行 `window.alert()` 等会产生弹出提示框的 JavaScript 方法。
- `allow-popups`：允许嵌入的网页使用 `window.open()` 方法弹出窗口。
- `allow-popups-to-escape-sandbox`：允许弹出窗口不受沙箱的限制。
- `allow-orientation-lock`：允许嵌入的网页用脚本锁定屏幕的方向，即横屏或竖屏。
- `allow-pointer-lock`：允许嵌入的网页使用 Pointer Lock API，锁定鼠标的移动。
- `allow-presentation`：允许嵌入的网页使用 Presentation API。
- `allow-same-origin`：不打开该项限制，将使得所有加载的网页都视为跨域。
- `allow-scripts`：允许嵌入的网页运行脚本（但不创建弹出窗口）。
- `allow-storage-access-by-user-activation`：`sandbox` 属性同时设置了这个值和 `allow-same-origin` 的情况下，允许 `<iframe>` 嵌入的第三方网页通过用户发起 `document.requestStorageAccess()` 请求，经由 Storage Access API 访问父窗口的 Cookie。
- `allow-top-navigation`：允许嵌入的网页对顶级窗口进行导航。
- `allow-top-navigation-by-user-activation`：允许嵌入的网页对顶级窗口进行导航，但必须由用户激活。
- `allow-downloads-without-user-activation`：允许在没有用户激活的情况下，嵌入的网页启动下载。

注意，不要同时设置 `allow-scripts` 和 `allow-same-origin` 属性，这将使得嵌入的网页可以改变或删除 `sandbox` 属性。

### `loading` 属性

`<iframe>` 指定的网页会立即加载，有时这不是希望的行为。`<iframe>` 滚动进入视口以后再加载，这样会比较节省带宽。

`loading` 属性可以触发 `<iframe>` 网页的懒加载。该属性可以取以下三个值：

- `auto`：浏览器的默认行为，与不使用 `loading` 属性效果相同。
- `lazy`：`<iframe>` 的懒加载，即将滚动进入视口时开始加载。
- `eager`：立即加载资源，无论在页面上的位置如何。

有一点需要注意，如果 `<iframe>` 是隐藏的，则 `loading` 属性无效，将会立即加载。只要满足以下任一个条件，Chrome 浏览器就会认为`<iframe>` 是隐藏的。

- `<iframe>` 的宽度和高度为4像素或更小。
- 样式设为 `display: none` 或 `visibility: hidden`。
- 使用定位坐标为负X或负Y，将 `<iframe>` 放置在屏幕外。

### `<fencedframe>` 标签

`<fencedframe>` 是 一种正在标准化中的 HTML 新标签，主要用于在网页中安全地嵌入第三方内容，目标是成为 `<iframe>` 的更安全替代方案（尤其用于广告、跨站内容等场景）。

`<fencedframe>` 用来嵌入一个被强隔离的子页面，子页面与父页面之间的信息通道被严格限制，设计目标是：

- 防止用户被跨站追踪。
- 防止嵌入内容泄露或获取父页面信息。
- 支持隐私保护相关的 Web API（如 Privacy Sandbox）。

`<fencedframe>` 有以下属性：

- `src`：指定被嵌入页面的地址，是一个必需属性。父页面无法读取或修改这个 URL，子页面也无法知道自己的嵌入来源。
- `width` / `height`：设置 fenced frame 的尺寸。但子页面无法通过 JavaScript 获取自己的尺寸，防止利用尺寸进行指纹识别。
- `loading`：控制是否延迟加载。可选值有 `lazy` 和 `eager` 两个。`eager` 是默认值。

## 表格标签

- `<table>` 是一个块级容器标签，所有表格内容都要放在这个标签里面。
- `<caption>` 总是 `<table>` 里面的第一个子元素，表示表格的标题。该元素是可选的。
- `<thead>`、`<tbody>`、`<tfoot>` 都是块级容器元素，且都是 `<table>` 的一级子元素，分别表示表头、表体和表尾。
- `<colgroup>` 是 `<table>` 的一级子元素，用来包含一组列的定义。`<col>` 是 `<colgroup>` 的子元素，用来定义表格的一列。
    - 注意 `<col>` 只能设置 背景、宽度、visibility 等和整列容器相关的属性。不能直接影响单元格里的文本样式（字体、颜色、对齐等）。
    - 给一列的文本统一设置样式：
        - 给 `<td>` / `<th>` 加上统一的 class。缺点是需要在每个 `<td>` / `<th>` 上都加上相同的 class。
        - 利用 CSS 的 `nth-child()` 选择器。缺点是如果表格列数会变，选择器要小心维护。
    - `<col>` 有一个 `span` 属性，表示当前 `<col>` 定义应用到多少列。`span="N"` 表示控制接下来的 N 列。
- `<tr>` 标签表示表格的一行（table row）。
- `<th>` 和 `<td>` 都用来定义表格的单元格。其中，`<th>` 是标题单元格，`<td>` 是数据单元格。
    - 单元格会有跨越多行或多列的情况，这要通过 `colspan` 属性和 `rowspan` 属性设置，前者表示单元格跨越的栏数，后者表示单元格跨越的行数。它们的值都是一个非负整数，默认为1。
    - `headers` 是一个 [A11y](https://developer.mozilla.org/en-US/docs/Web/Accessibility) 属性，用来明确某个单元格关联到哪些表头。主要用于屏幕阅读器用户。
    - `scope` 属性是 `<th>`（Table Header）标签的专用属性，也是一个 A11y 属性。
        - `row`：该行的所有单元格，都与该标题单元格相关。
        - `col`：该列的所有单元格，都与该标题单元格相关。
        - `rowgroup`：多行组成的一个行组的所有单元格，都与该标题单元格相关，可以与 `rowspan` 属性配合使用。
        - `colgroup`：多列组成的一个列组的所有单元格，都与该标题单元格相关，可以与 `colspan` 属性配合使用。
        - `auto`：默认值，表示由浏览器自行决定。

    ```html
    <table border="1">
    <colgroup>
        <col style="background: lightblue;">
        <col span="2" style="background: lightgreen;">
    </colgroup>
    <tr>
        <th>姓名</th>
        <th>年龄</th>
        <th>城市</th>
    </tr>
    <tr>
        <td>小明</td>
        <td>18</td>
        <td>北京</td>
    </tr>
    </table>

    <table>
        <thead>
            <tr>
            <th scope="col">海报名称</th>
            <th scope="col">颜色</th>
            <th colspan="3" scope="colgroup">尺寸</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <th rowspan="3" scope="rowgroup">Zodiac</th>
            <th scope="row">Full color</th>
            <td>A2</td>
            <td>A3</td>
            <td>A4</td>
            </tr>
            <tr>
            <th scope="row">Black and white</th>
            <td>A1</td>
            <td>A2</td>
            <td>A3</td>
            </tr>
            <tr>
            <th scope="row">Sepia</th>
            <td>A3</td>
            <td>A4</td>
            <td>A5</td>
            </tr>
        </tbody>
    </table>
    ```

## 表单标签

`<form>` 标签用来定义一个表单，所有表单内容放到这个容器元素之中。

```html
<form action="https://example.com/api" method="post">
  <label for="POST-name">用户名：</label>
  <input id="POST-name" type="text" name="user">
  <input type="submit" value="提交">
</form>
```

- `<label>` 标签的 `for` 属性把这个标签和 `id = 'POST-name'` 的输入框绑定起来，当你点击“用户名：”这个文字时，浏览器会自动把焦点切换到对应的 `<input>` 框里。
- 文本输入框的 `name` 属性是 user，表示将向服务器发送一个键名为 user 的键值对，键值就是这个控件的 value 属性，等于用户输入的值。
- 用户在文本输入框里面输入用户名，比如 foobar，然后点击提交按钮，浏览器就会向服务器 <https://example.com/api> 发送一个 POST 请求，发送 user=foobar 这样一段数据。

`<form>` 有以下属性。

- `accept-charset`：服务器接受的字符编码列表，使用空格分隔，默认与网页编码相同。
- `action`：服务器接收数据的 URL。
- `autocomplete`：如果用户没有填写某个控件，浏览器是否可以自动填写该值。它的可能取值分别为 `off` 和 `on`。
- `method`：提交数据的 HTTP 方法，可能的值有 `post`（表单数据作为 HTTP 数据体发送），`get`（表单数据作为 URL 的查询字符串发送），`dialog`（表单位于 `<dialog>` 内部使用）。
- `enctype`：当 `method` 属性等于 `post`时，该属性指定提交给服务器的 MIME 类型。可能的值为 `application/x-www-form-urlencoded`（默认值），`multipart/form-data`（文件上传的情况），`text/plain`。
- `name`：表单的名称，应该在网页中是唯一的。注意，如果一个控件没有设置 `name` 属性，那么这个控件的值就不会作为键值对，向服务器发送。
- `novalidate`：布尔属性，表单提交时是否取消验证。
- `target`：在哪个窗口展示服务器返回的数据，可能的值有 `_self`（当前窗口），`_blank`（新建窗口），`_parent`（父窗口），`_top`（顶层窗口），`<iframe>` 标签的 `name` 属性（即表单返回结果展示在 `<iframe>` 窗口）。

### enctype 属性

`<form>` 表单的 `enctype` 属性，指定了采用 POST 方法提交数据时，浏览器给出的数据的 MIME 类型。该属性可以取以下值。

- `application/x-www-form-urlencoded`：是默认类型，把表单键值对编码为 `key1=value1&key2=value2` 形式；空格会变成 +，非 ASCII / 特殊字符会被百分号编码（%xx）
- `multipart/form-data`：主要用于文件上传。当表单包含 `<input type="file">` 必须使用这个值，如若没有则文件不会被上传到 `request.FILES`，服务器拿不到文件内容。

### `<fieldset>`，`<legend>`

`<fieldset>` 标签是一个块级容器标签，表示控件的集合，用于将一组相关控件组合成一组。

```html
<form>
  <fieldset>
    <p>年龄：<input type="text" name="age"></p>
    <p>性别：<input type="text" name="gender"></p>
  </fieldset>
</form>
```

`<fieldset>` 有以下属性。

- `disabled`：布尔属性，一旦设置会使得 `<fieldset>` 内部包含的控件都不可用，都变成灰色状态。
- `form`：指定控件组所属的 `<form>` ，它的值等于 `<form>` 的 id 属性。
- `name`：该控件组的名称。

`<legend>` 标签用来设置 `<fieldset>` 控件组的标题，通常是 <`fieldset>` 内部的第一个元素，会嵌入显示在控件组的上边框里面。

```html
<fieldset>
  <legend>学生情况登记</legend>
  <p>年龄：<input type="text" name="age"></p>
  <p>性别：<input type="text" name="gender"></p>
</fieldset>
```

### `<label>`

`<label>` 标签是一个行内元素，提供控件的文字说明，帮助用户理解控件的目的。

```html
<label for="user">用户名：</label>
<input type="text" name="user" id="user">
```

控件也可以放在 `<label>` 之中，这时不需要 `for` 属性和 `id` 属性。

```html
<label>用户名：
  <input type="text" name="user">
</label>
```

`<label>` 的属性如下：

- `for`：关联控件的 `id` 属性。
- `form`：关联表单的 `id` 属性。设置了该属性后，`<label>` 可以放置在页面的任何位置，否则只能放在 `<form>` 内部。

一个控件可以有多个关联的 `<label>` 标签。

```html
<label for="username">用户名：</label>
<input type="text" id="username" name="username">
<label for="username"><abbr title="required">*</abbr></label>
```

### `<input>`

`<input>` 标签是一个行内元素，用来接收用户的输入。它是一个单独使用的标签，没有结束标签。它有多种类型，取决于 `type` 属性的值，默认值是 `text`，表示一个输入框。

`<input>` 的共有属性。

- `autofocus`：布尔属性，是否在页面加载时自动获得焦点。
- `disabled`：布尔属性，是否禁用该控件。一旦设置，该控件将变灰，用户可以看到，但是无法操作。
- `form`：关联表单的 `id` 属性。设置了该属性后，控件可以放置在页面的任何位置，否则只能放在 `<form>` 内部。
- `list`：关联的 `<datalist>` 的 `id` 属性，设置该控件相关的数据列表，详见后文。
- `name`：控件的名称，主要用于向服务器提交数据时，控件键值对的键名。注意：只有设置了 `name` 属性的控件，才会向服务器提交，不设置就不会提交。
- `readonly`：布尔属性，是否为只读。
- `required`：布尔属性，是否为必填。
- `type`：控件类型，详见下文。
- `value`：控件的值。

#### `type` 属性

`type` 属性决定了 `<input>` 的形式。

##### `type="text"`

`type="text"` 是一个普通的文本输入框，用来输入单行文本。如果用户输入换行符，换行符会自动从输入中删除。

```html
<input type="text" id="name" name="name" minlength="4" maxlength="8" size="10" required>
```

`text` 输入框有以下配套属性。

- `maxlength`：可以输入的最大字符数，值为一个非负整数。
- `minlength`：可以输入的最小字符数，值为一个非负整数，且必须小于 `maxlength`。
- `pattern`：用户输入必须匹配的正则表达式。
- `placeholder`：输入字段为空时，用于提示的示例值。只要用户没有任何字符，该提示就会出现，否则会消失。
- `readonly`：布尔属性，表示该输入框是只读的，用户只能看，不能输入。
- `size`：表示输入框的显示长度有多少个字符宽，它的值是一个正整数，默认等于 20。超过这个数字的字符，必须移动光标才能看到。
- `spellcheck`：是否对用户输入启用拼写检查，可能的值为 true 或 false 。

##### `type="search"`

`type="search"` 是一个用于搜索的文本输入框，基本等同于 `type="text"`。某些浏览器会在输入的时候，在输入框的尾部显示一个删除按钮，点击就会删除所有输入，让用户从头开始输入。

```html
<form>
  <input type="search" id="mySearch" name="q" placeholder="输入搜索词……" required>
  <input type="submit" value="搜索">
</form>
```

##### `type="button"`

`type="button"` 是没有默认行为的按钮，通常脚本指定 `click` 事件的监听函数来使用。

```html
<input type="button" value="点击">
```

尽量不要使用这个类型，而使用 `<button>` 标签代替，一则语义更清晰，二则 `<button>` 标签内部可以插入图片或其他 HTML 代码。

##### `type="submit"`

`type="submit"` 是表单的提交按钮。用户点击这个按钮，就会把表单提交给服务器。

```html
<input type="submit" value="提交">
```

如果不指定 `value` 属性，浏览器会在提交按钮上显示默认的文字，通常是 Submit。

该类型有以下配套属性，用来覆盖 `<form>` 标签的相应设置。：

- `formaction`：提交表单数据的服务器 URL。
- `formenctype`：表单数据的编码类型。
- `formmethod`：提交表单使用的 HTTP 方法（get 或 post）。
- `formnovalidate`：一个布尔值，表示数据提交给服务器之前，是否要忽略表单验证。
- `formtarget`：收到服务器返回的数据后，在哪一个窗口显示。

##### `type="image"`

`type="image"` 表示将一个图像文件作为提交按钮，行为和用法与 `type="submit"` 完全一致。

```html
<input type="image" alt="登陆" src="login-button.png">
```

该类型有以下配套属性：

- `alt`：图像无法加载时显示的替代字符串。
- `src`：加载的图像 URL。
- `height`：图像的显示高度，单位为像素。
- `width`：图像的显示宽度，单位为像素。
- `formaction`：提交表单数据的服务器 URL。
- `formenctype`：表单数据的编码类型。
- `formmethod`：提交表单使用的 HTTP 方法（get 或 post）。
- `formnovalidate`：一个布尔值，表示数据提交给服务器之前，是否要忽略表单验证。
- `formtarget`：收到服务器返回的数据后，在哪一个窗口显示。

用户点击图像按钮提交时，会额外提交两个参数 `x` 和 `y` 到服务器，表示鼠标的点击位置，比如 x=52&y=55。x 是横坐标，y 是纵坐标，都以图像左上角作为原点(0, 0)。如果图像按钮设置了 `name` 属性，比如 `name="position"`，那么将以该值作为坐标的前缀，比如 position.x=52&position.y=55。这个功能通常用来地图类型的操作，让服务器知道用户点击了地图的哪个部分。

##### `type="reset"`

`type="reset"` 是一个重置按钮，用户点击以后，所有表格控件重置为初始值。

如果不设置 `value` 属性，浏览器会在按钮上面加上默认文字，通常是 Reset。这个控件用处不大，用户点错了还会使得所有已经输入的值都被重置，建议不要使用。

##### `type="checkbox"`

`type="checkbox"` 是复选框，允许选择或取消选择该选项。

```html
<input type="checkbox" id="agreement" name="agreement" checked>
<label for="agreement">是否同意</label>
```

上面代码会在文字前面，显示一个可以点击的选择框，点击可以选中，再次点击可以取消。上面代码中，`checked` 属性表示默认选中。`value` 属性的默认值是 `on`。也就是说，如果没有设置 `value` 属性，以上例来说，选中复选框时，会提交 `agreement=on`。如果没有选中，提交时不会有该项。

多个相关的复选框，可以放在 `<fieldset>` 里面。

```html
<fieldset>
  <legend>你的兴趣</legend>
  <div>
    <input type="checkbox" id="coding" name="interest" value="coding">
    <label for="coding">编码</label>
  </div>
  <div>
    <input type="checkbox" id="music" name="interest" value="music">
    <label for="music">音乐</label>
  </div>
</fieldset>
```

上面代码中，如果用户同时选中两个复选框，提交的时候就会有两个 `name` 属性，比如 interest=coding&interest=music。

##### `type="radio"`

`type="radio"` 是单选框，表示一组选择之中，只能选中一项。单选框通常为一个小圆圈，选中时会被填充或突出显示。

```html
<fieldset>
  <legend>性别</legend>
  <div>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">男</label>
  </div>
  <div>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">女</label>
  </div>
</fieldset>
```

单选按钮之所以只能选一个，是因为它们共享相同的 `name` 属性值。

该类型的配套属性如下：

- `checked`：布尔属性，表示是否默认选中当前项。
- `value`：用户选中该项时，提交到服务器的值，默认为 `on`。

##### `type="email"`

`type="email"` 是一个只能输入电子邮箱的文本输入框。表单提交之前，浏览器会自动验证是否符合电子邮箱的格式，如果不符合就会显示提示，无法提交到服务器。

```html
<input type="email" pattern=".+@foobar.com" size="30" required>
```

该类型有一个 `multiple` 的布尔属性，一旦设置，就表示该输入框可以输入多个逗号分隔的电子邮箱。

```html
<input id="emailAddress" type="email" multiple required>
```

注意，如果同时设置了 `multiple` 属性和 `required` 属性，零个电子邮箱是允许的，也就是该输入框允许为空。

该类型的配套属性如下：

- `maxlength`：可以输入的最大字符数。
- `minlength`：可以输入的最少字符数。
- `multiple`：布尔属性，是否允许输入多个以逗号分隔的电子邮箱。
- `pattern`：输入必须匹配的正则表达式。
- `placeholder`：输入为空时的显示文本。
- `readonly`：布尔属性，该输入框是否只读。
- `size`：一个非负整数，表示输入框的显示长度为多少个字符。
- `spellcheck`：是否对输入内容启用拼写检查，可能的值为 true 或 false。

该类型还可以搭配 `<datalist>` 标签，提供输入的备选项。

```html
<input type="email" size="40" list="defaultEmails">

<datalist id="defaultEmails">
  <option value="jbond007@mi6.defence.gov.uk">
  <option value="jbourne@unknown.net">
  <option value="nfury@shield.org">
  <option value="tony@starkindustries.com">
  <option value="hulk@grrrrrrrr.arg">
</datalist>
```

##### `type="password"`

`type="password"` 是一个密码输入框。用户的输入会被遮挡，字符通常显示星号（`*`）或点（`·`）。

```html
<input id="pass" type="password" name="password" minlength="8" required>
```

如果用户输入内容包含换行符（U+000A）和回车符（U+000D），浏览器会自动将这两个字符过滤掉。

该类型的配套属性如下：

- `maxlength`：可以输入的最大字符数。
- `minlength`：可以输入的最少字符数。
- `pattern`：输入必须匹配的正则表达式。
- `placeholder`：输入为空时的显示文本。
- `readonly`：布尔属性，该输入框是否只读。
- `size`：一个非负整数，表示输入框的显示长度为多少个字符。
- `autocomplete`：是否允许自动填充，可能的值有 `on`（允许自动填充）、`off`（不允许自动填充）、`current-password`（填入当前网站保存的密码）、`new-password`（自动生成一个随机密码）。
- `inputmode`：允许用户输入的数据类型，可能的值有 `none`（不使用系统输入法）、`text`（标准文本输入）、`decimal`（数字，包含小数）、`numeric`（数字0-9）等。

##### `type="file"`

`type="file"` 是一个文件选择框，允许用户选择一个或多个文件，常用于文件上传功能。

```html
<input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg">
```

该类型有以下属性：

- `accept`：允许选择的文件类型，使用逗号分隔，可以使用 MIME 类型（比如 image/jpeg），也可以使用后缀名（比如 .doc），还可以使用 audio/*（任何音频文件）、video/*（任何视频文件）、image/*（任何图像文件）等表示法。
- `capture`：用于捕获图像或视频数据的源，可能的值有 user（面向用户的摄像头或麦克风），environment（外接的摄像头或麦克风）。
- `multiple`：布尔属性，是否允许用户选择多个文件。

##### `type="hidden"`

`type="hidden"` 是一个不显示在页面的控件，用户无法输入它的值，主要用来向服务器传递一些隐藏信息。比如，CSRF 攻击会伪造表单数据，那么使用这个控件，可以为每个表单生成一个独一无二的隐藏编号，防止伪造表单提交。

```html
<input id="prodId" name="prodId" type="hidden" value="xm234jq">
```

上面这个控件，页面上是看不见的。用户提交表单的时候，浏览器会将 `prodId=xm234jq` 发给服务器。

##### `type="number"`

`type="number"` 是一个数字输入框，只能输入数字。浏览器通常会在输入框的最右侧，显示一个可以点击的上下箭头，点击向上箭头，数字会递增，点击向下箭头，数字会递减。

```html
<input type="number" id="tentacles" name="tentacles" min="10" max="100">
```

该类型可以接受任何数值，包括小数和整数。可以通过 `step` 属性，限定只接受整数。

- `max`：允许输入的最大数值。
- `min`：允许输入的最小数值。
- `placeholder`：用户输入为空时，显示的示例值。
- `readonly`：布尔属性，表示该控件是否为只读。
- `step`：点击向上和向下箭头时，数值每次递减的步长值。如果用户输入的值，不符合步长值的设定，浏览器会自动四舍五入到最近似的值。默认的步长值是 1，如果初始的 value 属性设为 1.5，那么点击向上箭头得到 2.5，点击向下箭头得到 0.5。

##### `type="range"`

`type="range"` 是一个滑块，用户拖动滑块，选择给定范围之中的一个数值。因为拖动产生的值是不精确的，如果需要精确数值，不建议使用这个控件。常见的例子是调节音量。

```html
<input type="range" id="start" name="volume" min="0" max="11">
```

该类型的配套属性如下，用法与 `type="number"` 一致。

- `max`：允许的最大值，默认为100。
- `min`：允许的最小值，默认为0。
- `step`：步长值，默认为1。
`value` 属性的初始值就是滑块的默认位置。如果没有设置 `value` 属性，滑块默认就会停在最大值和最小值中间。如果 `max` 属性、`min` 属性、`value` 属性都没有设置，那么 `value` 属性为 50。

该类型与 `<datalist>` 标签配合使用，可以在滑动区域产生刻度。

```html
<input type="range" list="tick_marks">

<datalist id="tick_marks">
  <option value="0" label="0%">
  <option value="10">
  <option value="20">
  <option value="30">
  <option value="40">
  <option value="50" label="50%">
  <option value="60">
  <option value="70">
  <option value="80">
  <option value="90">
  <option value="100" label="100%">
</datalist>
```

注意，浏览器生成的都是水平滑块。如果想要生成垂直滑块，可以使用 CSS 改变滑块区域的方向。

##### `type="url"`

`type="url"` 是一个只能输入网址的文本框。提交表单之前，浏览器会自动检查网址格式是否正确，如果不正确，就会无法提交。

```html
<input type="url" name="url" id="url" placeholder="https://example.com" pattern="https://.*" size="30" required>
```

上面代码的 `pattern` 属性指定输入的网址只能使用 HTTPS 协议。注意：该类型规定，不带有协议的网址是无效的，比如 foo.com 是无效的，<http://foo.com> 是有效的。

该类型的配套属性如下。

- `maxlength`：允许的最大字符数。
- `minlength`：允许的最少字符串。
- `pattern`：输入内容必须匹配的正则表达式。
- `placeholder`：输入为空时显示的示例文本。
- `readonly`：布尔属性，表示该控件的内容是否只读。
- `size`：一个非负整数，表示该输入框显示宽度为多少个字符。
- `spellcheck`：是否启动拼写检查，可能的值为 true（启用）和 false（不启用）。

该类型与 `<datalist>` 标签搭配使用，可以形成下拉列表供用户选择。随着用户不断键入，会缩小显示范围，只显示匹配的备选项。

```html
<input id="myURL" name="myURL" type="url" list="defaultURLs">

<datalist id="defaultURLs">
  <option value="https://developer.mozilla.org/" label="MDN Web Docs">
  <option value="http://www.google.com/" label="Google">
  <option value="http://www.microsoft.com/" label="Microsoft">
  <option value="https://www.mozilla.org/" label="Mozilla">
  <option value="http://w3.org/" label="W3C">
</datalist>
```

##### `type="tel"`

`type="tel"` 是一个只能输入电话号码的输入框。由于全世界的电话号码格式都不相同，因此浏览器没有默认的验证模式，大多数时候需要自定义验证。

```html
<input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
<small>Format: 123-456-7890</small>
```

该类型的配套属性如下。

- `maxlength`：允许的最大字符数。
- `minlength`：允许的最少字符串。
- `pattern`：输入内容必须匹配的正则表达式。
- `placeholder`：输入为空时显示的示例文本。
- `readonly`：布尔属性，表示该控件的内容是否只读。
- `size`：一个非负整数，表示该输入框显示宽度为多少个字符。

##### `type="color"`

`type="color"` 是一个选择颜色的控件，它的值一律都是 `#rrggbb` 格式。

```html
<input type="color" id="background" name="background" value="#e66465">
```

上面代码在 Chrome 浏览器中，会显示一个 #e66465 的色块。点击色块，就会出现一个拾色器，供用户选择颜色。如果没有指定 `value` 属性的初始值，默认值为 #000000（黑色）。

##### `type="date"`

`type="date"` 是一个只能输入日期的输入框，用户可以输入年月日，但是不能输入时分秒。输入格式是 YYYY-MM-DD。

```html
<input type="date" id="start" name="start" value="2018-07-22" min="2018-01-01" max="2018-12-31">
```

上面代码会显示一个输入框，默认日期是2018年7月22日。用户点击以后，会日期选择器，供用户选择新的日期。

该类型有以下配套属性：

- `max`：可以允许的最晚日期，格式为 yyyy-MM-dd。
- `min`：可以允许的最早日期，格式为 yyyy-MM-dd。
- `step`：步长值，一个数字，以天为单位。

##### `type="time"`

`type="time"` 是一个只能输入时间的输入框，可以输入时分秒，不能输入年月日。日期格式是 24 小时制的 hh:mm，如果包括秒数，格式则是hh:mm:ss。日期选择器的形式则随浏览器不同而不同。

```html
<input type="time" id="appt" name="appt" min="9:00" max="18:00" required>
<small>营业时间上午9点到下午6点</small>
```

该类型有以下配套属性：

- `max`：允许的最晚时间。
- `min`：允许的最早时间。
- `readonly`：布尔属性，表示用户是否不可以编辑时间。
- `step`：步长值，单位为秒。

##### `type="month"`

`type="month"` 是一个只能输入年份和月份的输入框，格式为 YYYY-MM。

```html
<input type="month" id="start" name="start" min="2018-03" value="2018-05">
```

该类型有以下配套属性。

- `max`：允许的最晚时间，格式为yyyy-MM。
- `min`：允许的最早时间，格式为yyyy-MM。
- `readonly`：布尔属性，表示用户是否不可以编辑时间。
- `step`：步长值，单位为月。

##### `type="week"`

`type="week"` 是一个输入一年中第几周的输入框。格式为 yyyy-Www，比如 2018-W18 表示 2018 年第 18 周。

```html
<input type="week" name="week" id="camp-week" min="2018-W18" max="2018-W26" required>
```

该类型有以下配套属性：

- `max`：允许的最晚时间，格式为 yyyy-Www。
- `min`：允许的最早时间，格式为 yyyy-Www。
- `readonly`：布尔属性，表示用户是否不可以编辑时间。
- `step`：步长值，单位为周。

##### `type="datetime-local"`

`type="datetime-local"` 是一个时间输入框，让用户输入年月日和时分，格式为 yyyy-MM-ddThh:mm。注意，该控件不支持秒。

```html
<input
    id="meeting-time"
    type="datetime-local"
    name="meeting-time"
    value="2018-06-12T19:30"
    min="2018-06-07T00:00"
    max="2018-06-14T00:00"
>
```

该类型有以下配套属性。

- `max`：允许的最晚时间，格式为 yyyy-MM-ddThh:mm。
- `min`：允许的最早时间，格式为 yyyy-MM-ddThh:mm。
- `step`：步长值，单位为秒，默认值是 60。

### `<button>`

`<button>` 标签会生成一个可以点击的按钮，没有默认行为，通常需要用 `type` 属性或脚本指定按钮的功能。

```html
<button name="search" type="submit">
  <img src="search.gif">搜索
</button>
```

`<button>` 具有以下属性：

- `autofocus`：布尔属性，表示网页加载时，焦点就在这个按钮。网页里面只能有一个元素具有这个属性。
- `disabled`：布尔属性，表示按钮不可用，会导致按钮变灰，不可点击。
- `name`：按钮的名称，将以 `name=value` 的形式，随表单一起提交到服务器。
- `value`：按钮的值，将以 `name=value` 的形式，随表单一起提交到服务器。
- `type`：按钮的类型，可能的值有三种：
    - `submit`：默认值，点击后将数据提交给服务器。
    - `reset`：将所有控件的值重置为初始值。
    - `button`：没有默认行为，由脚本指定按钮的行为。
- `form`：指定按钮关联的 `<form>` 表单，值为 `<form>` 的 `id` 属性。如果省略该属性，默认关联按钮所在父表单。
- `formaction`：数据提交到服务器的目标 URL，会覆盖 `<form>` 元素的 `action` 属性。
- `formenctype`：数据提交到服务器的编码方式，会覆盖 `<form>` 元素的 `enctype` 属性。可能的值有三种：
    - `application/x-www-form-urlencoded`：默认值。
    - `multipart/form-data`：只用于文件上传。
    - `text/plain`
- `formmethod`：数据提交到服务器使用的 HTTP 方法，会覆盖 `<form>` 元素的 `method` 属性，可能的值为 post 或 get。
- `formnovalidate`：布尔属性，数据提交到服务器时关闭本地验证，会覆盖 `<form>` 元素的 `novalidate` 属性。
- `formtarget`：数据提交到服务器后，展示服务器返回数据的窗口，会覆盖 `<form>` 元素的 `target` 属性。可能的值有：
    - `_self`：当前窗口。
    - `_blank`：新的空窗口。
    - `_parent`：父窗口。
    - `_top`：顶层窗口。

### `<select>`

`<select>` 标签用于生成一个下拉菜单。

```html
<label for="pet-select">宠物：</label>

<select id="pet-select" name="pet-select">
  <option value="">--请选择一项--</option>
  <option value="dog">狗</option>
  <option value="cat">猫</option>
  <option value="others">其他</option>
</select>
```

下拉菜单的菜单项由 `<option>` 标签给出，每个 `<option>` 代表可以选择的一个值。选中的 `<option>` 的 `value` 属性，就是 `<select>` 控件发送的服务器的值。`<option>` 有一个布尔属性 `selected`，一旦设置，就表示该项是默认选中的菜单项。

```html
<select name="choice">
  <option value="first">First Value</option>
  <option value="second" selected>Second Value</option>
  <option value="third">Third Value</option>
</select>
```

上面代码中，第二项 Second Value 是默认选中的。页面加载的时候，会直接显示在下拉菜单上。

`<select>` 有如下属性：

- `autofocus`：布尔属性，页面加载时是否自动获得焦点。
- `disabled`：布尔属性，是否禁用当前控件。
- `form`：关联表单的 `id` 属性。
- `multiple`：布尔属性，是否可以选择多个菜单项。默认情况下，只能选择一项。一旦设置，多数浏览器会显示一个滚动列表框。用户可能需要按住 Shift 或其他功能键，选中多项。
- `name`：控件名。
- `required`：布尔属性，是否为必填控件。
- `size`：设置了 `multiple` 属性时，页面显示时一次可见的行数，其他行需要滚动查看。

### `<option>`，`<optgroup>`

`<option>` 标签用在 `<select>`、`<optgroup>`、`<datalist>` 里面，表示一个菜单项。

它有如下属性。

- `disabled`：布尔属性，是否禁用该项。
- `label`：该项的说明。如果省略，则等于该项的文本内容。
- `selected`：布尔属性，是否为默认值。显然，一组菜单中，只能有一个菜单项设置该属性。
- `value`：该项提交到服务器的值。如果省略，则等于该项的文本内容。

`<optgroup>` 表示菜单项的分组，通常用在 `<select>` 内部。

上面代码中，`<select>` 是一个下拉菜单，它的内部使用 `<optgroup>` 将菜单项分成两组。每组有自己的标题，会加粗显示，但是用户无法选中。

它的属性如下：

`disabled`：布尔设置，是否禁用该组。一旦设置，该组所有的菜单项都不可选。
`label`：菜单项分组的标题。

### `<datalist>`

`<datalist>` 标签是一个容器标签，用于为指定控件提供一组相关数据，通常用于生成输入提示。它的内部使用 `<option>`，生成每个菜单项。

```html
<label for="ice-cream-choice">冰淇淋：</label>
<input type="text" list="ice-cream-flavors" id="ice-cream-choice" name="ice-cream-choice">
<datalist id="ice-cream-flavors">
  <option value="巧克力">
  <option value="椰子">
  <option value="薄荷">
  <option value="草莓">
  <option value="香草">
</datalist>
```

`<option>` 标签还可以加入 `label` 属性，作为说明文字。Chrome 浏览器会将其显示在 `value` 的下一行。

```html
<datalist id="ide">
  <option value="Brackets" label="by Adobe">
  <option value="Coda" label="by Panic">
</datalist>
```

### `<textarea>`

`<textarea>` 是一个块级元素，用来生成多行的文本框。

```html
<textarea id="story" name="story" rows="5" cols="33"> 这是一个很长的故事。</textarea>
```

该标签有如下属性：

- `autofocus`：布尔属性，是否自动获得焦点。
- `cols`：文本框的宽度，单位为字符，默认值为 20。
- `dir`：设定文本方向，
    - `dir="ltr"`：从左到右。
    - `dir="rtl"`：从右到左，
    - `dir="auto"`：让浏览器根据用户输入自动调整。
- `disabled`：布尔属性，是否禁用该控件。
- `form`：关联表单的 `id` 属性。
- `maxlength`：允许输入的最大字符数。如果未指定此值，用户可以输入无限数量的字符。
- `minlength`：允许输入的最小字符数。
- `name`：控件的名称。
- `placeholder`：输入为空时显示的提示文本。
- `readonly`：布尔属性，控件是否为只读。
- `required`：布尔属性，控件是否为必填。
- `rows`：文本框的高度，单位为行。
- `spellcheck`：是否打开浏览器的拼写检查。
    - `default`：由父元素或网页设置决定。
    - `true`
    - `false`
- `wrap`：输入的文本是否自动换行。
    - `soft`：输入内容超过宽度时自动换行，但不会加入新的换行符，并且浏览器保证所有换行符都是 CR + LR，这是默认值。
    - `hard`：浏览器自动插入换行符 CR + LF，使得每行不超过控件的宽度。
    - `off`：关闭自动换行，单行长度超过宽度时，会出现水平滚动条。

### `<output>`

`<output>` 标签是一个行内元素，用于显示用户操作的结果。

```html
<input type="number" name="a" value="10"> +
<input type="number" name="b" value="10"> =
<output name="result">20</output>
```

该标签有如下属性：

- `for`：关联控件的 `id` 属性，表示为该控件的操作结果。
- `form`：关联表单的 `id` 属性。
- `name`：控件的名称。

### `<progress>`

`<progress>` 标签是一个行内元素，表示任务的完成进度。浏览器通常会将显示为进度条。

```html
<progress id="file" max="100" value="70"> 70% </progress>
```

该标签有如下属性：

- `max`：进度条的最大值，应该是一个大于 0 的浮点数。默认值为 1。
- `value`：进度条的当前值。它必须是 0 和 `max` 属性之间的一个有效浮点数。如果省略了 `max` 属性，该值则必须在 0 和 1 之间。如果省略了 `value` 属性，则进度条会出现滚动，表明正在进行中，无法知道完成的进度。

### `<meter>`

`<meter>` 标签是一个行内元素，表示指示器，用来显示已知范围内的一个值，很适合用于任务的当前进度、磁盘已用空间、充电量等带有比例性质的场合。浏览器通常会将其显示为一个不会滚动的指示条。

```html
<p>烤箱的当前温度是<meter min="200" max="500" value="350"> 350 度</meter>。</p>
```

`<meter>` 元素的子元素，正常情况下不会显示。只有在浏览器不支持 `<meter>` 时才会显示。

该标签有如下属性：

- `min`：范围的下限，必须小于 `max` 属性。如果省略，则默认为 0。
- `max`：范围的上限，必须大于 `min` 属性。如果省略，则默认为 1。
- `value`：当前值，必须在 `min` 属性和 `max` 属性之间。如果省略，则默认为 0。
- `low`：表示“低端”的上限门槛值，必须大于 `min` 属性，小于 `high` 属性和 `max` 属性。如果省略，则等于 `min` 属性。
- `high`：表示“高端”的下限门槛值，必须小于 `max` 属性，大于 `low` 属性和 `min` 属性。如果省略，则等于 `max` 属性。
- `optimum`：指定最佳值，必须在 `min` 属性和 `max` 属性之间。它应该与 `low` 属性和 `high` `属性一起使用，表示最佳范围。如果optimum` 小于 `low` 属性，则表示“低端”是最佳范围；如果大于 `high` 属性，则表示“高端”是最佳范围；如果在 `low` 和 `high` 之间，则表示“中间地带”是最佳范围。如果省略，则等于 `min` 和 `max` 的中间值。
- `form`：关联表单的 `id` 属性。

Chrome 浏览器使用三种颜色，表示指示条所处的位置。较好情况时，当前位置为绿色；一般情况时，当前位置为黄色；较差情况时，当前位置为红色。

```html
<meter id="fuel" name="fuel" min="0" max="100" low="33" high="66" optimum="80" value="50"> at 50/100 </meter>
```

## 其他标签

### `<dialog>`

`<dialog>` 标签表示一个可以关闭的对话框。默认情况下，对话框是隐藏的，不会在网页上显示。如果要让对话框显示，必须加上 `open` 属性。

```html
<dialog open>
  Hello world
</dialog>
```

`<dialog>` 元素里面，可以放入其他 HTML 元素。

```html
<dialog open>
  <form method="dialog">
    <input type="text">
    <button type="submit" value="foo">提交</button>
  </form>
</dialog>
```

上例中 `<form>` 的 `method` 属性设为 dialog，这时点击提交按钮，对话框就会消失。但是表单不会提交到服务器，浏览器会将表单元素的`returnValue` 属性设为 Submit 按钮的 `value` 属性。

#### JavaScript API

`<dialog>` 元素的 JavaScript API 提供 `Dialog.showModal()` 和 `Dialog.close()` 两个方法，用于打开/关闭对话框。

```js
const modal = document.querySelector('dialog');
// 对话框显示，相当于增加 open 属性
modal.showModal();
// 对话框关闭，相当于移除 open 属性
modal.close();
```

开发者可以提供关闭按钮，让其调用 `Dialog.close()` 方法，关闭对话框。`Dialog.close()` 方法可以接受一个字符串作为参数，用于传递信息。`<dialog>` 接口的 `returnValue` 属性可以读取这个字符串，否则`returnValue` 属性等于提交按钮的 `value` 属性。

```js
modal.close('Accepted');
modal.returnValue // "Accepted"
```

`Dialog.showModal()` 方法唤起对话框时，会有一个透明层，阻止用户与对话框外部的内容互动。CSS 提供了一个 Dialog 元素的 `::backdrop` 伪类，用于选中这个透明层，因此可以编写样式让透明层变得可见。

```css
dialog {
  padding: 0;
  border: 0;
  border-radius: 0.6rem;
  box-shadow: 0 0 1em black;
}

dialog::backdrop {
  /* make the backdrop a semi-transparent black */
  background-color: rgba(0, 0, 0, 0.4);
}
```

上面代码不仅为 `<dialog>` 指定了样式，还将对话框的透明层变成了灰色透明。

`<dialog>` 元素还有一个 `Dialog.show()` 方法，也能唤起对话框，但是没有透明层，用户可以与对话框外部的内容互动。

#### 事件

`<dialog>` 元素有两个事件，可以监听。

- `close`：对话框关闭时触发。
- `cancel`：用户按下 Esc 键关闭对话框时触发。

如果希望用户点击透明层，就关闭对话框，可以用下面的代码。

```js
modal.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.close('cancelled');
  }
});
```

### `<details>`，`<summary>`

- `<details>` 标签用来折叠内容，浏览器会折叠显示该标签的内容。
    - `<details>` 标签的 `open` 属性，用于默认打开折叠。
- `<summary>` 标签用来定制折叠内容的标题。

    ```html
    <details>
      <summary>这是标题</summary>
      这是一段解释文本。
    </details>
    ```

通过 CSS 设置 `summary::-webkit-details-marker`，可以改变标题前面的三角箭头。

```css
summary::-webkit-details-marker {
  background: url(https://example.com/foo.svg);
  color: transparent;
}
```

另一种替换箭头的方法：

```css
summary::-webkit-details-marker {
  display: none;
}
summary:before {
  content: "\2714";
  color: #696f7c;
  margin-right: 5px;
}
```

#### `<details>`，`<summary>` 的 JavaScript API

`Details` 元素的 `open` 属性返回 `<details>` 当前是打开还是关闭。

```js
const details = document.querySelector('details');

if (detail.open === true) {
  // 展开状态
} else {
  // 折叠状态
}
```

`Details` 元素有一个 `toggle` 事件，打开或关闭折叠时，都会触发这个事件。

```js
details.addEventListener('toggle', event => {
  if (details.open) {
    /* 展开状况 */
  } else {
    /* 折叠状态 */
  }
});
```
