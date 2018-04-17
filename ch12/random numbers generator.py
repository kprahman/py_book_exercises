# import random
#
# def make_random_nubers(num,lower,upper):
#     rng=random.Random()
#     result = []
#     for i in range(num):
#         result.append(random.randrange(lower,upper))
#     return result
#
# print(make_random_nubers(5,0,100))

import random

def make_random_no_duplicates(n,lower,upper):
    """generates random numbers across a domain
    until a new number is found"""

    result = []
    rng = random.Random()
    for i in range(n):
        while True:
            candidate = rng.randrange(lower,upper)
            if candidate not in result:
                break
        result.append(candidate)
    return result

print(make_random_no_duplicates(10,1,6))

from unit_tester import test

