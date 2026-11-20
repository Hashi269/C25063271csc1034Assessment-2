#create a class to represent a point on a graph
class Point:
    def __init__(self, x, y):
            if not isinstance(x, int):
                raise TypeError("x and must be an integer")
            if not isinstance(y, int):
                raise TypeError("y and must be an integer")
            self.x = x
            self.y = y


    def __str__(self):
        return f'Point: {self.x}, {self.y}'

    def __repr__(self):
        return f'Point: {self.x}, {self.y}'