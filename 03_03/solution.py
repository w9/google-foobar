# ........   0 -> ........   0
# .......1   1 -> .......1   1
# ......1.   2 -> ......11   3
# ......11   3 -> ........   0

# .....1..   4 -> .....1..   4
# .....1.1   5 -> .......1   1
# .....11.   6 -> .....111   7
# .....111   7 -> ........   0

# ....1...   8 -> ....1...   8
# ....1..1   9 -> .......1   1
# ....1.1.  10 -> ....1.11  11
# ....1.11  11 -> ........   0


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
    current = start
    acc = 0
    for i in range(length):
        line_start = start + i * length
        line_end = line_start + (length - i)
        acc ^= xor_sum(line_end) ^ xor_sum(line_start)

    return acc
