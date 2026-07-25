# Proxy & Reflect

## 早期痛点

在 ES6 以前，如何知道一个对象被访问了或者被赋值了呢？  
**Object.defineProperty**
通过下方案例，我们可以通过 closure 的方式，劫持对象中的 getter / setter

<<< ./demo/simple.js

如果需要劫持多个 key / value，可以通过以下方式，同时 Vue2 中，实现响应式原理也是通过该 API

<<< ./demo/mulit.js

虽然可以监听对象的 getter / setter，但是其他的操作比如：删除，新增 它是无能为力的，并且这个 API 设计的初衷并不是为了监听对象的。

## Proxy 代理

通过 Proxy 可以创建出一个代理对象，对代理对象进行一些列操作会被捕获器捕获

<<< ./demo/proxy.js

与 `Object.defineProperty` 不同的是，它有更强大的监听能力，有 13 个捕获器并且也能监听对象的新增，删除等。另外要特殊说明的是其中的 `target === obj`，而 `receiver === proxyed`
Vue3 源码中实现响应式则是通过 Proxy 的方式

## Reflect 反射

Reflect 提供了许多操作对象的方法，与 Object 中操作的对象方法类似，而 Object 作为构造函数把这些静态方法放在它身上并不合适，所以有了 Reflect。  
大部分反射的 API 在 Object 中都有对应的方法

```js
const obj = {
  name: "ice",
};
Reflect.get(obj, "name"); // ice
Reflect.set(obj, "name", "panda"); // true
Reflect.has(obj, "name"); // true
// ...
```

了解了 Reflect 方法，我们来改造下原有的 Proxy

<<< ./demo/reflect&proxy.js

另外有一个参数 receiver 参数，我们一直都没有用到，那它是用来干嘛的？

- 当源对象使用了 getter/setter 时，可以通过 receiver 改变其内部的 this 指向

<<< ./demo/reflect&proxy&receiver.js
