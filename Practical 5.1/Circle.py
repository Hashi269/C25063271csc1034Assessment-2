from Point import Point
import math

class Circle:
    def __init__(self, o, r):
        if not isinstance(o, Point):
            raise TypeError("o is not a Point")
        self.o = o
        self.r = r

    def __str__(self):
        """string representation of a circle"""
        return "circle({}, {}, {})".format(self.o.x, self.o.y, self.r)

    def __repr__(self):
        """formal string representation of a circle"""
        return "circle({}, {})".format(self.o, self.r)

    def area(self):
        """method to find the area of a circle"""
        return math.pi * (self.r * self.r)

    def perimeter(self):
        """method to find the perimeter of a circle"""
        return 2 * math.pi * self.r

    def __contains__(self, p):
        """method to determine whether a given point is inside the object"""
        if p.x > self.o.x + self.r / 2 or p.x < self.o.x - self.r / 2:
            return False
        if p.y > self.o.y + self.r / 2 or p.y < self.o.y - self.r / 2:
            return False

        return True
