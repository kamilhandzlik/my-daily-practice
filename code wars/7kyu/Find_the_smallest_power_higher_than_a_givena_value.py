"""
Find the smallest power higher than a given a value

We have the number 12385 . We want to know the value of the closest cube but higher than 12385. The answer will be 13824 .

Now, another case. We have the number 1245678 . We want to know the 5th power, closest and higher than that number. The value will be 1419857.

We need a function that receives two arguments, a value val , and the exponent of the power,  pow_ , and outputs the value that we want to find.

Let'see some cases:

(12385, 3) ==> 13824
(1245678, 5) ==> 1419857
The value, val will be always a positive integer.

The power, pow_ , always higher than 1 .

Happy coding!!
"""
from math import ceil


# Solution 1
def find_next_power(val, pow_):
    root = val ** (1 / pow_)
    next_int = ceil(root)
    return next_int ** pow_


# Solution 2
def find_next_power(val, pow_):
    return ceil(val ** (1 / pow_)) ** pow_

# Solution 3 or without using math library
def find_next_power(val, pow_):
    return int(val ** (1.0 / pow_) + 1) ** pow_


print(f"output:{find_next_power(12385, 3)} expected: 13824")
