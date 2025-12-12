"""
Age Range Compatibility Equation

Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.

Min
=
Age
2
+
7
Min=
2
Age
​
 +7

Max
=
2
⋅
(
Age - 7
)
Max=2⋅(Age - 7)

Minimum age
≤
Your age
≤
Maximum age
Minimum age≤Your age≤Maximum age

Task
Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so if the age <= 14, use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form "[min]-[max]"

Examples:
age = 27   =>   "20-40"
age = 5    =>   "4-5"
age = 17   =>   "15-20"
"""

# Solution 1
from math import floor

def dating_range(age):
    return f"{age//2+7}-{2*(age-7)}" if age > 14 else f"{int(floor(age-0.1 *age))}-{int(floor(age+0.1 *age))}"


# Solution 2
def dating_range(age: int) -> str:
    if age > 14:
        return f"{age // 2 + 7}-{2 * (age - 7)}"
    else:
        return f"{int(age * 0.9)}-{int(age * 1.1)}"


# Solution 3
def dating_range(age: int) -> str:
    return f"{age // 2 + 7}-{2 * (age - 7)}" if age > 14 else f"{int(age * 0.9)}-{int(age * 1.1)}"