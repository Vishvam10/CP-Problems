def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


def solve():
    [na, nq] = inlt()
    arr = inlt()
    pre = [0]
    for x in arr:
        pre.append(pre[-1] + x)

    tot = pre[-1]

    for _ in range(nq):
        [l, r, k] = inlt()

        orig_s = pre[r] - pre[l-1]
        obt_s = k * (r - l + 1)
        ans = tot - orig_s + obt_s
        if (ans % 2 == 1):
            print("YES")
        else:
            print("NO")


t = inp()

for _ in range(t):
    solve()
