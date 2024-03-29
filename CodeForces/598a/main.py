def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


def solve():
    n = inp()
    s = n * (n + 1) // 2
    p = 1
    while (p <= n):
        s -= 2 * p  # subtract twice for the 'minus' sign
        p *= 2

    print(s)
    return


t = inp()

for _ in range(t):
    solve()
