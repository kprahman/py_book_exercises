def merge_a(xs, ys):
    """return only those items that are present on both lists"""
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

def merge_b(xs, ys):
    """return only those items that are in the first list, but not the second"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1

def merge_c(xs, ys):
    """return only those items that are present in the second list"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def merge_d(xs, ys):
    """return only those items that are on either list"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend((xs[xi:]))
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def merge_bagdiff(xs, ys):
    """return only those items in the first list
    that are not eliminated by a matching case in
    the second list"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            yi += 1
            xi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1


print(merge_a([0,0,0,8,56,78], [0,0,0,0,41,42]))





