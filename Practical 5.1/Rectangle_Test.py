from Rectrangle import Rectangle
from Point import Point

# define a rectangle
r = Rectangle(Point(1, 1), 2, 3)
# r = Rectangle((1,1),2,3) # should raise a TypeError
print(r)
print(r.__repr__())
print("{} -> area={}, peri={}".format(r, r.area(), r.perimeter()))
# should be true
print(Point(1, 1) in r)  # == print(r.__contains__(Point(1,1)))
print(Point(1, 0) in r)
# should be false
print(Point(0, 3) in r)
print(Point(3, 0) in r)