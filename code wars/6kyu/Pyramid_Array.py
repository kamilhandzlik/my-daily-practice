"""
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]
"""


# Solution 1
def pyramid(n):
    result = []

    for i in range(1, n + 1):
        current = []
        for _ in range(1, i + 1):
            current.append(1)
        result.append(current)

    return result


# Solution 2
def pyramid(n):
    result = []

    for i in range(1, n + 1):
        result.append([1] * i)

    return result


# Solution 3
def pyramid(n):
    return [[1] * i for i in range(1, n + 1)]


print(pyramid(3))
