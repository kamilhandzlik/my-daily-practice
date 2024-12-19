"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

# Solution 1
def prime_factors(n):
    i = 2
    result = ''
    factor = []
    while i * i < n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factor.append(f"({i}{f'**{count}' if count > 1 else ''})")
        i += 1
    if n> 1:
        factor.append(f"({n})")
    result = ''.join(factor)
    return result

# Solution 2



# Solution 3
from sympy import factorint

def prime_factors(n):
    factors = factorint(n)
    return ''.join(f"({base}{f'**{exp}' if exp > 1 else ''})" for base, exp in factors.items())