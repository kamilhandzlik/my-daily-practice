"""
Even or Odd - Which is Greater?

Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"
"""


def even_or_odd(s):
    even = sum([int(i) for i in s if int(i) % 2 == 0])
    odd = sum([int(i) for i in s if int(i) % 2 != 0])
    if even > odd:
        return 'Even is greater than Odd'
    elif even < odd:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'
