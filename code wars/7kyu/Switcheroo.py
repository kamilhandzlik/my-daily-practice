"""
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""


# Solution 1
def switcheroo(s):
    result = ''
    for i in s:
        if i == 'a':
            result += 'b'
        elif i == 'b':
            result += 'a'
        else:
            result += i
    return result



# Solution 2
def switcheroo(s):
    return ''.join('b' if i == 'a' else 'a' if i == 'b' else i  for i in s)

