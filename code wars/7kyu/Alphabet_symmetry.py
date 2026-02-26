"""
Alphabet symmetry

Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]
See test cases for more examples.

Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

Good luck!

If you like this Kata, please try:

Last digit symmetry

Alternate capitalization

KenKamau
"""


# Solution 1
def solve(strings: list[str]) -> list[int]:
    result = []

    for i in strings:
        k = 0

        for poz, j in enumerate(i):
            if j.isupper() and ord(j) - 64 == poz + 1:
                k += 1
            elif j.islower() and ord(j) - 96 == poz + 1:
                k += 1

        result.append(k)

    return result


# Solution 2
def solve(strings: list[str]) -> list[int]:
    return [
        sum((ord(c.lower()) - 96) == i + 1 for i, c in enumerate(word))
        for word in strings
    ]


print(solve(["abode", "ABc", "xyzD"]))
