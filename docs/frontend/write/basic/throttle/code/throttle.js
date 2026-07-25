function throttle(fn, wait, options = {}) {
  // 1. 定义 options
  const { leading = true, trailing = true } = options;
  // 2. 上一次执行 fn 的时间戳
  let lastTime = 0;
  // 3. 尾部的定时器变量
  let timer = null;

  return function (...args) {
    // 4. 执行截流后的函数，每次拿到最新的时间戳
    const now = Date.now();
    // 5. 是否达到了间隔时间
    if (now - lastTime >= wait) {
      // 6. 头部是否执行
      if (leading) {
        fn.apply(this, args);
      }
      lastTime = now;
    }

    // 7. 尾部需要执行 & timer 没值的情况 & 不是头部需要执行
    if (trailing && !timer && !leading) {
      // 8. 开启定时器
      timer = setTimeout(() => {
        // 9. 执行函数
        fn.apply(this, args);
        // 10. 清空定时器
        timer = null;
      }, wait);
    }
  };
}
