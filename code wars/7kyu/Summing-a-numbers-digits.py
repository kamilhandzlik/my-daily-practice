"""
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)

10 --> 1
99 --> 18
-32 --> 5
Let's assume that all numbers in the input will be integer values.
"""

# Solution 1
def sum_digits(number):
    j = []
    for i in str(number):
        if i in '0123456789':
            j.append(int(i))
    return sum(j)


# Solution 2
def sum_digits(number):
    return sum([int(i) for i in str(number) if i in '0123456789'])