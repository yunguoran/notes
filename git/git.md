# Git

- [Pro Git](https://git-scm.com/book/zh/v2)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN)

## 在 Git Bash 中设置 Git Alias

- save *.git-plugin-bash.sh* in your home directory(cd ~).
- to *~/.bashrc* file add line: `source ~/.git-plugin-bash.sh`.
- open new terminal (your bash have to reload).
- check if it working. Type `gst` in repository folder instead of `git status`.

## Common Operations

- 远程分支覆盖本地分支。

    ```shell
    git fetch --all && git reset --hard origin/master && git pull
    ```

- 删除本地已 merge 的分支。

    ```shell
    git branch --merged | grep -v \* | xargs git branch -D
    ```

- 删除本地除了含有 *develop* 和 *master* 的分支。

    ```shell
    git branch | grep -v "develop" | grep -v "master" | xargs git branch -D
    ```

- 一次性执行 *add*、*commit* 和 *push*。

    ```zsh
    gaa && gcn! && gpf
    ```
