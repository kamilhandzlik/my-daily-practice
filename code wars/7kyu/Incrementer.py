"""
Incrementer

Given an input of an array of digits, return the array with each digit incremented by its position in the array: the first digit will be incremented by 1, the second digit by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).

Your result can only contain single digit numbers, so if adding a digit with its position gives you a multiple-digit number, only the last digit of the number should be returned.

Notes:
return an empty array if your array is empty
arrays will only contain numbers so don't worry about checking that
Examples:
[1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]

[4, 6, 9, 1, 3]  -->  [5, 8, 2, 5, 8]  #  [4+1, 6+2, 9+3, 1+4, 3+5]
                                       #  9+3 = 12  -->  2

kkavita92
https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python
"""
import unittest
import random


# Solution 1
def incrementer(nums):
    return [num + poz + 1 if num + poz + 1 < 10 else int(f"{num + poz + 1}"[-1]) for num, poz in enumerate(nums)]


# Solution 2
def incrementer(nums):
    return [(num + i + 1) % 10 for i, num in enumerate(nums)]


# Solution 3
def incrementer(nums):
    return list(map(lambda x: (x[1] + x[0] + 1) % 10, enumerate(nums)))


# Solution 4
def incrementer(nums):
    result = []
    for i, num in enumerate(nums):
        result.append((num + i + 1) % 10)
    return result


# Solution 5
from itertools import count


def incrementer(nums):
    return [(n + c) % 10 for n, c in zip(nums, count(1))]


# Tests
class TestIncementer(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(incrementer([]), [])
        self.assertEqual(incrementer([1, 2, 3]), [2, 4, 6])
        self.assertEqual(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])


def reference(nums):
    return [(num + i + 1) % 10 for i, num in enumerate(nums)]


class TestIncrementerRandom(unittest.TestCase):
    def test_random(self):
        for _ in range(200):
            test_case = [random.randint(0, 9) for _ in range(50)]
            self.assertEqual(incrementer(test_case), reference(test_case))
