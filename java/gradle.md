# Gradle

- **GRADLE_USER_HOME** 类似于 Maven 的本地仓库。
- `gradle -v` 检测安装是否成功。

## 入门

### 目录结构

- build：封装编译后的字节码、Jar、War、测试报告等信息。
- src
    - main
        - java
        - resources
        - webapp (仅 War 包会生成)
            - WEB-INF
                - web.xml
            - index.jsp
    - test
        - java
        - resources
- build.gradle：构建脚本，类似于 Maven 的 pom.xml
- setting.gradle：设置文件，定义项目及子项目名称信息，和项目是一一对应的关系。

### 创建一个 Gradle 项目

- `gradle init`
- [Cloud Native App Initializer](https://start.aliyun.com/)

### 常用命令

gradle 的指令要在含有 build.gradle 的目录执行。

- `gradle clean`：清空 build 目录
- `gradle classes`：编译业务代码和配置文件（src/main 目录下的所有文件）
- `gradle test`：编译测试代码，生成测试报告（src/test 目录下的所有文件）
- `gradle build`：构建项目（编译、测试、打包、部署）
- `gradle build -x test`：跳过编译测试代码的步骤

### Gradle 下载源换成国内

```groovy
allprojects {
    repositories {
        mavenLocal()
        maven { name "Alibaba" ; url "https://maven.aliyun.com/repository/public" }
        maven { name "Bstek" ; url "https://nexus.bsdn.org/content/groups/public/" }
        mavenCentral()
    }

    buildscript {
        repositories {
            maven { name "Alibaba" ; url 'https://maven.aliyun.com/repository/public' }
            maven { name "Bstek" ; url 'https://nexus.bsdn.org/content/groups/public/' }
            maven { name "M2" ; url 'https://plugins.gradle.org/m2/' }
        }
    }
}
```

### Wrapper 包装器

- Gradle Wrapper 实际上就是对 Gradle 的一层包装，用于解决实际开发中可能会遇到的不同的项目需要不同版本的 Gradle。
- 有了 Gradle Wrapper 之后，本地是可以不配置 Gradle 的，下载 Gradle 项目后，使用 Gradle 项目自带的 wrapper 操作也可以。
- `gradle` 指令和 `gradlew` 指令所使用的 Gradle 版本有可能是不一样的。
- `gradle wrapper --gradle-version=8.9`：升级 wrapper 版本号，只是修改 gradle.properties 中 wrapper 版本，并未实际下载。
- 当我们第一次执行 `./gradlew build` 命令的时候，Gradlew 会读取 gradle-wrapper.properties 文件的配置信息并下载。

## Gradle 与 IDEA 整合

### Groovy 基本语法

- Groovy 基于 Java 语言，因此完全兼容 Java 语言。不仅可作为面向对象编程语言，也可作为脚本语言。
- 在一个 Groovy 文件中可以混合类的定义和脚本定义。此时不能再定义一个与文件同名的类（There is a synthetic class 'xxx' generated for script code）。
- Groovy 中使用 def 定义变量、方法，不建议使用具体的数据类型。
- Groovy 注释与 Java 注释一致。
- Groovy 中语句末尾的分号可以省略，以换行作为结束。
- 默认类、方法、字段都是 public 修饰的。
- 对象的属性操作
    - 给对象属性赋值
        - 对象.属性名 = xxx
        - 对象的具名构造器（Groovy 类自带的）
    - 读取对象属性
        - 对象.属性名
        - 对象["属性名"]
        - 对象.getter 方法
    - 对象属性的操作本质是通过属性对应的 getter setter 方法完成的。
- 方法
    - 声明时参数类型和返回值类型可以省略
    - 默认使用方法最后一句的返回值作为方法返回值
    - 调用时在不引起歧义的情况下`()`可以省略
- 基本类型也是对象，可以直接调用对象的方法。
- 引号
    - 单引号：作为字符串常量使用，没有运算能力。
    - 双引号：可使用 `${var}`，有运算能力。
    - 三引号：模板字符串，支持换行。
- 变量、属性、方法、闭包的参数以及方法的返回值类型都是可有可无的，都是在给变量赋值的时候才决定它的类型。
- 当需要时，类型之间会自动发生类型转换: 字符串（String）、基本类型（如 int）和类型的包装类 (如 Integer)。
- 如果在一个 Groovy 文件中没有任何类定义，它将被当做 script 来处理，也就意味着这个文件将被透明的转换为一个 Script 类型的类，这个自动转换得到的类将使用原始的 Groovy 文件名作为类的名字。Groovy 文件的内容被打包进 run 方法，另外在新产生的类中被加入一个 main 方法以进行外部执行该脚本。
