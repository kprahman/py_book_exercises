class Point:
    def __init__(self, x=0, y=0):
        """Create new point at x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """initialize rectangle at posn with width w and height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner,
                                        self.width,
                                        self.height)

    def __contains__(self, item):
        """Tests whether a given point resides within the rectangle"""
        w_range = self.width + self.corner.x
        h_range = self.height + self.corner.y
        in_x = self.corner.x <= item.x < w_range
        in_y = self.corner.y <= item.y < h_range
        return in_x and in_y

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def flip(self):
        """Flips the h and w of a rectangle"""
        import copy
        h = copy.deepcopy(self.height)
        w = copy.deepcopy(self.width)
        self.height = w
        self.width = h
        return self

    def get_verticies(self):
        """Finds the corners of rectangle"""
        a = Point(self.corner.x,
                  self.corner.y + self.height)
        b = self.corner
        c = Point(self.corner.x + self.width,
                  self.corner.y + self.height)
        d = Point(self.corner.x + self.width,
                  self.corner.y)
        return a, b, c, d

    def test_collision(self, target):
        b = target.get_verticies()
        for i in b:
            if i in self:
                return True
        return False


r = Rectangle(Point(0, 0), 10, 5)
s = Rectangle(Point(1, 1), 16, 7)
v = Rectangle(Point(10, 5), 4, 5)
print(r.test_collision(s))
