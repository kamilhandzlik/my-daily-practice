"""
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.
"""
from math import sqrt

# Solution 1
def square_or_square_root(arr):
    result = []

    for i in arr:
        if i % sqrt(i) == 0:
            result.append(int(sqrt(i)))
        else:
            result.append(i**2)

    return result

# Solution 2
def square_or_square_root(arr):
    return [int(sqrt(i)) if i%sqrt(i) == 0 else i**2 for i in arr]
print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))