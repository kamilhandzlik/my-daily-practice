"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

# Solution 1
def pig_it(text):
    words = text.split(" ")
    new_words = []
    for word in words:
        if word in "?!@#$%^&*().":
            new_words.append(word)
        else:
            new_words.append((word[1:] + word[0] + "ay"))
    return " ".join(new_words)

def pig_it(text):
    return " ".join([word  if word in ".?!" else word[1:] + word[0] + "ay" for word in text.split(" ")])

print(pig_it('Pig latin is cool'))
print(pig_it("Quis custodiet ipsos custodes ?"))