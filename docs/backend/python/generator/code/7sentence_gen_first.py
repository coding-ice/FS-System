import re


WORD_RE = re.compile(r'\w+')

class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self.words = WORD_RE.findall(text)

    def __iter__(self):
        for word in self.words:
            yield word


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