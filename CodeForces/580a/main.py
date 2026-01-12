def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


def solve():
    n = inp()
    arr = inlt()

    ans, c = 0, 1
    prev = arr[0]

    for i in range(1, n):
        if arr[i] < prev:
            ans = max(ans, c)
            c = 1
        else:
            c += 1

        prev = arr[i]

    ans = max(ans, c)

    print(ans)


solve()
