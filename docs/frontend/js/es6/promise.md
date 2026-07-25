# Promise

## 1. 早期异步代码困境

众所周知，js 是单线程的，耗时操作都是交给浏览器来处理，等时间到了从队列中取出执行，设计到事件循环的概念，笔者也分享过，可以看以下，理解了可以更好的理解`promise`。
我以一个需求为切入点，我模拟网络请求(异步操作)

- 如果网络请求成功了，你告知我成功了
- 如果网络请求失败了，你告知我失败了

### 1.1 大聪明做法

```js
function requestData(url) {
  setTimeout(() => {
    if (url === "iceweb.io") {
      return "请求成功";
    }
    return "请求失败";
  }, 3000);
}

const result = requestData("iceweb.io");

console.log(result); //undefined
```

首先你要理解`js`代码的执行顺序，而不是是想当然的，代码其实并不是按照你书写的顺序执行的。  
那么为什么是 `undefined`？

- 当我执行`requestData`函数，开始执行函数。遇到了异步操作不会阻塞后面代码执行的，因为 js 是单线程的，所以你写的`return`成功或者失败并没有返回给`requestData`，那我这个函数中，抛开异步操作，里面并没有返回值，所以值为`undefined`。

### 2.2 早期正确做法

```js
function requestData(url, successCB, failureCB) {
  setTimeout(() => {
    if (url === "iceweb.io") {
      successCB("我成功了,把获取到的数据传出去", [{ name: "ice", age: 22 }]);
    } else {
      failureCB("url错误，请求失败");
    }
  }, 3000);
}

//3s后 回调successCB
//我成功了,把获取到的数据传出去 [ { name: 'ice', age: 22 } ]
requestData(
  "iceweb.io",
  (res, data) => console.log(res, data),
  (rej) => console.log(rej)
);

//3s后回调failureCB
//url错误，请求失败
requestData(
  "icexxx.io",
  (res) => console.log(res),
  (rej) => console.log(rej)
);
```

早期解决方案都是传入两个回调，一个失败的，一个成功的。那很多开发者会问这不是挺好的吗？挺简单的，js 中函数是一等公民，可以传来传去，但是这样太灵活了，没有规范。  
如果使用的是框架，还要阅读一下框架源码，正确失败的传实参的顺序，如果传参顺序错误这样是非常危险的。

## 2. Promise

Promise(承诺)，给予调用者一个承诺，过一会返回数据给你，就可以创建一个 promise 对象
当我们`new`一个`promise`，此时我们需要传递一个回调函数，这个函数为立即执行的，称之为（executor）  
这个回调函数，我们需要传入两个参数回调函数，`reslove`,`reject`(函数可以进行传参)

- 当执行了`reslove`函数，会回调 promise 对象的.then 函数
- 当执行了`reject`函数，会回调 promise 对象的.catche 函数

### 2.1 Executor 立即执行

```js
new Promise((resolve, reject) => {
  console.log(`executor 立即执行`);
});
```

传入的`executor`是立即执行的

### 2.2 requestData 重构

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url === "iceweb.io") {
        //只能传递一个参数
        resolve("我成功了,把获取到的数据传出去");
      } else {
        reject("url错误，请求失败");
      }
    }, 3000);
  });
}

//1. 请求成功
requestData("iceweb.io").then((res) => {
  //我成功了,把获取到的数据传出去
  console.log(res);
});

//2. 请求失败

//2.2 第一种写法
//url错误，请求失败
requestData("iceweb.org").then(
  (res) => {},
  (rej) => console.log(rej)
);

