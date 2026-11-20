from Point import Point

class Curve:
    """Class to represent a list of points on a graph"""

    def __init__(self, *inputs):
        self.items = []
        for input in inputs:
            self.append_if_valid(input)

    def append_if_valid(self, item):

        if not isinstance(item, Point):
            raise TypeError("item is not a Point")
        self.items.append(item)


    def __str__(self):
        """string representation of a curve"""
        return "Curve:{}".format(self.items)

    def __repr__(self):
        """formal string representation of a curve"""
        s = ", "
        s = s.join([repr(x) for x in self.items])
        return "Curve:({})".format(s)


    def __getitem__(self, index):
        """get point(s) in curve"""
        if isinstance(index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])

    def __setitem__(self, index, item):
        """update curve with given point value"""
        if not isinstance(item, Point):
            raise TypeError("input must be a Point")
        self.items[index] = item