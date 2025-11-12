"""
Alternate capitalization

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
"""


# Solution 1
def capitalize(s):
    res_1 = ''
    res_2 = ''

    for i, letter in enumerate(s):
        if i % 2 == 0 or i == 0:
            res_1 += letter.upper()
            res_2 += letter
        else:
            res_1 += letter
            res_2 += letter.upper()

    return [res_1, res_2]


# Solution 2
def capitalize(s):
    res_1 = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    res_2 = ''.join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(s)])
    return [res_1, res_2]


# Solution 3
def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


print(capitalize("abcdef"))
