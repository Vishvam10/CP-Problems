def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    [a, b, c] = inlt()
    if a + b == c:
        print("+")
        return
    elif a - b == c:
        print("-")
        return


t = inp()

for _ in range(t):
    solve()
