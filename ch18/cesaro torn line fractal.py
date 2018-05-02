import turtle

tess = turtle.Turtle()
wn = turtle.Screen()

def cesaro(t, order, size, tear):
    """A direct rip-off of Koch. Just played with the angles"""
    angle = (90 -tear)* -1
    other = angle * -2
    angle_list = [angle,other,angle,0]
    if order == 0:
        t.forward(size)
    else:
        for a in angle_list:
           cesaro(t, order-1, size/3, tear)
           t.left(a)

def cesaro_snowflake(t,order, size, tear):
    for i in range(4):
        cesaro(t,order,size, tear)
        t.left(-90)

cesaro_snowflake(tess,4,600, 10)
wn.mainloop()