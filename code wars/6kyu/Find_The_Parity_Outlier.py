"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""


# Solution 1
def find_outlier(integers):
    even = []
    odd = []

    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even[0] if len(even) == 1 else odd[0]


# Solution 2 - optimized version
def find_outlier(integers):
    sample = integers[:3]
    even_count = sum(1 for x in sample if x % 2 == 0)

    if even_count >= 2:
        return next(x for x in integers if x % 2 != 0)
    else:
        return next(x for x in integers if x % 2 == 0)


# Solution 3
def find_outlier(integers):
    even = [i for i in integers if i % 2 ==0]
    odd = [i for i in integers if i % 2 !=0]
    return even[0] if len(even) == 1 else odd[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
