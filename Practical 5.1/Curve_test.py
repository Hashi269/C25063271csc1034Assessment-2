from Curve import Curve
from Point import Point

# define a curve
cur = Curve(Point(1, 1), Point(2, 4), Point(3, 9))
# cur = Curve(Point(1,1),(2,2)) # should raise a TypeError
print(cur)
print(cur.__repr__())
# return a point/item
print(cur[1])  # == print(cur.__getitem__(1))
# return points/items i.e. subcurve
print(cur[0:2])  # == print(cur.__getitem__(slice(0,2)))
# update point
cur[1] = Point(1, 1)  # == print(cur.__setitem__(1,Point(1,1)))
# cur[1] = (1,1) # should raise a TypeError
print(cur)