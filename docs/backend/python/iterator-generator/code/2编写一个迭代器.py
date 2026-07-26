"""
迭代器一定是一个可迭代对象
可迭代对象不一定是迭代器

"""

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        result = self.data[self.index]
        self.index += 1
        return result


stus = MyIterator(["ice", "panda", "kitty"])
stu2 = MyIterator(["1", "2", "3"])

for stu in stus:
    print(stu)

# 再次遍历, 会发现没有输出, 因为迭代器已经遍历完了
for stu in stus:
    print(stu)
