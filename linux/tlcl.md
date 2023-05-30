# TLCL

## The Linux Command Line

Click [here](http://billie66.github.io/TLCL/book/chap01.html) to see the the original.

### Foreword

The only way to really get anything done on a computer is by typing on a keyboard.

### What is shell

- The name “bash” is an acronym for “Bourne Again SHell”.
- If the last character of the prompt is a pound sign (“#”) rather than a dollar sign, the terminal session has superuser privileges.
- Press the up-arrow key, This is called command history.
- If you highlight some text by holding down the left mouse button and dragging the mouse over it (or double clicking on a word), it is copied into a buffer maintained by X. Pressing the middle mouse button will cause the text to be pasted at the cursor location.
- Don’t be tempted to use Ctrl-c and Ctrl-v to perform copy and paste inside a terminal window. They don’t work. These control codes have different meanings to the shell and were assigned many years before Microsoft Windows.
- Even if we have no terminal emulator running, several terminal sessions continue to run behind the graphical desktop. Called virtual terminals or virtual consoles, these sessions can be accessed on most Linux distributions by pressing Ctrl + Alt + F1 through Ctrl + Alt + F6 on most systems. When a session is accessed, it presents a login prompt into which we can enter our user name and password. To switch from one virtual console to another, press Alt and F1-F6. To return to the graphical desktop, press Alt + F7.

```shell
date
cal
# 查看磁盘剩余空间
df
# 查看剩余内存
free
# 结束终端会话
exit
```

- `pwd`(print working directory) - Print name of current working directory
- `cd` - Change directory
    - `cd` - Changes the working directory to your home directory.
    - `cd -` - Changes the working directory to the previous working directory.
    - `cd ~user_name` Changes the working directory to the home directory of user_name. For example, cd ~bob will change the directory to the home directory of user “bob.”
- `ls` - List directory contents
    - In general, if you do not specify a pathname to something, the working directory will be assumed.

Important Facts About Filenames

- Filenames that begin with a period character are hidden. This only means that ls will not list them unless you say ls -a.
- Filenames and commands in Linux, like Unix, are case sensitive.
- Linux has no concept of a “file extension” like some other operating systems.
- Though Linux supports long filenames which may contain embedded spaces and punctuation characters, limit the punctuation characters in the names of files you create to period, dash, and underscore. Most importantly, do not embed spaces in filenames. If you want to represent spaces between words in a filename, use underscore characters.

### 探究操作系统

- ls – List directory contents
    - Besides the current working directory, we can specify the directory to list, like so: `ls /usr`.
    - Or even specify multiple directories: `ls ~ /usr`.
    - The `t` option to sort the result by the file’s modification time.
    - The `ls` command has a way to reveal this information. It is invoked with the `-i` option: `ls -li`.

    | Option | Long Option| Description
    | ---- | ---- | ---- |
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
| ----- | ----- |
| Page UP or b | Scroll back one page
| Page Down or space | Scroll forward one page
| UP Arrow | Scroll Up one line
| Down Arrow | Scrow Down one line
| G | Move to the end of the text file
| 1G or g | Move to the beginning of the text file
| /characters | Search forward for the next occurrence of characters
| n | Search forward for the next occurrence of the previous search
| h | Display help screen
| q | Quit less

## 操作文件和目录

Wildcard

| Wildcard | Meaning
| ---- | ---- |
| * | Matches any characters
| ? | Matches any single character
| [characters] | Matches any character that is a member of the set characters
| [!characters] | Matches any character that is not a member of the set characters
| [[:class:]] | Matches any character that is a member of the specified class

| Character Class | Meaning
| ---- | ---- |
| [:alnum:] | Matches any alphanumeric character
| [:alpha:] | Matches any alphabetic character
| [:digit:] | Matches any numeral
| [:lower:] | Matches any lowercase letter
| [:upper:] | Matches any uppercase letter

- cp – Copy files and directories
    - Copy all the `HTML` files from one directory to another: `cp -u *.html destination`
    - The cp command copies files or directories. It can be used two different ways: `cp item1 item2` and `cp item... directory` (copy multiple items (either files or directories) into a directory.)

    | Option | Meaning
    | ---- | ---- |
    | -a, --archive | Copy the files and directories and all of their attributes, including ownerships and permissions. Normally, copies take on the default attributes of the user performing the copy
    | -i, --interactive | Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, cp will silently overwrite files.
    | -r, --recursive | Recursively copy directories and their contents. This option (or the -a option) is required when copying directories.
    | -u, --update | When copying files from one directory to another, only copy files that either don't exist, or are newer than the existing corresponding files, in the destination directory.
    | -v, --verbose | Display informative messages as the copy is performed.

    | Command | Results
    | ---- | ---- |
    | cp file1 file2 | Copy file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created.
    | cp -i file1 file2 | Same as above, except that if file2 exists, the user is prompted before it is overwritten.
    | cp file1 file2 dir1 | Copy file1 and file2 into directory dir1. dir1 must already exist.
    | cp dir1/* dir2 | Using a wildcard, all the files in dir1 are copied into dir2. dir2 must already exist.
    | cp -r dir1 dir2 | Copy the contents of directory dir1 to directory dir2. If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1. If directory dir2 does exist, then directory dir1 (and its contents) will be copied into dir2.

- mv – Move/rename files and directories
    - mv shares many of the same options as cp.
- mkdir – Create directories
    - Example: `mkdir directory...`
    - When three periods follow an argument in the description of a command (as above), it means that the argument can be repeated
    - `mkdir dir1 dir2 dir3` would create three directories  named “dir1”, “dir2”, “dir3”.
- rm – Remove files and directories
    - Example: `rm item...`
    - Whenever you use wildcards with rm (besides carefully checking your typing!), test the wildcard first with ls. This will let you see the files that will be deleted. Then press the up arrow key to recall the command and replace the ls with rm.

    | Option | Meaning
    | ---- | ---- |
    | -i, --interactive | Before deleting an existing file, prompt the user for confirmation. If this option is not specified, rm will silently delete files.
    | -r, --recursive | Recursively delete directories. This means that if a directory being deleted has subdirectories, delete them too. To delete a directory, this option must be specified.
    | -f, --force | Ignore nonexistent files and do not prompt. This overrides the --interactive option.
    | -v, --verbose | Display informative messages as the deletion is performed.

- ln – Create hard and symbolic links
    - The ln command is used to create either hard or symbolic links. It is used in one of two ways: `ln file link` and `ln -s item link` (to create a symbolic link where “item” is either a file or a directory.)
    - Hard link
        - A hard link cannot reference a file outside its own file system. This means a link may not reference a file that is not on the same disk partition as the link itself.
        - A hard link may not reference a directory.
    - Symbolic link
        - Symbolic links were created to overcome the limitations of hard links. Symbolic links work by creating a special type of file that contains a text pointer to the referenced file or directory. In this regard, they operate in much the same way as a Windows shortcut though of course, they predate the Windows feature by many years.
        - A file pointed to by a symbolic link, and the symbolic link itself are largely indistinguishable from one another. For example, if you write some something to the symbolic link, the referenced file is also written to. However when you delete a symbolic link, only the link is deleted, not the file itself. If the file is deleted before the symbolic link, the link will continue to exist, but will point to nothing. In this case, the link is said to be broken.

Symbolic links were created to overcome the two disadvantages of hard links: hard links cannot span physical devices and hard links cannot reference directories, only files. Symbolic links are a special type of file that contains a text pointer to the target file or directory.
