"""
You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'. The rest of the string will be made up of '.'.

You need to find out if the cat can catch the mouse from its current position. The cat can jump at most (j) characters, and cannot jump over the dog.

So:

if j = 5:

..C.....m...D returns 'Caught!' <-- not more than j characters between the cat and the mouse

.....C............m......D returns 'Escaped!' <-- as there are more than j characters between the two, the cat cannot jump far enough

if j = 10:

...m.........C...D returns 'Caught!' <-- Cat can jump far enough and jump is not over dog

...m....D....C....... returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse

Finally, if not all three animals are present, return 'boring without all three'
"""


# Solution 1
def cat_mouse(x, j):
    if 'C' not in x or 'D' not in x or 'm' not in x:
        return "boring without all three"

    c_pos = x.index('C')
    m_pos = x.index('m')

    if abs(c_pos - m_pos) > j:
        return "Escaped!"
    elif x.count('D', c_pos, m_pos) == 1 or x.count('D', m_pos, c_pos) == 1:
        return "Protected!"
    else:
        return "Caught!"


# Solution 2
def cat_mouse(x, j):
    if not {'C', 'D', 'm'}.issubset(x):
        return "boring without all three"

    c_pos = x.index('C')
    m_pos = x.index('m')
    distance = abs(c_pos - m_pos)

    if distance > j:
        return "Escaped!"

    start, end = sorted([c_pos, m_pos])
    if 'D' in x[start:end]:
        return "Protected!"
    return "Caught!"




print(cat_mouse('..D.....C.m', 2))
print(cat_mouse('.....m....D..C.......', 25))
