"""
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.


def correct_tail(body, tail):
     sub = body.substr(len(body)-len(tail.length)
        if sub = tai:
    return True
        else:
    return False
"""


# 1. Idk why complicate things
def correct_tail(body, tail):
    return body[-1:] == tail


# 2. Solution for tail of different length than 1
def correct_tail(body, tail):
    return body[-len(tail):] == tail

# 3. Same thing as the second
def correct_tail(body, tail):
    return body.endswith(tail)

print(correct_tail("Fox", "x"))
