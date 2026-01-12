import sys

input = sys.stdin.readline

############# Util Functions ############


def prime_factors(n):
    c, t = [], n
    for j in range(2, int(n**0.5) + 1):
        if t % j == 0:
            c.append(j)
            while t % j == 0:
                t //= j
    if t > 1:
        c.append(t)
    return c


def prime_sieve(n):
    num = [i for i in range(n + 1)]
    pr = [True] * (n + 1)
    p = 2
    while p < int(n**0.5) + 1:
        if pr[p]:
            for i in range(p * p, n + 1, p):
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
            if n // i != i:
                ans.append(n // i)
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
        ans *= ((p**cnt) - 1) // (p - 1)
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
        ans *= cnt + 1
        p += 1
    if n > 1:
        ans *= 2
    return ans


############ Input Functions ############


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


############# Main Function #############


def solve():
    n = inp()
    s = insr()

    ans = []

    """

    0 0 0 0 0 0 := yes
    0 0 0 0 0 1 := yes
    0 0 0 0 1 0 := yes
    0 0 0 0 1 1 := yes
    0 0 0 1 0 0 := yes
    0 0 0 1 0 1 := yes
    0 0 0 1 1 0 := yes
    0 0 0 1 1 1 := yes

    0 0 1 0 0 1 1 1 0 0 0 1
    1 1 1 0 0 0 1 1 0 0

    Maybe number of 1's in the string based ?
    Just remove all 1s or 0s ... ?

    Then it is a valid subsequence and ... the result will always be a 
    palindrome no matter odd or even as the numbers are the same
    AND the removed part is NON DECREASING as the numbers are the same ..

    """

    for i in range(n):
        if s[i] == "0":
            ans.append(str(i + 1))

    print(len(ans))
    print(" ".join(ans))

    return


t = inp()

for _ in range(t):
    solve()
