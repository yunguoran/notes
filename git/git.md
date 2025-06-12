# Git

- [Pro Git](https://git-scm.com/book/zh/v2)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN)

## 初次使用配置

```shell
git config --global user.name "Guoran Yun"
git config --global user.email yunguoran@gmail.com
git config --global core.editor vim
```

## 常用命令

```shell
# 查看所有配置以及他们所在的文件。
git config --list --show-origin
# 检查 Git 的某一项配置。
git config <key>
# 检查哪一个配置文件最后设置了该值。
git config --show-origin <key>
# 获取帮助。
git help <verb>
git <verb> --help
# -h 选项获得更简明的 help 输出。
git <verb> -h
# 输出修改之后还没有暂存起来的变化内容
git diff
# 将比对已暂存文件与最后一次提交的文件差异
git diff --staged
# Git 会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 git add 步骤
git commit -a
# 从 Git 中移除且从本地目录删除
git rm
# 从 Git 中移除但保留在本地
git rm --cached
# 显示最近的两次提交所引入的差异
git log -p -2
# 显示每次提交的简略统计信息
git log --stat
```

## 组合操作

```shell
# 远程分支覆盖本地分支。
git fetch --all && git reset --hard origin/master && git pull
# 删除本地已 merge 的分支。
git branch --merged | grep -v \* | xargs git branch -D
# 删除本地除了含有 *develop* 和 *master* 的分支。
git branch | grep -v "develop" | grep -v "master" | xargs git branch -D
# 一次性执行 *add*、*commit* 和 *push*。
gaa && gcn! && gpf
```

## 在 Git Bash 中设置 Git Alias

- save *.git-plugin-bash.sh* in your home directory(cd ~).
- to *~/.bashrc* file add line: `source ~/.git-plugin-bash.sh`.
- open new terminal (your bash have to reload).
- check if it working. Type `gst` in repository folder instead of `git status`.
