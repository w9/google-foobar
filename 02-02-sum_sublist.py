def answer(l, t):
    for i in range(len(l)):
        acc = 0
        for j in range(i, len(l)):
            acc += l[j]
            if acc == t:
                return [i, j]
            elif acc > t:
                break
    return [-1, -1]
