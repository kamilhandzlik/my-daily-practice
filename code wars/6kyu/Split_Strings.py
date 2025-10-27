"""
Split Strings

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


# Solution 1
def solution(s):
    if len(s) % 2 != 0:
        s += '_'

    result = []
    prev = 0

    for i in range(2, len(s) + 1, 2):
        result.append(s[prev: i])
        prev += 2

    return result


# Solution 2
def solution(s):
    s += '_' * (len(s) % 2)
    return [s[i:i + 2] for i in range(0, len(s), 2)]


# Solution 3
def solution(s):
    result = []
    i = 0
    while i < len(s):
        pair = s[i:i + 2]
        if len(pair) == 1:
            pair += '_'
        result.append(pair)
        i += 2
    return result


print(solution("asdfadsf"))