//2.2 第二种写法
//url错误，请求失败
requestData("iceweb.org").catch((e) => console.log(e));
```

- 在函数中，new 这个类的时候，传入的回调函数称之为`executor`（会被 Promise 类中自动执行）
- 在正确的时候调用`resolve`函数，失败的时候调用`reject`函数，把需要的参数传递出去。
- 异常处理
  - 其中在`.then`方法中可以传入两个回调，您也可以查看[Promise/A+](https://promisesaplus.com/)规范
    - 第一个则是`fulfilled`的回调
    - 第二个则是`rejected`的回调
- 那这样有什么好处呢？ 看起来比早期处理的方案还要繁琐呢?
  1. 统一规范，可以增强阅读性和扩展性
  2. 小幅度减少回调地狱

### 2.3 promise 的状态

首先先给大家举个栗子，把代码抽象为现实的栗子

- 你答应你女朋友，下周末带她去吃好吃的 (还未到下周末，此时状态为**待定状态**)
- 时间飞快，今天就是周末了，你和你女友一起吃了烤肉、甜点、奶茶...（**已兑现状态**）
- 时间飞快，今天就是周末了，正打算出门。不巧产品经理，因为线上出现的紧急问题，需要回公司解决一下，你(为了生活)只能委婉的拒绝一下女友，并且说明一下缘由(**已拒绝状态**)
  使用`promise`的时候，给它一个承诺，我们可以将他划分为三个阶段
  - pending(待定)，执行了 executor，状态还在等待中，没有被兑现，也没有被拒绝
  - fulfilled(已兑现)，执行了`resolve`函数则代表了已兑现状态
  - rejected(已拒绝)，执行了`reject`函数则代表了已拒绝状态

状态只要从待定状态，变为其他状态，则状态不能再改变

思考以下代码:

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("失败");
    resolve("成功");
  }, 3000);
});

promise.then((res) => console.log(res)).catch((err) => console.log(err));

//失败
```

当我调用`reject`之后，在调用`resolve`是无效的，因为状态已经发生改变，并且是不可逆的。

### 2.4 resolve 不同值的区别

如果`resolve`传入一个普通的值或者对象，**只能传递接受一个参数**，那么这个值会作为`then`回调的参数

```js
const promise = new Promise((resolve, reject) => {
  resolve({ name: "ice", age: 22 });
});

promise.then((res) => console.log(res));

// {name: 'ice', age: 22}
```

如果`resolve`中传入的是另外一个`Promise`，那么这个新`Promise`会决定原`Promise`的状态

```js
const promise = new Promise((resolve, reject) => {
  resolve(
    new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("ice");
      }, 3000);
    })
  );
});

promise.then((res) => console.log(res));

//3s后 ice
```

如果`resolve`中传入的是一个对象，并且这个对象有实现`then`方法，那么会执行该`then`方法，`then`方法会传入`resolve`，`reject`函数。此时的`promise`状态取决于你调用了`resolve`，还是`reject`函数。这种模式也称之为: **thenable**

```js
const promise = new Promise((resolve, reject) => {
  resolve({
    then(res, rej) {
      res("hi ice");
    },
  });
});

promise.then((res) => console.log(res));

// hi ice
```

### 2.5 Promise 的实例方法

实例方法，存放在`Promise.prototype`上的方法，也就是 Promise 的显示原型上，当我 new Promise 的时候，会把返回的该对象的 promise[[prototype]]（隐式原型） === Promise.prototype (显示原型)  
即 new 返回的对象的隐式原型指向了 Promise 的显示原型

#### 2.5.1 then 方法

##### 2.5.1.1 then 的参数

`then`方法可以接受参数，一个参数为成功的回调，另一个参数为失败的回调，前面重构`requestData`中有演练过。

```js
const promise = new Promise((resolve, reject) => {
  resolve("request success");
  // reject('request error')
});

promise.then(
  (res) => console.log(res),
  (rej) => console.log(rej)
);

//request success
```

如果只捕获错误，还可以这样写

- 因为第二个参数是捕获异常的，第一个可以写个`null`或`""`占位

```js
const promise = new Promise((resolve, reject) => {
  // resolve('request success')
  reject("request error");
});

promise.then(null, (rej) => console.log(rej));

//request error
```

##### 2.5.1.2 then 的多次调用

```js
const promise = new Promise((resolve, reject) => {
  resolve("hi ice");
});

promise.then((res) => console.log(res));
promise.then((res) => console.log(res));
promise.then((res) => console.log(res));
```

- 调用多次则会执行多次

##### 2.5.1.3 then 的返回值

- `then`方法是有返回值的，它的返回值是`promise`，但是`promise`那它的状态如何决定呢？接下来让我们一探究竟。

