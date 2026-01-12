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


############ Input Functions #############
def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


############# Main Function #############


def solve():
    """
    a[i] + 1 < a[i + 1]
    => Write Condition : a[i + 1] - a[i] > 1

    1, 4, 5, 5, 7, 7

    Without dup removal : [1], [4, 5, 5], [7, 7]
    With dup removal    : [1], [4, 5], [7]

    So, dup removal is fine

    1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 10, 12
    => 1, 2, 4, 5, 6, 7, 10, 12
    => x, 1, 2, 1, 1, 1, 3, 2

    1, 2, 2, 4
    => 1, x, 4
    => x, 1, 2

    1, 2, 3, 4, 5, 6
    x, 1, 1, 1, 1, 1, 2, 2, 2, 2

    [1, 2], [4, 5, 6, 7], [10], [12]

    Yoink, common difference 1 elements ?
    Many common diff 1 elements (say = k) then after removals (alternating),
    we can get upto k // 2 gains
    """

    _ = inp()

    arr = inlt()
    n, ones, ans = len(arr), 0, 1

    for i in range(1, n, 1):
        d = arr[i] - arr[i - 1]

        # Skip duplicates. sorted(set(inlt())) throws TLE
        if d == 0:
            continue
        if d == 1:
            ones += 1
        else:
            # Either streak ended and / or we get d != 1
            ans += (ones // 2) + 1
            ones = 0

    # If we reached the end with a 1 diff streak, consider that as well
    if ones:
        ans += ones // 2

    print(ans)
    return


t = inp()

for _ in range(t):
    solve()
