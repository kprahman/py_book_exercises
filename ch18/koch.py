import turtle

tess = turtle.Turtle()
wn = turtle.Screen()

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)


def koch_snowflake(t,order, size):
    for i in range(3):
        koch(t,order,size)
        t.left(-120)

koch(tess,2,200)
wn.mainloop()