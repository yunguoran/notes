# LaTeX 语法详解

LaTeX 是一种基于 TeX 的排版系统，特别适合生成复杂的数学公式、科学文档和技术文档。本文档将详细介绍 LaTeX 的基础语法和常用功能。

- 完整的 LaTeX 符号表：[http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf](http://tug.ctan.org/info/symbols/comprehensive/symbols-a4.pdf)
- Overleaf 在线编辑器：[https://www.overleaf.com/](https://www.overleaf.com/)
- LaTeX 项目官方网站：[https://www.latex-project.org/](https://www.latex-project.org/)

## 文档结构

LaTeX 文档的基本结构如下：

```latex
\documentclass[...]{...}
% 导言区：加载宏包、定义命令等
\usepackage{...}
\title{...}
\author{...}
\date{...}

\begin{document}
% 正文内容
\maketitle % 生成标题页
...
\end{document}
```

- `\documentclass`: 指定文档类型（如 `article`，`book`，`report` 等）和选项（如字体大小、纸张大小等）。
- 导言区: 位于 `\documentclass` 和 `\begin{document}` 之间，用于设置文档的各种参数、加载宏包（`\usepackage`）、定义新的命令或环境等。
- `\title`，`\author`，`\date`: 分别定义文档的标题、作者和日期。这些信息不会直接显示在文档中，需要配合 `\maketitle` 命令使用。
- `\begin{document}` ... `\end{document}`: 包含文档的实际内容。

## 常用命令

### 文本格式化

- `\textbf{...}`: 粗体 (Bold Face)
- `\textit{...}`: 斜体 (Italic)
- `\underline{...}`: 下划线
- `\emph{...}`: 强调（通常为斜体）
- `\textrm{...}`: 直立罗马字体
- `\texttt{...}`: 打字机字体 (Typewriter Text)
- `\textsf{...}`: 无衬线字体 (Sans Serif)

### 特殊字符与符号

- `%`，`$`，`&`，`#`，`_`，`{`，`}` 需要使用反斜杠转义，如 `\%`，`\$`，`\&`，`\#`，`\_`，`\{`，`\}`。
- 省略号: `\dots` (行内)，`\cdots` (居中)，`\vdots` (垂直)，`\ddots` (对角)。
- 引号: 左单引号 `` ` ``，右单引号 `'`，左双引号 `` ` ``，右双引号 `''`。
- 破折号: 短破折号 `-`，长破折号 `--`，连字符 `---`。
- 版权符号: `\copyright`
- 注册商标: `\textregistered`
- 商标: `\texttrademark`

### 换行与分段

- `\\` 或 `\newline`: 强制换行（不开始新段落）。
- `\newpage` 或 `\clearpage`: 强制分页。
- 空行: 开始新段落。

### 空格

- `~`: 不可断行的空格。
- `\,`: 小空格 (thin space)。
- `\:`: 中等空格 (medium space)。
- `\;`: 大空格 (thick space)。
- `\!`: 负空格 (neg thinspace)。
- `\quad`，`\qquad`: 较大空格。

### 其他常用命令

- `\label{...}`: 给图表、公式、章节等添加标签，用于交叉引用。
- `\ref{...}`: 引用带有 `\label` 的对象的编号。
- `\cite{...}`: 引用参考文献。
- `\footnote{...}`: 添加脚注。
- `\url{...}` (需 `url` 宏包): 插入网址。
- `\includegraphics[...]{...}` (需 `graphicx` 宏包): 插入图片。

## 数学公式语法

LaTeX 最强大的功能之一是数学公式的排版。

### 数学模式

在 LaTeX 中有两种对数学公式排版的模式：

1. 使用 `$` 符号嵌入到文本中。
2. 使用数学“环境”。

#### 把数学公式嵌入到文本中

把数学公式放在两个 `$` 符号之间，例如：`$f(x) = x^2$` 会渲染为 $f(x) = x^2$。

#### 数学公式环境

使用 `equation` 环境，在这个环境中的代码都会渲染成数学公式：

**单行公式：**

```latex
\begin{equation}
  E = mc^2
\end{equation}
```

**多行对齐公式（align 环境）：**

```latex
\begin{align}
  1 + 2 &= 3\\
  1 &= 3 - 2
\end{align}
```

**带编号的多行公式（gather 环境）：**

```latex
\begin{gather}
  a = b + c\\
  d = e + f
\end{gather}
```

### 上下标

使用 `^` 表示上标，`_` 表示下标。

- `x^2` 显示为 $x^2$。
- `a_1` 显示为 $a_1$。
- `x^{2n+1}` 显示为 $x^{2n+1}$。
- `a_{ij}` 显示为 $a_{ij}$。

### 分数

使用 `\frac{分子}{分母}` 命令。

- `g(x) = \frac{1}{x}` 显示为 $g(x) = \frac{1}{x}$。
- `\frac{1}{\sqrt{x}}` 显示为 $\frac{1}{\sqrt{x}}$。

### 根式

使用 `\sqrt{被开方数}` 命令。

- `\sqrt{x}` 显示为 $\sqrt{x}$。
- `\sqrt[n]{x}` 显示为 $\sqrt[n]{x}$。

### 积分

使用 `\int` 命令，可添加上下限。

- `F(x) = \int_a^b \frac{1}{3}x^3` 显示为 $F(x) = \int_a^b \frac{1}{3}x^3$。
- `\int_{-\infty}^{+\infty} e^{-x^2} dx` 显示为 $\int_{-\infty}^{+\infty} e^{-x^2} dx$。

### 求和与乘积

- `\sum_{i=1}^{n} i` 显示为 $\sum_{i=1}^{n} i$。
- `\sum_{k=0}^{\infty} \frac{x^k}{k!}` 显示为 $\sum_{k=0}^{\infty} \frac{x^k}{k!}$。

使用 `\prod` 命令：

`\prod_{i=1}^{n} x_i` 显示为 $\prod_{i=1}^{n} x_i$。

### 希腊字母

希腊字母通过特定命令表示。

- `\alpha` 显示为 $\alpha$。
- `\beta` 显示为 $\beta$。
- `\gamma` 显示为 $\gamma$。
- `\delta` 显示为 $\delta$。
- `\epsilon` 显示为 $\epsilon$。
- `\zeta` 显示为 $\zeta$。
- `\eta` 显示为 $\eta$。
- `\theta` 显示为 $\theta$。
- `\iota` 显示为 $\iota$。
- `\kappa` 显示为 $\kappa$。
- `\lambda` 显示为 $\lambda$。
- `\mu` 显示为 $\mu$。
- `\nu` 显示为 $\nu$。
- `\xi` 显示为 $\xi$。
- `\pi` 显示为 $\pi$。
- `\rho` 显示为 $\rho$。
- `\sigma` 显示为 $\sigma$。
- `\tau` 显示为 $\tau$。
- `\upsilon` 显示为 $\upsilon$。
- `\phi` 显示为 $\phi$。
- `\chi` 显示为 $\chi$。
- `\psi` 显示为 $\psi$。
- `\omega` 显示为 $\omega$。

### 关系运算符

常见的关系运算符：

- `+`：$+$，`-`：$-$，`*`：$*$，`/`：$/$。
- `\cdot`：$\cdot$ (点乘)。
- `\times`：$\times$ (叉乘)。
- `\div`：$\div$ (除法)。
- `=`：$=$ (等于)。
- `\neq`：$\neq$ (不等于)。
- `<`：$<$，`>`：$>$ (小于，大于)。
- `\leq`：$\leq$ (小于等于)。
- `\geq`：$\geq$ (大于等于)。
- `\approx`：$\approx$ (约等于)。
- `\equiv`：$\equiv$ (恒等于)。
- `\pm`：$\pm$ (正负)。
- `\mp`：$\mp$ (负正)。

### 其他常用数学符号

- `\infty`：$\infty$ (无穷)。
- `\partial`：$\partial$ (偏导数)。
- `\nabla`：$\nabla$ (梯度)。
- `\forall`：$\forall$ (任意)。
- `\exists`：$\exists$ (存在)。
- `\emptyset`：$\emptyset$ (空集)。
- `\cup`：$\cup$ (并集)。
- `\cap`：$\cap$ (交集)。
- `\subset`：$\subset$ (子集)。
- `\in`：$\in$ (属于)。
- `\notin`：$\notin$ (不属于)。

### 矩阵

LaTeX 可以显示矩阵，放在 `matrix` 环境中：

```latex
\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}

% 带 [ ] 的矩阵
\left[
\begin{matrix}
1 & 0\\
0 & 1
\end{matrix}
\right]

% 其他类型的矩阵
\begin{pmatrix} % 圆括号矩阵
1 & 0\\
0 & 1
\end{pmatrix}

\begin{bmatrix} % 方括号矩阵
1 & 0\\
0 & 1
\end{bmatrix}

\begin{vmatrix} % 单竖线矩阵(行列式)
1 & 0\\
0 & 1
\end{vmatrix}

\begin{Vmatrix} % 双竖线矩阵
1 & 0\\
0 & 1
\end{Vmatrix}
```

### 自动调整大小的括号

使用 `\left` 和 `\right` 命令：

- `\left(\frac{1}{\sqrt{x}}\right)` 显示为 $\left(\frac{1}{\sqrt{x}}\right)$。
- `\left[\frac{a}{b}\right]` 显示为 $\left[\frac{a}{b}\right]$。
- `\left\{\frac{c}{d}\right\}` 显示为 $\left\{\frac{c}{d}\right\}$。

### 三角函数

- `\sin`：$\sin$，`\cos`：$\cos$，`\tan`：$\tan$，`\cot`：$\cot$，`\sec`：$\sec$，`\csc`：$\csc$。
- `\arcsin`：$\arcsin$，`\arccos`：$\arccos$，`\arctan`：$\arctan$。
- `\sinh`：$\sinh$，`\cosh`：$\cosh$，`\tanh`：$\tanh$。

### 微积分相关

- `\lim_{x \to \infty}` 显示为 $\lim_{x \to \infty}$。
- `\int` 显示为 $\int$。
- `\oint` 显示为 $\oint$。
- `\iint` 显示为 $\iint$。
- `\iiint` 显示为 $\iiint$。

### 特殊格式

- `\cdots` 显示为 $\cdots$ (居中省略号)。
- `\ldots` 显示为 $\ldots$ (底端省略号)。
- `\vdots` 显示为 $\vdots$ (垂直省略号)。
- `\ddots` 显示为 $\ddots$ (对角省略号)。

## 表格语法

### Table 环境和 Tabular 环境

#### Table 环境

Table 环境用于定义表格的整体结构，包括表格标题和位置控制：

```latex
\begin{table}[位置参数]
    % 表格内容
\end{table}
```

- 位置参数：`[htbp]`
    - `h`: 此处（here）- 尽量将表格放在当前位置
    - `t`: 顶部（top）- 页面顶部
    - `b`: 底部（bottom）- 页面底部
    - `p`: 浮动页（page）- 专门用于浮动体的单独页面
- 其他参数：
    - `!`: 忽略某些限制条件
    - `H`: 强制在此处放置（需要 `\usepackage{float}`）

#### Tabular 环境

Tabular 环境用于定义表格的具体内容和布局：

```latex
\begin{tabular}{列格式}
    % 表格数据
\end{tabular}
```

### 列格式

#### 基本对齐方式

- `l`: 左对齐
- `c`: 居中对齐
- `r`: 右对齐

#### 列间分隔符

- `|`: 垂直线
- `@{内容}`: 自定义列间内容
- `!{内容}`: 在列间插入内容

#### 示例

```latex
% 基本格式
\begin{tabular}{|l|c|r|}
    左对齐 & 居中 & 右对齐 \\
\end{tabular}

% 自定义间距
\begin{tabular}{l@{.}c@{--}r}
    内容 1 & 内容 2 & 内容 3 \\
\end{tabular}
```

#### 调整列间距

```latex
\setlength{\tabcolsep}{10 pt}  % 默认值为 6 pt
```

### 表格内容格式

#### 行和列的分隔

- `&`: 分隔列
- `\\`: 结束行
- `\hline`: 绘制水平线

#### 基本表格示例

```latex
\begin{table}[htbp]
    \centering
    \caption{一个简单的表格}
    \begin{tabular}{|c|c|}
        \hline
        列 1 & 列 2 \\
        \hline
        数据 1 & 数据 2 \\
        \hline
        数据 3 & 数据 4 \\
        \hline
    \end{tabular}
\end{table}
```

### 合并单元格

#### 合并列（使用 multicols 宏包）

需要引入宏包：

```latex
\usepackage{multirow}
\usepackage{multicol}
```

#### 使用 multicolumn 合并列

```latex
\multicolumn{列数}{对齐方式}{内容}
```

示例：

```latex
\begin{tabular}{|c|c|c|}
    \hline
    \multicolumn{2}{|c|}{合并前两列} & 第三列 \\
    \hline
    A & B & C \\
    \hline
\end{tabular}
```

#### 使用 multirow 合并行

```latex
\multirow{行数}{宽度}{内容}
```

示例：

```latex
\begin{tabular}{|c|c|}
    \hline
    \multirow{2}{4 em}{合并两行} & 内容 1 \\
    & 内容 2 \\
    \hline
\end{tabular}
```

### 三线表

三线表在学术论文中常用，只包含三条水平线：

```latex
% 需要引入 booktabs 宏包
\usepackage{booktabs}

\begin{table}[htbp]
    \centering
    \caption{一个三线表}
    \begin{tabular}{ccc}
        \toprule
        列 1 & 列 2 & 列 3 \\
        \midrule
        数据 1 & 数据 2 & 数据 3 \\
        数据 4 & 数据 5 & 数据 6 \\
        \bottomrule
    \end{tabular}
\end{table}
```

- `\toprule`: 顶部线
- `\midrule`: 中间线
- `\bottomrule`: 底部线

### 高级表格特性

#### 彩色单元格

```latex
\usepackage[table]{xcolor}

\begin{tabular}{|c|c|}
    \hline
    \cellcolor{blue!25} 蓝色背景 & 普通单元格 \\
    \hline
    \rowcolor{gray!25} 整行灰色 & 整行灰色 \\
    \hline
\end{tabular}
```

#### 跨页表格

```latex
\usepackage{longtable}

\begin{longtable}{|c|c|}
    \hline
    \multicolumn{2}{|c|}{表格标题} \\
    \hline
    列 1 & 列 2 \\
    \hline
    \endfirsthead

    \multicolumn{2}{c}{续表} \\
    \hline
    列 1 & 列 2 \\
    \hline
    \endhead

    数据 1 & 数据 2 \\
    数据 3 & 数据 4 \\
    \hline
\end{longtable}
```

### 表格标题和引用

```latex
\caption{表格标题}
\label{tab:label_name}

% 引用表格
如表 \ref{tab:label_name} 所示...
```

## 图片语法

### 插入图片

插入图片主要使用 `graphicx` 宏包提供的 `\includegraphics` 命令，并常与 `figure` 浮动环境结合使用。

```latex
\usepackage{graphicx}

\begin{figure}[位置参数]
  \centering % 使图片居中
  \includegraphics[选项]{图片文件名}
  \caption{图片标题} % 图片说明
  \label{fig:标签名} % 用于交叉引用
\end{figure}
```

- **位置参数**: `[h]` (here)，`[t]` (top)，`[b]` (bottom)，`[p]` (page of floats) 等，建议组合使用如 `[htbp]`。
- **选项**: 常用选项包括 `width=...`，`height=...`，`scale=...` (缩放比例) 等，用于调整图片大小。
- **图片文件名**: 不含扩展名，LaTeX 会自动查找支持的格式（如 `.pdf`，`.png`，`.jpg` 等）。

### 图片选项

- `width=0.5\textwidth`: 设置宽度为文本宽度的一半
- `height=5 cm`: 设置高度为 5 厘米
- `scale=0.8`: 按比例缩放
- `angle=45`: 旋转 45 度

## 列表语法

### 无序列表

```latex
\begin{itemize}
    \item 第一项
    \item 第二项
    \item 第三项
\end{itemize}
```

### 有序列表

```latex
\begin{enumerate}
    \item 第一项
    \item 第二项
    \item 第三项
\end{enumerate}
```

### 描述列表

```latex
\begin{description}
    \item[术语 1] 描述内容
    \item[术语 2] 描述内容
\end{description}
```

## 高级功能和环境

### 文本环境

- `center`: 居中文本
- `flushleft`: 左对齐文本
- `flushright`: 右对齐文本
- `quote`，`quotation`: 引用环境
- `verse`: 诗歌环境

### 框架环境

- `minipage{宽度}`: 创建一个独立的小页面环境
- `\fbox{...}` 或 `\framebox{...}`: 创建带边框的框

### 数学环境

- `equation`: 单行编号公式
- `align`，`alignat`: 多行对齐公式
- `gather`: 多行居中公式
- `multline`: 多行长公式（第一行左对齐，最后一行右对齐，中间居中）
- `cases`: 分情况讨论的公式

### 浮动环境

- `figure`: 图片浮动体
- `table`: 表格浮动体
- 通常包含 `\caption{...}` (标题) 和 `\label{...}` (标签)，并指定位置参数 `[h]`，`[t]`，`[b]`，`[p]` 等

### 代码环境

需要使用 `listings` 宏包：

```latex
\usepackage{listings}
\usepackage{xcolor}

\lstset{
    backgroundcolor=\color{gray!10},
    basicstyle=\ttfamily,
    keywordstyle=\color{blue},
    commentstyle=\color{green!60!black},
    stringstyle=\color{red}
}

\begin{lstlisting}[language=Python]
def hello():
    print("Hello, world!")
\end{lstlisting}
```

## 常用宏包

以下是一些常用的 LaTeX 宏包：

- `amsmath`: 增强数学功能
- `amssymb`: 额外的数学符号
- `geometry`: 页面布局设置
- `graphicx`: 图片插入
- `hyperref`: 超链接功能
- `listings`: 代码高亮
- `booktabs`: 专业表格线
- `multirow`: 表格跨行
- `multicol`: 多栏布局
- `xcolor`: 颜色支持

## 实用技巧

### 引用和交叉引用

```latex
\section{引言}
\label{sec:intro}

如 \ref{sec:intro} 节所述...

图 \ref{fig:myfig} 展示了...

表 \ref{tab:mytable} 列出了...
```

### 生成目录

```latex
\tableofcontents
```

### 生成参考文献

```latex
\begin{thebibliography}{99}
\bibitem{ref1} 作者. 文章标题. 期刊名称, 年份.
\end{thebibliography}
```

或者使用 BibTeX：

```latex
\bibliographystyle{plain}
\bibliography{references}
```

### 页面设置

```latex
\usepackage[margin=1 in]{geometry}  % 设置页边距
\usepackage{setspace}              % 设置行距
\doublespacing                    % 双倍行距
```
