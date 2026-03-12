"""
Wave Sorting

A list of integers is sorted in “Wave” order if alternate items are not less than their immediate neighbors (thus the other alternate items are not greater than their immediate neighbors).

Thus, the array [4, 1, 7, 5, 6, 2, 3] is in Wave order because 4 >= 1, then 1 <= 7, then 7 >= 5, then 5 <= 6, then 6 >= 2, and finally 2 <= 3.

The wave-sorted lists has to begin with an element not less than the next, so [1, 4, 5, 3] is not sorted in Wave because 1 < 4

Your task is to implement a function that takes a list of integers and sorts it into wave order in place; your function shouldn't return anything.

Note:

The resulting array shouldn't necessarily match anyone in the tests, a function just checks if the array is now wave sorted.

kodejuice
https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/python
"""


# Solution 1
def wave_sort(a):
    a.sort()

    for i in range(0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]


# Solution 2
def wave_sort(a):
    n = len(a)

    for i in range(0, n, 2):

        if i > 0 and a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]

        if i < n - 1 and a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]


# Solution 3
def wave_sort(a):
    a.sort()

    res = []
    left = 0
    right = len(a) - 1

    while left <= right:
        if right >= left:
            res.append(a[right])
            right -= 1

        if left <= right:
            res.append(a[left])
            left += 1

    a[:] = res


# Solution 4
def wave_sort(a):
    expect_greater = True

    for i in range(len(a) - 1):

        if expect_greater:
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        else:
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

        expect_greater = not expect_greater


# Tests
import unittest
import random


def is_wave(a):
    for i in range(len(a) - 1):

        if i % 2 == 0:
            if a[i] < a[i + 1]:
                return False
        else:
            if a[i] > a[i + 1]:
                return False

    return True


class TestWaveSort(unittest.TestCase):

    def test_basic(self):
        a = [4, 1, 7, 5, 6, 2, 3]
        wave_sort(a)
        self.assertTrue(is_wave(a))

    def test_sorted(self):
        a = [1, 2, 3, 4, 5, 6]
        wave_sort(a)
        self.assertTrue(is_wave(a))

    def test_reverse(self):
        a = [6, 5, 4, 3, 2, 1]
        wave_sort(a)
        self.assertTrue(is_wave(a))

    def test_duplicates(self):
        a = [3, 3, 3, 3, 3]
        wave_sort(a)
        self.assertTrue(is_wave(a))

    def test_small(self):
        a = [1, 2]
        wave_sort(a)
        self.assertTrue(is_wave(a))


class TestWaveSortRandom(unittest.TestCase):

    def test_random(self):
        for _ in range(100):
            size = random.randint(1, 50)

            arr = [
                random.randint(-100, 100)
                for _ in range(size)
            ]

            wave_sort(arr)

            self.assertTrue(is_wave(arr))


print(wave_sort([4, 1, 7, 5, 6, 2, 3]))
