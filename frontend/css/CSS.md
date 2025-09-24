# CSS（Cascading Style Sheets）

```css
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

上述代码的整个结构被称为 **ruleset**（规则集）。

- `p` 被称为 **selector**（选择器）。
- 大括号中以 semicolon（`;`）分隔的每一行称为一个 **declaration**（声明）。
- 第一个 **declaration** 中的 `color` 被称为 **property**（属性）。
- 第一个 **declaration** 中的 `red` 被称为 **property value**（属性值）。
- **property** 和 **property value** 中间以 colon（`:`）分隔。

```css
p,
.my-class,
#my-id {
  color: red;
}
```

多个 **selector** 之间以 comma（`,`）分隔。

- 上述例子中的 `p` 是 **type selector**（元素选择器）。
- `.my-class` 是 **class selector**（类选择器）。
- `#my-id` 是 **ID selector**（ID 选择器）。

## 字体

**Web safe fonts**（网页安全字体）指的是在大多数操作系统和设备上都自带安装、无需额外下载的字体。因为它们几乎可以保证在不同平台上正常显示，所以叫 “web safe”。

### `font-family` 属性

`font-family` 属性的值是按顺序写的多个字体名称，浏览器会依次寻找能用的字体，找到第一个可用的就用它。**通用字体族**通常写在最后作为兜底。下方例子中 `'Times New Roman'` 和 `Helvetica` 是字体名称，`sans-serif` 是通用字体族。`'Times New Roman'` 是带空格的字体，使用时必须加引号。

```css
body {
font-family: 'Times New Roman', Helvetica, sans-serif;
}
```

常见的通用字体族以及对应的网页安全字体如下：

- `serif`：有衬线字体
    - Times New Roman
    - Georgia
    - Garamond
    - Palatino Linotype / Book Antiqua
- `sans-serif`：无衬线字体
    - Arial
    - Helvetica
    - Verdana
    - Tahoma
    - Trebuchet MS
    - Geneva
- `monospace`：等宽字体
    - Courier New
    - Lucida Console
    - Monaco
- `cursive`：手写体
    - Comic Sans
    - Comic Sans MS
- `fantasy`：装饰性字体
    - Brush Script MT

### `font-size` 属性

CSS 中的 px（像素）是一个绝对长度单位，它定义为 1/96 英寸，因此 16px 在不同屏幕上显示的视觉大小是一致的。

- **PPI**（Pixels Per Inch）：每英寸像素数（物理像素密度）是每英寸所包含的像素数量，每英寸像素值越高，屏幕能显示的图像越精细。
- **DPR**（Device Pixel Ratio）设备像素比是 1 个 CSS 像素对应多少个物理像素。

    ```js
    value = window.devicePixelRatio
    console.log(value)
    ```

在 PPI 为 2 的屏幕上，1 个 CSS 像素会对应 2*2=4 个物理像素点，对于高度 16 CSS 像素 × 2 = 32 物理像素，因此 16px **大约**会占用 32 个物理像素的高度。大约是因为**字体渲染并不是严格的方块像素堆积**，字体有轮廓曲线，渲染引擎会用抗锯齿、亚像素渲染等手段来进行优化。

`font-size` 属性真正控制的是字体的标准高度（全方高度），当 `font-size` 改变时，整个字体字形被等比例放大或缩小。字体的宽度并不是独立变化的，它遵循一个核心原则：**保持字体的原始比例**。

### 加载第三方字体

