# data-types

## 类别

截止目前为止（2024），分为**两大类**（简单/复杂），**八种数据类型**

1. 简单数据类型（原始）
   - 简单数据类型占用内存小，存储在栈空间，栈空间存储值
   - 分别为
     1. String
     2. Number
     3. Boolean
     4. Undefined
     5. Null
     6. Symbol
     7. BigInt
2. 复杂数据类型
   - 复杂数据类型占用内存大，存储在堆空间，栈空间存储其引用（指针）指向堆空间
     1. Object

**查看以下代码内存图**

```js
const obj = { name: "ice", age: 24 };
const name = "ice";
```

!["memory"](../images/memory.png)

## 区分数据类型

1. typeof
2. instanceof
3. Object.prototype.toString.call(this)

### typeof

它可以用来区分出简单数据类型或函数

```js
typeof "ice"; // 'string'
typeof 25; // 'number'
typeof 25n; // 'bigint'
typeof true; // 'boolean'
typeof undefined; // 'undefined'
typeof (() => {}); // 'function'

typeof {}; // 'object'
typeof []; // 'object'
typeof null; // 'object'
```

它不能用来区分对象类型，因为都会是 `object` （除了 func），另外 `typeof null === 'object'`，[即诞生以来即使如此](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/typeof#typeof_null)。因为在 js 中 存储值，分为两种

1. 类型标签
2. 存储值

object 和 null 的类型标签都是 0 ，null 在大多数语言中代表空指针 （0x00），所以它 `typeof null  === 'object'`

### instanceof

用来区分复杂数据类型，后续在原型链一文会详细介绍

```js
/**
 * 1. A instanceof B
 *  A 的原型链中是否出现过 B 的原型对象
 */

({}) instanceof Object; // true

// 等同于

// ({}).__proto__ === Object.prototype

[] instanceof Array; // true
```

### toString

`Object.prototype.toString` 方法，可以判断复杂/简单数据类型，大部分包装类都会实现自己的 `toString` 方法（重写），利用它以及 `call` 改变其 this 指向，可以拿到精确的类型

```js
Object.prototype.toString.call(0); // '[object Number]'
Object.prototype.toString.call(""); // '[object String]'
Object.prototype.toString.call(null); // '[object Null]'
Object.prototype.toString.call(null); // '[object Null]'
Object.prototype.toString.call(() => {}); // [object Function]
Object.prototype.toString.call([]); // '[object Array]'
Object.prototype.toString.call({}); // '[object Object]'
```

### getDataType

我们知道，可以通过 toString 拿到更精确的数据类型，那么我们来实现一个 getDataType 工具函数

<<< ../utils/getDataType.js

## 包装类

```js
// 1. 包装类
const name2 = new String("ice");
// 2. 字面量
const name1 = "ice";
```

从上面的代码，我们可以得知 name1 只是一个单纯的字符串，而 name2 是一个对象。

```js
const name1 = new String("ice");
name1.toUpperCase(); // ICE

const name2 = "ice";
name2.toUpperCase(); // ICE
```

- name1 它的“隐式原型”是 `String.prototype`，因为它是 String 的实例对象，所以它继承了父类原型上的方法，因此可以调用 toUpperCase 方法
- name2（原始值） 它也可以调用 toUpperCase，这是为什么呢？ 它不就是一个简单的字符串吗？
  - 每当用到某个原始值的方法，后台都会创建对应的包装类型对象，从而暴露出操作原始值的各种方法
    1. 创建 String 类型的实例
    2. 调用实例上的特定方法
    3. 销毁实例

也就是说

```js
const name2 = "ice";
const uName2 = name2.toUpperCase(); // ICE

// 相当于

let name3 = new String("ice");
const uName3 = name3.toUpperCase(); // ICE
name3 = null;
```

前面我们有说道原始类型/复杂数据的区别，这也是这样设计的原因

## 隐式类型转换

有三种隐式类型转换

1. toPrimitive
2. toNumber
3. toString

思考以下代码：

```js
const info = {
  age: 24,
  valueOf() {
    return this.age++;
  },
};

if (info == 24 && info == 25) {
  console.log("age: ", info.age); // age：25
}
```

通过以上代码，我们可以知道 == ，比较的时候调用了 valueOf 方法，接下来我们开始探究这一行为

### toPrimitive

`toPrimitive(input, PreferredType?: number | string)`

- input 为输入的值
- PreferredType 为首选类型，如果没有传入参数，为 number 类型

::: tip
PreferredType 只是一个类型符号，不一定返回的值就是该类型值
:::

#### type：string

当 `PreferredType：string` 有以下规则

```js
// pseudocode
function toPrimitive(input, PreferredType) {
  if (input === 原始值) {
    return input;
  } else if (input.toString() === 原始值) {
    return input.toString();
  } else if (input.valueOf() === 原始值) {
    return input.valueOf();
  }

  throw new TypeError();
}

toPrimitive(unknown, string);
```

根据以上规则转为 type：string 规则

1. 如果是原始值，直接返回
2. 如果`input.toString()`是原始值，直接返回
3. 如果`input.valueOf()`是原始值，直接返回
4. 抛出 TypeError

#### type：number

<!-- prettier-ignore -->
```js
// pseudocode
function toPrimitive(input, PreferredType) {
  if (input === 原始值) {
    return input;
  } else if (input.toString() === 原始值) { // [!code --]
    return input.toString(); // [!code --]
  } else if (input.valueOf() === 原始值) { // [!code --]
    return input.valueOf(); // [!code --]

  } else if (input.valueOf() === 原始值) {// [!code ++]
    return input.valueOf(); // [!code ++]
  } else if (input.toString() === 原始值) { // [!code ++]
    return input.toString(); // [!code ++]
  }

  throw new TypeError();
}

toPrimitive(unknown, string); // [!code --]
toPrimitive(unknown, number); // [!code ++]
```

- 从代码中，我们可以得知 type 的类型不同，也只是 toString ｜ valueOf 调用的先后顺序不同而已

1. number -> valueOf -> toString
2. string -> toString -> valueOf

### ToString

| input     | output                                             |
| --------- | :------------------------------------------------- |
| string    | 无需转换                                           |
| undefined | 'undefined'                                        |
| null      | 'null'                                             |
| 123       | '123'                                              |
| false     | 'false'                                            |
| {}        | toPrimitive({}, string)获得原始值，再进行 toString |

### ToNumber

| input     | output                                             |
| --------- | :------------------------------------------------- |
| number    | 无需转换                                           |
| ''        | 0                                                  |
| '123'     | 123                                                |
| 'abc'     | NaN                                                |
| false     | 0                                                  |
| null      | 0                                                  |
| undefined | NaN                                                |
| {}        | toPrimitive({}, number)获得原始值，再进行 toNumber |

### 实战案例

#### + 运算符

```js
// + 运算符，可以是值运算也可以是字符串相加
1 + null; // 1
1 + undefined; // NaN (Not a Number)

// 如果一段出现了字符串，字符串类型优先
1 + ""; // 1
1 + "A"; // '1A'
1 + "1"; // 一端出现了字符串，直接拼接 -> '11'
/**
 * {} 空对象，不是原始数据类型，不能进行相加操作，所有要通过 toPrimitive 转为原始数据类型，type 没有指定的情况为 number
 * toPrimitive({}, number) 先 valueOf （返回自身，不是原始类型），toString（原始数据类型 即：'[object, Object]'）
 * 1 + '[object, Object]' -> '1[object, Object]' 一端出现了 str 为字符串拼接
 */
1 + {}; // 1[object, Object]

1 + []; // '1' 推导过程：[].toString() -> "" -> 1 + "" -> '1'
```

#### == 运算符

- null 和 undefined 相等，且不能转换为其他类型进行比较
- 如果一端出现 Number 类型，其他类型都转为 Number 类型，如果是复杂数据类型，先进行 toPrimitive(input, number) 也就是先拿到 valueOf 的原始值，在进行 ToNumber 操作
- 如果是复杂数据类型，则进行引用比较
- NaN 不等于自身

```js
null == undefined; // true
NaN == NaN; // false
NaN != NaN; // true

null == 0; // false
undefined == 0; // false
"" == 0; // true
1 == "1"; // true
false == 0; // true
1 == "true"; // false  "true" -> NaN (toNumber)

({}) == {}; // false
```
