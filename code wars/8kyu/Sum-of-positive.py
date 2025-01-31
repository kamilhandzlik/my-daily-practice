"""
Task
You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] =>
1
+
7
+
12
=
20
1+7+12=20
Note
If there is nothing to sum, the sum is default to 0.
"""


# Solution 1
def positive_sum(arr):
    j = 0
    for i in arr:
        if i > 0:
            j += i
    return j


# Solution 2
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
