"""
Area of a Polygon (Easy)

Write the function polygonArea(A,B,C,D) that finds the area of polygons of this type:

alt text

Assume D always equals B/2.
Assume the angles formed by AB and BC are right angles.

"""


def polygon_area(a, b, c, d):
    return a * b + ((c - a) * d)
