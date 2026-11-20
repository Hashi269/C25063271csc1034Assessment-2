from Point import Point
import numpy as np


class Circle:
    def __init__(self, o, r):
        if not isinstance(o, Point):
            raise TypeError("o is not a Point")
        self.o = o
        self.r = r


    def __init__(self, o, r):
        """constructor for a circle, origin point is middle"""

        pass

    def __str__(self):
        """string representation of a circle"""
        pass

    def __repr__(self):
        """formal string representation of a circle"""
        pass

    def area(self):
        """method to find the area of a circle"""
        pass

    def perimeter(self):
        """method to find the perimeter of a circle"""
        pass

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""