# 类与继承

## 前言

> &emsp;&emsp;JS 中的原型/继承，我个人觉得是 JS 中最难的一个知识点。从对象的`[[prototype]]`(即隐式原型)，再到函数`prototype`(显示原型)，再到原型链、再到继承的多种方式原型链继承、借用构造函数继承、组合借用继承、寄生组合式继承，最终再到`ES6`的`class`关键字实现继承。 <br> &emsp;&emsp;无论再多的术语，其实都离不开生活，技术也是如此，技术源于生活，却不会高于生活，大部分都是现实的一种抽象。

## 1. 对象的原型(隐式原型)

在 JS 当中，每个对象中都有一个特殊的内置属性(`[[prototype]]`)/隐式原型，其实就是对于其他对象的引用而已，换句话说就是：这个特殊的内置属性指向着另外一个对象，它也称之为对象的隐式原型。

### 1.1 查看隐式原型

- `obj.__proto__`,早期由浏览器实现，兼容性较差
- `Object.getPrototypeOf`方法也能获取到

```js
const info = {
  name: "ice",
  age: 22,
};

console.log(info.__proto__);
console.log(Object.getPrototypeOf(info));

console.log(info.__proto__ === Object.getPrototypeOf(info)); // true
```

- 打印结果如下: - 我们从打印结果可以看出，通过`__proto__`和`Object.getPrototypeOf`方法，获取的对象应用是同一个
  ![1663940777873.jpg](./images/1.png) - `constructor`这个特殊的属性，我们在后面再来剖析，它默认会指向当前的函数对象

### 1.2 隐式原型有什么用？

1. 当你访问该对象的属性时会触发`[[GET]]`操作（对象的存取描述符）
2. 当我访问`info.name`的时候，首先会查找该`info`对象中，是否有这个属性，有就使用它

```js
const info = {
  name: "ice",
  age: 22,
};

console.log(info.name);
```

3. 如果无法在该`info`对象中找到，就会沿着该对象的隐式原型`[[prototype]]`(沿着原型链)，有就使用它。直到查询到“尽头”后，还未找到该属性的值，返回`undefined`

```js
//1. 未找到
const info1 = {
  name: "ice",
  age: 22,
};

console.log(info1.money); //undefined

//2. 隐式原型中找到
const info2 = {
  name: "ice",
  age: 22,
};

///后续会讲到是什么
Object.prototype.money = 100;

console.log(info2.money); //100
```

## 2. 函数的显示原型

多年以来，js 中有一种奇怪的行为，一直被“无耻”的滥用，那就是模仿类（早期是面向对象编程的天下）。这种奇怪的“类似类”的行为，就是利用函数的特殊属性，因为所有函数都会有一个显示原型(`prototype`)属性，它会指向另外一个对象，可以通过这一特性变相实现继承。

### 2.1 查看函数的原型

- 所有的函数都一个`prototype`属性(**箭头函数除外**)，注意：**不是对象的 \_\_proto\_\_**

```js
function bar() {}

//所有的函数都有prototype属性
console.log(bar.prototype);

const info = {};
//对象没有prototype属性
console.log(info.prototype);
```

### 2.2 显示原型有什么用呢？

- 最直接的解释，通过`new`关键字调用的函数(`new Foo()`)，创建的对象，最终这个对象的`[[prototype]]` (`__proto__`/隐式原型)，会指向`Foo.prototype`（**函数的显示原型**）这个对象。

```js
function Person() {}

const p1 = new Person();
const p2 = new Person();

console.log(p1.__proto__ === Person.prototype); //true
console.log(p1.__proto__ === p2.__proto__); //true
```

**内存表现**

![image.png](./images/2.png)

### 2.3 构造函数(类)

当首字母大写的函数，我们称之为构造函数(社区约定规范)，早期 ES5 模仿类，在 JS 中也可以把`new Fn()`这种行为称之为`类`

#### 2.3.1 `new Fn()` 发生了什么

1. 创建一个空对象
2. `this`指向创建出来的对象
3. 这个对象的隐式原型指向了函数的显示原型，(即`p1.__proto__ === Person.prototype`)
4. 运行函数体代码
5. 如果没有明确返回一个非空对象，那么返回的就是创建出来的对象

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const p1 = new Person("ice", 22);

