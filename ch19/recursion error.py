def recursion_depth(number):
    print("Depth | {} ".format(number))
    try:
        recursion_depth(number+1)
    except:
        print("I cannot go deeper into this MESS lEarN HOW To COdE PROPERLY!")

def readposint():
    try:
        ruh_roh = False
        x = int(input("enter a positive integer"))
        if x < 0:
            ruh_roh = True
            raise ruh_roh
        readposint()
    except:
        if ruh_roh:
            print("{} is not a positive integer!".format(x))
        else:
            print("that's not an integer")
        readposint()

readposint()