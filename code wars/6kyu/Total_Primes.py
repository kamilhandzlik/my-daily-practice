"""
Total Primes

The number 23 is special in the sense that all of its digits are prime numbers. Furthermore, it's a prime itself. There are 4 such numbers between 10 and 100: 23, 37, 53, 73. Let's call these numbers "total primes".

Complete the function that takes a range (a, b) and returns the number of total primes within that range (a <= primes < b). The test ranges go up to 107.

Examples
(10, 100)  ==> 4  # 23, 37, 53, 73
(500, 600) ==> 3  # 523, 557, 577
Happy coding!

Mcoury
https://www.codewars.com/kata/5a516c2efd56cbd7a8000058/train/python
"""

from bisect import bisect_left
from math import sqrt

PRIME_DIGITS = {'2', '3', '5', '7'}


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    r = int(sqrt(n))

    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


TOTAL_PRIMES = []


def generate_total_primes(limit=10_000_000):
    stack = ['2', '3', '5', '7']

    while stack:
        s = stack.pop()
        n = int(s)

        if n > limit:
            continue
        if is_prime(n):
            TOTAL_PRIMES.append(n)

        for d in PRIME_DIGITS:
            stack.append(s + d)


generate_total_primes()
TOTAL_PRIMES.sort()


def get_total_primes(a, b):
    return bisect_left(TOTAL_PRIMES, b) - bisect_left(TOTAL_PRIMES, a)
