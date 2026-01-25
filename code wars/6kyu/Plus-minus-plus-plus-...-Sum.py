"""
Plus - minus - plus - plus - ... - Sum

Given an array [x1, x2, ..., xn] determine whether it is possible to put + or - between the elements and get an expression equal to sum. Result is boolean

2 <= n <= 22
0 <= xi <= 20
-10 <= sum <= 10
Example
arr = [1, 3, 4, 6, 8]

sum = -2

1 + 3 - 4 + 6 - 8 = -2

Result is: true

Notes
If it is impossible to find a solution then you should return false.

kdmatrosov
https://www.codewars.com/kata/5bc463f7797b00b661000118/train/python
"""


def is_possible(arr, goal):
    def dfs(index, current_sum):
        if index == len(arr):
            return current_sum == goal

        return (dfs(index + 1, current_sum + arr[index]) or
                dfs(index + 1, current_sum - arr[index]))

    return dfs(1, arr[0])
