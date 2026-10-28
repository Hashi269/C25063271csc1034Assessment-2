#create a class to represent a point on a graph
class Point:
    def __init__(self, x, y):
        #constructor for a point
        pass
    def __str__(self):
        #string representation of a point
        pass
    def __repr__(self):
        #formal representation of a string
        pass

    p = "Point(2, 1)"
    #should raise a typeerror
    print(p)
    print(p.__repr__())