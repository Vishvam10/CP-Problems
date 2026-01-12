def inp():
    return int(input())


def insr():
    return input().strip()


def unique(s):
    return len(set(s))


def solve():
    n = inp()
    s = insr()

    ind = []
    mp = {}
    max_s = -1
    temp = 0
    for i, ch in enumerate(s):
        if ch in mp:
            ind.append(i)
        else:
            mp[ch] = 1

    for i in ind:
        temp = unique(s[:i]) + unique(s[i:])
        max_s = max(max_s, temp)

    print(max_s)


t = inp()

for _ in range(t):
    solve()
