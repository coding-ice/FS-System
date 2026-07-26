from dataclasses import dataclass
import re
import reprlib


RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f"Sentence({self.text})"


s = Sentence("Hi ice, Hello World!")
# print(s[0])
# print(s[1])
# print(s[2])

@dataclass
class Person:
    name: str
    age: int

p = Person("ice", 18)

for i in p:
    print(i)

# for word in s:
#     print(word)