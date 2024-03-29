def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def solve():
    n = inp()
    arr = inlt()
    s = sum(arr)
    if (s % 2 == 0):
        print('YES')
        return
    else:
        print('NO')
        return


t = inp()

for _ in range(t):
    solve()
