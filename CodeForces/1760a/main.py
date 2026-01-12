def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def solve():
    arr = inlt()
    arr.sort()
    print(arr[1])
    return


t = inp()

for _ in range(t):
    solve()
