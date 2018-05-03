import turtle

tess = turtle.Turtle()
wn = turtle.Screen()
tess.speed(100000000)

def sirpink(t,order,size):

    if order == 0: ##this is the basic shape
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        for i in range(3):
            sirpink(t,order-1,size/2)
            t.forward(size)
            t.left(120)



sirpink(tess,8,1000)
wn.mainloop()