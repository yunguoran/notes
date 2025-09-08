# TLCL

The Linux Command Line, click [here](http://billie66.github.io/TLCL/book/chap01.html) to see the the original, click [here](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download) to download the PDF file.

## Introduction

The only way to really get anything done on a computer is by typing on a keyboard.

## What is the Shell?

- The name `bash` is an acronym for `Bourne Again SHell`
- If the last character of the prompt is a pound sign (“#”) rather than a dollar sign, the terminal session has superuser privileges
- Press the up-arrow key, This is called command history
- If you highlight some text by holding down the left mouse button and dragging the mouse over it (or double clicking on a word), it is copied into a buffer maintained by X. Pressing the middle mouse button will cause the text to be pasted at the cursor location
- Don’t be tempted to use Ctrl-c and Ctrl-v to perform copy and paste inside a terminal window. They don’t work. These control codes have different meanings to the shell and were assigned many years before Microsoft Windows
- Even if we have no terminal emulator running, several terminal sessions continue to run behind the graphical desktop. Called virtual terminals or virtual consoles, these sessions can be accessed on most Linux distributions by pressing Ctrl + Alt + F1 through Ctrl + Alt + F6 on most systems. When a session is accessed, it presents a login prompt into which we can enter our user name and password. To switch from one virtual console to another, press Alt and F1-F6. To return to the graphical desktop, press Alt + F7

```shell
date
cal
# View remaining disk space
df
# View remaining memory
free
# End Terminal Session
exit
```

- `pwd`(print working directory) - Print name of current working directory
- `cd` - Change directory
    - `cd` - Changes the working directory to your home directory
    - `cd -` - Changes the working directory to the previous working directory
    - `cd ~user_name` Changes the working directory to the home directory of user_name. For example, cd ~bob will change the directory to the home directory of user “bob.”
- `ls` - List directory contents
    - In general, if you do not specify a pathname to something, the working directory will be assumed

Important Facts About Filenames

- Filenames that begin with a period character are hidden. This only means that ls will not list them unless you say ls -a
- Filenames and commands in Linux, like Unix, are case sensitive
- Linux has no concept of a “file extension” like some other operating systems
- Though Linux supports long filenames which may contain embedded spaces and punctuation characters, limit the punctuation characters in the names of files you create to period, dash, and underscore. Most importantly, do not embed spaces in filenames. If you want to represent spaces between words in a filename, use underscore characters

## Exploring the System

- ls – List directory contents
    - Besides the current working directory, we can specify the directory to list, like so: `ls /usr`
    - Or even specify multiple directories: `ls ~ /usr`
    - The `t` option to sort the result by the file’s modification time
    - The `ls` command has a way to reveal this information. It is invoked with the `-i` option: `ls -li`

    | Option | Long Option| Description
    | ---- | ---- | ----
    | -a | --all | List all files, even those with names that begin with a period, which are normally not listed(ie.,hidden).
    | -d | --directory | Ordinarily, if a directory is specified, ls will list the contents of the directory, not the directory itself. Use this option in conjunction with the -l option to see details about the directory rather than its contents.
    | -F | --classify | This option will append an indicator character to the end of each listed name. For example, a '/' if the name is a directory.
    | -h | --human-readable | In long format listings, display file sizes in human readable format rather than in bytes.
    | -l | | Display results in long format.
    | -r | --reverse | Display the results in reverse order. Normally, ls display its results in ascending alphabetical order.
    | -S | | Sort results by file size.
    | -t | | Sort by modification time.

- file – Determine file type
- less – View file contents

| Command | Action
| ----- | -----
| Page UP or b | Scroll back one page
| Page Down or space | Scroll forward one page
| UP Arrow | Scroll Up one line
| Down Arrow | Scroll Down one line
| G | Move to the end of the text file
| 1G or g | Move to the beginning of the text file
| /characters | Search forward for the next occurrence of characters
| n | Search forward for the next occurrence of the previous search
| h | Display help screen
| q | Quit less

## 操作文件和目录

### 通配符

| 通配符 | 意义
| ---- | ----
| * | 匹配任意多个字符（包括零个或一个）
| ? | 匹配任意一个字符（不包括零个）
| [characters] | 匹配任意一个属于字符集（characters）中的字符
| [!characters] | 匹配任意一个不是字符集中的字符
| [[:class:]] | 匹配任意一个属于指定字符类中的字符

| 字符类 | 意义
| ---- | ----
| [:alnum:] | 匹配任意一个字母或数字
| [:alpha:] | 匹配任意一个字母
| [:digit:] | 匹配任意一个数字
| [:lower:] | 匹配任意一个小写字母
| [:upper:] | 匹配任意一个大写字母

接受文件名作为参数的任何命令，都可以使用通配符。

- cp – 复制文件和目录
    - `cp item1 item2`：复制单个文件或目录 item1 到文件或目录 item2。
    - `cp item... directory`：复制多个项目（文件或目录）到一个目录下。
    - `cp -u *.html destination`：拷贝一个目录下的 HTML 文件到目标目录，同时保证只拷贝目标目录不存在或者版本比目标目录的文件更新的文件。

    | Option | Meaning
    | ---- | ----
    | -a, --archive | 复制文件和目录，以及它们的属性，包括拥有者和所有权。 通常情况下，文件拷贝具有执行拷贝操作的用户的默认属性。
    | -i, --interactive | 在覆盖已存在文件之前，提示用户确认。如果这个选项不指定， cp 命令会默认覆盖文件。
    | -r, --recursive | 递归地复制目录及目录中的内容。当复制目录时， 需要这个选项（或者 -a 选项）。
    | -u, --update | 当把文件从一个目录复制到另一个目录时，仅复制 目标目录中不存在的文件，或者是文件内容新于目标目录中已经存在文件的内容的文件。
    | -v, --verbose | 显示翔实的命令操作信息。

    | Command | Results
    | ---- | ----
    | cp file1 file2 | 复制文件 file1 内容到文件 file2。如果 file2 已经存在， file2 的内容会被 file1 的内容覆盖。如果 file2 不存在，则会创建 file2。
    | cp -i file1 file2 | 这条命令和上面的命令一样，除了如果文件 file2 存在的话，在文件 file2 被覆盖之前， 会提示用户确认信息。
    | cp file1 file2 dir1 | 复制文件 file1 和文件 file2 到目录 dir1。目录 dir1 必须存在。
    | cp dir1/* dir2 | 使用一个通配符，在目录 dir1 中的所有文件都被复制到目录 dir2 中。 dir2 必须已经存在。
    | cp -r dir1 dir2 | 复制目录 dir1 中的内容到目录 dir2。如果目录 dir2 不存在， 创建目录 dir2，操作完成后，目录 dir2 中的内容和 dir1 中的一样。 如果目录 dir2 存在，则目录 dir1 (和目录中的内容)将会被复制到 dir2 中。

- mv – 执行文件移动和文件命名任务
    - `mv item1 item2`
    - `mv item... directory`
    - `mv` 与 `cp` 共享了很多一样的选项：`-i`、`-u`、`-v`。
- mkdir – 创建目录。
    - 例如: `mkdir directory...`
    - 注意: 在描述一个命令时（如上所示），当有三个圆点跟在一个命令的参数后面，这意味着那个参数可以跟多个。
    - `mkdir dir1 dir2 dir3` 会创建三个目录，名为 dir1, dir2, dir3。
- rm – 删除文件和目录
    - 例如: `rm item...`
    - 当你使用带有通配符的 `rm` 命令时（除了仔细检查输入的内容外）， 先用 `ls` 命令来测试通配符。这会让你看到将要被删除的文件是什么。然后按下上箭头按键，重新调用刚刚执行的命令，用 `rm` 替换 `ls。`

    | Option | Meaning
    | ---- | ----
    | -i, --interactive | 在删除已存在的文件前，提示用户确认信息。 如果不指定这个选项，rm 会默默地删除文件
    | -r, --recursive | 递归地删除文件，这意味着，如果要删除一个目录，而此目录 又包含子目录，那么子目录也会被删除。要删除一个目录，必须指定这个选项。
    | -f, --force | 忽视不存在的文件，不显示提示信息。这选项覆盖了 `--interactive` 选项。
    | -v, --verbose | 在执行 `rm` 命令时，显示翔实的操作信息。

- ln – 创建硬链接或者符号链接（软链接）。
    - `ln file link`：创建硬链接。
    - `ln -s item link`：创建符号链接。

- 硬链接
    - 相当于给文件多起了个名字，通过两个名字都能找到这个文件（磁盘上只有一个文件）。
    - 硬链接文件和源文件拥有相同的 inode 号，使用 `ls -i` 命令来确认。
    - 硬链接与原始文件完全平等。系统无法区分哪个名字是先创建的，哪个是后创建的。删除任何一个名字，只要还有至少一个硬链接存在，该 inode 和数据块就不会被释放。
    - 一个硬链接不能关联它所在文件系统之外的文件。这是说一个链接不能关联与链接本身不在同一个磁盘分区上的文件。因为 inode 号仅在同一个文件系统内是唯一的。
    - 硬链接不能关联一个目录。
    - 性能开销极低。
- 符号链接
    - 符号链接生效是通过创建一个特殊类型的文件，这个文件包含一个关联文件或目录的文本指针（类似于 Windows 的快捷方式）。
    - 如果你往一个符号链接里面写入东西，那么相关联的文件也被写入。
    - 当你删除一个符号链接时，只有这个链接被删除，而不是文件自身。
    - 如果先于符号链接删除文件，这个链接仍然存在，但是不指向任何东西，即坏链。
    - 对于符号链接，有一点值得记住，执行的大多数文件操作是针对链接的对象，而不是链接本身。 而 `rm` 命令是个特例。当你删除链接的时候，删除链接本身，而不是链接的对象。

## 使用命令

命令可以是下面四种形式之一：

- 一个可执行程序，就像我们所看到的位于目录/usr/bin 中的文件一样。 这一类程序可以是用诸如 C 和 C++ 语言写成的程序然后编译得到的二进制文件, 也可以是由诸如 Shell，Perl，Python，Ruby 等等脚本语言写成的程序。
- 一个内建于 Shell 自身的命令。Bash 支持若干命令，内部叫做 Shell 内部命令 (builtins)。例如，`cd` 命令，就是一个 Shell 内部命令。
- 一个 Shell 函数。这些是小规模的 Shell 脚本，它们混合到环境变量中。
- 一个命令别名。我们可以定义自己的命令，建立在其它命令之上。

识别命令以及得到命令文档。

- type – 显示命令的类型。
    - `type` 命令是 Shell 内部命令，它会显示命令的类型，给出一个特定的命令名（做为参数）。
    - 例如：`type command`。
- which – 显示一个可执行程序的位置。
    - 有时候在一个操作系统中，不只安装了可执行程序的一个版本。虽然在桌面系统中这并不普遍，但在大型服务器中却很平常。为了确定所给定的执行程序的准确位置，使用 `which` 命令。
    - 例如：`which command`。
    - `which` 命令只对可执行程序有效，不包括内建命令和命令别名。
- help
    - 得到 Shell 内建命令的帮助文档。
    - 例如：`help command`。
    - 出现在命令语法说明中的方括号证的内容是可选的项目。一个竖杠字符 表示互斥选项。
    - `cd [-L|-P] [dir]` 说明 `cd` 命令可以跟一个 `-L` 选项和 `-P` 选项其中之一或者什么都不跟，`dir` 也是可选参数。
    - 许多可执行程序支持一个 `--help` 选项。例如: `mkdir --help`。
- man – 显示用户手册。
    - 许多希望被命令行使用的可执行程序，提供了一个正式的文档，叫做手册或手册页(man page)。
    - 例如：`man command`
    - 在大多数 Linux 系统中，`man` 使用 `less` 工具来显示参考手册。
    - `man` 所显示的参考手册，被分成几个章节，它们不仅仅包括用户命令，也包括系统管理员 命令、程序接口、文件格式等等。下表描绘了手册的布局：

        | 章节 | 内容
        | ---- | ----
        | 1 | 用户命令
        | 2 | 程序接口内核系统调用
        | 3 | C 库函数程序接口
        | 4 | 特殊文件，比如说设备结点和驱动程序
        | 5 | 文件格式
        | 6 | 游戏娱乐，如屏幕保护程序
        | 7 | 其他方面
        | 8 | 系统管理员命令

    - 指定章节号：`man 5 passwd`。
- apropos – 搜索全部参考手册来找到自己需要的命令。
    - 例如：`apropos floppy`。
    - `man -k floppy` 等同于 `apropos floppy`。
- info – 显示命令 info 条目。
- whatis – 显示一个命令的简洁描述。
- alias – 创建命令别名。

## 重定向

与 Unix 主题“任何东西都是一个文件”保持一致，像 ls 这样的程序实际上把他们的运行结果输送到一个叫做标准输出的特殊文件（经常用 stdout 表示），而它们的状态信息则送到另一个叫做标准错误输出的文件（stderr）。默认情况下，标准输出和标准错误输出都连接到屏幕，而不是保存到磁盘文件。除此之外，许多程序从一个叫做标准输入（stdin）的设备得到输入，默认情况下，标准输入连接到键盘。

- cat － 连接文件
- sort － 排序文本行
- uniq － 报道或省略重复行
- grep － 打印匹配行
- wc － 打印文件中换行符，字，和字节个数
- head － 输出文件第一部分
- tail - 输出文件最后一部分
- tee - 从标准输入读取数据，并同时写到标准输出和文件

### Redirecting Standard Output

To redirect standard output to another file besides the screen, we use the `>` redirection operator followed by the name of the file.

- `ls -l /usr/bin > ls-output.txt`
- `ls` program does not send its error messages to standard output. It sends its error messages to standard error
- If we ever need to actually truncate a file we can use a trick like this: `> ls-output.txt`
- Use the `>>` redirection operator to append redirected output to a file instead of overwriting the file: `ls -l /usr/bin >> ls-output.txt`

### Redirecting Standard Error

To redirect standard error we must refer to its file descriptor. A program can produce output on any of several numbered file streams. While we have referred to the first three of these file streams as standard input, output and error, the shell references them internally as file descriptors zero, one and two, respectively. The shell provides a notation for redirecting files using the file descriptor number. Since standard error is the same as file descriptor number two, we can redirect standard error with this notation: `ls -l /bin/usr 2> ls-error.txt`

- The file descriptor `2` is placed immediately before the redirection operator to perform the redirection of standard error to the file ls-error.txt.

#### Redirecting Standard Output and Standard Error to One File

There are cases in which we may wish to capture all of the output of a command to a single file. To do this, we must redirect both standard output and standard error at the same time.

- `ls -l /bin/usr > ls-output.txt 2>&1`
- The redirection of standard error must always occur after redirecting standard output or it doesn’t work
- `ls -l /bin/usr &> ls-output.txt`
- We use the single notation `&>` to redirect both standard output and standard error to the file ls-output.txt

#### Disposing of Unwanted Output

Sometimes *silence is golden* and we don’t want output from a command, we just want to throw it away. This applies particularly to error and status messages. The system provides a way to do this by redirecting output to a special file called `/dev/null`.

- `ls -l /bin/usr 2> /dev/null`

### Redirecting Standard Input

- `cat ls-output.txt`
- cat - The `cat` command reads one or more files and copies them to standard output
- You can use `cat` to display files without paging
- Say we have downloaded a large file that has been split into multiple parts and we want to join them back together. If the files were named: *movie.mpeg.001 movie.mpeg.002 … movie.mpeg.099*. we could join them back together with this command: `cat movie.mpeg.0* > movie.mpeg`
- Type a `Ctrl + d` to tell `cat` that it has reached end of file (EOF) on standard input
- Type `cat > lazy_dog.txt` followed by the text we want in to place in the file. Remember to type `Ctrl + d` at the end

### Pipelines

Using the pipe operator `|` (vertical bar), the standard output of one command can be piped into the standard input of another.

- `ls -l /usr/bin | less`
- `less` command accepts standard input

#### Filters

Pipelines are often used to perform complex operations on data. It is possible to put several commands together into a pipeline. Frequently, the commands used this way are referred to as filters.

- `ls /bin /usr/bin | sort | less`

#### uniq - Report or Omit Repeated lines

The `uniq` command is often used in conjunction with `sort`. `uniq` accepts a sorted list of data from either standard input or a single filename argument and, by default, removes any duplicates from the list.

- `ls /bin /usr/bin | sort | uniq | less`
- If we want to see the list of duplicates instead, we add the `-d` option to uniq like so: `ls /bin /usr/bin | sort | uniq -d | less`

#### wc － Print Line, Word and Byte Counts

The `wc` (word count) command is used to display the number of lines, words, and bytes contained in files.

- `wc ls-output.txt`
- If executed without command line arguments, `wc` accepts standard input. The `-l` option limits its output to only report lines. Example: `ls /bin /usr/bin | sort | uniq | wc -l`

#### grep － Print Lines Matching a Pattern

- Find all the files in our list of programs that had the word *zip* embedded in the name: `ls /bin /usr/bin | sort | uniq | grep zip`
- `-i` which causes `grep` to ignore case when performing the search (normally searches are case sensitive) and `-v` which tells `grep` to only print lines that do not match the pattern

#### head / tail － Print First / Last Part of Files

The `head` command prints the first *ten* lines of a file and the `tail` command prints the *last* ten lines. By default, both commands print ten lines of text, but this can be adjusted with the `-n` option.

- `head -n 5 ls-output.txt`
- `tail -n 5 ls-output.txt`
- `ls /usr/bin | tail -n 5`
- `tail` has an option which allows you to view files in real-time. This is useful for watching the progress of log files as they are being written: `tail -f /var/log/messages`
- Using the `-f` option, `tail` continues to monitor the file and when new lines are appended, they immediately appear on the display. This continues until you type `Ctrl + c`.

### tee － Read from Stdin and Output to Stdout and Files

- The `tee` program reads standard input and copies it to both standard output and to one or more files.
- `ls /usr/bin | tee ls.txt | grep zip`