以 [Google Fonts](https://fonts.google.com/) 为例:

- 选择你喜欢的字体。
- 在详情页点击 "Get font" 按钮。
- 在下一页中点击 "Get embed code" 按钮。
- 复制代码即可。

中国大陆建议先下载字体，导入到项目中自行维护。

## 文本

### `color` 属性

- `color` 属性专门用来设置文本的前景色（即字体颜色）。
- 应用到 `<p>` 元素时，会影响该段落里所有的文字内容。
- 注意：`color` 是 可继承属性，如果父元素设置了 `color`，子元素默认会继承。

### `text-align` 属性

决定行内内容（文字、行内元素、行内块元素）的水平对齐方式。常见取值如下：

- `left`：左对齐（默认，大多数语言用这个）
- `right`：右对齐（阿拉伯语等从右到左语言常用）
- `center`：居中对齐
- `justify`：两端对齐（调整单词间或字间距，让左右对齐，看起来像报纸排版）
- `start` / `end`：根据书写方向自动选择（现代浏览器更推荐）

### `line-height` 属性

用于设置行框的高度，即两行文本基线之间的距离。常见取值如下：

- `normal`：`line-height: normal;` 浏览器的默认值。具体数值由浏览器和字体族决定。
- 数值：`line-height: 1.5;` 表示相对于当前元素的 `font-size` 的倍数。
    - 具有继承性时，子元素会继承这个倍数，并根据自己的字体大小计算行高，不会产生意外的重叠问题。
- 长度值：`line-height: 24px;` 或者 `line-height: 1.5em;`（效果上等同于 `line-height: 1.5`）
    - 当使用 `em` 并发生继承时，子元素继承的是计算后的固定值，而不是比例，可能导致子元素字体变大时行高不够用。
- `percentage`：相对于当前元素的 `font-size` 进行计算。`line-height: 150%` 效果上等同于 `line-height: 1.5`。
    - 和 `em` 一样，存在继承问题。子元素继承的是计算后的固定值。

### `letter-spacing` 属性

用于控制字符之间的水平间距。常见取值如下：

- `normal`：默认字距（由字体自身决定）。
- 长度值：可以是固定像素，也可以是 `±0.02em` 这样的相对值，相对于当前元素的 `font-size` 进行计算。

### `word-spacing` 属性

用于控制单词之间的水平间距。常见取值同 `letter-spacing`。注意：在中文文本中，单词不是通过空格分隔的，所以 `word-spacing` 不起作用。

## CSS box 模型

CSS 布局主要是基于 box 模型。网页上的每个元素都是一个 box 模型。

![alt text](./images/box-mode.png)

### `width` 属性

设置元素的**内容区域**的宽度。常见取值如下：

- `auto`（默认值：由浏览器根据内容和父元素决定。。
- 具体数值：`px`、`em`、`rem`、`%` 等，如 `width: 200px;`。
- 现代 CSS 值
    - max-content
    - min-content
    - fit-content

注意：

- `width` 只控制 内容区域，不包括 `padding`、`border` 和 `margin`。
- 如果加上 `box-sizing: border-box;`，则 `width` 会包括 `padding` 和 `border`。

### `padding` 属性

设置内容和边框之间的**内边距**。和 `margin` 一样，可以写 1–4 个值。

注意：

- `padding` 会撑大元素的可见区域。
- 如果 `box-sizing: content-box;`（默认），`padding` 会增加元素总宽度。
- 如果 `box-sizing: border-box;`，则 `width` 包含 `padding`。

### `border` 属性

给元素内容和 padding 的外围绘制**边框**。组成部分如下：

- border-width：边框宽度（如：1px、2px）。
- border-style：边框样式（如：`solid`、`dashed`、`dotted`、`double`、`none`）。
- border-color：边框颜色（如：`red`）。

可以单独设置边框的每条边：

- `border-top`
- `border-right`
- `border-bottom`
- `border-left`

#### `border-radius` 属性

`border-radius` 可以让元素的 四个角（上左、上右、下右、下左）变成圆角或椭圆角。常见取值如下：

- 长度值：如 `px`、`em`，表示圆角半径。
- 百分比：相对于元素自身的大小计算（更常用于做圆形/椭圆）。

`border-radius` 的简写形式：

- `border-radius: 10px;`：四个角都是 10px 的圆角。
- `border-radius: 10px 20px;`：左上和右下角半径为 10px，右上和左下角半径为 20px。
- `border-radius: 10px 20px 30px;`：左上角 10px，右上和左下 20px，右下 30px。
- `border-radius: 10px 20px 30px 40px;`：左上、右上、右下、左下（顺时针）。

注意：

- 边框也会撑大元素的总尺寸，除非使用 `box-sizing: border-box;`。

### `background-color` 属性

设置元素背景的颜色，默认情况下作用范围是 content + padding + border。常见取值如下：

- 颜色名称：`red`、`blue`。
- 十六进制：#ff0000。
- RGB / RGBA：`rgb(255,0,0)`/ `rgba(255,0,0,0.5)`。
- HSL / HSLA：`hsl(0, 100%, 50%)`。
- transparent：`透明`。

### `margin` 属性

设置元素与外部其他元素之间的**外边距**。常见取值如下：

- 具体数值：`px`、`em`、`%` 等。
- `auto`：常用于水平居中（`margin: 0 auto;`）。

`margin` 的简写形式：

- `margin: 5px;`：上右下左都是 5px。
- `margin: 10px 20px;`：上下 10px，左右 20px。
- `margin: 0px 0px 5px;`：上 0px，左右 0px，下 5px。
- `margin: 5px 10px 15px 20px;`：上 5px，右 10px，下 15px，左 20px（顺时针）。

## 继承

`font-family`、`font-size`、`color` 属性都会继承自直接的父元素，继承的起点是 `<html>` 元素。

## 注释

在 `/*` 和 `*/` 之间的内容都是注释。
