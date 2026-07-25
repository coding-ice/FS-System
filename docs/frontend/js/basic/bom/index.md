# Bom

<script setup>
  import Hashchange from './demo/Hashchange.vue'
</script>

Bom 全称是 Browser Object Model （浏览器对象模型）

## History & Hash

这两个是非常重要的概念，客户端路由的底层实现（监听路由的变化且不刷新页面），其本质是映射关系，path : component。
API 用法请直接查阅 MDN 文档。

### History

- 通过 history.pushState 不刷新改变 path
- 通过 location.pathname 获取 pathname

### Hash

改变 hash，查看控制台

<Hashchange />

::: details
<<< ./demo/Hashchange.vue
:::

## 客户端存储

存储/共享，条件都是基于同域的，会有各自的作用域

### localStorage

- 存储在 localStorage 的数据可以长期保留
- 可以被同域访问

### sessionStorage

- 存储在 sessionStorage 的数据在会话关闭后清除
- 需要注意的是
  - 在存储了 sessionStorage 的会话的页面内，打开一个同域的会话，即使是新窗口打开，也会复制当前浏览会话的上下文到新窗口中
  - 复制一个会话，同样会共享上下文，但是新创建一个标签页，输入同样的地址，不会共享

**两者的区别**

1. 页面会话关闭后，localStorage 保留，sessionStorage 会被删除
2. 页面内进行跳转（同域），数据都会保留
3. 外部打开（新选项卡），localStorage 会保留，sessionStorage 不会保留
