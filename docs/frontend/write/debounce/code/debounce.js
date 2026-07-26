function debounce(fn, delay, immediate) {
  // 1. 记录 timer，用于清除定时器
  let timer = null;

  // 2. 返回一个新的被防抖过的函数
  return function (...args) {
    // 3. 如果多次调用该函数，会清除上一次的定时器
    if (timer) clearTimeout(timer);

    // 4. 如果是立即执行的，主动调用一次 fn
    if (immediate) {
      fn.apply(this, args);
      immediate = false;
    }

    // 5. 开启一个定时器，delay 达到后，开始执行
    timer = setTimeout(() => {
      fn.apply(this, args);
      timer = null;
    }, delay);
  };
}

const debounced = debounce(function () {
  console.log("debounced");
}, 3000);

// 连续调用了 5 次，实际调用只有一次
debounced();
debounced();
debounced();
debounced();
debounced();
