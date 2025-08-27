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
