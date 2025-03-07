"""
Complete the method which accepts an array of integers, and returns one of the following:

"yes, ascending" - if the numbers in the array are sorted in an ascending order
"yes, descending" - if the numbers in the array are sorted in a descending order
"no" - otherwise
You can assume the array will always be valid, and there will always be one correct answer.
"""

# Solution 1
def is_sorted_and_how(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return "yes, ascending"
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "yes, descending"
    else:
        return "no"



# Solution 2
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'