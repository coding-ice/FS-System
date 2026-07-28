# 生成器

函数体中出现 `yield` 时，它是生成器函数。调用函数不会立即执行函数体，而是返回生成器对象；生成器本身就是迭代器。

<<< @/backend/python/iterator-generator/code/6generator.py

每次调用 `next(gen)`，生成器从上次暂停处继续，运行到下一个 `yield` 后再次暂停并产出值。函数结束后生成器耗尽，不能重新开始。

## 用生成器实现 `__iter__`

生成器可以代替手写的迭代器类：

<<< @/backend/python/iterator-generator/code/7sentence_gen_first.py

每次 `iter(sentence)` 都会创建新的生成器，因此同一个 `Sentence` 可以重复遍历。

## 惰性产生结果

`findall()` 会先创建完整的匹配列表；`finditer()` 配合生成器会按需产生每个匹配结果：

<<< @/backend/python/iterator-generator/code/8sentence_gen_惰性.py

适合大文件、流式数据和计算成本较高的数据。

## 生成器表达式

生成器表达式使用圆括号，结果按需产生；列表推导会立即创建完整列表。

```python
squares = (x * x for x in range(5))
```
