"""
Keypad Heist: The Riley Poole Logic


"Riley, get me every possible combination!"
Keypad Heist: The Riley Poole Logic (Hard Version) is the next step after this kata. Make sure to check it out!

In National Treasure, Ben Gates smudges heat-sensitive powder on a keypad and finds the letters: A, E, F, G, L, O, R, V, Y.

Riley's standard anagram program fails because it doesn't account for letters being pressed more than once. Ben realizes the password is 11 characters long, meaning some of those letters are repeats!

The Mission
Help Riley rewrite his code! Create a function get_passwords(keys, length) that generates every possible string of a specific length using only the characters in keys.

The Rules
Mandatory Presence: Every single letter in the keys string must appear at least once in the result.
Length: Every string must be exactly length characters long.
Format: The output must be a sorted list of unique strings.
Example
get_passwords("ab", 3)
# 'a' and 'b' must both be there at least once.
# Result: ["aab", "aba", "abb", "baa", "bab", "bba"]
Notes
Please rank the kata and tell me what you think in discourse. All your feedback is very important!
Huge thanks to 'National Treasure' for the inspiration! Now let's go steal the Declaration of Independence.


ZlataBrain
https://www.codewars.com/kata/69db87ed65da17c01436ecbe/train/python

"""

from itertools import product


def get_passwords(keys, length):
    result = []

    for combo in product(keys, repeat=length):
        word = ''.join(combo)

        if all(k in word for k in keys):
            result.append(word)

    return sorted(result)
