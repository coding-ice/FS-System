/**
 * 1. 构造器接受一个 executor
 * 2. 定义变量 status / value / reason / onFulfilledCbs / onRejectedCbs
 * 3. 向 executor 传递 resolve，reject（要箭头函数，不然会有 this 指向的问题）
 * 4. resolve reject 分别接受 value / reason （异步执行， onFulfilledCbs / onRejectedCbs）
 * 5. 当执行 then 函数，分别接受 成功/失败的 cb，往队列中 push，然后分别执行
 */
class ICEPromise {
  constructor(executor) {
    this.status = "PENDING";
    this.value = undefined;
    this.reason = undefined;
    this.onFulfilledCbs = [];
    this.onRejectedCbs = [];

    const resolve = (value) => {
      if (this.status === "PENDING") {
        this.status = "FULFILLED";
        this.value = value;

        setTimeout(() => {
          this.onFulfilledCbs.forEach((fn) => fn(value));
        });
      }
    };

    const reject = (reason) => {
      if (this.status === "PENDING") {
        this.status = "REJECTED";
        this.reason = reason;

        setTimeout(() => {
          this.onRejectedCbs.forEach((fn) => fn(reason));
        });
      }
    };

    try {
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  then(onFulfilled, onRejected) {
    this.onFulfilledCbs.push(onFulfilled);
    this.onRejectedCbs.push(onRejected);
  }
}

const p = new ICEPromise((resolve, reject) => {
  // resolve(1);
  reject(2);
});

p.then(
  (value) => {
    console.log("res1: ", value);
  },
  (err) => {
    console.log("err1:", err);
  }
);

p.then(
  (value) => {
    console.log("res2: ", value);
  },
  (err) => {
    console.log("err2:", err);
  }
);
