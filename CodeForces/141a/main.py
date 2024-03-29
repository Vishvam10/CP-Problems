def inp():
    return (int(input()))


def insr():
    return (input().strip())


def solve():
    a, b, c = insr(), insr(), insr()

    if (len(a) + len(b) != len(c)):
        print('NO')
        return

    x = list(sorted(a + b))
    c = list(sorted(c))
    if (x == c):
        print('YES')
        return
    else:
        print('NO')
        return


solve()
