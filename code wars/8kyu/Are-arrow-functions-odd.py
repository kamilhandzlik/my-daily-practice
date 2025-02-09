"""
Time to test your basic knowledge in functions! Return the odds from a list:

[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
"""

# Solution 1
odds = lambda lst: [x for x in lst if x % 2 != 0]

# Solution 2
odds = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
