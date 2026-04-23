"""
Combining N Ratios

This is a more difficult version of this kata - I suggest solving that kata before attempting this one.

Task
Your task is similar to the kata above, however now you are not limited to only 2 sets of ratios - you will be given an array of ratios as strings, and you must return a combined ratio in its simplest form, as a string. See the example below:

Example:

ratio_combinator(["12:4","3:7","24:30"]) -> '36:12:28:35'
The given input ratios may not be in their simplest form, and the inputs range from
[1,10^5][1,105] (1 to 1e5 inclusive).


AbdisamadAbdi
https://www.codewars.com/kata/69e4c22bd10a363dd5b75a7f/train/python
"""

from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def ratio_combinator(ratios):
    pairs = [list(map(int, r.split(":"))) for r in ratios]

    result = [pairs[0][0]]
    current = pairs[0][1]

    for a, b in pairs[1:]:
        common = lcm(current, a)

        factor_current = common // current
        result = [x * factor_current for x in result]

        factor_a = common // a
        result.append(common)
        current = b * factor_a


    result.append(current)

    common_gcd = reduce(gcd, result)
    result = [x // common_gcd for x in result]

    return ":".join(map(str, result))