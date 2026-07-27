import re


WORD_RE = re.compile(r'\w+')

class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self.words = WORD_RE.findall(text)

    def __iter__(self):
        return SentenceIterator(self.words, 0)


class SentenceIterator:
    def __init__(self, words: list[str], index: int) -> None:
        self.words = words
        self.index = index
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        result = self.words[self.index]
        self.index += 1
        return result

s = Sentence("Hi ice, Hello World!")

it1 = iter(s)

# for word in s:
#     print(word)

# for word in s:
#     print(word)


for word in it1:
    print(word)

for word in it1:
    print(word)