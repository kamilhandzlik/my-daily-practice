"""
Rock Off!

Alice and Bob have participated to a Rock Off with their bands. A jury of true metalheads rates the two challenges,
awarding points to the bands on a scale from 1 to 50 for three categories: Song Heaviness, Originality, and Members' outfits.

For each one of these 3 categories they are going to be awarded one point, should they get a better judgement from the jury.
No point is awarded in case of an equal vote.

You are going to receive two arrays, containing first the score of Alice's band and then those of Bob's. Your task is to find their total score by comparing them in a single line.

Example:

Alice's band plays a Nirvana inspired grunge and has been rated 20 for Heaviness, 32 for Originality and only 18 for Outfits.
Bob listens to Slayer and has gotten a good 48 for Heaviness, 25 for Originality and a rather honest 40 for Outfits.

The total score should be followed by a colon : and by one of the following quotes: if Alice's band wins: Alice made "Kurt"
proud! if Bob's band wins: Bob made "Jeff" proud! if they end up with a draw: that looks like a "draw"! Rock on!

The solution to the example above should therefore appear like '1, 2: Bob made "Jeff" proud!'.

boi87
https://www.codewars.com/kata/5b097da6c3323ac067000036/train/python
"""


# Solution 1
def solve(a, b):
    alice = 0
    bob = 0

    for i, j in enumerate(a):
        if j > b[i]:
            alice += 1
        elif b[i] > j:
            bob += 1

    if alice > bob:
        return f'{alice}, {bob}: Alice made "Kurt" proud!'
    elif bob > alice:
        return f'{alice}, {bob}: Bob made "Jeff" proud!'
    else:
        return f'{alice}, {bob}: that looks like a "draw"! Rock on!'


# Solution 2
"""
Rock Off!

Alice and Bob have participated to a Rock Off with their bands. A jury of true metalheads rates the two challenges,
awarding points to the bands on a scale from 1 to 50 for three categories: Song Heaviness, Originality, and Members' outfits.

For each one of these 3 categories they are going to be awarded one point, should they get a better judgement from the jury.
No point is awarded in case of an equal vote.

You are going to receive two arrays, containing first the score of Alice's band and then those of Bob's. Your task is to find their total score by comparing them in a single line.

Example:

Alice's band plays a Nirvana inspired grunge and has been rated 20 for Heaviness, 32 for Originality and only 18 for Outfits.
Bob listens to Slayer and has gotten a good 48 for Heaviness, 25 for Originality and a rather honest 40 for Outfits.

The total score should be followed by a colon : and by one of the following quotes: if Alice's band wins: Alice made "Kurt"
proud! if Bob's band wins: Bob made "Jeff" proud! if they end up with a draw: that looks like a "draw"! Rock on!

The solution to the example above should therefore appear like '1, 2: Bob made "Jeff" proud!'.

boi87
https://www.codewars.com/kata/5b097da6c3323ac067000036/train/python
"""


# Solution 1
def solve(a, b):
    alice = 0
    bob = 0

    for i, j in enumerate(a):
        if j > b[i]:
            alice += 1
        elif b[i] > j:
            bob += 1

    if alice > bob:
        return f'{alice}, {bob}: Alice made "Kurt" proud!'
    elif bob > alice:
        return f'{alice}, {bob}: Bob made "Jeff" proud!'
    else:
        return f'{alice}, {bob}: that looks like a "draw"! Rock on!'


# Solution 2
def solve(a, b):
    alice = sum(x > y for x, y in zip(a, b))
    bob = sum(y > x for x, y in zip(a, b))

    if alice > bob:
        msg = 'Alice made "Kurt" proud!'
    elif bob > alice:
        msg = 'Bob made "Jeff" proud!'
    else:
        msg = 'that looks like a "draw"! Rock on!'

    return f'{alice}, {bob}: {msg}'


# Solution 3
def solve(a, b):
    alice = sum(x > y for x, y in zip(a, b))
    bob = sum(y > x for x, y in zip(a, b))
    return f'{alice}, {bob}: ' + (
        'Alice made "Kurt" proud!' if alice > bob else
        'Bob made "Jeff" proud!' if bob > alice else
        'that looks like a "draw"! Rock on!'
    )
