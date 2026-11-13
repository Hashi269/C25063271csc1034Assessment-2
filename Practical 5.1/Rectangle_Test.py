from Point import Point
from Rectrangle import Rectangle

r = Rectangle(Point(1,1),2,3)
print(r)
print(r.__repr__())
print("{} -> area={}, peri={}". format(r, r.area(), r.perimeter()))
