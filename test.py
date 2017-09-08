from time import sleep
from itertools import count

def gen():
    next = ''
    for i in range(5):
        next = yield next



def sieve(n, last_sieve):
    print(n, end=',')
    for i in last_sieve:
        if i % n != 0:
            yield i


def main(m):
    head = sieve(2, count(2))
    for i in range(m):
        p = next(head)
        head = sieve(p, head)
