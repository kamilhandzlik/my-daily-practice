"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
"""

vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}


# Solution 1
def encode(st):
    result = st
    for vowel, number in vowels.items():
        result = result.replace(vowel, str(number))
    return result


def decode(st):
    result = st
    for vowel, number in vowels.items():
        result = result.replace(str(number), vowel)
    return result


# Solution 2

def encode(st):
    vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    return ''.join(c if c not in vowels else str(vowels[c]) for c in st)


def decode(st):
    vowels = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join(vowels[c] if c in vowels else c for c in st)


# Solution 3
vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

def encode(st):
    return ''.join(str(vowels[c]) if c in vowels else c for c in st)

def decode(st):
    reverse_vowels = {str(v): k for k , v in vowels.items()}
    return ''.join(reverse_vowels[c] if c in reverse_vowels else c for c in st)

# Solution 4
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

print(encode('hello'))
print(decode('h2ll4'))
