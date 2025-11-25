# Hive

## Commands

Commands 是可以在 HiveQL 脚本、CLI 或者 Beeline 中直接使用的非 SQL 语句。

- `quit` 和 `exit`：用来退出交互式 Shell。
- `reset`：使用 `set` 和 `-hiveconf` 参数设置的任何配置都将重置为默认值。
- `set`：显示当前 Hive 会话中实际生效的配置参数。
- `set <key>`：查看单个参数的值。
- `set -v`：查看所有参数。
- `set <key>=<value>`：设置参数。
- 添加、列出或删除分布式缓存中的 jar 包（JAR）、文件（FILE）、或者归档文件（ARCHIVE）。
    - `add`。
    - `list`。
    - `delete`。
- `!`：可以在 Hive Shell 中执行 Linux 命令。
- `dfs`：可以在 Hive Shell 中执行 `dfs` 命令。
- `source <file>`：可以在 Hive Shell 中执行脚本文件。
- `show processlist`：显示当前在 HiveServer2 上运行的操作信息。

## HiveServer2（HS2）

HiveServer2 是一种使客户端能够对 Hive 执行查询的服务，且支持多客户端并发和身份认证。

HiveServer2 是一个单进程的复合服务，包括：基于 Thrift 的 Hive 服务和 Jetty Web UI 服务。

### HS2 Architecture

基于 [Thrift](https://thrift.apache.org/) 的 Hive 服务是 HS2 的核心，负责为 Hive 查询提供服务（例如来自 Beeline 的查询）。Thrift 是一个用于构建跨平台服务的 RPC 框架。
