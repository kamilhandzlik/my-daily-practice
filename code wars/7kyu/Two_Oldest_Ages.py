"""
Two Oldest Ages

he two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]


jhoffner
https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python
"""

# Solution 1 XD
def two_oldest_ages(ages):
    result = []
    oldest = max(ages)
    result.append(oldest)
    ages.remove(oldest)
    sec = max(ages)
    result.append(sec)

    return result[::-1]


# Solution 2
def two_oldest_ages(ages):
    return sorted(ages)[-2:]

# Solution 3
def two_oldest_ages(ages):
    oldest = second = float("-inf")

    for age in ages:
        if age > oldest:
            second = oldest
            oldest = age
        elif age > second:
            second = age

    return [second, oldest]

# Solution 4
import heapq

def two_oldest_ages(ages):
    return heapq.nlargest(2, ages)[::-1]


# Solution 4 without sorted and max
def two_oldest_ages(ages):
    a, b = ages[0], ages[1]

    if a < b:
        a, b = b, a

    for age in ages[2:]:
        if age > a:
            b = a
            a = age
        elif age > b:
            b = age

    return [b, a]