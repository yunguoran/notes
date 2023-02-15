# Git

## Elementary Knowledge

- [Pro Git](https://git-scm.com/book/zh/v2).
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN).

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
