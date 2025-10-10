"""
Fizz Buzz

Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
N will never be less than 1.

Method calling example:

fizzbuzz(3) -->  [1, 2, "Fizz"]
"""

# Solution 1
def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(i)

    return result

# Solution 2
def fizzbuzz(n):
    return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i for i in range(1, n+1)]


# Solution 3
def fizzbuzz(n):
    return [
        (("Fizz" * (i % 3 == 0)) + ("Buzz" * (i % 5 == 0))) or i
        for i in range(1, n + 1)
    ]

# Solution 4
def fizzbuzz(n):
    return list(map(lambda i: "FizzBuzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i, range(1, n + 1)))

print(fizzbuzz(10))