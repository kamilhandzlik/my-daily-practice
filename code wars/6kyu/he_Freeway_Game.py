"""
The Freeway Game

Back-Story
Every day I travel on the freeway.

When I am more bored than usual I sometimes like to play the following counting game I made up:

As I join the freeway my count is 0
Add 1 for every car that I overtake
Subtract 1 for every car that overtakes me
Stop counting when I reach my exit
What an easy game! What fun!

Kata Task
You will be given

The distance to my exit (km)
How fast I am going (kph)
Information about a lot of other cars
Their time (relative to me) as I join the freeway. For example,
-1.5 means they already passed my starting point 1.5 minutes ago
2.2 means they will pass my starting point 2.2 minutes from now
How fast they are going (kph)
Find what is my "score" as I exit the freeway!

Notes
Assume all cars travel at a constant speeds
 Safety Warning

If you plan to play this "game" remember that it is not really a game. You are in a real car.

There may be a temptation to try to beat your previous best score.

Please don't do that...

https://www.codewars.com/kata/59279aea8270cc30080000df/train/python
"""


def freeway_game(dist, my_speed, cars):
    my_time = dist / my_speed
    score = 0

    for offset_min, speed in cars:
        offset_h = offset_min / 60

        car_pos_start = -offset_h * speed

        car_pos_end = car_pos_start + speed * my_time

        my_pos_start = 0
        my_pos_end = dist

        if (my_pos_start - car_pos_start) * (my_pos_end - car_pos_end) < 0:
            score += 1 if my_speed > speed else -1

    return score

