"""
Alex & snooker: Find Them Al
Even more meticulously, Alex keeps records of snooker matches. Alex can see into the past or the future (magic vision or balls stuffed with all sorts of electronics?). Your task is to find out how many points the player scored in the match, having only one single record of a pocketed ball.

Input
The input is an instance of the "Ball" class, which has the following attributes: color, value of the ball in points, bindings to the previous and next "Ball". Class Ball is dataclass. Dataclass is used to store data.

    from dataclasses import dataclass
    from typing import Union, NewType


    Ball = NewType("Ball", dataclass)


    @dataclass
    class Ball:
        previous: Union[Ball, None] # The variable holds a reference to the previous element in the sequence.
        next: Union[Ball, None] # The variable holds a reference to the next element in the sequence.
        color: str # Вall color
        point: int # The value of the ball in game points

        def __repr__(self):
            return self.color
previous, next, color and point is an instance attribute and can either be called or assigned

  red = Ball(None, None, "Red", 1)
  red.point # 1
  red.color # "Red"
  red.previous # None
  yellow = Ball(None, None, "Yellow", 2)
  red.next = yellow # set next element
  yellow.previous = red # set red like a previous element
  red # Ball(previous=None, next=yellow, color='Red', point=1)
  yellow # Ball(previous=red, next=None, color='Yellow', point=2)
Snooker ball value
Red - 1 point
Yellow - 2 points
Green - 3 points
Brown - 4 points
Blue - 5 points
Pink - 6 points
Black - 7 points
Output
As a result, it is necessary to accumulate the sum of all balls pocketed into the pockets, restoring the entire sequence of balls pocketed by the player (from the first ball pocketed to the last ball pocketed). The first one does not refer to the previous "Ball". and the latter does not refer to the next potted "Ball".

Balls in the sequence
In snooker ball's color differ from shot to shot: a red ball, if potted, must be followed by a colour, a potted colour must be followed by a red, and so on until red balls ends. The alternation between red balls and colours ends when all reds have been potted and an attempt (successful or not) to pot a colour is made after the last red is potted. All six colours have then to be potted in ascending order of their value (yellow, green, brown, blue, pink, black). Each becomes the target ball in that order. During this phase, the colours are not replaced on the table after being legally potted.

Sequence is doubly linked list. A doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes.

    balls = [Red, Black, Red, Green, Red, Black, Red, Yellow, Red, Green, Red, Yellow, Red, Green, Red, Blue, Red, Blue, Red, Yellow, Red, Black, Red, Blue, Red, Green, Red, Black, Red, Yellow, Yellow, Green, Brown, Blue, Pink, Black]
At the input of the function, a ball is randomly selected from the sequence.

"""


def score(ball):
    while ball.previous is not None:
        ball = ball.previous

    total = 0
    current = ball

    while current is not None:
        total += current.point
        current = current.next

    return total
