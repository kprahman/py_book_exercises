def recursive_min(nxs):
    smallest = None
    first_time = True
    for element in nxs:
        if type(element) == type([]):
            value = recursive_min(element)
        else:
            value = element

        if first_time or value < smallest:
            smallest = value
            first_time = False

    return smallest

def count(target, nxs):
    counter = 0
    for e in nxs:
        if type(e) == type([]):
            counter += count(target, e)
    counter += nxs.count(target)
    return counter

def flatten(nxs):
    flat_list = []
    for e in nxs:
        if type(e) == type([]):
            flat_list.extend(flatten(e))
        else:
            flat_list.append(e)
    return flat_list

def non_recursive_fibonacci(n):
    init = 1
    prev = 0
    for i in range(n-1):
        running_total = init + prev
        prev = init
        init = running_total
    return running_total


from unit_test import timer
timer(non_recursive_fibonacci(200))



