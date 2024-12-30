# Hadoop

## HDFS（Hadoop Distributed File System）

- NameNode：存储文件的**元数据**，如文件名、文件目录结构、文件属性，以及每个文件的**块列表**和**块所在的 DataNode**。
- DataNode：在本地文件系统**存储文件块数据**，以及**块数据的校验和**。
- Secondary NameNode：**每隔一段时间对 NameNode 元数据进行备份**。

## Yarn（Yet Another Resource Negotiator）

- ResourceManager：掌控整个集群的资源。
- NodeManager：掌控单个节点的资源。
- ApplicationMaster：掌控单个任务的资源。
- Container：相当于一台独立的服务器，封装了任务运行所需要的资源。

## MapReduce

- Map 阶段并行处理输入数据。
- Reduce 阶段对 Map 结果进行汇总。

##

## Shell

```shell
# 切换到 root 用户
su root

# 添加用户 yunguoran
useradd yunguoran

# 更改文件拥有者
chown yunguoran:yunguoran software/
```

## 关键位置

```text
# IP 配置
/etc/sysconfig/network-scripts/ifcfg-ens33

# 主机名称
/etc/hostname

# 主机映射
/ect/hosts
```
