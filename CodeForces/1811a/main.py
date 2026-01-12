def inp():
    return int(input())


def insr():
    return input().strip()


def solve():
    [n, d] = input().split()
    s = insr()

    i = 0

    while i < int(n) and s[i] >= d:
        i += 1

    print(s[:i] + str(d) + s[i:])
    return


t = inp()

for _ in range(t):
    solve()
