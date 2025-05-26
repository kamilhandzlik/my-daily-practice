"""
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"

"""

# Solution 1
def spin_words(sentence):
    result = []
    for word in sentence.split(" "):
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)

# Solution 2
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])