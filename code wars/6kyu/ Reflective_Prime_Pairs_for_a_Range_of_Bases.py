"""
Reflective Prime Pairs for a Range of Bases

Problem Description Find how many reflective prime pairs exist in a given range for each base in a given range. You'll be given two integers as parameters — ceiling range for primes and ceiling range for bases (ranges include the parameters). By "reflective" I mean two distinct numbers who are each other's reflection in the same base (e.g. 37 and 73).

Palindromic numbers like 101 don't count as reflective pairs with themselves — their pair must be distinct. Return a dictionary where ascending bases are keys and the count of reflective pairs within each are the values. e.g.

{ base : count of reflective pairs for base, ... }
Input

Two integers: max_prime_range and max_base_range, where:
2 <= max_prime_range <= 10^4
3 <= max_base_range <= 50
Output

A dictionary where the keys are ascending bases within the range [2, max_base_range] (inclusive), and the values are the counts of reflective prime pairs for each base.
Examples

Input: `(100, 5)`
Output: `{2: 6, 3: 6, 4: 4, 5: 6}`

Prime numbers in the range (inclusive) [2, 100]: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

For base 2: {('101011', '110101'), ('10111', '11101'), ('1000011', '1100001'), ('100101', '101001'), ('1011', '1101'), ('101111', '111101')}

For base 3: {('102', '201'), ('1112', '2111'), ('1011', '1101'), ('1202', '2021'), ('12', '21'), ('1222', '2221')}

For base 4: {('1021', '1201'), ('133', '331'), ('113', '311'), ('13', '31')}

For base 5: {('243', '342'), ('23', '32'), ('142', '241'), ('122', '221'), ('12', '21'), ('34', '43')}}
"""


def prime_reflections(max_prime_range, max_base_range):
    n = max_prime_range
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            step = i * i
            sieve[step:n+1:i] = [False] * (((n - step)//i) + 1)

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    primes_set = set(primes)

    result = {}
    for base in range(2, max_base_range + 1):
        seen_pairs = set()
        count = 0

        for p in primes:
            if p == 0:
                digits = [0]
            else:
                digits = []
                t = p
                while t:
                    digits.append(t % base)
                    t //= base


            if digits == digits[::-1]:
                continue

            reflected = 0
            for d in digits:
                reflected = reflected * base + d

            if reflected in primes_set:
                pair = tuple(sorted((p, reflected)))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    count += 1

        result[base] = count

    return result