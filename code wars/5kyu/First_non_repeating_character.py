"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.
"""
from itertools import count


# Solution 1
def first_non_repeating_letter(s):
    result = ""
    for i in s:
        if s.count(i) == 1:
            if s.lower().count(i.lower()) == 0:
                result = ""
            elif s.lower().count(i.lower()) == 1:
                result += i

    return "" if result == "" else result[0]


# Solution 2
def first_non_repeating_letter(s):
    lower_s = s.lower()
    counts = {}

    for char in lower_s:
        counts[char] = counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if counts[char.lower()] == 1:
            return char

    return ""

print(first_non_repeating_letter(''))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('sTreSS'))
