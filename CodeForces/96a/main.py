def inp():
    return (int(input()))


def inlt():
    return input().split()


def insr():
    return (input().strip())


def solve():
    s = insr()
    if ('1111111' in s or '0000000' in s):
        print('YES')
    else:
        print('NO')
    return


solve()
