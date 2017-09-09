from collections import deque

N_WALL_REMOVABLE = 1

possible_moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def move(sq, d):
    x, y = sq
    dx, dy = d
    return (x + dx, y + dy)


def answer(maze):
    w = len(maze)
    h = len(maze[0])

    # The first dimension of `state` is the number of walls removed

    state = [[[True for y in range(h)] for x in range(w)]
             for z in range(N_WALL_REMOVABLE + 1)]

    state[0][0][0] = False

    # Active square queue
    # The four numbers are
    #   - number of walls removed (r)
    #   - coordinates (x, y)
    #   - current path length (l)

    active_sqs = deque([(0, 0, 0, 1)])

    while active_sqs:
        r, fx, fy, l = active_sqs.popleft()

        next_sqs = [move((fx, fy), d) for d in possible_moves]
        legal_sqs = [(x, y) for x, y in next_sqs if 0 <= x < w and 0 <= y < h]

        def try_walk(r, tx, ty, l):
            if state[r][tx][ty]:
                state[r][tx][ty] = False
                active_sqs.append((r, tx, ty, l + 1))

        for tx, ty in legal_sqs:
            if (tx, ty) == (w - 1, h - 1):
                # The end point is reached!
                return l + 1

            if maze[tx][ty] == 0:
                try_walk(r, tx, ty, l)
            else:
                if r < N_WALL_REMOVABLE:
                    # Try break a wall
                    try_walk(r + 1, tx, ty, l)
                else:
                    # Uh-uh, you have removed too many walls
                    pass

    # The end point is unreachable.
    return -1
