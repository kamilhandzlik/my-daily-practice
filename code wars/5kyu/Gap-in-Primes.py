"""
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise `nil or null or None or Nothing (or ... depending on the language).

In such a case (no pair of prime numbers with a gap of `g`)
In C: return [0, 0]
In C++, Lua, COBOL: return `{0, 0}`.
In F#: return `[||]`.
In Kotlin, Dart and Prolog: return `[]`.
In Pascal: return Type TGap (0, 0).
Examples:
- gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return []`

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} or ... : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap because there is 103in between and 103-109is not a 6-gap because there is 107in between.

You can see more examples of return in Sample Tests.

Note for Go
For Go: nil slice is expected when there are no gap between m and n. Example: gap(11,30000,100000) --> nil

Ref
https://en.wikipedia.org/wiki/Prime_gap
"""


# Solution 1 - it does work properly albeit it may be too slow for codewars and you will get error
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num * 0.5) + 1):
        if num % i == 0:
            return False
    return True


def gap(g, m, n):
    previous_prime = None

    for num in range(m, n + 1):
        if is_prime(num):
            if previous_prime and num - previous_prime == g:
                return [previous_prime, num]
            previous_prime = num

    return None


# Soltuion 2 - slightly optimized using sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def gap(g, m, n):
    is_prime = sieve_of_eratosthenes(n)

    previous_prime = None
    for num in range(m, n + 1):
        if is_prime(num):
            if previous_prime and num - previous_prime == g:
                return [previous_prime, num]
            previous_prime = num

    return None

# Solution 3 - optimized more
def is_prime(a):
    return all(a % i for i in range(2, int(a ** 0.5) + 1))


def gap(g, m, n):
    for a in range(m, n - g + 1):
        if is_prime(a) and is_prime(a + g) and not any(is_prime(j) for j in range(a + 1, a + g)):
            return [a, a + g]

# Solution 4 - best one I came up with
def is_prime(a):
    if a < 2:
        return False
    return all(a % i for i in range(2, int(a ** 0.5) + 1))


def gap(g, m, n):
    previous_prime = None
    for a in range(m, n + 1):
        if is_prime(a):
            if previous_prime and a - previous_prime == g:
                return [previous_prime, a]
            previous_prime = a

    return None

