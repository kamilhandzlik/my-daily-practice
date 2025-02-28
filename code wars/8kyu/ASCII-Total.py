"""
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

Examples:

uniTotal("a") == 97
uniTotal("aaa") == 291
"""


def uni_total(s):
    if s == '':
        return 0
    result = 0
    for i in s:
        result += ord(i)
    return result