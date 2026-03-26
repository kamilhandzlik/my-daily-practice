"""
All unique

Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

pinelopi
https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python
"""


# Solution 1
def has_unique_chars(string):
    return len(string) <= len(set(string))


# Solution 2
def has_unique_chars(string):
    return len(string) == len(set(string))


# Solution 3
def has_unique_chars(string):
    seen = set()
    for ch in string:
        if ch in seen:
            return False
        seen.add(ch)
    return True
