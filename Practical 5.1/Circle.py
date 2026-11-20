from Point import Point
from Rectrangle import Rectangle


class Circle:
    def __init__(self, o, r):
        if not isinstance(o, Point):
            raise TypeError("o is not a Point")
        if not isinstance(r, Rectangle):
            raise TypeError("r is not a rectangle")
        self.o = o
        self.r = r


    def __init__(self, o, r):
        """constructor for a rectangle, origin point is middle"""
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