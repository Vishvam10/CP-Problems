def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


def solve():

    n = inp()
    arr = inlt()
    arr.sort()

    if (n == 1 or n == 2):
        print(0)
        return

    print(min(arr[n-2] - arr[0], arr[n-1] - arr[1]))
    return


solve()
