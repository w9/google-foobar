# In the state map, each of the h * w squares has the state in the form of an
# array -- in this case, an array with length <= 2

# [a, b] -> [x, y] b =>
#     if b == 0:
#         [min(a, x), min(b, y)]
#     if b == 1:
#         [Inf, min(b, y)]

from math import inf
from collections import deque

possible_moves = [
    ( 1,  0),
    (-1,  0),
    ( 0,  1),
    ( 0, -1),
    ]


def move(sq, d):
    x, y = sq
    dx, dy = d
    return (x + dx, y + dy)


def answer(maze):
    w = len(maze)
    h = len(maze[0])

    state   = [[True for i in range(h)] for j in range(w)]
    state_r = [[True for i in range(h)] for j in range(w)]

    state[0][0] = False

    active_sqs = deque([(0, 0, False, 1)])

    while active_sqs:
        print('========== while active_sqs: ==========')
        print('active_sqs =', active_sqs)

        fx, fy, removed, step = active_sqs.popleft()

        print('(fx, fy, removed) =', (fx, fy, removed))

        next_sqs = [move((fx, fy), d) for d in possible_moves]
        legal_sqs = [(x, y) for x, y in next_sqs if 0 <= x < w and 0 <= y < h]

        print('legal_sqs =', legal_sqs)

        for tx, ty in legal_sqs:
            print('-------- for tx, ty in legal_sqs: --------')
            print('(tx, ty) =', (tx, ty))

            if (tx, ty) == (w - 1, h - 1):
                print(state)
                print(state_r)
                return step + 1

            if removed:
                print('------ if removed: ------')
                if maze[tx][ty] == 0:
                    print('---- if maze[tx][ty] == 0: ----')
                    print('state_r[tx][ty] =', state_r[tx][ty])
                    print('state_r[fx][fy] =', state_r[fx][fy])
                    if state_r[tx][ty]:
                        state_r[tx][ty] = False
                        active_sqs.append((tx, ty, True, step + 1))
                else:
                    print('---- if not maze[tx][ty] == 0: ----')
                    # Uh-uh, you can't remove two walls
                    pass
            else:
                print('------ if not removed: ------')
                if maze[tx][ty] == 0:
                    print('---- if maze[tx][ty] == 0: ----')
                    print('state[tx][ty] =', state[tx][ty])
                    print('state[fx][fy] =', state[fx][fy])
                    if state[tx][ty]:
                        state[tx][ty] = False
                        active_sqs.append((tx, ty, False, step + 1))
                else:
                    print('---- if not maze[tx][ty] == 0: ----')
                    print('state[tx][ty] =', state[tx][ty])
                    print('state[fx][fy] =', state[fx][fy])
                    if state_r[tx][ty]:
                        state_r[tx][ty] = False
                        active_sqs.append((tx, ty, True, step + 1))
