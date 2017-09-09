def ff(n):
    return '{:08b}'.format(n).replace('0', '.')


def diagram(m):
    acc = 0
    n = 0
    for i in range(m, m + 60):
        if n % 4 == 0:
            print('')
        acc ^= i
        print('{0} {1:3} -> {2} {3:3}'.format(ff(i), i, ff(acc), acc))
        n += 1

# > diagram(0)
#
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

# ....11..  12 -> ....11..  12
# ....11.1  13 -> .......1   1
# ....111.  14 -> ....1111  15
# ....1111  15 -> ........   0

# ...1....  16 -> ...1....  16
# ...1...1  17 -> .......1   1
# ...1..1.  18 -> ...1..11  19
# ...1..11  19 -> ........   0

# ...1.1..  20 -> ...1.1..  20
# ...1.1.1  21 -> .......1   1
# ...1.11.  22 -> ...1.111  23
# ...1.111  23 -> ........   0

# ...11...  24 -> ...11...  24
# ...11..1  25 -> .......1   1
# ...11.1.  26 -> ...11.11  27
# ...11.11  27 -> ........   0

# ...111..  28 -> ...111..  28
# ...111.1  29 -> .......1   1
# ...1111.  30 -> ...11111  31
# ...11111  31 -> ........   0

# ..1.....  32 -> ..1.....  32
# ..1....1  33 -> .......1   1
# ..1...1.  34 -> ..1...11  35
# ..1...11  35 -> ........   0

# ..1..1..  36 -> ..1..1..  36
# ..1..1.1  37 -> .......1   1
# ..1..11.  38 -> ..1..111  39
# ..1..111  39 -> ........   0

# ..1.1...  40 -> ..1.1...  40
# ..1.1..1  41 -> .......1   1
# ..1.1.1.  42 -> ..1.1.11  43
# ..1.1.11  43 -> ........   0

# ..1.11..  44 -> ..1.11..  44
# ..1.11.1  45 -> .......1   1
# ..1.111.  46 -> ..1.1111  47
# ..1.1111  47 -> ........   0

# ..11....  48 -> ..11....  48
# ..11...1  49 -> .......1   1
# ..11..1.  50 -> ..11..11  51
# ..11..11  51 -> ........   0

# ..11.1..  52 -> ..11.1..  52
# ..11.1.1  53 -> .......1   1
# ..11.11.  54 -> ..11.111  55
# ..11.111  55 -> ........   0

# ..111...  56 -> ..111...  56
# ..111..1  57 -> .......1   1
# ..111.1.  58 -> ..111.11  59
# ..111.11  59 -> ........   0
