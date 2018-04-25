import random

##CREATE LIST OF POSSIBLE GUESSES
def is_prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def build_primes(size):
    prime_list = []
    for i in range(1,size):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

##CREATE LOTTO DRAWS AND TICKETS
def lotto_ticket(size):
    lotto = []
    prime_list = build_primes(size)
    for i in range(0,6):
        rng = random.randrange(0, len(prime_list))
        lotto.append(prime_list[rng])
    return lotto

def lotto_draw(size):
    lotto = []
    for i in range(0,6):
        rng = random.randrange(1,size+1)
        lotto.append(rng)
    return lotto

def lotto_match(xs,ys):
    matches = 0
    reset = list(ys)
    for i in xs:
        if i in reset:
            matches += 1
            reset.remove(i)
    return matches

def lotto_matches(draw, ticket_list):
    match_list = []
    for i in ticket_list:
        match_list.append(lotto_match(i,draw))
    return match_list

def prime_misses(tickets):
    all_of_em = []
    misses = []
    for i in tickets:
        all_of_em.extend(i)
    primes = build_primes(49)
    for i in primes:
        if i not in all_of_em:
            misses.append(i)
    return misses

def auto_draw(tickets, draw_size, threshold):
    tries = 0
    while True:
        draw = (lotto_draw(draw_size))
        draw_primes = []
        for i in draw:
            if is_prime(i):
                draw_primes.append(i)
        match_detector = (lotto_matches(draw, tickets))
        for i in match_detector:
            if i >= threshold:
                tries += 1
                print("It took {0} tries to find draw {1} with at least {2} prime numbers: {3}.".format(tries,draw, threshold, draw_primes))
                return tries
            tries +=1


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

import time
average = 0
t0 = time.clock()
a = int(input("How many matches do I need to win?"))
b = int(input("And how many tests should I run?"))
for i in range(0,20):
    average += auto_draw(my_tickets, 49, a)
average = average / 20
t1= time.clock()
print("It took an average of {0:.0f} attempts to find a draw with at least {1} prime numbers. The whole operation took {2:.2f}s to complete.".format(average,a,t1-t0))

