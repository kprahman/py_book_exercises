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

def main():
    import random
    rng = random.Random()

    bd=list(range(8))
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries".format(bd,tries))
            tries = 0
            num_found += 1

main()


