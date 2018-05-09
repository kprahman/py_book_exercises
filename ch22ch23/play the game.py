import turtle

class TurtleGTX(turtle.Turtle): ##
    def __init__(self,name="",range=300):
        super().__init__()
        self.name = name
        self.odometer = 0
        self.range = range


    def __str__(self):
        return self.name + " | Odometer: {}".format(self.odometer)

    def forward(self, distance): ## ideally replicated for fd, backward, bk etc.
        x = self.odometer + distance
        broke_dist = 350- self.odometer
        if x > self.range:
            super().forward(broke_dist)
            self.odometer += abs(broke_dist)
            raise ValueError("{} got a flat tire! Fix it!".format(self.name))
        super().forward(distance)
        self.odometer += abs(distance)


    def jump_forward(self,distance):
        self.penup()
        self.forward(distance)
        self.pendown()

    def fix_tire(self):
        self.range = self.range * 2


wn = turtle.Screen()
sonic = TurtleGTX("sonic")
sonic.jump_forward(60)
sonic.forward(300)
sonic.fix_tire()
sonic.forward(300)



