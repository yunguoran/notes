# 额外教程（Additional tutorials）

## 高级效果（Advanced styling effects）

### 使用 `box-shadow` 属性实现阴影效果

`box-shadow` 是 CSS 中用于给元素盒子添加阴影效果的属性，可以创建外阴影、内阴影和多层阴影。该属性不影响布局尺寸，只是视觉效果。

```css
box-shadow: [inset] <offset-x> <offset-y> [blur-radius] [spread-radius] <color>;
```

- `inset`：可选，内阴影。
    - 值就是 `inset`，将阴影画在元素内部。常用于凹陷效果或输入框。
- `offset-x`：水平偏移（必填）。
    - 正值向右，负值向左。
- `offset-y`：垂直偏移（必填）。
    - 正值向下，负值向上。
- `blur-radius`：模糊半径（可选）。
    - 数值越大，阴影越软。
    - 不能为负数。
- `spread-radius`：扩散半径（可选）。
    - 正值阴影向外扩张。
    - 负值阴影向内收缩。
- `color`：颜色（可选，默认当前文字颜色）。
    - 支持所有 CSS 颜色格式。

注意：

- 可以在单个 `box-shadow` 中指定多个阴影，以逗号分隔。
- `inset` 和正负偏移结合可以实现不同的效果：
    - `inset` + 正偏移可以实现凹陷效果。
    - `inset` + 负偏移可以实现凸起或浮雕效果。
    - 常规阴影 + 正偏移可以实现外凸效果。
    - 常规阴影 + 负偏移可以实现反向外凸效果。

### 使用 `filter` 属性实现滤镜效果

`filter` 是在绘制阶段生效（类似于后期特效），不会影响布局。

- 可以同时叠加多个滤镜，叠加顺序会影响最终效果。
- 可以给任何元素添加滤镜，而不仅仅只是图片元素。

#### `blur()` 函数

常用于背景虚化，参数必须是 `<length>` 类型，不能是百分比。

```css
filter: blur(4px);
```

#### `grayscale()` 函数

灰度。`0%` 是原图；`100%` 是完全灰度。

```css
filter: grayscale(100%);
```

#### `brightness()` 函数

亮度。`< 100%` 变暗；`> 100%`：变亮。

```css
filter: brightness(120%);
```

#### `contrast()` 函数

对比度。`100%` 是原始对比度。

```css
filter: contrast(150%);
```

#### `sepia()` 函数

复古棕褐色。

```css
filter: sepia(80%);
```

#### `invert()` 反转

颜色反转，常用于深色模式下反转图标。

```css
filter: invert(100%);
```

#### `opacity()` 函数

区别于 `opacity` 属性，`filter: opacity()` 不会影响子元素的点击测试方式，是在绘制后处理的。

```css
filter: opacity(50%);
```

#### `saturate()` 函数

饱和度。`100%` 是原始饱和度；`0%` 约等于灰度。

```css
filter: saturate(200%);
```

#### `hue-rotate()` 函数

色相旋转。参数是角度，常用于动态主题色，`hover` 色变。

```css
filter: hue-rotate(90deg);
```

#### `drop-shadow()` 函数

投影。基于元素的 alpha 通道，不会产生矩形阴影，适合 PNG / SVG 图标。

- `drop-shadow()` 产生的投影遵循文本和边框虚线的确切形状。
- `box-shadow()` 产生的阴影是跟随盒子的正方形。

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Sizing a blog page challenge</title>
    <link href="styles.css" rel="stylesheet" />
  </head>
  <body>
    <p class="filter">Filter</p>
    <p class="box-shadow">Box shadow</p>
  </body>
</html>
```

```css
body {
  font-family: sans-serif;
}
p {
  margin: 1em 2em;
  padding: 20px;
  width: 100px;
  display: inline-block;
  border: 5px dashed red;
}

.filter {
  filter: drop-shadow(5px 5px 1px rgb(0 0 0 / 70%));
}

