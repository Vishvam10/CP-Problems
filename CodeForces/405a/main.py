def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


n = inp()
arr = inlt()
arr.sort()

for x in arr:
    print(x, end=' ')
