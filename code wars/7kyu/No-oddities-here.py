"""
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

# Solution 1
def no_odds(values):
    i = []
    for n in values:
        if n % 2 == 0:
            i.append(n)
    return  i

# Solution 2
def no_odds(values):
    return [n for n in values if n % 2 == 0]