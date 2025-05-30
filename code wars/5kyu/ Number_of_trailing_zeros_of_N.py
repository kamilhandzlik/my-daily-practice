"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
N	Product	N factorial	Trailing zeros
6	1*2*3*4*5*6	720	1
12	1*2*3*4*5*6*7*8*9*10*11*12	479001600	2
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""

# Solution 1 (it works but codewars will return out of time! So lets make it better!)XD
def factorial(n):
    count = n
    result = n
    while count != 1:
        count -= 1
        result *= count
    return result



def zeros(n):
    prod = factorial(n)
    current = ''
    count = 0
    for i in str(prod)[::-1]:
        current = i
        if current != "0":
            break
        else:
            count += 1
    return count


# Solution 2
"""
How it works?
Zeroes at the end of the numbers are made through divides of 10 = 2 * 5.
In n! that is multiple of numbers in range 1 to n there are a lot of 2 and 5. But there are more2 than 5.
1. Divides of 5 in range 100
 100 // 5 = 20
We have 20 fives in range 1-100
2. Divides of 25
Some numbers have more than one 5 as divider
25 = 5 × 5 → 2 fives

50 = 2 × 5 × 5 → also 2 fives

75 = 3 × 5 × 5

100 = 2 × 2 × 5 × 5
So we have to add number of this numbers  that have second 5 so
100 // 5 = 20 → base fives

100 // 25 = 4 → second fives

100 // 125 = 0 → don't have third fives
"""
def zeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


