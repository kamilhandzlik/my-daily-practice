"""
Find Nearest square number

Your task is to find the nearest square number of a positive integer n. In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

For example, if n = 111, then the nearest square number equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If n is already a perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)

Check my other katas:

Alphabetically ordered

Case-sensitive!

Not prime numbers

Find your caterer
"""


# Solution 1
def nearest_sq(n):
    root = round(n ** 0.5)
    return root * root


# Solution 2
def nearest_sq(n):
    return round(n ** 0.5) ** 2


print(nearest_sq(10))
