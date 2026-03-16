# 基础

## SPA

SPA（Single Page Application）导航。

- 传统网页 (MPA)：你点击一个链接，浏览器会向服务器请求一个新的 `.html` 文件。整个页面会白屏一瞬间，然后重新加载所有的资源（图片、CSS、JS）。
- SPA 导航：浏览器只在第一次进入网站时加载一次 HTML。之后的“跳转”其实是 JavaScript 拦截了你的点击事件，动态地把旧内容删掉，把新内容塞进去，同时更新浏览器的 URL 地址。

RouteLink (路由链接)

RouteLink（在不同框架里叫法不同，如 React Router 里的 `<Link>` 或 Vue Router 里的 `<router-link>`）是实现 SPA 导航的专用组件。

它长得像 HTML 的 `<a>` 标签，但行为完全不同：

- 传统 `<a>` 标签会强行打断当前状态，让浏览器重新发起网络请求。

    ```html
    <a href="/about">关于我们</a>
    ```

- RouteLink 组件
    - 阻止默认行为：防止浏览器刷新页面。
    - 调用 History API：手动修改地址栏（比如从 / 变成 /about），但不触发跳转。
    - 触发组件更新：通知前端路由中心（Router），“用户想看 About 页面”，于是 Router 把 `About` 组件渲染到屏幕上。

    ```html
    <Link to="/about">关于我们</Link>
    ```

核心原理：History API

SPA 导航之所以能成功，是因为浏览器提供了一个 History API ($window.history$)。它允许开发者通过代码修改 URL 路径而不触发加载。

- `history.pushState()`: 把新路径推入浏览器历史记录。
- `popstate` 事件：当用户点击浏览器“后退”按钮时，程序能监听到并切回旧内容。

## 标识系统

Favicon 网站图标。

Favicon 是 "Favorite Icon" 的缩写。会出现在：

- 浏览器标签页（Tab）。
- 浏览器的书签栏。
- 浏览器的历史记录列表。

有多种格式，通常是 $16 \times 16$ 像素或 $32 \times 32$ 像素。在 HTML 的 `<head>` 标签中定义如下：

```html
<link rel="icon" href="/favicon.ico" type="image/x-icon">
```

PWA 图标（Progressive Web App Icons）。

PWA（渐进式 Web 应用）允许用户将网站“安装”到手机桌面或电脑桌面上。此时，网站就像一个真正的 App 软件，需要一个高分辨率的图标。通常出现在：

- 手机屏幕桌面。
- 电脑的任务栏（Windows）或 Dock 栏（macOS）。
- 应用启动时的闪屏（Splash Screen）。

特点为高分辨率，因为要在不同尺寸的屏幕上显示，通常需要提供多种尺寸（如 $192 \times 192$ 和 $512 \times 512$ 像素）。Android 等系统会对图标进行裁剪（圆角或圆形），PWA 图标支持“安全区”设计，确保图标核心内容不被裁掉。它不在 HTML 里直接定义，而是写在网站根目录的 `manifest.json` 文件中：

```json
"icons": [
  {
    "src": "icon-192x192.png",
    "sizes": "192x192",
    "type": "image/png",
    "purpose": "any maskable"
  }
]
```
