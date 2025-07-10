"""
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
Don't forget to rate this kata! Thanks :)
"""


# Solution 1
def camel_case(s):
    result = []

    for i in s.split(' '):
        result.append(i.capitalize())

    return ''.join(result)


# Solution 2
def camel_case(s):
    return ''.join([i.capitalize() for i in s.split(' ')])


# Solution 3
def camel_case(string):
    return string.title().replace(" ", "")


print(camel_case("test case"))
