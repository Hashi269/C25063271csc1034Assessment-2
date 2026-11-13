#class to represent a rectangle on a graph
class Rectangle:
    def __init__(self, o, w, l):
        # string representation of a rectangle
        self.o = o
        self.w = w
        self.l = l
        pass

    def __str__(self):
        return str(self.o)
    #formal string representation of a rectangle
    def __repr__(self):

        pass
    #method to find the area of a rectangle
    def area(self):
        pass
    #method to find the perimeter of a rectangle
    def perimeter(self):
        pass
    #method to determine whether a given point is inside the object
    def __contains__(self, p):
        pass