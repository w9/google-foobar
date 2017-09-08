from itertools import starmap, repeat
from operator import mul
from functools import partial


def transition(m, a):
    """
    It's basically a matrix-vector multiplication optimized
    for sparse matrices.
    """
    return [sum(starmap(mul, zip(r, a))) for r in m]


def get_trans_mat(l):
    """
    *Divisible and preceeding in list* is a partial order.
    This function gives the transition matrice of the corresponding DAG,
    with its diagnal removed.
    """
    return [[1 if i < j and l[j] % l[i] == 0 else 0
             for i in range(j)]
            for j in range(len(l))]


def answer(l):
    trans_mat = get_trans_mat(l)
    # print(trans_mat)
    walk = partial(transition, trans_mat)
    one_step = walk(list(repeat(1, len(l))))
    # print(one_step)
    two_step = walk(one_step)
    # print(two_step)
    return sum(two_step)
