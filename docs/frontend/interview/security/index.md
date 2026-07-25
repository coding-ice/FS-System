# Web 安全

## XSS

**其核心：永远不要相信用户输入的内容**  

场景描述：攻击人通过在输入框输入恶意代码（script/img onload），并提交(服务器上)，当其他用户浏览该页面时，恶意代码执行，从而达到攻击的目的。
现代框架 如 React/Vue 等，都默认开启了 XSS 防护，但是做 **富文本、Markdown** 等场景时，需要关闭防护。

## CSRF

在用户不知情的情况下，攻击人利用用户身份（cookie），以用户的名义发送请求，从而达到攻击的目的。  

场景描述：
1. 用户登录了银行网站 -> /transfer?amount=1000&to=1234567890
2. 攻击人诱导用户点击了恶意链接 -> 里面包含了银行网站的 transfer 请求
3. 用户在不知情的情况下，点击了恶意链接，银行网站会以用户的身份，发送 transfer 请求，从而达到攻击的目的。

## 如何防范 XSS/CSRF

- 使用 `HttpOnly` 属性，禁止 JavaScript 访问 Cookie
- 使用 `Content-Security-Policy` 限制页面可以加载的资源
- 使用 `CSRF Token` 验证请求来源
- 使用 `SameSite` 属性，限制 Cookie 的传输
- 使用 React/Vue 等框架的 `XSS` 防护
- 使用 token 存入 localStorage 中，每次请求时，将 token 存入请求头中 (避免 CSRF 攻击)
