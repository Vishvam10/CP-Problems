def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


def solve():
    a = inp()
    b = inp()
    c = inp()
    ans = a + b + c
    ans = max(ans, (a + b) * c)
    ans = max(ans, a * (b + c))
    ans = max(ans, a * b * c)

    print(ans)
    return


solve()
