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

## Manipulating Files and Directories

Wildcard

| Wildcard | Meaning
| ---- | ----
| * | Matches any characters
| ? | Matches any single character
| [characters] | Matches any character that is a member of the set characters
| [!characters] | Matches any character that is not a member of the set characters
| [[:class:]] | Matches any character that is a member of the specified class

| Character Class | Meaning
| ---- | ----
| [:alnum:] | Matches any alphanumeric character
| [:alpha:] | Matches any alphabetic character
| [:digit:] | Matches any numeral
| [:lower:] | Matches any lowercase letter
| [:upper:] | Matches any uppercase letter

- cp – Copy files and directories
    - Copy all the `HTML` files from one directory to another: `cp -u *.html destination`
    - The cp command copies files or directories. It can be used two different ways: `cp item1 item2` and `cp item... directory` (copy multiple items (either files or directories) into a directory.)

    | Option | Meaning
    | ---- | ----
    | -a, --archive | Copy the files and directories and all of their attributes, including ownerships and permissions. Normally, copies take on the default attributes of the user performing the copy
    | -i, --interactive | Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, cp will silently overwrite files.
    | -r, --recursive | Recursively copy directories and their contents. This option (or the -a option) is required when copying directories.
    | -u, --update | When copying files from one directory to another, only copy files that either don't exist, or are newer than the existing corresponding files, in the destination directory.
    | -v, --verbose | Display informative messages as the copy is performed.

    | Command | Results
    | ---- | ----
    | cp file1 file2 | Copy file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created.
    | cp -i file1 file2 | Same as above, except that if file2 exists, the user is prompted before it is overwritten.
    | cp file1 file2 dir1 | Copy file1 and file2 into directory dir1. dir1 must already exist.
    | cp dir1/* dir2 | Using a wildcard, all the files in dir1 are copied into dir2. dir2 must already exist.
    | cp -r dir1 dir2 | Copy the contents of directory dir1 to directory dir2. If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1. If directory dir2 does exist, then directory dir1 (and its contents) will be copied into dir2.

- mv – Move/rename files and directories
    - mv shares many of the same options as cp
- mkdir – Create directories
    - Example: `mkdir directory...`
    - When three periods follow an argument in the description of a command (as above), it means that the argument can be repeated
    - `mkdir dir1 dir2 dir3` would create three directories named “dir1”, “dir2”, “dir3”
- rm – Remove files and directories
    - Example: `rm item...`
    - Whenever you use wildcards with rm (besides carefully checking your typing!), test the wildcard first with ls. This will let you see the files that will be deleted. Then press the up arrow key to recall the command and replace the `ls` with `rm`

    | Option | Meaning
    | ---- | ----
    | -i, --interactive | Before deleting an existing file, prompt the user for confirmation. If this option is not specified, rm will silently delete files.
    | -r, --recursive | Recursively delete directories. This means that if a directory being deleted has subdirectories, delete them too. To delete a directory, this option must be specified.
    | -f, --force | Ignore nonexistent files and do not prompt. This overrides the --interactive option.
    | -v, --verbose | Display informative messages as the deletion is performed.

- ln – Create hard and symbolic links
    - The ln command is used to create either hard or symbolic links. It is used in one of two ways: `ln file link` and `ln -s item link` (to create a symbolic link where “item” is either a file or a directory.)
    - Hard link
        - A hard link cannot reference a file outside its own file system. This means a link may not reference a file that is not on the same disk partition as the link itself
        - A hard link may not reference a directory
    - Symbolic link
        - Symbolic links were created to overcome the limitations of hard links. Symbolic links work by creating a special type of file that contains a text pointer to the referenced file or directory. In this regard, they operate in much the same way as a Windows shortcut though of course, they predate the Windows feature by many years
        - A file pointed to by a symbolic link, and the symbolic link itself are largely indistinguishable from one another. For example, if you write some something to the symbolic link, the referenced file is also written to. However when you delete a symbolic link, only the link is deleted, not the file itself. If the file is deleted before the symbolic link, the link will continue to exist, but will point to nothing. In this case, the link is said to be broken

Symbolic links were created to overcome the two disadvantages of hard links: hard links cannot span physical devices and hard links cannot reference directories, only files. Symbolic links are a special type of file that contains a text pointer to the target file or directory.

## Working with Commands

- type – Indicate how a command name is interpreted
    - The type command is a shell builtin that displays the kind of command the shell will execute, given a particular command name
    - It works like this: `type command`
- which – Display which executable program will be executed
    - Sometimes there is more than one version of an executable program installed on a system. While this is not very common on desktop systems, it’s not unusual on large servers
    - To determine the exact location of a given executable, the which command is used: `which command`
- help
    - `bash` has a built-in help facility available for each of the shell builtins. To use it, type `help` followed by the name of the shell builtin
    - For example: `help cd`
    - When square brackets appear in the description of a command’s syntax, they indicate optional items. A vertical bar character indicates mutually exclusive items
    - `cd [-L|-P] [dir]` says that the command `cd` may be followed optionally by either a `-L` or a `-P` and further, optionally followed by the argument `dir`
    - Many executable programs support a `--help` option that displays a description of the command’s supported syntax and options
    - For example: `mkdir --help`
- man – Display a command’s manual page
    - Most executable programs intended for command line use provide a formal piece of documentation called a manual or man page
    - It is used like this: `man command`
    - On most Linux systems, `man` uses `less` to display the manual page, so all of the familiar `less` commands work while displaying the page.
    - The manual that `man` displays is broken into sections and not only covers user commands but also system administration commands, programming interfaces, file formats and more. The table below describes the layout of the manual:

        | Section | Contents
        | ---- | ----
        | 1 | User commands
        | 2 | Programming interfaces kernel system calls
        | 3 | Programming interfaces to the C library
        | 4 | Special files such as device nodes and drivers
        | 5 | File formats
        | 6 | Games and amusements such as screen savers
        | 7 | Miscellaneous
        | 8 | System administration commands

    - To specify a section number, we use man like this: `man 5 passwd`
- apropos – Display a list of appropriate commands
    - It is also possible to search the list of `man` pages for possible matches based on a search term. It is used like this: `apropos floppy`
    - The first field in each line of output is the name of the `man` page, the second field shows the section. Note that the man command with the `-k` option performs the exact same function as `apropos`
- info – Display a command’s info entry
- whatis – Display a very brief description of a command
- alias – Create an alias for a command

Many software packages installed on your system have documentation files residing in the `/usr/share/doc` directory. Most of these are stored in plain text format and can be viewed with `less`. We may encounter some files ending with a **.gz** extension. This indicates that they have been compressed with the `gzip` compression program. The `gzip` package includes a special version of `less` called `zless` that will display the contents of gzip-compressed text files.

We will create a command of our own using the `alias` command.

- Notice the structure of this command: `alias name='string'`. Example: `alias foo='cd /usr; ls; cd -'`
- To remove an alias, the `unalias` command is used, like so: `unalias foo`
- To see all the aliases defined in the environment, use the `alias` command without arguments

## Redirection

- cat - Concatenate files
- sort - Sort lines of text
- uniq - Report or omit repeated lines
- grep - Print lines matching a pattern
- wc - Print newline, word, and byte counts for each file
- head - Output the first part of a file
- tail - Output the last part of a file
- tee - Read from standard input and write to standard output and files

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
