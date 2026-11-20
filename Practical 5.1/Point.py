#create a class to represent a point on a graph
class Point:
    def __init__(self, x, y):
            if not isinstance(x, int) or not isinstance(y, int):
                raise TypeError("x and y must be integers")
            self.x = x
            self.y = y


    def __str__(self):
        return f'Point: {self.x}, {self.y}'

    def __repr__(self):
        return f'Point: {self.x}, {self.y}'