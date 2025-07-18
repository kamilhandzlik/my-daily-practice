"""
In this Kata, you will implement a function count that takes an integer and returns the number of digits in factorial(n).

For example, count(5) = 3, because 5! = 120, and 120 has 3 digits.

More examples in the test cases.

Brute force is not possible. A little research will go a long way, as this is a well known series.

Good luck!
"""


# This works but not for this kata author want you to be able to use this code upon numbers large enough to exceed
# limit (4300 digits) for integer string conversion.
def count(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return len(str(result))


# Instead use une of this
# Solution 1
import math


def count(n):
    if n == 0 or n == 1:
        return 1
    digits = sum(math.log10(i) for i in range(2, n + 1))
    return math.floor(digits) + 1


# Solution 1
from math import *


def count(n):
    return ceil(lgamma(n + 1) / log(10))


print(count(5000))