.box-shadow {
  box-shadow: 5px 5px 1px rgb(0 0 0 / 70%);
}
```

### [混合模式（Blend Modes）](https://mdn.github.io/learning-area/css/styling-boxes/advanced_box_effects/blend-modes.html)

CSS 混合模式用来定义两个图层的颜色如何进行混合计算。

#### `background-blend-mode` 属性

控制同一个元素的多个 `background` 之间如何混合，不影响元素与外部内容。

#### `mix-blend-mode` 属性

控制一个元素与它后面的一切内容如何混合，类似 PS 中图层混合模式。

`background-blend-mode` 和 `mix-blend-mode` 的属性值是通用的：

- `normal`：默认，不混合，直接覆盖。
- `multiply`：正片叠底。
- `screen`：滤色（变亮）。
- `overlay`：叠加（亮的更亮，暗的更暗）。
- `darken`。
- `lighten`。

### CSS shapes

CSS Shapes 用来定义非矩形的内容环绕区域，主要解决文字如何绕着不规则形状排版的问题。

#### `shape-outside` 属性

用来定义内容环绕的形状，但没有 `float`（或类似效果）是不会生效的。

```html
<div class="wrapper">
  <img
    alt="balloon"
    src="https://mdn.github.io/shared-assets/images/examples/round-balloon.png" />
  <p>
    One November night in the year 1782, so the story runs, two brothers sat
    over their winter fire in the little French town of Annonay, watching the
    grey smoke-wreaths from the hearth curl up the wide chimney. Their names
    were Stephen and Joseph Montgolfier, they were papermakers by trade, and
    were noted as possessing thoughtful minds and a deep interest in all
    scientific knowledge and new discovery. Before that night—a memorable night,
    as it was to prove—hundreds of millions of people had watched the rising
    smoke-wreaths of their fires without drawing any special inspiration from
    the fact.
  </p>
</div>
```

```css
body {
  font-family: sans-serif;
}

img {
  float: left;
  shape-outside: circle(50%);
}
```

### `-webkit-background-clip: text`

把元素的背景裁剪成文字的形状，背景只在文字轮廓里可见。用以实现渐变文字或图片填充文字。

```html
<h2>WOW</h2>
<h2 class="text-clip">WOW</h2>
```

```css
h2 {
  color: white;
  display: inline-block;
  background: url("colorful-heart.png") no-repeat center;
}

