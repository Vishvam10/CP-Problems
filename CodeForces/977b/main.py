from collections import defaultdict


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    n = inp()
    arr = insr()
    mp = defaultdict(int)

    ans = ""
    maxi = -1

    for i in range(n):
        substr = arr[i : i + 2]
        if len(substr) == 2:
            mp[substr] += 1
            if mp[substr] >= maxi:
                maxi = mp[substr]
                ans = substr

    print(ans)
    return


solve()
