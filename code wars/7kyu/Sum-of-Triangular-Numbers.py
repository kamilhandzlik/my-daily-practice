"""
Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."

[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]
e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.

Triangular Numbers cannot be negative so return 0 if a negative number is given.
"""

# Solution 1
def sum_triangular_numbers(n):
    list_of_triangular_numbers = []

    for num in range(1, n + 1):
        triangular_number = num * (num + 1) / 2
        list_of_triangular_numbers.append(triangular_number)

    result = sum(list_of_triangular_numbers)
    return result


# Solution 2
def sum_triangular_numbers(n):
    return sum([num * (num + 1) / 2 for num in range(1, n + 1)])


# Solution 3 if you want to check if n different than 0 and n > 0 exercise does not require you to do this
def sum_triangular_numbers(n):
    if n < 1:
        return 0
    return sum([num * (num + 1) / 2 for num in range(1, n + 1)])

print(sum_triangular_numbers(6))
