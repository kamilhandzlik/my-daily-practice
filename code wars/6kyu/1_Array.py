"""
1 Array

Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

If the array is invalid (empty, or contains negative integers or integers with more than 1 digit), return nil (or your language's equivalent).

Examples
Valid arrays

[4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
[1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
[9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
[0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)
Invalid arrays

[] is invalid because it is empty
[1, -9] is invalid because -9 is not a non-negative integer
[1, 2, 33] is invalid because 33 is not a single-digit integer


khelmar
https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
"""


# Solution that somewhat works
def up_array(arr):
    if not arr or any(i < 0 or i > 9 for i in arr):
        return None

    for i in range(len(arr) - 1, -1, -1):
        arr[i] += 1

        if arr[i] < 10:
            return arr

        arr[i] = 0

    if arr[0] == 0:
        arr[0] = 1
        arr.append(0)

        return arr

    return arr


# Real solution
def up_array(arr):
    if not arr or any(i < 0 or i > 9 for i in arr):
        return None

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0

    return [1] + arr
