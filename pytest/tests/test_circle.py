import pytest
import source.shapes as shapes
from math import pi


class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down{method}")
        del self.circle

    def test_area(self):
        expected = pi * self.circle.radius**2
        assert self.circle.area() == expected

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