console.log(p1); //{ name: 'ice', age: 22 }
console.log(p1.__proto__ === Person.prototype); //true
```

**内存表现**

![image.png](./images/3.png)

#### 2.3.2 显示原型上添加属性/方法

函数的显示原型，是一个对象，我们当然可以在对象上面添加我们自定义属性，思考以下代码

```js
function Person() {}

Person.prototype.money = 100;
Person.prototype.getDoubleMoney = function () {
  return this.money * 2;
};

const p1 = new Person();

console.log(p1.money); //100
console.log(p1.getDoubleMoney()); //200
```

- 我们在构造函数的显示原型上，添加了`money`属性和`getDoubleMoney`方法
- 当我们对象自身上没有该`money`属性和`getDoubleMoney`方法，就会沿着对象的原型链一直查找，直至找到“尽头”，还未找到则为`undefined`，其实很明显这些属性/方法，存放在`Person`函数的原型上
- `p1`对象为`Person`的实例（instance），即 `p1.__proto__ === Person.prototype`

**内存表现**

![image.png](./images/4.png)

- 每个函数都会有`name`和`length`属性，`name`为函数的名称，`length`为函数的形参个数

**为什么添加到原型上？**

- 为什么我要添加到原型上？ 我为啥不能把属性/方法写在函数内部呢？

思考以下代码

```js
function Person(name, age, money) {
  this.name = name;
  this.age = age;
  this.money = money;

  this.getDoubleMoney = function () {
    return this.money * 2;
  };
}

const p1 = new Person("ice", 22, 100);
const p2 = new Person("panda", 22, 200);

console.log(p1.name, p1.money); //ice 100
console.log(p1.name, p1.getDoubleMoney()); //ice 200

console.log(p2.name, p2.money); //panda 200
console.log(p2.name, p2.getDoubleMoney()); //panda 400
```

- 我这里直接说结论：
  - 属性应该写在函数内部，而不是写在原型对象上，因为对于构造函数来说，每个实例对象应该有属于自己的属性，而不是同一个。
  - **公共方法**应该放在构造函数的原型上，因为**可以复用**。当我创建一个实例都会运行构造函数，我创建多个实例，那么就要调用多次。如果方法在函数体中，调用多次构造函数，方法就会被定义多次，这样其实是没有必要的。(多次调用、多次定义、浪费性能)

### 2.4 constructor 属性

我们无论是前面打印原型对象，还是查看内存表现图，多次提到了`constructor`，那`constructor`到底是什么呢？

- 每个原型对象上都有一个`constructor`，它默认指向了当前的函数，形成循环引用，V8 引擎 GC 采用标记清除算法，不会存在内存泄漏问题
- `Person.prototype.constructor === Person`

```js
function Person() {}

const p1 = new Person();

console.log(Person.prototype.constructor.name); //person
console.log(Person.prototype.constructor === Person); //true
console.log(p1.__proto__.constructor === Person.prototype.constructor); //true
```

### 2.5 重写函数的显示原型

```js
function Person(name, age, money) {
  this.name = name;
  this.age = age;
  this.money = money;
}

//重写了显示原型，是一个全新的对象
Person.prototype = {
  getDoubleMoney() {
    return this.money * 2;
  },
};

const p1 = new Person("ice", 22, 100);

console.log(p1.getDoubleMoney()); //200
```

- 我们之前采用赋值的方式，是添加属性的方式添加方法，即`Person.prototype.getDoubleMoney = function() {} `，这是相当于在原对象上添加
- 这个案例是，是直接赋值了一个新对象，在内存中的表现为，指向了另外一个对象，而不是默认的显示原型了。

**探究 constructor**  
上面的案例中我们把函数的原型进行了**重写**的操作，你们有思考过`constructor`属性吗，原来的原型已经被我重写，赋值为一个全新的对象了，那这个全新的对象`constructor`又指向谁了呢？  
绕来绕去都快被绕晕了，什么乱七八糟的！接下来跟我一起探究

```js
function Person(name, age, money) {
  this.name = name;
  this.age = age;
  this.money = money;
}

Person.prototype = {
  getDoubleMoney() {
    return this.money * 2;
  },
};

