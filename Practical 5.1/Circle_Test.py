from Circle import Circle
from Point import Point

# define a circle
cir = Circle(Point(1, 1), 2)
#c = Circle((1,1),2) # should raise a TypeError
print(cir)
print(cir.__repr__())
print("{} -> area={}, peri={}".format(cir, cir.area(), cir.perimeter()))
# should be true
print(Point(1, 1) in cir)  # == print(cir.__contains__(Point(1,1)))
print(Point(1, 0) in cir)
# should be false
print(Point(0, 3) in cir)
print(Point(3, 0) in cir)