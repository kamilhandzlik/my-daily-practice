"""
My Language Skills

Task
You are given a dictionary-like object (implementation may vary by language) containing languages as keys and your corresponding test results as values. Return the list of languages where your score is at least 60, in descending order of the scores.

Note: the scores will always be unique (so no duplicate values)

Examples
Input object with key-value pairs:
"Java" -> 10, "Ruby" -> 80, "Python" -> 65
Ouput:
[ "Ruby", "Python" ]

Input object with key-value pairs:
"Hindi" -> 60, "Greek" -> 71, "Dutch" -> 93
Output:
[ "Dutch", "Greek", "Hindi" ]

Input object with key-value pairs:
"C++" -> 50, "ASM" -> 10, "Haskell" -> 20
Output:
[ ]
My other katas
If you enjoyed this kata then please try my other katas! :-)

Translations are welcome!
"""


# Solution 1
def my_languages(results):
    x = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
    return [name for name, num in x.items() if num >= 60]


# Solution 2
def my_languages(results):
    return [
        lang
        for lang, score in sorted(results.items(), key=lambda x: x[1], reverse=True)
        if score >= 60
    ]


# Solution 3
def my_languages(results):
    passed = [(lang, score) for lang, score in results.items() if score >= 60]
    passed_sorted = sorted(passed, key=lambda x: x[1], reverse=True)
    return [lang for lang, _ in passed_sorted]


# Solution 4
from operator import itemgetter


def my_languages(results):
    return [
        lang
        for lang, score in sorted(results.items(), key=itemgetter(1), reverse=True)
        if score >= 60
    ]


print(my_languages({"Hindi": 60, "Dutch": 93, "Greek": 71}))