console.log(Person.prototype.constructor === Object); // true
```

- 你会惊讶的发现，woc，这是什么意思？ 为什么指向的却是 Object 呢？难道是 bug 吗？其实并不是，原型/原型链/继承都是环环相扣，一环扣着一环，一个点没吃透，剩下的就很难明白。

**继续推断探究**

- 探索`Person.prototype.constructor === Object`

```js
/*解: Person.prototype.constructor === Object
      1. 首先我们对原对象进行了重写
      2. 每个原型对象上都有constructor属性，我们赋值的那个对象身上肯定也有原型对象啊！
        Person.prototype = { getDoubleMoney () { return this.money * 2 } }
      3. 此时的Person.prototype = {}，等于了一个全新的对象，并不用关心里面的方法getDoubleMoney
      4. 伪代码: const obj = {}（字面量写法） 等同于 const obj = new Object()，所以obj对象的隐式原型即（obj.__proto__ === Object.prototype），obj为Object的实例对象。
      5. 我们赋值的新对象的隐式原型指向了Object.prototype,所以Person.prototype.constructor去查找constructor的时候，自己没有constructor，找到的其实Object.prototype.constructor,所以它的值等于Object
      6. js中的一句话：万物皆对象(虽然不严谨)，因为Object.prototype是"尽头"，在查找就等于null了
*/
```

**自定义 constructor**

```js
function Person(name, age, money) {
  this.name = name;
  this.age = age;
  this.money = money;
}

Person.prototype = {
  getDoubleMoney() {
    return this.money * 2;
  },
};

Object.defineProperty(Person.prototype, "constructor", {
  value: Person,
  writable: true,
  configurable: false,
  enumerable: false,
});

console.log(Person.prototype.constructor === Person); // true
```

- 这样才是正确重写函数显示原型的正确方法，跟默认提供的显示原型一致

## 3. 函数的隐式原型

- 函数是一个函数，（写累了就开始水文章，说废话了是吧？），但它也是一个特殊的对象。函数就像我们人类一样，在生活中，扮演着许多角色(身份)。
- 函数，既有函数身份，也有对象身份，既然是对象那肯定有隐式原型，我们又绕回来了哈哈哈哈哈哈。

```js
function Person() {}

Person.fullName = "ice";

console.log(Person.fullName); //ice
console.log(Person.__proto__ === Function.prototype); //true
```

- 为什么 `Person.__proto__ === Function.prototype`相等，在介绍 constructor，我们已经详细的分析过类似的了，其实本质都一样
  - `Person`作为对象的身份有`__proto__`，`Person`则是 `new Function()`的实例对象，所以`Person.__proto__ === Function.prototype`
- 这里涉及到了原型的继承关系，我们不在这里继续深挖下去，不然不好理解。

## 4. 面向对象 ES5 -> 继承

- 举个栗子，把继承抽象成现实的栗子。
  - 首先我们是人类，在生活中我们扮演着各种角色，每个年龄段扮演着不同的角色。当我们读书期间我们扮演着学生这一角色，当我们踏入社会参加工作的那一刻，我们扮演着员工这一角色，如果有幸各位当老板了，扮演着老板这一角色，但是无论扮演着什么角色，我们终究是人类（**共性，代码亦是如此，抽取共享，提高代码复用性**）。谁也逃离不了，生老病死，我们要在活着的时候多做一些有意义的事，日行一善，多帮助他人，回馈社会。
- 面向对象之四大特性，我们主要来研究继承，将复用的代码抽取到父类中，子类继承父类直接使用即可，子类可以使用父类中的方法或属性了。
  - 封装
  - 继承
  - 多态
  - 抽象

### 4.1 原型链

那 JS 中如何实现继承呢？我们前面说过，其实 JS 中本没“类”，模仿的多了，也就有了“类”，而在 JS 中，实现继承，是逃不开原型链的，因为正是利用原型链这一机制，实现了“类”

- 前面我们已经在对象的隐式原型中，谈到了原型链，现在我们要对它进行剖析了

```js
let info = {
  name: "ice",
  age: "22",
};

console.log(info.__proto__); //Object.prototype

console.log(info.__proto__.__proto__); //null
```

- 最开始说过，一个对象查找属性（key）的时候，首先从自己本身查找，如果有直接返回值（value），如果没有则沿着原型链查找，原型链中有则返回，直至找到“尽头”(`Object.prototype`)，还未找到，则返回 undefined。

```js
let info = {
  name: "ice",
  age: "22",
};

