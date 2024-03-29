def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def solve():
    n = inp()
    arr = inlt()
    s = 0
    c = 0
    arr.sort()
    while s <= sum(arr):
        s += arr.pop()
        c += 1
    print(c)

    return


solve()
