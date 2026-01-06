"""
The Hunger Games - Shut the gate

Story
Old MacDingle had a farm...

...and on that farm he had

horses
chickens
rabbits
some apple trees
a vegetable patch
Everything is idylic in the MacDingle farmyard unless somebody leaves the gates open

Depending which gate was left open then...

horses might run away
horses might eat the apples
horses might eat the vegetables
chickens might run away
rabbits might run away
rabbits might eat the vegetables
Kata Task
Given the state of the farm gates in the evening, your code must return what the farm looks like the next morning when daylight reveals what the animals got up to.

Legend
H horse
C chicken
R rabbit
A apple tree
V vegetables
| gate (closed),
\ or / gate (open)
. everything else
Example
Before	```|..HH....\AAAA\CC..|AAA/VVV/RRRR|CCC```
After	```|..HH....\....\CC..|AAA/.../RRRR|...``` Because:
The horses ate whatever apples they could get to
The rabbits ate the vegetables
The chickens ran away
Notes
If the animals can eat things and also run away then they do BOTH - it is best not to run away when you are hungry!
An animal cannot "go around" a closed gate...
...but it is possible to run away from the farm and then RUN BACK and re-enter though more open gates on the other side!


https://www.codewars.com/kata/59218bf66034acb9b7000040/train/python
"""

def shut_the_gate(farm):
    frm = list(farm)

    bounds = [i for i, ch in enumerate(frm) if ch == '|']

    if bounds:
        ranges = [
            list(range(0, bounds[0])) + list(range(bounds[-1], len(frm)))
        ]
        ranges += [list(range(a, b)) for a, b in zip(bounds, bounds[1:])]
    else:
        ranges = [list(range(len(frm)))]

    for rng in ranges:
        no_horses = all(frm[i] != 'H' for i in rng)
        no_rabbits = no_horses and all(frm[i] != 'R' for i in rng)

        for i in rng:
            if frm[i] == 'A' and not no_horses:
                frm[i] = '.'
            elif frm[i] == 'V' and not no_rabbits:
                frm[i] = '.'

    for i in ranges[0]:
        if frm[i] in 'HCR':
            frm[i] = '.'

    return ''.join(frm)

print(shut_the_gate("|..HH....\\AAAA\\CC..|VVV/RRRR|CCC"))
print(f"expected: '|..HH....\\....\\CC..|.../RRRR|...'")
