"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""


# Solution 1
def stray(arr):
    return list(set(arr))[0] if arr.count(list(set(arr))[0]) == 1 else list(set(arr))[1]


# Solution 2
from collections import Counter


def stray(arr):
    return next(num for num, count in Counter(arr).items() if count == 1)


print(stray([1, 1, 1, 1, 1, 1, 2]))
