"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


"""

# Solution 1 my occur Execution timed out
def max_sequence(arr):
    if all(i < 0 for i in arr):
        return 0

    sums = []

    for j, e in enumerate(arr):
        sums.append(e)
        for i in range(j + 1, len(arr)):
            e += arr[i]
            sums.append(e)

    return max(sums)


# Solution 2 using Kadane algorythm
def max_sequence(arr):
    max_current = max_global = 0

    for num in arr:
        max_current = max(0, max_current + num)
        max_global = max(max_global, max_current)

    return max_global