"""
Sum of many ints

Write this function (image in the link
https://www.codewars.com/kata/54c2fc0552791928c9000517/train/python

for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
You'll need to get a little clever with performance, since n can be a very large number
"""


# This will not work
def f(n, m):
    return sum([i % m for i in range(1, n + 1)])

# Solution 1
def f(n, m):
    full_cycle = n // m
    remainder = n % m

    cycle_sum = m * (m-1) // 2
    return full_cycle * cycle_sum + remainder * (remainder + 1) // 2

# Solution 2
def f(n, m):
    return (n // m) * (m * (m-1) // 2) + (n % m) * (n % m + 1) // 2