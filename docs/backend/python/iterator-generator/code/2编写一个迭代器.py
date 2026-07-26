import re


WORD_RE = re.compile(r"\w+")


class Sentence:
    """可迭代对象：保存数据，并在需要时创建迭代器。"""

    def __init__(self, text: str) -> None:
        self.words = WORD_RE.findall(text)

    def __iter__(self):
        # 每次都返回新的迭代器，让不同的遍历互不影响。
        return SentenceIterator(self.words)


class SentenceIterator:
    """迭代器对象：保存本次遍历的进度，并产出下一个单词。"""

    def __init__(self, words: list[str]) -> None:
        self.words = words
        self.index = 0

    def __iter__(self):
        # 迭代器本身也是可迭代对象。
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration

        word = self.words[self.index]
        self.index += 1
        return word


sentence = Sentence("Hi ice, Hello World!")

first_iterator = iter(sentence)
second_iterator = iter(sentence)
print(first_iterator is second_iterator)  # False：每次都会创建新的迭代器

print(next(first_iterator))  # Hi
print(next(first_iterator))  # ice

# sentence 是可迭代对象，因此可以从头遍历多次。
for word in sentence:
    print(word)

for word in sentence:
    print(word)

# first_iterator 是迭代器；它会从当前位置继续，并且耗尽后不能自动重置。
for word in first_iterator:
    print(word)  # Hello、World

for word in first_iterator:
    print(word)  # 没有输出
