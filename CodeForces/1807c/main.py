def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    n = inp()
    s = insr()

    if n == 1:
        print("YES")
        return

    if n == 2:
        if s[0] == s[1]:
            print("NO")
            return
        else:
            print("YES")
            return

    for i in range(n):
        ch = s[i]
        if ch != "0" and ch != "1":
            s = s.replace(ch, str(i % 2))

    for i in range(1, n, 1):
        if s[i - 1] == s[i]:
            print("NO")
            return

    print("YES")
    return


t = inp()

for _ in range(t):
    solve()
