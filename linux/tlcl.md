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
- Even if we have no terminal emulator running, several terminal sessions continue to run behind the graphical desktop. Called virtual terminals or virtual consoles, these sessions can be accessed on most Linux distributions by pressing Ctrl- Alt-F1 through Ctrl-Alt-F6 on most systems. When a session is accessed, it presents a login prompt into which we can enter our user name and password. To switch from one virtual console to another, press Alt and F1-F6. To return to the graphical desktop, press Alt-F7.

```shell
date
cal
df
free
exit
```

- pwd - Print name of current working directory
- cd - Change directory
- ls - List directory contents
