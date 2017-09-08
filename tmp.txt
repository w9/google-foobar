from itertools import starmap, repeat
from operator import mul
from functools import partial


def transition(m, a):
    """ i.e., matrix-vector multiplication """
    return [sum(starmap(mul, zip(r, a))) for r in m]


def get_trans_mat(l):
    """ *Divisible and preceeding in list* is a partial order.
    This function gives the transition matrice of the corresponding DAG,
    with its diagnal removed.
    """
    return [[1 if i < j and l[j] % l[i] == 0 else 0
             for j in range(len(l))]
            for i in range(len(l))]


def answer(l):
    trans_mat = get_trans_mat(l)
    walk = partial(transition, trans_mat)
    one_step = walk(list(repeat(1, len(l))))
    two_step = walk(one_step)
    return sum(two_step)
