#create a class to represent a point on a graph
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def __str__(self):
        return f'Point: {self.x}, {self.y}'

    def __repr__(self):
        return f'Point: {self.x}, {self.y}'