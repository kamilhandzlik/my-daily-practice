"""
Given a string s, write a method (function) that will return true if its a valid single integer or floating number or false if its not.

Valid examples, should return true:

isDigit("3")
isDigit("  3  ")
isDigit("-3.23")
should return false:

isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")
"""

def is_digit(s):
    try :
        float(s.strip())
        return True
    except ValueError:
        return False


# Whats below was made for fun XD - yes I know about unittest
print(f"{is_digit('s2324')} | proper solution: False  {'Test passed' if is_digit('s2324') == False else 'Test Failed'}")
print(f"{is_digit('-232.4')} | proper solution: True  {'Test passed' if is_digit('-232.4') == True else 'Test Failed'}")
print(f"{is_digit('3 4')} | proper solution: False  {'Test passed' if is_digit('3 4') == False else 'Test Failed'}")
print(f"{is_digit('3-4')} | proper solution: False  {'Test passed' if is_digit('3-4') == False else 'Test Failed'}")
print(f"{is_digit('34.65')} | proper solution: False  {'Test passed' if is_digit('34.65') == False else 'Test Failed'}")
print(f"{is_digit('-0')} | proper solution: True  {'Test passed' if is_digit('-0') == True else 'Test Failed'}")
print(f"{is_digit('0.0')} | proper solution: True  {'Test passed' if is_digit('0.0') == True else 'Test Failed'}")
print(f"{is_digit('')} | proper solution: False  {'Test passed' if is_digit('') == False else 'Test Failed'}")
print(f"{is_digit(' ')} | proper solution: False  {'Test passed' if is_digit(' ') == False else 'Test Failed'}")
