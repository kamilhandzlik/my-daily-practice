"""
You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.
"""

# Solution 1
def consecutive(arr, a, b):
    for i, j in enumerate(arr):
        if i + 1 == len(arr):
            break
        elif (j == a and arr[i + 1] == b) or (j == b and arr[i + 1] == a):
            return True
    return False


# Solution 2
def consecutive(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1
print(f"test: {consecutive([1, 3, 5, 7], 3, 7)} expected: False")
print(f"test: {consecutive([1, 3, 5, 7], 3, 1)} expected: True")