**返回一个普通值 _状态:fulfilled_**

```js
const promise = new Promise((resolve, reject) => {
  resolve("hi ice");
});

promise
  .then((res) => ({ name: "ice", age: 22 }))
  .then((res) => console.log(res));

//{name:'ice', age:22}
```

- 返回一个普通值，则相当于主动调用`Promise.resolve`，并且把返回值作为实参传递到`then`方法中。
- 如果没有返回值，则相当于返回`undefined`

**明确返回一个 promise _状态:fulfilled_**

```js
const promise = new Promise((resolve, reject) => {
  resolve("hi ice");
});

promise
  .then((res) => {
    return new Promise((resolve, reject) => {
      resolve("then 的返回值");
    });
  })
  .then((res) => console.log(res));

//then 的返回值
```

主动返回一个`promise`对象，状态和你调用`resolve`，还是`reject`有关

**返回一个 thenable 对象 _状态：fulfilled_**

```js
const promise = new Promise((resolve, reject) => {
  resolve("hi ice");
});

promise
  .then((res) => {
    return {
      then(resolve, reject) {
        resolve("hi webice");
      },
    };
  })
  .then((res) => console.log(res));

//hi webice
```

- 返回了一个 thenable 对象，其状态取决于你是调用了`resolve`,还是`reject`

#### 2.5.2 catch 方法

##### 2.5.2.1 catch 的多次调用

```js
const promise = new Promise((resolve, reject) => {
  reject("ice error");
});

promise.catch((err) => console.log(err));
promise.catch((err) => console.log(err));
promise.catch((err) => console.log(err));

//ice error
//ice error
//ice error
```

##### 2.5.2.2 catch 的返回值

catch 方法是有返回值的，它的返回值是 promise，但是是 promise 那它的状态如何决定呢？接下来让我们一探究竟。  
如果返回值明确一个 promise 或者 thenable 对象，取决于你调用了`resolve`还是`reject`

###### 2.5.2.2.1 返回一个普通对象

```js
const promise = new Promise((resolve, reject) => {
  reject("ice error");
});

promise
  .catch((err) => ({ name: "ice", age: 22 }))
  .then((res) => console.log(res));

//{name:'ice', age: 22}
```

###### 2.5.2.2.2 明确返回一个 promise

```js
const promise = new Promise((resolve, reject) => {
  reject("ice error");
});

promise
  .catch((err) => {
    return new Promise((resolve, reject) => {
      reject("ice error promise");
    });
  })
  .catch((res) => console.log(res));

//ice error promise
```

- 此时`new Promise() `调用了`reject`函数，则会被`catch`捕获到

###### 2.5.2.2.3 返回 thenable 对象

```js
const promise = new Promise((resolve, reject) => {
  reject("ice error");
});

promise
  .catch((err) => {
    return {
      then(resolve, reject) {
        reject("ice error then");
      },
    };
  })
  .catch((res) => console.log(res));

//ice error then
```

#### 2.5.3 finally 方法

- ES9（2018）新实例方法
- finally(最后)，无论 promise 状态是 fulfilled 还是 rejected 都会执行一次`finally`方法

```js
const promise = new Promise((resolve, reject) => {
  resolve("hi ice");
});

promise
  .then((res) => console.log(res))
  .finally(() => console.log("finally execute"));

//finally execute
```

### 2.6 Promise 中的类方法/静态方法

#### 2.6.1 Promise.reslove

```js
Promise.resolve("ice");
//等价于
new Promise((resolve, reject) => resolve("ice"));
```

有的时候，你已经预知了状态的结果为 fulfilled，则可以用这种简写方式

#### 2.6.2 Promise.reject

```js
Promise.reject("ice error");
//等价于
new Promise((resolve, reject) => reject("ice error"));
```

有的时候，你已经预知了状态的结果为 rejected，则可以用这种简写方式

#### 2.6.3 Promise.all

**fulfilled 状态**

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi ice");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi panda");
  }, 2000);
});

const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi grizzly");
  }, 3000);
});

