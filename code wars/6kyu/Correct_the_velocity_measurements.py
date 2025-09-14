"""
Correct the velocity measurements

Overview
You, a police officer, have been tasked with catching speeding drivers on your town's roads. You were given access to the following equipment:

A clock
A LIDAR gun which tells you the distance to (but not speed of) a given object
As you set about your duties, your first thought was to measure a car's distance from yourself twice, divide by the time between measurements, and calculate its speed that way. Simple physics! Two crafty criminals, however, challenge you in court:

Criminal #1: But you were walking toward me at the time! That means you actually measured the sum of our speeds, not just mine!

Criminal #2: But I wasn't driving directly toward you! Your measurement is subject to cosine error!

The judge agrees. Using just distance-to-target over time is insufficient if the one doing the measuring is moving, or if the target's trajectory is not directly towards/away from the observer. Your department begrudgingly shells out for another two pieces of equipment:

A compass
A GPS
You now have what you need to catch these dastardly, mathematically-adept speedsters.

The Task
Given two sets of readings from the equipment specified above, calculate the speed of the target.

Inputs
Two dictionaries in the following form

reading = {
  'time': A float, the time in seconds since some arbitrary epoch when the reading was taken
  'distance': A float, the distance in meters to the target of your LIDAR
  'angle': A float, the angle in radians between the positive x-axis and the target relative to the observer*
  'position': A 2-tuple of floats, the observer's coordinates in meters from some arbitrary origin
}
Outputs
The target's speed in m/s

Example
Let's say you're in your police car at (0, 0) and your clock reads 0s. You see a (putative) speedster north of you, along the positive Y axis 30m away. Taking a reading of your instruments, you see:

reading_a = {
  'time': 0,
  'distance': 30,
  'angle': pi/2,
  'position': (0, 0)
}
after 5 seconds, your squad car has rolled 10m to the west, putting you at (-10, 0). The offender is now due east and 50m away; your measurements are:

reading_b = {
  'time': 5,
  'distance': 50,
  'angle': 0,
  'position': (-10, 0)
}
From the information above, you're able to deduce that the other party moved 50m in 5s, and so they were moving at 10m/s.

Constraints/assumptions/notes
* In other words, if you (the observer) are looking along the positive x-axis, how many radians must you turn anti-clockwise until you are facing the target? This will always be 0 <= angle < 2π.
The world is a 2D plane (harharhar).
Time between measurements will always be >= 0.1s, with the second reading coming later than the first.
The target and observer will always be moving at <= 100m/s relative to the world.
Results are validated +-0.01m/s.
"""

import math

def calculate_speed(reading_a, reading_b):
    # Rozpakowanie danych
    t1, d1, ang1, pos1 = reading_a['time'], reading_a['distance'], reading_a['angle'], reading_a['position']
    t2, d2, ang2, pos2 = reading_b['time'], reading_b['distance'], reading_b['angle'], reading_b['position']

    # Współrzędne celu w pierwszym pomiarze
    tx1 = pos1[0] + d1 * math.cos(ang1)
    ty1 = pos1[1] + d1 * math.sin(ang1)

    # Współrzędne celu w drugim pomiarze
    tx2 = pos2[0] + d2 * math.cos(ang2)
    ty2 = pos2[1] + d2 * math.sin(ang2)

    # Odległość pokonana przez cel
    dist = math.hypot(tx2 - tx1, ty2 - ty1)

    # Różnica czasu
    dt = t2 - t1

    # Prędkość
    return dist / dt