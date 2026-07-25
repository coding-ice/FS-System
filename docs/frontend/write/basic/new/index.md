# new 操作符

## new Foo() 做了哪些事情？

1. 创建一个空对象

```js
const obj = {};
```

2. 这个对象的隐式原型指向函数的显示原型 （即 `obj.__proto__ === Foo.prototype`）

```js
obj.__proto__ = Foo.prototype;
```

3. this 指向这个空对象，并且执行构造函数

```js
const result = Foo.apply(obj, args);
```

4. 返回这个创建的对象 （前提：没有显示的返回对象）

- 基本类型 / 无返回值，就返回创建的对象
- 如果返回值是 obj / fn，返回该值

```js
if (
  (typeof result === "object" && result !== null) ||
  typeof result === "function"
)
  return result;

return obj;
```

## 用法

<<< ./code/new_demo.js

## 实现

<<< ./code/new.js

其中，第一步和第二步可以合并为：

```js
const obj = Object.create(Fn.prototype);
```
