"""
characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia c"

"zodiac" -> 26
The consonant substrings are: "z", "d" and "c" with values "z" = 26, "d" = 4 and "c" = 3. The highest is 26.

"strength" -> 57
The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

For C: do not mutate input.

More examples in test cases. Good luck!

If you like this Kata, please try:

Word values

Vowel-consonant lexicon
"""

# Solution 1
def solve(s):
    vowels = "aeiou"
    substrings = []
    result = []
    temp = ''

    for char in s:
        if char in vowels:
            if temp != '':
                temp = ''
        else:
            temp += char
        if temp != '':
            substrings.append(temp)

    for substring in substrings:

        substring_numbers = []
        for i in substring:
            substring_numbers.append(ord(i) - 96)

        substring_value = sum(substring_numbers)
        result.append(substring_value)

    return max(result)


# Solution2
def solve(s):
    vowels = "aeiou"
    max_sum = current_sum = 0

    for char in s:
        if char in vowels:
            current_sum = 0
        else:
            current_sum += ord(char) - 96
            max_sum = max(max_sum, current_sum)

    return max_sum

print(f"case: {solve('cozy')} expected: 51")
print(f"case: {solve('xyzzy')} expected: 126")
print(f"case: {solve('zodiac')} expected: 26")
