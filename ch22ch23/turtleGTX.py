import turtle

class TurtleGTX(turtle.Turtle): ##
    def __init__(self,name="",range=300):
        super().__init__()
        self.name = name
        self.odometer = 0
        self.range = range


    def __str__(self):
        return self.name + " | Odometer: {}".format(self.odometer)

    def GTXforward(self, distance): ## ideally replicated for fd, backward, bk etc.
        x = self.odometer + distance
        broke_dist = self.range - self.odometer
        if x > self.range:
            super().forward(broke_dist)
            self.odometer += abs(broke_dist)
            raise ValueError("{} got a flat tire! Fix it!".format(self.name))
        super().forward(distance)
        self.odometer += abs(distance)


    def jump_forward(self,distance):
        self.penup()
        self.GTXforward(distance)
        self.pendown()

    def fix_tire(self):
        self.range = self.range * 2



