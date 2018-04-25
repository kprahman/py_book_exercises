##FUNCTION SET: FIND COLLISIONS
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

##FUNCTION SET: FIND SOLUTION FAMILY
def rotate(bd, times):
    counter = 0
    while counter < times:
        yl = []
        xl = []
        newx = []
        combine = []
        final_list = []
        for (x,y) in enumerate(bd):
            yl.append(y)
            xl.append(x)

        for i in yl:
            newx.append(i)
        xl.reverse()

        for i,v in enumerate(newx):
            pair = [v,xl[i]]
            combine.append(pair)
        combine.sort()

        for i in combine:
            final_list.append(i[1])
        counter += 1
        bd = final_list
    return final_list

def invert_y(bd):
    result = []
    for i in bd:
        new_y = (len(bd)-1) - i
        result.append(new_y)
    return result

def invert_x(bd):
    placeholder = list(bd)
    placeholder.reverse()
    return placeholder

def find_family(bd):
    result = []
    result.append(invert_x(bd))
    for i in range(1,4):
        result.append(rotate(bd, i))
        result.append(rotate(invert_x(bd),i))
    print("Family for solution {0} found: {1}".format(bd, result))
    return result

##FUNCTION SET: COMPILE LIST OF SOLUTIONS
def novel(candidate, list):
    return candidate not in list

def main(size, solutions):
    import random
    rng = random.Random()
    bd = list(range(size)) #this is the only line where the range is specified
    num_found = 0
    tries = 0
    average = 0
    list_of_solutions = []

    while num_found < solutions:
        rng.shuffle(bd) ##generate a new permutation
        also_bd = list(bd)
        tries += 1      ## adds a try
        if not has_clashes(bd) and novel(bd,list_of_solutions):
            list_of_solutions.append(also_bd)
            new_find = find_family(bd)
            for i in new_find:
                list_of_solutions.append(i)
            print("that took {} tries to find!".format(tries))
            average += tries
            num_found += 1
            tries = 0
    print("Each solution took an average of {:.0f} tries to find".format(average/solutions))


import time
t0= time.clock()
main(16, 12)
t1 = time.clock()
print("That whole operation took {} seconds to complete".format(t1-t0))
