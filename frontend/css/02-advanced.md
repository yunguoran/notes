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
