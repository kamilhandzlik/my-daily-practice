"""
Find the divisors!

Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Examples:
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""


# Solution 1
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divisors(integer):
    divs = [i for i in range(2, integer) if integer % i == 0]
    return f"{integer} is prime" if is_prime(integer) else divs


# Solution 2
def divisors(num):
    l = [a for a in range(2, num) if num % a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l


print(divisors(15))
print(divisors(253))
print(divisors(13))
