# Security

- [CVE Details](https://www.cvedetails.com/)
- [RCE](https://en.wikipedia.org/wiki/Arbitrary_code_execution)

## 跨站请求伪造

跨站请求伪造（CSRF，Cross-Site Request Forgery）是一种常见的 Web 攻击方式。它的核心思想是攻击者诱导用户在已登录的情况下，去访问攻击者构造的恶意请求，从而冒充用户执行敏感操作。

### 样例

假设有一个银行网站 <https://bank.com>，用户在上面登录了账户，浏览器保存了登录 Cookie。
银行转账的接口是：

```nginx
POST https://bank.com/transfer
参数：to=收款人账号&amount=转账金额
```

正常情况下，用户在银行页面填写表单并提交，服务器会根据用户的 Cookie 判断这是“你本人在操作”，于是执行转账。

攻击者的操作：

- 攻击者知道这个转账接口的规则。
- 攻击者伪造一个网页，比如：

    ```html
    <html>
    <body>
        <h1>点这里领取奖品！</h1>
        <form action="https://bank.com/transfer" method="POST">
        <input type="hidden" name="to" value="attacker_account">
        <input type="hidden" name="amount" value="1000">
        <input type="submit" value="领取奖品">
        </form>
    </body>
    </html>
    ```

- 用户在已登录银行网站的情况下，点击了攻击者的页面按钮。
- 浏览器提交表单时，会自动带上用户在 bank.com 的 Cookie。
- 银行服务器收到请求后，以为真的是用户在操作，于是把钱转到了攻击者账号。

## 窥探历史记录攻击

这种攻击的核心原理是：**浏览器会对访问过的链接（`<a>` 标签）应用不同的样式**。

最关键的差异在于 `:visited` 这个 CSS 伪类。某些网页点过的链接会变成另一种颜色（通常是紫色），这就是 `:visited` 样式在起作用。攻击者无法直接读取你的历史记录列表，但他们可以“试探”你的浏览器。

一个简化的攻击步骤如下：

- 布下陷阱：攻击者创建一个网页，上面有大量他们想探测的网站链接（比如，一个新闻网站、一个银行网站、一个医疗咨询网站等）。
- 样式差异：他们通过 CSS 为“已访问过”的链接（`a:visited`）和“未访问过”的链接（`a:link`）设置明显不同的样式，比如不同的宽度、背景图片、字体等。早期的攻击甚至可以直接通过 JavaScript 读取链接的颜色。
- 进行探测：当你访问这个恶意网页时，你的浏览器会自动根据你的历史记录，为这些链接应用正确的样式（哪些是 `a:visited`，哪些不是）。
- 检测差异：攻击者通过 JavaScript（例如，测量元素的宽度、偏移量或检查是否加载了某个背景图片）来检测哪些链接应用了“已访问”的样式。
- 得出结论：通过检测到的样式差异，攻击者就能知道“哦，这个用户访问过 A 银行、B 医疗网站和 C 新闻网站”。
