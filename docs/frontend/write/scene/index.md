# 应用场景

## 限制网络并发数量

```js
function createConcurrencyLimiter(maxConcurrency) {
  const queue = [];
  let running = 0;

  async function run() {
    if (running >= maxConcurrency || queue.length === 0) return;

    const { task, resolve, reject } = queue.shift();
    running++;

    try {
      const result = await task();
      resolve(result);
    } catch (err) {
      reject(err);
    } finally {
      running--;
      run();
    }
  }

  return function enqueue(task) {
    return new Promise((resolve, reject) => {
      queue.push({ task, resolve, reject });
      run();
    });
  };
}

const runWithLimit = createConcurrencyLimiter(5);

const urls = Array(100)
  .fill()
  .map((_, i) => `https://jsonplaceholder.typicode.com/posts/${i + 1}`);

const promises = urls.map((url) =>
  runWithLimit(() => fetch(url).then((r) => r.json()))
);

const results = await Promise.allSettled(promises);

console.log("完成:", results.filter((r) => r.status === "fulfilled").length);
```

**核心思路**

- 控制 promise 何时执行，应顺序的受限（不能超过最大并发数量）的执行
- 利用 队列 + promise 控制最大数量即可
