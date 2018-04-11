import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
gerry = turtle.Turtle()
rory = turtle.Turtle()
yang = turtle.Turtle()
turtles = [gerry,rory,yang]

def draw_housing():
    """Draws a housing for the traffic lights"""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

def drawlight(t):
    for i in t:
        i.shape("circle")
        i.shapesize(3)

draw_housing()
gerry.setposition(40,50)
yang.setposition(40,125)
rory.setposition(40,200)
drawlight(turtles)





#initialize positions for the stoplights, while hidden. each turtle is 50 units away from one another
#gerry.hideturtle()
#rory.hideturtle()
#yang.hideturtle()




wn.mainloop()