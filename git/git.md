# Git

## Elementary Knowledge

- [Pro Git](https://git-scm.com/book/zh/v2).
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN).

## Common Operations

- Remote branch overrides local branch(Replace the `master` to the corresponding branch name).

```shell
git fetch --all && git reset --hard origin/master && git pull
```

- Delete some local branches like `feat-xxx`.

```shell
git branch | grep "feat" | xargs git branch -d
```

- Execute "add、commit、push" in one zsh command.

```zsh
gaa && gcn! && gpf!
```
