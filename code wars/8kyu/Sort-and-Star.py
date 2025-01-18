"""
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
"""


# Solution 1
def two_sort(array):
    array_sorted = sorted(array)
    first_element = array_sorted[0]
    return '***'.join(first_element)


# Solution 2
def two_sort(lst):
    return '***'.join(min(lst))
