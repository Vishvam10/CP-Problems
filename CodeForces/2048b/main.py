def inp():
    return int(input())


def inlt():
    return list(map(int, (input().split())))


def solve():
    n, k = inlt()

    if k == 1:
        arr = [i for i in range(1, n)]
        print(arr)
        return

    # For element, I have (k - 1) coverage towards left and right.
    # So, skip (k - 1) at beginning, then put 1, then skip (k - 1) positions
    # after it and put 2 and so on, the intermediate elements can be anything

    arr = [-1] * n
    i, num = 0, 0

    for i in range(0, n, k - 1):
        arr[i] = num
        num += 1

    num += 1

    # Now, I have numbers from range (num + 1) to n
    for i in range(n):
        if arr[i] == -1:
            arr[i] = num
            num += 1

    print(arr)

    return


t = inp()

for _ in range(t):
    solve()
