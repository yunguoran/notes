# SSH

## 本地生成 SSH key

```shell
ssh-keygen -t rsa -b 4096 -C 'yunguoran@gmail.com'
```

## 新增其他 SSH key

### 生成新的 SSH Key

```shell
# -f 指定生成文件名，生成的公钥文件为：~/.ssh/id_rsa_work.pub
ssh-keygen -t rsa -b 4096 -C 'yunguoran@xxx.com' -f ~/.ssh/id_rsa_work
```

### 配置 SSH config 文件

```text
# 默认个人 GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

# 公司 Git 服务器
Host company-git
    HostName 192.168.x.x
    User git
    IdentityFile ~/.ssh/id_rsa_work
```

## 测试 SSH 连通性

- 测试使用 SSH 协议连接到 github.com，使用 git 这个用户名进行认证，且不需要一个交互式的 shell，只要测试认证是否成功。
- `-v` 选项会显示详细连接过程，比如这里指出服务器 coding.xxx.com 的 443 端口上运行的是 Web 服务（nginx），根本不是 Git 的 SSH 服务，因此只能使用 HTTPS 协议来访问 Git 仓库。

```shell
ssh -T git@github.com
# Hi yunguoran! You've successfully authenticated, but GitHub does not provide shell access.
ssh -vT git@coding.xxx.com
# $ ssh -vT git@coding.xxx.com
# OpenSSH_9.9p1, OpenSSL 3.2.4 11 Feb 2025
# debug1: Reading configuration data /c/Users/123456/.ssh/config
# debug1: /c/Users/123456/.ssh/config line 7: Applying options for coding.xxx.com
# debug1: Reading configuration data /etc/ssh/ssh_config
# debug1: Connecting to coding.xxx.com [192.168.x.x] port 443.
# debug1: Connection established.
# debug1: identity file /c/Users/123456/.ssh/id_rsa_work type 0
# debug1: identity file /c/Users/123456/.ssh/id_rsa_work-cert type -1
# debug1: Local version string SSH-2.0-OpenSSH_9.9
# debug1: kex_exchange_identification: banner line 0: HTTP/1.1 400 Bad Request
# debug1: kex_exchange_identification: banner line 1: Server: nginx
# debug1: kex_exchange_identification: banner line 2: Date: Thu, 28 Aug 2025 08:58:13 GMT
# debug1: kex_exchange_identification: banner line 3: Content-Type: text/html; charset=utf-8
# debug1: kex_exchange_identification: banner line 4: Content-Length: 166
# debug1: kex_exchange_identification: banner line 5: Connection: close
# debug1: kex_exchange_identification: banner line 6:
# debug1: kex_exchange_identification: banner line 7: <html>
# debug1: kex_exchange_identification: banner line 8: <head><title>400 Bad Request</title></head>
# debug1: kex_exchange_identification: banner line 9: <body bgcolor="white">
# debug1: kex_exchange_identification: banner line 10: <center><h1>400 Bad Request</h1></center>
# debug1: kex_exchange_identification: banner line 11: <hr><center>nginx</center>
# debug1: kex_exchange_identification: banner line 12: </body>
# debug1: kex_exchange_identification: banner line 13: </html>
# kex_exchange_identification: Connection closed by remote host
# Connection closed by 192.168.x.x port 443
```

在 PowerShell 中执行直观的 telnet。

```powershell
Test-NetConnection -ComputerName github.com -Port 443
```

若 SSH 22 端口被封则可配置 SSH over HTTPS，使用 HTTPS 的 443 端口。

```shell
vim ~/.ssh/config

# 填写以下内容
Host github.com
    Hostname ssh.github.com
    User git
    Port 443
    IdentityFile ~/.ssh/id_rsa
```
