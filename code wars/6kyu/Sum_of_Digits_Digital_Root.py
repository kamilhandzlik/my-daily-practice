"""
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


user578387

https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
"""

# Solution 1
def digital_root(n):
    y = sum([int(i) for i in str(n)])
    x = 0

    if y <= 9:
        return y
    else:
        while y > 9:
            x = sum([int(i) for i in str(y)])
            y = x
    return x

# Solution 2
def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(int(i) for i in str(n)))

# Solution 3
def digital_root(n):
    return 1 + (n - 1) % 9 if n > 0 else 0


print(digital_root(942))
