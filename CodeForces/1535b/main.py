def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def solve():
    n = inp()
    arr = inlt()
    t1, t2 = [], []
    ans = 0

    for x in arr:
        if x % 2 == 0:
            t1.append(x)
        else:
            t2.append(x)

    arr = t1 + t2

    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], 2 * arr[j]) > 1:
                ans += 1

    print(ans)

    return


t = inp()

for _ in range(t):
    solve()
