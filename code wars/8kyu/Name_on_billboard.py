"""
Name on billboard

You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1 (always 2 for Java).

You can not use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 letters * 30 = 600 (Space counts as a character).

val_alex
https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python
"""


# Solution 1
def billboard(name, price=30):
    return sum([price for _ in range(len(name))])


# Solution 2
def billboard(name, price=30):
    return sum(price for _ in name)


# Solution 3
def billboard(name, price=30):
    total = 0
    for _ in name:
        total += price
    return total


# Solution 4
def billboard(name, price=30):
    total = 0
    i = 0
    while i < len(name):
        total += price
        i += 1
    return total


# Solution 4
from functools import reduce


def billboard(name, price=30):
    return reduce(lambda acc, _: acc + price, name, 0)
