# 迭代器

可迭代对象负责提供迭代器；迭代器负责逐个产出值。

- `iter(obj)`：从可迭代对象取得迭代器。
- `next(it)`：取得下一个值；耗尽时抛出 `StopIteration`。
- `for x in obj` 会自动重复调用这两个步骤。

迭代器会被消耗。可迭代对象每次调用 `iter()` 应返回新的迭代器，才能从头重复遍历。

## 手写迭代器

数据容器不保存遍历位置；迭代器保存游标。这样多个迭代器互不影响：

<<< @/backend/python/iterator/code/9sentence_iter_good.py

`SentenceIterator.__iter__()` 返回自身，因为它已经是迭代器；`Sentence.__iter__()` 返回新的 `SentenceIterator`，因为它是可重复遍历的数据容器。
