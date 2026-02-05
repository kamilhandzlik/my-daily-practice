"""
A disguised sequence (I)

g964
https://www.codewars.com/kata/563f0c54a22b9345bf000053/train/python
"""


def fcn(n):
    if n == 0:
        return 1
    return  3 * (2 ** (n -1))