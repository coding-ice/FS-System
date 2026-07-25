# This 指向

## 1. 调用位置

- 作用域跟在哪里定义有关，与在哪里执行无关
- `this`指向跟在哪里定义无关，跟如何调用，通过什么样的形式调用有关
- `this`(这个) 这个函数如何被调用(方便记忆)
- 为了方便理解，默认情况下不开启严格模式

## 2. 绑定规则

&emsp;&emsp;上面我们介绍了，`this`的指向主要跟通过什么样的形式调用有关。接下来我就给大家介绍一下调用规则，没有规矩不成方圆，大家把这几种调用规则牢记于心就行了，没有什么难的地方。

- 你必须找到调用位置，然后判断是下面四种的哪一种绑定规则
- 其次你要也要晓得，这四种绑定规则的优先顺序
- 这两点你都知道了，知道 this 的指向对于你来说易如反掌

### 2.1 默认绑定

&emsp;&emsp; 函数最常用的调用方式，调用函数的类型：独立函数调用

```js
function bar() {
  console.log(this); // window
}
```

- bar 是不带任何修饰符的直接调用 所以为默认绑定 为`window`
- 在严格模式下 这里的`this`为`undefined`

### 2.2 隐式绑定

&emsp;&emsp;用最通俗的话表示就是：对象拥有某个方法，通过这个对象访问方法且直接调用（注:箭头函数特殊，下面会讲解）

```js
const info = {
  fullName: "ice",
  getName: function () {
    console.log(this.fullName);
  },
};

info.getName(); // 'ice'
```

- 这个函数被`info`发起调用，进行了隐式绑定，所以当前的`this`为`info`，通过`this.fullName`毫无疑问的就访问值为`ice`

**隐式丢失 普通**

&emsp;&emsp;有些情况下会进行隐式丢失，被隐式绑定的函数会丢失绑定对象，也就是说它变为默认绑定，默认绑定的`this`值，为`window`还是`undefined`取决于您当前所处的环境，是否为严格模式。

```js
const info = {
  fullName: "ice",
  getName: function () {
    console.log(this.fullName);
  },
};

const fn = info.getName;

fn(); //undefined
```

&emsp;&emsp;这种情况下就进行了隐式丢失，丢失了绑定的对象，为什么会产生这样的问题呢？如果熟悉内存的小伙伴，就会很容易理解。

- 这里并没有直接调用，而是通过`info`找到了对应`getName`的内存地址，赋值给变量`fn`
- 然后通过`fn` 直接进行了调用
- 其实这里的本质就是独立函数调用也就是为`window`，从`window`中取出`fullName`属性，必定为`undefined`

**隐式丢失进阶**  
&emsp;&emsp;这里大家首先要理解什么是回调函数。其实可以这样理解，就是我现在不调用它，把他通过参数的形式传入到其他地方，在别的地方调用它。

```js
// 申明变量关键字必须为var
var fullName = "panpan";

const info = {
  fullName: "ice",
  getName: function () {
    console.log(this.fullName);
  },
};

function bar(fn) {
  //fn = info.getName
  fn(); // panpan
}

bar(info.getName);
```

- 首先`bar`中的`fn`为一个回调函数
- `fn = info.getName` 参数传递就是一种隐式赋值，其实跟上面的隐式丢失是一个意思，他们都是指向的`getName`引用，也就是它的的内存地址
- 因为他们的`this`丢失，`this`为全局的`window`对象
- 注意: 为什么申明必须为`var`呢？
  - 因为只有`var`申明的变量才会加入到全局`window`对象上
  - 如果采用`let\const` 则不是，具体的后续介绍一下这两个申明变量的关键字
- 但是有些场景，我不想让隐式丢失怎么办，下面就来给大家介绍一下显示绑定，也就是固定调用。

### 2.3 显示绑定

&emsp;&emsp;但是在某些场景下，`this`的改变都是意想不到的，实际上我们无法控制回调函数的执行方式，因此没有办法控制调用位置已得到期望的绑定即 this 指向。

接下来的显示绑定就可以用来解决这一隐式丢失问题。

**call / apply / bind**

&emsp;&emsp;js 中的 ”所有“函数都有一些有用的特性，这个跟它的原型链有关系，后续我会在原型介绍，通过原型链 js 中变相实现继承的方法，其中`call/apply/bind`这三个方法就是函数原型链上的方法，可以在函数中调用它们。

#### 2.3.1 call

- `call()` 方法使用一个指定的 `this` 值和单独给出的一个或多个参数来调用一个函数。
  - 第一个参数为固定绑定的`this`对象
  - 第二个参数以及二以后的参数，都是作为参数进行传递给所调用的函数
  - 该方法的语法和作用与  [`apply()`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)  方法类似，只有一个区别，就是  `call()`  方法接受的是**一个参数列表**，而  `apply()`  方法接受的是**一个包含多个参数的数组**。

```js
var fullName = "panpan";

const info = {
  fullName: "ice",
  getName: function (age, height) {
    console.log(this.fullName, age, height);
  },
};

function bar(fn) {
  fn.call(info, 20, 1.88); //ice 20 1.88
}

bar(info.getName);
```

#### 2.3.2 apply

- 与`call`的方法类似，只是参数列表有所不同
  - `call` 参数为单个传递
  - `apply` 参数为数组传递

```js
var fullName = "panpan";

const info = {
  fullName: "ice",
  getName: function (age, height) {
    console.log(this.fullName, age, height);
  },
};

function bar(fn) {
  fn.apply(info, [20, 1.88]); //ice 20 1.88
}

bar(info.getName);
```

#### 2.3.3 bind

