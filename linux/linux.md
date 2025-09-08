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

## Basic

- 单引号中的任何内容都会被字面意义地保留。
- 双引号中的内容会进行变量替换，并会解释某些特殊字符（如：换行符、制表符等）。
- `echo "${var:-default}"`：如果 var 未定义或者为空值，则使用默认值 default。
- `$()` 可以执行一个命令并捕获其输出。
- `kinit`
- `java -xvf test.jar`
- 清空文件：`> test.sh`。
- 拼接变量名和变量值：`echo 'MONTH:' "${MONTH}"`。

## Summaries

[Locale Environment Variables](https://www.baeldung.com/linux/locale-environment-variables)

## Command

### su

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

### sudo

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

### [openssl](https://www.geeksforgeeks.org/linux-unix/practical-uses-of-openssl-command-in-linux/)

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

### [dc](https://www.geeksforgeeks.org/linux-unix/dc-command-in-linux-with-examples/)

`dc` 的主要功能是来计算**逆波兰式**。

- `P` 的作用是弹出栈顶的值并打印它。
    - 如果栈顶是 字符串（由 [...] 组成），P 直接按字符原样打印该字符串（不加结尾换行）。
    - 如果栈顶是 数字，P 把该数字当作 base-256（即 256 进制）的表示，然后把每个“字节”作为 ASCII/字节值输出（同样不加结尾换行）。因此 P 常被用来输出原始字节/字符流。
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

### date

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
date +'%A'
# Tuesday
date +'%B'
# September
date '+%F'
# 2025-09-02
date '+%Y-%m-%d'
# 2025-09-02
date +'%T'
# 10:10:44
date +'%H:%M:%S'
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
date -d '20250902' +'%F'
```
