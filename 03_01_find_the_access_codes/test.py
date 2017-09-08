from random import randint
from answer import answer
from timeit import default_timer as timer
from itertools import repeat

print('> answer(range(1,2001))')
tic = timer()
print(answer(range(1, 2001)))
toc = timer()
print(toc - tic)
print('')

print('> answer([2**x for x in range(1,32) for y in range(60)])')
tic = timer()
print(answer([2**x for x in range(32) for y in range(60)]))
toc = timer()
print(toc - tic)
print('')

print('> answer(list(repeat(1, 2000)))')
tic = timer()
print(answer(list(repeat(1, 2000))))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 10) for x in range(2000)]))')
tic = timer()
print(answer(sorted([randint(1, 10) for x in range(2000)])))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 100) for x in range(2000)]))')
tic = timer()
print(answer(sorted([randint(1, 100) for x in range(2000)])))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 999999) for x in range(2000)]))')
tic = timer()
print(answer(sorted([randint(1, 999999) for x in range(2000)])))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 10) for x in range(5000)]))')
tic = timer()
print(answer(sorted([randint(1, 10) for x in range(5000)])))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 100) for x in range(5000)]))')
tic = timer()
print(answer(sorted([randint(1, 100) for x in range(5000)])))
toc = timer()
print(toc - tic)
print('')

print('> answer(sorted([randint(1, 999999) for x in range(5000)]))')
tic = timer()
print(answer(sorted([randint(1, 999999) for x in range(5000)])))
toc = timer()
print(toc - tic)
print('')