- `bind`与`apply/call`之间有所不同，`bind`传入`this`，则是返回一个`this`绑定后的函数，调用返回后的函数，就可以拿到期望的 this。
- 参数传递则是
  - 调用`bind`时，可以传入参数
  - 调用`bind`返回的参数也可以进行传参

```js
var fullName = "panpan";

const info = {
  fullName: "ice",
  getName: function (age, height) {
    console.log(this.fullName, age, height); //ice 20 1.88
  },
};

function bar(fn) {
  let newFn = fn.bind(info, 20);
  newFn(1.88);
}

bar(info.getName);
```

### 2.4 new 绑定

&emsp;&emsp;谈到`new`关键字，就不得不谈构造函数，也就是 JS 中的 "类"，后续原型篇章在跟大家继续探讨这个 new 关键字，首先要明白以下几点，`new Fn()`的时候发生了什么，有利于我们理解`this`的指向。

1.  创建了一个空对象
2.  将 this 指向所创建出来的对象
3.  把这个对象的[[prototype]] 指向了构造函数的 prototype 属性
4.  执行代码块代码
5.  如果没有明确返回一个非空对象，那么返回的对象就是这个创建出来的对象

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const p1 = new Person("ice", 20);

console.log(p1); // {name:'ice', age:20}
```

- 当我调用`new Person()`的时候，那个 this 所指向的其实就是`p1`对象

## 3. 绑定优先级

### 3.1 隐式绑定 > 默认绑定

```js
function bar() {
  console.log(this); //info
}

const info = {
  bar: bar,
};

info.bar();
```

- 虽然这样比较有些勉强，有些开发者会认为这是默认绑定的规则不能直接的显示谁的优先级高
- 但是从另外一个角度来看，隐式绑定的 this 丢失以后 this 才会指向 `widonw 或者 undefined`，变相的可以认为隐式绑定 > 默认绑定

### 3.2 显示绑定 > 隐式绑定

```js
var fullName = "global ice";
const info = {
  fullName: "ice",
  getName: function () {
    console.log(this.fullName);
  },
};

info.getName.call(this); //global ice
info.getName.apply(this); //global ice
info.getName.bind(this)(); //global ice
```

- 通过隐式绑定和显示绑定的一起使用很明显 显示绑定 > 隐式绑定

### 3.3 bind(硬绑定) > apply/call

```js
function bar() {
  console.log(this); //123
}

const newFn = bar.bind(123);
newFn.call(456);
```

### 3.4 new 绑定 > bind 绑定

首先我们来说一下，为什么是和`bind`比较，而不能对`call`和`apply`比较，思考下面代码

```js
const info = {
  height: 1.88,
};

function Person(name, age) {
  this.name = name;
  this.age = age;
}

const p1 = new Person.call("ice", 20);

//报错: Uncaught TypeError: Person.call is not a constructor
```

**new 绑定和 bind 绑定比较**

```js
const info = {
  height: 1.88,
};

function Person(name, age) {
  this.name = name;
  this.age = age;
}

const hasBindPerson = Person.bind(info);

const p1 = new hasBindPerson("ice", 20);

console.log(info); //{height: 1.88}
```

- 我们通过`bind`对`Person`进行了一次劫持，硬绑定了 this 为`info`对象
- `new` 返回的固定 this 的函数
- 但是我们发现并不能干预 this 的指向

### 3.5 总结

`new关键字` > `bind` > `apply/call` > `隐式绑定` > `默认绑定`

## 4. 箭头函数 (arrow function)

首先箭头函数是`ES6`新增的语法

```JS
const foo = () => {}
```

### 4.1 箭头函数 this

```js
var fullName = "global ice";

const info = {
  fullName: "ice",
  getName: () => {
    console.log(this.fullName);
  },
};

info.getName(); //global ice
```

- 你会神奇的发现？ 为什么不是默认绑定，打印结果为`ice`
- 其实这是`ES6`的新特性，箭头函数不绑定`this`，它的`this`是上一层作用域，上一层作用域为`window`
- 所以打印的结果是 `global ice`

### 4.2 箭头函数的应用场景 进阶

- 需求: 在`getInternalName`通过`this`拿到`info`中的`fullName` (值为`ice`的`fullName`)

```js
const info = {
  fullName: "ice",
  getName: function () {
    let _this = this;
    return {
      fullName: "panpan",
      getInternalName: function () {
        console.log(this); // obj
        console.log(_this.fullName);
      },
    };
  },
};

const obj = info.getName();
obj.getInternalName();
```

1.  当我调用 `info.getName()` 返回了一个新对象
2.  当我调用返回对象的`getInternalName`方法时，我想拿到最外层的`fullName`，我通过，`getInternalName`的 this 访问，拿到的 this 却是`obj`，不是我想要的结果
3.  我需要在调用`info.getName()` 把 this 保存下来，`info.getName()` 是通过隐式调用，所以它内部的 this 就是 info 对象
4.  `getInternalName`是 obj 对象，因为也是隐式绑定，this 必定是 obj 对象，绕了一大圈我只是想拿到上层作用域的 this 而已，恰好箭头函数解决了这一问题

```js
const info = {
  fullName: "ice",
  getName: function () {
    return {
      fullName: "panpan",
      getInternalName: () => {
        console.log(this.fullName);
      },
    };
  },
};

const obj = info.getName();
obj.getInternalName();
```

## 5. 总结

### 5.1 this 的四种绑定规则

1.  默认绑定
2.  隐式绑定
3.  显示绑定 apply/call/bind(也称硬绑定)
4.  new 绑定

### 5.2 this 的优先级 从高到低

1.  new 绑定
2.  bind
3.  call/apply
4.  隐式绑定
5.  默认绑定
