"""
Missing and Duplicate Number

You are given an array containing all integers from 1 to N, except one that is missing.

In order to fill the array, one of the elements of the sequence has been duplicated.

Your mission is to find which number is missing and which one is duplicated.

Example:

solution([2,4,1,6,3,4]) should return [5,4] because 5 is missing and 4 appears twice.

Remarks:

You are not allowed to mutate the array.
You are not allowed to sort the array.
Your solution should not time out for large values of N.
Ideally, your solution should not use extra space except the one provided by the input array (which can be modified).
"""


def solution(array):
    n = len(array)

    actual_sum = 0
    actual_sum_sq = 0

    for x in array:
        actual_sum += x
        actual_sum_sq += x * x

    expected_sum = n * (n + 1) // 2
    expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6

    diff_sum = expected_sum - actual_sum
    diff_sum_sq = expected_sum_sq - actual_sum_sq

    sum_both = diff_sum_sq // diff_sum

    missing = (diff_sum + sum_both) // 2
    duplicate = (sum_both - diff_sum) // 2

    return (missing, duplicate)
