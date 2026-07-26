function throttle(fn, delay) {
  // 1. 上一次执行的时间
  let lastTime = 0;

  return function (...args) {
    // 2. 每次调用这个函数，获取最新的时间
    const now = Date.now();
    // 3. 当前时间 - 上一次的时间 >= 应等待的时间
    if (now - lastTime >= delay) {
      // 4. 执行传递的函数，并绑定 this
      const result = fn.apply(this, args);
      // 5. 上一次执行的时间 为当前时间
      lastTime = now;
      // 6. 返回返回值
      return result;
    }
  };
}

const throttled = throttle(function () {
  console.log("hi throttle");
}, 3000);

setInterval(() => {
  throttled();
}, 500);
