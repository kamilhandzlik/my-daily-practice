"""
Array element parity

In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.

Examples:

[1, -1, 2, -2, 3] => 3

3 has no matching negative appearance

[-3, 1, 2, 3, -1, -4, -2] => -4

-4 has no matching positive appearance

[1, -1, 2, -2, 3, 3] => 3

(the only-positive or only-negative integer may appear more than once)

Good luck!
"""

# Solution 1
def solve(arr):
    for i in set(arr):
        if arr.count(i) == 0:
            return -i
        elif arr.count(-i) == 0:
            return i

# Solution 2
def solve(arr):
    for i in set(arr):
        if -i not in set(arr):
            return i


# Solution 3
from collections import Counter

def solve(arr):
    counts = Counter(arr)
    for i in counts:
        if -i not in counts:
            return i


# Solution 4
def solve(arr):
    return next(i for i in set(arr) if -i not in arr)