import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

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

draw_housing()

tess.penup() #Move tess to the green light
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle") #transform tess from turtle to light
tess.shapesize(3)
tess.fillcolor("green")

#traffic lights have 3 states: green, yellow, red.
#these states are numbered 0, 1, 2
#when the machine changes states, we change tess' position and color

state_num = 0 #holds tess' current state

def advance_state_machine():
    global state_num
    if state_num == 0: #transition from state 0 to 1
        tess.forward(70)
        tess.fillcolor("yellow")
        state_num = 1
    elif state_num == 1: #transition from 1 to 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: #2 to 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

wn.onkey(advance_state_machine, "space") #bind event handler

wn.listen()
wn.mainloop()


