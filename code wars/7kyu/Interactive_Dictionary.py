"""
Interactive Dictionary

In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

 d = Dictionary()

 d.newentry('Apple', 'A fruit that grows on trees')

 print(d.look('Apple'))
A fruit that grows on trees

print(d.look('Banana'))
Can't find entry for Banana
Good luck and happy coding!
"""


class Dictionary():
    def __init__(self):
        self.dictionary = {}

    def newentry(self, word, definition):
        self.dictionary[word] = definition

    def look(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        return f"Can't find entry for {key}"
