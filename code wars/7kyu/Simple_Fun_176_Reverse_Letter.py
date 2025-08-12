"""
Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string
"""
import re


def reverse_letter(st):
    return ''.join(re.findall('[a-zA-Z]', st)[::-1])


print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
