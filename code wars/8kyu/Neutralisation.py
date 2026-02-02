"""
Neutralisation

Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
"""


# Solution 1 XD
def neutralise(s1, s2):
    s11 = [i for i in s1]
    s22 = [i for i in s2]
    result = []

    for i in range(len(s1)):
        if s11[i] == '+' and s22[i] == '+':
            result.append('+')
        elif s11[i] == '-' and s22[i] == '+' or s11[i] == '+' and s22[i] == '-':
            result.append('0')
        else:
            result.append('-')

    return ''.join(result)


# Solution 2
def neutralise(s1, s2):
    result = []

    for a, b in zip(s1, s2):
        if a == b:
            result.append(a)
        else:
            result.append('0')
    return ''.join(result)


# Solution 3
def neutralise(s1, s2):
    return ''.join([a if a == b else '0' for a, b in zip(s1, s2)])