info.__proto__ = {
  money: 100,
};

info.__proto__.__proto__ = {
  website: "iceweb.icu",
};

console.log(info.name); //ice
console.log(info.money); //100
console.log(info.website); //iceweb.icu
console.log(info.girlFriend); // undefined
```

- 只要你想你可以一直定义对象的隐式原型(`__proto__`)，让它一直查找，（因为`info`的隐式原型又是一个对象，对象又有隐式原型，这样一直查找下去），这样一层一层像链条一样，所以我们把它称之为**原型链**，这就是 JS 中实现继承的本质。

#### 4.1.1 查看顶层原型（原型链尽头）

- 默认情况下: 顶层原型为`Object.prototype`，再继续查找下去就为 null 了，也可以说 Object 是所有类的父类

#### 4.1.2 顶层原型有什么用？

- `Object.prototype`有什么用呢？
  - 该对象上默认有许许多多的属性和方法，创建出来的对象继承自`Object.prototype`，所以通过字面量创建出来的对象/`new Object()`都能使用顶层原型上的属性和方法。如：toString()...

```js
const info1 = {
  name: "ice",
  age: 22,
};

const info2 = new Object({
  name: "panda",
  age: 20,
});

console.log(info1.name); //ice
console.log(info1.valueOf() === info1); //true
console.log(info1.toString()); //[object Object]

console.log(info2.name); //ice
console.log(info2.valueOf() === info2); //true
console.log(info2.toString()); //[object Object]
```

**创建对象的原型图**

![image.png](./images/5.png)

### 4.2 实现继承的多种办法

#### 4.2.1 引用赋实现(大聪明做法)

```js
//父类
function Person() {}
//在父类
Person.prototype.running = function () {
  console.log(`${this.name} running!!!`);
};

function Student(name, age) {
  this.name = name;
  this.age = age;
}

//引用赋值，此时子类的原型对象 === 父类的原型对象
Student.prototype = Person.prototype;
Student.prototype.studying = function () {
  console.log(`${this.name} studying!!!`);
};

const ice = new Student("ice", 22);

ice.running();
ice.studying();

//ice running!!!
//ice studying!!!
```

- “看起来”好像是实现了继承，确实“使用”子类/父类的方法，但是真的是这样吗？
- 因为父类与子类用的是一个原型对象，无论我操作子类/父类 它们互相影响

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.running = function () {
  console.log(`${this.name} running!!!`);
};

function Student(name, age) {
  this.name = name;
  this.age = age;
}

Student.prototype = Person.prototype;
Student.prototype.studying = function () {
  console.log(`${this.name} studying!!!`);
};

const p1 = new Person("panda", 20);

//被子类操作后，父类也有了studying方法，显然是错误的做法
p1.studying();
```

- 我们再仔细看，明明`Person`和`Stuedent`都有的`name`/`age`属性，我们却要定义两遍，我们能不能进行属性复用呢？完了第一个方法的继承都没解决，又来了一个属性复用的问题...,别着急让我们一起来探究~

#### 4.2.2 原型链继承

```js
//1. 父类
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sex = "male";
}

//2. 父类显示原型上添加方法
Person.prototype.running = function () {
  console.log(`${this.name} running!!!`);
};

//3. 子类
function Student(name, age) {
  this.name = name;
  this.age = age;
}

//4. 创建父类的实例，这个对象`p1.__proto__ === Person.prototype`
const p1 = new Person();

//5. 子类显示的原型对象 = p1对象
Student.prototype = p1;

//6. 在p1对象上添加方法
Student.prototype.studying = function () {
  console.log(`${this.name} studying!!!`);
};

const s1 = new Student("ice", 22);
console.log(s1);
console.log(s1.sex);

s1.running();
s1.studying();

//Person { name: 'ice', age: 22 }
//male
//ice running!!!
//ice studying!!!
```

- 这样是初步的实现了继承，但是它们存在几个问题
  - 当我打印 s1 对象的时候，有一些值(`sex`)，是存在 p1 对象上的，我直接打印却查询不到这个属性，但是我通过`s1.sex`却能访问到，容易产生误解
  - s1 的类型错误，具体的类型居然为`Person`，应该是`Student`类型
  - 没有进行属性的复用，父类有的属性，子类竟然还重复定义了一次

**内存表现**

