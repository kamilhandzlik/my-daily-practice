"""
Separate The Wheat From The Chaff

Scenario
With Cereal crops like wheat or rice, before we can eat the grain kernel, we need to remove that inedible hull, or to separate the wheat from the chaff.

Task
Given a sequence of n integers , separate the negative numbers (chaff) from positive ones (wheat).!alt

Notes
Sequence size is at least 3
Return a new sequence, such that negative numbers (chaff) come first, then positive ones (wheat).
In Java , you're not allowed to modify the input Array/list/Vector
Have no fear , it is guaranteed that there will be no zeroes .!alt
Repetition of numbers in the input sequence could occur , so duplications are included when separating.
If a misplaced positive number is found in the front part of the sequence, replace it with the last misplaced negative number (the one found near the end of the input). The second misplaced positive number should be swapped with the second last misplaced negative number. Negative numbers found at the head (begining) of the sequence , should be kept in place .
Input >> Output Examples:
wheatFromChaff ({7, -8, 1 ,-2}) ==> return ({-2, -8, 1, 7})
Explanation:
Since 7  is a positive number , it should not be located at the beginnig so it needs to be swapped with the last negative number -2.
wheatFromChaff ({-31, -5, 11 , -42, -22, -46, -4, -28 }) ==> return ({-31, -5,- 28, -42, -22, -46 , -4, 11})
Explanation:
Since, {-31, -5}  are negative numbers found at the head (begining) of the sequence , so we keep them in place .
Since 11 is a positive number, it's replaced by the last negative which is -28 , and so on till sepration is complete.
wheatFromChaff ({-25, -48, -29, -25, 1, 49, -32, -19, -46, 1}) ==> return ({-25, -48, -29, -25, -46, -19, -32, 49, 1, 1})
Explanation:
Since {-25, -48, -29, -25}  are negative numbers found at the head (begining) of the input , so we keep them in place .

Since 1 is a positive number, it's replaced by the last negative which is -46 , and so on till sepration is complete.

Remeber, duplications are included when separating , that's why the number 1 appeared twice at the end of the output.

Tune Your Code , There are 250 Assertions , 100.000 element For Each .
Only O(N) Complexity Solutions Will pass .
Playing with Numbers Series
Playing With Lists/Arrays Series
Bizarre Sorting-katas
For More Enjoyable Katas
ALL translations are welcome
Enjoy Learning !!
Zizou


MrZizoScream
https://www.codewars.com/kata/5bdcd20478d24e664d00002c/train/python
"""


def wheat_from_chaff(values):
    arr = values[:]
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] < 0:
            i += 1
            continue

        if arr[j] > 0:
            j -= 1
            continue

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


# Tests
import pytest
import random


def test_basic_examples():
    assert wheat_from_chaff([7, -8, 1, -2]) == [-2, -8, 1, 7]
    assert wheat_from_chaff([-31, -5, 11, -42, -22, -46, -4, -28]) == \
           [-31, -5, -28, -42, -22, -46, -4, 11]
    assert wheat_from_chaff([-25, -48, -29, -25, 1, 49, -32, -19, -46, 1]) == \
           [-25, -48, -29, -25, -46, -19, -32, 49, 1, 1]


def test_all_negatives_at_start():
    assert wheat_from_chaff([-9, -8, -7, 1, 2, 3]) == [-9, -8, -7, 1, 2, 3]


def test_all_positives_at_start():
    assert wheat_from_chaff([9, 8, 7, -1, -2, -3]) == [-3, -2, -1, 7, 8, 9]


def test_duplicates():
    assert wheat_from_chaff([1, 1, 1, -1, -1, -1]) == [-1, -1, -1, 1, 1, 1]
    assert wheat_from_chaff([-5, -5, 10, 10, -5, 10]) == [-5, -5, -5, 10, 10, 10]


def test_minimal_cases():
    assert wheat_from_chaff([1, -1, 2]) == [-1, 1, 2]
    assert wheat_from_chaff([-1, 2, -3]) == [-1, -3, 2]


def test_mixed_pattern():
    assert wheat_from_chaff([5, 4, 3, -1, -2, -3]) == [-3, -2, -1, 3, 4, 5]
    assert wheat_from_chaff([-1, -2, -3, 5, 4, 3]) == [-1, -2, -3, 5, 4, 3]
    assert wheat_from_chaff([10, -1, 20, -2, 30, -3]) == [-3, -2, -1, 20, 30, 10]


def is_valid_separation(arr):
    """Sprawdza czy wszystkie negatywy są przed pozytywami."""
    seen_positive = False
    for x in arr:
        if x > 0:
            seen_positive = True
        if seen_positive and x < 0:
            return False
    return True


def test_random_cases():
    for _ in range(200):
        arr = [random.choice([-1, 1]) * random.randint(1, 1000) for _ in range(50)]
        result = wheat_from_chaff(arr)

        assert len(result) == len(arr)

        assert sorted(result) == sorted(arr)

        assert is_valid_separation(result)
