import re


RE_WORD = re.compile(r'\w+')


"""
    糟糕的, 从可迭代对象的角度来看
        每次调用 iter 都应该是返回一个新的迭代器对象
"""

# class Sentence:
#     def __init__(self, text: str) -> None:
#         self.text = text
#         self.words = RE_WORD.findall(text)
#         self.index = 0

#     def __iter__(self):
#         return self

    
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         result = self.words[self.index]
#         self.index += 1
#         return result


# s = Sentence("Hi ice, Hello World!")

# it1 = iter(s)
# it2 = iter(s)
# print(it1.__dict__)
# print(it2.__dict__)
# print(it1 == it2)

# for word in s:
#     print(word)

# for word in s:
#     print(word)