"""
for in 和迭代器的关系

大白话：
    for in 先问“谁能负责一个个取元素？”，再不断问“下一个元素是什么？”。

    1. iter(stus) 会调用 stus.__iter__()
    2. __iter__ 返回 self，意思是：stus 自己就是那个负责取下一个元素的迭代器
    3. next(stus) 会调用 stus.__next__()
    4. __next__ 每次返回一个元素；没有元素时抛出 StopIteration，for 循环结束

因此，下面这段 for in：

    for stu in stus:
        print(stu)

大致等价于：

    iterator = iter(stus)  # 即 stus.__iter__()，返回 stus 自己
    while True:
        try:
            stu = next(iterator)  # 即 stus.__next__()
            print(stu)
        except StopIteration:
            break
"""


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0  # 记录已经取到第几个元素

    def __iter__(self):
        # 我自己有 data、也有 index、也能执行 __next__，所以迭代器就是我自己。
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result


stus = MyIterator(["ice", "panda", "kitty"])

for stu in stus:
    print(stu)

# 等价写法：
# iterator = iter(stus)  # iterator 就是 stus 本人
# while True:
#     try:
#         stu = next(iterator)
#         print(stu)
#     except StopIteration:
#         break

