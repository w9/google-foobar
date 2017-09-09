def xor_sum(n):
    """
    0 ^ 1 ^ ... ^ (n - 1)

    Note that xor_sum(0) == 0.
    """
    if n % 4 == 0:
        return 0
    elif n % 4 == 1:
        return (n - 1)
    elif n % 4 == 2:
        return 1
    else:
        return n


def answer(start, length):
    """
    The speed-up trick is:

        k ^ (k+1) ^ ... ^ n   =   (0 ^ 1 ^ ... ^ n) ^ (0 ^ 1 ^ ... ^ (k-1))

    where (0 ^ 1 ^ ... ^ n) can be calculated fast.
    """
    acc = 0
    for i in range(length):
        line_start = start + i * length
        line_end = line_start + (length - i)
        acc ^= xor_sum(line_end) ^ xor_sum(line_start)

    return acc
