"""
Tidy Number (Special Numbers Series #9)

Definition
A Tidy Number is a number whose digits are in non-decreasing order.

Task
Given a number, determine if it is tidy or not.

Notes
The number passed will always be positive.
Return the result as a boolean.
Examples
12 ==> return true
Explanation: Digits {1, 2} are in non-decreasing order (1 <= 2).

32 ==> return false
Explanation: Digits {3, 2} are not in non-decreasing order (3 > 2).

1024 ==> return false
Explanation: Digits {1, 0, 2, 4} are not in non-decreasing order (1 > 0).

13579 ==> return true
Explanation: Digits {1, 3, 5, 7, 9} are in non-decreasing order.

2335 ==> return true
Explanation: Digits {2, 3, 3, 5} are in non-decreasing order (3 = 3).


MrZizoScream
https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python
"""


# Solution 1
def tidyNumber(n):
    return int(''.join(sorted(str(n)))) == n


# Solution 2
def tidyNumber(n):
    return str(n) == ''.join(sorted(n))


# Solution 3
def tidyNumber(n):
    digits = str(n)
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))


# Solution 4
def tidyNumber(n):
    return all(a <= b for a, b in zip(str(n), str(n)[1:]))
