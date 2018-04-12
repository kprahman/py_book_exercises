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
off= "gray19"

def hideturtles():
    tess.hideturtle()
    rory.hideturtle()
    gerry.hideturtle()
    yang.hideturtle()

def showturtles():
    tess.showturtle()
    gerry.showturtle()
    rory.showturtle()
    yang.showturtle()

def draw_housing():
    """Draws a housing for the traffic lights"""
    tess.speed(900)
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

def init_drawlight(t):
    for i in t:
        i.penup()
        i.shape("circle")
        i.shapesize(3)
        i.fillcolor(off)

def advance_state_machine():
    global state_num
    if state_num == 0: #transition from state 0 to 1
        gerry.fillcolor("green")
        yang.fillcolor(off), rory.fillcolor(off)
        state_num = 1
        wn.ontimer(advance_state_machine,2000)
    elif state_num == 1: #transition from 1 to 2
        yang.fillcolor("yellow")
        gerry.fillcolor(off), rory.fillcolor(off)
        state_num = 2
        wn.ontimer(advance_state_machine, 500)
    else: #2 to 0
        rory.fillcolor("red")
        yang.fillcolor(off), gerry.fillcolor(off)

        state_num = 0
        wn.ontimer(advance_state_machine, 1000)

hideturtles()
draw_housing()
init_drawlight(turtles)
gerry.setposition(40,50)
yang.setposition(40,125)
rory.setposition(40,200)
showturtles()


state_num = 0 #holds tess' current state
advance_state_machine()






wn.mainloop()