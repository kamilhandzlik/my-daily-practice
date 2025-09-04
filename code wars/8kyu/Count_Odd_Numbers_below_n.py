"""
Given a number n, return the number of positive odd numbers below n, EASY!

Examples (Input -> Output)
7  -> 3 (because odd numbers below 7 are [1, 3, 5])
15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])
Expect large Inputs!
"""


# This is one way of doing it but triggers "Execution Timed Out (12000 ms)" because it has 2 loops
def odd_count(n):
    return len([i for i in range(n) if i % 2 != 0])


# This is one will also trigger "Execution Timed Out (12000 ms)" because it's inefficient
def odd_count(n):
    result = 0
    for i in range(n):
        if i % 2 != 0:
            result += 1
    return result


# Solution it does not use loops and even and odd numbers split range evenly so yeah
def odd_count(n):
    return n // 2


print(odd_count(15023))
