#change the chess board's size to 4,12,and 16.

def share_diagonal(x0,y0,x1,y1):
    dy = (y1-y0)
    dx = (x0-x1)
    return abs(dx/dy) == 1

def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i,bs[i],c,bs[c]):
            return True
    return False

def has_clashes(the_board):
    for col in range(1, len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False

def invert_y(bd):
    result = []
    for i in bd:
        new_y = (len(bd)-1) - i
        result.append(new_y)
    return result

def invert_x(bd):
    init = list(bd)
    init.reverse()
    return init



def main():
    import random
    rng = random.Random()

    bd = list(range(8)) #this is the only line where the range is specified
    num_found = 0
    tries = 0
    average = 0
    pl_list = []
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd in pl_list:
                continue
            else:
                print("Found solution {0} in {1} tries.".format(bd,tries), end= "\t")
                print("y-inversion at {0}".format(y_inversion), end = "\t")
                print("x-inversion at {0}".format(x_inversion))
                average += tries
                tries = 0
                num_found += 1
                pl_bd = list(bd)
                pl_list.append(pl_bd)
    pl_list.sort()
    print(pl_list)



    print("it took an average of {} tries to find a solution".format(average/10))
import time
t0 = time.clock()
main()
t1 = time.clock()
print("It took {} seconds to finish that operation".format(t1-t0))


