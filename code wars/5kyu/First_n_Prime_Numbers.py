"""
First n Prime Numbers

A prime number is an integer greater than 1 that is only evenly divisible by itself and 1.

Write your own Primes class with class method Primes.first(n) that returns an array of the first n prime numbers.

For example:

Primes.first(1)
# => [2]

Primes.first(2)
# => [2, 3]

Primes.first(5)
# => [2, 3, 5, 7, 11]

Primes.first(20).last(5)
# => [53, 59, 61, 67, 71]
Note: An inefficient algorithm will time out. Memoization may help.

More info on primes here.
"""


class Primes:
    _primes = [2]

    @classmethod
    def first(cls, n):
        while len(cls._primes) < n:
            cls._generate_next_prime()
        return cls._primes[:n]

    @classmethod
    def _generate_next_prime(cls):
        candidate = cls._primes[-1] + 1

        while True:
            if cls._is_prime(candidate):
                cls._primes.append(candidate)
                return
            candidate += 1

    @classmethod
    def _is_prime(cls, number):
        for p in cls._primes:
            if p * p > number:
                break
            if number % p == 0:
                return False
        return True
