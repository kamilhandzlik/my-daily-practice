"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
"""

# version 1
def find_longest(arr):
    lengths = [[len(str(i)), i] for i in arr]
    max_length = max(arr)
    final_numbers = []

    for j in lengths:
        if j[0] == len(str(max_length)):
            final_numbers.append(j[1])

    return final_numbers[0]


# version 2
def find_longest(arr):
    lengths = [[len(str(i)), i] for i in arr]
    return [j[1] for j in lengths if j[0] == len(str(max(arr)))][0]


# version 3 XD - python list comprehension madness
def find_longest(arr):
    return [j[1] for j in [[len(str(i)), i] for i in arr] if j[0] == len(str(max(arr)))][0]

# version 4
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))

