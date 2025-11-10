"""
Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000.
"""


# Solution 1
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Solution 2
def is_leap_year(year):
    return True if year % 400 == 0 else False if year % 100 == 0 else True if year % 4 == 0 else False


# Solution 3
def is_leap_year(year):
    return (year % 100 and not year % 4) or not year % 400
