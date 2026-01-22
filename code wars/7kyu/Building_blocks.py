"""
Building blocks

Write a class Block that creates a block (Duh..)

Requirements
The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.

Define these methods:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`
Examples
    b = Block([2,4,6]) -> create a `Block` object with a width of `2` a length of `4` and a height of `6`

    b.get_width() -> return 2

    b.get_length() -> return 4

    b.get_height() -> return 6

    b.get_volume() -> return 48

    b.get_surface_area() -> return 88
Note: no error checking is needed

Any feedback would be much appreciated

NaMe613
https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python
"""


# Solution 1
class Block:
    def __init__(self, atr: list):
        self.atr = atr

    def get_width(self):
        return self.atr[0]

    def get_length(self):
        return self.atr[1]

    def get_height(self):
        return self.atr[2]

    def get_volume(self):
        return self.atr[0] * self.atr[1] * self.atr[2]

    def get_surface_area(self):
        return 2 * self.atr[0] * self.atr[1] + 2 * self.atr[0] * self.atr[2] + 2 * self.atr[1] * self.atr[2]


# Solution 2
class Block:
    def __init__(self, dims: list):
        self.width, self.length, self.height = dims

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        w, l, h = self.width, self.length, self.height
        return 2 * (w * l + w * h + l * h)



