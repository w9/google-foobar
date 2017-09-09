from solution import answer
from timeit import default_timer as timer


print('input: 0, 3')
print('expected: 2')
tic = timer()
print('answer: {}'.format(answer(0, 3)))
toc = timer()
print('time: {}'.format(toc - tic))
print('')

print('input: 17, 4')
print('expected: 14')
tic = timer()
print('answer: {}'.format(answer(17, 4)))
toc = timer()
print('time: {}'.format(toc - tic))
print('')

print('input: 2000000000, 1000')
print('expected: 7684864')
tic = timer()
print('answer: {}'.format(answer(2000000000, 1000)))
toc = timer()
print('time: {}'.format(toc - tic))
print('')

print('input: 2000000000, 5000')
print('expected: 4235264')
tic = timer()
print('answer: {}'.format(answer(2000000000, 5000)))
toc = timer()
print('time: {}'.format(toc - tic))
print('')
