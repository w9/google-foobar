def answer(start, length):
    current = start
    acc = 0
    for i in range(length):
        for j in range(length):
            if j < length - i:
                acc ^= current
            current += 1
    return acc
