# Linux

- [What is Linux and Why There are 100’s of Linux Distributions?](https://itsfoss.com/what-is-linux/)
- [Terminator 使用教程](https://zhuanlan.zhihu.com/p/391076088)
- [快乐的命令行](http://billie66.github.io/TLCL/book/index.html)
- [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh/wiki)
- [DNS 原理入门](https://www.ruanyifeng.com/blog/2016/06/dns.html)
- [Curl 的用法指南](http://www.ruanyifeng.com/blog/2019/09/curl-reference.html)
- [Telnet 模拟 HTTP 请求](https://www.cnblogs.com/stg609/archive/2008/07/06/1237000.html)
- [Linux 守护进程的启动方法](https://www.ruanyifeng.com/blog/2016/02/linux-daemon.html)
- [Systemd 入门教程：命令篇](https://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html)
- [SSH 教程](https://wangdoc.com/ssh/)

## 基础

- 单引号中的任何内容都会被字面意义地保留。
- 双引号中的内容会进行变量替换，并会解释某些特殊字符（如：换行符、制表符等）。
- `echo "${var:-default}"`：如果 `var` 未定义或者为空值，则使用默认值 `default`。
- `$()` 可以执行一个命令并捕获其输出。
- `kinit`。
- `java -xvf test.jar`。
- 清空文件：`> test.sh`。
- 拼接变量名和变量值：`echo 'MONTH:' "${MONTH}"`。
- `!!` 会执行上一条命令。

## 本地化环境变量

[Locale Environment Variables](https://www.baeldung.com/linux/locale-environment-variables).

## 常用命令

### `dirs`、`pushd` 和 `popd`

While the `pushd` command adds a directory on top of the stack, on the other hand, the `popd` command removes an item from the top.

```shell
# 显示目录栈
dirs
# 显示目录栈及其索引（方便和 pushd +N、popd +N 配合）
dirs -v
# 每个目录单独一行输出
dirs -p
# 清空目录栈
dirs -c
# 切换到 directory 目录，并将 directory 目录压入栈顶
pushd <directory>
# 不改变当前目录，并将 directory 目录压入栈底
pushd -n <directory>
# 回到上一次执行 pushd 命令时所在的目录，并移除栈顶元素。注意 cd - 回到的是上一次访问的目录，这与 pushd 行为不同
popd
```

### `su`

用以切换用户。

```shell
# 切到 root 用户，但不加载 root 环境，需要 root 用户密码
su
# 切到 root 用户并加载 root 环境，需要 root 用户密码
su -
# 切到 user 用户，但不加载 user 环境，需要 user 用户密码
su user
# 切到 user 用户并加载 user 环境，需要 user 用户密码
su - user
```

### `sudo`

用以临时执行。

```shell
# 以 root 用户执行命令
sudo <command>
# 以 user 用户执行命令
sudo -u user <command>
# 输入当前用户的密码切换至 root（前提是当前用户在 sudoers 里）并模拟 root 登录环境
sudo -i
# 输入当前用户的密码切换至 root（前提是当前用户在 sudoers 里）但并不加载 root 环境
sudo -s
```

### [zip](https://www.geeksforgeeks.org/linux-unix/zip-command-in-linux-with-examples/)

```shell
zip [options] archive_name.zip file1 file2 folder/
```

默认 `unzip` 会保留原压缩包本身。

```shell
unzip [file_name.zip]
```

解压之后立即删除压缩包。

```shell
unzip archive_name.zip && rm archive_name.zip
```

压缩之后删除原文件。

```shell
zip -m archive_name.zip *.txt
```

递归打包目录和其中的文件，打包时会显示目录为单独一项，解压之后会保存原有的目录结构。

```shell
zip -r archive_name.zip directory/
```

打包时排除某个文件。

```shell
zip -r archive_name.zip dir/ -x dir/test.txt
```

zip -D 有两个行为：

- 压缩文件时不会把**非空目录**单独列为一个条目，对于非空目录来说，压缩时加 `-D` 与不加解压来说没有任何影响。
- 压缩时完全忽略空目录，不会在解压时生成它们。

```shell
zip -Dr archive.zip dir/
```

直接丢弃文件路径，只保留文件名。

```shell
zip -jr archive.zip dir/
```

综上所述 `zip -Dj` 选项中的 `D` 选项完全没用，因为 `j` 选项就把所有目录剔除掉了。

### [`openssl`](https://www.geeksforgeeks.org/linux-unix/practical-uses-of-openssl-command-in-linux/)

查看版本。

```shell
openssl version
```

加密时使用明文密码。

```shell
openssl enc -aes-256-cbc -e -salt -in <inputfile> -out <outputfile> -k password
openssl enc -aes-256-cbc -e -salt -in <inputfile> -out <outputfile> -pass pass:password
```

加密时从环境变量读取密码。

```shell
export PASSWORD=password
openssl enc -aes-256-cbc -e -salt -in <inputfile> -out <outputfile> -pass env:PASSWORD
```

解密。

```shell
export PASSWORD=password
openssl enc -aes-256-cbc -d -salt -in <inputfile> -out <outputfile> -pass env:PASSWORD
```

### [`dc`](https://www.geeksforgeeks.org/linux-unix/dc-command-in-linux-with-examples/)

`dc` 的主要功能是来计算**逆波兰式**。

- `P` 的作用是弹出栈顶的值并打印它。
    - 如果栈顶是**字符串**（由 `[...]` 组成），`P` 直接按字符原样打印该字符串（不加结尾换行）。
    - 如果栈顶是**数字**，`P` 把该数字当作 base-256（即 256 进制）的表示，然后把每个字节作为 ASCII/字节值输出（同样不加结尾换行）。因此 `P` 常被用来输出原始字节/字符流。
- `p` 的作用是原样打印栈顶并保留栈内容，输出后会带换行（更适合打印人类可读的数字或字符串并换行）。

```shell
echo "5 3 + p" | dc
# 8
dc -e '50 10 * 9 + p'
# 509
dc -e '[Hello] P'
# Hello (无换行)
dc -e '[Hello] P 10 P'
# Hello (有换行)
dc -e '65 P'
# A (无换行)
dc -e '65 P 10 P'
# A (有换行)
dc -e '65 p'
# 65 (有换行)
```

### `date`

[Date format](https://www.man7.org/linux/man-pages/man1/date.1.html).

- UTC（Coordinated Universal Time，协调世界时）：全球统一的时间标准，基于原子钟和天文观测调整。
- CST 很特殊，它不是唯一指代一个时区，全球有多个地方的时区都叫 CST。
    - China Standard Time（UTC+8）
    - Central Standard Time（UTC-6 夏令时 UTC-5）
    - Cuba Standard Time（UTC-5）
    - Canada Central Standard Time（UTC-6）
- GMT（Greenwich Mean Time，格林尼治平时）：UTC 出现之前的全球标准，基于地球自转，取英国格林尼治天文台的平均太阳时，但不再是严格的国际计时标准，因为地球自转并不完全稳定。

```shell
date
# Tue Sep  2 09:54:37 CST 2025
date -u
# Tue Sep  2 01:54:37 UTC 2025

# RFC 2822 时间格式，用于互联网邮件服务
date -R
# Tue, 02 Sep 2025 09:54:37 +0800
date '+%A'
# Tuesday
date '+%B'
# September
date '+%F'
# 2025-09-02
date '+%Y-%m-%d'
# 2025-09-02
date '+%Y 年 %m 月 %d 日'
# 2025 年 09 月 02 日
date '+%Y 年 %-m 月 %-d 日'
# 2025 年 9 月 2 日
date '+%T'
# 10:10:44
date '+%H:%M:%S'
# 10:10:44

date -d '20250902 10:10:44'
# Tue Sep  2 09:54:37 CST 2025
date -d '2025-09-02 10:10:44'
# Tue Sep  2 09:54:37 CST 2025
date -d '2025/09/02 10:10:44'
# Tue Sep  2 09:54:37 CST 2025
date -d '2 Sep 2025 10:10:44'
# Tue Sep  2 09:54:37 CST 2025
date -d 'yesterday'
# Mon Sep  1 09:54:37 CST 2025
date -d 'tomorrow'
# Wed Sep  3 09:54:37 CST 2025
date -d '3 days ago'
# Sat Aug 30 09:54:37 CST 2025
date -d 'last week'
# Tue Aug 26 09:54:37 CST 2025
date -d 'next wed'
# Wed Sep  3 00:00:00 CST 2025
date -d 'last Sunday'
# Sun Aug 31 00:00:00 CST 2025
date -d '+7 day'
# Tue Sep  9 09:54:37 CST 2025
date -d '-3 year'
# Fri Sep  2 09:54:37 CST 2022
date -d '+10 week'
# Tue Nov 11 09:54:37 CST 2025
date -d '20250902 -3 days'
# Sat Aug 30 00:00:00 CST 2025
date -d '20250902 last year'
# Mon Sep  2 00:00:00 CST 2025
date -d '20250902 -3 tomorrow'
# Wed Sep  3 00:00:00 CST 2025
date -d '20250902 -3 month ago'
# Wed Jul  2 00:00:00 CST 2025

# 使用 root 用户设置本地时间
date -s '2025-09-02 09:54:37'

# -d 选项和 + 一起使用
date -d '20250902' '+%F'
# 2025-09-02
date -d '20250902' '+%Y 年 %m 月 %d 日'
# 2025 年 09 月 02 日
```

### `du` 和 `df`

`du`（Disk Usage）：统计文件或目录实际占用的磁盘空间，统计时是逐个文件累加统计的。

- **稀疏文件**是一种特殊类型的文件，它只存储实际包含数据的部分，而不分配存储空间给全零的空洞部分，操作系统会记录文件中哪些部分是空洞，并在读取时动态返回零值。
- `du` 看的是已分配的块。对于稀疏文件来说 `du` 和 `ls` 统计出来的磁盘空间会差很多。
- 文件被进程占用时，此时删除文件但空间没释放。那么 `du` 看不到，`df` 会看到。

```shell
# 不加选项会遍历 testDir 目录，列出来其中每一个目录以及其子目录所占用磁盘的大小，单位是 KB。
du testDir
# -h（human-readable）：以人类可读方式显示。
du -h testDir
# -s（summary）：只显示总大小，不变遍历子目录。
du -sh testDir
# -a：显示所有文件（不只是目录）。
du -ah testDir
# --max-depth=N：限制遍历目录层级深度。
du -h --max-depth=1 testDir
# 显示总计。
du -h --max-depth=1 testDir -c
```

`df`（Disk Free）：看磁盘或文件系统的整体空间。统计已用、可用和总容量等，适合用来判断磁盘是否满了。

- Inode（Index Node）是 Unix/Linux 文件系统中用于描述文件和目录的元数据的数据结构。它存储了文件的所有属性信息，但不包含文件名和文件内容本身。
- `df` 统计的是整个文件系统，包含已删除但仍被进程占用的文件和文件系统保留空间（如 ext4 为 root 保留 5%）。

```shell
# -h（human-readable）：以人类可读方式显示。
df -h
# -T：显示文件系统类型。
df -Th
# -i：查看 inode 使用情况。
df -ih
# 指定路径：查看某路径所在的文件系统。
df -h testDir
```

常见使用方式如下：

```shell
# 统计当前目录下所有目录的占用空间大小，并以人类可读的方式从大到小排列（不包含隐藏文件）。
du -sh * | sort -rh
# 统计 .snapshot 目录以及其子目录占用空间大小，并以人类可读的方式从大到小排列。
du -h --max-depth=1 .snapshot | sort -rh
```

### `sed` 命令

`sed` 是 Stream Editor（流编辑器）的缩写。它是 Linux 系统中非常强大的文本处理工具，通常用于对文件进行查找、替换、删除或插入操作。`sed` 不需要打开文件交互，而是通过命令行通过模式匹配直接处理文本流。`sed` 采用的是“行处理”模式，逐行执行指定的脚本命令，并将处理后的结果输出。

`sed` 命令有两个工作空间：模式空间（Pattern Space）和暂存空间（Hold Space）。

- 模式空间是 `sed` 的默认工作区域。
    - `sed` 读取文件的一行，去掉换行符，将其放入模式空间，然后对其执行脚本中的命令。
    - 模式空间是临时的。每当处理完一行并输出后，模式空间就会被清空，读入下一行。
    - 主要用于主文本的匹配、替换和修改。
- 暂存空间是一个额外的辅助缓冲区，用于在处理行之间保存数据。
    - 暂存空间是持久的。除非你显式地清空或覆盖它，否则它的内容在处理整个文件期间都会保留。
    - 主要用于存储特定的行，以便稍后将其拉回到模式空间进行对比、合并或重新排序。

要让这两个空间协作，你需要使用特定的命令来移动数据。

- `h`：完整写法为 `hold`。作用是 Pattern -> Hold，效果是覆盖：用模式空间内容覆盖暂存空间。
- `H`：完整写法为 `Hold`。作用是 Pattern -> Hold，效果是追加：将模式空间内容追加到暂存空间。
- `g`：完整写法为 `get`。作用是 Hold -> Pattern，效果是覆盖：用暂存空间内容覆盖模式空间。
- `G`：完整写法为 `Get`。作用是 Hold -> Pattern，效果是追加：将暂存空间内容追加到模式空间。
- `x`：完整写法为 `exchange`。作用是 Pattern <-> Hold，效果是交换：互换两个空间的内容。

基本用法：

```shell
sed [选项] '命令' 文件名
```

常用选项：

- 无选项时可以预览数据，`sed` 会将内容输出到终端。
- `-i`：直接修改文件内容。
- `-n`：取消默认输出，仅打印经过命令处理过的行（常与 `p` 命令配合）。
- `-e`：指定多个编辑命令。
- `-f`: 从文件中读取命令。
- `-r`：支持扩展正则表达式。

核心功能示例：

- 文本替换。
    - 基本替换（只替换每行第一个匹配项）：`sed 's/apple/orange/' test.txt`。
    - 全局替换（替换每行所有匹配项）：`sed 's/apple/orange/g' test.txt`。
    - 只替换特定行（只替换第 2 行的第一个匹配项）：`sed '2s/apple/orange/' test.txt`。
    - 替换范围内的行。
        - 替换 1~3 行的第一个匹配项：`sed '1,3s/apple/orange/' test.txt`。
        - 替换第 2 行到最后一行的第一个匹配项：`sed '2,$/apple/orange/' test.txt`。
    - 只替换每行第 n（此处为 2）个出现的匹配项：`sed 's/apple/orange/2' test.txt`。
    - 从每行的第 n（此处为 3）个匹配项开始，替换掉后面所有的匹配项：`sed 's/apple/orange/3g' test.txt`。
    - `echo "Welcome To The Geek Stuff" | sed 's/\(\b[A-Z]\)/\(\1\)/g'`：`(W)elcome (T)o (T)he (G)eek (S)tuff`。
    - 使用正则表达式进行替换：`sed -r 's/\ba\w+/orange/g' test.txt`。
- 插入与附加。
    - 在第 1 行之前插入一行：`sed '1i\Hello World' test.txt`。
    - 在最后一行之后追加一行：`sed '$a\The End' test.txt`。
- 删除行。
    - 删除第 2 行：`sed '2d' test.txt`。
    - 删除范围内（3-6）所有行：`sed '3,6d' test.txt`。
    - 删除最后一行：`sed '$d' test.txt`。
    - 删除包含 `error` 的所有行：`sed '/error/d' test.txt`。
- 打印与提取。
    - 仅显示第 5 到第 10 行：`sed -n '5,10p' test.txt`。
    - 显示包含 Linux 的行：`sed -n '/Linux/p' test.txt`。
    - `sed 's/apple/orange/p' test.txt`，由于 `sed` 默认就会打印处理后的每一行，加上 `/p` 标志后：
        - 如果行内匹配到了 `apple`，`sed` 执行替换，因为默认输出，打印一次修改后的行。因为末尾有 `p`，再打印一次修改后的行，结果会导致这一行在屏幕上出现了两次。
        - 如果行内没有 `apple`，`sed` 不执行替换，因为默认输出，打印一次原行。因为没发生替换，`p` 不起作用。结果为这一行在屏幕上正常出现一次。
    - 只打印被替换的行：`sed -n 's/apple/orange/p' test.txt`。此时如果使用 `-n` 选项但不使用 `p` 命令，那么命令行将不会有任何输出。

在对重要配置文件使用 `sed -i` 之前，可以先用 `sed -i.bak`。这样它会在修改文件的同时，自动创建一个名为 `文件名.bak` 的备份：`sed -i.bak '1i\Hello World' test.txt`。