![image.png](./images/6.png)

- 其本质两点概括
  - 创建了一个全新的对象（`p1`），且这个对象的隐式原型指向了父类的显示原型
  - 子类的显示原型指向那个新创建来的对象
    - 当我 new 子类的时候，其创建的实例的隐式原型，已经指向了新创建出来的对象（`p1`），沿着新对象的隐式原型，从而实现了继承

#### 4.2.3 借用构造函数继承(经典继承)

- 借用构造函数继承主要解决的问题就是复用父类属性，这里就非常容易理解，废话少说我们直接看代码。

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

function Student(name, age) {
  Person.apply(this, [name, age]);
}

const s1 = new Student("ice", 22);
console.log(s1);

//{ name: 'ice', age: 22 }
```

- 借用，其实就是主动的调用一下父类，通过改变 this 的指向，变相的实现父类属性的复用，有关 this 问题就不再赘述了，可以看下我之前写的 this 文章，这里用 apply/call 都可以，传参形式不同而已。

#### 4.2.4 组合继承

- 组合继承则是原型链继承+借用构造函数继承的结合

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.running = function () {
  console.log(`${this.name} running!!!`);
};

function Student(name, age) {
  Person.apply(this, [name, age]);
}

const p1 = new Person();

Student.prototype = p1;

Object.defineProperty(Student.prototype, "constructor", {
  value: Student,
  writable: true,
  configurable: false,
  enumerable: false,
});

Student.prototype.studying = function () {
  console.log(`${this.name} studying!!!`);
};

const s1 = new Student("ice", 22);
console.log(s1);

s1.running();
s1.studying();

// Student { name: 'ice', age: 22 }
// ice running!!!
// ice studying!!!
```

- 组合继承是 js 中最常用的模式之一，到了这里，继承的基本实现已经没有了什么问题了，但是它仍然有一些不完美的地方
- 缺点:
  - 最大的问题就是，父类都会被调用两次，第一次是构建`p1`对象的时候，第二次是借用构造函数实现父类属性复用的时候。

#### 4.2.5 原型式继承函数

- 最早由 JavaScript 领域的知名开发者道格拉斯提出；他也是 `JSON` 的创立者。Brendan Eich 曾称道格拉斯为 JS 界的宗师。
- 与寄生式继承函数类似的一种思想

**1. 兼容性最好的写法**

```js
function create(obj) {
  function Fn() {}
  Fn.prototype = obj;

  return new Fn();
}
```

**2. setPrototypeOf 方法**

- 方法设置一个指定的对象的原型
- 不推荐使用，由于现代 JavaScript 引擎优化属性访问所带来的特性的关系，更改对象的  `[[Prototype]]`  在各个浏览器和 JavaScript 引擎上都是一个很慢的操作。

```js
function create(obj) {
  let newObj = {};
  Object.setPrototypeOf(newObj, obj);

  return newObj;
}
```

**3. create 方法**

```js
function create(obj) {
  let newObj = Object.create(obj);

  return newObj;
}
```

- 方法用于创建一个新对象，使用现有的对象来作为新创建对象的原型`[[prototype]]`
- 其本质跟第一种方式没有区别

**4. `__proto__`写法，不考虑兼容性**

```js
function create(obj) {
  let newObj = {};
  newObj.__proto__ = obj;

  return newObj;
}
```

**总结: 原型式继承函数的本质**

1. 创建一个空对象
2. 这个空对象的隐式原型`[[prototype]]`，等于父类的显示原型
3. 最后返回这个对象

#### 4.2.6 寄生式继承函数

```js
//1. 原型式继承函数
function create(obj) {
  function Fn() {}
  Fn.prototype = obj;
  return new Fn();
}

//父类
function Person() {}
Person.prototype.running = function () {
  console.log("running!!!");
};

//2. 寄生式继承函数
function createStu(person) {
  const s1 = create(person);

  s1.studying = function () {
    console.log("Studying code");
  };
  return s1;
}

//3. 子类对象
const s1 = createStu(Person.prototype);
s1.running();
```

- 在原型式继承函数的基础上又进行了一次封装，在函数内部来增强对象，最后将这个对象返回

#### 4.2.7 寄生式组合继承

