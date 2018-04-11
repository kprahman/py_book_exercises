import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess is ready to rumble!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
   tess.goto(x, y)
   wn.title("Tess moved to {0},{1}".format(x,y))

wn.onclick(h1)  # Wire up a click on the window.
wn.mainloop()