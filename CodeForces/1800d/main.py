def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    n = inp()
    s = insr()
    ans = n - 1
    for i in range(1, n - 1, 1):
        if s[i - 1] == s[i + 1]:
            ans -= 1
    print(ans)


t = inp()

for _ in range(t):
    solve()