.text-clip {
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

## 层叠（Cascade）

### 特异性（Specificity）

特异性是一种算法，浏览器用它来决定哪个属性值适用于某个元素。

不同的选择器类型有不同的特异性：

- 类型（元素）选择器和伪元素选择器具有相同的特异性，优先级较低。
- 类选择器、属性选择器和伪类选择器具有相同的特异性，优先级中等。
- ID 选择器优先级较高。

注意：

- 通用选择器、组合器选择器和特异性调整选择器（`:where()`）对特异性计算没有影响。
- 每种选择器有自己的特异性级别，高特异性的选择器不能被低特异性的选择器所覆盖。即：一百万个类选择器加起来也无法覆盖一个 ID 选择器。
- 内联样式没有任何的选择器，但具有比 ID 选择器更高的特异性，因此优先级比所有的选择器都要高。

### `!important`

`!important` 标志拥有最高的优先级（比内联样式还要高），它作用在单个声明上（即一个属性和属性值对上）。

- **除非万不得已，否则请不要使用它**。因为 `!important` 改变了层叠的正常工作方式，这会导致在大型的样式表中调试起来非常困难。
- 覆盖 `!important` 的唯一方法是在源代码顺序的较后位置包含另一个具有相同特殊性的 `!important`，或具有更高特殊性的 `!important`。

### 层叠算法

层叠算法是指浏览器在多个 CSS 规则同时作用到同一个元素、同一个属性时，如何一步步决定到底用哪一个值，其完整决策流程如下：

- 相关性（Relevance）：先初步筛选哪些规则能用得上。
    - 浏览器首先会寻找所有与该元素匹配的选择器声明块，如果一个属性在任何地方都没有被定义，则可能使用继承值或初始值。
- 重要性（Importance）：浏览器将规则分为普通声明和重要声明。
    - 带有 `!important` 标记的规则优先级高于不带该标记的规则。
- 来源（Origin）：区分规则来自那个来源。三种来源如下：
    - `user-agent stylesheets`：用户代理样式（浏览器默认样式）。
    - `user stylesheets`：用户样式（如阅读模式）。
    - `author stylesheets`：开发者写的 CSS。
- 层叠层（Cascade Layers）：同一来源内，按 `@layer` 再排序。
    - 普通声明：先声明的 layer > 后声明的 layer > 未分层样式。
    - 重要声明：未分层 important > 最后声明的 layer important > 最先声明的 layer important。
- 特异性（Specificity）：比谁的选择器更精确。
    - `inline` > `id` > `class` > `element`。
    - 只有在前面步骤完全打平时才看特异性。
- 作用域接近度（Scoping Proximity）：这是 Scoped CSS 专用规则。
    - 当特异性相同时，谁离作用域根更近谁就赢。
- 声明顺序（Order of Appearance）：谁写在后面用谁。

#### 来源和重要性

- 浏览器根据来源和重要性将每个声明分为六类，加上动画和过渡样式，优先级等级分为八个，从低到高依次为：
    - `user-agent normal styles`：浏览器默认样式。
    - `user normal styles`：用户自定义样式。
    - `author normal styles`：开发者写的普通 CSS。
    - `styles being animated`：正在被 CSS animation 控制的属性。
    - `author important styles`：开发者写的 `!important` 样式。
    - `user important styles`：用户自定义的 `!important` 样式。
    - `user-agent important styles`：浏览器的 `!important` 样式。
    - `styles being transitioned`：正在被 CSS transition 改变的属性。
- 其中有三类角色，分别为：
    - 用户代理（User Agent）就是代表用户获取、解析、渲染网页内容的软件程序，在绝大多数情况下，它指的是网页浏览器。
    - 用户（User）是指网站的访问者。
    - 作者（Author）是指开发者。
        - 写在 HTML 元素 `style` 属性中的样式属于开发者样式。
- 为什么动画优先级要低于 `!important`？
    - 动画可以长时间运行，必须可以被强制打断，而 `!important` 正是来做这件事情的。
- 为什么过渡状态必须是最高优先级？
    - 过渡是状态变化的视觉连续性保障。
    - 过渡不声明目标值，它只是让已有的变化变平滑。
    - 过渡运行时间极短，不应该被强制打断。

#### 来源和特异性

- 当重要性、来源和层叠层都一致时才比较特异性。不同来源的选择器，永远不会互相比较特异性。

    ```html
    <p><a href="https://example.org">User agent styles</a></p>
    <p><a class="author" href="https://example.org">Author styles</a></p>
    ```

    ```css
    :where(a.author) {
    text-decoration: overline;
    color: red;
    }
    ```

- 当重要性、来源、层叠层和特异性都一致时才比较出现顺序。

### 层叠层（Cascade Layers）

`@layer` 是 CSS Cascade Layers（层叠层）的一部分，是在 CSS Cascade Level 5 中引入的新特性，用来显式控制不同样式来源的层叠顺序，从而让样式的优先级管理更可控、更清晰。

```css
/* 声明顺序 */
@layer yellow, purple, green;

@layer yellow {
  #outer div ul .nav a {
    padding: 5px;
    display: inline-block;
    margin-bottom: 10px;
  }
}

@layer purple {
  div div li a {
    color: rebeccapurple;
  }
}

@layer green {
  a {
    color: lightgreen;
  }
}

/* 嵌套层 */
@layer framework {
  @layer reset, components;

  @layer reset {
    * { margin: 0; }
  }

  @layer components {
    button { border-radius: 4px; }
  }
}

@layer reset, theme, components;

@import url('reset.css') layer(reset);
@import url('theme.css') layer(theme);
@import url('components.css') layer(components);

/* 也可以导入到一个匿名层中 */
@import "style.css" layer;
```

- 后声明的层优先级更高，无层样式优先级高于所有在 `@layer` 内定义的样式。
- 如果在 `@layer` 后声明的层级先前已存在，那么该层不会被创建，且该层优先级高于此次新创建的层。
- 可以嵌套定义多个层，便于结构化管理。上述嵌套层的优先级顺序是 `framework.reset < framework.components`。
- 可以在 `@import` 时指定该文件属于某个 `layer`。
- 在 `!important` 下，优先级顺序完全反转。先声明的层优先级更高，且所有在 `@layer` 内定义的样式，优先级高于无层样式。

```css
/* 无层样式 */
body {
  color: #333333;
}

/* 创建第一层：layout */
@layer layout {
  main {
    display: grid;
  }
}

/* 创建第二层：匿名层 <anonymous(01)> */
@layer {
  body {
    margin: 0;
  }
}

/* 创建第三、四层: theme 和 utilities */
@layer theme, layout, utilities;

/* 添加样式给已经存在的 layout 层 */
@layer layout {
  main {
    color: black;
  }
}

/* 创建第五层：匿名层 <anonymous(02)> */
@layer {
  body {
    margin: 1vw;
  }
}
```

- 创建后无法更改图层顺序。
- 匿名层是通过向层叠层指定样式而不命名图层来创建的。只能在创建匿名层时添加样式且无法引用匿名层。
- 所有的无层样式都会处于一个隐式层中。

#### 层叠层创建和媒体查询

```css
@media (width >= 50em) {
  @layer site;
}

@layer page {
  h1 {
    text-decoration: overline;
    color: red;
  }
}

@layer site {
  h1 {
    text-decoration: underline;
    color: green;
  }
}
```

#### 使用 `@import` 将样式表导入具名和匿名层叠层

- `@import` 前面只能有 `@layer` 声明的层和 `@charset` 规则，其他的任何规则和样式都不能出现在 `@import` 之前。
- 可以将样式表导入到具名层中、嵌套层中和匿名层中。
- 可以将多个样式表导入到同一个层叠层中。
- 可以使用媒体查询和特性查询导入样式并根据特定条件创建层叠层。

```css
/* 将样式表导入到具名层中、嵌套层中和匿名层中 */
@import "components-lib.css" layer(components);
@import "dialog.css" layer(components.dialog);
@import "marketing.css" layer();

/* 将多个样式表导入到同一个层中 */
@import "comments.css" layer(social);
@import "sm-icons.css" layer(social);

/* 使用媒体查询和特性查询导入样式并根据特定条件创建层叠层 */
@import "ruby-narrow.css" layer(international) supports(display: ruby) (width < 32rem);
@import "ruby-wide.css" layer(international) supports(display: ruby) (width >= 32rem);
```

#### 嵌套层叠层

```css
@import "components-lib.css" layer(components);
@import "narrow-theme.css" layer(components.narrow);
@import "layers1.css" layer(example);

@layer example.layout {
  main {
    width: 50vw;
  }
}
```

#### 根据层的顺序确定优先级

##### 常规层

```css
@import "A.css" layer(firstLayer);
@import "B.css" layer(secondLayer);
@import "C.css";
```

优先级从低到高排序如下：

- firstLayer normal styles (A.css).
- secondLayer normal styles (B.css).
- unlayered normal styles (C.css).
- inline normal styles.
- animating styles.
- unlayered important styles (C.css).
- secondLayer important styles (B.css).
- firstLayer important styles (A.css).
- inline important styles.
- transitioning styles.

```html
<div>
  <h1 style="color: yellow; background-color: maroon !important;">
    Inline styles
  </h1>
</div>
```

```css
@layer A, B;

h1 {
  font-family: sans-serif;
  margin: 1em;
  padding: 0.2em;
  color: orange;
  background-color: green;
  text-decoration: overline pink !important;
  box-shadow: 5px 5px lightgreen !important;
}

@layer A {
  h1 {
    color: grey;
    background-color: black !important;
    text-decoration: line-through grey;
    box-shadow: -5px -5px lightblue !important;
    font-style: normal;
    font-weight: normal !important;
  }
}

@layer B {
  h1 {
    color: aqua;
    background: yellow !important;
    text-decoration: underline aqua;
    box-shadow: -5px 5px magenta !important;
    font-style: italic;
    font-weight: bold !important;
  }
}
```

##### 嵌套层

```css
div {
  background-color: wheat;
  color: pink !important;
}

@layer components {
  div {
    background-color: yellow;
    border: 1rem dashed red;
    color: orange !important;
  }
}

@layer components.narrow {
  div {
    background-color: skyblue;
    border: 1rem dashed blue;
    color: purple !important;
    border-radius: 50%;
  }
}

@layer components.wide {
  div {
    background-color: limegreen;
    border: 1rem dashed green;
    color: seagreen !important;
    border-radius: 20%;
  }
}
```

## 多文本方向（Multiple text directions）

处理不同文本方向是现代 Web 开发的重要部分，特别是对于支持多种语言的国际化应用。CSS 提供了多种机制来处理从左到右（LTR）和从右到左（RTL）的文本方向。

### 书写模式（Writing Modes）

`writing-mode` 属性定义了文本行块的流动方向，以及行内内容的排列方向。

```css
/* 水平书写模式 */
.horizontal-tb { writing-mode: horizontal-tb; } /* 默认值，水平从上到下 */

/* 垂直书写模式 */
.vertical-rl { writing-mode: vertical-rl; } /* 垂直从右到左 */
.vertical-lr { writing-mode: vertical-lr; } /* 垂直从左到右 */
```

块级元素和内联元素的方向并不是固定的，而是随着文字书写方向改变的。

- 块级方向是块级元素在页面上排列的方向。
    - 在 `horizontal-tb`（水平）模式下，块级方向是从上到下。
    - 在 `vertical-rl`（垂直）模式下，块级方向变为水平地从右向左。
- 内联方向始终指代句子流动的方向（即一行文字书写的方向）。

```html
<div class="wrapper">
  <div class="box horizontal">
    <h2>Heading</h2>
    <p>A paragraph demonstrating writing modes in CSS.</p>
  </div>
  <div class="box vertical">
    <h2>Heading</h2>
    <p>A paragraph demonstrating writing modes in CSS.</p>
  </div>
</div>
```

```css
body {
  font-family: sans-serif;
  height: 300px;
}
.wrapper {
  display: flex;
}

.box {
  border: 1px solid #cccccc;
  padding: 0.5em;
  margin: 10px;
}

.horizontal {
  writing-mode: horizontal-tb;
}

.vertical {
  writing-mode: vertical-rl;
}
```

### 方向（Direction）

`direction` 属性指定块级元素中文本的基线方向。

```css
/* 从左到右（默认） */
.ltr { direction: ltr; }

/* 从右到左 */
.rtl { direction: rtl; }
```

### 文本方向（Text Direction）

`text-direction` 属性控制行内文本的方向，通常与 `direction` 属性配合使用。

```css
/* 自动检测文本方向 */
.auto-dir { unicode-bidi: embed; }

/* 强制双向算法覆盖 */
.bidi-override { unicode-bidi: bidi-override; }
```

### 逻辑属性和值（Logical Properties and Values）

逻辑属性和值提供了一种与书写模式无关的方式来设置样式，它们基于文档的逻辑流而不是物理方向。

#### 逻辑尺寸（Sizing）

```css
.size-logical {
  /* 块级方向的尺寸 */
  block-size: 100px;
  min-block-size: 50px;
  max-block-size: 200px;

  /* 行内方向的尺寸 */
  inline-size: 200px;
  min-inline-size: 100px;
  max-inline-size: 300px;
}
```

```html
<div class="wrapper">
  <div class="box horizontal">
    <h2>Heading</h2>
    <p>A paragraph demonstrating writing modes in CSS.</p>
    <p>These boxes have inline-size.</p>
  </div>
  <div class="box vertical">
    <h2>Heading</h2>
    <p>A paragraph demonstrating writing modes in CSS.</p>
    <p>These boxes have inline-size.</p>
  </div>
</div>
```

```css
.wrapper {
  display: flex;
}

.box {
  border: 1px solid #cccccc;
  padding: 0.5em;
  margin: 10px;
  inline-size: 100px;
}

.horizontal {
  writing-mode: horizontal-tb;
}

.vertical {
  writing-mode: vertical-rl;
}
```

#### 逻辑边距（Margin）

```css
/* 物理属性 */
.margin-physical {
  margin-left: 10px;
  margin-right: 20px;
}

/* 逻辑属性 */
.margin-logical {
  margin-inline-start: 10px;  /* 对应 LTR 的 left，RTL 的 right */
  margin-inline-end: 20px;    /* 对应 LTR 的 right，RTL 的 left */
  margin-block-start: 15px;   /* 对应 top */
  margin-block-end: 10px;     /* 对应 bottom */
}
```

#### 逻辑内边距（Padding）

```css
.padding-logical {
  padding-inline-start: 10px;
  padding-inline-end: 20px;
  padding-block-start: 15px;
  padding-block-end: 10px;
}
```

#### 逻辑边框（Border）

```css
.border-logical {
  border-inline-start: 1px solid black;  /* 对应 LTR 的 left，RTL 的 right */
  border-inline-end: 1px solid black;    /* 对应 LTR 的 right，RTL 的 left */
  border-block-start: 1px solid black;   /* 对应 top */
  border-block-end: 1px solid black;     /* 对应 bottom */
}
```

### 实际应用示例

```html
<div class="container" dir="rtl">
  <p class="text">هذا نص عربي من اليمين إلى اليسار</p>
  <div class="box">
    <span class="item">عنصر 1</span>
    <span class="item">عنصر 2</span>
  </div>
</div>
```

```css
.container {
  writing-mode: horizontal-tb;
  direction: rtl;
}

.text {
  margin-inline-start: 20px;  /* 在 RTL 中表现为右边距 */
  margin-inline-end: 10px;    /* 在 RTL 中表现为左边距 */
}

.box {
  display: flex;
  gap: 10px;
}

.item {
  padding-inline: 10px;       /* 在 RTL 中 start 是右边，end 是左边 */
  border-inline-start: 1px solid #ccc;  /* 在 RTL 中表现为右边框 */
  border-inline-end: 1px solid #ddd;    /* 在 RTL 中表现为左边框 */
}
```

### 最佳实践

- 在需要支持多语言的项目中，优先使用逻辑属性而非物理属性，这样可以确保样式在不同文本方向下都能正确显示。
- 开发过程中使用 `dir="rtl"` 测试页面在从右到左文本方向下的表现。
- 对于需要支持中文、日文、韩文等语言的应用，考虑使用垂直书写模式。
- 许多现代 CSS 框架提供了工具类来处理文本方向，利用这些工具可以简化开发过程。

## 组织 CSS 代码

<https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/CSS>

### CSS 代码组织最佳实践

#### 保持一致性

在项目中保持一致性是最重要的原则。这包括：

- 类名命名约定。
- 颜色描述方式。
- 代码格式（使用制表符还是空格，缩进几个字符）。

#### 格式化可读的 CSS

有两种常见的 CSS 格式：

```css
/* 单行格式 */
.box {background-color: #567895; }
h2 {background-color: black; color: white; }

/* 多行格式（推荐） */
.box {
  background-color: #567895;
}

h2 {
  background-color: black;
  color: white;
}
```

#### 注释你的 CSS

```css
/* 这是一个 CSS 注释
可以跨多行 */

/* || 通用样式 */
/* || 排版 */
/* || 头部和主导航 */
```

#### 创建逻辑分段

```css
/* || 通用样式 */
body {
  /* ... */
}

h1, h2, h3, h4 {
  /* ... */
}

/* || 工具类 */
.no-bullets {
  list-style: none;
  margin: 0;
  padding: 0;
}

/* || 全站样式 */
.main-nav {
  /* ... */
}

.logo {
  /* ... */
}

/* || 商店页面 */
.product-listing {
  /* ... */
}

.product-box {
  /* ... */
}
```

#### 避免过度具体的选择器

```css
/* 不好的做法 */
article.main p.box {
  border: 1px solid #cccccc;
}

/* 好的做法 */
.box {
  border: 1px solid #cccccc;
}
```

### CSS 方法论 (CSS Methodologies)

CSS 方法论提供结构化的 CSS 编写和组织指南，强调可重用性和一致性，便于团队协作。

#### OOCSS（面向对象 CSS）

OOCSS 的核心思想是将 CSS 分离成可重用的对象，可以在网站任何地方使用。

传统方法的问题：

```css
.comment {
  display: grid;
  grid-template-columns: 1fr 3fr;
}

.comment img {
  border: 1px solid grey;
}

.comment .content {
  font-size: 0.8rem;
}

.list-item {
  display: grid;
  grid-template-columns: 1fr 3fr;
  border-bottom: 1px solid grey;
}

.list-item .content {
  font-size: 0.8rem;
}
```

OOCSS 方法：

```css
.media {
  display: grid;
  grid-template-columns: 1fr 3fr;
}

.media .content {
  font-size: 0.8rem;
}

.comment img {
  border: 1px solid grey;
}

.list-item {
  border-bottom: 1px solid grey;
}
```

HTML 使用：

```html
<!-- 评论 -->
<div class="media comment">
  <img src="" alt="" />
  <div class="content"></div>
</div>

<!-- 列表项 -->
<ul>
  <li class="media list-item">
    <img src="" alt="" />
    <div class="content"></div>
  </li>
</ul>
```

#### BEM（块元素修饰符）

BEM 将组件分为三个部分：

- 块：独立实体（如按钮、菜单）。
- 元素：与块相关的部分（如列表项、标题）。
- 修饰符：改变样式或行为的标志。

```html
<form class="form form--theme-xmas form--simple">
  <label class="label form__label" for="inputId"></label>
  <input class="form__input" type="text" id="inputId" />

  <input
    class="form__submit form__submit--disabled"
    type="submit"
    value="Submit" />
</form>
```

对应的 CSS：

```css
.form { }
.form--theme-xmas { }
.form--simple { }
.form__label { }
.form__input { }
.form__submit { }
.form__submit--disabled { }
```

### CSS 预处理器：Sass

Sass 是一种 CSS 预处理器，提供额外的功能来增强 CSS。

#### 变量定义

```scss
$base-color: #c6538c;

.alert {
  border: 1px solid $base-color;
}
```

编译后的 CSS：

```css
.alert {
  border: 1px solid #c6538c;
}
```

#### 组件样式表编译

使用 Sass 的部分功能（partials）来组织代码：

目录结构：

```text
foundation/
├── _code.scss
├── _lists.scss
├── _footer.scss
└── _links.scss
```

使用 `@use` 规则导入：

```scss
// foundation/_index.scss
@use "code";
@use "lists";
@use "footer";
@use "links";

// style.scss
@use "foundation";
```

这样可以将多个小样式表编译成一个或少数几个最终的样式表。
