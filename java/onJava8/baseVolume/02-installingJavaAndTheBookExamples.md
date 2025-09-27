# 安装 Java 和本书用例

## Gradle 基础任务

```shell
# 编译本书中的所有 Java 文件，除了部分错误示范的
gradlew compileJava

# 编译并执行 Java 文件（某些文件是库组件）
gradlew run

# 执行所有的单元测试
gradlew test

# 编译并运行一个具体的示例程序，示例：gradlew objects:HelloDate
gradlew <本书章节>:<示例名称>
```