Promise.all([promise1, promise2, promise3]).then((res) => console.log(res));

//[ 'hi ice', 'hi panda', 'hi grizzly' ]
```

all 方法的参数传入为一个可迭代对象，返回一个 promise，只有三个都为`resolve`状态的时候才会调用`.then`方法。  
只要有一个 promise 的状态为 rejected，则会回调`.catch`方法

**rejected 状态**

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi ice");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi panda");
  }, 2000);
});

const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi grizzly");
  }, 3000);
});

Promise.all([promise1, promise2, promise3])
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

//hi panda
```

当遇到 rejectd 的时候，后续的 promise 结果我们是获取不到，并且会把 reject 的实参，传递给 catch 的 err 形参中

#### 2.6.4 Promise.allSettled

上面的`Promise.all`有一个缺陷，就是当遇到一个 rejected 的状态，那么对于后面是`resolve`或者`reject`的结果我们是拿不到的  
ES11 新增语法`Promise.allSettled`，无论状态是 fulfilled/rejected 都会把参数返回给我们

---

**所有 promise 都有结果**

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi ice");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi panda");
  }, 2000);
});

const promise3 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi grizzly");
  }, 3000);
});

Promise.allSettled([promise1, promise2, promise3]).then((res) =>
  console.log(res)
);

/* [
  { status: 'rejected', reason: 'hi ice' },
  { status: 'fulfilled', value: 'hi panda' },
  { status: 'rejected', reason: 'hi grizzly' }
] */
```

该方法会在所有的 Promise 都有结果，无论是 fulfilled，还是 rejected，才会有最终的结果

**其中一个 promise 没有结果**

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi ice");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi panda");
  }, 2000);
});

const promise3 = new Promise((resolve, reject) => {});

Promise.allSettled([promise1, promise2, promise3]).then((res) =>
  console.log(res)
);
// 什么都不打印
```

其中一个 promise 没有结果，则什么都结果都拿不到

#### 2.6.5 Promise.race

- race(竞争竞赛)
- 优先获取第一个返回的结果，无论结果是 fulfilled 还是 rejectd

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi error");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi panda");
  }, 2000);
});

Promise.race([promise1, promise2])
  .then((res) => console.log(res))
  .catch((e) => console.log(e));

//hi error
```

#### 2.6.6 Promise.any

与 race 类似，只获取第一个状态为 fulfilled，如果全部为 rejected 则报错`AggregateError`

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject("hi error");
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("hi panda");
  }, 2000);
});

Promise.any([promise1, promise2])
  .then((res) => console.log(res))
  .catch((e) => console.log(e));

//hi panda
```

## 3. 回调地狱 (进阶)

当我发送网络请求的时候，需要拿到这次网络请求的数据，再发送网络请求，就这样重复三次，才能拿到我最终的结果。

### 3.1 卧龙解法

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

requestData("iceweb.io").then((res) => {
  requestData(`iceweb.org ${res}`).then((res) => {
    requestData(`iceweb.com ${res}`).then((res) => {
      console.log(res);
    });
  });
});

//iceweb.com iceweb.org iceweb.io
```

虽然能够实现，但是多层代码的嵌套，可读性非常差，我们把这种多层次代码嵌套称之为回调地狱

### 3.2 凤雏解法

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

requestData("iceweb.io")
  .then((res) => {
    return requestData(`iceweb.org ${res}`);
  })
  .then((res) => {
    return requestData(`iceweb.com ${res}`);
  })
  .then((res) => {
    console.log(res);
  });

//iceweb.com iceweb.org iceweb.io
```

利用了 then 链式调用这一特性，返回了一个新的 promise，但是不够优雅，思考一下能不能写成同步的方式呢？

### 3.3 生成器+Promise 解法

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

function* getData(url) {
  const res1 = yield requestData(url);
  const res2 = yield requestData(res1);
  const res3 = yield requestData(res2);

  console.log(res3);
}

const generator = getData("iceweb.io");

generator.next().value.then((res1) => {
  generator.next(`iceweb.org ${res1}`).value.then((res2) => {
    generator.next(`iceweb.com ${res2}`).value.then((res3) => {
      generator.next(res3);
    });
  });
});

