def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    [n, k] = inlt()
    arr = inlt()

    if list(sorted(arr)) == arr:
        print("YES")
        return

    if k >= 2:
        print("YES")
        return

    print("NO")
    return


t = inp()

for _ in range(t):
    solve()
