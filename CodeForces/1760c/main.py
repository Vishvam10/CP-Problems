def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


def solve():
    n = inp()
    arr = inlt()
    smax_ = float("-inf")
    max_ = min(arr)

    for i in range(n):
        if (arr[i] > max_):
            smax_ = max_
            max_ = arr[i]
        else:
            smax_ = max(smax_, arr[i])
    for x in arr:
        if (x == max_):
            print(x - smax_, end=" ")
        else:
            print(x - max_, end=" ")
    print()
    return


t = inp()

for _ in range(t):
    solve()
