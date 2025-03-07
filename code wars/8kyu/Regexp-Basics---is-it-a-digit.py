"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
"""
import re


# version 1
def is_digit(n):
    return False if n == '' or len(n) > 1 else n in "0123456789"


# version 2 - with regex
import re

def is_digit(n):
    return bool(re.fullmatch(r"[0-9]", n))