"""
An element in an array is dominant if it is greater than all elements to its right. You will be given an array and your task will be to return a list of all dominant elements. For example:

solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are greater than elments to their right.
solve([5,4,3,2,1]) = [5,4,3,2,1]

Notice that the last element is always included. All numbers will be greater than 0.
More examples in the test cases.

Good luck!
"""


# Solution 1
def solve(arr):
    result = []

    for i, j in enumerate(arr):
        if j == max(arr[i:]):
            result.append(j)
    return sorted(list(set(result)))[::-1]


# Solution 2
def solve(arr):
    return sorted(list(set(j for i, j in enumerate(arr) if j == max(arr[i:]))))[::-1]


print(f"solution: {solve([16, 17, 14, 3, 14, 5, 2])} | expected: [ 17,14,5,2]")
print(f"solution: {solve([92, 52, 93, 31, 89, 87, 77, 105])} | expected: [105]")
