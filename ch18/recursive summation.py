def r_sum(nested_list):
    tot = 0
    for element in nested_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

print(r_sum([1,2,[3,4],5]))

def r_max(nxs):
    """Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are EMPTY"""
    largest = None
    for i,e in enumerate(nxs):
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if i == 0 or val > largest:
            largest = val

    return largest

def r_max_book(nxs):
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest


import time
t0 = time.clock()
r_max([2, 9, [1, 13], 8, 6])
t1 = time.clock()
print("That took {} seconds".format(t1-t0))
t0 = time.clock()
r_max_book([2, 9, [1, 13], 8, 6])
t1 = time.clock()
print("That took {} seconds".format(t1-t0))


