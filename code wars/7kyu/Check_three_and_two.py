"""
Check three and two

Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran, Chars in Haskell), check if the array contains three and two of the same values.

Examples
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"

"""


# Solution 1
def check_three_and_two(array):
    result = ''
    for i in set(array):
        if array.count(i) == 2:
            result += '2'
        elif array.count(i) == 3:
            result += '3'
    return result == '32' or result == '23'


# Solution 2
from collections import Counter


def check_three_and_two(array):
    counts = Counter(array).values()
    return sorted(counts) == [2, 3]


# Solution 3
def check_three_and_two(array):
    return len(set(array)) == 2 and {array.count(x) for x in set(array)} == {2, 3}


# Solution 4
def check_three_and_two(array):
    return sorted(list(map(array.count, set(array)))) == [2, 3]