- 组合继承是比较理想的继承方案，但是最大的问题最少要调用父构造函数两次，但是寄生式组合继承就能解决这一问题
- 寄生式组合继承，就成是利用寄生式继承函数(与原型式继承函数类似)，像寄生虫一样，寄生在另外的对象上。

```js
function create(o) {
  function F() {}
  F.prototype = o;
  return new F();
}
//1. 创建一个新对象
//2. 新对象 __proto__ 指向父类的prototype
//3. 最后返回这个对象

function inherit(SubType, SuperType) {
  //子类的prototype = 新创建出来的对象
  SubType.prototype = create(SuperType.prototype);
  Object.defineProperty(SubType.prototype, "constructor", {
    writable: true,
    configurable: false,
    enumerable: false,
    value: SubType,
  });
}

//父类
function Person(name, age) {
  this.name = name;
  this.age = age;
}
//原型上增加方法
Person.prototype.running = function () {
  console.log(`${this.name} running!!!`);
};

//子类
function Student(name, age) {
  //借用构造函数
  Person.apply(this, [name, age]);
}

//调用inherit，实现继承
inherit(Student, Person);

//子类原型上的方法
Student.prototype.studying = function () {
  console.log(`${this.name} studying!!!`);
};

//Student的实例对象
const s1 = new Student("ice", 22);

console.log(s1);
s1.studying();
s1.running();

//Student { name: 'ice', age: 22 }
//ice studying!!!
//ice running!!!
```

**总结**

- 我们绕了一大圈，其实就是通过寄生的方式（中间人模式）
  - 让子类实例的隐式原型，指向了一个新的对象
    - 即 `子类实例.__proto__ = 子类.prototype = newObject`
      - 我们在原型上添加的方法，本质上是添加在这个新对象上的
  - 这个新的对象的隐式原型指向了父类的显示原型
    - 即 `newObject.__proto__ = 父类.prototype`
      - 这个新对象上的隐式原型(`__proto__`)，就指向了父类的 prototype，从而实现了继承
- 最早的大聪明做法，我们直接把父类的`prototype`赋值给了子类的`prototype`, 它们公用同一个原型，看上去是能实现，但是它们互相影响，因为这么做意味着以后修改了子类型原型对象的某个引用类型的时候, 父类型原生对象的引用类型也会被修改。

## 5. 原型继承关系

- 这是非常经典的一张图，好像已经被分析烂了，但是很多文章感觉分析的不够透彻，可以把这张图一共分为两部分
- 前面我们已经说过了，函数比较特殊有两种身份，第一种是函数身份，另外一种是对象身份。你是一个对象，你就会有你自己的类，这样说会比较抽象，我们来一起分析，解析之前我们先把图放在旁边，一点一点的查阅。

![b58117e53b0147e79115fad4fa0a99d8_tplv-k3u1fbpfcp-zoom-in-crop-mark_3024_0_0_0.webp](./images/7.png)

### 5.1 new Foo()

首先就是`new Foo`出发

1. `f1 = new Foo()`  
   即 `f1.__proto__ === Foo.prototype`
2. `Foo.prototype`也是一个对象，也有自己的隐式原型  
   即 `Foo.prototype.__proto__ === Object.prototype`  
   `Object.prototype`是顶层（"尽头"）, 在继续查找就为 null
3. `Foo`函数的`prototype`则是，`Foo.prototype`
4. `Foo`身为对象身份也有属于自己的`__proto__`,也有自己的构造函数  
   即`Foo.__proto__ === Function.prototype `, 因为`Foo的创建`相当于 `new Function()`
5. `Function.prototype`也是一个对象，它的`__proto__`为`Object.prototype`“尽头”，在查找下去为 null
6. `Function`也是一个对象，它也有自己的构造函数，但是它也是相当于`new Function`创建出来的**比较特殊**  
   即`Function.__proto__ === Function.prototype `

### 5.2 new Object()

从 `new Object()`出发

1. `o1 = new Object()`  
   即`o1.__proto__ === Object.prototype`, 因为它是由`Object`的实例，“尽头”，在沿着**proto**查找，则为 null
2. `Object`它的显示原型为`Object.prototype`,作为对象身份也有自己的`__proto__`，那它是由谁构建出来的呢？  
   即 `Object.__proto__ === Function.prototype`,它是由函数构建出来的，也可以说它是函数的实例对象

### 5.3 内存图分析

![image.png](./images/8.png)

