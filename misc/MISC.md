# MISC

- While exporting data to CSV file, but a field which has values separated by comma, replace comma with linefeed and then double quote the value of this field can solve this issue.
- Use kdocs or markdown table instead of uploading files on gitlab.
- [Zip bomb](https://en.wikipedia.org/wiki/Zip_bomb), [reference from stack overflow: Zip Bomb detected](https://stackoverflow.com/questions/44897500/using-apache-poi-zip-bomb-detected).
- 当升级一个包时，如果依赖的包也需要升级，则也需要查看相应依赖包的 changelog，并做相应测试。
- 只有一个入口方法时，简单的叫做 run 没问题。现在增加了入口方法，第一个方法还叫 run 就不合适了。命名看上下文，尤其注意上下文是会变的，重构、新增代码都需要重新审视上下文。
