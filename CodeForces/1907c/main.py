from collections import defaultdict


def inp():
    return int(input())


def inlt():
    return input().split()


def insr():
    return input().strip()


def check(s):
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            return True
    return False


def solve():
    n = inp()
    s = list(insr())
    mp = defaultdict(int)
    maxi = 0

    for i in range(n):
        mp[s[i]] += 1
        maxi = max(maxi, mp[s[i]])

    # (n - maxi) : no. of removals
    # max(0/1 depending on odd or even, max - (n - maxi)) : no. of letters left

    print(max(n & 1, 2 * maxi - n))

    return


t = inp()

for _ in range(t):
    solve()
