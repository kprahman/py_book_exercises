def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1
print(merge(["a","b","c"],["a","b","d",]))

