def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def solve():
    [a, b, c] = inlt()

    if (a + b == c) or (b + c == a) or (a + c == b):
        print("YES")
    else:
        print("NO")


t = inp()

for _ in range(t):
    solve()
