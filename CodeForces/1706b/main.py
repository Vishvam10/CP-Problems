# ?? DOUBT ??


from collections import defaultdict

import sys
input = sys.stdin.readline

############# Util Functions ############


def prime_factors(n):
    c, t = [], n
    for j in range(2, int(n**0.5)+1):
        if t % j == 0:
            c.append(j)
            while t % j == 0:
                t //= j
    if t > 1:
        c.append(t)
    return c


def prime_sieve(n):
    num = [i for i in range(n+1)]
    pr = [True]*(n+1)
    p = 2
    while p < int(n**0.5)+1:
        if pr[p]:
            for i in range(p*p, n+1, p):
                pr[i] = False
                num[i] = p
        p += 1
    return num


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def all_factors(n):
    i = 1
    ans = []
    while i < int(n**0.5) + 1:
        if n % i == 0:
            ans.append(i)
            if n//i != i:
                ans.append(n//i)
        i += 1
    return ans


def sum_all_fac(n):
    ans = 1
    p = 2
    while p < int(n**0.5) + 1:
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        ans *= ((p ** cnt) - 1)//(p-1)
        p += 1
    return ans


def number_of_divisor(n):
    ans = 1
    p = 2
    while p < int(n**0.5) + 1:
        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1
        ans *= (cnt+1)
        p += 1
    if n > 1:
        ans *= 2
    return ans

############ Input Functions ############


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())

############# Main Function #############


def solve():

    n = inp()
    arr = inlt()
    mp = defaultdict(list)

    for i in range(n):
        mp[arr[i]].append(i)

    ans = [0] * (n)

    for x in mp:

        ans[x-1] = 1
        c, s = 0, 0

        for y in range(1, len(mp[x])):

            s += (mp[x][y] - mp[x][y-1])
            print('s, c : ', s, c)

            # why does this cover both left and right cases ?
            if s % 2 == 1:
                c += 1
                s = 0

        ans[x-1] = max(ans[x-1], c + 1)

    print(*ans)

    return


t = inp()

for _ in range(t):
    solve()
