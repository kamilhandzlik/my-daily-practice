"""
Find the unique string

There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

Find the unique number
Find the unique string (this kata)
Find The Unique
"""


# I would have worked but last test has huge array eg 1 000 000. Count is responsible here for failure so it needs to be removed or side stepped
def find_uniq(arr):
    normalized = [set(s.replace(' ', '').lower()) for s in arr]

    for i, chars in enumerate(normalized):
        if normalized.count(chars) == 1:
            return arr[i]


# Solution
from collections import Counter


def find_uniq(arr):
    normalized = [''.join(sorted(set(s.replace(' ', '').lower()))) for s in arr]

    counts = Counter(normalized)

    unique_pattern = next(k for k, v in counts.items() if v == 1)

    for i, pattern in enumerate(normalized):
        if pattern == unique_pattern:
            return arr[i]


print(find_uniq(['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']))
