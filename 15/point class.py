class Point:

    def __init__(self, x=0, y=0):
        """Create new point at x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def distance_from_origin(self):
        "Compute my distance from the origin"
        return ((self.x **2) + (self.y **2)) ** 0.5

    def distance_from_point(self,target):
        """Compute my distance from the target"""
        dx = self.x - target.x
        dy = self.y - target.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5

    def midpoint(self,target):
        """Finds the midpoint between myself and the target"""
        dx = (self.x + target.x) / 2
        dy = (self.y + target.y) / 2
        p = Point(dx,dy)
        return p

    def reflect_x(self):
        new_y = self.y * -1
        return Point(self.x,new_y)

    def slope_from_origin(self):
        """Finds the slope of the line connecting me with the origin"""
        if self.x == 0:
            return "undefined"
        if self.y == 0:
            return 0
        return (self.y/self.x)

    def get_line_to(self,target):
        dx = self.x - target.x
        dy = self.y - target.y
        if dx == 0:
            return "undefined"
        a = (dy/dx)
        b = self.y - (a* self.x)
        return (a,b)

    def bisect_line(self,target):
        slope = -1/float(self.get_line_to(target)[0])
        midpoint = self.midpoint(target)
        b = midpoint.y - (slope * midpoint.x)
        return (slope,b)

    def find_mid_x(self,target, target2):
        bisect_self = self.bisect_line(target)
        bisect_target = target.bisect_line(target2)
        a = bisect_self[0]
        b = bisect_self[1]
        c = bisect_target[0]
        d = bisect_target[1]
        x = (d-b)/(a-c)
        return x,a,b

    def find_midcircle(self,target,target2):
        points = self.find_mid_x(target,target2)
        x = points[0]
        m = points[1]
        b = points[2]
        y = m*x + b
        return Point(x,y)


p = Point(-3,5)
q = Point(3,3)
r = Point(11,19)

import time
t0=time.clock()
z = p.find_midcircle(q,r)
t1=time.clock()
print(z, t1-t0)














