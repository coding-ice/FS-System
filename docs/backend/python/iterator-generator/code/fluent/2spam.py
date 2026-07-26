from collections import abc
from dataclasses import dataclass

s = [1,2]

class Spam:
    def __init__(self):
        pass

    def __getitem__(self, index):
        print(f"{index=}")
        raise IndexError(f"Index {index} is out of range")
        # return self.data[index]

@dataclass
class Person:
    name: str
    age: int


s = Spam()
p = Person("ice", 18)

print(iter(s)) # getitem 兼容于 iter 协议
print(list(s))
print(isinstance(s, abc.Iterable)) # 按照是否有 iter 方法来判断是否是可迭代对象

# print(iter(p)) # Person is not iterator