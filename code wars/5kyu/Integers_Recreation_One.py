"""
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".
"""
import math

# Solution 1 - version slow as f*** may return Timed out
def list_squared(m, n):
    result = []

    for num in range(m, n+1):
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i**2)
        total = sum(divisors)
        if math.isqrt(total)**2 == total:
            result.append([num, total])

    return result

# Solution 2
def list_squared(m, n):
    result = []

    for num in range(m, n + 1):
        sum_of_squares = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_of_squares += i ** 2
                if i != num // i:
                    sum_of_squares += (num // i) ** 2

        if math.isqrt(sum_of_squares) ** 2 == sum_of_squares:
            result.append([num, sum_of_squares])

    return result


print(list_squared(1, 250))