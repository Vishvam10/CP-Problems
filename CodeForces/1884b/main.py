from collections import deque


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


# for arr to be divisible by 2**n, you need to make
# the first (n-1) bits 0. so, for every 1,
# find the nearest 0.


def solve():
    n = inp()
    arr = list(map(int, list(insr())))
    ans = 0

    st = deque()
    for i in range(n):
        if arr[i] == 0:
            # negative because it's from the front
            # and we will be using it from the back
            st.append(-i)

    for i in range(n - 1, -1, -1):
        if len(st) == 0:
            print("-1", end=" ")
        else:
            ind = st.pop()
            ans += i + ind
            print(ans, end=" ")

    print()


t = inp()

for _ in range(t):
    solve()
