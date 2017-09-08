from answer_03_01_lucky_triple import answer
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
