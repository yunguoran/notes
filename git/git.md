# Git

- [Pro Git](https://git-scm.com/book/zh/v2)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN)

## 初次使用配置

```shell
# 此处使用双引号的原因
#   - 名字中间有空格
#   - 在 Windows CMD 命令行下单引号不会被识别为字符串界定符，而是把单引号当作字符串的一部分传过去。
#   - 如果是 Linux 系统或在 Windows 下用的是 Git Bash，则可以使用单引号。
git config --global user.name "Guoran Yun"
git config --global user.email yunguoran@gmail.com
git config --global core.editor vim
# 使用 HTTPS 协议时长期存储账号密码（磁盘上明文存储）
git config --global credential.helper store
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
# 一行展示每个提交
git log --oneline
# 显示最近的两次提交所引入的差异
git log -p -2
# 显示每次提交的简略统计信息
git log --stat
# 切换远程地址
git remote set-url origin https://github.com/yunguoran/notes.git
```

### git stash show

```shell
# 看概要（文件级别统计）
git stash show
# 查看指定 stash
git stash show stash@{n}
# 看详细改动（行级 diff）
git stash show -p stash@{n}
# 只显示文件名
git stash show stash@{n} --name-only
# 删除指定 stash
git stash drop stash@{n}
# 清空所有 stash
git stash clear
```

### 撤销本地 commit

```shell
# 单纯撤销 commit，但保留代码修改
git reset --soft HEAD^
# 撤销 commit，代码回到 unstaged 状态
git reset --mixed HEAD^
# 撤销 commit 并 彻底丢掉代码修改。
git reset --hard HEAD^
```

### 撤销已 push 的 commit

```shell
# 本地执行再 push
git revert --no-edit <commitID>
```

### [合并 commit](https://www.baeldung.com/ops/git-squash-commits)

Squashing commits helps keep our Git history clean and easy to understand.

#### 使用 git reset

该种方式适用开发者在个人分支上使用。

```shell
git reset --soft c497509
git add .
git commit -m "commit message"
git push -f
```

#### 使用 git rebase -i

该种方式适用开发者在个人分支上使用，且控制的颗粒度比 `git reset` 更加精细。

```shell
git rebase -i c497509
# 在 interactive rebase 中将除第一个 commit 外的其他 commit 的前缀改为 squash。
git push -f
```

#### 使用 git merge --squash

该种方式会 squash 整个分支的提交历史，而不是只 squash 最近几个提交。

```shell
git checkout main
git merge --squash feat-update-git
git add .
git commit -m "commit message"
git push -f
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
