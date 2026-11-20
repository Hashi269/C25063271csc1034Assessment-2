#class to represent a rectangle on a graph
from Point import Point

class Rectangle:
    def __init__(self, o, w, l):
        if not isinstance(o, Point):
            raise TypeError("o is not a Point")
        if not isinstance(w, int):
            raise TypeError("w is not an integer")
        if not isinstance(l, int):
            raise TypeError("l is not an integer")
        # string representation of a rectangle o = origin, l = length, w = width
        self.o = o
        self.w = w
        self.l = l

    def __str__(self):
        return "Rectangle({}, {}, {}, {})".format(self.o.x, self.o.y, self.w, self.l)

    #formal string representation of a rectangle
    def __repr__(self):
        return "Rectangle({}, {}, {})".format(self.o, self.w, self.l)

    #method to find the area of a rectangle
    def area(self):
        return self.w * self.l

    #method to find the perimeter of a rectangle
    def perimeter(self):
        return self.w * 2 + self.l * 2

    #method to determine whether a given point is inside the object
    def __contains__(self, p):
        if p.x > self.o.x + self.l / 2 or p.x < self.o.x - self.l / 2:
            return False
        if p.y > self.o.y + self.w / 2 or p.y < self.o.y - self.w / 2:
            return False

        return True
