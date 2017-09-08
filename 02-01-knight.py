from itertools import chain, count


def id_to_loc(id):
    return (id // 8, id % 8)


def loc_to_id(x, y):
    return x * 8 + y


possible_moves = [
    ( 1,  2),
    (-1,  2),
    ( 1, -2),
    (-1, -2),
    ( 2,  1),
    (-2,  1),
    ( 2, -1),
    (-2, -1),
    ]


def jump(l, d):
    x, y = l
    dx, dy = d
    return (x + dx, y + dy)


def legal(l):
    x, y = l
    return 0 <= x < 8 and 0 <= y < 8


def possible_next(l):
    return [jump(l, d) for d in possible_moves if legal(jump(l, d))]


def answer(src, dist):
    src_loc = id_to_loc(src)
    dist_loc = id_to_loc(dist)

    covered_locs = last_locs = {src_loc}
    for i in count():
        if dist_loc in last_locs:
            return i
        reachable_locs = set(chain.from_iterable([possible_next(l) for l in covered_locs]))
        last_locs = reachable_locs - covered_locs
        covered_locs |= last_locs
