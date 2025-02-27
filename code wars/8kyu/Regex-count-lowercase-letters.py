"""
our task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26
"""


# Solution 1
def lowercase_count(strng):
    a = ""
    for i in strng:
        if i in "abcdefghijklmnqoprstuvwxyz":
            a += i
    return len(a)

# Solution 2
def lowercase_count(strng):
    return len(''.join(i for i in strng if i in "abcdefghijklmnqoprstuvwxyz"))


# Solution 3
import re


def lowercase_count(strng):
    return len(re.findall("[a-z]", strng))