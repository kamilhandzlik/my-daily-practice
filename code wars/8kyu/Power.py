"""
The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power times).

Examples
number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
number_to_pwr(10, 6) # -> 1000000
Note: math.pow and some others math functions are disabled on final tests.
"""


# Solution 1
def number_to_pwr(number, p):
    if p == 0:
        return 1

    result = number
    for _ in range(p - 1):
        result *= number
    return result

# Solution 2
def number_to_pwr(number, p):
    result = 1
    for i in range(p):
        result *= number
    return result

# Solution 3
# Technically this is easiest but this kata does not allow it
# No ** allowed: False should equal True
def number_to_pwr(number, p):
    return number ** p

