def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    n, k = inlt()
    s = insr()
    odd = 0
    for i in set(s):
        odd += s.count(i) % 2
    if k + 1 < odd:
        print("NO")
    else:
        print("YES")


t = inp()
for _ in range(t):
    solve()
