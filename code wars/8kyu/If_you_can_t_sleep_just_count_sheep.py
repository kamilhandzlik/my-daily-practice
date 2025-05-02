"""
If you can't sleep, just count sheeps!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


"""


# Solution 1
def count_sheep(n):
    result = ''
    for i in range(1, n + 1):
        result += f"{i} sheep..."

    return result


# Solution 2
def count_sheep(n):
    return ''.join((f"{i} sheep..." for i in range(1, n + 1)))