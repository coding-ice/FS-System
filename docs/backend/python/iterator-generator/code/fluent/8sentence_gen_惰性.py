from pydoc import text
import re


WORD_RE = re.compile(r'\w+')

class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text

    def __iter__(self):
        # for match in WORD_RE.finditer(self.text):
        #     yield match.group()
        return (match.group() for match in WORD_RE.finditer(self.text))


s = Sentence("Hi ice, Hello World!")

for word in s:
    print(word)
    
print('-------------')

for word in s:
    print(word)