"""
Reverse every other word in the string

Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

Confettimaker
https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python
"""


# Solution 1
def reverse_alternate(st):
    arr = st.strip().split()
    result = []

    for i, j in enumerate(arr):
        if (i + 1) % 2 == 0:
            result.append(j[::-1])
        else:
            result.append(j)

    return ' '.join(result)


# Solution 2
def reverse_alternate(st):
    return ' '.join([j[::-1] if (i + 1) % 2 == 0 else j for i, j in enumerate(st.strip().split())])


print(reverse_alternate('This       is a  test '))
