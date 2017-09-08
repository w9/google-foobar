from math import sqrt
from itertools import islice, count


def primes_iter():
    primes = []
    for n in count(2):
        if not any([n % x == 0 for x in primes if x <= sqrt(n)]):
            primes.append(n)
            for c in str(n):
                yield c


def answer(n):
    return ''.join(islice(primes_iter(), n, n+5))
