"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""


def to_weird_case(words):
    words_split = words.split(' ')
    result = []

    for word in words_split:
        new_word = ''
        for i, j in enumerate(word):
            if i % 2 == 0:
                new_word += j.upper()
            else:
                new_word += j.lower()
        result.append(new_word)

    return ' '.join(result)


def to_weird_case(words):
    return ' '.join(
        ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)) for word in words.split())


print(f'Output: {to_weird_case("THIs iS a TEST")} | Expected: ThIs Is A TeSt')
