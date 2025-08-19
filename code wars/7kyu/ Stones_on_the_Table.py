"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colors.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
"""


# Solution 1
def solution(stones):
    result = 0

    for i, j in enumerate(stones):
        if i == len(stones) - 1:
            break
        elif j == stones[i + 1]:
            result += 1
    return result


# Solution 2
def solution(stones):
    return sum(a == b for a, b in zip(stones, stones[1:]))


# Solution 3
from itertools import pairwise


def solution(stones):
    return sum(a == b for a, b in pairwise(stones))


print(solution("RGBRGBRGGB"))
print(solution("RRRRGGGGBBBB"))