## 6. 面向对象 ES6 -> 继承

- 我们前面介绍了，通过构造函数的形式来模仿“类”，在 ES6 的新标准中，使用`class`关键字来定义类
- 其 class 的本质就是前面构造函数、原型链的那一套东西，就是几个 API 调用而已

### 6.1 定义类

```js
//1. 类申明
class Person1 {}

//2. 类表达式
const Person2 = class {};
```

### 6.2 类与构造函数

- 其本质是跟构造函数一样

```js
class Person {}

const p1 = new Person();

console.log(Person.prototype);
console.log(Person.prototype.constructor);
console.log(p1.__proto__ === Person.prototype);

//{}
//[class Person]
//true
```

### 6.3 类的构造函数

- 如果我们希望在创建对象的时候给类传递一些参数，这个时候应该如何做呢？
  - 每个类都可以有一个自己的构造函数（方法），这个方法的名称是固定的 constructor；
  - 当我们通过 new 操作符，操作一个类的时候会调用这个类的构造函数 constructor；
  - 每个类只能有一个构造函数，如果包含多个构造函数，那么会抛出异常；

```js
class Person {
  constructor(name, age, money) {
    this.name = name;
    this.age = age;
    this.money = money;
  }

  running() {
    console.log(`${this.name} running!!!`);
  }
  eating() {
    console.log(`${this.name} eating!!!`);
  }
}

const p1 = new Person("ice", 22, 100);
console.log(p1);
p1.running();
p1.eating();

// Person { name: 'ice', age: 22, money: 100 }
// ice running!!!
// ice eating!!!
```

### 6.4 类的实例方法

```js
class Person {
  running() {
    console.log("running!!!");
  }
  eating() {
    console.log("eating!!!");
  }
}

const p1 = new Person();

p1.running();
p1.eating();

console.log(p1.running === Person.prototype.running);
console.log(p1.eating === Person.prototype.eating);

// running!!!
// eating!!!
// true
// true
```

- 从打印结果我们可以看出，通过类关键字定义的方法，是存放在 Person 的原型对象上的，这样的话可以给多个实例进行共享

### 6.5 类的静态方法(类方法)

- 静态方法通常用于定义直接使用类来执行的方法，不需要有类的实例，使用 static 关键字来定义：

```js
Function.prototype.money = 100;
class Person {
  static getMoney() {
    console.log(this.money);
  }
}

Person.getMoney(); //100
```

- 这里给大家留两个问题
  - 第一：静态方法中的 this 指向谁
  - 第二： Person 作为对象身份，它的隐式原型是谁

### 6.6 类实现继承

```js
class Person {}

class Student extends Person {}
```

- 对你没有看错，两行代码就实现了以前 ES5 以前的一系列繁琐的操作，很容易实现了继承。
- 在 ES6 中新增了使用 extends 关键字，可以方便的帮助我们实现继承
- 即 `Sub extend Super`

### 6.7 类继承初体验

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  running() {
    console.log("running!!!");
  }
}

class Student extends Person {
  constructor(name, age, sno) {
    super(name, age);
    this.sno = sno;
  }

  studying() {
    console.log("studying!!!");
  }
}

const s1 = new Student("ice", 22, 200010);

console.log(s1);
s1.running();
s1.studying();

// Student { name: 'ice', age: 22, sno: 200010 }
// running!!!
// studying!!!
```

我们会发现在上面的代码中我使用了一个 super 关键字，这个 super 关键字有不同的使用方式：

- 在子（派生）类的构造函数中使用 this 或者返回默认对象之前，必须先通过 super 调用父类的构造函数！
- super 的使用位置有三个：子类的构造函数、实例方法、静态方法

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  running() {
    console.log("person running!!!");
  }
}

class Student extends Person {
  stuRunning() {
    //调用父类的方法
    super.running();
  }
}

const s1 = new Student();
s1.stuRunning();

//person running!!!
```

- 静态方法调用就不演示了，想演练的可以自己尝试一下，都比较简单就是 API 调用而已。

### 6.8 继承内置类

```js
class ICEArray extends Array {
  lastItem() {
    return this[this.length - 1];
  }
}

const arr = new ICEArray(1, 2, 3);
console.log(arr.lastItem()); //3
```

- 继承字内置 Array 类，调用`lastItem`，每次获取最后一个元素。
