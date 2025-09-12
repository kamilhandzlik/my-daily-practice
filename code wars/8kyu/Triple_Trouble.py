"""
Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length.
"""


# Solution 1
def triple_trouble(one, two, three):
    result = []
    for i in range(len(one)):
        result.append(one[i] + two[i] + three[i])
    return ''.join(result)


# Solution 2 list comprehension
def triple_trouble(one, two, three):
    return ''.join([one[i] + two[i] + three[i] for i in range(len(one))])


# Solution 3
def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))


print(triple_trouble("aaa", "bbb", "ccc"))
print(triple_trouble("burn", "reds", "roll"))
