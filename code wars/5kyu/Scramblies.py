"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
from collections import Counter


def scramble(s1, s2):
    return not (Counter(s2) - Counter(s1))

# Solution 2
def scramble(s1, s2):
    for char in set(s2):
        if s2.count(char) > s1.count(char):
            return False
    return True



print(scramble('cedewaraaossoqqyt', 'codewars'))