//iceweb.com iceweb.org iceweb.io
```

大家可以发现我们的`getData`已经变为同步的形式，可以拿到我最终的结果了。那么很多同学会问，generator 一直调用`.next`不是也产生了回调地狱吗？  
其实不用关心这个，我们可以发现它这个是有规律的，我们可以封装成一个自动化执行的函数，我们就不用关心内部是如何调用的了。

### 3.4 自动化执行函数封装

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

function* getData() {
  const res1 = yield requestData("iceweb.io");
  const res2 = yield requestData(`iceweb.org ${res1}`);
  const res3 = yield requestData(`iceweb.com ${res2}`);

  console.log(res3);
}

//自动化执行 async await相当于自动帮我们执行.next
function asyncAutomation(genFn) {
  const generator = genFn();

  const _automation = (result) => {
    let nextData = generator.next(result);
    if (nextData.done) return;

    nextData.value.then((res) => {
      _automation(res);
    });
  };

  _automation();
}

asyncAutomation(getData);

//iceweb.com iceweb.org iceweb.io
```

- 利用 promise+生成器的方式变相实现解决回调地狱问题，其实就是`async await`的一个变种而已
- 最早由 **TJ** 实现，是 JavaScript 社区的知名开发者
- async await 核心代码就类似这些，内部主动帮我们调用`.next`方法

### 3.5 最终解决回调地狱的办法

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

async function getData() {
  const res1 = await requestData("iceweb.io");
  const res2 = await requestData(`iceweb.org ${res1}`);
  const res3 = await requestData(`iceweb.com ${res2}`);

  console.log(res3);
}

getData();

//iceweb.com iceweb.org iceweb.io
```

- 你会惊奇的发现，只要把`getData`生成器函数函数，改为`async`函数，`yeild`的关键字替换为`await`就可以实现异步代码同步写法了。

## 4. async/await 剖析

- async（异步的）
- async 用于申明一个异步函数

### 4.1 async 内部代码同步执行

- 异步函数的内部代码执行过程和普通的函数是一致的，默认情况下也是会被同步执行

```js
async function sayHi() {
  console.log("hi ice");
}

sayHi();

//hi ice
```

### 4.2 异步函数的返回值

- 异步函数的返回值和普通返回值有所区别

  - 普通函数主动返回什么就返回什么，不返回为`undefined`
  - 异步函数的返回值特点
    - 明确有返回一个普通值，相当于`Promise.resolve`(返回值)
    - 返回一个 thenable 对象则由，then 方法中的`resolve`,或者`reject`有关
    - 明确返回一个 promise，则由这个 promise 决定

- 异步函数中可以使用`await`关键字，现在在全局也可以进行`await`，但是不推荐。会阻塞主进程的代码执行

### 4.3 异步函数的异常处理

- 如果函数内部中途发生错误，可以通过 try catch 的方式捕获异常
- 如果函数内部中途发生错误，也可以通过函数的返回值.catch 进行捕获

```js
async function sayHi() {
  console.log(res);
}
sayHi().catch((e) => console.log(e));

//或者

async function sayHi() {
  try {
    console.log(res);
  } catch (e) {
    console.log(e);
  }
}

sayHi();

//ReferenceError: res is not defined
```

### 4.4 await 关键字

- 异步函数中可以使用`await`关键字，普通函数不行
- await 特点
  - 通常 await 关键字后面都是跟一个 Promise
    - 可以是普通值
    - 可以是 thenable
    - 可以是 Promise 主动调用`resolve或者reject`
  - 这个 promise 状态变为 fulfilled 才会执行`await`后续的代码，所以`await`后面的代码，相当于包括在`.then`方法的回调中，如果状态变为 rejected，你则需要在函数内部`try catch`，或者进行链式调用进行`.catch`操作

```js
function requestData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url.includes("iceweb")) {
        resolve(url);
      } else {
        reject("请求错误");
      }
    }, 1000);
  });
}

async function getData() {
  const res = await requestData("iceweb.io");
  console.log(res);
}

getData();

// iceweb.io
```
