"""
Length of missing array

You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

user5036852
https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python
"""

# Solution 1
def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0

    lengths = sorted(len(arr) if arr else 0 for arr in array_of_arrays)

    if 0 in lengths:
        return 0

    for i in range(lengths[0], lengths[-1]):
        if i not in lengths:
            return i


# Solution 2
def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or any(not arr for arr in array_of_arrays):
        return 0

    lengths =sorted(len(arr) for arr in array_of_arrays)
    start = lengths[0]

    for expected, actual in enumerate(lengths, start):
        if expected != actual:
            return expected


# Solution 3
def get_length_of_missing_array(arrays):
    if not arrays or any(not arr for arr in arrays):
        return 0

    lengths = sorted(len(arr) for arr in arrays)
    expected_sum = (lengths[0] + lengths[-1]) * (len(lengths) + 1) // 2
    actual_sum = sum(lengths)
    return expected_sum - actual_sum