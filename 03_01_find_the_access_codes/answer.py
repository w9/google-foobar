from itertools import repeat
from functools import partial


def transition(m, a):
    """ Matrix-vector multiplication.
    """
    return [sum([a[i] for i in r]) for r in m]


def get_trans_mat(l):
    """ *Divisible and preceeding in list* is a partial order.
    This function gives the transition matrix of the corresponding DAG,
    in a sparse format.
    """
    return [[i for i in range(j) if i < j and l[j] % l[i] == 0]
            for j in range(len(l))]


def answer(l):
    trans_mat = get_trans_mat(l)
    walk = partial(transition, trans_mat)
    one_step = walk(list(repeat(1, len(l))))
    two_step = walk(one_step)
    return sum(two_step)
